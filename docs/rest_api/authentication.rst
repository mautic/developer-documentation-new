Authentication
##############

Mautic supports OAuth2 or Basic Authentication for API authentication.

Basic authentication
********************

To get started quickly with Mautic's API, you can use Basic Authentication.

.. note::

    Mautic recommends OAuth2 for security reasons. If you still want to use Basic Authentication, you must first enable it in ``Configuration -> API Settings`` in the Mautic UI, or by setting ``'api_enable_basic_auth' => true`` in ``app/config/local.php`` directly.

After enabling Basic Authentication, you can use it in Mautic's API as follows:

Using Mautic's API library with ``BasicAuth``
=============================================

.. code-block:: php

   <?php
   
   use GuzzleHttp\Client;
   use Mautic\Auth\ApiAuth;
   use Mautic\MauticApi;

   // Initiate an HTTP Client
   $httpClient = new Client([
       'timeout'  => 10,
   ]);

   // Initiate the auth object
   $settings = [
       'userName' => 'YOUR_USERNAME',
       'password' => 'YOUR_PASSWORD'
   ];
   $apiUrl = 'https://mautic.example.com';

   $initAuth = new ApiAuth($httpClient);
   $auth     = $initAuth->newAuth($settings, 'BasicAuth');

   $api         = new MauticApi();
   $contactsApi = $api->newApi('contacts', $auth, $apiUrl);
   $contacts    = $contactsApi->getList();

.. vale off

Plain HTTP requests
===================

.. vale on

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
     - This flow is best if you want Users to log in with their own Mautic accounts. All actions taken get registered as if the User performed them in Mautic's UI.
   * - Client Credentials flow
     - This flow is best for Machine-to-Machine, M2M, communications. For example, in cron jobs that run on at fixed times of the day.
       All actions get registered under the name that you provided in ``Settings > API Credentials``.
       So if you called your API Credential ``Mautibot test``, Contacts created through the API show up as ``Contact was identified by Mautibot test [1]``, where ``[1]`` is the ID of the API Credential.
 

Authorization code flow 
========================

Using Mautic's API library for the Authorization Code flow
----------------------------------------------------------

Mautic's API library has built-in support for the OAuth2 Authorization Code flow. You can use it as follows:

.. code-block:: php

   <?php

   use Mautic\Auth\ApiAuth;

   // This is needed for the API library to store the OAuth2 state in the $_SESSION
   session_start();

   // $initAuth->newAuth() will accept an array of OAuth settings
   $settings = array(
       'baseUrl'      => 'https://mautic.example.com',
       'version'      => 'OAuth2',
       'clientKey'    => '5ad6fa7asfs8fa7sdfa6sfas5fas6asdf8', // A Client Key can be created in Mautic's UI through the "API Credentials" menu item
       'clientSecret' => 'adf8asf7sf54asf3as4f5sf6asfasf97dd', // A Client Secret can be created in Mautic's UI through the "API Credentials" menu item
       'callback'     => 'https://example.com/your-callback'
   );

   // Initiate the auth object
   $initAuth = new ApiAuth();
   $auth     = $initAuth->newAuth($settings, 'OAuth');

   // Initiate process for obtaining an access token; this method will redirect the user to the authorize endpoint and/or set the tokens when the user is redirected back after granting authorization
   if ($auth->validateAccessToken()) {
       if ($auth->accessTokenUpdated()) {
           $accessTokenData = $auth->getAccessTokenData();

           // store the access token data however you want
       }
   }

Using plain OAuth2 for the Authorization Code flow
--------------------------------------------------

.. note::

   The OAuth processes can be tricky. If possible, it's best to use an OAuth library for the language that's used. If you're using PHP, Mautic recommends using the :xref:`Mautic API Library`.

Step one - obtain authorization code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Redirect the User to the authorize endpoint ``/oauth/v2/authorize``:

.. code-block:: console

    # NOTE: navigate to this URL in the browser as it renders the login form
    https://mautic.example.com/oauth/v2/authorize?grant_type=authorization_code
        &client_id=CLIENT_ID
        &redirect_uri=https%3A%2F%2Fexample.com%2Fyour-callback
        &response_type=code
        &state=UNIQUE_STATE_STRING
    
    (note that the query has been wrapped for legibility)

.. note:: 

    The state is optional but recommended to prevent ``CSRF`` attacks. It should be a uniquely generated string and stored locally in a session, cookie, etc. so you can compare it with the returned value.

.. note:: 

    Note that the ``redirect_uri`` should be URL encoded.

