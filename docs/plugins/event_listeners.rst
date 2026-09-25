.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Event listeners
###############

.. vale off

Mautic leverages Symfony's EventDispatcher to execute and communicate various actions through Mautic. Plugins can hook into these to extend Mautic's capabilities. Refer to the :doc:`Extending Mautic <../components/api>` section of the documentation for some of the ways to do this.

.. vale on

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/EventListener/LeadSubscriber.php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Mautic\LeadBundle\Event\LeadPostDeleteEvent;
    use Mautic\LeadBundle\Event\LeadPostSaveEvent;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    final class LeadSubscriber implements EventSubscriberInterface
    {
        public static function getSubscribedEvents(): array
        {
            return [
                LeadPostSaveEvent::class   => ['onLeadPostSave', 0],
                LeadPostDeleteEvent::class => ['onLeadDelete', 0],
            ];
        }

        public function onLeadPostSave(LeadPostSaveEvent $event): void
        {
            $lead = $event->getLead();

            // do something
        }

        public function onLeadDelete(LeadPostDeleteEvent $event): void
        {
            $lead = $event->getLead();

            $deletedId = $lead->deletedId;

            // do something
        }
    }

Event subscribers
*****************

The easiest way to listen to various events is to use an event subscriber. Read more about :xref:`Symfony event subscribers` in Symfony's documentation.

.. vale off

Plugin event subscribers can extend ``Symfony\Component\EventDispatcher\EventSubscriberInterface``, which gives access to commonly used dependencies and also allows registering the subscriber service through autowiring.

.. vale on
    
Available events
****************

There are many events available throughout Mautic. Depending on what you're trying to implement, look at the ``*Event.php`` for the core bundle, located in the root of the bundle. For example, the ``app\bundles\LeadBundle\LeadEvents.php`` file defines and describes events relating to Contacts. The final classes provide the names of the events to listen to. Always use the event constants to ensure future changes to event names won't break the Plugin.

Custom events
*************

A Plugin can create and dispatch its own events. 

Custom events require the following:

#. The class defines the available events for the Plugin using a ``final class`` with constants.

   .. code-block:: php

       <?php
       // plugins\HelloWorldBundle\HelloWorldEvents.php
    
       namespace MauticPlugin\HelloWorldBundle;
    
       final class HelloWorldEvents
       {
           /**
            * The giant meteor that dooms a world triggers the helloworld.armageddon event
            *
            * The event listener receives a MauticPlugin\HelloWorldBundle\Event\ArmageddonEvent instance.
            *
            * @var string
            */
           const ARMAGEDDON = 'helloworld.armageddon';
       }
       // ...


#. The listeners receive the ``Event`` class. This class should extend ``Symfony\Contracts\EventDispatcher\Event``. The event object contains all data required for listeners to process the event.

   .. code-block:: php

       <?php  
    // plugins\HelloWorldBundle\Event\ArmageddonEvent.php  
    
       namespace MauticPlugin\HelloWorldBundle\Event;  
    
       use Symfony\Contracts\EventDispatcher\Event;  
       use MauticPlugin\HelloWorldBundle\Entity\World;  
    
       final class ArmageddonEvent extends Event  
       {  
           private bool $falseAlarm = false;  
         
           public function __construct(private World $world)
           {  
               $this->world = $world;
           }  
        
           public function shouldPanic(): bool  
           {  
               return ('earth' == $this->world->getName());  
           }  
        
           public function setIsFalseAlarm(): void  
           {  
               $this->falseAlarm = true;  
           }  
        
           public function getIsFalseAlarm(): bool  
           {  
               return $this->falseAlarm;  
           }  
       }
       // ...


#. The code that dispatches the event where appropriate using the ``event_dispatcher`` service.

   .. code-block:: php

       <?php
    
       $dispatcher = $this->get('event_dispatcher');
       if ($dispatcher->hasListeners   (HelloWorldEvents::ARMAGEDDON)) {
           $event = $dispatcher->dispatch(HelloWorldEvents::ARMAGEDDON, new ArmageddonEvent($world));

           if ($event->shouldPanic()) {
               throw new \Exception("Run for the hills!");
           }
       }

.. _leadbundle events dispatched by event class:

.. vale off

LeadBundle events dispatched by event class
*******************************************

.. vale on

Since Mautic 8, Mautic dispatches the LeadBundle events for Contacts, Companies, Segments, Custom Fields, Tags, notes, devices, imports, and Contact exports by their event class instead of a ``LeadEvents`` string constant. Key ``getSubscribedEvents()`` on ``EventClass::class``. All the event classes below live in the ``Mautic\LeadBundle\Event`` namespace.

Where several ``LeadEvents`` constants used to share one event class, each event now has its own subclass of that shared class. For example, ``LeadPreSaveEvent`` and ``LeadPostSaveEvent`` both extend ``LeadEvent``. Listener methods that type-hint the former shared class keep working.

