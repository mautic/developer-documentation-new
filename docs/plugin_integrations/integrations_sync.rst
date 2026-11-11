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

To tell the IntegrationsBundle that this Integration provides a syncing feature, register the Integration or support class as a service in the Plugin's ``Config/services.php`` and tag it with ``mautic.sync_integration``.

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/Config/services.php

    declare(strict_types=1);

    use Mautic\CoreBundle\DependencyInjection\MauticCoreExtension;
    use Symfony\Component\DependencyInjection\Loader\Configurator\ContainerConfigurator;

    return function (ContainerConfigurator $configurator): void {
        $services = $configurator->services()
            ->defaults()
            ->autowire()
            ->autoconfigure()
            ->public();

        $services->load('MauticPlugin\\HelloWorldBundle\\', '../')
            ->exclude('../{'.implode(',', MauticCoreExtension::DEFAULT_EXCLUDES).'}');

        $services->set(\MauticPlugin\HelloWorldBundle\Integration\Support\SyncSupport::class)
            ->tag('mautic.sync_integration');
    };

The ``SyncSupport`` class must implement::

        \Mautic\IntegrationsBundle\Integration\Interfaces\SyncInterface.

Syncing
*******

The mapping manual
==================

The mapping manual tells the Sync Engine which Integration should sync with which Mautic object like Contact or Company, the Integration fields. These fields should get mapped to Mautic fields, and the direction in the data suppose to flow.

``SyncInterface::getMappingManual()`` returns the mapping manual as a ``MappingManualDAO``. Pass each ``ObjectMappingDAO`` to the ``MappingManualDAO`` constructor. This example maps the Integration's ``citizen`` object to the Mautic Contact object and its ``world`` object to the Mautic Company object.

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/Sync/Mapping/Manual/MappingManualFactory.php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\Sync\Mapping\Manual;

    use Mautic\IntegrationsBundle\Sync\DAO\Mapping\MappingManualDAO;
    use Mautic\IntegrationsBundle\Sync\DAO\Mapping\ObjectMappingDAO;
    use Mautic\IntegrationsBundle\Sync\SyncDataExchange\Internal\Object\Company;
    use Mautic\IntegrationsBundle\Sync\SyncDataExchange\Internal\Object\Contact;
    use MauticPlugin\HelloWorldBundle\Integration\HelloWorldIntegration;

    final class MappingManualFactory
    {
        public const string CITIZEN_OBJECT = 'citizen';
        public const string WORLD_OBJECT   = 'world';

        public function getManual(): MappingManualDAO
        {
            // This example hardcodes the field mappings. Build them from the Integration's
            // saved field mapping configuration when users can change them.
            $citizenMapping = new ObjectMappingDAO(Contact::NAME, self::CITIZEN_OBJECT);

            // Arguments: Mautic field alias, Integration field name, sync direction, required
            $citizenMapping->addFieldMapping('email', 'email_address', ObjectMappingDAO::SYNC_BIDIRECTIONALLY, true);
            $citizenMapping->addFieldMapping('firstname', 'first_name');
            $citizenMapping->addFieldMapping('lastname', 'last_name', ObjectMappingDAO::SYNC_TO_MAUTIC);

            $worldMapping = new ObjectMappingDAO(Company::NAME, self::WORLD_OBJECT);
            $worldMapping->addFieldMapping('companyname', 'name', ObjectMappingDAO::SYNC_BIDIRECTIONALLY, true);

            return new MappingManualDAO(HelloWorldIntegration::NAME, [$citizenMapping, $worldMapping]);
        }
    }

``addFieldMapping()`` syncs a field in both directions by default. To sync a field in one direction only, pass ``ObjectMappingDAO::SYNC_TO_MAUTIC`` or ``ObjectMappingDAO::SYNC_TO_INTEGRATION`` as the direction.

The sync data exchange
======================

This is where the sync takes place, and the ``mautic:integrations:sync``  executes it. Mautic and the Integration build their respective Reports of new or modified objects, then execute the order from the other side.

