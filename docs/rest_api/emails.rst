Emails
######

Use this endpoint to obtain details, create, update, or delete Mautic's Emails.

.. code-block:: php

   <?php
   use Mautic\MauticApi;
   use Mautic\Auth\ApiAuth;

   // ...
   $initAuth = new ApiAuth();
   $auth     = $initAuth->newAuth($settings);
   $apiUrl   = "https://your-mautic.com";
   $api      = new MauticApi();
   $emailApi = $api->newApi("emails", $auth, $apiUrl);

.. vale off

.. _get_email_section:

Get Email
*********

.. vale on

Get an individual Email.

.. code-block:: php

   <?php

   //...
   $email = $emailApi->get($id);

.. vale off

HTTP request
============

.. vale on

``GET /emails/ID``

Response
========

* Returns ``200`` when the request successfully retrieves an Email.

.. code-block:: json

   {
     "email":{
       "isPublished":true,
       "dateAdded":"2016-10-25T18:51:17+00:00",
       "createdBy":1,
       "createdByUser":"John Doe",
       "dateModified":null,
       "modifiedBy":null,
       "modifiedByUser":null,
       "id":560,
       "name":"test",
       "subject":"API test email",
       "language":"en",
       "category":null,
       "fromAddress":null,
       "fromName":null,
       "replyToAddress":null,
       "bccAddress":null,
       "customHtml":"<h1>Hi there!<\/h1>",
       "plainText":null,
       "template":null,
       "emailType":"list",
       "publishUp":null,
       "publishDown":null,
       "readCount":0,
       "sentCount":0,
       "revision":1,
       "assetAttachments":[],
       "variantStartDate":null,
       "variantSentCount":0,
       "variantReadCount":0,
       "variantParent":null,
       "variantChildren":[],
       "translationParent":null,
       "translationChildren":[],
       "unsubscribeForm":null,
       "dynamicContent":[
         {
           "tokenName":null,
           "content":null,
           "filters":[
             {
               "content":null,
               "filters":[
                 {
                   "glue":null,
                   "field":null,
                   "object":null,
                   "type":null,
                   "operator":null,
                   "display":null,
                   "filter":null
                 }
               ]
             }
           ]
         }
       ],
       "lists":[
         {
           "createdByUser":"John Doe",
           "modifiedByUser":null,
           "id":256,
           "name":"test",
           "alias":"test29",
           "description":null
         }
       ]
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
     - Email ID
   * - ``name``
     - string
     - Internal name of the Email
   * - ``subject``
     - string
     - Subject of the Email
   * - ``fromAddress``
     - string
     - The from Email address if it differs from the Mautic configuration
   * - ``fromName``
     - string
     - The from name if it differs from the Mautic configuration
   * - ``replyToAddress``
     - string
     - The reply to Email address if it differs from the Mautic configuration
   * - ``bccAddress``
     - string
     - The bcc Email address if it differs from the Mautic configuration
   * - ``isPublished``
     - boolean
     - Email publication status
   * - ``publishUp``
     - datetime/null
     - Date and time when the Email becomes available
   * - ``publishDown``
     - datetime/null
     - Date and time when the Email becomes unavailable
   * - ``dateAdded``
     - datetime
     - Date and time of Email creation
   * - ``createdBy``
     - int
     - Email creator User ID
   * - ``createdByUser``
     - string
     - Email creator User name
   * - ``dateModified``
     - datetime/null
     - Date and time of the last Email modification
   * - ``modifiedBy``
     - int
     - Email last modifier User ID
   * - ``modifiedByUser``
     - string
     - Email last modifier User name
   * - ``language``
     - string
     - Language locale of the Email
   * - ``readCount``
     - int
     - Total Email read count
   * - ``sentCount``
     - int
     - Total Email sent count
   * - ``revision``
     - int
     - Email revision
   * - ``customHtml``
     - string
     - The HTML content of the Email
   * - ``plainText``
     - string
     - The plain text content of the Email
   * - ``template``
     - string
     - The name of the template used as the base for the Email
   * - ``emailType``
     - string
     - Identifies if this is a Segment Email or template Email. Possible values include ``list`` and ``template``
   * - ``translationChildren``
     - array
     - Array of page entities for translations of this Landing Page
   * - ``translationParent``
     - object
     - The parent/main page if this is a translation
   * - ``variantSentCount``
     - int
     - Sent count since the ``variantStartDate``
   * - ``variantReadCount``
     - int
     - Read count since the ``variantStartDate``
   * - ``variantChildren``
     - array
     - Array of Email entities for variants of this landing Email
   * - ``variantParent``
     - object
     - The parent/main Email if this is a variant or A/B test
   * - ``variantSettings``
     - array
     - The properties of the A/B test
   * - ``variantStartDate``
     - datetime/null
     - The date and time the A/B test began
   * - ``category``
     - object/null
     - Category information
   * - ``unsubscribeForm``
     - int
     - ID of the Form displayed in the unsubscribe page
   * - ``dynamicContent``
     - object
     - Dynamic Content configuration
   * - ``lists``
     - array
     - Contains an array of Segment IDs to add to the Segment Email
   * - ``assetAttachments``
     - array
     - Asset IDs array for Email attachment
   * - ``grapesjsbuilder``
     - array
     - ``customMjml`` key along with MJML content for Email based on MJML

.. vale off

List Emails
***********

Get a list of Emails.

.. vale on

.. code-block:: php

   <?php
   // ...

   $emails = $emailApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

HTTP request
============

.. vale on

``GET /emails``

Query parameters
----------------

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Name
     - Description
   * - ``search``
     - String or search command to filter entities
   * - ``start``
     - Sets the starting row for the entities returned. Defaults to 0
   * - ``limit``
     - Sets the number of entities to return. Defaults to the system configuration for pagination, which is 30
   * - ``orderBy``
     - Sorts the results by a specific column. Any column listed in the response is valid
   * - ``orderByDir``
     - Defines the sort direction: ascending or descending
   * - ``publishedOnly``
     - Filters the results to include only currently available entities
   * - ``minimal``
     - Returns only an array of entities without additional lists

Response
========

* Returns ``200`` when the request successfully retrieves the list of Emails.

.. code-block:: json

   {
     "total": 1,
     "emails": [
       {
         "isPublished":true,
         "dateAdded":"2016-10-25T18:51:17+00:00",
         "createdBy":1,
         "createdByUser":"John Doe",
         "dateModified":null,
         "modifiedBy":null,
         "modifiedByUser":null,
         "id":560,
         "name":"test",
         "subject":"API test email",
         "language":"en",
         "category":null,
         "fromAddress":null,
         "fromName":null,
         "replyToAddress":null,
         "bccAddress":null,
         "customHtml":"<h1>Hi there!<\/h1>",
         "plainText":null,
         "template":null,
         "emailType":"list",
         "publishUp":null,
         "publishDown":null,
         "readCount":0,
         "sentCount":0,
         "revision":1,
         "assetAttachments":[],
         "variantStartDate":null,
         "variantSentCount":0,
         "variantReadCount":0,
         "variantParent":null,
         "variantChildren":[],
         "translationParent":null,
         "translationChildren":[],
         "unsubscribeForm":null,
         "dynamicContent":[
           {
             "tokenName":null,
             "content":null,
             "filters":[
               {
                 "content":null,
                 "filters":[
                   {
                     "glue":null,
                     "field":null,
                     "object":null,
                     "type":null,
                     "operator":null,
                     "display":null,
                     "filter":null
                   }
                 ]
               }
             ]
           }
         ],
         "lists":[
           {
             "createdByUser":"John Doe",
             "modifiedByUser":null,
             "id":256,
             "name":"test",
             "alias":"test29",
             "description":null
           }
         ]
       }
     ]
   }

Properties
----------

Same as :ref:`get_email_section`.

.. vale off

Create Email
************

Create a new Email.

.. vale on

.. code-block:: php

   <?php

   $data = array(
     'name'        => 'Email A',
     'subject'     => 'This is my first email created via API.',
     'isPublished' => 1
   );

   $email = $emailApi->create($data);

.. vale off

HTTP request
============

.. vale on

``POST /emails/new``

POST parameters
---------------

.. list-table::
   :widths: 30 20 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - Email ID
   * - ``name``
     - string
     - Internal name of the Email
   * - ``subject``
     - string
     - Subject of the Email
   * - ``fromAddress``
     - string
     - The from Email address if it differs from the Mautic configuration
   * - ``fromName``
     - string
     - The from name if it differs from the Mautic configuration
   * - ``replyToAddress``
     - string
     - The reply to Email address if it differs from the Mautic configuration
   * - ``bccAddress``
     - string
     - The bcc Email address if it differs from the Mautic configuration
   * - ``isPublished``
     - boolean
     - Email publication status
   * - ``publishUp``
     - datetime/null
     - Date and time when the Email becomes available
   * - ``publishDown``
     - datetime/null
     - Date and time when the Email becomes unavailable
   * - ``language``
     - string
     - Language locale of the Email
   * - ``readCount``
     - int
     - Total Email read count
   * - ``sentCount``
     - int
     - Total Email sent count
   * - ``revision``
     - int
     - Email revision
   * - ``customHtml``
     - string
     - The HTML content of the Email
   * - ``plainText``
     - string
     - The plain text content of the Email
   * - ``template``
     - string
     - The name of the template used as the base for the Email
   * - ``emailType``
     - string
     - Identifies if this is a Segment Email or template Email. Possible values include ``list`` and ``template``
   * - ``translationChildren``
     - array
     - Array of Page entities for translations of this Landing Page
   * - ``translationParent``
     - object
     - The parent/main page if this is a translation
   * - ``variantSentCount``
     - int
     - Sent count since the ``variantStartDate``
   * - ``variantReadCount``
     - int
     - Read count since the ``variantStartDate``
   * - ``variantChildren``
     - array
     - Array of Email entities for variants of this landing Email
   * - ``variantParent``
     - object
     - The parent/main Email if this is a variant or A/B test
   * - ``variantSettings``
     - array
     - The properties of the A/B test
   * - ``variantStartDate``
     - datetime/null
     - The date and time the A/B test began
   * - ``category``
     - object/null
     - Category information
   * - ``unsubscribeForm``
     - int
     - ID of the Form displayed in the unsubscribe page
   * - ``dynamicContent``
     - object
     - Dynamic Content configuration
   * - ``lists``
     - array
     - Contains an array of Segment IDs to add to the Segment Email
   * - ``assetAttachments``
     - array
     - Asset IDs array for Email attachment
   * - ``grapesjsbuilder``
     - array
     - ``customMjml`` key along with MJML content for Email based on MJML

Response
========

* Returns ``201`` when the request successfully creates an Email.

Properties
----------

Same as :ref:`get_email_section`.

.. vale off

Edit Email
**********

Edit an Email. This operation supports ``PUT`` or ``PATCH`` depending on the desired behavior:

* ``PUT``: creates an Email when the ID doesn't exist. If the ID exists, the request clears the Email data and adds the request values.
* ``PATCH``: updates field values for an existing Email using the request data. The request fails when the ID doesn't exist.

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
     'name'        => 'New email name',
     'isPublished' => 0
   );

   // Create a new email if ID 1 is not found?
   $createIfNotFound = true;

   $email = $emailApi->edit($id, $data, $createIfNotFound);

.. vale off

HTTP request
============

.. vale on

* ``PATCH /emails/ID/edit``: edits an existing Email. The request fails with a 404 error when the ID doesn't exist.
* ``PUT /emails/ID/edit``: edits an existing Email or creates a new one when the ID doesn't exist.

POST parameters
---------------

.. list-table::
   :widths: 30 20 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - Email ID
   * - ``name``
     - string
     - Internal name of the Email
   * - ``subject``
     - string
     - Subject of the Email
   * - ``fromAddress``
     - string
     - The from Email address if it differs from the Mautic configuration
   * - ``fromName``
     - string
     - The from name if it differs from the Mautic configuration
   * - ``replyToAddress``
     - string
     - The reply to Email address if it differs from the Mautic configuration
   * - ``bccAddress``
     - string
     - The bcc Email address if it differs from the Mautic configuration
   * - ``isPublished``
     - boolean
     - Email publication status
   * - ``publishUp``
     - datetime/null
     - Date and time when the Email becomes available
   * - ``publishDown``
     - datetime/null
     - Date and time when the Email becomes unavailable
   * - ``language``
     - string
     - Language locale of the Email
   * - ``readCount``
     - int
     - Total Email read count
   * - ``sentCount``
     - int
     - Total Email sent count
   * - ``revision``
     - int
     - Email revision
   * - ``customHtml``
     - string
     - The HTML content of the Email
   * - ``plainText``
     - string
     - The plain text content of the Email
   * - ``template``
     - string
     - The name of the template used as the base for the Email
   * - ``emailType``
     - string
     - Identifies if this is a Segment Email or template Email. Possible values include ``list`` and ``template``
   * - ``lists``
     - array
     - Contains an array of Segment IDs to add to the Segment Email

Response
========

* ``PUT``: returns ``200`` when the request successfully edits an Email or ``201`` when the request creates an Email.
* ``PATCH``: returns ``200`` when the request successfully edits an Email.

Properties
----------

Same as :ref:`get_email_section`.

.. vale off

Delete Email
************

.. vale on

Delete an Email.

.. code-block:: php

   <?php

   $email = $emailApi->delete($id);

.. vale off

HTTP request
============

.. vale on

``DELETE /emails/ID/delete``

Response
========

* Returns ``200`` when the request successfully deletes an Email.

Properties
----------

Same as :ref:`get_email_section`.

.. vale off

Send Email to Contact
*********************

Send a predefined Email to an existing Contact.

.. vale on

.. code-block:: php

   <?php
   
   //...
   $email = $emailApi->sendToContact($emailId, $contactId);

You can reference Asset IDs for attaching documents. Use existing IDs or IDs returned by the :ref:`Create Asset <rest_api/assets:Create Asset>` endpoint.

.. vale off

HTTP request
============

.. vale on

``POST /emails/ID/contact/CONTACT_ID/send``

POST parameters
---------------

.. list-table::
   :widths: 30 20 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``tokens``
     - array
     - Array of tokens in the Email
   * - ``assetAttachments``
     - array
     - Array of Asset IDs

Response
========

* Returns ``200`` when the request successfully sends the Email to the Contact.

Properties
----------

.. code-block:: json

   {
     "success": 1
   }

.. vale off

Send Email to Segment
*********************

.. vale on

Send a Segment Email to linked Segments.

.. code-block:: php

   <?php
   
   //...
   $email = $emailApi->send($id);

.. vale off

HTTP request
============

.. vale on

``POST /emails/ID/send``

Response
========

* Returns ``200`` when the request successfully sends the Email to the Segments.

Properties
----------

.. code-block:: json

   {
     "success": 1,
     "sentCount": 1,
     "failedCount": 0
   }

.. vale off

Create a reply to a send Email send row
***************************************

.. vale on

This endpoint creates a record that a specific Email stat row received a reply. It marks an Email send stat as read.

.. vale off

HTTP request
============

.. vale on

``POST /emails/reply/TRACKING_HASH``

The tracking hash provides a unique reference for each Email send stat record.

Response
========

* Returns ``200`` when the tracking successfully records the reply.

Properties
----------

.. code-block:: json

   {
     "success": 1
   }