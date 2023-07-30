Authentication
##############

Mautic supports OAuth2 or Basic Authentication for API authentication.

Basic authentication
********************

To get started quickly with Mautic's API, you can use Basic Authentication.

.. note::

    Mautic recommends OAuth2 for security reasons. If you still want to use Basic Authentication, you must first enable it in ``Configuration -> API Settings`` in the Mautic UI, or by setting ``'api_enable_basic_auth' => true`` in ``app/config/local.php`` directly.

After enabling Basic Authentication, you can use it in Mautic's API as follows:

Using Mautic's API library
==========================

TODO

Plain http requests
===================

1. Combine the username and password of a Mautic user with a colon ``:``. For example, ``user:password``.
2. Base64 encode this value. For example, with ``echo -n 'user:password' | base64``. This outputs something like ``dXNlcjpwYXNzd29yZA==``.
3. Add an Authorization header to each API request as ``Authorization: Basic dXNlcjpwYXNzd29yZA==``

Here's an example:

.. code-block:: console

  curl -H "Authorization: Basic dXNlcjpwYXNzd29yZA==" https://mautic.example.com/api/contacts

OAuth2
******

After enabling Mautic's API, the "API Credentials" menu item shows up in the administrator menu. You can create Client ID and Secret there, which you can then use in the next steps.

.. note:: 

    Mautic supports the ``authorization_code``, ``refresh_token`` and ``client_credentials`` grant types.

There are two main flows that Mautic supports:

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - Authorization code flow
     - This flow is best if you want Users to log in with their own Mautic accounts. All actions taken will then be registered as if the user performed them in Mautic's UI.
   * - Client Credentials flow
     - This flow is best for Machine-to-Machine, M2M, communications. For example, in cron jobs or other automations where no humans are involved. All actions taken will be registered as XXXXXX.
 

Authorization code flow 
========================

Using Mautic's API library
--------------------------

Mautic's API library has built-in support for the OAuth2 Authorization Code flow. You can use it as follows:

.. code-block:: php

   <?php
   use Mautic\Auth\ApiAuth;

   // $initAuth->newAuth() will accept an array of OAuth settings
   $settings = array(
       'baseUrl'      => 'https://example.mautic.com',
       'version'      => 'OAuth2',
       'clientKey'    => '5ad6fa7asfs8fa7sdfa6sfas5fas6asdf8', // A Client Key can be created in Mautic's UI through the "API Credentials" menu item
       'clientSecret' => 'adf8asf7sf54asf3as4f5sf6asfasf97dd', // A Client Secret can be created in Mautic's UI through the "API Credentials" menu item
       'callback'     => 'https://your-callback.com'
   );

   // Initiate the auth object
   $initAuth = new ApiAuth();
   $auth     = $initAuth->newAuth($settings);

   // Initiate process for obtaining an access token; this will redirect the user to the authorize endpoint and/or set the tokens when the user is redirected back after granting authorization

   if ($auth->validateAccessToken()) {
       if ($auth->accessTokenUpdated()) {
           $accessTokenData = $auth->getAccessTokenData();

           //store access token data however you want
       }
   }

Using plain OAuth2
------------------

.. note::

   The OAuth processes can be tricky. If possible, it's best to use an OAuth library for the language being used. If you're using PHP, Mautic recommends using the :xref:`Mautic API Library`.

Step one - obtain authorization code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Redirect the user to the authorize endpoint ``/oauth/v2/authorize``:

.. code-block:: console

    GET /oauth/v2/authorize?
       client_id=CLIENT_ID
       &grant_type=authorization_code
       &redirect_uri=https%3A%2F%2Fyour-redirect-uri.com%2Fcallback
       &response_type=code
       &state=UNIQUE_STATE_STRING
    
    (note that the query has been wrapped for legibility)

.. note:: 

    The state is optional but recommended to prevent CSRF attacks. It should be a uniquely generated string and stored locally in session, cookie, etc. to be compared with the returned value.

.. note:: 

    Note that the redirect_uri should be URL encoded.

The user will be prompted to login. Once they do, Mautic will redirect back to the URL specified in redirect_uri with a code appended to the query.

It may look something like: `https://your-redirect-uri.com?code=UNIQUE_CODE_STRING&state=UNIQUE_STATE_STRING`

The state returned should be compared against the original to ensure nothing has been tampered with. 

Step two - replace with an access token
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Obtain the value of the code from Step One then immediately POST it back to the access token endpoint `oauth/v2/token` with:

.. code-block:: console

  POST /oauth/v2/token
    ?client_id=CLIENT_ID
    &client_secret=CLIENT_SECRET
    &grant_type=authorization_code
    &redirect_uri=https%3A%2F%2Fyour-redirect-uri.com%2Fcallback
    &code=UNIQUE_CODE_STRING

    (note that the post body has been wrapped for legibility)

