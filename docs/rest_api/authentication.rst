.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Authentication
##############

Mautic supports OAuth2 or Basic Authentication for API authentication.

Basic authentication
********************

To get started quickly with Mautic's API, you can use Basic Authentication.

.. note::

   Mautic recommends OAuth2 for security reasons. If you still want to use Basic Authentication, you must first turn it on in ``Configuration -> API Settings`` in the Mautic UI, or by setting ``'api_enable_basic_auth' => true`` in ``config/local.php`` directly.

After enabling Basic Authentication, you can use it in Mautic's API.

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

#. Combine the username and password of a Mautic User with a colon ``:``. For example, ``user:password``.

#. Base64 encode the value. For example, ``echo -n 'user:password' | base64`` results in ``dXNlcjpwYXNzd29yZA==``. The output varies based on the specific credentials used.

#. Add an Authorization header to each API request as ``Authorization: Basic dXNlcjpwYXNzd29yZA==``. Here's an example:

   .. code-block:: bash

      curl -H "Authorization: Basic dXNlcjpwYXNzd29yZA==" https://mautic.example.com/api/contacts

OAuth2
******

After turning on Mautic's API, the **API Credentials** menu item shows up in the administrator menu. Create a Client ID and Secret there, and use them in the next steps.

.. note:: 

   Mautic supports the ``authorization_code``, ``refresh_token`` and ``client_credentials`` grant types.

There are two main flows that Mautic supports:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Name
     - Description
   * - Authorization code flow
     - This flow is best if you want Users to log in with their own Mautic accounts. All actions taken get registered as if the User performed them in Mautic's UI.
   * - Client Credentials flow
     - This flow is best for Machine-to-Machine - M2M - communications. For example, in Cron jobs that run at fixed times of day.
       
       All actions get registered under the name that you provided in **Settings > API Credentials**.
       So if you called your API Credential ``Mautibot test``, Contacts created through the API show up as ``Contact was identified by Mautibot test [1]``, where ``[1]`` is the ID of the API Credential.
 
Authorization Code flow 
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

.. tip::

   OAuth processes can be complex. It's best to use an OAuth library for the language that you use. For PHP, Mautic recommends using the :xref:`Mautic API Library`.

.. _step one:

Step one - obtain authorization code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Redirect the User to the authorize endpoint ``/oauth/v2/authorize``:

.. code-block:: bash

    # Navigate to this URL in the browser, as it renders the login form
    https://mautic.example.com/oauth/v2/authorize?grant_type=authorization_code
        &client_id=CLIENT_ID
        &redirect_uri=https%3A%2F%2Fexample.com%2Fyour-callback
        &response_type=code
        &state=UNIQUE_STATE_STRING

.. note:: 

   * Line breaks in the example help distinguish the different parts of the query.
   * The state is optional but recommended to prevent ``CSRF`` attacks. It should be a uniquely generated string and stored locally in a session, cookie, etc., so you can compare it with the returned value.
   * The ``redirect_uri`` should be URL encoded.

This prompts the User to log in. Once they do, Mautic redirects them back to the URL specified in the ``redirect_uri`` with a code appended to the query.

It may look something like: ``https://example.com/your-callback?code=UNIQUE_CODE_STRING&state=UNIQUE_STATE_STRING``.

You should compare the returned ``state`` against the original to ensure the request wasn't tampered with. 

Step two - replace with an access token
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Obtain the value of the code from :ref:`step one <step one>`, then immediately ``POST`` it back to the access token endpoint ``oauth/v2/token``.

.. code-block:: bash

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

Please store this data securely and use it to authenticate API requests.

Refreshing tokens
~~~~~~~~~~~~~~~~~

The response's ``expires_in`` field is the number of seconds the access token is valid for and may differ depending on what you configured in Mautic. The code handling the authorization process should generate an expiration timestamp based on that value. For example, ``<?php $expiration = time() + $response['expires_in']; ?>``. If the access token has expired, you can use the ``refresh_token`` to obtain a new access token.

By default, the refresh token is valid for 14 days unless configured otherwise in Mautic.

* If your app requests a new access token using the refresh token within 14 days, there's no need for any User interaction. Your app receives a new access token and a new refresh token, both of which remain valid for another 14 days from the date of issuance.
* If your app doesn't request a new token using the refresh token within 14 days, you need to start from :ref:`step one <step one>` again and redirect the User to Mautic's login.

The refresh token's expiration time is configurable through Mautic's Configuration. 

.. note::

   The app should monitor for a ``400 Bad Request`` response when requesting a new access token and redirect the User back through the authorization process if that happens.

To obtain a new access token, you should do a ``POST`` call to the access token's endpoint ``oauth/v2/token`` using the ``refresh_token`` grant type.

.. code-block:: bash

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

   Mautic's API library doesn't support this flow yet, but there's an open PR that adds support. See :xref:`Client Credentials Support`.

.. vale off

Using plain OAuth2 for the Client Credentials flow
--------------------------------------------------

.. vale on

To obtain a new access token, make a ``POST`` request to the access token's endpoint ``oauth/v2/token`` using the ``client_credentials`` grant type.

.. code-block:: bash

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

Authenticating the API request
==============================

Authenticating API requests with OAuth2 is straightforward. Choose one of the following methods that fits the app's needs.

Authorization header
--------------------

The Authorization header enables authentication for all Mautic API endpoints.

However, this method requires the Mautic server to pass headers to PHP or provide access to the ``apache_request_headers()`` function. Note that ``apache_request_headers()`` is unavailable when running PHP under FastCGI.

.. code-block:: bash

    Authorization: Bearer ACCESS_TOKEN

Other methods
-------------

You can also append the access token to the query or include it in the ``POST`` body, but only when using ``x-www-form-unencoded``.

.. code-block:: bash
    
    GET https://mautic.example.com/api/leads?access_token=ACCESS_TOKEN

.. code-block:: bash

    curl -X POST \
         -H "Content-Type: application/x-www-form-urlencoded" \
         -d "firstname=John&lastname=Smith&access_token=ACCESS_TOKEN" \
         https://mautic.example.com.com/api/leads/new