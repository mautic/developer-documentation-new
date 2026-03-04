Authentication
##############

Mautic supports OAuth2 or Basic Authentication for API authentication.

Basic authentication
********************

To get started quickly with Mautic's API, you can use Basic Authentication.

.. note::

   Mautic recommends OAuth2 for security reasons. If you still want to use Basic Authentication, you must first turn it on in ``Configuration -> API Settings`` in the Mautic UI, or by setting ``'api_enable_basic_auth' => true`` in ``config/local.php`` directly.

After enabling Basic Authentication, you can use it in Mautic's API.

Using the Mautic API library
============================

Read the :xref:`using basic auth` to interact with Mautic's API.
   
.. vale off

HTTP requests
-------------

.. vale on

#. Combine the username and password of a Mautic User with ``:`` - a colon. For example, ``user:password``.

#. Base64 encode the value. For example, ``echo -n 'user:password' | base64`` results in ``dXNlcjpwYXNzd29yZA==``. The output varies based on the specific credentials used.

#. Add an ``Authorization`` header to each API request. Here's an example:

   .. code-block:: bash

      curl -H "Authorization: Basic dXNlcjpwYXNzd29yZA==" https://mautic.example.com/api/contacts

OAuth2
******

After turning on Mautic's API, the **API Credentials** menu item shows up in the administrator menu. Create a **Client ID** and **Secret**, and use them in the next steps.

.. note:: 

   Mautic supports the ``authorization_code``, ``refresh_token`` and ``client_credentials`` grant types.

There are two main flows that Mautic supports:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Name
     - Description
   * - Authorization Code flow
     - This flow is best if you want Users to log in with their own Mautic accounts. All actions taken get registered as if the User performed them in Mautic's UI.
   * - Client Credentials flow
     - This flow suits Machine-to-Machine - M2M - communications such as Cron jobs.
     
       Mautic registers all actions under the name provided in **Settings > API Credentials**. For example, a credential named ``Mautibot test`` identifies Contacts created through the API as ``Contact was identified by Mautibot test [1]`` where ``[1]`` represents the credential ID.
 
Authorization Code flow
=======================

Using the Mautic API library for Authorization Code flow
--------------------------------------------------------

Read the :xref:`Obtaining an access token` to interact with Mautic's API.

Using the standard OAuth2 for Authorization Code flow
-----------------------------------------------------

.. tip::

   OAuth processes can be complex. Use an OAuth library for your language. For PHP, Mautic recommends the :xref:`Mautic API Library`.

.. _step one:

Step one - obtain Authorization Code
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
   * The state is optional but recommended to prevent ``CSRF`` attacks. It should be a uniquely generated string and stored locally in a session, cookie, and so on, so you can compare it with the returned value.
   * The ``redirect_uri`` should be URL encoded.

The URL prompts the User to log in. After the User logs in, Mautic redirects the browser to the URL defined in the ``redirect_uri``. The redirected URL follows this structure:

``https://example.com/your-callback?code=UNIQUE_CODE_STRING&state=UNIQUE_STATE_STRING``

To ensure the request remains secure, compare the returned ``state`` value against the original value stored in the session.

Step two - exchange authorization code for access token
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Obtain the authorization code value from the ``code`` parameter in the redirect URL from :ref:`step one <step one>`. Immediately ``POST`` this value to the token endpoint ``oauth/v2/token``.

.. code-block:: bash

    curl -X POST \
         -H "Content-Type: application/x-www-form-urlencoded" \
         -d "grant_type=authorization_code&client_id=CLIENT_ID&redirect_uri=https%3A%2F%2Fexample.com%2Fyour-callback&client_secret=CLIENT_SECRET&code=UNIQUE_CODE_STRING" \
         https://mautic.example.com/oauth/v2/token

Access token response
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: json

    {
        "access_token": "ACCESS_TOKEN",
        "expires_in": 3600,
        "token_type": "bearer",
        "scope": "",
        "refresh_token": "REFRESH_TOKEN"
    }

