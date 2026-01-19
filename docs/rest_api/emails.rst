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

.. code-block:: php

   <?php

   //...
   $email = $emailApi->get($id);

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

Get an individual Email by ID.

.. vale off

HTTP request
============

.. vale on

``GET /emails/ID``

Response
========

``Expected Response Code: 200``

See JSON code example.

**Email Properties**

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
     - Internal name of the Email
   * - ``subject``
     - string
     - Subject of the Email
   * - ``fromAddress``
     - string
     - The from Email address if it's different than the one in the Mautic configuration
   * - ``fromName``
     - string
     - The from name if it's different than the one in the Mautic configuration
   * - ``replyToAddress``
     - string
     - The reply to Email address if it's different than the one in the Mautic configuration
   * - ``bccAddress``
     - string
     - The bcc Email address if it's different than the one in the Mautic configuration
   * - ``isPublished``
     - boolean
     - Available for use state
   * - ``publishUp``
     - datetime/null
     - Date/time when the Email should be available
   * - ``publishDown``
     - datetime/null
     - Date/time the Email should be unavailable
   * - ``dateAdded``
     - datetime
     - Date/time of Email creation
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
   * - ``EmailType``
     - string
     - If it's a Segment - former list - Email or template Email. Possible values are ``list`` and ``template``
   * - ``translationChildren``
     - array
     - Array of page entities for translations of this Landing Page
   * - ``translationParent``
     - object
     - The parent/main page if this is a translation
   * - ``variantSentCount``
     - int
     - Sent count since ``variantStartDate``
   * - ``variantReadCount``
     - int
     - Read count since ``variantStartDate``
   * - ``variantChildren``
     - array
     - Array of Email entities for variants of this landing Email
   * - ``variantParent``
     - object
     - The parent/main Email if this is a variant - A/B test
   * - ``variantSettings``
     - array
     - The properties of the A/B test
   * - ``variantStartDate``
     - datetime/null
     - The date/time the A/B test began
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
     - ``customMjml`` key along with MJML content for Email based on MJML.

.. vale off

List Emails
***********

.. vale on

.. code-block:: php

   <?php
   // ...

   $emails = $emailApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

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

.. _http-request-1:

.. vale off

HTTP request
============

.. vale on

``GET /emails``

**Query Parameters**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Name
     - Description
   * - ``search``
     - String or search command to filter entities by.
   * - ``start``
     - Starting row for the entities returned. Defaults to 0.
   * - ``limit``
     - Limit number of entities to return. Defaults to the system configuration for pagination, which is 30.
   * - ``orderBy``
     - Column to sort by. Can use any column listed in the response.
   * - ``orderByDir``
     - Sort direction: ascending or descending.
   * - ``publishedOnly``
     - Only return currently available entities.
   * - ``minimal``
     - Return only array of entities without additional lists in it.

.. _response-1:

Response
========

``Expected Response Code: 200``

See JSON code example.

**Properties**

Same as :ref:`get_email_section`.

.. vale off

Create Email
************

.. vale on

.. code-block:: php

   <?php

   $data = array(
       'title'        => 'Email A',
       'description' => 'This is my first email created via API.',
       'isPublished' => 1
   );

   $email = $emailApi->create($data);

Create a new Email.

.. _http-request-2:

.. vale off

HTTP request
============

.. vale on

``POST /emails/new``

**POST Parameters**

.. list-table::
   :widths: 30 20 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Email
   * - ``name``
     - string
     - Internal name of the Email
   * - ``subject``
     - string
     - Subject of the Email
   * - ``fromAddress``
     - string
     - The from Email address if it's different than the one in the Mautic configuration
   * - ``fromName``
     - string
     - The from name if it's different than the one in the Mautic configuration
   * - ``replyToAddress``
     - string
     - The reply to Email address if it's different than the one in the Mautic configuration
   * - ``bccAddress``
     - string
     - The bcc Email address if it's different than the one in the Mautic configuration
   * - ``isPublished``
     - boolean
     - Available state
   * - ``publishUp``
     - datetime/null
     - Date/time when the Email should be available
   * - ``publishDown``
     - datetime/null
     - Date/time the Email should be unavailable
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
     - If it's a Segment - former list - Email or template Email. Possible values are ``list`` and ``template``
   * - ``translationChildren``
     - array
     - Array of Page entities for translations of this Landing Page
   * - ``translationParent``
     - object
     - The parent/main page if this is a translation
   * - ``variantSentCount``
     - int
     - Sent count since ``variantStartDate``
   * - ``variantReadCount``
     - int
     - Read count since ``variantStartDate``
   * - ``variantChildren``
     - array
     - Array of Email entities for variants of this landing Email
   * - ``variantParent``
     - object
     - The parent/main Email if this is a variant - A/B test
   * - ``variantSettings``
     - array
     - The properties of the A/B test
   * - ``variantStartDate``
     - datetime/null
     - The date/time the A/B test began
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
     - ``customMjml`` key along with MJML content for Email based on MJML.

