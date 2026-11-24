Contact Segment membership change event
#######################################

Triggered when Mautic adds a Contact to a Segment or removes a Contact from a Segment. Mautic sends this event whether a User or an automated action, such as a Campaign action, changes the membership, and when the ``mautic:segments:update`` command rebuilds a Segment. Mautic queues one payload for each Contact that joins or leaves the Segment. Deleting a Segment doesn't trigger this event for its Contacts.

.. _segment_membership_change_event_type:

Event type
**********

``mautic.lead_list_change``

To subscribe a Webhook to this event, select **Contact Segment Membership Change Event** when you create or edit the Webhook.

.. _segment_membership_change_event_properties:

Event properties
****************

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``contact``
      - object
      - :ref:`Contact object<webhooks/events/lead_post_save_new:Contact properties>`.
    * - ``segment``
      - object
      - The Segment the Contact joined or left. See :ref:`Segment properties <get Segment properties>`.
    * - ``action``
      - string
      - ``added`` if Mautic added the Contact to the Segment. ``removed`` if Mautic removed the Contact from the Segment.
    * - ``timestamp``
      - string
      - Date/time the event occurred in ISO 8601 format.
