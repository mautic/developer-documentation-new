Email send event
----------------
Triggered when an Mautic sends an Email to a Contact.

Event type
""""""""""""""""""
``mautic.email_on_send``

Event properties
""""""""""""""""""

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``email``
      - object
      - :ref:`Email object<Email properties>`
    * - ``contact``
      - object
      - :ref:`Contact object<Contact properties>`
    * - ``tokens``
      - object
      - Key/value pairs of personalized tokens and values for the Contact.
    * - ``contentHash``
      - string
      - Identifies the unique Email templated content.
    * - ``idHash``
      - string
      - Unique to the specific Email send to the Contact.
    * - ``content``
      - string
      - The HTML sent to the Contact.
    * - ``subject``
      - string
      - The rendered subject of the Email sent to the Contact.
    * - ``source``
      - array
      - The Component that sent the Email. Key 0 is the Component and key 1 is the ID if applicable. For example, if a Campaign sent the email, this value will be ``['campaign.event', 1]`` which means that Campaign Event ID 1 sent the Email.
    * - ``headers``
      - object
      - Key/value pairs of headers set on the Email sent to the Contact.
    * - ``timestamp``
      - string
      - Date/time the event occurred in ISO 8601 format.

.. _Email properties:

Email properties
"""""""""""""""""""

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``id``
      - int
      - ID of the Email
    * - ``isPublished``
      - boolean
      - Published state of the Email.
    * - ``dateAdded``
      - string
      - Date/time the Email was created in ISO 8601 format.
    * - ``createdBy``
      - int|null
      - The ID of the User who created the Email.
    * - ``createdByUser``
      - string|null
      - Name of the User that created the Email.
    * - ``dateModified``
      - string|null
      - Date/time the Email was last modified in ISO 8601 format or null if it has not been modified.
    * - ``modifiedBy``
      - int|null
      - The ID of the User who last modified the Email or null if it has not been modified.
    * - ``modifiedByUser``
      - string|null
      - Name of the User that last modified the Email if applicable. Otherwise null.
    * - ``name``
      - string
      - Internal name of the Email.
    * - ``subject``
      - string
      - Subject of the Email.
    * - ``language``
      - string
      - Locale for the Email content.
    * - ``category``
      - object
      - :ref:`Category object<Category properties>`
    * - ``fromAddress``
      - string|null
      - A custom from address if configured.
    * - ``fromName``
      - string|null
      - A custom from name if configured.
    * - ``replyToAddress``
      - string|null
      - A custom reply to address if configured.
    * - ``useOwnerAsMailer``
      - boolean
      - True if a Contact's Owner should be set as the Email's from address and name.
    * - ``customHtml``
      - string
      - HTML template for the Email.
    * - ``plainText``
      - string|null
      - Plain text for the email.
    * - ``template``
      - string
      - The Mautic theme used as the originating content.
    * - ``emailType``
      - string
      - Type of Email. Options are ``template`` and ``list`` (broadcast).
    * - ``readCount``
      - int
      - The number of times the Email has been opened.
    * - ``sentCount``
      - int
      - The number of times the Email has been sent.
    * - ``revision``
      - int
      - The number of times the Email has been edited.
    * - ``dynamicContent``
      - object[]
      - Array of objects that contain the Dynamic Content configured as tokens for the Email.
    * - ``utmTags``
      - object
      -
    * - ``publishUp``
      - string|null
      -
    * - ``publishDown``
      - string|null
      -
    * - ``assetAttachments``
      - array
      -
    * - ``variantStartDate``
      - string|null
      -
    * - ``variantSentCount``
      - int
      -
    * - ``variantReadCount``
      - int
      -
    * - ``variantParent``
      - object|null
      -
    * - ``variantChildren``
      - array
      -
    * - ``translationParent``
      - object|null
      -
    * - ``translationChildren``
      - array
      -
    * - ``unsubscribeForm``
      - object|null
      -
    * - ``lists``
      - array
      -
    * - ``headers``
      - array
      -

.. _Category properties:

Category properties
"""""""""""""""""""

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``id``
      - int
      - ID of the Category
    * - ``title``
      - string
      - Title of the Category.
    * - ``alias``
      - string
      - API name of the Category.
    * - ``description``
      - string
      - Description of the Category.
    * - ``color``
      - string
      - Hex code for the configured color for the Category.
    * - ``bundle``
      - string
      - The Component or Channel the Category is applicable. Can also be ``global``.
    * - ``createdByUser``
      - string
      - Name of the User that created the Category.
    * - ``modifiedByUser``
      - string|null
      - Name of the User who last updated the Category. Null if it has not been modified.