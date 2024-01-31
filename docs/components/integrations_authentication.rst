.. It is a reference only page, not a part of doc tree.

:orphan:

.. vale off

Authentication integration
##########################

.. vale on

The IntegrationsBundle provides factories and helpers to create Guzzle Client classes for common authentication protocols.

----------

.. vale off

Register the Integration for Authentication
*******************************************

.. vale on

If the Integration requires the User to authenticate through the web (OAuth2 three legged), the Integration needs to tag a service with ``mautic.auth_integration`` to handle the authentication process like redirecting to login, request the access token, and so forth.

.. code-block:: php

    <?php
    return [
        // ...
        'services' => [
            // ...
            'integrations' => [
                // ...
                'helloworld.integration.authentication' => [
                    'class' => \MauticPlugin\HelloWorldBundle\Integration\Support\AuthSupport::class,
                    'tags'  => [
                        'mautic.auth_integration',
                    ],
                ],
                // ...
            ],
            // ...
        ],
        // ...
    ];


This service needs to implement ``\Mautic\IntegrationsBundle\Integration\Interfaces\AuthenticationInterface``.

.. php:interface:: Mautic\IntegrationsBundle\Integration\Interfaces\AuthenticationInterface

.. php:method:: public function isAuthenticated(): bool;

    :return:  Returns true if the Integration has already been authorized with the third party service.
    :returntype: bool

.. php:method:: public function authenticateIntegration(Request $request): string;

    :param Request $request: The request object.

    :return: A message to render if succeeded.
    :returntype: string

Find the code snippet as follows,

.. code-block:: php

    <?php
    namespace MauticPlugin\HelloWorldBundle\Integration\Support;

    use MauticPlugin\HelloWorldBundle\Connection\Client;
    use MauticPlugin\HelloWorldBundle\Integration\HelloWorldIntegration;
    use Mautic\IntegrationsBundle\Integration\ConfigurationTrait;
    use Mautic\IntegrationsBundle\Integration\Interfaces\AuthenticationInterface;
    use Symfony\Component\HttpFoundation\Request;

    class AuthSupport implements AuthenticationInterface
    {
        use ConfigurationTrait;

        private Client $client;

        public function __construct(Client $client)
        {
            $this->client = $client;
        }

        public function getName(): string
        {
            return HelloWorldIntegration::NAME;
        }

        public function getDisplayName(): string
        {
            return 'Hello World';
        }

        /**
         * Returns true if the integration has already been authorized with the third party service.
         *
         * @return bool
         */
        public function isAuthenticated(): bool
        {
            $apiKeys = $this->getIntegrationConfiguration()->getApiKeys();

            return !empty($apiKeys['access_token']) && !empty($apiKeys['refresh_token']);
        }

        /**
         * Authenticate and obtain the access token
         *
         * @param Request $request
         *
         * @return string
         */
        public function authenticateIntegration(Request $request): string
        {
            $code = $request->query->get('code');

            $this->client->authenticate($code);

            return 'Success!';
        }
    }

Authentication providers
************************

The Integration bundle comes with a number of popular authentication protocols available to use as Guzzle clients. New ones should implement:

    ``\Mautic\IntegrationsBundle\Auth\Provider\AuthProviderInterface``

**The examples below use anonymous classes. Use Object Oriented Programming with services and factories to generate credential, configuration, and client classes.**

The best way to get configuration values such as username, password, consumer key, consumer secret, and so forth is by using the ``mautic.integrations.helper`` ``(\Mautic\IntegrationsBundle\Helper\IntegrationsHelper)`` service to leverage the configuration stored in the ``Integration`` entity's API keys.

.. code-block:: php

    <?php
    use MauticPlugin\HelloWorldBundle\Integration\HelloWorldIntegration;
    use Mautic\IntegrationsBundle\Helper\IntegrationsHelper;

    /** @var $integrationsHelper IntegrationsHelper */
    $integration = $integrationsHelper->getIntegration(HelloWorldIntegration::NAME);

    $configuration = $integration->getIntegrationConfiguration();
    $apiKeys       = $configuration->getApiKeys();

    $username = $apiKeys['username'] ?? null;
    $password = $apiKeys['password'] ?? null;

    //...


