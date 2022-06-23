Email send event
################

Triggered when an Mautic sends an Email to a Contact.

Event type
**********

``mautic.email_on_send``

Event properties
****************

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
      - Identifies the unique Email content including template.
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
      - The Component that sent the Email. Key 0 is the Component and key 1 is the ID if applicable. For example, if a Campaign sent the Email, this value is ``['campaign.event', 1]`` which means that Campaign Event ID 1 sent the Email.
    * - ``headers``
      - object
      - Key/value pairs of headers set on the Email sent to the Contact.
    * - ``timestamp``
      - string
      - Date/time the event occurred in ISO 8601 format.

Email properties
****************

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
      - Date/time of Email creation in ISO 8601 format.
    * - ``createdBy``
      - int|null
      - The ID of the User who created the Email.
    * - ``createdByUser``
      - string|null
      - Name of the User that created the Email.
    * - ``dateModified``
      - string|null
      - Date/time the Email was last modified in ISO 8601 format or null if not modified.
    * - ``modifiedBy``
      - int|null
      - The ID of the User who last modified the Email or null if not modified.
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
      - TRUE if a Contact's Owner should the Email's from address and name.
    * - ``customHtml``
      - string
      - HTML template for the Email.
    * - ``plainText``
      - string|null
      - Plain text for the Email.
    * - ``template``
      - string
      - The Mautic Theme used as the originating content.
    * - ``emailType``
      - string
      - Type of Email. Options are ``template`` and ``list`` - broadcast.
    * - ``readCount``
      - int
      - The number of opens for the Email.
    * - ``sentCount``
      - int
      - The number of sends for the Email.
    * - ``revision``
      - int
      - The number of edits for the Email.
    * - ``dynamicContent``
      - object[]
      - Array of objects that contain the Dynamic Content configured as tokens for the Email.
    * - ``utmTags``
      - object
      - Key/value pairs of UTM Tags as keys. Mautic supports the following keys: ``utmSource``, ``utmMedium``, ``utmCampaign``, and ``utmContent``. Values are strings or null.
    * - ``publishUp``
      - string|null
      - Date/time for publishing the Email in ISO 8601 format. ``null`` to consider the Email published if now is before ``publishDown``, if applicable.
    * - ``publishDown``
      - string|null
      - Date/time for unpublishing the Email in ISO 8601 format. ``null`` to consider the Email published if now is after ``publishUp``, if applicable.
    * - ``assetAttachments``
      - array
      - Array of :ref:`Asset objects<Asset properties>`.
    * - ``variantStartDate``
      - string|null
      - Date/time the Email started to track A/B test statistics. ``null`` if the Email isn't part of an A/B test.
    * - ``variantSentCount``
      - int
      - The number of times sent since the last edit to an A/B test Email.
    * - ``variantReadCount``
      - int
      - The number of times read since the last edit to an A/B test Email.
    * - ``variantParent``
      - object|null
      - :ref:`Email object<Email properties>`. The A test for an Email configured as an A/B test.
    * - ``variantChildren``
      - array
      - Array of  :ref:`Email objects<Email properties>`. The B, C, D, and so forth tests for an Email configured as an A/B test.
    * - ``translationParent``
      - object|null
      - :ref:`Email object<Email properties>`. The main translation of an Email configured to be a translation of another.
    * - ``translationChildren``
      - array
      - Array of :ref:`Email objects<Email properties>`. The translations of an Email configured to be a translation of another.
    * - ``unsubscribeForm``
      - object|null
      - :ref:`Unsubscribe Form object<Unsubscribe Form properties>`.
    * - ``lists``
      - array
      - :ref:`Segment object<Segment properties>`.
    * - ``headers``
      - array
      - Key/value pairs of header templates configured for the Email.

Category properties
*******************

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
      - Name of the User who last updated the Category. Null if not modified.

