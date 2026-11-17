Form submit event
################# 

Triggered when a Contact submits a Mautic Form.

.. _form_submit_event_type:

Event type
**********

``mautic.form_on_submit``

.. _form_submit_event_properties:

Event properties
****************

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``submission``
      - object
      - :ref:`Submission object<Webhooks/events/form_on_submit:Submission properties>`
    * - ``timestamp``
      - string
      - Date/time the event occurred in ISO 8601 format.

Submission properties
*********************

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``id``
      - int
      - ID of the Submission.
    * - ``ipAddress``
      - object
      - :ref:`IP address basic object<Webhooks/events/form_on_submit:IP address basic properties>` for the Contact when they submitted the Form.
    * - ``form``
      - object
      - :ref:`Form basic object<Webhooks/events/form_on_submit:Form basic properties>`.
    * - ``lead``
      - object
      - The Contact who submitted the Form. Contains only the Contact's ``id``, ``points``, ``color``, and ``fields``. See :ref:`Contact object<Webhooks/events/lead_post_save_new:Contact properties>` for these properties.
    * - ``trackingId``
      - string
      - Generated ID for the tracking session.
    * - ``dateSubmitted``
      - string
      - Date/time the submission occurred in ISO 8601 format.
    * - ``referer``
      - string
      - URL the Form submitted from.
    * - ``results``
      - object
      - Key/value pairs with Form field API names as the keys and submitted values.
    * - ``page``
      - object|null
      - :ref:`Landing Page basic object<Webhooks/events/page_on_hit:Landing Page basic properties>` if the Contact submitted the Form when embedded on a Landing Page. Otherwise, ``null``.

Form basic properties
*********************

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``id``
      - int
      - ID of the Form
    * - ``name``
      - string
      - Name of the Form
    * - ``alias``
      - string
      - API name for the Form
    * - ``category``
      - object|null
      - Empty object if the Form has a Category. Otherwise, ``null``.

IP address basic properties
***************************

.. list-table::
    :header-rows: 1

    * - ``ipAddress``
      - string
      - IP address for the Contact.
    * - ``id``
      - int
      - ID of the IP address stored in Mautic's database.
    * - ``ipDetails``
      - object|null
      - Details of the IP address populated from the configured IP lookup service.