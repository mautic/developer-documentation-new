Integrations
############

Each Integration provides its unique name as registered with Mautic, an icon, and a display name. When an Integration registers, the Integration helper classes manage the ``\Mautic\PluginBundle\Entity\Integration`` object through ``\Mautic\IntegrationsBundle\Integration\Interfaces\IntegrationInterface``. It handles decryption and encryption of the Integration's API keys, so the implementing code never has to.

----

.. vale off

Registering the integration
***************************

.. vale on

All Integrations, whether using the config, auth, or sync interfaces, must have a class that registers itself with Mautic. The Integration should list on the ``/s/plugins`` UI route.

In the Plugin's ``Config/config.php``, register the Integration using the tag ``mautic.basic_integration``.

.. code-block:: php

    <?php
    return [
        // ...
        'services' => [
            // ...
            'integrations' => [
                'helloworld.integration' => [
                    'class' => \MauticPlugin\HelloWorldBundle\Integration\HelloWorldIntegration::class,
                    'tags'  => [
                        'mautic.basic_integration',
                    ],
                ],
                // ...
            ],
            // ...
        ],
        // ...
    ];

The ``HelloWorldIntegration`` needs to implement ``\Mautic\IntegrationsBundle\Integration\Interfaces\IntegrationInterface`` and ``\Mautic\IntegrationsBundle\Integration\Interfaces\BasicInterface`` interfaces. Most use cases can simply extend the ``\Mautic\IntegrationsBundle\Integration\BasicIntegration`` abstract class.

.. php:class:: \Mautic\IntegrationsBundle\Integration\BasicIntegration

.. php:method:: public function getName(): string;

    :return: Return the Integration's name.
    :returntype: string

.. php:method:: public function getDisplayName(): string;

    :return: Return the Integration's display name.
    :returntype: string

.. php:method:: public function getIcon(): string;

    :return: Get the path to the Integration's icon.
    :returntype: string



.. code-block:: php

    <?php
    namespace MauticPlugin\HelloWorldBundle\Integration;

    use Mautic\IntegrationsBundle\Integration\BasicIntegration;
    use Mautic\IntegrationsBundle\Integration\Interfaces\BasicInterface;
    use Mautic\IntegrationsBundle\Integration\Interfaces\IntegrationInterface;

    class HelloWorldIntegration extends BasicIntegration
    {
        const NAME = 'HelloWorld';

        public function getName(): string
        {
            return self::NAME;
        }

        public function getDisplayName(): string
        {
            return 'Hello World';
        }

        public function getIcon(): string
        {
            return 'plugins/HelloWorldBundle/Assets/img/helloworld.png';
        }
    }

.. note:: 
   ``HelloWorldIntegration::NAME`` must only contain letters such as a-z or A-Z.



Integration authentication
**************************

If the Integration requires authentication with the third party service:

1. :ref:`Register the Integration<components/integrations_authentication:Register the Integration for Authentication>` as an Integration that requires authentication options.
2. Create a custom Symfony Form type for the required credentials and return it as part of the :ref:`config interface<components/integrations_configuration:ConfigFormAuthInterface>`.
3. Create a custom service that builds and configures the Guzzle client required to authenticate and communicate with the third party service. Use an :ref:`existing supported factory or create a new one<components/integrations_authentication:Authentication Providers>`.

Integration configuration
*************************


If the Integration has extra configuration settings for features unique to it:

1. :ref:`Register the Integration<components/integrations_configuration:Register the Integration for configuration>` as an Integration that requires configuration options.
2. Create a custom Symfony Form type for the features and return it as part of the :ref:`Config Form feature setting interface<components/integrations_configuration:ConfigFormFeatureSettingsInterface>`.

.. vale off

Integration sync engine
***********************

.. vale on

If the Integration syncs with Mautic's Contacts and/or Companies:

1. Read about :ref:`the sync engine<components/integrations_sync:Sync engine>`.

.. vale off

Integration Builders
********************

.. vale on

If the Integration includes a Builder, Email, or Landing Page:

1. :ref:`Register the Integration<components/integrations_builder:Register the Integration as a builder>` as an Integration that provides a custom builder.
2. Configure what featured builders the Integration supports (Mautic currently supports 'Email' and 'Landing Page' builders).
