Builder integrations
#####################

Builders can register itself as a "builder" for Email and/or Landing Pages.

----

.. vale off

Registering the Integration as a Builder
****************************************

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
                'helloworld.integration.builder' => [
                    'class' => \MauticPlugin\HelloWorldBundle\Integration\Support\BuilderSupport::class,
                    'tags'  => [
                        'mautic.builder_integration',
                    ],
                ],
                // ...
            ],
            // ...
        ],
        // ...
    ];


The ``BuilderSupport`` class must implement::

    \Mautic\IntegrationsBundle\Integration\Interfaces\BuilderInterface

The only method currently defined for the interface is ``isSupported`` which should return a boolean if it supports the given feature. Currently, Mautic supports ``email`` and ``page (Landing Pages)``. This determines what Themes should list as an option for the given builder/feature.
