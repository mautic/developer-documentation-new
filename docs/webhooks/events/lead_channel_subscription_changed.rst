Contact channel subscription change event
#########################################

Triggered when Mautic changes a Contact's Channel subscription status.

.. _channel_subscription_changed_event_type:

Event type
**********

``mautic.lead_channel_subscription_changed``

.. _channel_subscription_changed_event_properties:

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
    * - ``channel``
      - string
      - The Channel unsubscribed from. Examples are ``email`` and ``sms``.
    * - ``old_status``
      - string
      - The Contact's original state for the given Channel. Options are ``contactable``, ``bounced``, ``manual``, and ``unsubscribed``.
    * - ``new_status``
      - string
      - The Contact's new state for the given Channel. Options are ``contactable``, ``bounced``, ``manual``, and ``unsubscribed``
    * - ``timestamp``
      - string
      - Date/time the event occurred in ISO 8601 format.