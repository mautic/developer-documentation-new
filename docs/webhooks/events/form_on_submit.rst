Form submit event
--------------------
Triggered when a Contact submits a Mautic Form.

.. _Form submit event type:

Event type
""""""""""""""""""
``mautic.form_on_submit``

.. _Form submit event properties:

Event properties
""""""""""""""""""

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``submission``
      - object
      - :ref:`Submission object<Submission properties>`
    * - ``timestamp``
      - string
      - Date/time the event occurred in ISO 8601 format.

.. _Submission properties:

Submission properties
"""""""""""""""""""""

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
      - :ref:`IP address basic object<IP address basic properties>` for the Contact when they submitted the Form.
    * - ``form``
      - object
      - :ref:`Form basic object<Form basic properties>`.
    * - ``lead``
      - object
      - :ref:`Contact object<Contact properties>`.
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
      - :ref:`Landing Page basic object<Landing Page basic properties>` if the Contact submitted the Form from if the Form was embedded on a Landing Page. Otherwise, ``null``.

.. _Form basic properties:

Form basic properties
""""""""""""""""""""""

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
      - object
      - :ref:`Category object<Category properties>`

.. _IP address basic properties:

Form basic properties
"""""""""""""""""""""

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