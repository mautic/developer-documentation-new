**************************************************
Getting started with the ``Integration Framework``
**************************************************

.. contents:: Table of contents

The IntegrationsBundle is meant to be a drop in replacement for Mautic's PluginBundle's AbstractIntegration class. It provides cleaner interfaces for configuring, authenticating, and syncing Contacts/Companies with third party Integrations.

An example HelloWorld Plugin is available :xref:`Plugin HelloWorld`.

---------

Using the Integration Framework
###############################

Register the ``Integration`` for authentication
***********************************************

If the Integration requires authentication with the third party service:

1. :ref:`Register the Integration<Registering the Integration for authentication>` as an Integration that requires configuration options.
2. Create a custom Symfony Form type for the required credentials and return it as part of the :ref:`config interface<ConfigFormAuthInterface>`.
3. Create a custom service that builds and configures the Guzzle client required to authenticate and communicate with the third party service. Use an [existing supported factory or create a new one](#authentication-providers).

Register the ``Integration`` for configuration
***********************************************

If the Integration has extra configuration settings for features unique to it:

1. :ref:`Register the Integration<Registering the Integration for configuration>` as an Integration that requires configuration options.
2. Create a custom Symfony Form type for the features and return it as part of the :ref:`Config Form feature setting interface<ConfigFormFeatureSettingsInterface>`.

The sync engine
***************

If the Integration syncs with Mautic's Contacts and/or Companies:

1. Read about :doc:`the sync engine<sync>`.

Register the ``Integration`` as a Builder
*****************************************

If the Integration includes a Builder (Email or Landing Page):

1. :ref:`Register the Integration<Registering the Integration as a builder>` as an Integration that provides a custom builder.
2. Configure what featured builders the Integration supports (Mautic currently supports 'Email' and 'Landing Page' builders).

Basics
******

Each Integration provides its unique name as registered with Mautic, an icon, and a display name. When an Integration is registered, the Integration helper classes manages the ``\Mautic\PluginBundle\Entity\Integration`` object through ``\Mautic\IntegrationsBundle\Integration\Interfaces\IntegrationInterface``. It handles decryption and encryption of the Integration's API keys so the implementing code never has to.

Registering the integration
***************************

All Integrations, whether using the config, auth, or sync interfaces, must have a class that registers itself with Mautic. The Integration should list on the ``/s/plugins`` page.

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

The ``HelloWorldIntegration`` needs to implement ``\Mautic\IntegrationsBundle\Integration\Interfaces\IntegrationInterface`` and ``\Mautic\IntegrationsBundle\Integration\Interfaces\BasicInterface`` interfaces. Most use cases can simply extend the ``\Mautic\IntegrationsBundle\Integration\BasicIntegration`` abstract class then define the ``getName()``, ``getDisplayName()`` and ``getIcon()`` methods.

.. code-block:: php

    <?php
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

