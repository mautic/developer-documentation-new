Integrations
############

Integrate third-party services with Mautic by defining an Integration class for the service. Each Integration class handles the authorization process, configuration, and requests for that service.

.. vale off

.. note::

   This page covers the legacy ``AbstractIntegration`` approach. New Integrations should use the :doc:`Integrations framework</plugin_integrations/integrations>`, which separates authentication, configuration, and sync concerns into dedicated interfaces.

.. vale on

Integration class
*****************

A Plugin can provide multiple Integrations, each defined as its own class in the bundle's ``Integration`` folder. The class extends ``Mautic\PluginBundle\Integration\AbstractIntegration``, which provides many helper methods, including OAuth authorization and request signing:

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/Integration/MarsIntegration.php

    namespace MauticPlugin\HelloWorldBundle\Integration;

    use Mautic\PluginBundle\Integration\AbstractIntegration;

    class MarsIntegration extends AbstractIntegration
    {
        public function getName(): string
        {
            return 'Mars';
        }

        public function getDisplayName(): string
        {
            return 'Red Mars';
        }

        public function getAuthenticationType(): string
        {
            return 'oauth2';
        }

        public function getAuthenticationUrl(): string
        {
            return 'https://example.com/oauth/authorize';
        }

        public function getAccessTokenUrl(): string
        {
            return 'https://example.com/oauth/access_token';
        }

        public function getSupportedFeatures(): array
        {
            return ['public_profile', 'public_activity'];
        }
    }

``getName()`` must match the file - for example, ``IcontactIntegration`` returns ``Icontact``. ``getDisplayName()`` defaults to ``getName()`` unless you override it.

Integration image
*****************

Each Integration is displayed on a card in the 'Manage Plugins' area. To set its image, add a 128x128 px PNG to the bundle's ``Assets/img`` folder, named after the value returned by ``getName()`` in lowercase. For example, ``MarsIntegration`` uses ``plugins/HelloWorldBundle/Assets/img/mars.png``.

Authorization
*************

Out of the box, ``AbstractIntegration`` handles the standard key, OAuth1a, and OAuth2 specifications. The ``getAuthenticationType()`` method defines which one to use. ``getRequiredKeyFields()`` returns an array of ``keyName => label`` elements that defines each input the User must provide - username, password, and so on. You don't need that method when you use one of the standard specifications.

The Integration encrypts the keys it saves. To access the decrypted values inside the Integration class, use the ``$this->keys`` array. You can override any method defined in ``AbstractIntegration`` to suit the Integration's needs.

Functions
*********

The following table describes some of the main methods. Review the ``AbstractIntegration`` class and its method doc blocks for more detail.

.. list-table::
   :header-rows: 1

   * - Area
     - Function
     - Description
   * - Auth
     - ``getRequiredKeyFields``
     - Returns an array of ``keyName => label`` elements for settings the User must provide, such as username, password, client ID, or client secret. Mautic displays each element as an input in the Integration's settings.
   * - Auth
     - ``getSecretKeys``
     - Returns any ``keyName`` from ``getRequiredKeyFields`` that's secret, so Mautic masks it in the Form.
   * - Auth & Request
     - ``getClientIdKey``
     - Defines the 'username' for the Integration. Defaults to ``client_id`` for OAuth2 and ``keyName`` for the key authentication type.
   * - Auth & Request
     - ``getClientSecretKey``
     - Defines the 'password' for the Integration. By default, only OAuth2 uses this and returns ``client_secret``.
   * - Auth
     - ``getAuthLoginUrl``
     - Defines the login URL for the OAuth1a specification.
   * - Auth
     - ``getAuthenticationUrl``
     - Defines the login URL for the OAuth2 specification.
   * - Auth
     - ``getAccessTokenUrl``
     - Defines the access token URL for the OAuth2 specification.
   * - Auth
     - ``getAuthScope``
     - Defines the scope for the OAuth2 specification.
   * - Auth
     - ``getAuthCallbackUrl``
     - Defines the callback URL for the OAuth1a or OAuth2 specifications. Defaults to the ``mautic_integration_auth_callback`` route.
   * - General
     - ``isConfigured``
     - Determines whether the User has configured the Integration correctly.
   * - General
     - ``isAuthorized``
     - Determines whether the User has authorized the Integration. Mautic reauthorizes it automatically when a stored OAuth2 refresh token exists.
   * - Request
     - ``makeRequest``
     - Makes API requests, automatically handling the standard key, OAuth1a, and OAuth2 specifications.
   * - Form
     - ``getFormSettings``
     - Returns options for the Integration's configuration Form. Supported keys are ``requires_callback`` and ``requires_authorization``.
   * - Form
     - ``getFormNotes``
     - Returns helper notes to display in the Form.

.. vale off

makeRequest
===========

.. vale on

``makeRequest()`` can automatically sign outgoing requests and handle authentication. Any Integration can override it. It accepts the following parameters:

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``$url``
     - string
     - The URL to make the request to.
   * - ``$parameters``
     - array
     - Parameters to submit with the request. For a ``GET`` request, Mautic appends them to the query string; otherwise they form the POST body.
   * - ``$method``
     - string
     - The request method - ``GET``, ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
   * - ``$settings``
     - array
     - Configures the behavior of ``makeRequest()``. The following table lists the built-in optional settings.

Settings
~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Key
     - Type
     - Description
   * - ``auth_type``
     - string
     - Overrides the authentication type for the request. Defaults to ``getAuthenticationType()``.
   * - ``query``
     - array
     - Appends parameters to the query of the request URL.
   * - ``content_type``
     - string
     - Sets the ``Content-Type`` header for the request.
   * - ``encode_parameters``
     - string
     - If set to ``json``, Mautic JSON-encodes the POST parameters before the request.
   * - ``headers``
     - array
     - Custom headers to append to the request.
   * - ``ssl_verifypeer``
     - boolean
     - Sets ``CURLOPT_SSL_VERIFYPEER`` to true.
   * - ``curl_options``
     - array
     - A custom set of cURL options to apply to the request.
   * - ``return_raw``
     - boolean
     - If true, returns the raw response rather than running it through ``parseCallbackResponse()`` first.
