Integration Configuration
#########################

.. contents:: Table of Contents

The integration plugin provides interfaces to display and store configuration options that can be accessed through the ``\Mautic\PluginBundle\Entity\Integration`` object.

Registering the Integration for Configuration
=============================================

To tell the IntegrationsBundle that this integration has configuration options, tag the integration or support class with ``mautic.config_integration`` in the plugin's ``app/config.php``.

.. code-block:: php

    <?php
    return [
        // ...
        'services' => [
            // ...
            'integrations' => [
                // ...
                'helloworld.integration.configuration' => [
                    'class' => \MauticPlugin\HelloWorldBundle\Integration\Support\ConfigSupport::class,
                    'tags'  => [
                        'mautic.config_integration',
                    ],
                ],
                // ...
            ],
            // ...
        ],
        // ...
    ];

The ``ConfigSupport`` class must implement ``\Mautic\IntegrationsBundle\Integration\Interfaces\ConfigFormInterface``.

.. code-block:: php

    <?php
    namespace MauticPlugin\HelloBundle\Integration\Support;

    use MauticPlugin\HelloWorldBundle\Form\Type\ConfigAuthType;
    use MauticPlugin\IntegrationsBundle\Integration\DefaultConfigFormTrait;
    use MauticPlugin\IntegrationsBundle\Integration\Interfaces\ConfigFormInterface;
    use MauticPlugin\IntegrationsBundle\Integration\Interfaces\ConfigFormAuthInterface;

    class ConfigSupport implements ConfigFormInterface, ConfigFormAuthInterface
    {
        use DefaultConfigFormTrait;

        public function getDisplayName(): string
        {
            return 'Hello World';
        }

        /**
         * Return a custom Symfony form field type class that will be used on the Enabled/Auth tab.
         * This should include things like API credentials, URLs, etc. All values from this form fields
         * will be encrypted before being persisted.
         *
         * @link https://symfony.com/doc/2.8/form/create_custom_field_type.html#defining-the-field-type
         *
         * @return string
         */
        public function getAuthConfigFormName(): string
        {
            return ConfigAuthType::class;
        }
    }


Interfaces
==========

There are multiple interfaces that can be used to add form fields options to the provided configuration tabs.

Enabled/Auth Tab
----------------
These interfaces provide the configuration options for authenticating with the third party service. Read more about how to use integrations bundle's [auth providers here](#integration-authentication).

ConfigFormAuthInterface
^^^^^^^^^^^^^^^^^^^^^^^

Used in the example above. This, ``\Mautic\IntegrationsBundle\Integration\Interfaces\ConfigFormAuthInterface``, interface provides the Symfony form type class that defines the fields to be stored as the API keys.

.. code-block:: PHP

    <?php
    $apiKeys  = $integrationHelper->get(HelloWorldIntegration::NAME)->getIntegrationConfiguration()->getApiKeys();
    $username = $apiKeys['username'];


ConfigFormCallbackInterface
^^^^^^^^^^^^^^^^^^^^^^^^^^^
If the integration leverages an auth provider that requires a callback URL or something similar, this interface, ``\Mautic\IntegrationsBundle\Integration\Interfaces\ConfigFormCallbackInterface``, provides a means to return a translation string to display in the UI. For example, OAuth2 requires a redirect URI. If the admin has to configure the OAuth credentials in the third party service and needs to know what URL to use in Mautic as the return URI, or callback URL, use the ``getCallbackHelpMessageTranslationKey()`` method.

Feature Interfaces
------------------

ConfigFormFeatureSettingsInterface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The interface, ``\Mautic\IntegrationsBundle\Integration\Interfaces\ConfigFormFeatureSettingsInterface``, provides the Symfony form type class that defines the fields to be displayed on the Features tab. These values are not encrypted.

.. code-block:: PHP

    <?php
    $featureSettings  = $integrationHelper->get(HelloWorldIntegration::NAME)->getIntegrationConfiguration()->getFeatureSettings();
    $doSomething      = $featureSettings['do_Something'];


ConfigFormFeaturesInterface
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Currently the integrations bundle provides default features. To use these features, implement this, ``\Mautic\IntegrationsBundle\Integration\Interfaces\ConfigFormFeaturesInterface``, interface. ``getSupportedFeatures`` returns an array of supported features. For example, if the Integration syncs with Mautic Contacts, ``getSupportedFeatures()`` could ``return [ConfigFormFeaturesInterface::FEATURE_SYNC];``.

Contact/Company Syncing Interfaces
----------------------------------
The integrations bundle provides a sync framework for third party services to sync with Mautic's Contacts and Companies. The ``\Mautic\IntegrationsBundle\Integration\Interfaces\ConfigFormSyncInterface`` determines the configuration options for this sync feature. Refer to the method DocBlocks in the interface for more details.

Read more about how to leverage the :doc:`sync framework<sync>`.