Point Triggers
##############

Use this endpoint to obtain details on Mautic's Point Triggers.

**Using Mautic's API Library**

You can interact with this API through the :xref:`Mautic API Library` as follows, or use the various http endpoints as described in this document.

.. code-block:: php

   <?php
   use Mautic\MauticApi;
   use Mautic\Auth\ApiAuth;

   // ...
   $initAuth   = new ApiAuth();
   $auth       = $initAuth->newAuth($settings);
   $apiUrl     = "https://mautic.example.com";
   $api        = new MauticApi();
   $triggerApi = $api->newApi("pointTriggers", $auth, $apiUrl);

.. vale off

Get Point Trigger
*****************

.. vale on

.. code-block:: php

   <?php

   //...
   $trigger = $triggerApi->get($id);

Get an individual Point Trigger by ID.

.. vale off

**HTTP Request**

.. vale on

``GET /points/triggers/ID``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "trigger": {
            "id": 1,
            "name": "Trigger test",
            "description": null,
            "category": null,      
            "isPublished": true,      
            "publishUp": null,
            "publishDown": null,
            "dateAdded": "2015-07-23T03:20:42-05:00",
            "createdBy": 1,
            "createdByUser": "Joe Smith",
            "dateModified": null,
            "modifiedBy": null,
            "modifiedByUser": null,
            "points": 10,
            "color": "ab5959",
            "events": {
                "1": {
                    "id": 1,
                    "type": "email.send",
                    "name": "Send email",
                    "description": null,
                    "order": 1,
                    "properties": {
                       "email": 21
                    }
                }
            }
        }
   }

**Point Trigger Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Point Trigger
   * - ``name``
     - string
     - Name of the Point Trigger
   * - ``description``
     - string/null
     - Description of the Point Trigger
   * - ``category``
     - string
     - Category name
   * - ``isPublished``
     - boolean
     - Published state
   * - ``publishUp``
     - datetime/null
     - Point Trigger publish date/time
   * - ``publishDown``
     - datetime/null
     - Point Trigger unpublish date/time
   * - ``dateAdded``
     - ``datetime``
     - Point Trigger creation date/time
   * - ``createdBy``
     - int
     - ID of the User that created the Point Trigger
   * - ``createdByUser``
     - string
     - Name of the User that created the Point Trigger
   * - ``dateModified``
     - datetime/null
     - Date/time Point Trigger was last modified
   * - ``modifiedBy``
     - int
     - ID of the User that last modified the Point Trigger
   * - ``modifiedByUser``
     - string
     - Name of the User that last modified the Point Trigger
   * - ``points``
     - int
     - The minimum number of Points before the trigger events get executed
   * - ``color``
     - string
     - Color hex to highlight the Contact with. This value doesn't include the pound sign ``#``
   * - ``events``
     - array
     - Array of TriggerEvent entities for this trigger. See below.


**Trigger Event Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - id
     - int
     - ID of the event
   * - type
     - string
     - Event type
   * - name
     - string
     - Name of the event
   * - description
     - string
     - Description of the event
   * - order
     - int
     - Event order
   * - properties
     - array
     - Configured properties for the event

.. vale off

List Point Triggers
*******************

.. vale on

.. code-block:: php

   <?php
   // ...

   $triggers = $triggerApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

**HTTP Request**

.. vale on

``GET /points/triggers``

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
       "triggers": [
           {
               "id": 1,
               "name": "Trigger test",
               "description": null,
               "category": null,      
               "isPublished": true,      
               "publishUp": null,
               "publishDown": null,
               "dateAdded": "2015-07-23T03:20:42-05:00",
               "createdBy": 1,
               "createdByUser": "Joe Smith",
               "dateModified": null,
               "modifiedBy": null,
               "modifiedByUser": null,
               "points": 10,
               "color": "ab5959",
               "events": {
                   "1": {
                       "id": 1,
                       "type": "email.send",
                       "name": "Send email",
                       "description": null,
                       "order": 1,
                       "properties": {
                           "email": 21
                       }
                   }
               }
           }
       ]
   }

**Properties**

Same as `Get Point Trigger <#get-point-trigger>`_.

.. vale off

Create Point Trigger
********************

.. vale on