API key
=======

Use the ``mautic.integrations.auth_provider.api_key`` service - ``\Mautic\IntegrationsBundle\Auth\Provider\ApiKey\HttpFactory`` - to obtain a ``GuzzleHttp\ClientInterface`` that uses an API key for all requests. Out of the box, the factory supports a parameter API key or a header API key.

Parameter based API key
-----------------------

To use the parameter based API key, create a credentials class that implements ``\Mautic\IntegrationsBundle\Auth\Provider\ApiKey\Credentials\ParameterCredentialsInterface``.

.. php:class:: \Mautic\IntegrationsBundle\Auth\Provider\ApiKey\Credentials\ParameterCredentialsInterface

.. php:method:: public function getKeyName(): string;

    :return: Key name.
    :returntype: string

.. php:method:: public function getApiKey(): ?string;

    :return: API key or null.
    :returntype: ?string

Find the code snippet as follows,

.. code-block:: php

    <?php
    use MauticPlugin\HelloWorldBundle\Integration\HelloWorldIntegration;
    use Mautic\IntegrationsBundle\Auth\Provider\ApiKey\Credentials\ParameterCredentialsInterface;
    use Mautic\IntegrationsBundle\Auth\Provider\ApiKey\HttpFactory;
    use Mautic\IntegrationsBundle\Helper\IntegrationsHelper;

    /** @var $integrationsHelper IntegrationsHelper */
    $integration = $integrationsHelper->getIntegration(HelloWorldIntegration::NAME);

    $apiKeys = $integration->getIntegrationConfiguration()->getApiKeys();

    $credentials = new class($apiKeys['api_key']) implements ParameterCredentialsInterface {
        private $key;

        public function __construct(string $key)
        {
            $this->key = $key;
        }

        public function getKeyName(): string
        {
            return 'apikey';
        }

        public function getApiKey(): string
        {
            return $this->key;
        }
    };

    /** @var $factory HttpFactory */
    $client   = $factory->getClient($credentials);
    $response = $client->get('https://example.com/api/fetch');


Header based API key
--------------------

To use the header based API key, create a credentials class that implements ``\Mautic\IntegrationsBundle\Auth\Provider\ApiKey\Credentials\HeaderCredentialsInterface``.

.. php:class:: \Mautic\IntegrationsBundle\Auth\Provider\ApiKey\Credentials\HeaderCredentialsInterface

.. php:method:: public function getKeyName(): string;

    :return: Key name.
    :returntype: string

.. php:method:: public function getApiKey(): ?string;

    :return: API key or null.
    :returntype: ?string

Find the code snippet as follows,

.. code-block:: php

    <?php
    use MauticPlugin\HelloWorldBundle\Integration\HelloWorldIntegration;
    use Mautic\IntegrationsBundle\Auth\Provider\ApiKey\Credentials\HeaderCredentialsInterface;
    use Mautic\IntegrationsBundle\Auth\Provider\ApiKey\HttpFactory;
    use Mautic\IntegrationsBundle\Helper\IntegrationsHelper;

    /** @var $integrationsHelper IntegrationsHelper */
    $integration = $integrationsHelper->getIntegration(HelloWorldIntegration::NAME);

    $apiKeys = $integration->getIntegrationConfiguration()->getApiKeys();

    $credentials = new class($apiKeys['api_key']) implements HeaderCredentialsInterface {
        private $key;

        public function __construct(string $key)
        {
            $this->key = $key;
        }

        public function getKeyName(): string
        {
            return 'X-API-KEY';
        }

        public function getApiKey(): string
        {
            return $this->key;
        }
    };

    /** @var $factory HttpFactory */
    $client   = $factory->getClient($credentials);
    $response = $client->get('https://example.com/api/fetch');


Basic auth
==========

