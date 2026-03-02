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
