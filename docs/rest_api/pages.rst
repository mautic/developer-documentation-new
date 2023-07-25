Landing Pages API
#################

Use this endpoint to obtain details on Mautic's Landing Pages.

.. code-block:: php

   <?php
   use Mautic\MauticApi;
   use Mautic\Auth\ApiAuth;

   // ...
   $initAuth = new ApiAuth();
   $auth     = $initAuth->newAuth($settings);
   $apiUrl   = "https://example.com";
   $api      = new MauticApi();
   $pageApi  = $api->newApi("pages", $auth, $apiUrl);

.. vale off

Get Landing Page
****************

.. vale on

.. code-block:: php

   <?php

   //...
   $page = $pageApi->get($id);

Get an individual Landing Page by ID.

.. vale off

**HTTP Request**

.. vale on

``GET /pages/ID``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "page": {
           "id": 3,
           "title": "Webinar Landing Page",
           "description": null,
           "isPublished": true,
           "publishUp": null,
           "publishDown": null,
           "dateAdded": "2015-07-15T15:06:02-05:00",
           "createdBy": 1,
           "createdByUser": "Joe Smith",
           "dateModified": "2015-07-20T13:11:56-05:00",
           "modifiedBy": 1,
           "modifiedByUser": "Joe Smith",
           "category": "Events",
           "language": "en",
           "template": "blank",
           "customHtml": "<!DOCTYPE ...",
           "hits": 0,
           "uniqueHits": 0,
           "variantHits": 0,
           "revision": 1,
           "metaDescription": null,
           "redirectType": null,
           "redirectUrl": null,
           "translationChildren": [],
           "translationParent": null,
           "variantChildren": [],
           "variantParent": null,
           "variantSettings": [],
           "variantStartDate": null
       }
   }

**Landing Page Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Landing Page
   * - ``title``
     - string
     - Title of the Landing Page
   * - ``description``
     - string/null
     - Description of the Landing Page
   * - ``alias``
     - string
     - Used to generate the URL for the Landing Page
   * - ``isPublished``
     - boolean
     - Published state
   * - ``publishUp``
     - datetime/null
     - Landing Page publish date/time
   * - ``publishDown``
     - datetime/null
     - Landing Page unpublish date/time
   * - ``dateAdded``
     - ``datetime``
     - Landing Page creation date/time
   * - ``createdBy``
     - int
     - ID of the User that created the Landing Page
   * - ``createdByUser``
     - string
     - Name of the User that created the Landing Page
   * - ``dateModified``
     - datetime/null
     - Date/time Landing Page was last modified
   * - ``modifiedBy``
     - int
     - ID of the User that last modified the Landing Page
   * - ``modifiedByUser``
     - string
     - Name of the User that last modified the Landing Page
   * - ``language``
     - string
     - Language locale of the Landing Page
   * - ``template``
     - string
     - Template of the Landing Page
   * - ``customHtml``
     - string
     - Static HTML of the Landing Page
   * - ``hits``
     - int
     - Total Landing Page hit count
   * - ``uniqueHits``
     - int
     - Unique Landing Page hit count
   * - ``revision``
     - int
     - Landing Page revision
   * - ``metaDescription``
     - string
     - Meta description for the Landing Page's ``<head>``
   * - ``redirectType``
     - int
     - If unpublished, redirect with 301 or 302
   * - ``redirectUrl``
     - string
     - If unpublished, the URL to redirect to if ``redirectType`` isn't empty
   * - ``translationChildren``
     - array
     - Array of Landing Page entities for translations of this Landing Page
   * - ``translationParent``
     - object
     - The parent/main Landing Page if this is a translation
   * - ``variantHits``
     - int
     - Hit count since variantStartDate
   * - ``variantChildren``
     - array
     - Array of Landing Page entities for variants of this Landing Page
   * - ``variantParent``
     - object
     - The parent/main Landing Page if this is a variant, also known as A/B test
   * - ``variantSettings``
     - array
     - The properties of the A/B test
   * - ``variantStartDate``
     - datetime/null
     - The date/time the A/B test began

.. vale off

List Landing Pages
******************

.. vale on