Use the ``mautic.integrations.auth_provider.basic_auth`` service - ``\Mautic\IntegrationsBundle\Auth\Provider\BasicAuth\HttpFactory`` - to obtain a ``GuzzleHttp\ClientInterface`` that uses basic auth for all requests.

To use the basic auth, create a credentials class that implements ``\Mautic\IntegrationsBundle\Auth\Provider\BasicAuth\CredentialsInterface``.

.. php:class:: \Mautic\IntegrationsBundle\Auth\Provider\BasicAuth\CredentialsInterface

.. php:method:: public function getUsername(): ?string;

    :return: User name.
    :returntype: ?string

.. php:method:: public function getPassword(): ?string;

    :return: Password.
    :returntype: ?string

Find the code snippet as follows,

.. code-block:: php

    <?php
    use MauticPlugin\HelloWorldBundle\Integration\HelloWorldIntegration;
    use Mautic\IntegrationsBundle\Helper\IntegrationsHelper;
    use Mautic\IntegrationsBundle\Auth\Provider\BasicAuth\HttpFactory;
    use Mautic\IntegrationsBundle\Auth\Provider\BasicAuth\CredentialsInterface;

    /** @var $integrationsHelper IntegrationsHelper */
    $integration = $integrationsHelper->getIntegration(HelloWorldIntegration::NAME);

    $configuration = $integration->getIntegrationConfiguration();
    $apiKeys       = $configuration->getApiKeys();

    $credentials = new class($apiKeys['username'], $apiKeys['password']) implements CredentialsInterface {
        private $username;
        private $password;

        public function __construct(string $username, string $password)
        {
            $this->username = $username;
            $this->password = $password;
        }

        public function getUsername(): string
        {
            return $this->username;
        }

        public function getPassword(): string
        {
            return $this->password;
        }
    };

    /** @var $factory HttpFactory */
    $client   = $factory->getClient($credentials);
    $response = $client->get('https://example.com/api/fetch');


OAuth1a
=======

OAuth1a three legged
--------------------

Yet to implement in the core.

OAuth1a two legged
------------------

OAuth1a two legged doesn't require a User to login as would three legged.

.. code-block:: php

    <?php
    use MauticPlugin\HelloWorldBundle\Integration\HelloWorldIntegration;
    use Mautic\IntegrationsBundle\Helper\IntegrationsHelper;
    use Mautic\IntegrationsBundle\Auth\Provider\OAuth1aTwoLegged\HttpFactory;
    use Mautic\IntegrationsBundle\Auth\Provider\OAuth1aTwoLegged\CredentialsInterface;

    /** @var $integrationsHelper IntegrationsHelper */
    $integration = $integrationsHelper->getIntegration(HelloWorldIntegration::NAME);

    $configuration = $integration->getIntegrationConfiguration();
    $apiKeys       = $configuration->getApiKeys();

    $credentials = new class(
        'https://example.com/api/oauth/token',
        $apiKeys['consumer_key'],
        $apiKeys['consumer_secret']
    ) implements CredentialsInterface {
        private $authUrl;
        private $consumerKey;
        private $consumerSecret;

        public function __construct(string $authUrl, string $consumerKey, string $consumerSecret)
        {
            $this->authUrl        = $authUrl;
            $this->consumerKey    = $consumerKey;
            $this->consumerSecret = $consumerSecret;
        }

        public function getAuthUrl(): string
        {
            return $this->authUrl;
        }

        public function getConsumerKey(): ?string
        {
            return $this->consumerKey;
        }

        public function getConsumerSecret(): ?string
        {
            return $this->consumerSecret;
        }

        /**
         * Not used in this example. Tsk tsk for breaking the interface segregation principle
         *
         * @return string|null
         */
        public function getToken(): ?string
        {
            return null;
        }

        /**
         * Not used in this example. Tsk tsk for breaking the interface segregation principle
         *
         * @return string|null
         */
        public function getTokenSecret(): ?string
        {
            return null;
        }
    };

    /** @var $factory HttpFactory */
    $client   = $factory->getClient($credentials);
    $response = $client->get('https://example.com/api/fetch');

