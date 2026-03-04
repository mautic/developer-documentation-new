Segments
########

Use this endpoint to manipulate and obtain details on Mautic's Segments.

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
   $segmentApi = $api->newApi("segments", $auth, $apiUrl);

.. vale off

Get Segment
***********

.. vale on

Retrieves an individual Segment.

.. code-block:: php

   <?php

   //...
   $segment = $segmentApi->get($id);

.. vale off

HTTP request
============

.. vale on

``GET /segments/ID``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Segment.

.. _get Segment response:

.. code-block:: json

   {
      "list": {
          "isPublished": true,
          "dateAdded": "2026-02-19T19:36:21+00:00",
          "dateModified": "2026-02-19T19:37:16+00:00",
          "createdBy": 1,
          "createdByUser": "Admin Mautic",
          "modifiedBy": 1,
          "modifiedByUser": "Admin Mautic",
          "id": 2,
          "name": "Acme Global Conference",
          "publicName": "Acme Global Conference",
          "alias": "acme-global-conference",
          "description": null,
          "category": null,
          "filters": [
              {
                  "glue": "and",
                  "field": "companyname",
                  "object": "company",
                  "type": "text",
                  "operator": "=",
                  "properties": {
                      "filter": "Beta Inc."
                  }
              }
          ],
          "isGlobal": true,
          "isPreferenceCenter": false
      }
   }

.. _get Segment properties:

Segment properties
------------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``isPublished``
     - boolean
     - Segment publication status
   * - ``dateAdded``
     - datetime
     - Segment record creation date and time
   * - ``dateModified``
     - datetime
     - Segment record last modification date and time
   * - ``createdBy``
     - integer
     - ID of the User who created the Segment
   * - ``createdByUser``
     - string
     - Name of the User who created the Segment
   * - ``modifiedBy``
     - integer
     - ID of the User who last modified the Segment
   * - ``modifiedByUser``
     - string
     - Name of the User who last modified the Segment
   * - ``id``
     - integer
     - ID of the Segment
   * - ``name``
     - string
     - Segment name
   * - ``publicName``
     - string
     - Public name of the Segment displayed to Contacts
   * - ``alias``
     - string
     - The auto-generated alias or slug of the Segment
   * - ``description``
     - string
     - Description of the Segment
   * - ``category``
     - object
     - The Category assigned to the Segment
   * - ``filters``
     - array
     - Array of filter criteria that define the Segment entities
   * - ``isGlobal``
     - boolean
     - Global visibility status - set to ``1`` or ``true`` to share the Segment with all Users. When not set, it defaults to restricted access
   * - ``isPreferenceCenter``
     - boolean
     - Preference center status - set to ``1`` or ``true`` to include the Segment in preference centers. When not set, it defaults to hidden

.. vale off

List Segments
*************

.. vale on

Retrieves a list of Segments.

.. code-block:: php

   <?php

   //...
   $segments = $segmentApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

HTTP request
============

.. vale on

``GET /segments``

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
       
       **Note**: convert ``camelCase`` properties to ``snake_case``. For example, ``dateAdded`` becomes ``date_added``, ``webhookUrl`` becomes ``webhook_url``, and so on
   * - ``orderByDir``
     - string
     - Order direction - ``asc`` or ``desc``
   * - ``publishedOnly``
     - boolean
     - Returns only currently published entities
   * - ``minimal``
     - boolean
     - Returns only a simple mapped object of entities without additional lists in it

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Segments list.

