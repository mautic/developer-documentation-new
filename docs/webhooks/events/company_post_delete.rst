Company deleted event
#####################

Triggered when Mautic deletes a Company.

.. _company_deleted_updated_event_type:

Event type
**********

``mautic.company_post_delete``

.. _company_deleted_updated_event_properties:

Event properties
****************

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``id``
      - int
      - ID of the deleted Company
    * - ``company``
      - object
      - :ref:`Company object<webhooks/events/company_post_save:Company properties>`. Note that ``id`` is null in this context. Use the ``id`` in the event instead.
    * - ``timestamp``
      - string
      - Date/time the event occurred in ISO 8601 format.