.. _response-2:

Response
========

``Expected Response Code: 201``

**Properties**

Same as :ref:`get_email_section`.

.. vale off

Edit Email
**********

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'title'        => 'New email title',
       'isPublished' => 0
   );

   // Create new a email of ID 1 is not found?
   $createIfNotFound = true;

   $email = $emailApi->edit($id, $data, $createIfNotFound);

Edit a new Email. Note that this supports ``PUT`` or ``PATCH`` depending on the desired behavior.

* ``PUT``: creates an Email if the given ID doesn't exist and clears all the Email information, adds the information from the request.

* ``PATCH``: fails if the Email with the given ID doesn't exist and updates the Email field values with the values from the request.

.. _http-request-3:

.. vale off

HTTP request
============

.. vale on

To edit an Email and return a 404 if the Email isn't found:

``PATCH /emails/ID/edit``

To edit an Email and create a new one if the Email isn't found:

``PUT /emails/ID/edit``

**POST Parameters**

.. list-table::
   :widths: 30 20 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Email
   * - ``name``
     - string
     - Internal name of the Email
   * - ``subject``
     - string
     - Subject of the Email
   * - ``fromAddress``
     - string
     - The from Email address if it's different than the one in the Mautic configuration
   * - ``fromName``
     - string
     - The from name if it's different than the one in the Mautic configuration
   * - ``replyToAddress``
     - string
     - The reply to Email address if it's different than the one in the Mautic configuration
   * - ``bccAddress``
     - string
     - The bcc Email address if it's different than the one in the Mautic configuration
   * - ``isPublished``
     - boolean
     - Available state
   * - ``publishUp``
     - datetime/null
     - Date/time when the Email should be available
   * - ``publishDown``
     - datetime/null
     - Date/time the Email should be unavailable
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
     - If it's a Segment - former list - Email or template Email. Possible values are ``list`` and ``template``
   * - ``translationChildren``
     - array
     - Array of page entities for translations of this Landing Page
   * - ``translationParent``
     - object
     - The parent/main page if this is a translation
   * - ``variantSentCount``
     - int
     - Sent count since ``variantStartDate``
   * - ``variantReadCount``
     - int
     - Read count since ``variantStartDate``
   * - ``variantChildren``
     - array
     - Array of Email entities for variants of this landing Email
   * - ``variantParent``
     - object
     - The parent/main Email if this is a variant - A/B test
   * - ``variantSettings``
     - array
     - The properties of the A/B test
   * - ``variantStartDate``
     - datetime/null
     - The date/time the A/B test began
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

.. _response-3:

Response
========

* ``PUT``: returns code ``200`` for an edited Email or ``201`` for a created Email.

* ``PATCH``: the expected response code is ``200``.

**Properties**

Same as :ref:`get_email_section`.

.. vale off

Delete Email
************

.. vale on

.. code-block:: php

   <?php

   $email = $emailApi->delete($id);

Delete an Email.

.. _http-request-4:

.. vale off

HTTP request
============

.. vale on

``DELETE /emails/ID/delete``

.. _response-4:

Response
========

``Expected Response Code: 200``

**Properties**

Same as :ref:`get_email_section`.

.. vale off

Send Email to Contact
*********************

.. vale on

.. code-block:: php

   <?php

   $email = $emailApi->sendToContact($emailId, $contactId);

Send a predefined Email to existing Contact.

Reference Assets using IDs returned by the :ref:`Create Asset <rest_api/assets:Create Asset>` endpoint.

.. _http-request-5:

.. vale off

HTTP request
============

.. vale on

``POST /emails/ID/contact/CONTACT_ID/send``

**POST Parameters**

.. list-table::
   :widths: 30 20 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``tokens``
     - array
     - Array of tokens in Email
   * - ``assetAttachments``
     - array
     - Array of Asset IDs

.. _response-5:

Response
========

``Expected Response Code: 200``

**Properties**

.. code-block:: json

   {
       "success": 1
   }

.. vale off

Send Email to Segment
*********************

.. vale on

.. code-block:: php

   <?php

   $email = $emailApi->send($id);

Send a Segment Email to linked Segments.

.. _http-request-6:

.. vale off

HTTP request
============

.. vale on

``POST /emails/ID/send``

.. _response-6:

.. vale off

Response
========

.. vale on

``Expected Response Code: 200``

**Properties**

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

This endpoint can create a record that a specific Email stat row received a reply. It marks an Email send stat as read.

.. _http-request-7:

.. vale off

HTTP request
============

.. vale on

``POST /emails/reply/TRACKING_HASH``

The tracking hash provides a unique reference for each Email send stat record.

.. _response-7:

Response
========

``Expected Response Code: 200``

**Properties**

.. code-block:: json

   {
       "success": 1,
   }