.. code-block:: php

   <?php 

   $data = array(
       'name' => 'test',
       'description' => 'created as a API test',
       'points' => 5,
       'color' => '4e5d9d',
       'trigger_existing_leads' => false,
       'events' => array(
           array(
               'name' => 'tag test event',
               'description' => 'created as a API test',
               'type' => 'lead.changetags',
               'order' => 1,
               'properties' => array(
                   'add_tags' => array('tag-a'),
                   'remove_tags' => array()
               )
           ),
           array(
               'name' => 'send email test event',
               'description' => 'created as a API test',
               'type' => 'email.send',
               'order' => 2,
               'properties' => array(
                   'email' => 1
               )
           )
       )
   );

   $trigger = $triggerApi->create($data);

Create a new Point Trigger.

.. vale off

**HTTP Request**

.. vale on

``POST /points/triggers/new``

**POST Parameters**

Same as `Get Point Trigger <#get-point-trigger>`_. You can create or edit Point Trigger events via the Point Trigger event arrays placed in the Point Trigger array.

**Response**

``Expected Response Code: 201``

**Properties**

Same as `Get Point Trigger <#get-point-trigger>`_.

.. vale off

Edit Point Trigger
******************

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'name' => 'test',
       'description' => 'created as a API test',
       'points' => 5,
       'color' => '4e5d9d',
       'trigger_existing_leads' => false,
       'events' => array(
           array(
               'name' => 'tag test event',
               'description' => 'created as a API test',
               'type' => 'lead.changetags',
               'order' => 1,
               'properties' => array(
                   'add_tags' => array('tag-a'),
                   'remove_tags' => array()
               )
           ),
           array(
               'name' => 'send email test event',
               'description' => 'created as a API test',
               'type' => 'email.send',
               'order' => 2,
               'properties' => array(
                   'email' => 1
               )
           )
       )
   );

   // Create new a Point Trigger of ID 1 isn't found?
   $createIfNotFound = true;

   $trigger = $triggerApi->edit($id, $data, $createIfNotFound);

Edit a new Point Trigger. Note that this supports PUT or PATCH depending on the desired behavior.

**PUT** creates a Point Trigger if the given ID doesn't exist and clears all the Point Trigger information, adds the information from the request. Point Trigger events also get deleted if not present in the request.

**PATCH** fails if the Point Trigger with the given ID doesn't exist and updates the Point Trigger field values with the values Point Trigger the request.

.. vale off

**HTTP Request**

.. vale on

To edit a Point Trigger and return a 404 if the Point Trigger isn't found:

``PATCH /points/triggers/ID/edit``

To edit a Point Trigger and create a new one if the Point Trigger isn't found:

``PUT /points/triggers/ID/edit``

**POST Parameters**

Same as `Get Point Trigger <#get-point-trigger>`_. You can create or edit Point Trigger events via the Point Triggers event arrays placed in the Point Trigger array.

**Response**

If ``PUT``, the expected response code is ``200`` if editing an existing Point Trigger or ``201`` if creating a new one.

If ``PATCH``, the expected response code is ``200``.

**Properties**

Same as `Get Point Trigger <#get-point-trigger>`_.

.. vale off

Delete Point Trigger
********************

.. vale on

.. code-block:: php

   <?php

   $trigger = $triggerApi->delete($id);

Delete a Point Trigger.

.. vale off

**HTTP Request**

.. vale on

``DELETE /points/triggers/ID/delete``

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get Point Trigger <#get-point-trigger>`_.

.. vale off

Delete Point Trigger Events
***************************

.. vale on

The following examples show how to delete events with ID 56 and 59.

.. code-block:: php

   <?php

   $trigger = $triggerApi->deleteFields($triggerId, array(56, 59));

Delete a Point Trigger event.

.. vale off

**HTTP Request**

.. vale on

``DELETE /points/triggers/ID/events/delete?events[]=56&events[]=59``

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get Point Trigger <#get-point-trigger>`_.

.. vale off

Get Point Trigger Event Types
*****************************

.. vale on

.. code-block:: php

   <?php

   $point = $pointApi->getEventTypes();

Get array of available Point Trigger Event Types

.. vale off

**HTTP Request**

.. vale on

``GET /points/triggers/events/types``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {  
       "eventTypes":{  
           "campaign.changecampaign":"Modify contact's campaigns",
           "lead.changelists":"Modify contact's segments",
           "lead.changetags":"Modify contact's tags",
           "plugin.leadpush":"Push contact to integration",
           "email.send":"Send an email"
       }
   }
