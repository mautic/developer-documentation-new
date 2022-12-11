
Categories
##########

Use this endpoint to obtain details on Mautic's Categories, or to manipulate Category memberships.

**Using Mautic's API Library**

You can interact with this API through the :xref:`Mautic API Library` as follows, or use the various http endpoints as described in this document.

.. code-block:: php

   <?php
   use Mautic\MauticApi;
   use Mautic\Auth\ApiAuth;

   // ...
   $initAuth    = new ApiAuth();
   $auth        = $initAuth->newAuth($settings);
   $apiUrl      = "https://example.com";
   $api         = new MauticApi();
   $categoryApi = $api->newApi("categories", $auth, $apiUrl);

.. vale off

Get Category
************

.. vale on

.. code-block:: php

   <?php

   //...
   $category = $categoryApi->get($id);

.. code-block:: json

   {  
     "category":{  
       "id":221,
       "title":"test",
       "alias":"test4",
       "description":null,
       "color":null,
       "bundle":"asset"
     }
   }

Get an individual Category by ID.

.. vale off

**HTTP Request**

.. vale on

``GET /categories/ID``

**Response**

``Expected Response Code: 200``

See JSON code example.

**Category properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Category
   * - ``isPublished``
     - boolean
     - Published status of the Category
   * - ``dateAdded``
     - ``datetime``
     - Category creation date/time
   * - ``createdBy``
     - int
     - ID of the User that created the Category
   * - ``createdByUser``
     - string
     - Name of the User that created the Category
   * - ``dateModified``
     - datetime/null
     - Category modified date/time
   * - ``modifiedBy``
     - int
     - ID of the User that last modified the Category
   * - ``modifiedByUser``
     - string
     - Name of the User that last modified the Category
   * - ``title``
     - string
     - The Category title
   * - ``alias``
     - string
     - The Category alias
   * - ``description``
     - string
     - The Category description
   * - ``color``
     - string
     - The Category color
   * - ``bundle``
     - string
     - The bundle where the Category is available

.. vale off

List Contact Categories
***********************

.. vale on

.. code-block:: php

   <?php

   //...
   $categories = $categoryApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

Returns a list of Contact Categories available to the User. This list isn't filterable.

.. vale off

**HTTP Request**

.. vale on

``GET /categories``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {  
     "total":8,
     "categories":[  
       {  
         "id":1,
         "title":"Bold",
         "alias":"bold",
         "description":null,
         "color":"b36262",
         "bundle":"point"
       },
     ]
   }

**Category properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Category
   * - ``isPublished``
     - boolean
     - Published status of the Category
   * - ``dateAdded``
     - ``datetime``
     - Category creation date/time
   * - ``createdBy``
     - int
     - ID of the User that created the Category
   * - ``createdByUser``
     - string
     - Name of the User that created the Category
   * - ``dateModified``
     - datetime/null
     - Category modified date/time
   * - ``modifiedBy``
     - int
     - ID of the User that last modified the Category
   * - ``modifiedByUser``
     - string
     - Name of the User that last modified the Category
   * - ``title``
     - string
     - The Category title
   * - ``alias``
     - string
     - The Category alias
   * - ``description``
     - string
     - The Category description
   * - ``color``
     - string
     - The Category color
   * - ``bundle``
     - string
     - The bundle where the Category is available

.. vale off

Create Category
***************

.. vale on

.. code-block:: php

   <?php 

   $data = array(
       'categoryname' => 'test',
       'categoryemail' => 'test@example.com',
       'categorycity' => 'Raleigh',
   );

   $category = $categoryApi->create($data);

Create a new Category.

.. vale off

**HTTP Request**

.. vale on

``POST /categories/new``

**POST parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``title``
     - string
     - The Category title
   * - ``bundle``
     - string
     - The bundle where the Category is available


**Response**

``Expected Response Code: 201``

**Properties**

Same as `Get Category <#get-category>`_.

.. vale off

Edit Category
*************

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'title' => 'test',
       'bundle' => 'asset'
   );

   // Create new a Category if ID 1 isn't found?
   $createIfNotFound = true;

   $category = $categoryApi->edit($id, $data, $createIfNotFound);

Edit a new Category. Note that this supports PUT or PATCH depending on the desired behavior.

**PUT** creates a Category if the given ID doesn't exist and clears all the Category information, adds the information from the request.
**PATCH** fails if the Category with the given ID doesn't exist and updates the Category field values with the values from the request.

.. vale off

**HTTP Request**

.. vale on

To edit a Category and return a 404 if the Category isn't found:

``PATCH /categories/ID/edit``

To edit a Category and create a new one if the Category isn't found:

``PUT /categories/ID/edit``

**POST parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - title
     - string
     - The Category title
   * - bundle
     - string
     - The bundle where the Category is available


**Response**

If using ``PUT``, the expected response code is ``200`` if editing the Category or ``201`` if creating the Category.

If ``PATCH``, the expected response code is ``200``.

**Properties**

Same as `Get Category <#get-category>`_.

.. vale off

Delete Category
***************

.. vale on

.. code-block:: php

   <?php

   $category = $categoryApi->delete($id);

Delete a Category.

.. vale off

**HTTP Request**

.. vale on

``DELETE /categories/ID/delete``

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get Category <#get-category>`_.

.. vale off

Assign a Category
*****************

.. vale on

To assign a Category to an entity, set ``category = [ID]`` to the payload. For example, this is how you can assign Category 123 to a new Asset:

.. code-block:: php

   $data = array(
       'title' => 'PDF sent as a API request',
       'storageLocation' => 'remote',
       'file' => 'https://www.mautic.org/media/logos/logo/Mautic_Logo_DB.pdf'
       'category' => 123
   );

   $asset = $assetApi->create($data);

The Category must exist in the Mautic instance, and the entity must support Categories.
