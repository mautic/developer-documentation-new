Tags
####

Use this endpoint to obtain details on Mautic's Tags.

**Using Mautic's API Library**

You can interact with this API through the :xref:`Mautic API Library` as follows, or use the various http endpoints as described in this document.

.. code-block:: php

   <?php
   use Mautic\MauticApi;
   use Mautic\Auth\ApiAuth;

   // ...
   $initAuth        = new ApiAuth();
   $auth            = $initAuth->newAuth($settings);
   $apiUrl          = "https://mautic.example.com";
   $api             = new MauticApi();
   $tagApi = $api->newApi("tags", $auth, $apiUrl);

.. vale off

Get Tag
*******

.. vale on

.. code-block:: php

   <?php

   //...
   $tag = $tagApi->get($id);

Get an individual Tag by ID.

.. vale off

**HTTP Request**

.. vale on

``GET /tags/ID``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {  
       "tag": {
           "id": 34,
           "tag": "tagA",
       }
   }

**Tag Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Tag
   * - `tag`
     - string
     - Title of the Tag

.. vale off

List Tags
*********

.. vale on

.. code-block:: php

   <?php
   // ...

   $tags = $tagApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

**HTTP Request**

.. vale on

``GET /tags``

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
       "total":1,
       "tags":[  
           {
               "id": 34,
               "tag": "tagA",
           }
       ]
   }

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
   );

   $tag = $tagApi->create($data);

Create a new Tag.

.. vale off

**HTTP Request**

.. vale on

``POST /tags/new``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Tag
   * - ``tag``
     - string
     - Title of the Tag


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
   );

   // Create new a Tag if ID 1 isn't found?
   $createIfNotFound = true;

   $tag = $tagApi->edit($id, $data, $createIfNotFound);

Edit a new Tag. Note that this supports PUT or PATCH depending on the desired behavior.

**PUT** creates a Tag if the given ID doesn't exist and clears all the Tag information, adds the information from the request.

**PATCH** fails if the Tag with the given ID doesn't exist and updates the Tag field values with the values from the request.

.. vale off

**HTTP Request**

.. vale on

To edit a Tag and return a 404 if the Tag isn't found:

``PATCH /tags/ID/edit``

To edit a Tag and create a new one if the Tag isn't found:

``PUT /tags/ID/edit``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Tag
   * - ``tag``
     - string
     - Title of the Tag


**Response**

If ``PUT``, the expected response code is ``200`` if editing a Tag or ``201`` if creating a new one.

If ``PATCH``, the expected response code is ``200``.

**Properties**

Same as `Get Tag <#get-tag>`_.

.. vale off

Delete Tag
**********

.. vale on

.. code-block:: php

   <?php

   $tag = $tagApi->delete($id);

Delete a Tag.

.. vale off

**HTTP Request**

.. vale on

``DELETE /tags/ID/delete``

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get Tag <#get-tag>`_.
