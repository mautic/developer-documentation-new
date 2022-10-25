***********************
Integration sync engine
***********************

.. contents:: Table of contents

The sync engine supports bidirectional syncing between Mautic's Contact and Companies with third party objects. The engine generates a "``sync report``" from Mautic that it converts to a "``sync order``" for the Integration to process. It then asks for a "``sync report``" from the Integration which it converts to a "``sync order``" for Mautic to process.

When building the Report, Mautic or the Integration fetches the objects that have been modified or created within the specified timeframe. If the Integration supports changes at the field level, it should tell the Report on a per field basis when the field was last updated. Otherwise, it should tell the Report when the object itself was last modified. These dates are used by the "``sync judge``" to determine which value should be used in a bi-directional sync.

The sync is initiated using the ``mautic:integrations:sync`` command. For example::

    php bin/console mautic:integrations:sync HelloWorld --start-datetime="2020-01-01 00:00:00" --end-datetime="2020-01-02 00:00:00".

------

Registering the Integration for the sync engine
###############################################

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

The mapping manual tells the sync engine which Integration should be synced with which Mautic object (Contact or Company), the Integration fields that were mapped to Mautic fields, and the direction the data is supposed to flow. 

See :xref:`MappingManualFactory`.

The sync data exchange
======================

This is where the sync takes place and is executed by the ``mautic:integrations:sync`` command. Mautic and the Integration builds their respective Reports of new or modified objects then execute the order from the other side.

See :xref:`SyncDataExchange`.

Building sync report
____________________

The sync report tells the sync engine what objects are new and/or modified between the two timestamps given by the engine (or up to the Integration's discretion if it is a first time sync). Objects should be processed in batches which can be done using the ``RequestDAO::getSyncIteration()``. The sync engine executes ``SyncDataExchangeInterface::getSyncReport()`` until a Report comes back with no objects.

If the Integration supports field level change tracking, it should tell the Report so that the sync engine can merge the two data sets more accurately.

See :xref:`ReportBuilder`.


Executing the sync order
________________________

The sync order contains all the changes the sync engine has determined should be written to the Integration. The Integration should communicate back the ID of any objects created or adjust objects as needed such as if they were converted from one to another or deleted.

See :xref:`OrderExecutioner`.