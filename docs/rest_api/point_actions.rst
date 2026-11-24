Point Actions
#############

Use this endpoint to manipulate and obtain details on Mautic's Point Actions.

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
   $pointApi = $api->newApi("points", $auth, $apiUrl);

.. vale off

Get Point Action
****************

.. vale on

Retrieves an individual Point Action.

.. code-block:: php

   <?php

   //...
   $point = $pointApi->get($id);

.. vale off

HTTP request
============

.. vale on

``GET /points/ID``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Point Action.

.. _get Point Action response:

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

.. _get Point Action properties:

.. vale off

Point Action properties
-----------------------

.. list-table::
   :widths: 25 25 50
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
     - string
     - Description of the Point Action
   * - ``category``
     - string
     - The Category assigned to the Point Action
   * - ``type``
     - string
     - Point Action type. Refer to :ref:`Get Point Action types <get Point Action Types>` for the available types
   * - ``isPublished``
     - boolean
     - Point Action activation status
   * - ``publishUp``
     - datetime
     - Activation date and time for the Point Action
   * - ``publishDown``
     - datetime
     - Deactivation date and time for the Point Action
   * - ``dateAdded``
     - datetime
     - Point Action record creation date and time
   * - ``createdBy``
     - int
     - ID of the User who created the Point Action
   * - ``createdByUser``
     - string
     - Name of the User who created the Point Action
   * - ``dateModified``
     - datetime
     - Point Action record last modification date and time
   * - ``modifiedBy``
     - int
     - ID of the User who last modified the Point Action
   * - ``modifiedByUser``
     - string
     - Name of the User who last modified the Point Action
   * - ``delta``
     - int
     - Number of points to award the Contact when Mautic executes this action
   * - ``properties``
     - object
     - Configured properties for the specific Point Action type

.. vale on

.. vale off

List Point Actions
******************

.. vale on

Retrieves a list of Point Actions.

.. code-block:: php

   <?php

   //...
   $points = $pointApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

HTTP request
============

.. vale on

``GET /points``

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
     - int
     - Starting row for the returned entities - defaults to 0
   * - ``limit``
     - int
     - Maximum number of entities to return - defaults to 30
   * - ``orderBy``
     - string
     - Column to sort by. Any column in the response is valid.

       **Note**: convert ``camelCase`` properties to ``snake_case``. For example, ``dateAdded`` becomes ``date_added``, ``publishUp`` becomes ``publish_up``, and so on
   * - ``orderByDir``
     - string
     - Order direction - ``asc`` or ``desc``
   * - ``publishedOnly``
     - boolean
     - Returns only currently activated entities
   * - ``minimal``
     - boolean
     - Returns only a simple mapped object of entities without additional lists in it

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Point Actions list.

.. code-block:: json

   {
       "total": 1,
       "points": [
           {
               "id": 1,
               "name": "Opens Email",
               "description": null,
               "category": null,
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

Properties
----------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``total``
     - int
     - Total count of Point Actions
   * - ``points``
     - array
     - Array of Point Actions

.. vale off

For the rest of the properties, refer to :ref:`Point Action properties <get Point Action properties>`.

.. vale on

.. vale off

Create Point Action
*******************

.. vale on

Creates a new Point Action.

.. code-block:: php

   <?php

   $data = array(
       'name'        => 'test',
       'delta'       => 5,
       'type'        => 'page.hit',
       'description' => 'created as an API test'
   );

   $point = $pointApi->create($data);

.. vale off

HTTP request
============

.. vale on

``POST /points/new``

.. _create Point Action POST parameters:

.. vale off

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

       Name of the Point Action
   * - ``type``
     - string
     - **Required.**

       Point Action type. Refer to :ref:`Get Point Action types <get Point Action Types>` for the available types
   * - ``delta``
     - int
     - **Required.**

       Number of points to award the Contact when Mautic executes this action
   * - ``description``
     - string
     - Description of the Point Action
   * - ``category``
     - int
     - ID of the Category to assign to the Point Action
   * - ``isPublished``
     - boolean
     - Point Action activation status
   * - ``publishUp``
     - datetime
     - Activation date and time for the Point Action
   * - ``publishDown``
     - datetime
     - Deactivation date and time for the Point Action
   * - ``properties``
     - object
     - Configured properties for the specific Point Action type

.. vale on

Response
========

* Returns ``201 Created`` when the request successfully creates a Point Action.

The response is a JSON object similar to :ref:`Get Point Action <get Point Action response>`.

Properties
----------

Refer to :ref:`Point Action properties <get Point Action properties>`.

.. vale off

Edit Point Action
*****************

.. vale on

Edits a Point Action.

This operation supports ``PUT`` or ``PATCH`` depending on the desired behavior:

* ``PUT``: **full replacement**. The request creates a new Point Action if the ID is missing. If the ID exists, the request clears all existing data and replaces it with the provided values.
* ``PATCH``: **partial update**. The request only updates field values based on the request data. The request fails when the Point Action ID doesn't exist.

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'name'        => 'test',
       'delta'       => 5,
       'type'        => 'page.hit',
       'description' => 'created as an API test'
   );

   // Create a new Point Action if ID 1 isn't found
   $createIfNotFound = true;

   $point = $pointApi->edit($id, $data, $createIfNotFound);

.. vale off

HTTP request
============

.. vale on

* ``PUT /points/ID/edit``: updates an existing Point Action or creates a new one when the ID doesn't exist.
* ``PATCH /points/ID/edit``: updates an existing Point Action. The request fails when the ID doesn't exist.

POST parameters
---------------

Accepts the same parameters as those described in :ref:`Create Point Action <create Point Action POST parameters>`. All parameters are optional.

Response
========

* ``PUT``: returns ``200 OK`` when the request successfully updates the Point Action or ``201 Created`` when the request creates a Point Action.
* ``PATCH``: returns ``200 OK`` when the request successfully updates the Point Action or ``404 Not Found`` error when the Point Action ID doesn't exist.

The response is a JSON object similar to :ref:`Get Point Action <get Point Action response>`.

Properties
----------

Refer to :ref:`Point Action properties <get Point Action properties>`.

.. vale off

Delete Point Action
*******************

.. vale on

Deletes a Point Action.

.. code-block:: php

   <?php

   $point = $pointApi->delete($id);

.. vale off

HTTP request
============

.. vale on

``DELETE /points/ID/delete``

Response
========

* Returns ``200 OK`` when the request successfully deletes the Point Action.

The response is a JSON object containing the data of the deleted Point Action, similar to :ref:`Get Point Action <get Point Action response>`.

Properties
----------

Refer to :ref:`Point Action properties <get Point Action properties>`.

.. _get Point Action Types:

.. vale off

Get Point Action types
**********************

.. vale on

Retrieves an array of available Point Action types.

.. code-block:: php

   <?php

   //...
   $pointActionTypes = $pointApi->getPointActionTypes();

.. vale off

HTTP request
============

.. vale on

``GET /points/actions/types``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Point Action types.

.. code-block:: json

   {
       "pointActionTypes": {
           "asset.download": "Downloads an asset",
           "email.send": "Is sent an email",
           "email.open": "Opens an email",
           "form.submit": "Submits a form",
           "page.hit": "Visits a landing page",
           "url.hit": "Visits specific URL"
       }
   }