.. code-block:: json

   {
      "total": 2,
      "lists": {
          "2": {
              "isPublished": true,
              "dateAdded": "2026-02-19T19:36:21+00:00",
              "dateModified": "2026-02-19T19:37:16+00:00",
              "createdBy": 1,
              "createdByUser": "Admin Mautic",
              "modifiedBy": 1,
              "modifiedByUser": "Admin Mautic",
              "id": 2,
              "name": "Acme Global Conference",
              "publicName": "Acme Global Conference",
              "alias": "acme-global-conference",
              "description": null,
              "category": null,
              "filters": [
                  {
                      "glue": "and",
                      "field": "companyname",
                      "object": "company",
                      "type": "text",
                      "operator": "=",
                      "properties": {
                          "filter": "Beta Inc."
                      }
                  }
              ],
              "isGlobal": true,
              "isPreferenceCenter": false
          },
          // ...
      }
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
     - Total count of Segments
   * - ``lists``
     - object
     - A mapped collection of Segments indexed by their ID

.. vale off

For the rest of the properties, refer to :ref:`Segment properties <get Segment properties>`.

.. vale on

.. vale off

Create Segment
**************

.. vale on

Creates a new Segment.

.. code-block:: php

   <?php

    $data = array(
        'name'               => 'VIP Customers', // Required
        'alias'              => 'vip-customers',
        'description'        => 'High-value customers',
        'isPublished'        => true,
        'isGlobal'           => true,
        'filters'            => array(
            array(
                'glue'       => 'and',
                'field'      => 'points',
                'object'     => 'lead',
                'type'       => 'number',
                'operator'   => 'gte',
                'properties' => array(
                    'filter' => '100'
                )
            )
        )
    );

    $segment = $segmentApi->create($data);

.. vale off

HTTP request
============

.. vale on

``POST /segments/new``

.. _create Segment POST parameters:

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
     - **Required.**

       Segment name
   * - ``publicName``
     - string
     - Public name of the Segment displayed to Contacts
   * - ``alias``
     - string
     - The auto-generated alias or slug of the Segment
   * - ``description``
     - string
     - Description of the Segment
   * - ``isPublished``
     - boolean
     - Segment publication status
   * - ``category``
     - object
     - The Category assigned to the Segment
   * - ``filters``
     - array
     - Array of filter criteria that define the Segment entities
   * - ``isGlobal``
     - boolean
     - Global visibility status - set to ``1`` or ``true`` to share the Segment with all Users. When not set, it defaults to restricted access
   * - ``isPreferenceCenter``
     - boolean
     - Preference center status - set to ``1`` or ``true`` to include the Segment in preference centers. When not set, it defaults to hidden

Response
========

* Returns ``201 Created`` when the request successfully creates a Segment.

The response is the same as :ref:`Get Segment <get Segment response>`.

Properties
----------

Refer to :ref:`Segment properties <get Segment properties>`.

.. vale off

Edit Segment
************

.. vale on

Edits a Segment. 

This operation supports ``PUT`` or ``PATCH`` depending on the desired behavior:

* ``PUT``: **full replacement**. The request creates a new Segment if the ID is missing. If the ID exists, the request clears all existing data and replaces it with the provided values.
* ``PATCH``: **partial update**. The request only updates field values based on the request data. The request fails when the Segment ID doesn't exist.

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'name' => 'Updated VIP Customers',
       'description' => 'Updated high-value customers segment',
   );

   // Create a new Segment if ID 1 isn't found
   $createIfNotFound = true;

   $segment = $segmentApi->edit($id, $data, $createIfNotFound);

.. vale off

HTTP request
============

.. vale on

* ``PUT /segments/ID/edit``: updates an existing Segment or creates a new one when the ID doesn't exist.
* ``PATCH /segments/ID/edit``: updates an existing Segment. The request fails when the ID doesn't exist.

POST parameters
---------------

Accepts the same parameters as those described in :ref:`Create Segment <create Segment POST parameters>`. All parameters are optional.

Response
========

* ``PUT``: returns ``200 OK`` when the request successfully updates the Segment or ``201 Created`` when the request creates a Segment.
* ``PATCH``: returns ``200 OK`` when the request successfully updates the Segment or ``404 Not Found`` error when the Segment ID doesn't exist.

The response is the same as :ref:`Get Segment <get Segment response>`.

Properties
----------

Refer to :ref:`Segment properties <get Segment properties>`.

.. vale off

Delete Segment
**************

.. vale on

Deletes a Segment.

.. code-block:: php

   <?php

   $segment = $segmentApi->delete($id);

.. vale off

HTTP request
============

.. vale on

``DELETE /segments/ID/delete``

Response
========

* Returns ``200 OK`` when the request successfully deletes the Segment.

The response is similar to :ref:`Get Segment <get Segment response>` but contains the deleted Segment data.

Properties
----------

Refer to :ref:`Segment properties <get Segment properties>`.

.. vale off

Add Contact to Segment
**********************

.. vale on

Adds a Contact to a specific Segment.

.. code-block:: php

   <?php

   $segmentApi->addContact($segmentId, $contactId);

.. vale off

HTTP request
============

.. vale on

``POST /segments/SEGMENT_ID/contact/CONTACT_ID/add``

Response
========

* Returns ``200 OK`` when the request successfully adds the Contact to the Segment.

.. code-block:: json

   {
       "success": 1
   }

.. vale off

Add Contacts to Segment
***********************

.. vale on

Adds multiple Contacts to a specific Segment.

.. code-block:: php

   <?php

   $contactIds = array(1, 2, 3);
   $segmentApi->addContacts($segmentId, $contactIds);

.. vale off

HTTP request
============

.. vale on

``POST /segments/SEGMENT_ID/contacts/add``

