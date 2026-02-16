.. vale off

.. note::

  The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

  If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

  Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Emails
######

Use this endpoint to manipulate and obtain details on Mautic's Emails.

**Using Mautic's API Library**

You can interact with this API through the :xref:`Mautic API Library` as follows, or use the various http endpoints as described in this document.

.. code-block:: php

   <?php
   use Mautic\MauticApi;
   use Mautic\Auth\ApiAuth;

   // ...
   $initAuth = new ApiAuth();
   $auth     = $initAuth->newAuth($settings);
   $apiUrl   = "https://example.com";
   $api      = new MauticApi();
   $emailApi = $api->newApi("emails", $auth, $apiUrl);

.. vale off

Get Email
*********

.. vale on

.. code-block:: php

   <?php

   //...
   $email = $emailApi->get($id);

Get an individual Email by ID.

.. vale off

HTTP request
============

.. vale on

``GET /emails/ID``

Response
========

``Expected Response Code: 200``

.. code-block:: json

   {
       "email": {
           "isPublished": true,
           "dateAdded": "2017-02-03T16:51:06+00:00",
           "dateModified": "2017-02-03T19:11:54+00:00",
           "createdBy": 1,
           "createdByUser": "John Doe",
           "modifiedBy": 1,
           "modifiedByUser": "John Doe",
           "id": 1,
           "name": "API Test Email",
           "subject": "Email created via API",
           "fromAddress": "test@example.com",
           "fromName": "Test From Name",
           "replyToAddress": "reply@example.com",
           "bccAddress": "bcc@example.com",
           "useOwnerAsMailer": false,
           "template": "blank",
           "content": [],
           "utmTags": [],
           "plainText": "Plain text content here",
           "customHtml": "<h1>Custom HTML content</h1>",
           "emailType": "list",
           "translationChildren": [],
           "translationParent": null,
           "variantChildren": [],
           "variantParent": null,
           "variantSettings": [],
           "variantStartDate": null,
           "publishUp": null,
           "publishDown": null,
           "readCount": 0,
           "sentCount": 0,
           "revision": 1,
           "category": null,
           "lists": [
               {
                   "createdByUser": "John Doe",
                   "modifiedByUser": "John Doe",
                   "id": 2,
                   "name": "Test Segment",
                   "alias": "test-segment",
                   "description": "Description for test segment"
               }
           ],
           "language": "en",
           "publicPreview": false,
           "assetAttachments": [],
           "unsubscribeForm": null,
           "preferenceCenter": null,
           "dynamicContent": [],
           "variantSentCount": 0,
           "variantReadCount": 0,
           "headers": []
       }
   }

Email properties
----------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Email
   * - ``name``
     - string
     - Name of the Email
   * - ``subject``
     - string
     - Subject of the Email
   * - ``fromAddress``
     - string
     - From email address
   * - ``fromName``
     - string
     - From name
   * - ``replyToAddress``
     - string
     - Reply-to email address
   * - ``bccAddress``
     - string
     - BCC email address
   * - ``useOwnerAsMailer``
     - boolean
     - Whether to use the Contact owner as the mailer
   * - ``template``
     - string
     - Template used for the Email
   * - ``content``
     - array
     - Array of content for the template
   * - ``utmTags``
     - array
     - Array of UTM tags for tracking
   * - ``plainText``
     - string
     - Plain text version of the Email
   * - ``customHtml``
     - string
     - Custom HTML content of the Email
   * - ``emailType``
     - string
     - Type of the Email - ``list`` or ``template``
   * - ``publishUp``
     - datetime/null
     - Date/time when the Email should be published
   * - ``publishDown``
     - datetime/null
     - Date/time when the Email should be unpublished
   * - ``readCount``
     - int
     - Number of times the Email was read
   * - ``sentCount``
     - int
     - Number of times the Email was sent
   * - ``revision``
     - int
     - Revision number of the Email
   * - ``category``
     - object/null
     - Category the Email belongs to
   * - ``lists``
     - array
     - Array of Segments/Lists the Email is assigned to
   * - ``language``
     - string
     - Language of the Email
   * - ``publicPreview``
     - boolean
     - Whether the Email has public preview enabled
   * - ``assetAttachments``
     - array
     - Array of assets attached to the Email
   * - ``unsubscribeForm``
     - object/null
     - Unsubscribe form associated with the Email
   * - ``preferenceCenter``
     - object/null
     - Preference center page associated with the Email
   * - ``dynamicContent``
     - array
     - Array of dynamic content variants
   * - ``variantSentCount``
     - int
     - Number of times Email variants were sent
   * - ``variantReadCount``
     - int
     - Number of times Email variants were read
   * - ``headers``
     - array
     - Array of custom headers
   * - ``isPublished``
     - boolean
     - Published state
   * - ``dateAdded``
     - datetime
     - Date/time Email was created
   * - ``createdBy``
     - int
     - ID of the User that created the Email
   * - ``createdByUser``
     - string
     - Name of the User that created the Email
   * - ``dateModified``
     - datetime/null
     - Date/time Email was last modified
   * - ``modifiedBy``
     - int
     - ID of the User that last modified the Email
   * - ``modifiedByUser``
     - string
     - Name of the User that last modified the Email

