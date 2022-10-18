********************
Builder integrations
********************

.. contents:: Table of Contents

Builders can register itself as a "builder" for Email and/or Landing Pages. 

----

Registering the integration as a builder
========================================
To tell the IntegrationsBundle that this integration has configuration options, tag the integration or support class with ``mautic.config_integration`` in the Plugin's ``app/config.php``.

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

The only method currently defined for the interface is ``isSupported`` which should return a boolean if it supports the given feature. Currently, Mautic supports `email` and `page` (Landing Pages). This will determine what themes should be displayed as an option for the given builder/feature.
