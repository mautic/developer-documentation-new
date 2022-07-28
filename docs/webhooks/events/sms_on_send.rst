Text send event
###############

Triggered when Mautic sends a Text Message to a Contact.

.. _sms_on_send_event_type:

Event type
**********

``mautic.sms_on_send``

.. _sms_on_send_event_properties:

Event properties
****************

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``smsId``
      - int
      - ID of the SMS sent.
    * - ``contact``
      - object
      - :ref:`Contact object<Contact properties>`.
    * - ``content``
      - string
      - Content of the SMS sent to the Contact.
    * - ``timestamp``
      - string
      - Date/time the event occurred in ISO 8601 format.