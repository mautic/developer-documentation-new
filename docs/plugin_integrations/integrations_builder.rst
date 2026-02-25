.. It is a reference only page, not a part of doc tree.

:orphan:

.. vale off

Builder Integrations
####################

.. vale on

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Builders can register itself as a "builder" for Email and/or Landing Pages.

----

.. vale off

Register the Integration as a Builder
*************************************

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
