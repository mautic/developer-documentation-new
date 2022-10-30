Using the integration framework
###############################

The IntegrationsBundle is a drop-in replacement for ``PluginBundle``'s ``AbstractIntegration`` class. It provides cleaner interfaces for configuring, authenticating, and syncing Contacts/Companies with third-party Integrations.

An example HelloWorld Plugin is available :xref:`here<Plugin HelloWorld>`.

---------

.. vale off

Register the Integration for Authentication
*******************************************

.. vale on

If the Integration requires authentication with the third party service:

1. :ref:`Register the Integration<Registering the Integration for Authentication>` as an Integration that requires configuration options.
2. Create a custom Symfony Form type for the required credentials and return it as part of the :ref:`config interface<ConfigFormAuthInterface>`.
3. Create a custom service that builds and configures the Guzzle client required to authenticate and communicate with the third party service. Use an :ref:`existing supported factory or create a new one<Authentication Providers>`.

.. vale off

Register the Integration for configuration
******************************************

.. vale on

If the Integration has extra configuration settings for features unique to it:

1. :ref:`Register the Integration<Registering the Integration for configuration>` as an Integration that requires configuration options.
2. Create a custom Symfony Form type for the features and return it as part of the :ref:`Config Form feature setting interface<ConfigFormFeatureSettingsInterface>`.

.. vale off

The Sync Engine
***************

.. vale on

If the Integration syncs with Mautic's Contacts and/or Companies:

1. Read about :doc:`the sync engine<sync>`.

.. vale off

Register the Integration as a Builder
*************************************

.. vale on

If the Integration includes a Builder, Email or Landing Page:

1. :ref:`Register the Integration<Registering the Integration as a builder>` as an Integration that provides a custom builder.
2. Configure what featured builders the Integration supports (Mautic currently supports 'Email' and 'Landing Page' builders).