.. vale off

.. note::

  The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

  If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

  Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Segments
########

Use this endpoint to manipulate and obtain details on Mautic's Segments (also known as Lists).

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

HTTP request
============

.. vale on

``GET /segments/ID``

Response
========

``Expected Response Code: 200``

.. code-block:: json

   {
       "list": {
           "id": 1,
           "isPublished": true,
           "dateAdded": "2015-07-15T15:06:02-05:00",
           "createdBy": 1,
           "createdByUser": "Joe Smith",
           "dateModified": "2015-07-20T13:11:56-05:00",
           "modifiedBy": 1,
           "modifiedByUser": "Joe Smith",
           "name": "VIP Customers",
           "alias": "vip-customers",
           "description": "High-value customers",
           "publicName": "VIP List",
           "filters": [
               {
                   "glue": "and",
                   "field": "points",
                   "object": "lead",
                   "type": "number",
                   "operator": "gte",
                   "properties": {
                       "filter": "100"
                   }
               }
           ],
           "isGlobal": true,
           "isPreferenceCenter": false,
           "category": {
               "id": 1,
               "title": "Customer Segments",
               "alias": "customer-segments",
               "color": "4e5d9d",
               "bundle": "lead"
           }
       }
   }

Segment properties
------------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Segment
   * - ``isPublished``
     - boolean
     - ``true`` if the Segment is published
   * - ``dateAdded``
     - ``datetime``
     - Date/time Segment was created
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
   * - ``name``
     - string
     - Name of the Segment
   * - ``alias``
     - string
     - Alias of the Segment used for searches and URLs
   * - ``description``
     - string/null
     - Description of the Segment
   * - ``publicName``
     - string/null
     - Public name of the Segment (displayed to contacts)
   * - ``filters``
     - array
     - Array of filter criteria that define the Segment
   * - ``isGlobal``
     - boolean
     - ``true`` if the Segment is global (visible to all users)
   * - ``isPreferenceCenter``
     - boolean
     - ``true`` if the Segment can be used in preference centers
   * - ``category``
     - object/null
     - Category object that contains the Segment

.. vale off

List Segments
*************

.. vale on

.. code-block:: php

   <?php

   //...
   $segments = $segmentApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

Get a list of Segments.

.. vale off

HTTP request
============

.. vale on

``GET /segments``

Query parameters
----------------

.. list-table::
   :widths: 20 80
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
     - Column to sort by. Can use any column listed in the response. However, you need to change all properties in the response written in ``camelCase`` a bit. Before every capital, add an underscore ``_`` and then change the capital letters to non-capital letters. So ``dateAdded`` becomes ``date_added``, ``modifiedByUser`` becomes ``modified_by_user``, etc.
   * - ``orderByDir``
     - Sort direction: ``asc`` or ``desc``.
   * - ``publishedOnly``
     - Only return currently published entities.
   * - ``minimal``
     - Return only array of entities without additional lists in it.
   * - ``where``
     - An array of advanced where conditions
   * - ``order``
     - An array of advanced order statements

Response
========

``Expected Response Code: 200``

.. code-block:: json

   {
       "total": 1,
       "lists": {
           "1": {
               "id": 1,
               "isPublished": true,
               "dateAdded": "2015-07-15T15:06:02-05:00",
               "createdBy": 1,
               "createdByUser": "Joe Smith",
               "dateModified": "2015-07-20T13:11:56-05:00",
               "modifiedBy": 1,
               "modifiedByUser": "Joe Smith",
               "name": "VIP Customers",
               "alias": "vip-customers",
               "description": "High-value customers",
               "publicName": "VIP List",
               "filters": [
                   {
                       "glue": "and",
                       "field": "points",
                       "object": "lead",
                       "type": "number",
                       "operator": "gte",
                       "properties": {
                           "filter": "100"
                       }
                   }
               ],
               "isGlobal": true,
               "isPreferenceCenter": false,
               "category": {
                   "id": 1,
                   "title": "Customer Segments",
                   "alias": "customer-segments",
                   "color": "4e5d9d",
                   "bundle": "lead"
               }
           }
       }
   }

Properties
----------

Same as :ref:`rest_api/segments:Get Segment`.

.. vale off

Create Segment
**************