The response returned should be a JSON encoded string:

.. code-block:: json

    {
        "access_token": "ACCESS_TOKEN",
        "expires_in": 3600,
        "token_type": "bearer",
        "scope": "",
        "refresh_token": "REFRESH_TOKEN"
    }

Please store this data in a secure location and use it to authenticate API requests.

Refreshing tokens
^^^^^^^^^^^^^^^^^

The response's ``expires_in`` is the number of seconds the access token is good for and may differ based on what is configured in Mautic. The code handling the authorization process should generate an expiration timestamp based on that value. For example ``<?php $expiration = time() + $response['expires_in']; ?>``. If the access token has expired, the refresh_token should be used to obtain a new access token.

By default, the refresh token is valid for 14 days.


* If your application requests a new access token using the refresh token within 14 days, no user interaction is needed. Your application gets both a new access token and a new refresh token (which is valid for another 14 days after it's issued);
* If your application does not request a new token using the refresh token within 14 days, user interaction is required in order to get new tokens.

The refresh token's expiration time is configurable through Mautic's Configuration. 

.. note:: 
    The application should monitor for a ``400 Bad Request`` response when requesting a new access token and redirect the user back through the authorization process.


To obtain a new access token, a POST should be made to the access token's endpoint ``oauth/v2/token`` using the ``refresh_token`` grant type.

.. code-block:: console

    POST /oauth/v2/token
       ?client_id=CLIENT_ID
       &client_secret=CLIENT_SECRET
       &grant_type=refresh_token
       &refresh_token=REFRESH_TOKEN
       &redirect_uri=https%3A%2F%2Fyour-redirect-uri.com%2Fcallback

    (note that the post body has been wrapped for legibility)

The response returned should be a JSON encoded string:

.. code-block:: json

    {
        "access_token": "NEW_ACCESS_TOKEN",
        "expires_in": 3600,
        "token_type": "bearer",
        "scope": "",
        "refresh_token": "REFRESH_TOKEN"
    }

Client credentials flow
=======================

Using Mautic's API library
--------------------------

Mautic's API library has built-in support for the OAuth2 Client Credentials flow. You can use it as follows:

.. code-block:: php

   <?php
   use Mautic\Auth\ApiAuth;

   // $initAuth->newAuth() will accept an array of OAuth settings
   $settings = array(
       'baseUrl'      => 'https://example.mautic.com',
       'version'      => 'OAuth2',
       'clientKey'    => '5ad6fa7asfs8fa7sdfa6sfas5fas6asdf8', // A Client Key can be created in Mautic's UI through the "API Credentials" menu item
       'clientSecret' => 'adf8asf7sf54asf3as4f5sf6asfasf97dd', // A Client Secret can be created in Mautic's UI through the "API Credentials" menu item
       'callback'     => 'https://your-callback.com'
   );

   // Initiate the auth object
   $initAuth = new ApiAuth();
   $auth     = $initAuth->newAuth($settings);

   // Initiate process for obtaining an access token; this will redirect the user to the authorize endpoint and/or set the tokens when the user is redirected back after granting authorization

   if ($auth->validateAccessToken()) {
       if ($auth->accessTokenUpdated()) {
           $accessTokenData = $auth->getAccessTokenData();

           //store access token data however you want
       }
   }

Using plain OAuth2
------------------

To obtain a new access token, a POST should be made to the access token's endpoint ``oauth/v2/token`` using the ``client_credentials`` grant type.

.. code-block:: console

    POST /oauth/v2/token
      ?client_id=CLIENT_ID
      &client_secret=CLIENT_SECRET
      &grant_type=client_credentials

    (note that the post body has been wrapped for legibility)

The response returned should be a JSON encoded string:

.. code-block:: json

    {
        "access_token": "NEW_ACCESS_TOKEN",
        "expires_in": 3600,
        "token_type": "bearer",
        "scope": ""
    }

Authenticating the API Request
==============================

Authenticating the API request with OAuth2 is easy. Choose one of the following methods that is appropriate for the application's needs.

Authorization Header
--------------------

By using an authorization header, any request method can be authenticated.

However, note that this method requires that the server Mautic is installed on passes headers to PHP or has access to the ``apache_request_headers()`` function. ``apache_request_headers()`` is not available to PHP running under fcgi. 

.. code-block:: console

    Authorization: Bearer ACCESS_TOKEN

Other methods
-------------

You can also append the access token to the query or include it the POST body.

.. code-block:: console
    
    GET https://your-mautic.com/api/leads?access_token=ACCESS_TOKEN

.. code-block:: console
    
    POST https://your-mautic.com/api/leads/new

    firstname=John&lastname=Smith&access_token=ACCESS_TOKEN
