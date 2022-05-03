Contacts
==========================================================

There's several ways to extend Contacts in Mautic.
One of them is to show custom events in a Contact's event timeline - this document shows you how.

Contact timeline/history
------------------------

To inject events into a Contact's timeline, create an event listener that listens to the ``LeadEvents::TIMELINE_ON_GENERATE`` event.
Using this event, the plugin can inject unique items into the timeline and also into the engagements graph on each page.

.. note:: Before using this event listener, you'll need to ensure that you store your custom events in a custom database table. See :ref:`Generating timeline events from your own custom events` below for more details.

The event listener receives a ``Mautic\LeadBundle\Event\LeadTimelineEvent`` object. You can find the commonly used methods below the code example.

.. code-block:: PHP

    <?php
    // plugins/HelloWorldBundle/EventListener/LeadSubscriber.php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Doctrine\ORM\EntityManager;
    use Mautic\LeadBundle\Event\LeadTimelineEvent;
    use Mautic\LeadBundle\LeadEvents;
    use MauticPlugin\HelloWorldBundle\Entity\WorldRepository;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;
    use Symfony\Component\Routing\RouterInterface;
    use Symfony\Contracts\Translation\TranslatorInterface;

    final class LeadSubscriber implements EventSubscriberInterface
    {
        private TranslatorInterface $translator;
        private EntityManager $em;
        private RouterInterface $router;

        public function __construct(TranslatorInterface $translator, EntityManager $em, RouterInterface $router)
        {
            $this->translator = $translator;
            $this->em         = $em;
            $this->router     = $router;
        }

        public static function getSubscribedEvents(): array
        {
            return [
                LeadEvents::TIMELINE_ON_GENERATE => ['onTimelineGenerate', 0]
            ];
        }

        public function onTimelineGenerate(LeadTimelineEvent $event): void
        {
            // Add this event to the list of available events which generates the event type filters
            $eventTypeKey  = 'visited.worlds';
            $eventTypeName = $this->translator->trans('mautic.hello.world.visited_worlds');
            $event->addEventType($eventTypeKey, $eventTypeName);

            // Determine if this event has been filtered out
            if (!$event->isApplicable($eventTypeKey)) {
                return;
            }

            /** @var WorldRepository */
            $repository = $this->em->getRepository(WorldRepository::class);

            // $event->getQueryOptions() provide timeline filters, etc.
            // This method should use DBAL to obtain the events to be injected into the timeline based on pagination
            // but also should query for a total number of events and return an array of ['total' => $x, 'results' => []].
            // There is a TimelineTrait to assist with this. See repository example.
            $stats = $repository->getTimelineStats($event->getLead()->getId(), $event->getQueryOptions());

            // If isEngagementCount(), this event should only inject $stats into addToCounter() to append to data to generate
            // the engagements graph. Not all events are engagements if they are just informational so it could be that this
            // line should only be used when `!$event->isEngagementCount()`. Using TimelineTrait will determine the appropriate
            // return value based on the data included in getQueryOptions() if used in the stats method above.
            $event->addToCounter($eventTypeKey, $stats);

            if (!$event->isEngagementCount()) {
                // Add the events to the event array
                foreach ($stats['results'] as $stat) {
                    if ($stat['dateSent']) {
                        $event->addEvent(
                            [
                                // Event key type
                                'event'           => $eventTypeKey,
                                // Event name/label - can be a string or an array as below to convert to a link
                                'eventLabel'      => [
                                    'label' => $stat['name'],
                                    'href'  => $this->router->generate(
                                        'mautic_dynamicContent_action',
                                        ['objectId' => $stat['dynamic_content_id'], 'objectAction' => 'view']
                                    )
                                ],
                                // Translated string displayed in the Event Type column
                                'eventType'       => $eventTypeName,
                                // \DateTime object for the timestamp column
                                'timestamp'       => $stat['dateSent'],
                                // Optional details passed through to the contentTemplate
                                'extra'           => [
                                    'stat' => $stat,
                                    'type' => 'sent'
                                ],
                                // Optional template to customize the details of the event in the timeline
                                'contentTemplate' => 'MauticDynamicContentBundle:SubscribedEvents\Timeline:index.html.php',
                                // Font Awesome class to display as the icon
                                'icon'            => 'fa-envelope'
                            ]
                        );
                    }
                }
            }
        }
    }

