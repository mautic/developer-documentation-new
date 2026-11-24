Event dispatcher
################

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Use the event dispatcher to dispatch your Plugin's custom events. Inject ``Symfony\Component\EventDispatcher\EventDispatcherInterface`` into your service, and always type-hint the interface since the concrete class can differ between environments:

.. code-block:: php

    <?php

    use Symfony\Component\EventDispatcher\EventDispatcherInterface;
    use MauticPlugin\HelloWorldBundle\HelloWorldEvents;
    use MauticPlugin\HelloWorldBundle\Event\ArmageddonEvent;

    final class ExampleService
    {
        public function __construct(private EventDispatcherInterface $dispatcher)
        {
        }

        public function warnTheWorld(World $world): void
        {
            $event = $this->dispatcher->dispatch(
                new ArmageddonEvent($world),
                HelloWorldEvents::ARMAGEDDON
            );

            if ($event->shouldPanic()) {
                throw new \RuntimeException('Run for the hills!');
            }
        }
    }

In Mautic 7, ``dispatch()`` takes the event object as the first argument and the event name as the second. To listen for events, register an event subscriber. See :ref:`Custom events <dispatch custom events>` to learn how to define and dispatch your Plugin's own events.
