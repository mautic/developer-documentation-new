Marketing Messages
##################

Use this endpoint to obtain details, create, update, or delete Mautic's Marketing Messages.

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
   $messageApi = $api->newApi("messages", $auth, $apiUrl);

.. vale off

Get Marketing Message
*********************

.. vale on

.. code-block:: php

   <?php

   //...
   $message = $messageApi->get($id);

.. code-block:: json

   {
       "message": {
           "isPublished": true,
           "dateAdded": "2017-02-08T15:00:34+01:00",
           "dateModified": "2017-02-08T15:00:35+01:00",
           "createdBy": 1,
           "createdByUser": "John Doe",
           "modifiedBy": 1,
           "modifiedByUser": "John Doe",
           "id": 26,
           "name": "Thanks for the feedback!",
           "description": "",
           "publishUp": null,
           "publishDown": null,
           "channels": [
               {
                   "id": 55,
                   "channel": "email",
                   "channelId": 1197,
                   "channelName": "Email A",
                   "isEnabled": true
               },
               {
                   "id": 57,
                   "channel": "notification",
                   "channelId": null,
                   "channelName": null,
                   "isEnabled": false
               },
               {
                   "id": 56,
                   "channel": "sms",
                   "channelId": 103,
                   "channelName": "SMS A",
                   "isEnabled": false
               },
               {
                   "id": 91,
                   "channel": "tweet",
                   "channelId": null,
                   "channelName": null,
                   "isEnabled": false
               }
           ]
       }
   }

Get an individual Marketing Message by ID.

.. vale off

**HTTP Request**

.. vale on

``GET /messages/ID``

**Response**

``Expected Response Code: 200``

See JSON code example.

**Marketing Message Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the message
   * - name
     - string
     - Internal name of the message
   * - ``isPublished``
     - boolean
     - Published state
   * - ``publishUp``
     - datetime/null
     - Marketing Message publish date/time
   * - ``publishDown``
     - datetime/null
     - Marketing Message unpublish date/time
   * - ``dateAdded``
     - ``datetime``
     - Marketing Message creation date/time
   * - ``createdBy``
     - int
     - ID of the User that created the message
   * - ``createdByUser``
     - string
     - Name of the User that created the message
   * - ``dateModified``
     - datetime/null
     - Date/time message was last modified
   * - ``modifiedBy``
     - int
     - ID of the User that last modified the message
   * - ``modifiedByUser``
     - string
     - Name of the User that last modified the message
   * - ``channels``
     - array
     - Array of Channels configured for the Marketing Message

.. vale off

List Marketing Messages
***********************

.. vale on

.. code-block:: php

   <?php
   // ...

   $messages = $messageApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

**HTTP Request**

.. vale on

``GET /messages``

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
     - Limit number of entities to return. Defaults to the system configuration for pagination  - defaults to 30.
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
       "messages": {
           "1": {
               "isPublished": true,
               "dateAdded": "2017-02-03T16:51:58+00:00",
               "dateModified": "2017-02-03T19:11:41+00:00",
               "createdBy": 1,
               "createdByUser": "John Doe",
               "modifiedBy": 1,
               "modifiedByUser": "John Doe",
               "id": 1,
               "name": "Live long and prosper",
               "description": null,
               "publishUp": null,
               "publishDown": null,
               "channels": [
                   {
                       "id": 1,
                       "channel": "email",
                       "channelId": 44,
                       "channelName": "Email A",
                       "isEnabled": true
                   },
                   {
                       "id": 2,
                       "channel": "sms",
                       "channelId": 1,
                       "channelName": "SMS A",
                       "isEnabled": true
                   },
                   {
                       "id": 3,
                       "channel": "notification",
                       "channelId": 75,
                       "channelName": null,
                       "isEnabled": false
                   }
               ]
           }
       }
   }

**Properties**

Same as `Get Marketing Message <#get-message>`_.

.. vale off

Create Marketing Message
************************

.. vale on

.. code-block:: php

   <?php 

   $data = array(
       'name'        => 'Marketing Message A',
       'description' => 'This is my first message created via API.',
       'isPublished' => 1,
       'channels' => array(
           'email' => array(
               'channel' => 'email',
               'channelId' => 44,
               'isEnabled' => true,
           ),
           'sms' => array(
               'channel' => 'sms',
               'channelId' => 1,
               'isEnabled' => true,
           ),
           'notification' => array(
               'channel' => 'notification',
               'channelId' => 75,
               'isEnabled' => false,
           )
       )
   );

   $message = $messageApi->create($data);

Create a new message.

.. vale off

**HTTP Request**

.. vale on

``POST /messages/new``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the message
   * - ``name``
     - string
     - Internal name of the message
   * - ``isPublished``
     - boolean
     - Published state
   * - ``publishUp``
     - datetime/null
     - Marketing Message publish date/time
   * - ``publishDown``
     - datetime/null
     - Marketing Message unpublish date/time
   * - ``channels``
     - array
     - Array of Channels


**Response**

``Expected Response Code: 201``

**Properties**

Same as `Get Marketing Message <#get-message>`_.

.. vale off

Edit Marketing Message
**********************

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'name'        => 'New message title',
       'isPublished' => 0
   );

   // Create new a message of ID 1 isn't found?
   $createIfNotFound = true;

   $message = $messageApi->edit($id, $data, $createIfNotFound);

Edit a new message. Note that this supports PUT or PATCH depending on the desired behavior.

**PUT** creates a message if the given ID doesn't exist and clears all the message information, adds the information from the request.
**PATCH** fails if the message with the given ID doesn't exist and updates the message field values with the values from the request.

.. vale off

**HTTP Request**

.. vale on

To edit a message and return a 404 if the message isn't found:

``PATCH /messages/ID/edit``

To edit a message and create a new one if the message isn't found:

``PUT /messages/ID/edit``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the message
   * - ``name``
     - string
     - Internal name of the message
   * - ``isPublished``
     - ``boolean``
     - Published state
   * - ``publishUp``
     - datetime/null
     - Marketing Message publish date/time
   * - ``publishDown``
     - datetime/null
     - Marketing Message unpublish date/time
   * - ``channels``
     - array
     - Array of Channels


**Response**

If ``PUT``, the expected response code is ``200`` if editing a Marketing Message or ``201`` if creating one.

If ``PATCH``, the expected response code is ``200``.

**Properties**

Same as `Get Marketing Message <#get-message>`_.

.. vale off

Delete Marketing Message
************************

.. vale on

.. code-block:: php

   <?php

   $message = $messageApi->delete($id);

Delete a message.

.. vale off

**HTTP Request**

.. vale on

``DELETE /messages/ID/delete``

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get Marketing Message <#get-message>`_.