Parameters
----------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``contactIds``
     - array
     - **Required.**

       Array of Contact IDs to add to the Segment

Response
========

* Returns ``200 OK`` when the request successfully adds the Contacts to the Segment.

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

Properties
----------

.. list-table::
   :widths: 30 20 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``success``
     - integer
     - Overall status of the request where ``1`` indicates completion
   * - ``details``
     - object
     - A mapped collection of processing results indexed by Contact ID
   * - ``details/{id}``
     - object
     - Result status for a specific Contact within the request
   * - ``details/{id}/success``
     - boolean
     - Individual confirmation of whether the Contact joined the Segment successfully

.. vale off

Remove Contact from Segment
***************************

.. vale on

Remove a Contact from a specific Segment.

.. code-block:: php

   <?php

   $segmentApi->removeContact($segmentId, $contactId);

.. vale off

HTTP request
============

.. vale on

``POST /segments/SEGMENT_ID/contact/CONTACT_ID/remove``

Response
========

* Returns ``200 OK`` when the request successfully removes the Contact from the Segment.

.. code-block:: json

   {
       "success": 1
   }

.. vale off

Get User Segments
*****************

.. vale on

Retrieves a list of Segments that are available to the current User.

.. code-block:: php

   <?php

   $segments = $segmentApi->getUserSegments();

.. vale off

HTTP request
============

.. vale on

``GET /contacts/list/segments``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Segments for the User.

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
   * - ``{id}``
     - object
     - Segment data indexed by the Segment ID
   * - ``{id}/id``
     - integer
     - ID of the Segment
   * - ``{id}/name``
     - string
     - Segment name
   * - ``{id}/alias``
     - string
     - The auto-generated alias or slug of the Segment

Segment filters
***************

Segments use filters to define which object type - ``lead``, ``company``, or ``behaviors`` - to include. Filters support various field types and operators.

Filter structure
================

.. code-block:: json

   {
        "object": "company",
        "glue": "and",
        "field": "companyname",
        "type": "text",
        "operator": "=",
        "properties": {
            "filter": "Beta Inc."
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
   * - ``object``
     - string
     - Object type - ``lead``, ``company``, or ``behaviors``
   * - ``glue``
     - string
     - Connection between filters using ``and`` or ``or``
   * - ``field``
     - string
     - Field or behavior action identifier, such as ``email``, ``points``, ``lead_email_received``, and so on
   * - ``type``
     - string
     - Data type for the field, such as ``text``, ``number``, ``date``, and so on
   * - ``operator``
     - string
     - Comparison logic for the filter, such as ``=``, ``!empty``, ``lte``, ``startsWith``, and so on.
     
       Refer to :ref:`common operators` for details
   * - ``properties``
     - object
     - Object for the ``filter`` value and configurations, including ``display``

.. _common operators:

Common operators by field type
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Text fields
^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Operator
     - Description
   * - ``=``
     - Exact match for the specified text
   * - ``!=``
     - Exclusion of the specified text
   * - ``like``
     - Presence of the string within the field
   * - ``!like``
     - Absence of the string within the field
   * - ``empty``
     - Identification of fields with no data
   * - ``!empty``
     - Identification of fields with any data

Number fields
^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Operator
     - Description
   * - ``=``
     - Value equal to the specified number
   * - ``!=``
     - Value not equal to the specified number
   * - ``gt``
     - Value greater than the specified number
   * - ``gte``
     - Value greater than or equal to the specified number
   * - ``lt``
     - Value less than the specified number
   * - ``lte``
     - Value less than or equal to the specified number

Date fields
^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Operator
     - Description
   * - ``=``
     - Match for the specific date
   * - ``!=``
     - Exclusion of the specific date
   * - ``gt``
     - Occurrence after the specified date
   * - ``gte``
     - Occurrence on or after the specified date
   * - ``lt``
     - Occurrence before the specified date
   * - ``lte``
     - Occurrence on or before the specified date

Select or multi-select fields
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Operator
     - Description
   * - ``=``
     - Selection matching the specified value
   * - ``!=``
     - Selection not matching the specified value
   * - ``in``
     - Match for any value within the provided list
   * - ``!in``
     - Exclusion of all values within the provided list

Filter examples
---------------

Email domain filter
~~~~~~~~~~~~~~~~~~~

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

Points filter
~~~~~~~~~~~~~

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

Date filter
~~~~~~~~~~~

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

Behavior action filter
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

   {
       "glue": "and",
       "field": "url_title",
       "object": "behaviors",
       "type": "text",
       "operator": "startsWith",
       "properties": {
           "filter": "acme"
       }
   }
