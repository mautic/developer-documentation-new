Segments
########

Use this endpoint to obtain details on Mautic's Contact Segments or to manipulate Contact memberships.

**Using Mautic's API Library**

You can interact with this API through the :xref:`Mautic API Library` as follows, or use the various http endpoints as described in this document.

.. code-block:: php

   <?php
   use Mautic\MauticApi;
   use Mautic\Auth\ApiAuth;

   // ...
   $initAuth   = new ApiAuth();
   $auth       = $initAuth->newAuth($settings);
   $apiUrl     = "https://example.com";
   $api        = new MauticApi();
   $segmentApi = $api->newApi("segments", $auth, $apiUrl);

.. vale off

Get Segment
***********

.. vale on

.. code-block:: php

   <?php

   //...
   $segment = $segmentApi->get($id);

Get an individual Segment by ID.

.. vale off

**HTTP Request**

.. vale on

``GET /segments/ID``

**Response**

``Expected Response Code: 200``

.. code-block:: json

       "list": {
           "id": 47,
           "isPublished": 1,
           "dateAdded": "2015-07-21T12:27:12-05:00",
           "createdBy": 1,
           "createdByUser": "Joe Smith",
           "dateModified": "2015-07-21T14:12:03-05:00",
           "modifiedBy": 1,
           "modifiedByUser": "Joe Smith",
           "category": null,
           "name": "Segment A",
           "alias": "segment-a",
           "description": "This is my first Segment created via API.",
           "filters": [
             {
               "glue": "and",
               "field": "city",
               "type": "text",
               "filter": "Prague",
               "display": null,
               "operator": "=",
             }
           ],
           "isGlobal": true
       }

**Segment Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Segment
   * - ``isPublished``
     - boolean
     - Published state
   * - ``dateAdded``
     - ``datetime``
     - Segment creation date/time
   * - ``createdBy``
     - int
     - ID of the User that created the Segment
   * - ``createdByUser``
     - string
     - Name of the User that created the Segment
   * - ``dateModified``
     - datetime/null
     - Date/time Segment was last modified
   * - ``modifiedBy``
     - int
     - ID of the User that last modified the Segment
   * - ``modifiedByUser``
     - string
     - Name of the User that last modified the Segment
   * - ``category``
     - object/null
     - Object with the Category details
   * - ``name``
     - string
     - Segment name
   * - ``alias``
     - string
     - Segment alias
   * - ``description``
     - string
     - Segment description
   * - ``filters``
     - array
     - Smart filters for the Segment. See filter properties bellow
   * - ``isGlobal``
     - boolean
     - Whether the Segment is global. 0 means only the author can see it.


**Segment Filter Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``glue``
     - string
     - How to glue the filters to others. Possible values: ``and``, ``or``
   * - ``field``
     - string
     - Alias of the Contact or Company field to based the filter on
   * - ``object``
     - string
     - Object which have the field. Possible values: ``lead`` for Contacts, or ``company``
   * - ``type``
     - string
     - Type of the field. Possible values: 'boolean', ``date`` (format ``Y-m-d``\ ), ``datetime`` (format ``Y-m-d H:i:s``\ ), ``email``\ , ``country``\ , ``locale``\ , ``lookup``\ , ``number``\ , ``tel``\ , ``region``\ , ``select``\ , ``multiselect``\ , ``text``\ , ``textarea``\ , ``time``\ , ``timezone``\ , ``url``
   * - ``operator``
     - string
     - Operator used for matching the values. Possible values: '=', ``!=``\ , ``empty``\ , ``!empty``\ , ``like``\ , ``!like``\ , ``regexp``\ , ``!regexp``\ , ``startsWith``\ , ``endsWith``\ , ``contains``

.. vale off

List Contact Segments
*********************

.. vale on

.. code-block:: php

   <?php

   //...
   $segments = $segmentApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

Returns a list of Contact Segments available to the User. This list isn't filterable.

.. vale off

**HTTP Request**

.. vale on

``GET /segments``

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


**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
     "total": 13,
     "lists": [
       {
           "id": 47,
           "isPublished": 1,
           "dateAdded": "2015-07-21T12:27:12-05:00",
           "createdBy": 1,
           "createdByUser": "Joe Smith",
           "dateModified": "2015-07-21T14:12:03-05:00",
           "modifiedBy": 1,
           "modifiedByUser": "Joe Smith",
           "category": null,
           "name": "Segment A",
           "alias": "segment-a",
           "description": "This is my first Segment created via API.",
           "filters": [
             {
               "glue": "and",
               "field": "city",
               "type": "text",
               "filter": "Prague",
               "display": null,
               "operator": "=",
             }
           ],
           "isGlobal": true
       }
     ]
   }