OAuth2
======

Use the OAuth2 factory according to the grant type required. ``\Mautic\IntegrationsBundle\Auth\Provider\Oauth2ThreeLegged\HttpFactory`` supports ``code`` and ``refresh_token`` grant types. ``\Mautic\IntegrationsBundle\Auth\Provider\Oauth2TwoLegged\HttpFactory`` supports ``client_credentials`` and ``password``.

The OAuth2 factories leverages :xref:`Guzzle Oauth2 Subscriber` as a middleware.

Client configuration
--------------------

Both OAuth2 factories leverage the ``\Mautic\IntegrationsBundle\Auth\Provider\AuthConfigInterface`` object to manage things such as configuring the signer (basic auth, ``post form data``, custom), token factory, token persistence, and token signer (bearer auth, basic auth, query string, custom). Use the appropriate interfaces as required for the use case (see the interfaces in ``app/bundles/IntegrationsBundle/Auth/Support/Oauth2/ConfigAccess``).

See :xref:`Guzzle Oauth2 Subscriber` for additional details on configuring the credentials and token signers or creating custom token persistence and factories.

Token persistence
-----------------

For most use cases, a token persistence service requires fetching and storing the access tokens generated by using refresh tokens, etc. The IntegrationBundle provides one that natively uses the ``\Mautic\PluginBundle\Entity\Integration`` entity's API keys. Anything stored through the service is automatically encrypted.

Use the ``mautic.integrations.auth_provider.token_persistence_factory`` service - ``\Mautic\IntegrationsBundle\Auth\Support\Oauth2\Token\TokenPersistenceFactory`` - to generate a ``TokenFactoryInterface``. The``\Mautic\IntegrationsBundle\Auth\Support\Oauth2\ConfigAccess\ConfigTokenFactoryInterface`` interface returns it.
 
.. code-block:: php

    <?php
    use kamermans\OAuth2\Persistence\TokenPersistenceInterface;
    use MauticPlugin\HelloWorldBundle\Integration\HelloWorldIntegration;
    use Mautic\IntegrationsBundle\Auth\Support\Oauth2\ConfigAccess\ConfigTokenPersistenceInterface;
    use Mautic\IntegrationsBundle\Auth\Support\Oauth2\Token\TokenPersistenceFactory;
    use Mautic\IntegrationsBundle\Helper\IntegrationsHelper;

    /** @var $integrationsHelper IntegrationsHelper */
    $integration = $integrationsHelper->getIntegration(HelloWorldIntegration::NAME);

    /** @var $tokenPersistenceFactory TokenPersistenceFactory */
    $tokenPersistence = $tokenPersistenceFactory->create($integration);

    $config = new class($tokenPersistence) implements ConfigTokenPersistenceInterface {
        private $tokenPersistence;

        public function __construct(TokenPersistenceInterface$tokenPersistence)
        {
            $this->tokenPersistence = $tokenPersistence;
        }

        public function getTokenPersistence(): TokenPersistenceInterface
        {
            return $this->tokenPersistence;
        }
    };

The token persistence service automatically manages ``access_token``, ``refresh_token``, and ``expires_at`` from the authentication process and stores them in the ``Integration`` entity's API keys array.

Token factory
-------------

In some cases, the third-party service may return additional values that aren't traditionally part of the OAuth2 spec. Sometimes, the API service requires these values for further communication. In this case, the Integration bundle's ``\Mautic\IntegrationsBundle\Auth\Support\Oauth2\Token\IntegrationTokenFactory`` can use to capture those extra values and store them in the ``Integration`` entity's API keys array.

You can then return the ``IntegrationTokenFactory`` in a ``\Mautic\IntegrationsBundle\Auth\Support\Oauth2\ConfigAccess\ConfigTokenFactoryInterface`` when configuring the ``Client``.

