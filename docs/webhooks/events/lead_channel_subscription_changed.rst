Contact channel subscription change event
----------------------------
Triggered when Mautic changes a Contact's channel subscription status.

Event type
""""""""""""""""""
``mautic.lead_channel_subscription_changed``

Event properties
""""""""""""""""""

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``contact``
      - object
      - :ref:`Contact object<Contact properties>`.
    * - ``channel``
      - string
      - The channel the Contact was unsubscribed from. Examples are ``email`` and ``sms``.
    * - ``old_status``
      - string
      - The Contact's original state for the given channel. Options are ``contactable``, ``bounced``, ``manual``, and ``unsubscribed``.
    * - ``new_status``
      - string
      - The Contact's new state for the given channel. Options are ``contactable``, ``bounced``, ``manual``, and ``unsubscribed``.
    * - ``timestamp``
      - string
      - Date/time the event occurred in ISO 8601 format.