**Segment Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``total``
     - int
     - Count of all Segments
   * - ``id``
     - int
     - ID of the Segment
   * - ``isPublished``
     - boolean
     - Published state
   * - ``dateAdded``
     - ``datetime``
     - Segment creation date/time
   * - ``createdBy``
     - int
     - ID of the User that created the Segment
   * - ``createdByUser``
     - string
     - Name of the User that created the Segment
   * - ``dateModified``
     - datetime/null
     - Date/time Segment was last modified
   * - ``modifiedBy``
     - int
     - ID of the User that last modified the Segment
   * - ``modifiedByUser``
     - string
     - Name of the User that last modified the Segment
   * - ``category``
     - object/null
     - Object with the Category details
   * - ``name``
     - string
     - Segment name
   * - ``alias``
     - string
     - Segment alias
   * - ``description``
     - string
     - Segment description
   * - ``filters``
     - array
     - Smart filters for the Segment. See filter properties bellow
   * - ``isGlobal``
     - boolean
     - Whether the Segment is global. 0 means only the author can see it.


**Segment Filter Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - glue
     - string
     - How to glue the filters to others. Possible values: ``and``\ , ``or``
   * - field
     - string
     - Alias of the Contact or Company field to based the filter on
   * - object
     - string
     - Object which have the field. Possible values: ``lead`` for Contacts, or ``company``
   * - type
     - string
     - Type of the field. Possible values: 'boolean', ``date`` (format ``Y-m-d``\ ), ``datetime`` (format ``Y-m-d H:i:s``\ ), ``email``\ , ``country``\ , ``locale``\ , ``lookup``\ , ``number``\ , ``tel``\ , ``region``\ , ``select``\ , ``multiselect``\ , ``text``\ , ``textarea``\ , ``time``\ , ``timezone``\ , ``url``
   * - operator
     - string
     - Operator used for matching the values. Possible values: '=', ``!=``\ , ``empty``\ , ``!empty``\ , ``like``\ , ``!like``\ , ``regexp``\ , ``!regexp``\ , ``startsWith``\ , ``endsWith``\ , ``contains``

.. vale off

Create Segment
**************

.. vale on

.. code-block:: php

   <?php

   $data = array(
       'name'        => 'Segment A',
       'alias'       => 'segment-a',
       'description' => 'This is my first Segment created via API.',
       'isPublished' => 1,
       'filters' => array(
           array(
               'glue' => 'and',
               'field' => 'email',
               'object' => 'lead',
               'type' => 'email',
               'filter' => '*@gmail.com',
               'operator' => 'like',
           ),
       ),
   );

   $segment = $segmentApi->create($data);

Create a new Segment.

.. vale off

**HTTP Request**

.. vale on

``POST /segments/new``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``name``
     - string
     - Segment name is the only required field
   * - ``alias``
     - string
     - Name alias generated automatically if not set
   * - ``description``
     - string
     - A description of the Segment.
   * - ``isPublished``
     - int
     - A value of 0 or 1
   * - ``isGlobal``
     - boolean
     - Whether the Segment is global. 0 means only the author can see it.
   * - ``filters``
     - array
     - Array of filters. See possible properties bellow.


**Segment Filter Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``glue``
     - string
     - How to glue the filters to others. Possible values: ``and``\ , ``or``
   * - ``field``
     - string
     - Alias of the Contact or Company field to based the filter on
   * - ``object``
     - string
     - Object which have the field. Possible values: ``lead`` for Contacts, or ``company``
   * - ``type``
     - string
     - Type of the field. Possible values: 'boolean', ``date`` (format ``Y-m-d``\ ), ``datetime`` (format ``Y-m-d H:i:s``\ ), ``email``\ , ``country``\ , ``locale``\ , ``lookup``\ , ``number``\ , ``tel``\ , ``region``\ , ``select``\ , ``multiselect``\ , ``text``\ , ``textarea``\ , ``time``\ , ``timezone``\ , ``url``
   * - ``operator``
     - string
     - Operator used for matching the values. Possible values: '=', ``!=``\ , ``empty``\ , ``!empty``\ , ``like``\ , ``!like``\ , ``regexp``\ , ``!regexp``\ , ``startsWith``\ , ``endsWith``\ , ``contains``


