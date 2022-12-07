
Campaigns
#########

Use this endpoint to obtain details on Mautic's Campaigns.

**Using Mautic's API Library**

You can interact with this API through the :xref:`Mautic API Library` as follows, or use the various http endpoints as described in this document.

.. code-block:: php

   <?php
   use Mautic\MauticApi;
   use Mautic\Auth\ApiAuth;

   // ...
   $initAuth    = new ApiAuth();
   $auth        = $initAuth->newAuth($settings);
   $apiUrl      = "https://your-mautic.com";
   $api         = new MauticApi();
   $campaignApi = $api->newApi("campaigns", $auth, $apiUrl);

.. vale off

Get campaign
************

.. vale on

.. code-block:: php

   <?php

   //...
   $campaign = $campaignApi->get($id);

Get an individual Campaign by ID.

.. vale off

**HTTP Request**

.. vale on

``GET /campaigns/ID``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "campaign": {
           "id": 3,
           "name": "Email A/B Test",
           "description": null,
           "isPublished": true,
           "publishUp": null,
           "publishDown": null,
           "dateAdded": "2015-07-15T15:06:02-05:00",
           "createdBy": 1,
           "createdByUser": "Joe Smith",
           "dateModified": "2015-07-20T13:11:56-05:00",
           "modifiedBy": 1,
           "modifiedByUser": "Joe Smith",
           "category": null,
           "events": {
               "28": {
                   "id": 28,
                   "type": "lead.changepoints",
                   "eventType": "action",
                   "name": "Adjust lead points",
                   "description": null,
                   "order": 1,
                   "properties": {
                     "points": 20
                   },
                   "triggerDate": null,
                   "triggerInterval": 1,
                   "triggerIntervalUnit": "d",
                   "triggerMode": "immediate",
                   "children": [],
                   "parent": null,
                   "decisionPath": null
               }
           }
       }
   }

**Campaign Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Campaign
   * - ``name``
     - string
     - Name of the Campaign
   * - ``description``
     - string/null
     - Description of the Campaign
   * - ``alias``
     - string
     - Used to generate the URL for the Campaign
   * - ``isPublished``
     - boolean
     - Published state
   * - ``publishUp``
     - datetime/null
     - Date/time when the Campaign should get published
   * - ``publishDown``
     - datetime/null
     - Date/time the Campaign should get unpublished
   * - ``dateAdded``
     - ``datetime``
     - Date/time Campaign got created
   * - ``createdBy``
     - int
     - ID of the User that created the Campaign
   * - ``createdByUser``
     - string
     - Name of the User that created the Campaign
   * - ``dateModified``
     - datetime/null
     - Date/time Campaign was last modified
   * - ``modifiedBy``
     - int
     - ID of the User that last modified the Campaign
   * - ``modifiedByUser``
     - string
     - Name of the User that last modified the Campaign
   * - ``events``
     - array
     - Array of Event entities for the Campaign. See below.


**Event Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the event
   * - ``name``
     - string
     - Name of the event
   * - ``description``
     - string
     - Optional description for the event
   * - ``type``
     - string
     - Type of event
   * - ``eventType``
     - string
     - "action" or "decision"
   * - ``order``
     - int
     - Order in relation to the other events - used for levels
   * - ``properties``
     - object
     - Configured properties for the event
   * - ``triggerMode``
     - string
     - ``immediate``, ``interval`` or ``date``
   * - ``triggerDate``
     - datetime/null
     - Date/time of when the event should trigger if ``triggerMode`` is "date"
   * - ``triggerInterval``
     - int/null
     - Interval for when the event should trigger
   * - ``triggerIntervalUnit``
     - string
     - Interval unit for when the event should trigger. Options are ``i = minutes``, ``h = hours``, ``d = days``, ``m = months``, ``y = years``
   * - ``children``
     - array
     - Array of this event's children ,
   * - ``parent``
     - object/null
     - This event's parent
   * - ``decisionPath``
     - string/null
     - If the event connects to an action, this value is "no" for the non-decision path or "yes" for the actively followed path.

.. vale off

List campaigns
**************

.. vale on

.. code-block:: php

   <?php
   // ...

   $campaigns = $campaignApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

**HTTP Request**

.. vale on

``GET /campaigns``

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
   * - ``published``
     - Only return currently published entities.
   * - ``minimal``
     - Return only array of entities without additional lists in it.


**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "total": 1,
       "campaigns": {
           "3": {
               "id": 3,
               "name": "Welcome Campaign",
               "description": null,
               "isPublished": true,
               "publishUp": null,
               "publishDown": null,
               "dateAdded": "2015-07-15T15:06:02-05:00",
               "createdBy": 1,
               "createdByUser": "Joe Smith",
               "dateModified": "2015-07-20T13:11:56-05:00",
               "modifiedBy": 1,
               "modifiedByUser": "Joe Smith",
               "category": null,
               "events": {
                   "22": {
                       "id": 22,
                       "type": "email.send",
                       "eventType": "action",
                       "name": "Send welcome email",
                       "description": null,
                       "order": 1,
                       "properties": {
                           "email": 1
                       },
                       "triggerMode": "immediate",
                       "triggerDate": null,
                       "triggerInterval": null,
                       "triggerIntervalUnit": null,
                       "children": [],
                       "parent": null,
                       "decisionPath": null
                   },
                   "28": {
                       "id": 28,
                       "type": "lead.changepoints",
                       "eventType": "action",
                       "name": "Adjust lead points",
                       "description": null,
                       "order": 2,
                       "properties": {
                           "points": 20
                       },
                       "triggerMode": "immediate",                
                       "triggerDate": null,
                       "triggerInterval": null,
                       "triggerIntervalUnit": null,
                       "children": [],
                       "parent": null,
                       "decisionPath": null
                   }
               }
           }
       }
   }

