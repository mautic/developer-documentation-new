Tags
####

Use this endpoint to work with Mautic's Tags.

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
   $initAuth = new ApiAuth();
   $auth     = $initAuth->newAuth($settings);
   $apiUrl   = "https://example.com";
   $api      = new MauticApi();
   $tagApi   = $api->newApi("tags", $auth, $apiUrl);

.. vale off

Get Tag
*******

.. vale on

Retrieves an individual Tag.

.. code-block:: php

   <?php

   //...
   $tag = $tagApi->get($id);

.. vale off

HTTP request
============

.. vale on

``GET /tags/ID``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Tag.

.. _get Tag response:

.. code-block:: json

   {
       "tag": {
           "id": 34,
           "tag": "tagA",
           "description": "A tag for grouping contacts"
       }
   }

.. _get Tag properties:

Tag properties
--------------

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Tag
   * - ``tag``
     - string
     - Title of the Tag
   * - ``description``
     - string/null
     - Description of the Tag

.. vale off

List Tags
*********

.. vale on

Retrieves a list of Tags.

.. code-block:: php

   <?php

   //...
   $tags = $tagApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

HTTP request
============

.. vale on

``GET /tags``

Query parameters
----------------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Name
     - Description
   * - ``search``
     - String or search command to filter entities
   * - ``start``
     - Starting row for the returned entities - defaults to 0
   * - ``limit``
     - Maximum number of entities to return - defaults to 30
   * - ``orderBy``
     - Column to sort by. Any column in the response is valid.
   * - ``orderByDir``
     - Order direction - ``asc`` or ``desc``
   * - ``publishedOnly``
     - Returns only currently published entities
   * - ``minimal``
     - Returns only a simple mapped object of entities without additional lists in it

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Tags list.

.. code-block:: json

   {
       "total": 1,
       "tags": [
           {
               "id": 34,
               "tag": "tagA",
               "description": "A tag for grouping contacts"
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
     - Total count of Tags
   * - ``tags``
     - array
     - A mapped collection of Tags indexed by their ID

For the rest of the properties, refer to :ref:`Tag properties <get Tag properties>`.

.. vale off

Create Tag
**********

.. vale on

Creates a new Tag.

.. code-block:: php

   <?php

   $data = [
       'tag' => 'Tag A',
       'description' => 'Description of Tag A',
   ];

   $tag = $tagApi->create($data);

.. vale off

HTTP request
============

.. vale on

``POST /tags/new``

.. _create Tag POST parameters:

POST parameters
---------------

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Name
     - Type
     - Description
   * - ``tag``
     - string
     - **Required.**

       Title of the Tag
   * - ``description``
     - string
     - Description of the Tag

Response
========

* Returns ``201 Created`` when the request successfully creates a Tag.

Properties
----------

Refer to :ref:`Tag properties <get Tag properties>`.

.. vale off

Edit Tag
********

.. vale on

Edits a Tag.

This operation supports ``PUT`` or ``PATCH`` depending on the desired behavior:

* ``PUT``: **full replacement**. The request creates a new Tag if the ID doesn't exist. If the ID exists, the request clears all existing data and replaces it with the provided values.
* ``PATCH``: **partial update**. The request only updates field values based on the request data. The request fails when the Tag ID doesn't exist.

.. code-block:: php

   <?php

   $id   = 1;
   $data = [
       'tag' => 'Tag B',
       'description' => 'Updated description',
   ];

   // Create new Tag if ID 1 isn't found?
   $createIfNotFound = true;

   $tag = $tagApi->edit($id, $data, $createIfNotFound);

.. vale off

HTTP request
============

.. vale on

To edit a Tag and return a 404 if the Tag isn't found:

``PATCH /tags/ID/edit``

To edit a Tag and create a new one if the Tag isn't found:

``PUT /tags/ID/edit``

POST parameters
---------------

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Name
     - Type
     - Description
   * - ``tag``
     - string
     - Title of the Tag
   * - ``description``
     - string
     - Description of the Tag

Response
========

If using ``PUT``, the expected response code is ``200`` if editing the Tag or ``201`` if creating the Tag.

If using ``PATCH``, the expected response code is ``200``.

Properties
----------

Refer to :ref:`Tag properties <get Tag properties>`.

.. vale off

Delete Tag
**********

.. vale on

Deletes a Tag.

.. code-block:: php

   <?php

   $tag = $tagApi->delete($id);

.. vale off

HTTP request
============

.. vale on

``DELETE /tags/ID/delete``

Response
========

* Returns ``200 OK`` when the request successfully deletes the Tag.

Properties
----------

Refer to :ref:`Tag properties <get Tag properties>`.
