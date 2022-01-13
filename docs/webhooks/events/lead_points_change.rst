Contact points changed event
----------------------------
Triggered when Mautic modifies a Contact's points.

.. _Contact points changed event type:

Event type
""""""""""""""""""
``mautic.lead_points_change``

.. _Contact points changed event properties:

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
    * - ``points``
      - object
      - Contains the original Points and the new Points for the Contact.
    * - ``points.old_points``
      - int
      - The Contact's original Points.
    * - ``points.new_points``
      - int
      - The Contact's new Points.
    * - ``timestamp``
      - string
      - Date/time the event occurred in ISO 8601 format.