SMS and MMS
###########

This document describes how to extend Mautic's SMS capabilities by building a custom transport in a Plugin. It walks through implementing the transport interfaces, adding bulk and MMS support, registering the transport, hooking into the Contact filtering pipeline, and reacting to SMS lifecycle and reply events.

.. vale off

.. note::

   Extending generally works by hooking into events using event listeners or subscribers. Read more about them in the :doc:`/plugins/event_listeners` section.

.. vale on

Transport interfaces
********************

A custom transport implements one or more interfaces from the ``Mautic\SmsBundle\Sms`` namespace, depending on the capabilities it provides. These interfaces live in Mautic core, so your Plugin implements them rather than redefining them.

* :xref:`TransportInterface source` - the base interface every transport must implement. It defines ``sendSms(Lead $lead, $content)``, which sends a single message and returns ``true`` on success or an error message string on failure.
* :xref:`BulkTransportInterface source` - extends ``TransportInterface`` to enable native batch sending through ``sendBatchSms(RecipientCollection $collection, string $content): RecipientCollection``. Transports that implement only ``TransportInterface`` fall back to iterative per-Contact sending.
* :xref:`MMSTransportInterface source` - adds MMS support with media attachments through ``sendMms(Lead $lead, string $content, array $media): bool|string``. Because of carrier restrictions, MMS currently works only for recipients in the US, Canada, and Australia.

For the authoritative method signatures and documentation blocks, see the linked source files.

Building a custom SMS transport
*******************************

.. vale off

For the general Plugin layout, see the :doc:`Plugin structure</plugins/structure>` section.

.. vale on

The worked example below builds a transport inside a Plugin named ``HelloWorldBundle``. The transport-related files sit under the bundle's ``Sms/Transport`` directory:

.. code-block:: text

   plugins/HelloWorldBundle/
   ├── Config/
   │   └── config.php
   └── Sms/
       └── Transport/
           └── HelloWorldTransport.php

Implementing the transport
==========================

Implement the interfaces for the capabilities your provider supports. The example below implements all three, so the transport handles single SMS, bulk SMS, and MMS.

.. code-block:: php

   <?php
   // plugins/HelloWorldBundle/Sms/Transport/HelloWorldTransport.php

   declare(strict_types=1);

   namespace MauticPlugin\HelloWorldBundle\Sms\Transport;

   use Mautic\LeadBundle\Entity\Lead;
   use Mautic\SmsBundle\Collection\RecipientCollection;
   use Mautic\SmsBundle\Sms\BulkTransportInterface;
   use Mautic\SmsBundle\Sms\MMSTransportInterface;
   use Mautic\SmsBundle\Sms\TransportInterface;

   class HelloWorldTransport implements TransportInterface, BulkTransportInterface, MMSTransportInterface
   {
       public function sendSms(Lead $lead, $content)
       {
           $phone = $lead->getPhone();
           if (empty($phone)) {
               return 'No phone number available';
           }

           // Send the SMS through your provider here.
           // Return true on success or an error message string on failure.
           return true;
       }

       public function sendBatchSms(RecipientCollection $collection, string $content): RecipientCollection
       {
           foreach ($collection as $recipient) {
               $lead = $recipient->getLead();

               // getFinalMessage() returns the message with tokens already
               // replaced for this recipient.
               $message = $recipient->getFinalMessage();

               $success = $this->sendToProvider($lead, $message);

               // Record the outcome so Mautic can report per-Contact results.
               $recipient->setResult($success);
           }

           return $collection;
       }

       public function sendMms(Lead $lead, string $content, array $media): bool|string
       {
           // Send the MMS with its media attachments here.
           return true;
       }
   }

Registering the transport
==========================

Register the transport in your Plugin's ``Config/config.php`` by tagging the service with ``mautic.sms_transport``. Mautic builds Plugin ``config.php`` services through its own ``ServicePass`` compiler pass rather than Symfony autoconfiguration, so implementing ``TransportInterface`` doesn't tag the service for you, and you must declare the tag explicitly. The ``SmsTransportPass`` compiler pass then collects every service carrying this tag, and the ``integrationAlias`` tag argument sets the name shown in the UI.