**Properties**

Same as `Get Campaign <#get-campaign>`_.

.. vale off

List Campaign Contacts
**********************

.. vale on

This endpoint is basically an alias for the stats endpoint with ``campaign_leads`` table and ``campaign_id`` specified. Other parameters are the same as in the stats endpoint.

.. code-block:: php

   <?php
   // ...

   $response = $campaignApi->getContacts($campaignId, $start, $limit, $order, $where);

.. vale off

**HTTP Request**

.. vale on

``GET /campaigns/ID/contacts``

**Query Parameters**

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {  
     "total":"1",
     "contacts":[  
       {  
         "campaign_id":"311",
         "lead_id":"3126",
         "date_added":"2017-01-25 15:11:10",
         "manually_removed":"0",
         "manually_added":"1"
       }
     ]
   }

.. vale off

Create campaign
***************

.. vale on

.. code-block:: php

   <?php

   $data = array(
       'name'        => 'Campaign A',
       'description' => 'This is my first Campaign created via API.',
       'isPublished' => 1
   );

   $campaign = $campaignApi->create($data);

Create a new Campaign. To see more advanced example with Campaign events and so on, see the unit tests.

.. vale off

**HTTP Request**

.. vale on

``POST /campaigns/new``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``name``
     - string
     - Campaign name is the only required field
   * - ``alias``
     - string
     - Used to generate the URL for the Campaign
   * - ``description``
     - string
     - A description of the Campaign.
   * - ``isPublished``
     - int
     - A value of 0 or 1


**Response**

``Expected Response Code: 201``

**Properties**

Same as `Get Campaign <#get-campaign>`_.

.. vale off

Clone a campaign
****************

.. vale on

.. code-block:: php

   <?php

   $camnpaignId = 12;

   $campaign = $campaignApi->cloneCampaign($campaignId);

Clone an existing Campaign. To see more advanced example with Campaign events and so on, see the unit tests.

.. vale off

**HTTP Request**

.. vale on

``POST /campaigns/clone/CAMPAIGN_ID``

**Response**

``Expected Response Code: 201``

**Properties**

Same as `Get Campaign <#get-campaign>`_.

.. vale off

Edit campaign
*************

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'name'        => 'New Campaign name',
       'isPublished' => 0
   );

   // Create new a Campaign of ID 1 isn't found?
   $createIfNotFound = true;

   $campaign = $campaignApi->edit($id, $data, $createIfNotFound);

Edit a new Campaign. Note that this supports PUT or PATCH depending on the desired behavior.

**PUT** creates a Campaign if the given ID doesn't exist and clears all the Campaign information, adds the information from the request.
**PATCH** fails if the Campaign with the given ID doesn't exist and updates the Campaign field values with the values from the request.

.. vale off

**HTTP Request**

.. vale on

To edit a Campaign and return a 404 if the Campaign isn't found:

``PATCH /campaigns/ID/edit``

To edit a Campaign and create a new one if the Campaign isn't found:

``PUT /campaigns/ID/edit``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - ``name``
     - Campaign name is the only required field
   * - ``alias``
     - Name alias generated automatically if not set
   * - ``description``
     - A description of the Campaign.
   * - ``isPublished``
     - A value of 0 or 1


**Response**

If ``PUT``, the expected response code is ``200`` if the Campaign got edited or ``201`` if created.

If ``PATCH``, the expected response code is ``200``.

**Properties**

Same as `Get Campaign <#get-campaign>`_.

.. vale off

Delete campaign
***************

.. vale on

.. code-block:: php

   <?php

   $campaign = $campaignApi->delete($id);

Delete a Campaign.

.. vale off

**HTTP Request**

.. vale on

``DELETE /campaigns/ID/delete``

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get Campaign <#get-campaign>`_.

.. vale off

Add contact to a campaign
*************************

.. vale on

.. code-block:: php

   <?php

   //...
   $response = $campaignApi->addContact($campaignId, $contactId);
   if (!isset($response['success'])) {
       // handle error
   }

Manually add a Contact to a specific Campaign.

.. vale off

**HTTP Request**

.. vale on

``POST /campaigns/CAMPAIGN_ID/contact/CONTACT_ID/add``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "success": true
   }

.. vale off

Remove contact from a campaign
******************************

.. vale on

.. code-block:: php

   <?php

   //...
   $response = $listApi->removeContact($campaignId, $contactId);
   if (!isset($response['success'])) {
       // handle error
   }

Manually remove a Contact from a specific Campaign.

.. vale off

**HTTP Request**

.. vale on

``POST /campaigns/CAMPAIGN_ID/contact/CONTACT_ID/remove``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "success": true
   }
