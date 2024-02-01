Contact Points changed event
############################

Triggered when Mautic modifies a Contact's points.

.. _contact_points_changed_event_type:

Event type
**********

``mautic.lead_points_change``

.. _contact_points_changed_event_properties:

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