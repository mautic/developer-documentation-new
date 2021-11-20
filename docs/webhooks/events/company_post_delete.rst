Company deleted event
----------------------------
Triggered when Mautic deletes a Company.

Event type
""""""""""""""""""
``mautic.company_post_delete``

Event properties
""""""""""""""""""

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``id``
      - ID of the deleted Company
    * - ``company``
      - object
      - :ref:`Company object<Company properties>`. Note that ``id`` will be null in this context. Use the ``id`` in the event instead.
    * - ``timestamp``
      - string
      - Date/time the event occurred in ISO 8601 format.