.. code-block:: php

   <?php
   // plugins/HelloWorldBundle/Config/config.php

   return [
       'services' => [
           'other' => [
               'mautic.sms.transport.helloworld' => [
                   'class'        => \MauticPlugin\HelloWorldBundle\Sms\Transport\HelloWorldTransport::class,
                   'tag'          => 'mautic.sms_transport',
                   'tagArguments' => [
                       'integrationAlias' => 'Hello World SMS',
                   ],
               ],
           ],
       ],
   ];

To handle delivery callbacks from your provider, register a callback handler service with the ``mautic.sms_callback_handler`` tag. Mautic's built-in :xref:`Twilio transport source` is a useful reference for a complete transport and callback implementation.

Bulk sending and recipient data
********************************

When a transport implements ``BulkTransportInterface``, Mautic passes a :xref:`RecipientCollection source` to ``sendBatchSms()``. The collection extends ``\ArrayIterator``, so you can iterate it directly, and each item is an :xref:`SmsRecipientDTO source`.

Each Data Transfer Object - DTO - wraps one Contact together with its token data. The methods most relevant to a transport are:

.. vale off

* ``getLead()`` - Returns the ``Lead`` entity for this recipient.
* ``getFinalMessage()`` - Returns the message body with tokens already replaced for this recipient.
* ``getSubstitutionData()`` - Returns the raw token values, useful for providers that perform their own substitution.
* ``setResult(bool $result)`` - Records whether the send succeeded so Mautic can report per-Contact outcomes.

.. vale on

Contact filtering events
************************

Three events fire sequentially during SMS sending to filter Contacts before dispatch. Subscribe to them to exclude Contacts based on custom criteria. Mautic dispatches each of them by its event class, so key ``getSubscribedEvents()`` on the class name.

.. vale off

For how to register a subscriber, see the :doc:`listeners and subscribers</plugins/event_listeners>` section.

Do Not Contact filter
=====================

Subscribe to ``DncEvent::class`` to filter Contacts based on **Do Not Contact** status.

.. vale on

.. code-block:: php

   <?php

   declare(strict_types=1);

   use Mautic\SmsBundle\Event\DncEvent;
   use Symfony\Component\EventDispatcher\EventSubscriberInterface;

   final class SmsFilterSubscriber implements EventSubscriberInterface
   {
       public static function getSubscribedEvents(): array
       {
           return [
               DncEvent::class => ['onDncFilter', 0],
           ];
       }

       public function onDncFilter(DncEvent $event): void
       {
           foreach ($event->getContacts() as $id => $contact) {
               if ($this->shouldExclude($contact)) {
                   $event->removeContact($id);
               }
           }
       }
   }

Queue filter
============

Subscribe to ``QueueEvent::class`` to filter Contacts based on frequency rules or queueing logic. The listener receives a ``QueueEvent``.

Generic filter
==============

Subscribe to ``FilterEvent::class`` for any remaining filtering logic, such as removing Contacts without phone numbers. The listener receives a ``FilterEvent``.

All three event classes share a common API, shown here for :xref:`FilterEvent source`:

* ``getContacts()`` - Returns the array of Contacts
* ``removeContact(int $id)`` - Remove a single Contact by ID
* ``removeContacts(array $contacts)`` - Remove multiple Contacts
* ``getRemovedContacts()`` - Get the list of removed Contacts

Campaign SMS events
*******************

When integrating SMS with Campaigns, use the batch Campaign action event for better performance.

Batch action event
==================

Use ``SmsEvents::ON_CAMPAIGN_TRIGGER_BATCH_ACTION`` to handle Campaign SMS actions. Set it as the ``batchEventName`` when registering the action on ``CampaignEvents::CAMPAIGN_ON_BUILD``. See :doc:`/plugin_extensions/campaigns` for the full Campaign action workflow.

.. code-block:: php

   <?php

   use Mautic\CampaignBundle\Event\CampaignBuilderEvent;
   use Mautic\SmsBundle\SmsEvents;

   public function onCampaignBuild(CampaignBuilderEvent $event): void
   {
       $event->addAction(
           'my_plugin.send_sms',
           [
               'label'          => 'Send Custom SMS',
               'batchEventName' => SmsEvents::ON_CAMPAIGN_TRIGGER_BATCH_ACTION,
               // Other configuration...
           ]
       );
   }

