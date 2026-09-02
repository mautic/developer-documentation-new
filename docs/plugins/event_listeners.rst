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
    //plugins\HelloWorldBundle\EventListener\LeadSubscriber

    namespace MauticPlugin\HelloWorldBundle\EventListener;  

    use Mautic\LeadBundle\LeadEvent;  
    use Mautic\LeadBundle\LeadEvents;  
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;  

    final class LeadSubscriber extends EventSubscriberInterface  
    {  
        static public function getSubscribedEvents(): array  
        {  
            return [  
                LeadEvents::LEAD_POST_SAVE     => ['onLeadPostSave', 0],  
                LeadEvents::LEAD_POST_DELETE   => ['onLeadDelete', 0],  
            ];  
        }  
    
        public function onLeadPostSave(LeadEvent $event): void  
        {  
            $lead = $event->getLead();  
            
            // do something  
        }  
    
        public function onLeadDelete(LeadEvent $event): void  
        {  
            $lead = $event->getLead();  
            
            $deletedId = $lead->deletedId;  
            
            // do something  
        }  
    }  
    // ...

Event subscribers
*****************

The easiest way to listen to various events is to use an event subscriber. Read more about :xref:`Symfony event subscribers` in Symfony's documentation.

.. vale off

Plugin event subscribers can extend ``Symfony\Component\EventDispatcher\EventSubscriberInterface``, which gives access to commonly used dependencies and also allows registering the subscriber service through autowiring.

.. vale on
    
Available events
****************

There are many events available throughout Mautic. Depending on what you're trying to implement, look at the ``*Event.php`` for the core bundle, located in the root of the bundle. For example, the ``app\bundles\LeadBundle\LeadEvents.php`` file defines and describes events relating to Contacts. The final classes provide the names of the events to listen to. Always use the event constants to ensure future changes to event names won't break the Plugin.

.. note::

   This section is current for Mautic 8. Starting in Mautic 8, Mautic dispatches the LeadBundle events listed below by their event object, following the Symfony 4.3+ convention, so the identifier you subscribe to is the event class (``EventClass::class``) rather than the ``LeadEvents::*`` string constant. The constants remain defined in Mautic 8, so referencing one won't cause a fatal error. However, any listener still registered under the old event name receives nothing. This affects a subscriber whose ``getSubscribedEvents()`` still keys on one of these converted constants (or on the raw ``mautic.*`` string), and it equally affects a service tagged ``kernel.event_listener`` whose ``event`` attribute is the old ``mautic.*`` string, which is the value of the ``LeadEvents::*`` constant. The root cause is the same in both cases: Mautic 8 dispatches by the event object, so the event name is now the class name, and anything still registered under the old string name matches no listener. It produces no error and writes no log entry, because the dispatcher finds no listener registered under the class-name event. Re-key each affected subscriber or tagged listener on the event class so it receives the event again. This qualifies the preceding guidance to always use the event constants: that guidance still holds for the events that weren't converted, but for the events in this section you subscribe to the event class instead. This class-name dispatch conversion isn't limited to the LeadBundle: other bundles, such as the CoreBundle, converted their events the same way in Mautic 8, so a subscriber to another bundle's events should check the corresponding ``*Events`` class for that bundle too.

LeadBundle events dispatched by class name in Mautic 8
======================================================

