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

.. vale off

That advice holds for every event dispatched by a string constant. Since Mautic 8, some bundles instead dispatch an event by the event object alone - Symfony 4.3+ class-name dispatch - so the event name is the event class rather than a string constant. For a converted event, the event class - not a string constant - is the stable dispatch identifier, and you key ``getSubscribedEvents()`` on the class. The notes below cover the StageBundle and DashboardBundle events. Other bundles received similar conversions in this release.

.. note::

   Since Mautic 8, Mautic dispatches ``Mautic\StageBundle\Event\StageBuilderEvent`` by the event object alone. Key ``getSubscribedEvents()`` on ``StageBuilderEvent::class``, not on ``StageEvents::STAGE_ON_BUILD`` or the string ``mautic.stage_on_build``. Those constants remain for backward compatibility but no longer dispatch this event, so a subscriber still keyed on the old constant never fires - no exception is thrown and nothing is logged. The ``StageEvent`` CRUD group, ``STAGE_ON_ACTION``, and ``ON_CAMPAIGN_BATCH_ACTION`` are unchanged.

   .. code-block:: php

      return [
          StageBuilderEvent::class => ['onStageBuild', 0],
          // ...
      ];

.. note::

   Since Mautic 8, Mautic dispatches two DashboardBundle widget events by the event object alone. Key ``getSubscribedEvents()`` on the event class rather than on the former constant. The classes live in ``Mautic\DashboardBundle\Event``.

   .. list-table::
      :header-rows: 1
      :widths: 50 50

      * - Former event constant
        - Mautic 8 event class - subscription key
      * - ``DASHBOARD_ON_MODULE_LIST_GENERATE``
        - ``WidgetTypeListEvent``
      * - ``DASHBOARD_ON_MODULE_FORM_GENERATE``
        - ``WidgetFormEvent``

   The former constants remain for backward compatibility but no longer dispatch these events, so a subscriber still keyed on an old constant stays silent: it never fires, and nothing signals why. ``DASHBOARD_ON_MODULE_DETAIL_GENERATE`` and ``DASHBOARD_ON_MODULE_DETAIL_PRE_LOAD`` - both sharing ``WidgetDetailEvent`` - remain string-keyed and unchanged.

   .. code-block:: php

      return [
          WidgetTypeListEvent::class => ['onWidgetListGenerate', 0],
          WidgetFormEvent::class     => ['onWidgetFormGenerate', 0],
          // ...
      ];

.. note::

   To confirm Mautic registered a subscriber under an event's class name, run ``bin/console debug:event-dispatcher`` with the event's fully-qualified class name, for example:

   .. code-block:: bash

      bin/console debug:event-dispatcher 'Mautic\StageBundle\Event\StageBuilderEvent'

   Your subscriber's class and method appear in the listing for that event. If they're absent, you haven't registered the subscriber for it. This works for any event - pass the class name of whichever event you subscribe to.

.. vale on

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
