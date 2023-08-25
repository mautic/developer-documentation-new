Emails
######

Use this endpoint to obtain details, create, update, or delete Mautic's Emails.

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

**HTTP Request**

.. vale on

``GET /emails/ID``

**Response**

``Expected Response Code: 200``

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
       "subject":"API test Email",
       "language":"en",
       "category":null,
       "fromAddress":null,
       "fromName":null,
       "replyToAddress":null,
       "bccAddress":null,
       "utmTags": {
         "utmSource": "myUTMsource",
         "utmMedium": "email",
         "utmCampaign": "myUTMcampaign",
         "utmContent": null
       },
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

**Email Properties**

.. list-table::
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
     - The ``BCC`` Email address if it's different than the one in the Mautic configuration
   * - ``utmTags``
     - array
     - Array of UTM params, all of which are of type string. Options are: utmSource, utmMedium, utmCampaign, utmContent
   * - ``isPublished``
     - boolean
     - Published state
   * - ``publishUp``
     - datetime/null
     - Email publish date/time
   * - ``publishDown``
     - datetime/null
     - Email unpublish date/time
   * - ``dateAdded``
     - ``datetime``
     - Email creation date/time
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
   * - ``emailType``
     - string
     - Whether this is a Segment Email - formerly known as List Email - or a template Email. Possible values are 'list' and 'template'
   * - ``translationChildren``
     - array
     - Array of Landing Page entities for translations of this Landing Page
   * - ``translationParent``
     - object
     - The parent/main Landing Page if this is a translation
   * - ``variantSentCount``
     - int
     - Sent count since variantStartDate
   * - ``variantReadCount``
     - int
     - Read count since variantStartDate
   * - ``variantChildren``
     - array
     - Array of Email entities for variants of this landing Email
   * - ``variantParent``
     - object
     - The parent/main Email if this is a variant, also known as A/B test
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
     - ID of the Form displayed in the ``unsubscribe page``
   * - ``dynamicContent``
     - object
     - Dynamic Content configuration
   * - ``lists``
     - array
     - Array of Segment IDs linked to the Segment Email
   * - ``assetAttachments``
     - array
     - Array of Asset IDs to use as Email attachments

.. vale off

List Emails
***********

.. vale on

.. code-block:: php

   <?php
   // ...

   $emails = $emailApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

**HTTP Request**

.. vale on

``GET /emails``

**Query Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - ``search``
     - String or search command to filter entities by.
   * - ``start``
     - Starting row for the entities returned. Defaults to 0.
   * - ``limit``
     - Limit number of entities to return. Defaults to the system configuration for pagination - defaults to 30.
   * - ``orderBy``
     - Column to sort by. Can use any column listed in the response.
   * - ``orderByDir``
     - Sort direction: ``asc`` or ``desc``.
   * - ``publishedOnly``
     - Only return currently published entities.
   * - ``minimal``
     - Return only array of entities without additional lists in it.


**Response**

``Expected Response Code: 200``

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
               "subject":"API test Email",
               "language":"en",
               "category":null,
               "fromAddress":null,
               "fromName":null,
               "replyToAddress":null,
               "bccAddress":null,
               "utmTags": {
                 "utmSource": "myUTMsource",
                 "utmMedium": "email",
                 "utmCampaign": "myUTMcampaign",
                 "utmContent": null
               },
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

**Properties**

Same as `Get Email <#get-email>`_.

.. vale off

Create Email
************

.. vale on

.. code-block:: php

   <?php 

   $data = array(
       'title'        => 'Email A',
       'description' => 'This is my first Email created via API.',
       'isPublished' => 1
   );

   $email = $emailApi->create($data);

Create a new Email.

.. vale off

**HTTP Request**

.. vale on

``POST /emails/new``

**POST Parameters**

.. list-table::
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
     - The ``BCC`` Email address if it's different than the one in the Mautic configuration
   * - ``useOwnerAsMailer``
     - boolean
     - Whether or not contact owner should be used as mailer. Defaults to TRUE
   * - ``utmTags``
     - array
     - Array of UTM params, all of which are of type string. Options are: utmSource, utmMedium, utmCampaign, utmContent
   * - ``isPublished``
     - boolean
     - Published state
   * - ``publishUp``
     - datetime/null
     - Email publish date/time
   * - ``publishDown``
     - datetime/null
     - Email unpublish date/time
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
     - Whether this is a Segment Email - formerly known as List Email - or a template Email. Possible values are 'list' and 'template'
   * - ``translationChildren``
     - array
     - Array of Landing Page entities for translations of this Landing Page
   * - ``translationParent``
     - object
     - The parent/main Landing Page if this is a translation
   * - ``variantSentCount``
     - int
     - Sent count since variantStartDate
   * - ``variantReadCount``
     - int
     - Read count since variantStartDate
   * - ``variantChildren``
     - array
     - Array of Email entities for variants of this landing Email
   * - ``variantParent``
     - object
     - The parent/main Email if this is a variant, also known as A/B test
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
     - ID of the Form displayed in the ``unsubscribe page``
   * - ``dynamicContent``
     - object
     - Dynamic Content configuration
   * - ``lists``
     - array
     - Array of Segment IDs linked to the Segment Email