.. vale off

List Emails
***********

.. vale on

.. code-block:: php

   <?php

   //...
   $emails = $emailApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

Returns a list of contact Emails available to the User. This list is filterable and sortable.

.. vale off

HTTP request
============

.. vale on

``GET /emails``

Query parameters
----------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Name
     - Description
   * - ``search``
     - String or search command to filter entities by.
   * - ``start``
     - Starting row for the entities returned. Defaults to 0.
   * - ``limit``
     - Limit number of entities to return. Defaults to the system configuration for pagination, which is 30 by default.
   * - ``orderBy``
     - Column to sort by. Can use any column listed in the response. However, you need to change all properties in the response written in ``camelCase`` a bit. Before every capital, add an underscore - ``_`` - and then change the capital letters to non-capital letters. So ``dateAdded`` becomes ``date_added``, ``modifiedBy`` becomes ``modified_by``, etc.
   * - ``orderByDir``
     - Sort direction: ``asc`` or ``desc``.
   * - ``publishedOnly``
     - Only return currently published entities.
   * - ``minimal``
     - Return only array of entities without additional lists in it.

Response
========

``Expected Response Code: 200``

.. code-block:: json

   {
       "total": 1,
       "emails": {
           "1": {
               "isPublished": true,
               "dateAdded": "2017-02-03T16:51:06+00:00",
               "dateModified": "2017-02-03T19:11:54+00:00",
               "createdBy": 1,
               "createdByUser": "John Doe",
               "modifiedBy": 1,
               "modifiedByUser": "John Doe",
               "id": 1,
               "name": "API Test Email",
               "subject": "Email created via API",
               "fromAddress": "test@example.com",
               "fromName": "Test From Name",
               "replyToAddress": "reply@example.com",
               "bccAddress": "bcc@example.com",
               "useOwnerAsMailer": false,
               "template": "blank",
               "content": [],
               "utmTags": [],
               "plainText": "Plain text content here",
               "customHtml": "<h1>Custom HTML content</h1>",
               "emailType": "list",
               "publishUp": null,
               "publishDown": null,
               "readCount": 0,
               "sentCount": 0,
               "revision": 1,
               "category": null,
               "lists": [
                   {
                       "id": 2,
                       "name": "Test Segment",
                       "alias": "test-segment",
                       "description": "Description for test segment"
                   }
               ],
               "language": "en",
               "publicPreview": false,
               "assetAttachments": [],
               "unsubscribeForm": null,
               "preferenceCenter": null,
               "dynamicContent": [],
               "variantSentCount": 0,
               "variantReadCount": 0,
               "headers": []
           }
       }
   }

Properties
----------

