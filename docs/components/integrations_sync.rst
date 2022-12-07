.. It is a reference only page, not a part of doc tree.

:orphan:

.. vale off

Sync engine
###########

.. vale on

The Sync Engine supports bidirectional syncing between Mautic's Contact and Companies with third party objects. The engine generates a "``sync report``" from Mautic that it converts to a "``sync order``" for the Integration to process. It then asks for a "``sync report``" from the Integration which it converts to a "``sync order``" for Mautic to process.

When building the Report, Mautic or the Integration fetches the objects those either modified or created within the specified timeframe. If the Integration supports changes at the field level, it should tell the Report on a per-field basis when the field was last updated. Otherwise, it should tell the Report when the object itself was last modified. The "``sync judge``" uses these dates to determine which value to use in bi-directional sync.

The ``mautic:integrations:sync`` command initiates the sync. For example::

    php bin/console mautic:integrations:sync HelloWorld --start-datetime="2020-01-01 00:00:00" --end-datetime="2020-01-02 00:00:00".

------

.. vale off

Registering the Integration for the Sync Engine
***********************************************

.. vale on

To tell the IntegrationsBundle that this Integration provides a syncing feature, tag the Integration or support class with ``mautic.sync_integration`` in the Plugin's ``app/config.php``.

.. code-block:: php

    <?php
    return [
        // ...
        'services' => [
            // ...
            'integrations' => [
                // ...
                'helloworld.integration.sync' => [
                    'class' => \MauticPlugin\HelloWorldBundle\Integration\Support\SyncSupport::class,
                    'tags'  => [
                        'mautic.sync_integration',
                    ],
                ],
                // ...
            ],
            // ...
        ],
        // ...
    ];

The ``SyncSupport`` class must implement::

        \Mautic\IntegrationsBundle\Integration\Interfaces\SyncInterface.

Syncing
*******

The mapping manual
==================

The mapping manual tells the Sync Engine which Integration should sync with which Mautic object like Contact or Company, the Integration fields. These fields should get mapped to Mautic fields, and the direction in the data suppose to flow.

See :xref:`MappingManualFactory`.

The sync data exchange
======================

This is where the sync takes place, and the ``mautic:integrations:sync``  executes it. Mautic and the Integration build their respective Reports of new or modified objects, then execute the order from the other side.

See :xref:`SyncDataExchange`.

.. vale off

Building Sync Report
____________________

.. vale on

The Sync Report tells the Sync Engine what objects are new and/or modified between the two timestamps given by the engine. It's up to the Integration's discretion if it's a first-time sync. Objects should process in batches and ``RequestDAO::getSyncIteration()`` takes care of this batching. The Sync Engine executes ``SyncDataExchangeInterface::getSyncReport()`` until a Report comes back with no objects.

If the Integration supports field level change tracking, it should tell the Report so that the Sync Engine can merge the two data sets more accurately.

See :xref:`ReportBuilder`.

.. vale off

Executing the Sync Order
________________________

.. vale on

The Sync Order contains all the changes the Sync Engine has determined, and these should inform the Integration. The Integration should communicate back the ID of any objects created or adjust objects as needed, such as if they get converted from one to another or deleted.

See :xref:`OrderExecutioner`.
