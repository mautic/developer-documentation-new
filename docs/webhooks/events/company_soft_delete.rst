Company soft deleted event
##########################

.. vale off

Triggered when Mautic marks a Company as soft deleted. The soft delete mechanism marks the Company for deletion without immediately removing it from the database. Depending on the ``update_company_mapping_data_in_background`` configuration parameter, the permanent deletion and Contact cleanup either happens synchronously or through a CLI command.

.. vale on

Event type
**********

``Mautic\LeadBundle\Event\CompanySoftDeleteEvent``

Since Mautic 8, Mautic dispatches this event by its event class, which replaces the removed ``LeadEvents::COMPANY_SOFT_DELETE`` constant and its ``mautic.company_soft_delete`` event name. This event isn't a Webhook event type, so you can only subscribe to it from a Plugin. See :ref:`LeadBundle events dispatched by event class <LeadBundle events dispatched by event class>`.

Event instance
**************

``\Mautic\LeadBundle\Event\CompanySoftDeleteEvent``, which extends ``\Mautic\LeadBundle\Event\CompanyEvent``

Listening to the event
**********************

Developers can subscribe to this event to react when Mautic marks Companies for deletion. For example, you might synchronize the deletion to an external Customer Relationship Management - CRM - system or trigger cleanup processes.

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/EventListener/CompanySubscriber.php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Mautic\LeadBundle\Event\CompanySoftDeleteEvent;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    final class CompanySubscriber implements EventSubscriberInterface
    {
        public static function getSubscribedEvents(): array
        {
            return [
                CompanySoftDeleteEvent::class => ['onCompanySoftDelete', 0],
            ];
        }

        public function onCompanySoftDelete(CompanySoftDeleteEvent $event): void
        {
            $company = $event->getCompany();
            $companyId = $company->getId();

            // Synchronize the deletion to external systems
            // or trigger additional cleanup processes
        }
    }

.. seealso::

    * :doc:`company_post_delete` - Triggered after permanent deletion
    * :doc:`company_post_save` - Triggered when Mautic creates or updates a Company