.. code-block:: php

   <?php
   // ...

   $pages = $pageApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. code-block:: json

   {
       "total": 1,
       "pages": [
           {
               "id": 3,
               "title": "Webinar Landing Page",
               "description": null,
               "isPublished": true,
               "publishUp": null,
               "publishDown": null,
               "dateAdded": "2015-07-15T15:06:02-05:00",
               "createdBy": 1,
               "createdByUser": "Joe Smith",
               "dateModified": "2015-07-20T13:11:56-05:00",
               "modifiedBy": 1,
               "modifiedByUser": "Joe Smith",
               "category": "Events",
               "language": "en",
               "template": "blank",
               "hits": 0,
               "uniqueHits": 0,
               "variantHits": 0,
               "revision": 1,
               "metaDescription": null,
               "redirectType": null,
               "redirectUrl": null,
               "translationChildren": [],
               "translationParent": null,
               "variantChildren": [],
               "variantParent": null,
               "variantSettings": [],
               "variantStartDate": null
           }
       ]
   }

.. vale off

**HTTP Request**

.. vale on

``GET /pages``

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

See JSON code example.

**Properties**

Same as `Get Landing Page <#get-landing-page>`_.

.. vale off

Create Landing Page
*******************

.. vale on

.. code-block:: php

   <?php

   $data = array(
       'title'        => 'Page A',
       'description' => 'This is my first Landing Page created via API.',
       'isPublished' => 1
   );

   $page = $pageApi->create($data);

Create a new Landing Page.

.. vale off

**HTTP Request**

.. vale on

``POST /pages/new``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``title``
     - string
     - Landing Page title is the only required field
   * - ``alias``
     - string
     - Used to generate the URL for the Landing Page
   * - ``description``
     - string
     - A description of the Landing Page.
   * - ``isPublished``
     - int
     - A value of 0 or 1
   * - ``language``
     - string
     - Language locale of the Landing Page
   * - ``metaDescription``
     - string
     - Meta description for the Landing Page's ``<head>``
   * - ``redirectType``
     - int
     - If unpublished, redirect with 301 or 302
   * - ``redirectUrl``
     - string
     - If unpublished, the URL to redirect to if ``redirectType`` isn't empty

**Response**

``Expected Response Code: 201``

**Properties**

Same as `Get Landing Page <#get-landing-page>`_.

.. vale off

Edit Landing Page
*****************

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'title'        => 'New Landing Page title',
       'isPublished' => 0
   );

   // Create new a Landing Page of ID 1 isn't found?
   $createIfNotFound = true;

   $page = $pageApi->edit($id, $data, $createIfNotFound);

Edit a new Landing Page. Note that this supports PUT or PATCH depending on the desired behavior.

**PUT** creates a Landing Page if the given ID doesn't exist and clears all the Landing Page information, adds the information from the request.

**PATCH** fails if the Landing Page with the given ID doesn't exist and updates the Landing Page field values with the values from the request.

.. vale off

**HTTP Request**

.. vale on

To edit a Landing Page and return a 404 if the Landing Page isn't found:

``PATCH /pages/ID/edit``

To edit a Landing Page and create a new one if the Landing Page isn't found:

``PUT /pages/ID/edit``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``title``
     - string
     - Landing Page title is the only required field
   * - ``alias``
     - string
     - Name alias generated automatically if not set
   * - ``description``
     - string
     - A description of the Landing Page.
   * - ``isPublished``
     - int
     - A value of 0 or 1
   * - ``language``
     - string
     - Language locale of the Landing Page
   * - ``metaDescription``
     - string
     - Meta description for the Landing Page's ``<head>``
   * - ``redirectType``
     - int
     - If unpublished, redirect with 301 or 302
   * - ``redirectUrl``
     - string
     - If unpublished, the URL to redirect to if ``redirectType`` isn't empty


**Response**

If ``PUT``, the expected response code is ``200`` if editing a Landing Page or ``201`` if creating a new one.

If ``PATCH``, the expected response code is ``200``.

**Properties**

Same as `Get Landing Page <#get-landing-page>`_.

.. vale off

Delete Landing Page
*******************

.. vale on

.. code-block:: php

   <?php

   $page = $pageApi->delete($id);

Delete a Landing Page.

.. vale off

**HTTP Request**

.. vale on

``DELETE /pages/ID/delete``

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get Landing Page <#get-landing-page>`_.
