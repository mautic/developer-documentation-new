Event listeners
===============

Mautic leverages Symfony's EventDispatcher to execute and communicate various actions through Mautic. Plugins can hook into these to extend the capability of Mautic. Refer to the Extending Mautic section of the documentation for some of the ways to do this.

.. code-block:: php

    <?php
    //plugins\HelloWorldBundle\EventListener\LeadSubscriber

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Mautic\LeadBundle\Event as Events;
    use Mautic\LeadBundle\LeadEvents;

    /**
     * Class LeadSubscriber
     *
     * @package Mautic\LeadBundle\EventListener
     */
    class LeadSubscriber extends CommonSubscriber
    {
    
        /**
         * @return array
         */
        static public function getSubscribedEvents()
        {
            return array(
                LeadEvents::LEAD_POST_SAVE     => array('onLeadPostSave', 0),
                LeadEvents::LEAD_POST_DELETE   => array('onLeadDelete', 0)
            );
        }
    
        public function onLeadPostSave(LeadEvent $event)
        {
            $lead = $event->getLead();
            
            // do something
        }
    
        public function onLeadDelete(LeadEvent $event)
        {
            $lead = $event->getLead();
            
            $deletedId = $lead->deletedId;
            
            // do something
        }
    }
    // ...

Subscribers
-----------
The easiest way to listen to various events is to use an event subscriber. Read more about subscribers in :xref:`symfony-event-subscribers`. 

Plugin event subscribers can extend ``\Mautic\CoreBundle\EventListener\CommonSubscriber`` which gives access to commonly used dependencies and also allows registering the subscriber service through the config file for the bundle. See :ref:`plugins/config:Service config items` for more information on registering event services. 
    
Available events
----------------



There are many events available throughout Mautic. Depending on what you're trying to implement, look at the ``*Event.php`` for the core bundle, located in the root of the bundle. For example, the ``app\bundles\LeadBundle\LeadEvents.php`` file defines and describes events relating to Contacts. The final classes provide the names of the events to listen to. Always use the event constants to ensure future changes to event names won't break the Plugin.

Custom events
-------------
A Plugin can create and dispatch its own events. 

Custom events require the following:

1) The class defining the available events for the Plugin using a ``final class`` with constants.

.. code-block:: php

    <?php
    // plugins\HelloWorldBundle\HelloWorldEvents.php
    
    namespace MauticPlugin\HelloWorldBundle;
    
    /**
     * Class HelloWorldEvents
     */
    final class HelloWorldEvents
    {
        /**
         * The helloworld.armageddon event is dispatched when a world is doomed by a giant meteor
         *
         * The event listener receives a MauticPlugin\HelloWorldBundle\Event\ArmageddonEvent instance.
         *
         * @var string
         */
        const ARMAGEDDON = 'helloworld.armageddon';
    }
    // ...


2) The Event class that is received by the listeners. This class should extend ``Symfony\Component\EventDispatcher\Event``. It's created when the event is dispatched and should have any information listeners need to act on it.

.. code-block:: php

    <?php
    // plugins\HelloWorldBundle\Event\ArmageddonEvent.php
    
    namespace MauticPlugin\HelloWorldBundle\Event;
    
    use Symfony\Component\EventDispatcher\Event;
    use MauticPlugin\HelloWorldBundle\Entity\World;
    
    class ArmageddonEvent extends Event
    {
        /** @var World  */
        protected $world;
        
        /** @var bool  */    
        protected $falseAlarm = false;
         
        public function __construct(World $world)
        {
            $this->world = $world;
        }
        
        public function shouldPanic()
        {
            return ('earth' == $this->world->getName());
        }
        
        public function setIsFalseAlarm()
        {
            $this->falseAlarm = true;
        }
        
        public function getIsFalseAlarm()
        {
            return $this->falseAlarm;
        }
    }
    // ...


3) The code that dispatches the event where appropriate using the ``event_dispatcher`` service.

.. code-block:: php

    <?php
    
    $dispatcher = $this->get('event_dispatcher');
    if ($dispatcher->hasListeners(HelloWorldEvents::ARMAGEDDON)) {
        $event = $dispatcher->dispatch(HelloWorldEvents::ARMAGEDDON, new ArmageddonEvent($world));
        
        if ($event->shouldPanic()) {
            throw new \Exception("Run for the hills!");
        }
    }


