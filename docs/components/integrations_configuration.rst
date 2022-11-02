.. It is a reference only page, not a part of doc tree.

:orphan:

Configuration integration
#########################

The Integration Plugin provides interfaces to display and store configuration options that can be accessed through the ``\Mautic\PluginBundle\Entity\Integration`` object.

.. vale off

Register the Integration for Configuration
******************************************

.. vale on

To tell the IntegrationsBundle that this Integration has configuration options, tag the Integration or support class with ``mautic.config_integration`` in the Plugin's ``app/config.php``.

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

.. php:interface:: \Mautic\IntegrationsBundle\Integration\Interfaces\ConfigFormInterface

.. php:method:: public function getDisplayName(): string;

    :return: Return the Integration's display name.
    :returntype: string

.. php:method:: public function getConfigFormName(): ?string;

    :return: The name/class of the Form type to override the default or just return NULL to use the default.
    :returntype: ?string

.. php:method:: public function getConfigFormContentTemplate(): ?string;

    :return: The template to use from the controller. Return null to use the default.
    :returntype: ?string

Find the code snippet as follows,

.. code-block:: php

    <?php
    namespace MauticPlugin\HelloBundle\Integration\Support;

    use MauticPlugin\HelloWorldBundle\Form\Type\ConfigAuthType;
    use Mautic\IntegrationsBundle\Integration\DefaultConfigFormTrait;
    use Mautic\IntegrationsBundle\Integration\Interfaces\ConfigFormInterface;
    use Mautic\IntegrationsBundle\Integration\Interfaces\ConfigFormAuthInterface;

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
**********

There are multiple interfaces that can be used to add Form Fields options to the provided configuration tabs.

Enabled/auth tab
================

These interfaces provide the configuration options for authenticating with the third party service. Read more about how to use IntegrationsBundle's  :ref:`auth providers here<Authentication Providers>`.


.. vale off

ConfigFormAuthInterface
-----------------------

.. vale on

The ``\Mautic\IntegrationsBundle\Integration\Interfaces\ConfigFormAuthInterface``, interface provides the Symfony Form type class that defines the fields to be stored as the API keys.

.. php:interface:: \Mautic\IntegrationsBundle\Integration\Interfaces\ConfigFormAuthInterface

.. php:method:: public function getAuthConfigFormName(): string;

    :return: The name of the Form type service for the authorization tab which should include all the fields required for the API to work.
    :returntype: string

Find the following code snippet which helps you to fetch the API keys,

.. code-block:: PHP

    <?php
    $apiKeys  = $integrationHelper->get(HelloWorldIntegration::NAME)->getIntegrationConfiguration()->getApiKeys();
    $username = $apiKeys['username'];


.. vale off

ConfigFormCallbackInterface
---------------------------

.. vale on

If the Integration leverages an auth provider that requires a callback URL or something similar, this interface, ``\Mautic\IntegrationsBundle\Integration\Interfaces\ConfigFormCallbackInterface``, provides a means to return a translation string to display in the UI.
For example, OAuth2 requires a redirect URI. If the administrator has to configure the OAuth credentials in the third party service and needs to know what URL to use in Mautic as the return URI, or callback URL, use the ``getCallbackHelpMessageTranslationKey()`` method.

.. php:interface:: \Mautic\IntegrationsBundle\Integration\Interfaces\ConfigFormCallbackInterface

.. php:method:: public function getCallbackHelpMessageTranslationKey(): string;

    :return: Message ID used in Form as description what for is used callback URL.
    :returntype: string

Feature interfaces
==================

.. vale off

ConfigFormFeatureSettingsInterface
----------------------------------

.. vale on

The interface, ``\Mautic\IntegrationsBundle\Integration\Interfaces\ConfigFormFeatureSettingsInterface``, provides the Symfony Form type class that defines the fields to be displayed on the Features tab. These values are not encrypted.

.. php:interface:: \Mautic\IntegrationsBundle\Integration\Interfaces\ConfigFormFeatureSettingsInterface

.. php:method:: public function getFeatureSettingsConfigFormName(): string;

    :return: The name of the Form type service for the feature settings.
    :returntype: string


.. code-block:: PHP

    <?php
    $featureSettings  = $integrationHelper->get(HelloWorldIntegration::NAME)->getIntegrationConfiguration()->getFeatureSettings();
    $doSomething      = $featureSettings['do_Something'];

.. vale off

ConfigFormFeaturesInterface
---------------------------

.. vale on


Currently the IntegrationsBundle provides default features. To use these features, implement this, ``\Mautic\IntegrationsBundle\Integration\Interfaces\ConfigFormFeaturesInterface``, interface.
``getSupportedFeatures`` returns an array of supported features.
For example, if the Integration syncs with Mautic Contacts, ``getSupportedFeatures()`` could ``return [ConfigFormFeaturesInterface::FEATURE_SYNC];``.

.. php:interface:: \Mautic\IntegrationsBundle\Integration\Interfaces\ConfigFormFeaturesInterface

.. php:attr:: public const FEATURE_SYNC = 'sync';
.. php:attr:: public const FEATURE_PUSH_ACTIVITY = 'push_activity';

.. php:method:: public function getSupportedFeatures(): array;

    :return: An array of value => label pairs for the features this Integration supports.
    :returntype: array[]

.. vale off

Contact/Company syncing interfaces
==================================

.. vale on

The IntegrationsBundle provides a sync framework for third party services to sync with Mautic's Contacts and Companies. The ``\Mautic\IntegrationsBundle\Integration\Interfaces\ConfigFormSyncInterface`` determines the configuration options for this sync feature. Refer to the method DocBlocks in the interface for more details.

Read more about how to leverage the :doc:`sync framework<sync>`.

.. vale off

Config Form notes interface
===========================

.. vale on

The interface, ``\Mautic\IntegrationsBundle\Integration\Interfaces\ConfigFormNotesInterface``, provides a way to display notes, either info or warning, on the plugin configuration Form.

Read more about to how-tos :doc:`here<configuration_form_notes>`
