Dynamic Content
###############

Use this endpoint to obtain details on Mautic's Dynamic Content.

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
   $initAuth          = new ApiAuth();
   $auth              = $initAuth->newAuth($settings);
   $apiUrl            = "https://example.com";
   $api               = new MauticApi();
   $dynamicContentApi = $api->newApi("dynamicContents", $auth, $apiUrl);

.. vale off

Get Dynamic Content
*******************

.. vale on

Retrieves an individual Dynamic Content item.

.. code-block:: php

   <?php

   //...
   $dynamicContent = $dynamicContentApi->get($id);

.. vale off

HTTP request
============

.. vale on

``GET /dynamiccontents/ID``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Dynamic Content item.

.. _get Dynamic Content response:

.. code-block:: json

   {
      "dynamicContent": {
          "isPublished": true,
          "dateAdded": "2026-06-20T11:26:51+00:00",
          "createdBy": 1,
          "createdByUser": "John Doe",
          "dateModified": "2026-08-08T16:36:27+00:00",
          "modifiedBy": 1,
          "modifiedByUser": "John Doe",
          "id": 1,
          "name": "DC13",
          "category": null,
          "publishUp": null,
          "publishDown": null,
          "sentCount": 0,
          "variantParent": null,
          "variantChildren": []
      }
   }

.. _get Dynamic Content properties:

Dynamic Content properties
--------------------------

.. vale off

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - integer
     - ID of the Dynamic Content item
   * - ``name``
     - string
     - Name of the Dynamic Content item
   * - ``description``
     - string
     - Description of the Dynamic Content item
   * - ``isPublished``
     - boolean
     - Dynamic Content publication status
   * - ``publishUp``
     - datetime
     - Activation date and time for the Dynamic Content item
   * - ``publishDown``
     - datetime
     - Deactivation date and time for the Dynamic Content item
   * - ``dateAdded``
     - datetime
     - Dynamic Content record creation date and time
   * - ``createdBy``
     - integer
     - ID of the User who created the Dynamic Content item
   * - ``createdByUser``
     - string
     - Name of the User who created the Dynamic Content item
   * - ``dateModified``
     - datetime
     - Dynamic Content record last modification date and time
   * - ``modifiedBy``
     - integer
     - ID of the User who last modified the Dynamic Content item
   * - ``modifiedByUser``
     - string
     - Name of the User who last modified the Dynamic Content item
   * - ``category``
     - object
     - The Category for the Dynamic Content item
   * - ``variantParent``
     - object
     - The parent Dynamic Content item when this item is a variant in an A/B test
   * - ``variantChildren``
     - array
     - Array of Dynamic Content variants of this item
   * - ``sentCount``
     - integer
     - Number of times the system sent the Dynamic Content item

.. vale on

.. vale off

List Dynamic Contents
*********************

.. vale on

Retrieves a list of Dynamic Content items.

.. code-block:: php

   <?php
   // ...

   $dynamicContents = $dynamicContentApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

HTTP request
============

.. vale on

``GET /dynamiccontents``

Query parameters
----------------

.. list-table::
   :widths: 20 20 60
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
     - Maximum number of entities to return - defaults to the system pagination configuration, which is 30
   * - ``orderBy``
     - string
     - Column to sort by. Any column in the response is valid.

       **Note**: convert ``camelCase`` properties to ``snake_case``. For example, ``dateAdded`` becomes ``date_added``, and so on
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

* Returns ``200 OK`` when the request successfully retrieves the Dynamic Content list.

