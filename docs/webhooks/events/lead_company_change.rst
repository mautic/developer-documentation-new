Contact Company subscription change event
#########################################

Triggered when Mautic adds or removes a Contact to/from a Company.

.. _company_subscription_change_event_type:

Event type
**********

``mautic.lead_company_change``

.. _company_subscription_change_event_properties:

Event properties
****************

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``added``
      - boolean
      - ``TRUE`` if Contact added to the Company. ``FALSE`` if removed.
    * - ``contact``
      - object
      - :ref:`Contact object<Contact properties>`.
    * - ``company``
      - object
      - :ref:`Company object<Company properties>`.
    * - ``timestamp``
      - string
      - Date/time the event occurred in ISO 8601 format.