.. vale on

.. code-block:: php

   <?php

   $data = array(
       'name' => 'VIP Customers',
       'alias' => 'vip-customers',
       'description' => 'High-value customers',
       'isPublished' => true,
       'isGlobal' => true,
       'filters' => array(
           array(
               'glue' => 'and',
               'field' => 'points',
               'object' => 'lead',
               'type' => 'number',
               'operator' => 'gte',
               'properties' => array(
                   'filter' => '100'
               )
           )
       )
   );

   $segment = $segmentApi->create($data);

Create a new Segment.

.. vale off

HTTP request
============

.. vale on

``POST /segments/new``

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
     - Segment name (required)
   * - ``alias``
     - string
     - Segment alias used for URLs and searches
   * - ``description``
     - string
     - Segment description
   * - ``publicName``
     - string
     - Public name displayed to contacts
   * - ``isPublished``
     - boolean
     - Whether the Segment is published (defaults to ``false``)
   * - ``isGlobal``
     - boolean
     - Whether the Segment is global (defaults to ``true``)
   * - ``isPreferenceCenter``
     - boolean
     - Whether the Segment can be used in preference centers (defaults to ``false``)
   * - ``filters``
     - array
     - Array of filter criteria that define the Segment
   * - ``category``
     - int
     - ID of the Category to assign to the Segment

Response
========

``Expected Response Code: 201``

Properties
----------

Same as :ref:`rest_api/segments:Get Segment`.

.. vale off

Edit Segment
************

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'name' => 'Updated VIP Customers',
       'description' => 'Updated high-value customers segment',
   );

   // Create new a Segment of ID 1 isn't found?
   $createIfNotFound = true;

   $segment = $segmentApi->edit($id, $data, $createIfNotFound);

Edit an existing Segment. Note that this supports PUT or PATCH depending on the desired behavior.

**PUT** creates a Segment if the given ID doesn't exist and clears all the Segment information, adds the information from the request.
**PATCH** fails if the Segment with the given ID doesn't exist and updates the Segment field values with the values from the request.

.. vale off

HTTP request
============

.. vale on

To edit a Segment and return a 404 if the Segment isn't found:

``PATCH /segments/ID/edit``

To edit a Segment and create a new one if the Segment isn't found:

``PUT /segments/ID/edit``

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
     - Segment name
   * - ``alias``
     - string
     - Segment alias used for URLs and searches
   * - ``description``
     - string
     - Segment description
   * - ``publicName``
     - string
     - Public name displayed to contacts
   * - ``isPublished``
     - boolean
     - Whether the Segment is published
   * - ``isGlobal``
     - boolean
     - Whether the Segment is global
   * - ``isPreferenceCenter``
     - boolean
     - Whether the Segment can be used in preference centers
   * - ``filters``
     - array
     - Array of filter criteria that define the Segment
   * - ``category``
     - int
     - ID of the Category to assign to the Segment

Response
========

If ``PUT``, the expected response code is ``200`` if the Segment was edited or ``201`` if created.
If ``PATCH``, the expected response code is ``200``.

Properties
----------

Same as :ref:`rest_api/segments:Get Segment`.

.. vale off

Delete Segment
**************

.. vale on

.. code-block:: php

   <?php

   $segment = $segmentApi->delete($id);

Delete a Segment.

.. vale off

HTTP request
============

.. vale on

``DELETE /segments/ID/delete``

Response
========

``Expected Response Code: 200``

Properties
----------

Same as :ref:`rest_api/segments:Get Segment`.

.. vale off

Add Contact to Segment
**********************

.. vale on

.. code-block:: php

   <?php

   $segmentApi->addContact($segmentId, $contactId);

Add a Contact to a Segment.

.. vale off

HTTP request
============

.. vale on

``POST /segments/SEGMENT_ID/contact/CONTACT_ID/add``

Response
========

``Expected Response Code: 200``

.. code-block:: json

   {
       "success": 1
   }

.. vale off

Add Contacts to Segment
***********************

.. vale on

.. code-block:: php

   <?php

   $contactIds = array(1, 2, 3);
   $segmentApi->addContacts($segmentId, $contactIds);

Add multiple Contacts to a Segment.

.. vale off

HTTP request
============

