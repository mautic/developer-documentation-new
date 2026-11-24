Manipulating Contacts
#####################

Many Plugins that extend Mautic manipulate Contacts in some way. This guide shows you how to read the currently tracked Contact and how to create and merge Contacts from your own code.

.. note::

   Mautic originally called Contacts ``leads``. Much of the code still refers to Contacts as ``leads`` - for example, the ``lead`` model key and the ``Mautic\LeadBundle\Entity\Lead`` entity.

.. vale off

Reading and setting the tracked Contact
***************************************

.. vale on

Inject ``Mautic\LeadBundle\Tracker\ContactTracker`` to read or set the currently tracked Contact. These methods used to live on ``LeadModel``, but they now belong to the tracker service.

.. code-block:: php

    <?php

    use Mautic\LeadBundle\Entity\Lead;
    use Mautic\LeadBundle\Tracker\ContactTracker;

    final class ExampleService
    {
        public function __construct(private ContactTracker $contactTracker)
        {
        }

        public function example(): void
        {
            // Get the currently tracked Contact, or null when there isn't one.
            $currentContact = $this->contactTracker->getContact();

            // Get the tracking ID for the current device or session.
            $trackingId = $this->contactTracker->getTrackingId();

            // Set the currently tracked Contact and generate tracking cookies.
            $contact = new Lead();
            // ...
            $this->contactTracker->setTrackedContact($contact);

            // Set a Contact for system use - for events that call getContact() - without generating tracking cookies.
            $this->contactTracker->setSystemContact($contact);
        }
    }

Contact tracking
****************

Mautic tracks Contacts with two cookies. The first records the ID that Mautic tracks the Contact under. The second tracks the Contact's activity for the current session. It defaults to 30 minutes and resets on each interaction. The ``mautic_session_id`` holds the Contact's current session ID, which in turn names the cookie that holds the Contact's ID.

Mautic also places a cookie named ``mtc_id`` on any domain with ``mtc.js`` embedded that its CORS settings allow. This cookie contains the ID of the currently tracked Contact.

.. vale off

Creating and merging Contacts
*****************************

.. vale on

To create a new Contact, use the ``Mautic\LeadBundle\Entity\Lead`` entity and save it through ``Mautic\LeadBundle\Model\LeadModel``. Before you save, you can inspect the unique identifier fields to detect an existing Contact and merge the two through ``Mautic\LeadBundle\Deduplicate\ContactMerger``:

.. code-block:: php

    <?php

    use Mautic\CoreBundle\Helper\IpLookupHelper;
    use Mautic\LeadBundle\Deduplicate\ContactMerger;
    use Mautic\LeadBundle\Deduplicate\Exception\SameContactException;
    use Mautic\LeadBundle\Entity\Lead;
    use Mautic\LeadBundle\Field\FieldsWithUniqueIdentifier;
    use Mautic\LeadBundle\Model\LeadModel;

    final class ExampleContactCreator
    {
        public function __construct(
            private LeadModel $leadModel,
            private ContactMerger $contactMerger,
            private FieldsWithUniqueIdentifier $fieldsWithUniqueIdentifier,
            private IpLookupHelper $ipLookupHelper,
        ) {
        }

        public function create(): Lead
        {
            // Generate a completely new Contact.
            $contact = new Lead();
            $contact->setNewlyCreated(true);

            // The new or updated field values.
            $contactFields = [
                'firstname' => 'Bob',
                // ...
            ];

            // Optionally check the identifier fields to find an existing Contact.
            $uniqueFields    = $this->fieldsWithUniqueIdentifier->getFieldsWithUniqueIdentifier();
            $uniqueFieldData = array_intersect_key($contactFields, $uniqueFields);

            if ($uniqueFieldData) {
                $existingContacts = $this->leadModel
                    ->getRepository()
                    ->getLeadsByUniqueFields($uniqueFieldData);

                if (!empty($existingContacts)) {
                    try {
                        // A match was found, so merge the two Contacts.
                        $contact = $this->contactMerger->merge($contact, $existingContacts[0]);
                    } catch (SameContactException) {
                        // The winner and loser are the same Contact - nothing to merge.
                    }
                }
            }

            // Associate the request's IP address. addIpAddress() ignores IPs excluded in the Configuration.
            $ipAddress = $this->ipLookupHelper->getIpAddress();
            if (!$contact->getIpAddresses()->contains($ipAddress)) {
                $contact->addIpAddress($ipAddress);
            }

            // Set the Contact's field values and save the entity.
            $this->leadModel->setFieldValues($contact, $contactFields);
            $this->leadModel->saveEntity($contact);

            return $contact;
        }
    }