.. code-block:: php

    <?php
    use Mautic\IntegrationsBundle\Auth\Support\Oauth2\ConfigAccess\ConfigTokenFactoryInterface;
    use Mautic\IntegrationsBundle\Auth\Support\Oauth2\Token\IntegrationTokenFactory;
    use Mautic\IntegrationsBundle\Auth\Support\Oauth2\Token\TokenFactoryInterface;

    $tokenFactory = new IntegrationTokenFactory(['something_extra']);

    $config = new class($tokenFactory) implements ConfigTokenFactoryInterface {
        private $tokenFactory;

        public function __construct(TokenFactoryInterface $tokenFactory)
        {
            $this->tokenFactory = $tokenFactory;
        }

        public function getTokenFactory(): TokenFactoryInterface
        {
            return $this->tokenFactory;
        }
    };

OAuth2 two legged
=================

Password grant
--------------

Below is an example of the password grant for a service that uses a scope. The interfaces used are optional. The use of the token persistence is assuming the access token is valid for an hour.

.. code-block:: php

    <?php
    use kamermans\OAuth2\Persistence\TokenPersistenceInterface;
    use MauticPlugin\HelloWorldBundle\Integration\HelloWorldIntegration;
    use Mautic\IntegrationsBundle\Auth\Provider\Oauth2TwoLegged\Credentials\PasswordCredentialsGrantInterface;
    use Mautic\IntegrationsBundle\Auth\Provider\Oauth2TwoLegged\Credentials\ScopeInterface;
    use Mautic\IntegrationsBundle\Auth\Provider\Oauth2TwoLegged\HttpFactory;
    use Mautic\IntegrationsBundle\Auth\Support\Oauth2\ConfigAccess\ConfigTokenPersistenceInterface;
    use Mautic\IntegrationsBundle\Helper\IntegrationsHelper;

    /** @var $integrationsHelper IntegrationsHelper */
    $integration = $integrationsHelper->getIntegration(HelloWorldIntegration::NAME);

    $configuration = $integration->getIntegrationConfiguration();
    $apiKeys       = $configuration->getApiKeys();

    $credentials = new class(
        'https://example.com/api/oauth/token',
        'scope1,scope2',
        $apiKeys['client_id'],
        $apiKeys['client_secret'],
        $apiKeys['username'],
        $apiKeys['password']
    ) implements PasswordCredentialsGrantInterface, ScopeInterface {
        private $authorizeUrl;
        private $scope;
        private $clientId;
        private $clientSecret;
        private $username;
        private $password;

        public function getAuthorizationUrl(): string
        {
            return $this->authorizeUrl;
        }

        public function getClientId(): ?string
        {
            return $this->clientId;
        }

        public function getClientSecret(): ?string
        {
            return $this->clientSecret;
        }

        public function getPassword(): ?string
        {
            return $this->password;
        }

        public function getUsername(): ?string
        {
            return $this->username;
        }

        public function getScope(): ?string
        {
            return $this->scope;
        }
    };

    /** @var $tokenPersistenceFactory TokenPersistenceFactory */
    $tokenPersistence = $tokenPersistenceFactory->create($integration);
    $config           = new class($tokenPersistence) implements ConfigTokenPersistenceInterface {
        private $tokenPersistence;

        public function __construct(TokenPersistenceInterface$tokenPersistence)
        {
            $this->tokenPersistence = $tokenPersistence;
        }

        public function getTokenPersistence(): TokenPersistenceInterface
        {
            return $this->tokenPersistence;
        }
    };

    /** @var $factory HttpFactory */
    $client   = $factory->getClient($credentials, $config);
    $response = $client->get('https://example.com/api/fetch');

Client credentials grant
------------------------

Below is an example of the client credentials grant for a service that uses a scope. The interfaces used are optional. The use of the token persistence is assuming the access token is valid for an hour.

