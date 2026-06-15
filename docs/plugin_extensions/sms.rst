SMS and MMS
###########

This document describes how to extend Mautic's SMS capabilities, including creating custom SMS transports, supporting bulk messaging, implementing MMS, and hooking into the Contact filtering pipeline.

.. vale off

.. note::

   Extending generally works by hooking into events using event listeners or subscribers. Read more about them in the :doc:`/plugins/event_listeners` section.

.. vale on

SMS transports
**************

Mautic supports custom SMS transports through a set of interfaces. Each transport must implement at least ``TransportInterface`` and can optionally implement additional interfaces for bulk messaging and MMS support.

.. vale off

TransportInterface
==================

.. vale on

This is the base interface for all SMS transports. Implement this interface to create a transport that sends SMS messages one at a time.

.. code-block:: php

   <?php

   namespace Mautic\SmsBundle\Sms;

   use Mautic\LeadBundle\Entity\Lead;

   interface TransportInterface
   {
       /**
        * @return bool|string Returns true on success or an error message
        */
       public function sendSms(Lead $lead, string $content);
   }

.. vale off

BulkTransportInterface
======================

.. vale on

Implement this interface to enable native batch SMS sending. Transports that only implement ``TransportInterface`` fall back to iterative per-Contact sending.

.. code-block:: php

   <?php

   namespace Mautic\SmsBundle\Sms;

   use Mautic\SmsBundle\Collection\RecipientCollection;

   interface BulkTransportInterface extends TransportInterface
   {
       /**
        * @param RecipientCollection<SmsRecipientDTO> $collection
        *
        * @return RecipientCollection<SmsRecipientDTO>
        */
       public function sendBatchSms(RecipientCollection $collection, string $content): RecipientCollection;
   }

The ``RecipientCollection`` contains ``SmsRecipientDTO`` objects. After processing each recipient, call ``setResult(true)`` or ``setResult(false)`` on the Data Transfer Object (DTO) to indicate success or failure.

.. vale off

MMSTransportInterface
=====================

.. vale on

Implement this interface to support MMS with media attachments. Currently, MMS works for recipients in the US, Canada, and Australia due to carrier restrictions.

.. code-block:: php

   <?php

   namespace Mautic\SmsBundle\Sms;

   use Mautic\LeadBundle\Entity\Lead;

   interface MMSTransportInterface
   {
       /**
        * @param array<mixed> $media Array of media URLs
        *
        * @return bool|string Returns true on success or an error message
        */
       public function sendMms(Lead $lead, string $content, array $media);
   }

MMS messages can include up to 10 media files with a combined maximum size of 5 MB. For external URLs, validate that media files meet size requirements since Mautic only enforces size limits for locally uploaded files.

.. vale off

Registering SMS transports
==========================

.. vale on

Register a transport by tagging the service with ``mautic.sms_transport``. Set the ``integrationAlias`` argument to display the transport name in the UI.

.. code-block:: php

   <?php

   // config/config.php
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

To handle delivery callbacks from your transport provider, register a callback handler with the ``mautic.sms_callback_handler`` tag.

.. vale off

Example transport implementation
================================

.. vale on

The following example shows an SMS transport implementing all three interfaces.

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
       public function sendSms(Lead $lead, string $content)
       {
           $phone = $lead->getPhone();
           if (empty($phone)) {
               return 'No phone number available';
           }

           // Send SMS through your provider
           // Return true on success or an error message
           return true;
       }

       public function sendBatchSms(RecipientCollection $collection, string $content): RecipientCollection
       {
           foreach ($collection as $recipient) {
               $lead = $recipient->getLead();
               // Get token substitution data for this recipient
               $tokens = $recipient->getSubstitutionData();

               // Send to your provider
               $success = $this->sendToProvider($lead, $content);

               // Mark the result
               $recipient->setResult($success);
           }

           return $collection;
       }

       public function sendMms(Lead $lead, string $content, array $media)
       {
           // Send MMS with media attachments
           return true;
       }
   }

Recipient data structures
*************************

When using bulk SMS, Mautic provides data structures to manage recipient lists and token substitution.

.. vale off

SmsRecipientDTO
===============

.. vale on

The ``SmsRecipientDTO`` wraps each Contact with token substitution data.

.. code-block:: php

   <?php

   namespace Mautic\SmsBundle\Helper\DTO;

   use Mautic\LeadBundle\Entity\Lead;

   final class SmsRecipientDTO implements \JsonSerializable
   {
       public function getKey(): int;      // Returns the lead ID
       public function getLead(): Lead;    // Returns the contact entity
       public function getResult(): bool;  // Check if send succeeded
       public function setResult(bool $result): void;  // Set the send result
       public function getSubstitutionData(): array;   // Get token values for this contact
   }

.. vale off

RecipientCollection
===================

.. vale on

The ``RecipientCollection`` is a typed collection of ``SmsRecipientDTO`` objects that implements ``ArrayIterator``.