Mautic 8 keeps these ``LeadEvents`` constants because their string values remain the Webhook event type identifiers. Mautic no longer dispatches events under these names, so a subscriber still keyed on one of these constants silently stops receiving the event - no error, no log entry. Re-key it on the event class:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Kept ``LeadEvents`` constant
     - Event class to subscribe to
   * - ``LEAD_POST_SAVE``
     - ``LeadPostSaveEvent``
   * - ``LEAD_POST_DELETE``
     - ``LeadPostDeleteEvent``
   * - ``LEAD_POINTS_CHANGE``
     - ``PointsChangeEvent``
   * - ``LEAD_COMPANY_CHANGE``
     - ``LeadChangeCompanyEvent``
   * - ``LEAD_LIST_CHANGE``
     - ``ListChangeEvent``
   * - ``COMPANY_POST_SAVE``
     - ``CompanyPostSaveEvent``
   * - ``COMPANY_POST_DELETE``
     - ``CompanyPostDeleteEvent``

Mautic 8 removes these ``LeadEvents`` constants. Code that still references one of them throws a PHP fatal error - ``Error: Undefined constant``. Subscribe to the event class instead:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Removed ``LeadEvents`` constant
     - Event class to subscribe to
   * - ``LEAD_PRE_SAVE``
     - ``LeadPreSaveEvent``
   * - ``LEAD_PRE_DELETE``
     - ``LeadPreDeleteEvent``
   * - ``LEAD_PRE_MERGE``
     - ``LeadPreMergeEvent``
   * - ``LEAD_POST_MERGE``
     - ``LeadPostMergeEvent``
   * - ``LEAD_IDENTIFIED``
     - ``LeadIdentifiedEvent``
   * - ``LEAD_LIST_BATCH_CHANGE``
     - ``ListBatchChangeEvent``
   * - ``LEAD_PRE_BATCH_SAVE``
     - ``LeadPreBatchSaveEvent``
   * - ``LEAD_POST_BATCH_SAVE``
     - ``LeadPostBatchSaveEvent``
   * - ``CURRENT_LEAD_CHANGED``
     - ``LeadChangeEvent``
   * - ``LIST_PRE_SAVE``
     - ``ListPreSaveEvent``
   * - ``LIST_POST_SAVE``
     - ``ListPostSaveEvent``
   * - ``LIST_PRE_UNPUBLISH``
     - ``ListPreUnpublishEvent``
   * - ``LIST_PRE_DELETE``
     - ``ListPreDeleteEvent``
   * - ``ON_LIST_DELETE``
     - ``ListDeleteEvent``
   * - ``LIST_POST_DELETE``
     - ``ListPostDeleteEvent``
   * - ``FIELD_PRE_SAVE``
     - ``FieldPreSaveEvent``
   * - ``FIELD_POST_SAVE``
     - ``FieldPostSaveEvent``
   * - ``FIELD_PRE_DELETE``
     - ``FieldPreDeleteEvent``
   * - ``FIELD_POST_DELETE``
     - ``FieldPostDeleteEvent``
   * - ``NOTE_PRE_SAVE``
     - ``NotePreSaveEvent``
   * - ``NOTE_POST_SAVE``
     - ``NotePostSaveEvent``
   * - ``NOTE_PRE_DELETE``
     - ``NotePreDeleteEvent``
   * - ``NOTE_POST_DELETE``
     - ``NotePostDeleteEvent``
   * - ``IMPORT_PRE_SAVE``
     - ``ImportPreSaveEvent``
   * - ``IMPORT_POST_SAVE``
     - ``ImportPostSaveEvent``
   * - ``IMPORT_PRE_DELETE``
     - ``ImportPreDeleteEvent``
   * - ``IMPORT_POST_DELETE``
     - ``ImportPostDeleteEvent``
   * - ``IMPORT_BATCH_PROCESSED``
     - ``ImportBatchProcessedEvent``
   * - ``DEVICE_PRE_SAVE``
     - ``DevicePreSaveEvent``
   * - ``DEVICE_POST_SAVE``
     - ``DevicePostSaveEvent``
   * - ``DEVICE_PRE_DELETE``
     - ``DevicePreDeleteEvent``
   * - ``DEVICE_POST_DELETE``
     - ``DevicePostDeleteEvent``
   * - ``TAG_PRE_SAVE``
     - ``TagPreSaveEvent``
   * - ``TAG_POST_SAVE``
     - ``TagPostSaveEvent``
   * - ``TAG_PRE_DELETE``
     - ``TagPreDeleteEvent``
   * - ``TAG_POST_DELETE``
     - ``TagPostDeleteEvent``
   * - ``TAG_PRE_MERGE``
     - ``TagPreMergeEvent``
   * - ``TAG_POST_MERGE``
     - ``TagPostMergeEvent``
   * - ``COMPANY_PRE_SAVE``
     - ``CompanyPreSaveEvent``
   * - ``COMPANY_PRE_DELETE``
     - ``CompanyPreDeleteEvent``
   * - ``COMPANY_SOFT_DELETE``
     - ``CompanySoftDeleteEvent``
   * - ``COMPANY_PRE_MERGE``
     - ``CompanyPreMergeEvent``
   * - ``COMPANY_POST_MERGE``
     - ``CompanyPostMergeEvent``
   * - ``LIST_FILTERS_CHOICES_ON_GENERATE``
     - ``LeadListFiltersChoicesEvent``
   * - ``SEGMENT_DICTIONARY_ON_GENERATE``
     - ``SegmentDictionaryGenerationEvent``
   * - ``LIST_FILTERS_ON_FILTERING``
     - ``LeadListFilteringEvent``
   * - ``LIST_PRE_PROCESS_LIST``
     - ``ListPreProcessListEvent``
   * - ``ON_CLICKTHROUGH_IDENTIFICATION``
     - ``ContactIdentificationEvent``
   * - ``POST_CONTACT_EXPORT``
     - ``ContactExportEvent``
   * - ``POST_CONTACT_EXPORT_SCHEDULED``
     - ``ContactExportScheduledEvent``
   * - ``CONTACT_EXPORT_PREPARE_FILE``
     - ``ContactExportPrepareFileEvent``
   * - ``CONTACT_EXPORT_SEND_EMAIL``
     - ``ContactExportSendEmailEvent``
   * - ``POST_CONTACT_EXPORT_SEND_EMAIL``
     - ``ContactExportEmailSentEvent``

