Getting started
===============

The IntegrationsBundle provides clean interfaces for configuring, authenticating, and syncing Contacts/Companies with third party Integrations.

An example HelloWorld Plugin is available (TODO XREF Mautic Hello World Plugin).

.. vale off

Using the Integration Framework
-------------------------------

.. vale on

*If the Integration requires authentication with the third party service*

1. :ref:`Register the Integration<registering the integration>` as an Integration that requires configuration options.
2. Create a custom Symfony Form type for the required credentials and return it as part of the config interface (TODO link to ConfigFormAuthInterface).
3. Create a custom service that builds and configures the Guzzle client required to authenticate and communicate with the third party service. TODO link to Authentication providers section :doc:`Use an existing supported factory or create a new one</components/integrations/authentication>`.

*If the Integration has extra configuration settings for features unique to it*

1. :doc:`Register the integration</components/integrations/configuration>` (TODO link to Registering the Integration for Configuration section) as an Integration that requires configuration options.
2. Create a custom Symfony Form type for the features and return it as part of the config interface (TODO link to ConfirmFormFeatureSettingsInterface).

*If the Integration syncs with Mautic's Contacts and/or Companies*

1. Read about :doc:`the sync engine</components/integrations/sync>`.

*If the Integration includes a builder Integration - Email or Landing Page*

1. :doc:`Register the integration</components/integrations/builders>` as an Integration that provides a custom builder. 
2. Configure what featured builders the Integration supports (Mautic currently supports ``email`` and ``page`` builders).

Basics
------
Each Integration provides its unique name as registered with Mautic, icon, and display name. When an Integration is registered, the Integration helper classes will manage the `\Mautic\PluginBundle\Entity\Integration` object through `\Mautic\IntegrationsBundle\Integration\Interfaces\IntegrationInterface`. It handles decryption and encryption of the integration's API keys so the implementing code never has to.

.. vale off

Registering the Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. vale on

All Integrations whether it uses the config, auth or sync interfaces must have a class that registers itself with Mautic. The Integration will be listed no the `/s/plugins` page.

In the Plugin's ``Config/config.php``, register the Integration using the tag ``mautic.basic_integration``.

.. code-block:: PHP

    <?php
    declare(strict_types=1);

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

The ``HelloWorldIntegration`` needs to implement ``\Mautic\IntegrationsBundle\Integration\Interfaces\IntegrationInterface`` and ``\Mautic\IntegrationsBundle\Integration\Interfaces\BasicInterface`` interfaces. Most use cases can simply extend the ``\Mautic\IntegrationsBundle\Integration\BasicIntegration`` abstract class then define the ``getName()``, ``getDisplayName()`` and ``getIcon()`` methods.

.. code-block:: PHP

    <?php
    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\Integration;

    use MauticPlugin\IntegrationsBundle\Integration\BasicIntegration;
    use MauticPlugin\IntegrationsBundle\Integration\Interfaces\BasicInterface;
    use MauticPlugin\IntegrationsBundle\Integration\Interfaces\IntegrationInterface;

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