Same as :ref:`rest_api/emails:Get Email`.

.. vale off

Create Email
************

.. vale on

.. code-block:: php

   <?php

   $data = array(
       'name'       => 'Email created via API',
       'subject'    => 'Hello World!',
       'emailType'  => 'list',
       'customHtml' => '<h1>Hello from API!</h1>',
       'lists'      => array(1, 2),
   );

   $email = $emailApi->create($data);

Create a new Email.

.. vale off

HTTP request
============

.. vale on

``POST /emails/new``

POST parameters
---------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``name``
     - string
     - Email name is the only required field
   * - ``subject``
     - string
     - Email subject
   * - ``fromAddress``
     - string
     - From email address
   * - ``fromName``
     - string
     - From name
   * - ``replyToAddress``
     - string
     - Reply-to email address
   * - ``bccAddress``
     - string
     - BCC email address
   * - ``useOwnerAsMailer``
     - boolean
     - Whether to use the Contact owner as the mailer
   * - ``template``
     - string
     - Template to use for the Email
   * - ``content``
     - array
     - Array of content for the template
   * - ``utmTags``
     - array
     - Array of UTM tags for tracking
   * - ``plainText``
     - string
     - Plain text version of the Email
   * - ``customHtml``
     - string
     - Custom HTML content of the Email
   * - ``emailType``
     - string
     - Type of the Email - ``list`` or ``template``
   * - ``publishUp``
     - datetime
     - Date/time when the Email should be published
   * - ``publishDown``
     - datetime
     - Date/time when the Email should be unpublished
   * - ``category``
     - int
     - ID of the category to assign the Email to
   * - ``lists``
     - array
     - Array of Segment/List IDs to assign the Email to
   * - ``language``
     - string
     - Language of the Email
   * - ``publicPreview``
     - boolean
     - Whether to enable public preview for the Email
   * - ``assetAttachments``
     - array
     - Array of asset IDs to attach to the Email
   * - ``unsubscribeForm``
     - int
     - ID of the unsubscribe form to use
   * - ``preferenceCenter``
     - int
     - ID of the preference center page to use
   * - ``dynamicContent``
     - array
     - Array of dynamic content variants
   * - ``headers``
     - array
     - Array of custom headers
   * - ``isPublished``
     - boolean
     - Published state

Response
========

``Expected Response Code: 201``

Properties
----------

Same as :ref:`rest_api/emails:Get Email`.

.. vale off

Edit Email
**********

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'name'    => 'New email name',
       'subject' => 'New subject line',
   );

   // Create new a Email of ID 1 isn't found?
   $createIfNotFound = true;

   $email = $emailApi->edit($id, $data, $createIfNotFound);

Edit an existing Email. Note that this supports PUT or PATCH depending on the desired behavior.

**PUT** creates an Email if the given ID doesn't exist and clears all the Email information, adds the information from the request.
**PATCH** fails if the Email with the given ID doesn't exist and updates the Email field values with the values from the request.

.. vale off

HTTP request
============

.. vale on

To edit an Email and return a 404 if the Email isn't found:

``PATCH /emails/ID/edit``

To edit an Email and create a new one if the Email isn't found:

``PUT /emails/ID/edit``