Mautic 8 also changes how these events behave for code that creates or reads them:

* Mautic 8 makes 12 former shared classes ``abstract``: ``CompanyEvent``, ``CompanyMergeEvent``, ``ContactExportSchedulerEvent``, ``ImportEvent``, ``LeadDeviceEvent``, ``LeadFieldEvent``, ``LeadListEvent``, ``LeadMergeEvent``, ``LeadNoteEvent``, ``SaveBatchLeadsEvent``, ``TagEvent``, and ``TagMergeEvent``. If your Plugin creates one of these events with ``new``, create the matching subclass from the preceding tables instead. ``LeadEvent`` and ``ListChangeEvent`` are no longer ``final``, and Mautic still dispatches them directly.
* The event Mautic dispatches before a save, delete, or merge and the event it dispatches afterward are now separate objects. A value that a listener sets on the earlier event isn't available to listeners of the later one.
* ``Mautic\LeadBundle\Field\Dispatcher\FieldSaveDispatcher::dispatchEvent()`` now takes the ``LeadFieldEvent`` subclass to dispatch, instead of an event name, the field entity, and an ``isNew`` flag.

For the full list of Mautic 8 changes, see :xref:`UPGRADE_GUIDE_8`.

Tag merge events
****************

Mautic dispatches events when two Tags merge. Use these events to sync Tag changes to external systems, log merge operations, or trigger custom business logic.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Event class
     - Description
   * - ``Mautic\LeadBundle\Event\TagPreMergeEvent``
     - Dispatched before two Tags merge.
   * - ``Mautic\LeadBundle\Event\TagPostMergeEvent``
     - Dispatched after two Tags merge.

Both event classes extend ``Mautic\LeadBundle\Event\TagMergeEvent`` and provide the following methods:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Method
     - Description
   * - ``getPrimaryTag()``
     - Returns the Tag entity that remains after the merge.
   * - ``getSecondaryTag()``
     - Returns the Tag entity that merges into the primary Tag and then gets deleted.

Example subscriber
==================

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/EventListener/TagMergeSubscriber.php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Mautic\LeadBundle\Event\TagPostMergeEvent;
    use Mautic\LeadBundle\Event\TagPreMergeEvent;
    use Psr\Log\LoggerInterface;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    final class TagMergeSubscriber implements EventSubscriberInterface
    {
        public function __construct(private LoggerInterface $logger)
        {
        }

        public static function getSubscribedEvents(): array
        {
            return [
                TagPreMergeEvent::class  => ['onTagPreMerge', 0],
                TagPostMergeEvent::class => ['onTagPostMerge', 0],
            ];
        }

        public function onTagPreMerge(TagPreMergeEvent $event): void
        {
            $primaryTag   = $event->getPrimaryTag();
            $secondaryTag = $event->getSecondaryTag();

            $this->logger->info(sprintf(
                'About to merge tag "%s" into "%s"',
                $secondaryTag->getTag(),
                $primaryTag->getTag()
            ));
        }

        public function onTagPostMerge(TagPostMergeEvent $event): void
        {
            $primaryTag   = $event->getPrimaryTag();
            $secondaryTag = $event->getSecondaryTag();

            $this->logger->info(sprintf(
                'Tag "%s" merged into "%s"',
                $secondaryTag->getTag(),
                $primaryTag->getTag()
            ));

            // Sync to external CRM, analytics platform, etc.
        }
    }
