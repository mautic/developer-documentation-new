Dynamic Content
###############

Use this endpoint to obtain details on Mautic's web Dynamic Content.

**Using Mautic's API Library**

You can interact with this API through the :xref:`Mautic API Library` as follows, or use the various http endpoints as described in this document.

.. code-block:: php

   <?php
   use Mautic\MauticApi;
   use Mautic\Auth\ApiAuth;

   // ...
   $initAuth         = new ApiAuth();
   $auth             = $initAuth->newAuth($settings);
   $apiUrl           = "https://mautic.example.com";
   $api              = new MauticApi();
   $dynamicContentApi = $api->newApi("dynamicContents", $auth, $apiUrl);

.. vale off

Get Dynamic Content
*******************

.. vale on

.. code-block:: php

   <?php

   //...
   $dynamicContent = $dynamicContentApi->get($id);

Get an individual dynamicContent by ID.

.. vale off

**HTTP Request**

.. vale on

``GET /dynamiccontents/ID``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "dynamicContent":{
           "isPublished":true,
           "dateAdded":"2016-06-20T11:26:51+00:00",
           "createdBy":1,
           "createdByUser":"John Doe",
           "dateModified":"2016-08-08T16:36:27+00:00",
           "modifiedBy":1,
           "modifiedByUser":"John Doe",
           "id":1,
           "name":"DC13",
           "category":null,
           "publishUp":null,
           "publishDown":null,
           "sentCount":0,
           "variantParent":null,
           "variantChildren":[]
       }
   }

**Dynamic Content Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Dynamic Content
   * - ``name``
     - string
     - Name of the Dynamic Content
   * - ``description``
     - string/null
     - Description of the Dynamic Content
   * - ``isPublished``
     - boolean
     - Published state
   * - ``publishUp``
     - datetime/null
     - Dynamic Content publish date/time
   * - ``publishDown``
     - datetime/null
     - Dynamic Content unpublish date/time
   * - ``dateAdded``
     - ``datetime``
     - Dynamic Content creation date
   * - ``createdBy``
     - int
     - ID of the User that created the Dynamic Content
   * - ``createdByUser``
     - string
     - Name of the User that created the Dynamic Content
   * - ``dateModified``
     - datetime/null
     - Date/time Dynamic Content was last modified
   * - ``modifiedBy``
     - int
     - ID of the User that last modified the Dynamic Content
   * - ``modifiedByUser``
     - string
     - Name of the User that last modified the Dynamic Content
   * - ``variantChildren``
     - array
     - Array of Dynamic Content entities for variants of this landing Dynamic Content
   * - ``variantParent``
     - object
     - The parent/main Dynamic Content if this is a variant, also known as A/B test
   * - ``sentCount``
     - int
     - Count of how many times the Dynamic Content got sent

.. vale off

List Dynamic Contents
*********************

.. vale on

.. code-block:: php

   <?php
   // ...

   $dynamicContents = $dynamicContentApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

**HTTP Request**

.. vale on

``GET /dynamiccontents``

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
       "total":30,
       "dynamicContents":[
           {
               "isPublished":true,
               "dateAdded":"2016-06-20T11:27:09+00:00",
               "createdBy":1,
               "createdByUser":"John Doe",
               "dateModified":"2016-08-22T17:14:01+00:00",
               "modifiedBy":1,
               "modifiedByUser":"John Doe",
               "id":2,
               "name":"CD2",
               "category":null,
               "publishUp":null,
               "publishDown":null,
               "sentCount":0,
               "variantParent":null,
               "variantChildren":[]
           }
       ]
   }

**Properties**

Same as `Get Dynamic Content <#get-dynamic-content>`_.

.. vale off

Create Dynamic Content
**********************

.. vale on

.. code-block:: php

   <?php

   $data = array(
       'name'        => 'Dynamic Content A',
       'isPublished' => 1
   );

   $dynamicContent = $dynamicContentApi->create($data);

Create a new dynamicContent.

.. vale off

**HTTP Request**

.. vale on

