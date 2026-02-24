Contact deleted event
#####################

Triggered when Mautic deletes a Contact.

.. _contact_deleted_event_type:

Event type
**********

``mautic.lead_post_delete``

.. _contact_deleted_event_properties:

Event properties
****************

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``id``
      - int
      - ID of the deleted Contact
    * - ``company``
      - object
      - :ref:`Contact object<webhooks/events/lead_post_save_new:Contact properties>`. Note that ``id`` is null in this context. Use the ``id`` in the event instead.
    * - ``timestamp``
      - string
      - Date/time the event occurred in ISO 8601 format.