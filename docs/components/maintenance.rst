Extending maintenance cleanup
#############################

To hook into the ``mautic:maintenance:cleanup`` command, create a listener for the ``\Mautic\CoreBundle\CoreEvents::MAINTENANCE_CLEANUP_DATA`` event.
Use ``$event->setStat($key, $affectedRows, $sql, $sqlParameters)`` to give feedback to the CLI command.
Note that ``$sql`` and ``$sqlParameters`` are only used for debugging and shown only in the ``dev`` environment.

.. warning:: Don't delete records when the event is a dry run. You can use ``$event->isDryRun()`` to validate whether this is the case. See the code sample below for more details.

.. code-block:: php

    <?php
    // plugins\HelloWorldBundle\EventListener\MaintenanceSubscriber.php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Doctrine\DBAL\Connection;
    use Mautic\CoreBundle\CoreEvents;
    use Mautic\CoreBundle\Event\MaintenanceEvent;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;
    use Symfony\Contracts\Translation\TranslatorInterface;

    class MaintenanceSubscriber implements EventSubscriberInterface
    {
        protected Connection $db;
        protected TranslatorInterface $translator;

        public function __construct(Connection $db, TranslatorInterface $translator)
        {
            $this->db         = $db;
            $this->translator = $translator;
        }

        public static function getSubscribedEvents()
        {
            return [
                CoreEvents::MAINTENANCE_CLEANUP_DATA => ['onDataCleanup', -50]
            ];
        }

        public function onDataCleanup(MaintenanceEvent $event)
        {
            $qb = $this->db->createQueryBuilder()
                ->setParameter('date', $event->getDate()->format('Y-m-d H:i:s'));

            if ($event->isDryRun()) {
                $rows = (int) $qb->select('count(*) as records')
                    ->from(MAUTIC_TABLE_PREFIX . 'worlds', 'w')
                    ->where(
                        $qb->expr()->gte('w.date_added', ':date')
                    )
                    ->execute()
                    ->fetchColumn();
            } else {
                $rows = (int) $qb->delete(MAUTIC_TABLE_PREFIX . 'worlds')
                    ->where(
                        $qb->expr()->lte('date_added', ':date')
                    )
                    ->execute();
            }

            $event->setStat($this->translator->trans('mautic.maintenance.hello_world'), $rows, $qb->getSQL(), $qb->getParameters());
        }
    }