.. code-block:: json

   {
      "total": 30,
      "dynamicContents": [
          {
              "isPublished": true,
              "dateAdded": "2026-06-20T11:27:09+00:00",
              "createdBy": 1,
              "createdByUser": "John Doe",
              "dateModified": "2026-08-22T17:14:01+00:00",
              "modifiedBy": 1,
              "modifiedByUser": "John Doe",
              "id": 2,
              "name": "CD2",
              "category": null,
              "publishUp": null,
              "publishDown": null,
              "sentCount": 0,
              "variantParent": null,
              "variantChildren": []
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
     - Total count of Dynamic Content items
   * - ``dynamicContents``
     - array
     - A collection of Dynamic Content items

.. vale off

For the rest of the properties, refer to :ref:`Dynamic Content properties <get Dynamic Content properties>`.

.. vale on

.. vale off

Create Dynamic Content
**********************

.. vale on

Creates a new Dynamic Content item.

.. code-block:: php

   <?php

   $data = array(
       'name'        => 'Dynamic Content A',
       'isPublished' => 1,
   );

   $dynamicContent = $dynamicContentApi->create($data);

.. vale off

HTTP request
============

.. vale on

``POST /dynamiccontents/new``

.. _create Dynamic Content POST parameters:

POST parameters
---------------

.. vale off

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``name``
     - string
     - **Required.**

       Name of the Dynamic Content item
   * - ``description``
     - string
     - Description of the Dynamic Content item
   * - ``isPublished``
     - boolean
     - Dynamic Content publication status
   * - ``publishUp``
     - datetime
     - Activation date and time for the Dynamic Content item
   * - ``publishDown``
     - datetime
     - Deactivation date and time for the Dynamic Content item

.. vale on

Response
========

* Returns ``201 Created`` when the request successfully creates a Dynamic Content item.

The response is a JSON object similar to :ref:`Get Dynamic Content <get Dynamic Content response>`.

Properties
----------

Refer to :ref:`Dynamic Content properties <get Dynamic Content properties>`.

.. vale off

Edit Dynamic Content
********************

.. vale on

Edits a Dynamic Content item.

This operation supports ``PUT`` or ``PATCH`` depending on the desired behavior:

* ``PUT``: **full replacement**. The request creates a new Dynamic Content item if the ID is missing. If the ID exists, the request clears all existing data and replaces it with the provided values.
* ``PATCH``: **partial update**. The request only updates field values based on the request data. The request fails when the Dynamic Content ID doesn't exist.

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'name'        => 'New Dynamic Content name',
       'isPublished' => 0,
   );

   // Create a new Dynamic Content item if ID 1 isn't found
   $createIfNotFound = true;

   $dynamicContent = $dynamicContentApi->edit($id, $data, $createIfNotFound);

.. vale off

HTTP request
============

.. vale on

* ``PUT /dynamiccontents/ID/edit``: updates an existing Dynamic Content item or creates a new one when the ID doesn't exist.
* ``PATCH /dynamiccontents/ID/edit``: updates an existing Dynamic Content item. The request fails when the ID doesn't exist.

POST parameters
---------------

Accepts the same parameters as those described in :ref:`Create Dynamic Content <create Dynamic Content POST parameters>`. All parameters are optional.

Response
========

* ``PUT``: returns ``200 OK`` when the request successfully updates the Dynamic Content item or ``201 Created`` when the request creates a Dynamic Content item.
* ``PATCH``: returns ``200 OK`` when the request successfully updates the Dynamic Content item or ``404 Not Found`` error when the Dynamic Content ID doesn't exist.

The response is a JSON object similar to :ref:`Get Dynamic Content <get Dynamic Content response>`.

Properties
----------

Refer to :ref:`Dynamic Content properties <get Dynamic Content properties>`.

.. vale off

Delete Dynamic Content
**********************

.. vale on

Deletes a Dynamic Content item.

.. code-block:: php

   <?php

   $dynamicContent = $dynamicContentApi->delete($id);

.. vale off

HTTP request
============

.. vale on

``DELETE /dynamiccontents/ID/delete``

Response
========

* Returns ``200 OK`` when the request successfully deletes the Dynamic Content item.

The response is a JSON object containing the data of the deleted Dynamic Content item, similar to :ref:`Get Dynamic Content <get Dynamic Content response>`.

Properties
----------

Refer to :ref:`Dynamic Content properties <get Dynamic Content properties>`.