.. list-table::
   :header-rows: 1
   :widths: 34 33 33

   * - Old event name
     - ``LeadEvents`` constant
     - New event class
   * - ``mautic.lead_utmtags_add``
     - ``LEAD_UTMTAGS_ADD``
     - ``LeadUtmTagsEvent``
   * - ``mautic.lead_category_change``
     - ``LEAD_CATEGORY_CHANGE``
     - ``CategoryChangeEvent``
   * - ``mautic.lead_channel_subscription_changed``
     - ``CHANNEL_SUBSCRIPTION_CHANGED``
     - ``ChannelSubscriptionChange``
   * - ``mautic.lead_build_search_commands``
     - ``LEAD_BUILD_SEARCH_COMMANDS``
     - ``LeadBuildSearchEvent``
   * - ``mautic.company_build_search_commands``
     - ``COMPANY_BUILD_SEARCH_COMMANDS``
     - ``CompanyBuildSearchEvent``
   * - ``mautic.adjust_filter_form_type_for_field``
     - ``ADJUST_FILTER_FORM_TYPE_FOR_FIELD``
     - ``FormAdjustmentEvent``
   * - ``mautic.collect_operators_for_field_type``
     - ``COLLECT_OPERATORS_FOR_FIELD_TYPE``
     - ``TypeOperatorsEvent``
   * - ``mautic.collect_operators_for_field``
     - ``COLLECT_OPERATORS_FOR_FIELD``
     - ``FieldOperatorsEvent``
   * - ``mautic.collect_filter_choices_for_list_field_type``
     - ``COLLECT_FILTER_CHOICES_FOR_LIST_FIELD_TYPE``
     - ``ListFieldChoicesEvent``
   * - ``mautic.list_filters_delegate_decorator``
     - ``SEGMENT_ON_DECORATOR_DELEGATE``
     - ``LeadListFiltersDecoratorDelegateEvent``
   * - ``mautic.list_filters_merge``
     - ``LIST_FILTERS_MERGE``
     - ``LeadListMergeFiltersEvent``
   * - ``mautic.list_filters_operators_on_generate``
     - ``LIST_FILTERS_OPERATORS_ON_GENERATE``
     - ``LeadListFiltersOperatorsEvent``
   * - ``mautic.list_filters_operator_querybuilder_on_generate``
     - ``LIST_FILTERS_OPERATOR_QUERYBUILDER_ON_GENERATE``
     - ``SegmentOperatorQueryBuilderEvent``
   * - ``mautic.list_filters_querybuilder_generated``
     - ``LIST_FILTERS_QUERYBUILDER_GENERATED``
     - ``LeadListQueryBuilderGeneratedEvent``
   * - ``mautic.lead_import_on_initialize``
     - ``IMPORT_ON_INITIALIZE``
     - ``ImportInitEvent``
   * - ``mautic.lead_import_on_field_mapping``
     - ``IMPORT_ON_FIELD_MAPPING``
     - ``ImportMappingEvent``
   * - ``mautic.lead_import_on_process``
     - ``IMPORT_ON_PROCESS``
     - ``ImportProcessEvent``
   * - ``mautic.lead_import_on_validate``
     - ``IMPORT_ON_VALIDATE``
     - ``ImportValidateEvent``
   * - ``mautic.lead_field_pre_add_column``
     - ``LEAD_FIELD_PRE_ADD_COLUMN``
     - ``AddColumnEvent``
   * - ``mautic.lead_field_pre_add_column_background_job``
     - ``LEAD_FIELD_PRE_ADD_COLUMN_BACKGROUND_JOB``
     - ``AddColumnBackgroundEvent``
   * - ``mautic.lead_field_pre_update_column``
     - ``LEAD_FIELD_PRE_UPDATE_COLUMN``
     - ``UpdateColumnEvent``
   * - ``mautic.lead_field_pre_update_column_background_job``
     - ``LEAD_FIELD_PRE_UPDATE_COLUMN_BACKGROUND_JOB``
     - ``UpdateColumnBackgroundEvent``
   * - ``mautic.lead_field_pre_delete_column``
     - ``LEAD_FIELD_PRE_DELETE_COLUMN``
     - ``DeleteColumnEvent``
   * - ``mautic.lead_field_pre_delete_column_background_job``
     - ``LEAD_FIELD_PRE_DELETE_COLUMN_BACKGROUND_JOB``
     - ``DeleteColumnBackgroundEvent``

The six field-column classes (``AddColumnEvent``, ``AddColumnBackgroundEvent``, ``UpdateColumnEvent``, ``UpdateColumnBackgroundEvent``, ``DeleteColumnEvent``, and ``DeleteColumnBackgroundEvent``) live in the ``Mautic\LeadBundle\Field\Event`` namespace, while the other 18 live in the ``Mautic\LeadBundle\Event`` namespace.

``CHANNEL_SUBSCRIPTION_CHANGED`` is the one exception to watch: its event dispatch and subscription move to the ``ChannelSubscriptionChange`` event class, but its string value ``mautic.lead_channel_subscription_changed`` remains the Webhook type identifier, so Webhook configuration and receivers are unaffected; only your event-subscription code needs to change.

These illustrative fragments show the change inside an existing subscriber's ``getSubscribedEvents()`` method, using the ``LEAD_BUILD_SEARCH_COMMANDS`` event. Before Mautic 8, the subscriber keys on the constant:

.. code-block:: php

    <?php

    use Mautic\LeadBundle\LeadEvents;

    public static function getSubscribedEvents(): array
    {
        return [
            LeadEvents::LEAD_BUILD_SEARCH_COMMANDS => ['onBuildSearchCommands', 0],
        ];
    }

In Mautic 8, the subscriber keys on the event class:

.. code-block:: php

    <?php

    use Mautic\LeadBundle\Event\LeadBuildSearchEvent;

    public static function getSubscribedEvents(): array
    {
        return [
            LeadBuildSearchEvent::class => ['onBuildSearchCommands', 0],
        ];
    }

.. tip::

   To see which listeners are registered for an event, run the Symfony console command ``bin/console debug:event-dispatcher``, optionally passing the event class to list only that event's listeners. Run it before and after re-keying a subscriber to confirm the subscriber is registered under the new event-class name.

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

Tag merge events
****************

Mautic dispatches events when two Tags merge. Use these events to sync Tag changes to external systems, log merge operations, or trigger custom business logic.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Event constant
     - Description
   * - ``LeadEvents::TAG_PRE_MERGE``
     - Dispatched before two Tags merge. The event string is ``mautic.lead_tag_pre_merge``.
   * - ``LeadEvents::TAG_POST_MERGE``
     - Dispatched after two Tags merge. The event string is ``mautic.lead_tag_post_merge``.

Both events receive a ``Mautic\LeadBundle\Event\TagMergeEvent`` instance with the following methods:

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

    use Mautic\LeadBundle\Event\TagMergeEvent;
    use Mautic\LeadBundle\LeadEvents;
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
                LeadEvents::TAG_PRE_MERGE  => ['onTagPreMerge', 0],
                LeadEvents::TAG_POST_MERGE => ['onTagPostMerge', 0],
            ];
        }

        public function onTagPreMerge(TagMergeEvent $event): void
        {
            $primaryTag   = $event->getPrimaryTag();
            $secondaryTag = $event->getSecondaryTag();

            $this->logger->info(sprintf(
                'About to merge tag "%s" into "%s"',
                $secondaryTag->getTag(),
                $primaryTag->getTag()
            ));
        }

        public function onTagPostMerge(TagMergeEvent $event): void
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