.. vale on

``POST /segments/SEGMENT_ID/contacts/add``

POST parameters
---------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``ids``
     - array
     - Array of Contact IDs to add to the Segment

Response
========

``Expected Response Code: 200``

.. code-block:: json

   {
       "success": 1,
       "details": {
           "1": {
               "success": true
           },
           "2": {
               "success": true
           },
           "3": {
               "success": false
           }
       }
   }

.. vale off

Remove Contact from Segment
***************************

.. vale on

.. code-block:: php

   <?php

   $segmentApi->removeContact($segmentId, $contactId);

Remove a Contact from a Segment.

.. vale off

HTTP request
============

.. vale on

``POST /segments/SEGMENT_ID/contact/CONTACT_ID/remove``

Response
========

``Expected Response Code: 200``

.. code-block:: json

   {
       "success": 1
   }

.. vale off

Get User Segments
*****************

.. vale on

.. code-block:: php

   <?php

   $segments = $segmentApi->getUserSegments();

Get a list of Segments available to the current user.

.. vale off

HTTP request
============

.. vale on

``GET /contacts/list/segments``

Response
========

``Expected Response Code: 200``

.. code-block:: json

   {
       "1": {
           "id": 1,
           "name": "VIP Customers",
           "alias": "vip-customers"
       },
       "2": {
           "id": 2,
           "name": "Newsletter Subscribers",
           "alias": "newsletter-subscribers"
       }
   }

Segment properties
------------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Segment
   * - ``name``
     - string
     - Name of the Segment
   * - ``alias``
     - string
     - Alias of the Segment

.. vale off

Segment Filters
***************

.. vale on

Segments use filters to define which Contacts should be included. Filters support various field types and operators.

Filter structure
================

.. code-block:: json

   {
       "glue": "and",
       "field": "email",
       "object": "lead",
       "type": "email",
       "operator": "like",
       "properties": {
           "filter": "%@gmail.com"
       }
   }

Filter properties
-----------------

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``glue``
     - string
     - Logic operator to connect with previous filter: ``and`` or ``or``
   * - ``field``
     - string
     - Contact field to filter on, for example ``email``, ``firstname``, ``points``
   * - ``object``
     - string
     - Object type, typically ``lead`` for Contact fields
   * - ``type``
     - string
     - Field type, for example ``text``, ``number``, ``email``, ``date``, ``select``
   * - ``operator``
     - string
     - Comparison operator, for example ``=``, ``!=``, ``like``, ``!like``, ``gt``, ``gte``, ``lt``, ``lte``, ``in``, ``!in``
   * - ``properties``
     - object
     - Additional filter properties including the ``filter`` value

Common operators by field type
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Text fields:**

* ``=`` (equals)
* ``!=`` (not equals)  
* ``like`` (contains)
* ``!like`` (does not contain)
* ``empty`` (is empty)
* ``!empty`` (is not empty)

**Number fields:**

* ``=`` (equals)
* ``!=`` (not equals)
* ``gt`` (greater than)
* ``gte`` (greater than or equal)
* ``lt`` (less than)
* ``lte`` (less than or equal)

**Date fields:**

* ``=`` (equals)
* ``!=`` (not equals)
* ``gt`` (after)
* ``gte`` (on or after)
* ``lt`` (before)
* ``lte`` (on or before)

**Select or multi-select fields:**

* ``=`` (equals)
* ``!=`` (not equals)
* ``in`` (in list)
* ``!in`` (not in list)

Example filters
~~~~~~~~~~~~~~~

**Email domain filter:**

.. code-block:: json

   {
       "glue": "and",
       "field": "email",
       "object": "lead",
       "type": "email",
       "operator": "like",
       "properties": {
           "filter": "%@company.com"
       }
   }

**Points range filter:**

.. code-block:: json

   {
       "glue": "and",
       "field": "points",
       "object": "lead", 
       "type": "number",
       "operator": "gte",
       "properties": {
           "filter": "100"
       }
   }

**Date range filter:**

.. code-block:: json

   {
       "glue": "and",
       "field": "date_added",
       "object": "lead",
       "type": "datetime",
       "operator": "gte",
       "properties": {
           "filter": "2023-01-01 00:00:00"
       }
   }
