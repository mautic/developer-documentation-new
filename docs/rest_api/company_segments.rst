Company Segments
################

Use this endpoint to manipulate and obtain details on Mautic's Company Segments, which enable Account-Based Marketing (ABM).

.. vale off

Get Company Segment
*******************

.. vale on

Retrieves an individual Company Segment.

.. vale off

HTTP request
============

.. vale on

``GET /companysegments/ID``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Company Segment.

.. _get Company Segment response:

.. code-block:: json

   {
      "companysegment": {
          "isPublished": true,
          "dateAdded": "2026-04-09T12:00:00+00:00",
          "dateModified": "2026-04-09T12:30:00+00:00",
          "createdBy": 1,
          "createdByUser": "Admin Mautic",
          "modifiedBy": 1,
          "modifiedByUser": "Admin Mautic",
          "id": 1,
          "name": "Enterprise Accounts",
          "publicName": "Enterprise Accounts",
          "alias": "enterprise-accounts",
          "description": "Companies with over 500 employees",
          "category": null,
          "filters": [
              {
                  "glue": "and",
                  "field": "companynumber_of_employees",
                  "object": "company",
                  "type": "number",
                  "operator": "gte",
                  "properties": {
                      "filter": "500"
                  }
              }
          ]
      }
   }

.. _get Company Segment properties:

Company Segment properties
--------------------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``isPublished``
     - boolean
     - Company Segment publication status
   * - ``dateAdded``
     - datetime
     - Company Segment record creation date and time
   * - ``dateModified``
     - datetime
     - Company Segment record last modification date and time
   * - ``createdBy``
     - integer
     - ID of the User who created the Company Segment
   * - ``createdByUser``
     - string
     - Name of the User who created the Company Segment
   * - ``modifiedBy``
     - integer
     - ID of the User who last modified the Company Segment
   * - ``modifiedByUser``
     - string
     - Name of the User who last modified the Company Segment
   * - ``id``
     - integer
     - ID of the Company Segment
   * - ``name``
     - string
     - Company Segment name
   * - ``publicName``
     - string
     - Public name of the Company Segment
   * - ``alias``
     - string
     - The auto-generated alias or slug of the Company Segment
   * - ``description``
     - string
     - Description of the Company Segment
   * - ``category``
     - object
     - The Category assigned to the Company Segment
   * - ``filters``
     - array
     - Array of filter criteria that define which Companies belong to the Segment

.. vale off

List Company Segments
*********************

.. vale on

Retrieves a list of Company Segments.

.. vale off

HTTP request
============

.. vale on

``GET /companysegments``

Query parameters
----------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``search``
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

* Returns ``200 OK`` when the request successfully retrieves the Company Segments list.