Asset properties
****************

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``id``
      - int
      - ID of the Asset.
    * - ``title``
      - string
      - Title of the Asset.
    * - ``alias``
      - string
      - API name of the Asset.
    * - ``description``
      - string
      - Description of the Asset.
    * - ``category``
      - object
      - :ref:`Category object<Category properties>`
    * - ``revision``
      - int
      - The number of edits of the Asset.
    * - ``language``
      - string
      - The configured locale for the Asset.
    * - ``storageLocation``
      - string
      - ``local`` if an uploaded file. ``remote`` if hosted elsewhere, with the URL is available through ``downloadUrl``.
    * - ``downloadUrl``
      - string|null
      - The URL of the Asset if ``storageLocation`` is ``remote``. ``null`` if stored locally.
    * - ``extension``
      - string
      - File extension for the Asset.
    * - ``mime``
      - string
      - File type for the Asset.
    * - ``size``
      - int
      - File size in bytes.
    * - ``downloadCount``
      - int
      - Total number of downloads of the Asset.
    * - uniqueDownloadCount
      - int
      - Number of Contacts that has downloaded the Asset at least once.
    * - ``disallow``
      - boolean
      - ``TRUE`` if bots have access to index the Asset. ``FALSE`` otherwise. Applicable only for local Assets.

Segment properties
******************

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``id``
      - int
      - ID of the Segment.
    * - ``name``
      - string
      - Name of the Segment.
    * - ``publicName``
      - string
      - Name displayed in the Preference Center if ``isGlobal`` and ``isPreferenceCenter`` are ``TRUE``.
    * - ``alias``
      - string
      - API name of the Segment.
    * - ``description``
      - string
      - Description of the Segment.
    * - ``category``
      - object
      - :ref:`Category object<Category properties>`
    * - ``createdByUser``
      - string
      - The name of the User that created the Segment.
    * - ``modifiedByUser``
      - string|null
      - The name of the User that last modified the Segment. ``null`` if never modified.
    * - ``isGlobal``
      - boolean
      - ``TRUE`` if configured to be a Public Segment. ``FALSE`` otherwise.
    * - ``isPreferenceCenter``
      - boolean
      - ``TRUE`` if configured to display in the Preference Center for Contact Segments. ``FALSE`` otherwise.
    * - ``filters``
      - array
      - Array of :ref:`Segment filter objects<Segment filter properties>`.

Segment filter properties
*************************

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``glue``
      - string
      - Notes how the filter relates to the filter before it. Options are ``and`` or ``or``. ``and``  groups the filter with the previous filters. ``or`` starts a new group.
    * - ``field``
      - string
      - The field type for the filter. For example, it could be a custom field filter such as ``email``. Or it could be a behavioral based filter such as ``lead_asset_download``.
    * - ``object``
      - string
      - Object the filter's data belongs to. Currently supported values are ``lead`` for Contact and ``company``.
    * - ``type``
      - string
      - The filter's field type that corresponds with the underlying data. Current options are ``boolean``, ``date``, ``datetime``, ``email``, ``country``, ``locale``, ``number``, ``tel``, ``region``, ``select``, ``multiselect``, ``text``, ``textarea``, ``time``, ``timezone``, and ``url``.
    * - ``filter``
      - mixed
      - The value of the filter.
    * - ``display``
      - mixed
      - Value that displays in the UI for a lookup type field. For example, ``display`` may be a User's name where ``filter`` is the ID of the User.
    * - ``operator``
      - string
      - The comparison operator for the filter. Available values vary based on what the filter supports and includes ``=``, ``!=``, ``gt``, ``gte``, ``lt``, ``lte``, ``like``, ``!like``, ``startsWith``, ``endsWith``, ``contains``, ``empty``, ``!empty``, ``in``, ``!in``, and ``regexp``, ``!regexp``.

.. vale off 

Unsubscribe Form properties
***************************

