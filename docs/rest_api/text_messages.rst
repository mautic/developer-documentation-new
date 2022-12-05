Text messages
#############

Use this endpoint to obtain details on Mautic's Text Messages, or SMSs.

Text message properties
=======================

Use these properties when creating a Text Message in a ``POST`` request. These properties are also returned when listing or getting Text Messages.

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the SMS
   * - ``name``
     - string
     - Title of the SMS
   * - ``message``
     - string
     - Message of the SMS
   * - ``isPublished``
     - boolean
     - Published state
   * - ``publishUp``
     - datetime/null
     - Date/time when the SMS gets published
   * - ``publishDown``
     - datetime/null
     - Date/time the SMS gets unpublished
   * - ``dateAdded``
     - ``datetime``
     - Date/time SMS got created
   * - ``createdBy``
     - int
     - ID of the User that created the SMS
   * - ``createdByUser``
     - string
     - Name of the User that created the SMS
   * - ``dateModified``
     - datetime/null
     - Date/time SMS got last modified
   * - ``modifiedBy``
     - int
     - ID of the User that last modified the SMS
   * - ``modifiedByUser``
     - string
     - Name of the User that last modified the SMS
   * - ``language``
     - string
     - Language locale of the SMS
   * - ``sentCount``
     - int
     - How many times the SMS got sent

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
   $smsApi   = $api->newApi("smses", $auth, $apiUrl);

Get text message
================

.. code-block:: php

   <?php

   //...
   $sms = $smsApi->get($id);

Get an individual SMS by ID.

.. vale off

**HTTP Request**

.. vale on

``GET /smses/ID``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {  
       "sms":{  
           "isPublished":true,
           "dateAdded":"2016-09-14T12:14:45+00:00",
           "createdBy":1,
           "createdByUser":"Wu Popovski",
           "dateModified":null,
           "modifiedBy":null,
           "modifiedByUser":null,
           "id":1,
           "name":"Message A",
           "message":"Hello",
           "language":"en",
           "category":null,
           "publishUp":null,
           "publishDown":null,
           "sentCount":0
       }
   }

List text messages
==================

.. code-block:: php

   <?php
   // ...

   $smses = $smsApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

**HTTP Request**

.. vale on

``GET /smses``

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
     - Limit number of entities to return. Defaults to the system configuration for pagination, which defaults to 30.
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
       "total":1,
       "smses":[  
           {  
               "isPublished":true,
               "dateAdded":"2016-09-14T12:14:45+00:00",
               "createdBy":1,
               "createdByUser":"Kevin Bulgarelli",
               "dateModified":null,
               "modifiedBy":null,
               "modifiedByUser":null,
               "id":1,
               "name":"Message A",
               "message":"Hello",
               "language":"en",
               "category":null,
               "publishUp":null,
               "publishDown":null,
               "sentCount":0
           }
       ]
   }

**Properties**

See the "Text message properties" on top of this document.

Create text message
===================

.. code-block:: php

   <?php 

   $data = array(
       'name'        => 'Text message A',
       'message' => 'This is my first sms created via API.',
       'isPublished' => 1
   );

   $sms = $smsApi->create($data);

Create a new SMS.

.. vale off

**HTTP Request**

.. vale on

``POST /smses/new``

**POST Parameters**

See the "Text message properties" on top of this document.

**Response**

``Expected Response Code: 201``

**Properties**

See the "Text message properties" on top of this document.

Edit text message
=================

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'name'        => 'New sms name',
       'isPublished' => 0
   );

   // Create new a SMS of ID 1 is not found?
   $createIfNotFound = true;

   $sms = $smsApi->edit($id, $data, $createIfNotFound);

Edit a new SMS. Note that this supports PUT or PATCH depending on the desired behavior.

**PUT** creates an SMS if the given ID doesn't exist and clears all the SMS information, adds the information from the request.
**PATCH** fails if the SMS with the given ID doesn't exist and updates the SMS field values with the values from the request.

.. vale off

**HTTP Request**

.. vale on

To edit an SMS and return a 404 if the SMS isn't found:

``PATCH /smses/ID/edit``

To edit an SMS and create a new one if the SMS isn't found:

``PUT /smses/ID/edit``

**PUT/PATCH Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the SMS
   * - ``name``
     - string
     - Title of the SMS
   * - ``message``
     - string
     - Message of the SMS
   * - ``isPublished``
     - boolean
     - Published state
   * - ``publishUp``
     - datetime/null
     - Date/time when the SMS should gets published
   * - ``publishDown``
     - datetime/null
     - Date/time the SMS should gets unpublished
   * - ``language``
     - string
     - Language locale of the SMS


**Response**

If ``PUT``\ , the expected response code is ``200`` if the SMS got edited or ``201`` if created.

If ``PATCH``\ , the expected response code is ``200``.

**Properties**

See the "Text message properties" on top of this document.

Delete text message
===================

.. code-block:: php

   <?php

   $sms = $smsApi->delete($id);

Delete an SMS.

.. vale off

**HTTP Request**

.. vale on

``DELETE /smses/ID/delete``

**Response**

``Expected Response Code: 200``

**Properties**

See the "Text message properties" on top of this document.

.. vale off

Send SMS to contact
===================

.. vale on

.. code-block:: php

   <?php

   $sms = $smsApi->sendToContact($smsId, $contactId);

Send a predefined SMS to existing Contact.

.. vale off

**HTTP Request**

.. vale on

``GET /smses/ID/contact/CONTACT_ID/send``

**Response**

``Expected Response Code: 200``

**Properties**

.. code-block:: json

   {
       "success": 1,
       "status": "Delivered"
   }