.. code-block:: php

    <?php
    use kamermans\OAuth2\Persistence\TokenPersistenceInterface;
    use MauticPlugin\HelloWorldBundle\Integration\HelloWorldIntegration;
    use Mautic\IntegrationsBundle\Auth\Provider\Oauth2TwoLegged\Credentials\ClientCredentialsGrantInterface;
    use Mautic\IntegrationsBundle\Auth\Provider\Oauth2TwoLegged\Credentials\ScopeInterface;
    use Mautic\IntegrationsBundle\Auth\Provider\Oauth2TwoLegged\HttpFactory;
    use Mautic\IntegrationsBundle\Auth\Support\Oauth2\ConfigAccess\ConfigTokenPersistenceInterface;
    use Mautic\IntegrationsBundle\Helper\IntegrationsHelper;

    /** @var $integrationsHelper IntegrationsHelper */
    $integration = $integrationsHelper->getIntegration(HelloWorldIntegration::NAME);

    $configuration = $integration->getIntegrationConfiguration();
    $apiKeys       = $configuration->getApiKeys();

    $credentials = new class(
        'https://example.com/api/oauth/token',
        'scope1,scope2',
        $apiKeys['client_id'],
        $apiKeys['client_secret']
    ) implements ClientCredentialsGrantInterface, ScopeInterface {
        private $authorizeUrl;
        private $scope;
        private $clientId;
        private $clientSecret;

        public function getAuthorizationUrl(): string
        {
            return $this->authorizeUrl;
        }

        public function getClientId(): ?string
        {
            return $this->clientId;
        }

        public function getClientSecret(): ?string
        {
            return $this->clientSecret;
        }

        public function getScope(): ?string
        {
            return $this->scope;
        }
    };

    /** @var $tokenPersistenceFactory TokenPersistenceFactory */
    $tokenPersistence = $tokenPersistenceFactory->create($integration);
    $config           = new class($tokenPersistence) implements ConfigTokenPersistenceInterface {
        private $tokenPersistence;

        public function __construct(TokenPersistenceInterface$tokenPersistence)
        {
            $this->tokenPersistence = $tokenPersistence;
        }

        public function getTokenPersistence(): TokenPersistenceInterface
        {
            return $this->tokenPersistence;
        }
    };

    /** @var $factory HttpFactory */
    $client   = $factory->getClient($credentials, $config);
    $response = $client->get('https://example.com/api/fetch');

OAuth2 three legged
===================

Three legged OAuth2 with the code grant is the most complex to implement because it involves redirecting the User to the third party service to authenticate then sent back to Mautic to initiate the access token process using a code returned in the request.

The first step is to register the Integration as a :ref:`\\Mautic\\IntegrationsBundle\\Integration\\Interfaces\\AuthenticationInterface<components/integrations_authentication:Register the Integration for Authentication>`.
The ``authenticateIntegration()`` method initiates the access token process using the ``code`` returned in the request after the User logs into the third-party service.

.. vale off

The Integration bundle provides a route that can use as the redirect or callback URIs through the named route ``mautic_integration_public_callback`` that requires a ``integration`` parameter.

.. vale on

This redirect URI can display in the UI by using :xref:`ConfigFormCallbackInterface`. This route is to find the Integration by name from the ``AuthIntegrationsHelper`` and then execute its ``authenticateIntegration()``.

.. code-block:: php

    <?php
    namespace MauticPlugin\HelloWorldBundle\Integration\Support;

    use GuzzleHttp\ClientInterface;
    use Mautic\IntegrationsBundle\Integration\Interfaces\AuthenticationInterface;
    use Symfony\Component\HttpFoundation\Request;
    use Symfony\Component\HttpFoundation\Response;

    class AuthSupport implements AuthenticationInterface {
        private ClientInterface $client;

        // ...

        public function authenticateIntegration(Request $request): Response
        {
            $code = $request->query->get('code');

            $this->client->authenticate($code);

            return new Response('OK!');
        }
    }

The trick here is that the ``Client``'s ``authenticate`` method configures a ``ClientInterface`` and then calls any valid API URL.
The middleware initiates the access token process by making a call and storing it in the ``Integration`` entity's API keys through :ref:`TokenPersistenceFactory<components/integrations_authentication:Token Persistence>`.
Mautic recommends keeping the URL simple, like a checking version or fetching info for the authenticated User.