POST parameters
---------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``name``
     - string
     - Email name
   * - ``subject``
     - string
     - Email subject
   * - ``fromAddress``
     - string
     - From email address
   * - ``fromName``
     - string
     - From name
   * - ``replyToAddress``
     - string
     - Reply-to email address
   * - ``bccAddress``
     - string
     - BCC email address
   * - ``useOwnerAsMailer``
     - boolean
     - Whether to use the Contact owner as the mailer
   * - ``template``
     - string
     - Template to use for the Email
   * - ``content``
     - array
     - Array of content for the template
   * - ``utmTags``
     - array
     - Array of UTM tags for tracking
   * - ``plainText``
     - string
     - Plain text version of the Email
   * - ``customHtml``
     - string
     - Custom HTML content of the Email
   * - ``emailType``
     - string
     - Type of the Email - ``list`` or ``template``
   * - ``publishUp``
     - datetime
     - Date/time when the Email should be published
   * - ``publishDown``
     - datetime
     - Date/time when the Email should be unpublished
   * - ``category``
     - int
     - ID of the category to assign the Email to
   * - ``lists``
     - array
     - Array of Segment/List IDs to assign the Email to
   * - ``language``
     - string
     - Language of the Email
   * - ``publicPreview``
     - boolean
     - Whether to enable public preview for the Email
   * - ``assetAttachments``
     - array
     - Array of asset IDs to attach to the Email
   * - ``unsubscribeForm``
     - int
     - ID of the unsubscribe form to use
   * - ``preferenceCenter``
     - int
     - ID of the preference center page to use
   * - ``dynamicContent``
     - array
     - Array of dynamic content variants
   * - ``headers``
     - array
     - Array of custom headers
   * - ``isPublished``
     - boolean
     - Published state

Response
========

If ``PUT``, the expected response code is ``200`` if the Email was edited or ``201`` if created.
If ``PATCH``, the expected response code is ``200``.

Properties
----------

Same as :ref:`rest_api/emails:Get Email`.

.. vale off

Delete Email
************

.. vale on

.. code-block:: php

   <?php

   $email = $emailApi->delete($id);

Delete an Email.

.. vale off

HTTP request
============

.. vale on

``DELETE /emails/ID/delete``

Response
========

``Expected Response Code: 200``

Properties
----------

Same as :ref:`rest_api/emails:Get Email`.

.. vale off

Send Email to Segment
*********************

.. vale on

.. code-block:: php

   <?php

   // Send to all Contacts in the Email's assigned lists
   $response = $emailApi->send($id);

   // Send to specific list(s)
   $response = $emailApi->sendToLists($id, $listIds);

Send an Email to the Contacts in the Email's assigned lists or to provided list IDs.

.. vale off

HTTP request
============

.. vale on

``POST /emails/ID/send``

POST parameters
---------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Name
     - Description
   * - ``lists``
     - Array of list IDs to send to. If not provided, will use the Email's assigned lists.
   * - ``limit``
     - Maximum number of Contacts to send to. If not provided, will send to all Contacts.
   * - ``batch``
     - Batch size for sending. If not provided, will send all at once.

Response
========

``Expected Response Code: 200``

.. code-block:: json

   {
       "success": 1,
       "sentCount": 1,
       "failedRecipients": 0
   }

.. vale off

Send Email to Contact
*********************

.. vale on

.. code-block:: php

   <?php

   $response = $emailApi->sendToContact($emailId, $contactId, $options);

Send an Email to a specific Contact.

.. vale off

HTTP request
============

.. vale on

``POST /emails/ID/contact/CONTACT_ID/send``

POST parameters
---------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Name
     - Description
   * - ``tokens``
     - Array of tokens to replace in the Email content
   * - ``assetAttachments``
     - Array of asset IDs to attach to the Email

Response
========

``Expected Response Code: 200``

.. code-block:: json

   {
       "success": true
   }

Tokens
------

You can send custom tokens to the Email via the ``tokens`` parameter. Tokens should be in the format ``{token_name}`` and can be used in the Email content.

.. code-block:: php

   <?php

   $tokens = array(
       '{first_name}' => 'John',
       '{last_name}'  => 'Doe',
       '{custom_token}' => 'Custom Value'
   );

   $response = $emailApi->sendToContact($emailId, $contactId, array('tokens' => $tokens));

.. vale off

Create Email reply
******************

.. vale on

.. code-block:: php

   <?php

   $response = $emailApi->reply($trackingHash);

Create a reply to an Email using the tracking hash from the Email statistics.

.. vale off

HTTP request
============

.. vale on

``POST /emails/reply/TRACKING_HASH``

Response
========

``Expected Response Code: 201``

.. code-block:: json

   {
       "success": true
   }
