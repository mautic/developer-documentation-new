Point Actions
#############

Use this endpoint to obtain details on Mautic's Point Actions.

**Using Mautic's API Library**

You can interact with this API through the :xref:`Mautic API Library` as follows, or use the various http endpoints as described in this document.

.. code-block:: php

   <?php
   use Mautic\MauticApi;
   use Mautic\Auth\ApiAuth;

   // ...
   $initAuth = new ApiAuth();
   $auth     = $initAuth->newAuth($settings);
   $apiUrl   = "https://mautic.example.com";
   $api      = new MauticApi();
   $pointApi = $api->newApi("points", $auth, $apiUrl);

.. vale off

Get Point Action
****************

.. vale on

.. code-block:: php

   <?php

   //...
   $point = $pointApi->get($id);

Get an individual Point Action by ID.

.. vale off

**HTTP Request**

.. vale on

``GET /points/ID``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "point": {
           "id": 1,
           "name": "Opens Email",
           "description": null,
           "type": "email.send",
           "isPublished": true,
           "publishUp": null,
           "publishDown": null,
           "dateAdded": "2015-07-19T00:34:11-05:00",
           "createdBy": 1,
           "createdByUser": "Joe Smith",
           "dateModified": "2015-07-19T00:41:44-05:00",
           "modifiedBy": 1,
           "modifiedByUser": "Joe Smith",
           "delta": 10,
           "properties": {
               "emails": [
                   35
               ]
           },
           "category": null
       }
   }

**Point Action Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Point Action
   * - ``name``
     - string
     - Name of the Point Action
   * - ``description``
     - string/null
     - Description of the Point Action
   * - ``category``
     - string
     - Category name
   * - ``type``
     - string
     - Point Action type
   * - ``isPublished``
     - boolean
     - Published state
   * - ``publishUp``
     - datetime/null
     - Point Action publish date/time
   * - ``publishDown``
     - datetime/null
     - Point Action unpublish date/time
   * - ``dateAdded``
     - ``datetime``
     - Point Action creation date/time
   * - ``createdBy``
     - int
     - ID of the User that created the Point Action
   * - ``createdByUser``
     - string
     - Name of the User that created the Point Action
   * - ``dateModified``
     - datetime/null
     - Date/time Point Action was last modified
   * - ``modifiedBy``
     - int
     - ID of the User that last modified the Point Action
   * - ``modifiedByUser``
     - string
     - Name of the User that last modified the Point Action
   * - ``delta``
     - int
     - The number of Points to assign to the Contact when executing this Point Action
   * - ``properties``
     - array
     - Configured properties for this Point Action

.. vale off

List Point Actions
******************

.. vale on

.. code-block:: php

   <?php
   // ...

   $points = $pointApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

**HTTP Request**

.. vale on

``GET /points``

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
       "total": 1,
       "points": [
           {
               "id": 1,
               "name": "Opens Email",
               "description": null,
               "category": null
               "type": "email.send",
               "isPublished": true,
               "publishUp": null,
               "publishDown": null,
               "dateAdded": "2015-07-19T00:34:11-05:00",
               "createdBy": 1,
               "createdByUser": "Joe Smith",
               "dateModified": "2015-07-19T00:41:44-05:00",
               "modifiedBy": 1,
               "modifiedByUser": "Joe Smith",
               "delta": 10,
               "properties": {
                   "emails": [
                       35
                   ]
               }
           }
       ]
   }

**Properties**

Same as `Get Point Action <#get-point-action>`_.

.. vale off

Create Point Action
*******************

.. vale on

.. code-block:: php

   <?php 

   $data = array(
       'name' => 'test',
       'delta' => 5,
       'type' => 'page.hit',
       'description' => 'created as a API test'
   );

   $point = $pointApi->create($data);

Create a new Point Action.

.. vale off

**HTTP Request**

.. vale on

``POST /points/new``

**POST Parameters**

Same as `Get Point Action <#get-point-action>`_. You can create or edit Point Action fields and actions via the Point Actions/actions arrays in the Point Action array.

**Response**

``Expected Response Code: 201``

**Properties**

Same as `Get Point Action <#get-point-action>`_.

.. vale off

Edit Point Action
*****************

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'name' => 'test',
       'delta' => 5,
       'type' => 'page.hit',
       'description' => 'created as a API test'
   );

   // Create new a Point Action of ID 1 isn't found?
   $createIfNotFound = true;

   $point = $pointApi->edit($id, $data, $createIfNotFound);

Edit a Point Action. Note that this supports PUT or PATCH depending on the desired behavior.

**PUT** creates a Point Action if the given ID doesn't exist and overwrites all the Point Actions with the ones provided in the request. Note that Point Action fields and actions are also deleted if not present in the request.

**PATCH** fails if the Point Action with the given ID doesn't exist. Updates the Point Action field values with the values provided in the request.

.. vale off

**HTTP Request**

.. vale on

To edit a Point Action and return a 404 if the Point Action isn't found:

``PATCH /points/ID/edit``

To edit a Point Action and create a new one if the Point Action isn't found:

``PUT /points/ID/edit``

**POST Parameters**

Same as `Get Point Action <#get-point-action>`_. You can create or edit Point Action fields and actions via the Point Actions/actions arrays in the Point Action array.

**Response**

If ``PUT``, the expected response code is ``200`` if editing a Point Action or ``201`` if creating a new one.

If ``PATCH``, the expected response code is ``200``.

**Properties**

Same as `Get Point Action <#get-point-action>`_.

.. vale off

Delete Point Action
*******************

.. vale on

.. code-block:: php

   <?php

   $point = $pointApi->delete($id);

Delete a Point Action.

.. vale off

**HTTP Request**

.. vale on

``DELETE /points/ID/delete``

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get Point Action <#get-point-action>`_.

.. vale off

Get Point Action Types
**********************

.. vale on

.. code-block:: php

   <?php

   $point = $pointApi->getPointActionTypes();

Get array of available Point Action Types

.. vale off

**HTTP Request**

.. vale on

``GET /points/actions/types``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {  
       "pointActionTypes":{  
           "asset.download": "Downloads an asset",
           "email.send": "Is sent an email",
           "email.open": "Opens an email",
           "form.submit": "Submits a form",
           "page.hit": "Visits a landing page",
           "url.hit": "Visits specific URL"
       }
   }

See JSON code example.