``SyncInterface::getSyncDataExchange()`` returns a class that implements ``SyncDataExchangeInterface``. This example delegates building the Report to ``ReportBuilder`` and executing the Sync Order to ``OrderExecutioner``, which the following sections show.

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/Sync/DataExchange/SyncDataExchange.php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\Sync\DataExchange;

    use Mautic\IntegrationsBundle\Sync\DAO\Sync\Order\OrderDAO;
    use Mautic\IntegrationsBundle\Sync\DAO\Sync\Report\ReportDAO;
    use Mautic\IntegrationsBundle\Sync\DAO\Sync\Request\RequestDAO;
    use Mautic\IntegrationsBundle\Sync\SyncDataExchange\SyncDataExchangeInterface;

    final readonly class SyncDataExchange implements SyncDataExchangeInterface
    {
        public function __construct(
            private ReportBuilder $reportBuilder,
            private OrderExecutioner $orderExecutioner,
        ) {
        }

        public function getSyncReport(RequestDAO $requestDAO): ReportDAO
        {
            return $this->reportBuilder->build($requestDAO);
        }

        public function executeSyncOrder(OrderDAO $syncOrderDAO): void
        {
            $this->orderExecutioner->execute($syncOrderDAO);
        }
    }

.. vale off

Building Sync Report
____________________

.. vale on

The Sync Report tells the Sync Engine what objects are new and/or modified between the two timestamps given by the engine. It's up to the Integration's discretion if it's a first-time sync. Objects should process in batches and ``RequestDAO::getSyncIteration()`` takes care of this batching. The Sync Engine executes ``SyncDataExchangeInterface::getSyncReport()`` until a Report comes back with no objects.

If the Integration supports field level change tracking, it should tell the Report so that the Sync Engine can merge the two data sets more accurately.

This example fetches one batch of modified objects from the Integration for each sync iteration. ``Client`` stands in for the Plugin's own API client, so its methods and response format are placeholders.

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/Sync/DataExchange/ReportBuilder.php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\Sync\DataExchange;

    use Mautic\IntegrationsBundle\Sync\DAO\Sync\Report\FieldDAO;
    use Mautic\IntegrationsBundle\Sync\DAO\Sync\Report\ObjectDAO;
    use Mautic\IntegrationsBundle\Sync\DAO\Sync\Report\ReportDAO;
    use Mautic\IntegrationsBundle\Sync\DAO\Sync\Request\RequestDAO;
    use Mautic\IntegrationsBundle\Sync\DAO\Value\NormalizedValueDAO;
    use Mautic\IntegrationsBundle\Sync\ValueNormalizer\ValueNormalizer;
    use MauticPlugin\HelloWorldBundle\Connection\Client;
    use MauticPlugin\HelloWorldBundle\Integration\HelloWorldIntegration;

    final class ReportBuilder
    {
        private readonly ValueNormalizer $valueNormalizer;

        public function __construct(
            private readonly Client $client, // Placeholder for the Plugin's API client
        ) {
            $this->valueNormalizer = new ValueNormalizer();
        }

        public function build(RequestDAO $requestDAO): ReportDAO
        {
            $report = new ReportDAO(HelloWorldIntegration::NAME);

            foreach ($requestDAO->getObjects() as $requestedObject) {
                // Placeholder API call that returns one batch of objects created or modified
                // between the two dates, for example:
                // [['id' => 42, 'last_modified' => '2020-01-01T10:00:00+00:00', 'fields' => [...], 'field_changes' => [...]]]
                $items = $this->client->getModifiedObjects(
                    $requestedObject->getObject(),
                    $requestedObject->getFromDateTime(),
                    $requestedObject->getToDateTime(),
                    $requestDAO->getSyncIteration()
                );

                foreach ($items as $item) {
                    // The object's ID in the Integration and when the object last changed
                    $objectDAO = new ObjectDAO(
                        $requestedObject->getObject(),
                        $item['id'],
                        new \DateTimeImmutable($item['last_modified'])
                    );

                    // getFields() returns the Integration field names the mapping manual syncs to Mautic
                    foreach ($requestedObject->getFields() as $fieldName) {
                        if (!array_key_exists($fieldName, $item['fields'])) {
                            continue;
                        }

                        // Use the NormalizedValueDAO type constant that matches the field, such as INT_TYPE or DATETIME_TYPE
                        $value    = $this->valueNormalizer->normalizeForMautic(NormalizedValueDAO::STRING_TYPE, $item['fields'][$fieldName]);
                        $fieldDAO = new FieldDAO($fieldName, $value);

                        // With field level change tracking, record when this field last changed
                        if (isset($item['field_changes'][$fieldName])) {
                            $fieldDAO->setChangeDateTime(new \DateTimeImmutable($item['field_changes'][$fieldName]));
                        }

                        $objectDAO->addField($fieldDAO);
                    }

                    $report->addObject($objectDAO);
                }
            }

            // An empty Report ends the sync, so return no objects once the Integration has no more batches
            return $report;
        }
    }

