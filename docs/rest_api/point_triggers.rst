Point Triggers
##############

Use this endpoint to manipulate and obtain details on Mautic's Point Triggers.

Using the Mautic API library
****************************

.. vale off

You can interact with this API using the :xref:`Mautic API Library` as below, or the various HTTP endpoints described in this document.

.. vale on

.. code-block:: php

   <?php
   use Mautic\MauticApi;
   use Mautic\Auth\ApiAuth;

   // ...
   $initAuth   = new ApiAuth();
   $auth       = $initAuth->newAuth($settings);
   $apiUrl     = "https://example.com";
   $api        = new MauticApi();
   $triggerApi = $api->newApi("pointTriggers", $auth, $apiUrl);

.. vale off

Get Point Trigger
*****************

.. vale on

Retrieves an individual Point Trigger by ID.

.. code-block:: php

   <?php

   //...
   $trigger = $triggerApi->get($id);

.. vale off

HTTP request
============

.. vale on

``GET /points/triggers/ID``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Point Trigger.

.. _get Point Trigger response:

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

.. _get Point Trigger properties:

Properties
----------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - integer
     - ID of the Point Trigger
   * - ``name``
     - string
     - Name of the Point Trigger
   * - ``description``
     - string/null
     - Description of the Point Trigger
   * - ``category``
     - string/null
     - Category name
   * - ``isPublished``
     - boolean
     - Published state
   * - ``publishUp``
     - datetime/null
     - Date and time when the Point Trigger should activate
   * - ``publishDown``
     - datetime/null
     - Date and time when the Point Trigger should deactivate
   * - ``dateAdded``
     - datetime
     - Date and time the Point Trigger was created
   * - ``createdBy``
     - integer
     - ID of the User that created the Point Trigger
   * - ``createdByUser``
     - string
     - Name of the User that created the Point Trigger
   * - ``dateModified``
     - datetime/null
     - Date and time the Point Trigger was last modified
   * - ``modifiedBy``
     - integer/null
     - ID of the User that last modified the Point Trigger
   * - ``modifiedByUser``
     - string/null
     - Name of the User that last modified the Point Trigger
   * - ``points``
     - integer
     - Minimum number of points a Contact must reach before Mautic runs the trigger events
   * - ``color``
     - string
     - Hex color used to highlight the Contact. This value doesn't include the leading pound sign (#)
   * - ``events``
     - array
     - Array of trigger event entities for this Point Trigger. See :ref:`Trigger event properties <trigger event properties>`

.. _trigger event properties:

Trigger event properties
------------------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - integer
     - ID of the event
   * - ``type``
     - string
     - Event type
   * - ``name``
     - string
     - Name of the event
   * - ``description``
     - string/null
     - Description of the event
   * - ``order``
     - integer
     - Event order
   * - ``properties``
     - array
     - Configured properties for the event

.. vale off

List Point Triggers
*******************

.. vale on

Retrieves a list of Point Triggers.

.. code-block:: php

   <?php

   //...
   $triggers = $triggerApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

HTTP request
============

.. vale on

``GET /points/triggers``

Query parameters
----------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``searchFilter``
     - string
     - String or search command to filter entities
   * - ``start``
     - integer
     - Starting row for the returned entities - defaults to 0
   * - ``limit``
     - integer
     - Maximum number of entities to return - defaults to 30
   * - ``orderBy``
     - string
     - Column to sort by. Any column in the response is valid.

       **Note**: convert ``camelCase`` properties to ``snake_case``. For example, ``dateAdded`` becomes ``date_added``
   * - ``orderByDir``
     - string
     - Order direction - ``asc`` or ``desc``
   * - ``publishedOnly``
     - boolean
     - Returns only currently published entities
   * - ``minimal``
     - boolean
     - Returns only an array of entities without additional lists in it

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Point Triggers list.

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

Properties
----------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``total``
     - integer
     - Total count of Point Triggers
   * - ``triggers``
     - array
     - Array of Point Triggers

.. vale off

For the rest of the properties, refer to :ref:`Point Trigger properties <get Point Trigger properties>`.

.. vale on

.. vale off

Create Point Trigger
********************

.. vale on

Creates a new Point Trigger.

.. code-block:: php

   <?php

   $data = array(
       'name'                   => 'test',
       'description'            => 'created as an API test',
       'points'                 => 5,
       'color'                  => '4e5d9d',
       'trigger_existing_leads' => false,
       'events'                 => array(
           array(
               'name'        => 'tag test event',
               'description' => 'created as an API test',
               'type'        => 'lead.changetags',
               'order'       => 1,
               'properties'  => array(
                   'add_tags'    => array('tag-a'),
                   'remove_tags' => array(),
               ),
           ),
           array(
               'name'        => 'send email test event',
               'description' => 'created as an API test',
               'type'        => 'email.send',
               'order'       => 2,
               'properties'  => array(
                   'email' => 1,
               ),
           ),
       ),
   );

   $trigger = $triggerApi->create($data);

.. vale off

HTTP request
============

.. vale on

``POST /points/triggers/new``

.. _create Point Trigger POST parameters:

POST parameters
---------------