.. vale on

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``id``
      - int
      - ID of the Form.
    * - ``name``
      - string
      - Title of the Form.
    * - ``alias``
      - string
      - API name of the Form.
    * - ``description``
      - string
      - Description of the Form.
    * - ``category``
      - object
      - :ref:`Category object<Category properties>`
    * - ``createdByUser``
      - string
      - Name of the User that created the Form.
    * - ``modifiedByUser``
      - string|null
      - Name of the User who last updated the Form. Null if not modified.
    * - ``publishUp``
      - string|null
      - Date/time for publishing the Form in ISO 8601 format. ``null`` to consider the Form published if now is before ``publishDown``, if applicable.
    * - ``publishDown``
      - string|null
      - Date/time for unpublishing the Form in ISO 8601 format. ``null`` to consider the Form published if now is after ``publishUp``, if applicable.
    * - ``cachedHtml``
      - string
      - Cached rendered HTML for the Form.
    * - ``template``
      - string|null
      - Custom Mautic Theme used to style the Preview page or customize Form fields. See :ref:`Customizing forms`.
    * - ``formType``
      - string
      - Applicable values are ``standalone`` or ``campaign``.
    * - ``postAction``
      - string
      - Notes the behavior of the Form after submission. Current supported values are ``return``, ``redirect``, and ``message``.
    * - ``postActionProperty``
      - string|null
      - The URL to redirect a Contact to if ``postAction`` is ``redirect`` or the message to display to the Contact if ``postAction`` is ``message``.
    * - ``inKioskMode``
      - boolean
      - ``TRUE`` if Mautic has setting cookies for the tracked Contact turned off.
    * - ``renderStyle``
      - boolean
      - ``TRUE`` to render CSS styles from the configured ``template``.
    * - ``noIndex``
      - boolean
      - ``TRUE`` to ask bots to not track the Form's preview pages.
    * - ``formAttributes``
      - string|null
      - HTML attributes added to the <form> tag.
    * - ``fields``
      - array
      - Array of :ref:`Unsubscribe Form field objects<Unsubscribe Form field properties>`
    * - ``actions``
      - array
      - Array of :ref:`Unsubscribe Form action objects<Unsubscribe Form action properties>`

.. vale off

Unsubscribe Form field properties
*********************************

.. vale on

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``id``
      - int
      - ID of the Form field.
    * - ``alias``
      - string
      - API name for the Form field.
    * - ``label``
      - string
      - Label for the Form field.
    * - showLabel
      - boolean
      - ``TRUE`` to display the label in the Form's HTML.
    * - ``type``
      - string
      - The Form field's type. For example, ``email``.
    * - ``defaultValue``
      - mixed
      - Default value for the Form field.
    * - ``isRequired``
      - boolean
      - ``TRUE`` if required.
    * - ``validationMessage``
      - string|null
      - Message to display if empty when a mandatory field.
    * - ``helpMessage``
      - string|null
      - Message to display in the Form's HTML as instructions for the field.
    * - ``order``
      - int
      - Placement of the field within the order of Form fields.
    * - ``properties``
      - object
      - Mix of properties specific to the Form field's ``type``.
    * - ``labelAttributes``
      - string|null
      - HTML attributes to append to the field's label element.
    * - ``inputAttributes``
      - string|null
      - HTML attributes to append to the field's input element.
    * - ``containerAttributes``
      - string|null
      - HTML attributes to append to the field's wrapping element.
    * - ``leadField``
      - string|null
      - The Contact custom field to persist the data to upon submit.
    * - ``saveResult``
      - boolean
      - ``FALSE`` to prevent persisting the value to the database.
    * - ``isAutoFill``
      - boolean
      - ``TRUE`` to auto fill known values from the tracked Contact's profile.

.. vale off

Unsubscribe Form action properties
**********************************

.. vale on

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``id``
      - int
      - ID of the Form.
    * - ``name``
      - string
      - Name for the Form action.
    * - ``description``
      - string
      - Description for the Form action.
    * - ``type``
      - string
      - API name for the Form action. For example, ``lead.scorecontactscompanies``.
    * - ``order``
      - int
      - Placement of the action within the order of execution for the Form actions.
    * - ``properties``
      - object
      - Mix of properties specific to the Form action's ``type``.