.. It is a reference only page, not a part of doc tree.

:orphan:

.. vale off

Sync Engine
###########

.. vale on

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

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

Sync events
===========

The IntegrationsBundle dispatches events during a sync so a Plugin can act on Contact and Company data or on the results of each sync batch. Mautic dispatches each event by its class name, so key ``getSubscribedEvents()`` on the event class, such as ``InternalContactFieldChangesEvent::class``. All the classes are in the ``Mautic\IntegrationsBundle\Event`` namespace.

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Event class
     - When Mautic dispatches it
   * - ``InternalContactFieldChangesEvent``
     - Before Mautic stores a Contact's field changes in the ``sync_object_field_change_report`` table
   * - ``InternalCompanyFieldChangesEvent``
     - Before Mautic stores a Company's field changes in the ``sync_object_field_change_report`` table
   * - ``InternalContactFullReportBuildEvent``
     - Before the Sync Engine adds a Contact to a full object Report
   * - ``InternalCompanyFullReportBuildEvent``
     - Before the Sync Engine adds a Company to a full object Report
   * - ``IntegrationToMauticSyncCompletedEvent``
     - After the Sync Engine finishes processing a batch of objects synced from the Integration to Mautic
   * - ``MauticToIntegrationSyncCompletedEvent``
     - After the Sync Engine finishes processing a batch of objects synced from Mautic to the Integration

Each event class extends an abstract base class that provides its methods:

* The Contact events extend ``InternalContactEvent``, which provides ``getIntegrationName()`` and ``getContact()``.
* The Company events extend ``InternalCompanyEvent``, which provides ``getIntegrationName()`` and ``getCompany()``.
* The sync completed events extend ``CompletedSyncIterationEvent``, which provides ``getIntegration()``, ``getOrderResults()``, ``getIteration()``, ``getInputOptions()``, and ``getMappingManual()``. Use these to act on the object mappings the batch stored in the ``sync_object_mapping`` table.

A listener method can type-hint the base class to handle both events that share it, but subscribe to each concrete event class separately.

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/EventListener/SyncSubscriber.php

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Mautic\IntegrationsBundle\Event\InternalContactEvent;
    use Mautic\IntegrationsBundle\Event\InternalContactFieldChangesEvent;
    use Mautic\IntegrationsBundle\Event\InternalContactFullReportBuildEvent;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    final class SyncSubscriber implements EventSubscriberInterface
    {
        public static function getSubscribedEvents(): array
        {
            return [
                InternalContactFieldChangesEvent::class    => 'onContactEvent',
                InternalContactFullReportBuildEvent::class => 'onContactEvent',
            ];
        }

        public function onContactEvent(InternalContactEvent $event): void
        {
            if ('HelloWorld' !== $event->getIntegrationName()) {
                return;
            }

            $contact = $event->getContact();
            // ...
        }
    }

.. note::

   Mautic 8 removed the matching constants from ``Mautic\IntegrationsBundle\IntegrationEvents``, so code that still references one raises an undefined-constant error. Replace each constant with its event class:

   * ``INTEGRATION_BEFORE_CONTACT_FIELD_CHANGES`` - ``InternalContactFieldChangesEvent``
   * ``INTEGRATION_BEFORE_COMPANY_FIELD_CHANGES`` - ``InternalCompanyFieldChangesEvent``
   * ``INTEGRATION_BEFORE_FULL_CONTACT_REPORT_BUILD`` - ``InternalContactFullReportBuildEvent``
   * ``INTEGRATION_BEFORE_FULL_COMPANY_REPORT_BUILD`` - ``InternalCompanyFullReportBuildEvent``
   * ``INTEGRATION_BATCH_SYNC_COMPLETED_INTEGRATION_TO_MAUTIC`` - ``IntegrationToMauticSyncCompletedEvent``
   * ``INTEGRATION_BATCH_SYNC_COMPLETED_MAUTIC_TO_INTEGRATION`` - ``MauticToIntegrationSyncCompletedEvent``

   For how class-name dispatch works, see :ref:`Mautic 8 class-name event dispatch <Mautic 8 class-name event dispatch>`.