**Response**

``Expected Response Code: 201``

**Properties**

Same as `Get Email <#get-email>`_.

.. vale off

Edit Email
**********

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'title'        => 'New Email title',
       'isPublished' => 0
   );

   // Create new a Email of ID 1 isn't found?
   $createIfNotFound = true;

   $email = $emailApi->edit($id, $data, $createIfNotFound);

Edit a new Email. Note that this supports PUT or PATCH depending on the desired behavior.

**PUT** creates a Email if the given ID doesn't exist and clears all the Email information, adds the information from the request.
**PATCH** fails if the Email with the given ID doesn't exist and updates the Email field values with the values Form the request.

.. vale off

**HTTP Request**

.. vale on

To edit a Email and return a 404 if the Email isn't found:

``PATCH /emails/ID/edit``

To edit a Email and create a new one if the Email isn't found:

``PUT /emails/ID/edit``

**POST Parameters**

.. list-table::
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
     - The ``BCC`` Email address if it's different than the one in the Mautic configuration
   * - ``useOwnerAsMailer``
     - boolean
     - Whether or not contact owner should be used as mailer
   * - ``utmTags``
     - array
     - Array of UTM params, all of which are of type string. Options are: utmSource, utmMedium, utmCampaign, utmContent
   * - ``isPublished``
     - boolean
     - Published state
   * - ``publishUp``
     - datetime/null
     - Email publish date/time
   * - ``publishDown``
     - datetime/null
     - Email unpublish date/time
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
     - Whether this is a Segment Email - formerly known as List Email - or a template Email. Possible values are 'list' and 'template'
   * - ``translationChildren``
     - array
     - Array of Landing Page entities for translations of this Landing Page
   * - ``translationParent``
     - object
     - The parent/main Landing Page if this is a translation
   * - ``variantSentCount``
     - int
     - Sent count since variantStartDate
   * - ``variantReadCount``
     - int
     - Read count since variantStartDate
   * - ``variantChildren``
     - array
     - Array of Email entities for variants of this landing Email
   * - ``variantParent``
     - object
     - The parent/main Email if this is a variant, also known as A/B test
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
     - Id of the Form displayed in the ``unsubscribe page``
   * - ``dynamicContent``
     - object
     - Dynamic Content configuration
   * - ``lists``
     - array
     - Array of Segment IDs linked to the Segment Email


**Response**

If ``PUT``, the expected response code is ``200`` if editing the Email or ``201`` if creating one.
If ``PATCH``, the expected response code is ``200``.

**Properties**

Same as `Get Email <#get-email>`_.

.. vale off

Delete Email
************

.. vale on

.. code-block:: php

   <?php

   $email = $emailApi->delete($id);

Delete an Email.

.. vale off

**HTTP Request**

.. vale on

``DELETE /emails/ID/delete``

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get Email <#get-email>`_.

.. vale off

Send Email to Contact
*********************

.. vale on

.. code-block:: php

   <?php

   $email = $emailApi->sendToContact($emailId, $contactId);

Send a predefined Email to existing Contact.

You can reference Assets for attaching documents. You can either provide IDs of existing Assets or IDs returned by the Create Asset endpoint.

.. vale off

**HTTP Request**

.. vale on

``POST /emails/ID/contact/CONTACT_ID/send``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``tokens``
     - array
     - Array of tokens in Email
   * - ``assetAttachments``
     - array
     - Array of Asset IDs to use as Email attachments


**Response**

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

.. vale off

**HTTP Request**

.. vale on

``POST /emails/ID/send``

**Response**

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

This endpoint can create a record that a specific Email stat row received a reply. It also marks an Email send stat as ``read``.

.. vale off

**HTTP Request**

.. vale on

``POST /emails/reply/TRACKING_HASH``

**Response**

``Expected Response Code: 200``

**Properties**

.. code-block:: json

   {
       "success": 1,
   }
