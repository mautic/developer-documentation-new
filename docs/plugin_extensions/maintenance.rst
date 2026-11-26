Maintenance cleanup
###################

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

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

Contacts that the cleanup deletes
*********************************

The ``mautic:maintenance:cleanup`` command deletes inactive Contacts with SQL queries, so Mautic doesn't dispatch the ``LeadEvents::LEAD_PRE_DELETE`` and ``LeadEvents::LEAD_POST_DELETE`` events for them. To act on these Contacts before Mautic deletes them, for example to delete the data that your Plugin stores for them, create a listener for the ``\Mautic\LeadBundle\LeadEvents::LEAD_PRE_CLEANUP_DELETE`` event. Mautic dispatches it before it deletes each batch of Contacts. It doesn't dispatch the event when the command runs with ``--dry-run``.

The listener receives a ``Mautic\LeadBundle\Event\ContactPreCleanupDeleteEvent`` instance with these methods:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Method
     - Description
   * - ``getContactIds()``
     - Returns the IDs of the Contacts in the batch, as an array of integers.
   * - ``isGdpr()``
     - Returns ``true`` when the command runs with the ``--gdpr`` option. With this option, the batch can include identified Contacts. Without it, the batch contains only anonymous Contacts.

.. code-block:: php

    <?php
    // plugins\HelloWorldBundle\EventListener\ContactCleanupSubscriber.php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Doctrine\DBAL\ArrayParameterType;
    use Doctrine\DBAL\Connection;
    use Mautic\LeadBundle\Event\ContactPreCleanupDeleteEvent;
    use Mautic\LeadBundle\LeadEvents;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    final class ContactCleanupSubscriber implements EventSubscriberInterface
    {
        public function __construct(private Connection $db)
        {
        }

        public static function getSubscribedEvents(): array
        {
            return [
                LeadEvents::LEAD_PRE_CLEANUP_DELETE => ['onContactPreCleanupDelete', 0],
            ];
        }

        public function onContactPreCleanupDelete(ContactPreCleanupDeleteEvent $event): void
        {
            $this->db->createQueryBuilder()
                ->delete(MAUTIC_TABLE_PREFIX.'worlds')
                ->where('contact_id IN (:contactIds)')
                ->setParameter('contactIds', $event->getContactIds(), ArrayParameterType::INTEGER)
                ->executeStatement();
        }
    }