.. note::

   Store this data securely and use it to authenticate future API requests.

Refreshing tokens
~~~~~~~~~~~~~~~~~

The ``expires_in`` field indicates the number of seconds the access token remains valid. The code handling the authorization process should use this value to generate an expiration timestamp, for example, ``<?php $expiration = time() + $response['expires_in']; ?>``. When the access token expires, use the ``refresh_token`` value to obtain a new one.

By default, the refresh token remains valid for 14 days. Configure this duration in Mautic under **Configuration > API Settings**.

.. note::

   * When the app requests a new access token within the 14-day validity period, Mautic automatically issues a new access token and a new refresh token. Both tokens remain valid for another 14 days from the date of issuance.
   * If the app doesn't request a new token before the refresh token expires, restart the process from :ref:`step one <step one>` and redirect the User to the Mautic login.
   * The app must monitor for a ``400 Bad Request`` response when requesting a new access token. If this occurs, it should redirect the User through the authorization process again.

To obtain a new access token, send a ``POST`` request to the token endpoint ``oauth/v2/token`` using the ``refresh_token`` grant type.

.. code-block:: bash

    curl -X POST \
         -H "Content-Type: application/x-www-form-urlencoded" \
         -d "grant_type=refresh_token&client_id=CLIENT_ID&client_secret=CLIENT_SECRET&refresh_token=REFRESH_TOKEN" \
         https://mautic.example.com/oauth/v2/token

New access token response
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: json

    {
        "access_token": "NEW_ACCESS_TOKEN",
        "expires_in": 3600,
        "token_type": "bearer",
        "scope": "",
        "refresh_token": "REFRESH_TOKEN"
    }

.. note::

   Store this data securely and use it to authenticate future API requests.

.. vale off

Client Credentials flow
=======================

Using the Mautic API library for Client Credentials flow
--------------------------------------------------------

.. vale on

.. warning:: 

   Mautic's API library doesn't support this flow yet, but you can track the progress in the :xref:`Client Credentials Support` PR.

.. vale off

Using the standard OAuth2 for Client Credentials flow
-----------------------------------------------------

.. vale on

To obtain a new access token, send a ``POST`` request to the token endpoint ``oauth/v2/token`` using the ``client_credentials`` grant type.

.. code-block:: bash

    curl -X POST \
         -H "Content-Type: application/x-www-form-urlencoded" \
         -d "grant_type=client_credentials&client_id=CLIENT_ID&client_secret=CLIENT_SECRET" \
         https://mautic.example.com/oauth/v2/token

Client credentials response
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

    {
        "access_token": "NEW_ACCESS_TOKEN",
        "expires_in": 3600,
        "token_type": "bearer",
        "scope": ""
    }

.. note::

   Store this data securely and use it to authenticate future API requests.

Authenticating the API request
==============================

Authenticating API requests with OAuth2 is straightforward. Choose one of the following methods.

Authorization header
--------------------

The Authorization header enables authentication for all Mautic API endpoints.

This method requires the Mautic server to pass headers to PHP or provide access to the ``apache_request_headers()`` function. Note that ``apache_request_headers()`` is unavailable when running PHP under FastCGI.

.. code-block:: bash

    Authorization: Bearer ACCESS_TOKEN

Other methods
-------------

While the preferred method is to send the access token in the ``Authorization: Bearer`` header, you may alternatively include it in the ``POST`` body when using ``application/x-www-form-urlencoded`` if your client cannot set custom headers. Avoid putting access tokens in URL query strings, since server logs, browser history, and ``Referer`` headers often record URLs and can inadvertently expose your token.

.. code-block:: bash

    curl -X POST \
         -H "Content-Type: application/x-www-form-urlencoded" \
         -d "firstname=John&lastname=Smith&access_token=ACCESS_TOKEN" \
         https://mautic.example.com/api/leads/new