.. list-table::
   :widths: 30 20 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``name``
     - string
     - **Required.**

       Name of the Point Trigger
   * - ``description``
     - string
     - Description of the Point Trigger
   * - ``points``
     - integer
     - Minimum number of points a Contact must reach before Mautic runs the trigger events
   * - ``color``
     - string
     - Hex color used to highlight the Contact. This value doesn't include the leading pound sign (#)
   * - ``trigger_existing_leads``
     - boolean
     - Whether to run the trigger against existing Contacts that already meet the point threshold
   * - ``events``
     - array
     - Array of trigger events to attach to the Point Trigger. Create or edit events through the trigger event arrays placed in the ``events`` array

Response
========

* Returns ``201 Created`` when the request successfully creates the Point Trigger.

Properties
----------

Refer to :ref:`Point Trigger properties <get Point Trigger properties>`.

.. vale off

Edit Point Trigger
******************

.. vale on

Edits a Point Trigger.

This operation supports ``PUT`` or ``PATCH`` depending on the desired behavior:

* ``PUT``: **full replacement**. The request creates a Point Trigger if the ID is missing. If the ID exists, the request clears all existing data, including any trigger events not present in the request, and replaces it with the provided values.
* ``PATCH``: **partial update**. The request only updates field values based on the request data. The request fails when the Point Trigger ID doesn't exist.

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'name'                   => 'test',
       'description'            => 'created as an API test',
       'points'                 => 5,
       'color'                  => '4e5d9d',
       'trigger_existing_leads' => false,
       'events'                 => array(
           array(
               'name'        => 'tag test event',
               'description' => 'created as an API test',
               'type'        => 'lead.changetags',
               'order'       => 1,
               'properties'  => array(
                   'add_tags'    => array('tag-a'),
                   'remove_tags' => array(),
               ),
           ),
           array(
               'name'        => 'send email test event',
               'description' => 'created as an API test',
               'type'        => 'email.send',
               'order'       => 2,
               'properties'  => array(
                   'email' => 1,
               ),
           ),
       ),
   );

   // Create a new Point Trigger if ID 1 isn't found
   $createIfNotFound = true;

   $trigger = $triggerApi->edit($id, $data, $createIfNotFound);

.. vale off

HTTP request
============

.. vale on

* ``PUT /points/triggers/ID/edit``: updates an existing Point Trigger or creates a new one when the ID doesn't exist.
* ``PATCH /points/triggers/ID/edit``: updates an existing Point Trigger. The request fails when the ID doesn't exist.

POST parameters
---------------

Accepts the same parameters as those described in :ref:`Create Point Trigger <create Point Trigger POST parameters>`. You can create or edit trigger events through the trigger event arrays placed in the ``events`` array.

Response
========

* ``PUT``: returns ``200 OK`` when the request successfully updates the Point Trigger or ``201 Created`` when the request creates a Point Trigger.
* ``PATCH``: returns ``200 OK`` when the request successfully updates the Point Trigger or ``404 Not Found`` error when the Point Trigger ID doesn't exist.

The response is a JSON object similar to :ref:`Get Point Trigger <get Point Trigger response>`.

Properties
----------

Refer to :ref:`Point Trigger properties <get Point Trigger properties>`.

.. vale off

Delete Point Trigger
********************

.. vale on

Deletes a Point Trigger.

.. code-block:: php

   <?php

   $trigger = $triggerApi->delete($id);

.. vale off

HTTP request
============

.. vale on

``DELETE /points/triggers/ID/delete``

Response
========

* Returns ``200 OK`` when the request successfully deletes the Point Trigger.

The response is a JSON object containing the data of the deleted Point Trigger, similar to :ref:`Get Point Trigger <get Point Trigger response>`.

Properties
----------

Refer to :ref:`Point Trigger properties <get Point Trigger properties>`.

.. vale off

Delete Point Trigger events
***************************

.. vale on

Deletes one or more events from a Point Trigger. The following example deletes the events with ID 56 and 59.

.. code-block:: php

   <?php

   $trigger = $triggerApi->deleteTriggerEvents($triggerId, array(56, 59));

.. vale off

HTTP request
============

.. vale on

``DELETE /points/triggers/ID/events/delete?events[]=56&events[]=59``

Response
========

* Returns ``200 OK`` when the request successfully deletes the events.

The response is a JSON object containing the data of the updated Point Trigger, similar to :ref:`Get Point Trigger <get Point Trigger response>`.

Properties
----------

Refer to :ref:`Point Trigger properties <get Point Trigger properties>`.

.. vale off

Get Point Trigger event types
*****************************

.. vale on

Retrieves an array of the available trigger event types.

.. code-block:: php

   <?php

   //...
   $eventTypes = $triggerApi->getEventTypes();

.. vale off

HTTP request
============

.. vale on

``GET /points/triggers/events/types``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the event types.

.. code-block:: json

   {
       "eventTypes": {
           "campaign.changecampaign": "Modify contact's campaigns",
           "lead.changelists": "Modify contact's segments",
           "lead.changetags": "Modify contact's tags",
           "plugin.leadpush": "Push contact to integration",
           "email.send": "Send an email"
       }
   }