``POST /dynamiccontents/new``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Dynamic Content
   * - ``name``
     - string
     - Name of the Dynamic Content
   * - ``description``
     - string/null
     - Description of the Dynamic Content
   * - ``isPublished``
     - boolean
     - Published state
   * - ``publishUp``
     - datetime/null
     - Dynamic Content publish date/time
   * - ``publishDown``
     - datetime/null
     - Dynamic Content unpublish date/time
   * - ``dateAdded``
     - ``datetime``
     - Dynamic Content creation date
   * - ``createdBy``
     - int
     - ID of the User that created the Dynamic Content
   * - ``createdByUser``
     - string
     - Name of the User that created the Dynamic Content
   * - ``dateModified``
     - datetime/null
     - Date/time Dynamic Content was last modified
   * - ``modifiedBy``
     - int
     - ID of the User that last modified the Dynamic Content
   * - ``modifiedByUser``
     - string
     - Name of the User that last modified the Dynamic Content
   * - ``variantChildren``
     - array
     - Array of Dynamic Content entities for variants of this landing Dynamic Content
   * - ``variantParent``
     - object
     - The parent/main Dynamic Content if this is a variant, also known as A/B test
   * - ``sentCount``
     - int
     - Count of how many times the Dynamic Content got sent

**Response**

``Expected Response Code: 201``

**Properties**

Same as `Get Dynamic Content <#get-dynamic-content>`_.

.. vale off

Edit Dynamic Content
********************

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'name'        => 'New dynamicContent name',
       'isPublished' => 0
   );

   // Create new a dynamicContent of ID 1 isn't found?
   $createIfNotFound = true;

   $dynamicContent = $dynamicContentApi->edit($id, $data, $createIfNotFound);

Edit a new dynamicContent. Note that this supports PUT or PATCH depending on the desired behavior.

**PUT** creates a dynamicContent if the given ID doesn't exist and clears all the Dynamic Content information, adds the information from the request.
**PATCH** fails if the Dynamic Content with the given ID doesn't exist and updates the Dynamic Content field values with the values from the request.

.. vale off

**HTTP Request**

.. vale on

To edit a dynamicContent and return a 404 if the Dynamic Content isn't found:

``PATCH /dynamiccontents/ID/edit``

To edit a dynamicContent and create a new one if the Dynamic Content isn't found:

``PUT /dynamiccontents/ID/edit``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Dynamic Content
   * - ``name``
     - string
     - Name of the Dynamic Content
   * - ``description``
     - string/null
     - Description of the Dynamic Content
   * - ``isPublished``
     - boolean
     - Published state
   * - ``publishUp``
     - datetime/null
     - Dynamic Content publish date/time
   * - ``publishDown``
     - datetime/null
     - Dynamic Content unpublish date/time
   * - ``dateAdded``
     - ``datetime``
     - Dynamic Content creation date
   * - ``createdBy``
     - int
     - ID of the User that created the Dynamic Content
   * - ``createdByUser``
     - string
     - Name of the User that created the Dynamic Content
   * - ``dateModified``
     - datetime/null
     - Date/time Dynamic Content was last modified
   * - ``modifiedBy``
     - int
     - ID of the User that last modified the Dynamic Content
   * - ``modifiedByUser``
     - string
     - Name of the User that last modified the Dynamic Content
   * - ``variantChildren``
     - array
     - Array of Dynamic Content entities for variants of this landing Dynamic Content
   * - ``variantParent``
     - object
     - The parent/main Dynamic Content if this is a variant, also known as A/B test
   * - ``sentCount``
     - int
     - Count of how many times the Dynamic Content got sent


**Response**

If ``PUT``, the expected response code is ``200`` if editing an existing Dynamic Content entry or ``201`` if creating a new one.

If ``PATCH``, the expected response code is ``200``.

**Properties**

Same as `Get Dynamic Content <#get-dynamic-content>`_.

.. vale off

Delete Dynamic Content
**********************

.. vale on

.. code-block:: php

   <?php

   $dynamicContent = $dynamicContentApi->delete($id);

Delete a dynamicContent.

.. vale off

**HTTP Request**

.. vale on

``DELETE /dynamiccontents/ID/delete``

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get Dynamic Content <#get-dynamic-content>`_.
