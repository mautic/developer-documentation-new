Tags
####

Use this endpoint to work with Mautic's Tags.

**Using Mautic's API Library**

You can interact with this API through the :xref:`Mautic API Library` as follows, or use the various HTTP endpoints as described in this document.

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

.. code-block:: php

   <?php

   //...
   $tag = $tagApi->get($id);

.. code-block:: json

   {
     "tag": {
       "id": 34,
       "tag": "tagA",
       "description": "A tag for grouping contacts"
     }
   }

Retrieves an individual Tag.

.. vale off

**HTTP Request**

.. vale on

``GET /tags/ID``

**Response**

``Expected Response Code: 200``

See JSON code example.

**Tag properties**

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

.. code-block:: php

   <?php

   //...
   $tags = $tagApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

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

Retrieves a list of Tags.

.. vale off

**HTTP Request**

.. vale on

``GET /tags``

**Query parameters**

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Name
     - Description
   * - ``search``
     - String or search command to filter entities by.
   * - ``start``
     - Starting row for the entities returned. Defaults to 0.
   * - ``limit``
     - Limit number of entities to return. Defaults to the system configuration for pagination, which is 30 by default.
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

See JSON code example.

**Properties**

Same as `Get Tag <#get-tag>`_.

.. vale off

Create Tag
**********

.. vale on

.. code-block:: php

   <?php

   $data = array(
       'tag' => 'Tag A',
       'description' => 'Description of Tag A',
   );

   $tag = $tagApi->create($data);

Creates a new Tag.

.. vale off

**HTTP Request**

.. vale on

``POST /tags/new``

**POST parameters**

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Name
     - Type
     - Description
   * - ``tag``
     - string
     - Title of the Tag. Required.
   * - ``description``
     - string
     - Description of the Tag

**Response**

``Expected Response Code: 201``

**Properties**

Same as `Get Tag <#get-tag>`_.

.. vale off

Edit Tag
********

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'tag' => 'Tag B',
       'description' => 'Updated description',
   );

   // Create new Tag if ID 1 isn't found?
   $createIfNotFound = true;

   $tag = $tagApi->edit($id, $data, $createIfNotFound);

Edits a Tag.

This operation supports ``PUT`` or ``PATCH`` depending on the desired behavior:

* ``PUT``: **full replacement**. The request creates a new Tag if the ID doesn't exist. If the ID exists, the request clears all existing data and replaces it with the provided values.
* ``PATCH``: **partial update**. The request only updates field values based on the request data. The request fails when the Tag ID doesn't exist.

.. vale off

**HTTP Request**

.. vale on

To edit a Tag and return a 404 if the Tag isn't found:

``PATCH /tags/ID/edit``

To edit a Tag and create a new one if the Tag isn't found:

``PUT /tags/ID/edit``

**POST parameters**

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

**Response**

If using ``PUT``, the expected response code is ``200`` if editing the Tag or ``201`` if creating the Tag.

If using ``PATCH``, the expected response code is ``200``.

**Properties**

Same as `Get Tag <#get-tag>`_.

.. vale off

Delete Tag
**********

.. vale on

.. code-block:: php

   <?php

   $tag = $tagApi->delete($id);

Deletes a Tag.

.. vale off

**HTTP Request**

.. vale on

``DELETE /tags/ID/delete``

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get Tag <#get-tag>`_.
