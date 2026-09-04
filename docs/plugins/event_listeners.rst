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
    
.. _available events:

Available events
****************

There are many events available throughout Mautic. Depending on what you're trying to implement, look at the ``*Event.php`` for the core bundle, located in the root of the bundle. For example, the ``app\bundles\LeadBundle\LeadEvents.php`` file defines and describes events relating to Contacts. The final classes provide the names of the events to listen to. For event families that still use string constants, such as ``LeadEvents`` and ``PageEvents``, always use the event constant to ensure future changes to event names won't break the Plugin.

.. note::

   Since Mautic 8, Mautic dispatches CoreBundle events, the ``Mautic\CoreBundle\CoreEvents`` family, by the event object alone, so the event class is the event name. This matches the Symfony 4.3 dispatch style.

   * Key ``getSubscribedEvents()`` on the event class, for example ``MenuEvent::class``, not on the ``CoreEvents::*`` constant or the raw string name such as ``mautic.build_menu``.
   * The ``CoreEvents`` constants remain in the codebase but are no longer used for dispatch, so a subscriber still keyed on the constant or string won't fire. It fails silently: it throws no exception and logs nothing, and simply never runs.
   * Other event families, such as ``LeadEvents`` and ``PageEvents``, still use their constants. Keep keying on those.

The following table is the complete migration reference for CoreBundle event subscribers, mapping each old event name and ``CoreEvents`` constant to its new event class, all of which live in the ``Mautic\CoreBundle\Event`` namespace.

.. list-table::
   :header-rows: 1
   :widths: 40 35 25

   * - Old event name
     - CoreEvents constant
     - New event class
   * - ``mautic.build_menu``
     - ``CoreEvents::BUILD_MENU``
     - ``MenuEvent``
   * - ``mautic.build_route``
     - ``CoreEvents::BUILD_ROUTE``
     - ``RouteEvent``
   * - ``mautic.global_search``
     - ``CoreEvents::GLOBAL_SEARCH``
     - ``GlobalSearchEvent``
   * - ``mautic.list_stats``
     - ``CoreEvents::LIST_STATS``
     - ``StatsEvent``
   * - ``mautic.build_command_list``
     - ``CoreEvents::BUILD_COMMAND_LIST``
     - ``CommandListEvent``
   * - ``mautic.on_fetch_icons``
     - ``CoreEvents::FETCH_ICONS``
     - ``IconEvent``
   * - ``mautic.build_embeddable_js``
     - ``CoreEvents::BUILD_MAUTIC_JS``
     - ``BuildJsEvent``
   * - ``mautic.maintenance_cleanup_data``
     - ``CoreEvents::MAINTENANCE_CLEANUP_DATA``
     - ``MaintenanceEvent``
   * - ``mautic.view_inject_custom_buttons``
     - ``CoreEvents::VIEW_INJECT_CUSTOM_BUTTONS``
     - ``CustomButtonEvent``
   * - ``mautic.view_inject_custom_content``
     - ``CoreEvents::VIEW_INJECT_CUSTOM_CONTENT``
     - ``CustomContentEvent``
   * - ``mautic.view_inject_custom_template``
     - ``CoreEvents::VIEW_INJECT_CUSTOM_TEMPLATE``
     - ``CustomTemplateEvent``
   * - ``mautic.view_inject_custom_assets``
     - ``CoreEvents::VIEW_INJECT_CUSTOM_ASSETS``
     - ``CustomAssetsEvent``
   * - ``mautic.on_generated_columns_build``
     - ``CoreEvents::ON_GENERATED_COLUMNS_BUILD``
     - ``GeneratedColumnsEvent``

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