.. list-table::
    :header-rows: 1

    * - Method
      - Description
    * - ``isApplicable()``
      - Determines if this event is applicable and not filtered out.
    * - ``addEventType()``
      - Required - Add this event to the list of available events.
    * - ``getLead()``
      - Get the Contact entity
    * - ``getQueryOptions()``
      - Used to get pagination, filters, etc needed to generate an appropriate query.
    * - ``addToCounter()``
      - Used to add total number of events across all Pages to the counters. This also generates the numbers for the engagements graph.
    * - ``addEvent()``
      - Required - Injects an event into the timeline. Accepts an array with the keys defined as below. 

.. list-table::
    :header-rows: 1

    * - Key
      - Required
      - Type
      - Description
    * - ``event``
      - Required
      - string
      - The key for this event. Eg. world.visited
    * - ``eventType``
      - Required
      - string
      - The translated string representing this event type. Eg. Worlds visited
    * - ``timestamp``
      - Required
      - \DateTime
      - DateTime object when this event took place
    * - ``eventLabel``
      - Optional
      - string/array
      - The translated string to display in the event name. Examples include names of items, Landing Page titles, etc. This can also be an array of ['label' => '', 'href' => ''] to have the entry converted to a link. This defaults to eventType if not defined.
    * - ``extra``
      - Optional
      - array
      - Anything you want to pass through to the content template to generate the details view for this event
    * - ``contentTemplate``
      - Optional
      - string
      - Template you want to use to generate the details view for this event. Eg. ``HelloBundle:SubscribedEvents\Timeline:index.html.php``
    * - ``icon``
      - Optional
      - Font Awesome class
      - 

Generating timeline events from your own custom events
------------------------------------------------------

You're responsible for creating your own events and store them in some database tables.
From there, you can turn them into timeline events so they show up on the Contact's detail screen.
To make this process a bit easier, the ``Mautic\LeadBundle\Entity\TimelineTrait`` trait is available.

.. code-block:: PHP

    <?php
    // plugins/HelloWorldBundle/Entity/WorldRepository.php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\Entity;

    use Mautic\CoreBundle\Entity\CommonRepository;
    use Mautic\LeadBundle\Entity\TimelineTrait;

    /**
    * @extends CommonRepository<World>
    */
    class WorldRepository extends CommonRepository
    {
        use TimelineTrait;

        /**
        * @param array<string,string> $options
        * @return array<string,mixed>
        */
        public function getTimelineStats(int $leadId, array $options = []): array
        {
            $query = $this->getEntityManager()->getConnection()->createQueryBuilder();

            $query->select('w.id, w.name, w.visited_count, w.date_visited, w.visit_details')
                ->from(MAUTIC_TABLE_PREFIX . 'world_visits', 'w')
                ->where($query->expr()->eq('w.lead_id', (int) $leadId));

            if (isset($options['search']) && $options['search']) {
                $query->andWhere(
                    $query->expr()->like('w.name', $query->expr()->literal('%' . $options['search'] . '%'))
                );
            }

            return $this->getTimelineResults($query, $options, 'w.name', 'w.date_visited', ['visit_details'], ['date_visited']);
        }
    }


To leverage this, accept the array from ``$event->getQueryOptions()`` in the repository method. Create a DBAL QueryBuilder object (``$this->getEntityManager()->getConnection()->createQueryBuilder()``) and define the basics of the array, including filtering by lead id and search filter. Then pass the QueryBuilder object to the ``getTimelineResults()`` method along with the following arguments:

.. list-table::
    :header-rows: 1

    * - Key
      - Required
      - Type
      - Description
    * - $query
      - Required
      - QueryBuilder
      - Database Abstraction Layer QueryBuilder object defining basics of the query.
    * - $options
      - Required
      - array
      - Array generated and passed into method by ``$event->getQueryOptions()`` in the event listener above
    * - $eventNameColumn
      - Required
      - string
      - Name of the column with table prefix that should to use when sorting by event name
    * - $timestampColumn
      - Required
      - string
      - Name of the column with table prefix that should to use when sorting by timestamp
    * - $serializedColumns
      - Optional
      - array
      - When using the Database Abstraction Layer, arrays won't be auto-unserialized by Doctrine. Define the columns here, as returned by the query results, to auto-unserialize.
    * - $dateTimeColumns
      - Optional
      - array
      - When using the Database Abstraction Layer, ``datetime`` columns won't be auto converted to \DateTime objects by Doctrine. Define the columns here, as returned by the query results, to auto do so.
    * - $resultsParserCallback
      - Optional
      - callback
      - Callback to custom parse a result. This is optional and mainly used to handle a column result when all results are already looped over for $serializedColumns and $dateTimeColumns.