SMS lifecycle and reply events
******************************

Subscribe to these events to run custom logic when a User saves or deletes an SMS, or when a Contact replies to one. Mautic dispatches each of them by its event class, so key ``getSubscribedEvents()`` on the class name. All classes live in the ``Mautic\SmsBundle\Event`` namespace.

.. vale off

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Event class
     - Fires
   * - ``SmsPreSaveEvent``
     - Before Mautic saves an SMS.
   * - ``SmsPostSaveEvent``
     - After Mautic saves an SMS.
   * - ``SmsPreDeleteEvent``
     - Before Mautic deletes an SMS.
   * - ``SmsPostDeleteEvent``
     - After Mautic deletes an SMS.
   * - ``ReplyEvent``
     - When Mautic receives an SMS reply from a Contact.

.. vale on

The four lifecycle classes extend the abstract ``SmsEvent`` class. Use ``getSms()`` to read the SMS entity and ``isNew()`` to tell whether the save created it. Because each lifecycle class is a subclass, a listener type-hinted against ``SmsEvent`` keeps working. ``ReplyEvent`` exposes the Contact through ``getContact()`` and the reply text through ``getMessage()``.

.. code-block:: php

   <?php

   declare(strict_types=1);

   use Mautic\SmsBundle\Event\ReplyEvent;
   use Mautic\SmsBundle\Event\SmsEvent;
   use Mautic\SmsBundle\Event\SmsPostSaveEvent;
   use Symfony\Component\EventDispatcher\EventSubscriberInterface;

   final class SmsLifecycleSubscriber implements EventSubscriberInterface
   {
       public static function getSubscribedEvents(): array
       {
           return [
               SmsPostSaveEvent::class => ['onSmsPostSave', 0],
               ReplyEvent::class       => ['onSmsReply', 0],
           ];
       }

       public function onSmsPostSave(SmsEvent $event): void
       {
           $sms = $event->getSms();
           // Sync $sms to an external system, for example.
       }

       public function onSmsReply(ReplyEvent $event): void
       {
           $contact = $event->getContact();
           $message = $event->getMessage();
           // Handle the reply, for example by forwarding it to a support tool.
       }
   }

.. note::

   Mautic 8 removed the ``SMS_PRE_SAVE``, ``SMS_POST_SAVE``, ``SMS_PRE_DELETE``, ``SMS_POST_DELETE``, and ``ON_REPLY`` constants from ``SmsEvents``. Before Mautic 8, the four lifecycle events shared one ``SmsEvent`` object under four constant names. Code that still references one of these constants throws a PHP ``Error`` with the message 'Undefined constant'. Replace each constant with the matching event class from the preceding table.

SMS event constants
*******************

The :xref:`SmsEvents source` class defines the SMS event constants that remain string-keyed:

.. vale off

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Event constant
     - Description
   * - ``TOKEN_REPLACEMENT``
     - Fires right before Mautic returns SMS content, so listeners can replace tokens. The listener receives a ``Mautic\CoreBundle\Event\TokenReplacementEvent``.
   * - ``SMS_ON_SEND``
     - Registers the Webhook event type for sent SMS messages.
   * - ``ON_CAMPAIGN_TRIGGER_BATCH_ACTION``
     - Fires when a Campaign triggers an SMS action for a batch of Contacts.
   * - ``ON_CAMPAIGN_REPLY``
     - Identifies the Campaign decision that fires when a Contact replies to an SMS. The listener receives a ``ReplyEvent``.

.. vale on

Mautic 8 also removed the ``ON_CAMPAIGN_TRIGGER_ACTION``, ``ON_SMS_TOKENS_BUILD``, ``DNC_FILTER_CONTACTS_ON_SEND``, ``QUEUE_FILTER_CONTACTS_ON_SEND``, and ``FILTER_CONTACTS_ON_SEND`` constants from ``SmsEvents``. Mautic 8 dispatches no events under these names. To filter Contacts, subscribe to the event classes in `Contact filtering events`_.