**Response**

``Expected Response Code: 201``

**Properties**

Same as `Get Segment <#get-segment>`_.

.. vale off

Edit Segment
************

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'name'        => 'New Segment name',
       'isPublished' => 0
   );

   // Create new a Segment of ID 1 isn't found?
   $createIfNotFound = true;

   $segment = $segmentApi->edit($id, $data, $createIfNotFound);

Edit a new Segment. Note that this supports PUT or PATCH depending on the desired behavior.

**PUT** creates a Segment if the given ID doesn't exist and clears all the Segment information, adds the information from the request.

**PATCH** fails if the Segment with the given ID doesn't exist and updates the Segment field values with the values from the request.

.. vale off

**HTTP Request**

.. vale on

To edit a Segment and return a 404 if the Segment isn't found:

``PATCH /segments/ID/edit``

To edit a Segment and create a new one if the Segment isn't found:

``PUT /segments/ID/edit``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``name``
     - string
     - Segment name is the only required field
   * - ``alias``
     - string
     - Name alias generated automatically if not set
   * - ``description``
     - string
     - A description of the Segment.
   * - ``isPublished``
     - int
     - A value of 0 or 1
   * - ``isGlobal``
     - boolean
     - Whether the Segment is global. 0 means only the author can see it.
   * - ``filters``
     - array
     - Array of filters. See possible properties bellow.

**Segment Filter Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``glue``
     - string
     - How to glue the filters to others. Possible values: ``and``\ , ``or``
   * - ``field``
     - string
     - Alias of the Contact or Company field to based the filter on
   * - ``object``
     - string
     - Object which have the field. Possible values: ``lead`` for Contacts, or ``company``
   * - ``type``
     - string
     - Type of the field. Possible values: 'boolean', ``date`` (format ``Y-m-d``\ ), ``datetime`` (format ``Y-m-d H:i:s``\ ), ``email``\ , ``country``\ , ``locale``\ , ``lookup``\ , ``number``\ , ``tel``\ , ``region``\ , ``select``\ , ``multiselect``\ , ``text``\ , ``textarea``\ , ``time``\ , ``timezone``\ , ``url``
   * - ``operator``
     - string
     - Operator used for matching the values. Possible values: '=', ``!=``\ , ``empty``\ , ``!empty``\ , ``like``\ , ``!like``\ , ``regexp``\ , ``!regexp``\ , ``startsWith``\ , ``endsWith``\ , ``contains``


**Response**

If ``PUT``, the expected response code is ``200`` if editing a Segment or ``201`` if creating a new one.

If ``PATCH``, the expected response code is ``200``.

**Properties**

Same as `Get Segment <#get-segment>`_.

.. vale off

Delete Segment
**************

.. vale on

.. code-block:: php

   <?php

   $segment = $segmentApi->delete($id);

Delete a Segment.

.. vale off

**HTTP Request**

.. vale on

``DELETE /segments/ID/delete``

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get Segment <#get-segment>`_.

.. vale off

Add Contact to a Segment
************************

.. vale on

.. code-block:: php

   <?php

   //...
   $response = $segmentApi->addContact($segmentId, $contactId);
   if (!isset($response['success'])) {
       // handle error
   }

Manually add a Contact to a specific Segment.

.. vale off

**HTTP Request**

.. vale on

``POST /segments/SEGMENT_ID/contact/CONTACT_ID/add``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "success": true
   }

.. vale off

Add Contacts to a Segment
*************************

.. vale on

.. code-block:: php

   <?php

   //...
   $contactIds = ['ids'=>[ 1, 45, 39]];
   $response = $segmentApi->addContact($segmentId, $contactIds);
   if (!isset($response['success'])) {
       // handle error
   }

Manually add Contacts to a specific Segment.

.. vale off

**HTTP Request**

.. vale on

``POST /segments/SEGMENT_ID/contacts/add``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
        "success":true,
        "details":{
           "1" :{"success":true},
           "45":{"success":true},
           "39":{"success":false}
        }
   }

.. vale off

Remove Contact from a Segment
*****************************

.. vale on

.. code-block:: php

   <?php

   //...
   $response = $segmentApi->removeContact($segmentId, $contactId);
   if (!isset($response['success'])) {
       // handle error
   }

Manually remove a Contact to a specific Segment.

.. vale off

**HTTP Request**

.. vale on

``POST /segments/SEGMENT_ID/contact/CONTACT_ID/remove``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "success": true
   }
