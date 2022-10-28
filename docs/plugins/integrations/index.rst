*********************
Integration framework
*********************

.. toctree::
   :caption: Integration Framework
   :maxdepth: 3
   :hidden:

   integrations
   authentication
   builder
   configuration
   migrations
   sync


Each Integration provides its unique name as registered with Mautic, an icon, and a display name. When an Integration registers, the Integration helper classes manage the ``\Mautic\PluginBundle\Entity\Integration`` object through ``\Mautic\IntegrationsBundle\Integration\Interfaces\IntegrationInterface``. It handles decryption and encryption of the Integration's API keys, so the implementing code never has to.

----

.. vale off

Registering the Integration
###########################

.. vale on

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