This prompts the User to login. Once they do, Mautic redirects them back to the URL specified in the ``redirect_uri`` with a code appended to the query.

It may look something like: ``https://example.com/your-callback?code=UNIQUE_CODE_STRING&state=UNIQUE_STATE_STRING``

You should compare the returned ``state`` against the original to ensure the request wasn't tampered with. 

Step two - replace with an access token
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Obtain the value of the code from Step One, then immediately POST it back to the access token endpoint ``oauth/v2/token`` like so:

.. code-block:: console

    curl -X POST \
         -H "Content-Type: application/x-www-form-urlencoded" \
         -d "grant_type=authorization_code&client_id=CLIENT_ID&redirect_uri=https%3A%2F%2Fexample.com%2Fyour-callback&client_secret=CLIENT_SECRET&code=UNIQUE_CODE_STRING" \
         https://mautic.example.com/oauth/v2/token

The response returned is a JSON encoded string:

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

The response's ``expires_in`` is the number of seconds the access token is good for and may differ based on what you configured in Mautic. The code handling the authorization process should generate an expiration timestamp based on that value. For example ``<?php $expiration = time() + $response['expires_in']; ?>``. If the access token has expired, the ``refresh_token`` should be used to obtain a new access token.

By default, the refresh token is valid for 14 days unless configured otherwise in Mautic.

* If your app requests a new access token using the refresh token within 14 days, there's no need for any User interaction. Your app gets both a new access token and a new refresh token, which is valid for another 14 days after it's issued;
* If your app doesn't request a new token using the refresh token within 14 days, you'll need to start from Step One again and redirect the User to Mautic's login.

The refresh token's expiration time is configurable through Mautic's Configuration. 

.. note::
    The app should monitor for a ``400 Bad Request`` response when requesting a new access token and redirect the User back through the authorization process if that happens.

To obtain a new access token, you should do a POST call to the access token's endpoint ``oauth/v2/token`` using the ``refresh_token`` grant type, like so:

.. code-block:: console

    curl -X POST \
         -H "Content-Type: application/x-www-form-urlencoded" \
         -d "grant_type=refresh_token&client_id=CLIENT_ID&client_secret=CLIENT_SECRET&refresh_token=REFRESH_TOKEN" \
         https://mautic.example.com/oauth/v2/token

The response returned should be a JSON encoded string:

.. code-block:: json

    {
        "access_token": "NEW_ACCESS_TOKEN",
        "expires_in": 3600,
        "token_type": "bearer",
        "scope": "",
        "refresh_token": "REFRESH_TOKEN"
    }

.. vale off

Client Credentials flow
=======================

Using Mautic's API library for the Client Credentials flow
----------------------------------------------------------

.. vale on

.. warning:: 

    Mautic's API library doesn't have support yet for this flow, but there's an open PR that adds support: https://github.com/mautic/api-library/pull/269

.. vale off

Using plain OAuth2 for the Client Credentials flow
--------------------------------------------------

.. vale on

To obtain a new access token, make a POST request to the access token's endpoint ``oauth/v2/token`` using the ``client_credentials`` grant type.

.. code-block:: console

    curl -X POST \
         -H "Content-Type: application/x-www-form-urlencoded" \
         -d "grant_type=client_credentials&client_id=CLIENT_ID&client_secret=CLIENT_SECRET" \
         https://mautic.example.com/oauth/v2/token

The response returned should be a JSON encoded string:

.. code-block:: json

    {
        "access_token": "NEW_ACCESS_TOKEN",
        "expires_in": 3600,
        "token_type": "bearer",
        "scope": ""
    }

.. vale off

Authenticating the API Request
==============================

.. vale on

Authenticating the API request with OAuth2 is easy. Choose one of the following methods that's appropriate for the app's needs.

Authorization header
--------------------

By using an authorization header, you can authenticate against all of Mautic's API endpoints.

However, note that this method requires that your Mautic server can pass headers to PHP or has access to the ``apache_request_headers()`` function. ``apache_request_headers()`` isn't available to PHP running under FastCGI. 

.. code-block:: console

    Authorization: Bearer ACCESS_TOKEN

Other methods
-------------

You can also append the access token to the query or include it the POST body, but only when using ``x-www-form-unencoded``.

.. code-block:: console
    
    GET https://mautic.example.com/api/leads?access_token=ACCESS_TOKEN

.. code-block:: console

    curl -X POST \
         -H "Content-Type: application/x-www-form-urlencoded" \
         -d "firstname=John&lastname=Smith&access_token=ACCESS_TOKEN" \
         https://mautic.example.com.com/api/leads/new