Here is an example of a client, assuming that the User has already logged in and the code is in the request.

.. code-block:: php

    <?php
    use kamermans\OAuth2\Persistence\TokenPersistenceInterface;
    use MauticPlugin\HelloWorldBundle\Integration\HelloWorldIntegration;
    use Mautic\IntegrationsBundle\Auth\Provider\Oauth2ThreeLegged\Credentials\CodeInterface;
    use Mautic\IntegrationsBundle\Auth\Provider\Oauth2ThreeLegged\Credentials\CredentialsInterface;
    use Mautic\IntegrationsBundle\Auth\Provider\Oauth2ThreeLegged\Credentials\RedirectUriInterface;
    use Mautic\IntegrationsBundle\Auth\Provider\Oauth2TwoLegged\Credentials\ScopeInterface;
    use Mautic\IntegrationsBundle\Auth\Provider\Oauth2TwoLegged\HttpFactory;
    use Mautic\IntegrationsBundle\Auth\Support\Oauth2\ConfigAccess\ConfigTokenPersistenceInterface;
    use Mautic\IntegrationsBundle\Helper\IntegrationsHelper;
    use Symfony\Component\HttpFoundation\Request;
    use Symfony\Component\Routing\Router;

    /** @var $integrationsHelper IntegrationsHelper */
    $integration = $integrationsHelper->getIntegration(HelloWorldIntegration::NAME);

    /** @var Router $router */
    $redirectUrl = $router->generate('mautic_integration_public_callback', ['integration' => HelloWorldIntegration::NAME]);

    $configuration = $integration->getIntegrationConfiguration();
    $apiKeys       = $configuration->getApiKeys();

    /** @var Request $request */
    $code = $request->get('code');

    $credentials = new class(
        'https://example.com/api/oauth/authorize',
        'https://example.com/api/oauth/token',
        $redirectUrl,
        'scope1,scope2',
        $apiKeys['client_id'],
        $apiKeys['client_secret'],
        $code
    ) implements CredentialsInterface, RedirectUriInterface, ScopeInterface, CodeInterface {
        private $authorizeUrl;
        private $tokenUrl;
        private $redirectUrl;
        private $scope;
        private $clientId;
        private $clientSecret;
        private $code;

        public function __construct(string $authorizeUrl, string $tokenUrl, string $redirectUrl, string $scope, string $clientId, string $clientSecret, ?string $code)
        {
            $this->authorizeUrl = $authorizeUrl;
            $this->tokenUrl     = $tokenUrl;
            $this->redirectUrl  = $redirectUrl;
            $this->scope        = $scope;
            $this->clientId     = $clientId;
            $this->clientSecret = $clientSecret;
            $this->code         = $code;
        }

        public function getAuthorizationUrl(): string
        {
            return $this->authorizeUrl;
        }

        public function getTokenUrl(): string
        {
            return $this->tokenUrl;
        }

        public function getRedirectUri(): string
        {
            return $this->redirectUrl;
        }

        public function getClientId(): ?string
        {
            return $this->clientId;
        }

        public function getClientSecret(): ?string
        {
            return $this->clientSecret;
        }

        public function getScope(): ?string
        {
            return $this->scope;
        }

        public function getCode(): ?string
        {
            return $this->code;
        }
    };

    /** @var $tokenPersistenceFactory TokenPersistenceFactory */
    $tokenPersistence = $tokenPersistenceFactory->create($integration);
    $config           = new class($tokenPersistence) implements ConfigTokenPersistenceInterface {
        private $tokenPersistence;

        public function __construct(TokenPersistenceInterface$tokenPersistence)
        {
            $this->tokenPersistence = $tokenPersistence;
        }

        public function getTokenPersistence(): TokenPersistenceInterface
        {
            return $this->tokenPersistence;
        }
    };

    /** @var $factory HttpFactory */
    $client   = $factory->getClient($credentials, $config);
    $response = $client->get('https://example.com/api/fetch');