.. code-block:: php

   <?php

   namespace Mautic\SmsBundle\Collection;

   final class RecipientCollection extends \ArrayIterator
   {
       public function toChoices(): array;                    // Convert to choices array
       public function getFieldByKey(int $key): SmsRecipientDTO;  // Get recipient by lead ID
   }

Contact filtering events
************************

Three events fire sequentially during SMS sending to filter Contacts before dispatch. Use these events to exclude Contacts based on custom criteria.

.. vale off

Do Not Contact filter
=====================

Use ``SmsEvents::DNC_FILTER_CONTACTS_ON_SEND`` to filter Contacts based on **Do Not Contact** status.

.. vale on

.. code-block:: php

   <?php

   use Mautic\SmsBundle\Event\DncEvent;
   use Mautic\SmsBundle\SmsEvents;
   use Symfony\Component\EventDispatcher\EventSubscriberInterface;

   class SmsFilterSubscriber implements EventSubscriberInterface
   {
       public static function getSubscribedEvents(): array
       {
           return [
               SmsEvents::DNC_FILTER_CONTACTS_ON_SEND => ['onDncFilter', 0],
           ];
       }

       public function onDncFilter(DncEvent $event): void
       {
           $contacts = $event->getContacts();

           foreach ($contacts as $id => $contact) {
               if ($this->shouldExclude($contact)) {
                   $event->removeContact($id);
               }
           }
       }
   }

Queue filter
============

Use ``SmsEvents::QUEUE_FILTER_CONTACTS_ON_SEND`` to filter contacts based on frequency rules or queueing logic.

.. code-block:: php

   <?php

   use Mautic\SmsBundle\Event\QueueEvent;
   use Mautic\SmsBundle\SmsEvents;

   // In your subscriber
   public static function getSubscribedEvents(): array
   {
       return [
           SmsEvents::QUEUE_FILTER_CONTACTS_ON_SEND => ['onQueueFilter', 0],
       ];
   }

   public function onQueueFilter(QueueEvent $event): void
   {
       // Filter contacts based on frequency rules
   }

Generic filter
==============

Use ``SmsEvents::FILTER_CONTACTS_ON_SEND`` for any remaining filtering logic, such as removing Contacts without phone numbers.

.. code-block:: php

   <?php

   use Mautic\SmsBundle\Event\FilterEvent;
   use Mautic\SmsBundle\SmsEvents;

   // In your subscriber
   public static function getSubscribedEvents(): array
   {
       return [
           SmsEvents::FILTER_CONTACTS_ON_SEND => ['onFilter', 0],
       ];
   }

   public function onFilter(FilterEvent $event): void
   {
       // Remove contacts that shouldn't receive SMS
       $removedContacts = $event->getRemovedContacts();
   }

All three event classes share a common API:

* ``getContacts()`` - Returns the array of Contacts
* ``removeContact(int $id)`` - Remove a single Contact by ID
* ``removeContacts(array $contacts)`` - Remove multiple Contacts
* ``getRemovedContacts()`` - Get the list of removed Contacts

.. vale off

Campaign SMS events
*******************

.. vale on

When integrating SMS with Campaigns, use the batch Campaign action event for better performance.

Batch action event
==================

Use ``SmsEvents::ON_CAMPAIGN_TRIGGER_BATCH_ACTION`` to handle Campaign SMS actions.

.. code-block:: php

   <?php

   use Mautic\CampaignBundle\Event\CampaignBuilderEvent;
   use Mautic\CampaignBundle\CampaignEvents;
   use Mautic\SmsBundle\SmsEvents;
   use Symfony\Component\EventDispatcher\EventSubscriberInterface;

   class CampaignSubscriber implements EventSubscriberInterface
   {
       public static function getSubscribedEvents(): array
       {
           return [
               CampaignEvents::CAMPAIGN_ON_BUILD => ['onCampaignBuild', 0],
           ];
       }

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
   }

Deprecation notice
==================

.. deprecated:: 7.0

   Mautic deprecates ``SmsEvents::ON_CAMPAIGN_TRIGGER_ACTION``. Use ``SmsEvents::ON_CAMPAIGN_TRIGGER_BATCH_ACTION`` instead for improved performance with batch contact processing.

.. vale off

SMS event constants
*******************

.. vale on

The ``SmsEvents`` class defines all SMS-related event constants:

.. vale off

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Event constant
     - Description
   * - ``ON_CAMPAIGN_TRIGGER_BATCH_ACTION``
     - Fires when a Campaign triggers an SMS action for a batch of Contacts.
   * - ``ON_CAMPAIGN_TRIGGER_ACTION``
     - **Deprecated.** Legacy event for single-Contact Campaign SMS actions.
   * - ``DNC_FILTER_CONTACTS_ON_SEND``
     - Fires to filter Contacts based on **Do Not Contact** status.
   * - ``QUEUE_FILTER_CONTACTS_ON_SEND``
     - Fires to filter Contacts based on frequency rules.
   * - ``FILTER_CONTACTS_ON_SEND``
     - Fires for generic Contact filtering before SMS dispatch.

.. vale on