.. vale off

Executing the Sync Order
________________________

.. vale on

The Sync Order contains all the changes the Sync Engine has determined, and these should inform the Integration. The Integration should communicate back the ID of any objects created or adjust objects as needed, such as if they get converted from one to another or deleted.

This example sends each changed object to the Integration, then records the result for that object on the ``OrderDAO``.

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/Sync/DataExchange/OrderExecutioner.php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\Sync\DataExchange;

    use Mautic\IntegrationsBundle\Sync\DAO\Sync\Order\ObjectChangeDAO;
    use Mautic\IntegrationsBundle\Sync\DAO\Sync\Order\OrderDAO;
    use Mautic\IntegrationsBundle\Sync\ValueNormalizer\ValueNormalizer;
    use MauticPlugin\HelloWorldBundle\Connection\Client;

    final class OrderExecutioner
    {
        private readonly ValueNormalizer $valueNormalizer;

        public function __construct(
            private readonly Client $client, // Placeholder for the Plugin's API client
        ) {
            $this->valueNormalizer = new ValueNormalizer();
        }

        public function execute(OrderDAO $orderDAO): void
        {
            // Identified objects already exist in the Integration. Unidentified objects have no
            // mapping yet, so the Integration might need to create them.
            foreach ([$orderDAO->getIdentifiedObjects(), $orderDAO->getUnidentifiedObjects()] as $objectsByName) {
                foreach ($objectsByName as $objectChanges) {
                    foreach ($objectChanges as $objectChange) {
                        $this->syncObject($orderDAO, $objectChange);
                    }
                }
            }
        }

        private function syncObject(OrderDAO $orderDAO, ObjectChangeDAO $objectChange): void
        {
            // getFields() returns the changed fields and the required fields
            $payload = [];
            foreach ($objectChange->getFields() as $field) {
                $payload[$field->getName()] = $this->valueNormalizer->normalizeForIntegration($field->getValue());
            }

            // Placeholder API call that updates the object, or creates it when the ID is empty
            $response = $this->client->upsert($objectChange->getObject(), $objectChange->getObjectId(), $payload);

            switch ($response['code']) {
                case 200:
                    // Updated, so record the sync date
                    $orderDAO->updateLastSyncDate($objectChange);
                    break;
                case 201:
                    // Created, so map the new Integration object to the Mautic object
                    $orderDAO->addObjectMapping($objectChange, $objectChange->getObject(), $response['id']);
                    break;
                case 404:
                    // Deleted in the Integration, so stop syncing the object
                    $orderDAO->deleteObject($objectChange);
                    break;
                case 503:
                    // Temporary failure, so keep the Mautic changes for the next sync
                    $orderDAO->retrySyncLater($objectChange);
                    break;
                default:
                    // Report the failure as a sync issue without retrying it
                    $orderDAO->noteObjectSyncIssue($objectChange, $response['message'] ?? 'Unknown error');
            }

            // If the Integration converted the object to another object type, call
            // $orderDAO->remapObject() with the old and new object names and IDs.
        }
    }

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