.. code-block:: json

   {
      "total": 2,
      "companysegments": [
          {
              "isPublished": true,
              "dateAdded": "2026-04-09T12:00:00+00:00",
              "dateModified": "2026-04-09T12:30:00+00:00",
              "createdBy": 1,
              "createdByUser": "Admin Mautic",
              "modifiedBy": 1,
              "modifiedByUser": "Admin Mautic",
              "id": 1,
              "name": "Enterprise Accounts",
              "publicName": "Enterprise Accounts",
              "alias": "enterprise-accounts",
              "description": "Companies with over 500 employees",
              "category": null,
              "filters": [
                  {
                      "glue": "and",
                      "field": "companynumber_of_employees",
                      "object": "company",
                      "type": "number",
                      "operator": "gte",
                      "properties": {
                          "filter": "500"
                      }
                  }
              ]
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
     - Total count of Company Segments
   * - ``companysegments``
     - array
     - Array of Company Segment objects

.. vale off

For the rest of the properties, refer to :ref:`Company Segment properties <get Company Segment properties>`.

.. vale on

.. vale off

Create Company Segment
**********************

.. vale on

Creates a new Company Segment.

.. vale off

HTTP request
============

.. vale on

``POST /companysegments/new``

.. _create Company Segment POST parameters:

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

       Company Segment name
   * - ``publicName``
     - string
     - Public name of the Company Segment
   * - ``alias``
     - string
     - The auto-generated alias or slug of the Company Segment. Must be unique across Company Segments.
   * - ``description``
     - string
     - Description of the Company Segment
   * - ``isPublished``
     - boolean
     - Company Segment publication status
   * - ``category``
     - integer
     - The Category ID to assign to the Company Segment
   * - ``filters``
     - array
     - Array of filter criteria that define which Companies belong to the Segment

Response
========

* Returns ``201 Created`` when the request successfully creates a Company Segment.

The response is the same as :ref:`Get Company Segment <get Company Segment response>`.

Properties
----------

Refer to :ref:`Company Segment properties <get Company Segment properties>`.

.. vale off

Edit Company Segment
********************

.. vale on

Edits a Company Segment.

This operation supports ``PUT`` or ``PATCH`` depending on the desired behavior:

* ``PUT``: **full replacement**. The request creates a new Company Segment if the ID is missing. If the ID exists, the request clears all existing data and replaces it with the provided values.
* ``PATCH``: **partial update**. The request only updates field values based on the request data. The request fails when the Company Segment ID doesn't exist.

.. vale off

HTTP request
============

.. vale on

* ``PUT /companysegments/ID/edit``: updates an existing Company Segment or creates a new one when the ID doesn't exist.
* ``PATCH /companysegments/ID/edit``: updates an existing Company Segment. The request fails when the ID doesn't exist.

POST parameters
---------------

Accepts the same parameters as those described in :ref:`Create Company Segment <create Company Segment POST parameters>`. All parameters are optional.

Response
========

* ``PUT``: returns ``200 OK`` when the request successfully updates the Company Segment or ``201 Created`` when the request creates a Company Segment.
* ``PATCH``: returns ``200 OK`` when the request successfully updates the Company Segment or ``404 Not Found`` error when the Company Segment ID doesn't exist.

The response is the same as :ref:`Get Company Segment <get Company Segment response>`.

Properties
----------

Refer to :ref:`Company Segment properties <get Company Segment properties>`.

.. vale off

Delete Company Segment
**********************

.. vale on

Deletes a Company Segment.

.. vale off

HTTP request
============

.. vale on

``DELETE /companysegments/ID/delete``

Response
========

* Returns ``200 OK`` when the request successfully deletes the Company Segment.
* Returns ``HTTP 409 (Conflict)`` when the Company Segment is referenced by other Segment filters. The response includes the names of the dependent Segments.

.. code-block:: json

   {
       "errors": [
           {
               "message": "This Company Segment is used by the following Segments: Enterprise Contacts, VIP Companies",
               "code": 409,
               "type": null
           }
       ]
   }

Remove the Company Segment from all dependent Segment filters before attempting deletion.

On success, the response is similar to :ref:`Get Company Segment <get Company Segment response>` but contains the deleted Company Segment data.

Properties
----------

Refer to :ref:`Company Segment properties <get Company Segment properties>`.

Batch operations
****************

The Company Segments API supports batch operations for creating, editing, and deleting multiple Company Segments in a single request.

.. vale off

Batch create
============

.. vale on

Creates multiple Company Segments in a single request.

.. vale off

HTTP request
------------

.. vale on

``POST /companysegments/batch/new``

Request body
------------

An array of Company Segment objects to create:

.. code-block:: json

   [
       {
           "name": "Enterprise Accounts",
           "alias": "enterprise-accounts",
           "isPublished": true
       },
       {
           "name": "SMB Accounts",
           "alias": "smb-accounts",
           "isPublished": true
       }
   ]

Response
--------

* Returns ``200 OK`` with the created Company Segments and individual status codes.

.. code-block:: json

   {
       "companysegments": [
           {
               "id": 1,
               "name": "Enterprise Accounts",
               "alias": "enterprise-accounts"
           },
           {
               "id": 2,
               "name": "SMB Accounts",
               "alias": "smb-accounts"
           }
       ],
       "statusCodes": {
           "0": 201,
           "1": 201
       }
   }

.. vale off

Batch edit
==========

.. vale on

Edits multiple Company Segments in a single request.

.. vale off

HTTP request
------------

.. vale on

``PATCH /companysegments/batch/edit``

Request body
------------

An array of Company Segment objects with their IDs:

.. code-block:: json

   [
       {
           "id": 1,
           "name": "Updated Enterprise Accounts"
       },
       {
           "id": 2,
           "isPublished": false
       }
   ]

Response
--------

* Returns ``200 OK`` with the updated Company Segments and individual status codes.

.. code-block:: json

   {
       "companysegments": [
           {
               "id": 1,
               "name": "Updated Enterprise Accounts"
           },
           {
               "id": 2,
               "isPublished": false
           }
       ],
       "statusCodes": {
           "0": 200,
           "1": 200
       }
   }

.. vale off

Batch delete
============

.. vale on

Deletes multiple Company Segments in a single request.

.. vale off

HTTP request
------------

.. vale on

``DELETE /companysegments/batch/delete``

Request body
------------

An array of Company Segment IDs to delete, or a JSON object with an ``ids`` property:

.. code-block:: json

   {
       "ids": [1, 2, 3]
   }

Response
--------

* Returns ``200 OK`` with the deleted Company Segments and individual status codes.
* Returns ``HTTP 409 (Conflict)`` for any Company Segment that is referenced by other Segment filters.

.. code-block:: json

   {
       "companysegments": [
           {
               "id": 1,
               "name": "Enterprise Accounts"
           }
       ],
       "statusCodes": {
           "0": 200,
           "1": 409
       },
       "errors": [
           {
               "message": "This Company Segment is used by the following Segments: Enterprise Contacts",
               "code": 409,
               "type": null
           }
       ]
   }

Company Segment filters
***********************

Company Segments use filters to define which Companies to include. Filters support various Company field types and operators.

Filter structure
================

.. code-block:: json

   {
        "object": "company",
        "glue": "and",
        "field": "companyindustry",
        "type": "select",
        "operator": "=",
        "properties": {
            "filter": "Technology"
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
     - Object type - ``company`` for Company Segment filters
   * - ``glue``
     - string
     - Connection between filters using ``and`` or ``or``
   * - ``field``
     - string
     - Company Field alias, such as ``companyname``, ``companyindustry``, ``companynumber_of_employees``, and so on
   * - ``type``
     - string
     - Data type for the field, such as ``text``, ``number``, ``select``, and so on
   * - ``operator``
     - string
     - Comparison logic for the filter, such as ``=``, ``!=``, ``gte``, ``lte``, and so on
   * - ``properties``
     - object
     - Object for the ``filter`` value and configurations

For a complete list of operators by field type, refer to :ref:`common operators` in the Segments documentation.

Filter examples
---------------

Industry filter
~~~~~~~~~~~~~~~

.. code-block:: json

   {
       "glue": "and",
       "field": "companyindustry",
       "object": "company",
       "type": "select",
       "operator": "=",
       "properties": {
           "filter": "Technology"
       }
   }

Employee count filter
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

   {
       "glue": "and",
       "field": "companynumber_of_employees",
       "object": "company",
       "type": "number",
       "operator": "gte",
       "properties": {
           "filter": "100"
       }
   }

Annual revenue filter
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

   {
       "glue": "and",
       "field": "companyannual_revenue",
       "object": "company",
       "type": "number",
       "operator": "gte",
       "properties": {
           "filter": "1000000"
       }
   }

Company Segment reference filter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can create Company Segments that reference other Company Segments. This filter includes Companies that belong to another Company Segment:

.. code-block:: json

   {
       "glue": "and",
       "field": "companysegment",
       "object": "company",
       "type": "companysegment",
       "operator": "in",
       "properties": {
           "filter": [1, 2]
       }
   }

.. note::

   You can't delete a Company Segment that is referenced by other Segment filters. The API returns an ``HTTP 409 (Conflict)`` response with the names of the dependent Segments.
