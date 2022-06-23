Contact deleted event
#####################

Triggered when Mautic deletes a Contact.

Event type
**********

``mautic.lead_post_delete``

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
      - :ref:`Contact object<Contact properties>`. Note that ``id`` will be null in this context. Use the ``id`` in the event instead.
    * - ``timestamp``
      - string
      - Date/time the event occurred in ISO 8601 format.