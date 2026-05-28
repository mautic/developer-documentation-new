Company soft deleted event
##########################

Triggered when Mautic marks a Company as soft deleted. The soft delete mechanism marks the Company for deletion without immediately removing it from the database. Depending on the ``update_company_mapping_data_in_background`` configuration parameter, the permanent deletion and Contact cleanup either happens synchronously or through a CLI command.

.. _company_soft_deleted_event_type:

Event type
**********

``mautic.company_soft_delete``

.. _company_soft_deleted_event_properties:

Event properties
****************

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``id``
      - int
      - ID of the soft-deleted Company
    * - ``company``
      - object
      - :ref:`Company object<webhooks/events/company_post_save:Company properties>`.
    * - ``timestamp``
      - string
      - Date/time the event occurred in ISO 8601 format.

Listening to the event
**********************

Developers can subscribe to this event to react when Companies are marked for deletion. For example, you might synchronize the deletion to an external CRM or trigger cleanup processes.

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/EventListener/CompanySubscriber.php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Mautic\LeadBundle\Event\CompanyEvent;
    use Mautic\LeadBundle\LeadEvents;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    final class CompanySubscriber implements EventSubscriberInterface
    {
        public static function getSubscribedEvents(): array
        {
            return [
                LeadEvents::COMPANY_SOFT_DELETE => ['onCompanySoftDelete', 0],
            ];
        }

        public function onCompanySoftDelete(CompanyEvent $event): void
        {
            $company = $event->getCompany();
            $companyId = $company->getId();

            // Synchronize the deletion to external systems
            // or trigger additional cleanup processes
        }
    }

.. seealso::

    * :doc:`company_post_delete` - Triggered after permanent deletion
    * :doc:`company_post_save` - Triggered when Companies are created or updated
