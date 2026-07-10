Webhooks
########

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Webhooks let Mautic send data to external services through an endpoint URL. Extending them relies on event listeners with two responsibilities:

#. An event listener that adds Webhook types to the Webhook interface.
#. An event listener on whichever action should queue a Webhook payload.

.. vale off

In your own bundle you also need to dispatch your custom event and payload, register your listeners as services, and - in the receiving app - accept the payload. Refer to :ref:`Receiving Webhook payloads<plugin_extensions/webhooks:Receiving Webhook payloads>` for the receiving side.

.. vale on

Webhook type listener
*********************

Use the ``WebhookEvents::WEBHOOK_ON_BUILD`` event to add a webhook type to the Webhook interface. Call ``addEvent()`` with your payload event constant and an array containing a label and description:

.. code-block:: php

    <?php

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Mautic\WebhookBundle\Event\WebhookBuilderEvent;
    use Mautic\WebhookBundle\WebhookEvents;
    use MauticPlugin\HelloWorldBundle\HelloWorldEvents;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    class WebhookSubscriber implements EventSubscriberInterface
    {
        public static function getSubscribedEvents(): array
        {
            return [
                WebhookEvents::WEBHOOK_ON_BUILD => ['onWebhookBuild', 0],
            ];
        }

        public function onWebhookBuild(WebhookBuilderEvent $event): void
        {
            $type = [
                'label'       => 'mautic.helloworld.webhook.event.type.new',
                'description' => 'mautic.helloworld.webhook.event.type.new_desc',
            ];

            $event->addEvent(HelloWorldEvents::ACTION_TO_TRIGGER, $type);

            // You can call addEvent() multiple times to register several types at once.
        }
    }

``HelloWorldEvents::ACTION_TO_TRIGGER`` is a constant registered in your bundle. Mautic saves the type in the database and queries for it later, so you must reuse the exact same constant in the payload listener.

Payload event listener
**********************

Add a listener for the action that should create a payload. Inject ``Mautic\WebhookBundle\Model\WebhookModel`` and call ``queueWebhooksByType()`` with the same event constant, the payload array, and the serialization groups used to format the JSON:

.. code-block:: php

    <?php

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Mautic\LeadBundle\Event\LeadEvent;
    use Mautic\LeadBundle\LeadEvents;
    use Mautic\WebhookBundle\Model\WebhookModel;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    class LeadSubscriber implements EventSubscriberInterface
    {
        public function __construct(private WebhookModel $webhookModel)
        {
        }

        public static function getSubscribedEvents(): array
        {
            // Note: this is the same constant registered in the WEBHOOK_ON_BUILD listener.
            return [
                LeadEvents::LEAD_POST_SAVE => ['onLeadNewUpdate', 0],
            ];
        }

        public function onLeadNewUpdate(LeadEvent $event): void
        {
            // Only queue a payload when the Contact is new.
            if (!$event->isNew()) {
                return;
            }

            // Serialization groups format the payload JSON; they're defined on your bundle's entity.
            $this->webhookModel->queueWebhooksByType(
                LeadEvents::LEAD_POST_SAVE,
                ['contact' => $event->getLead()],
                ['leadDetails', 'userList', 'publishDetails', 'ipAddress']
            );
        }
    }

The event constant returned in ``getSubscribedEvents()`` must match the type from the type listener exactly, because it's used in a database query to decide which payloads to include in the POST. Register the listener as a service in your bundle's configuration file.

Receiving Webhook payloads
**************************

Webhooks send data for Contacts, Points, Email opens, and more to outside applications. Mautic takes the app's endpoint URL and sends a POST request there, including the data relevant to the event that fired.

To receive the payloads, create a publicly accessible endpoint in your app that accepts a POST request from Mautic. The payload contents vary based on the events the User selects. The following is a sample payload for a new Contact:

.. code-block:: json

    {
      "mautic.lead_post_save_new": [
        {
          "contact": {
            "id": 1,
            "points": 0,
            "fields": {
              "core": {
                "firstname": { "label": "First Name", "value": "Hello" },
                "lastname": { "label": "Last Name", "value": "World" },
                "email": { "label": "Email", "value": "contact@example.com" }
              }
            }
          },
          "timestamp": "2015-08-18T18:53:33+00:00"
        }
      ]
    }
