Focus
#####

Use this endpoint to obtain details on Mautic's Focus Items.

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
   $focusApi = $api->newApi("focus", $auth, $apiUrl);

.. vale off

Get Focus Item
**************

.. vale on

Retrieves an individual Focus Item.

.. code-block:: php

   <?php

   //...
   $focus = $focusApi->get($id);

.. vale off

HTTP request
============

.. vale on

``GET /focus/ID``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Focus Item.

.. _get Focus Item response:

.. code-block:: json

   {
       "focus": {
           "isPublished": true,
           "dateAdded": "2016-06-20T11:26:51+00:00",
           "createdBy": 1,
           "createdByUser": "John Doe",
           "dateModified": "2016-08-08T16:36:27+00:00",
           "modifiedBy": 1,
           "modifiedByUser": "John Doe",
           "category": null,
           "publishUp": null,
           "publishDown": null,
           "id": 1,
           "name": "Focus Bar",
           "type": "notice",
           "website": "",
           "htmlMode": "0",
           "html": "<div><strong style=\"color:red\">your html code</strong></div>",
           "css": ".mf-bar-collapser {border-radius: 0 !important}",
           "properties": {
               "bar": {
                   "allow_hide": 1,
                   "sticky": 1,
                   "size": "large",
                   "placement": "top"
               },
               "modal": {
                   "placement": "top"
               },
               "notification": {
                   "placement": "top"
               },
               "colors": {
                   "primary": "27184e"
               },
               "content": {
                   "headline": "",
                   "tagline": "",
                   "link_text": "",
                   "link_url": "",
                   "font": "Arial, Helvetica, sans-serif"
               },
               "animate": "1",
               "link_activation": "1",
               "when": "immediately",
               "frequency": "everypage",
               "stop_after_conversion": "1",
               "form": ""
           }
       }
   }

.. _get Focus Item properties:

Focus Item properties
----------------------

.. vale off

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Focus Item
   * - ``name``
     - string
     - Name of the Focus Item
   * - ``description``
     - string/null
     - Description of the Focus Item
   * - ``isPublished``
     - boolean
     - Published state
   * - ``publishUp``
     - datetime/null
     - Date/time when the Focus Item should be published
   * - ``publishDown``
     - datetime/null
     - Date/time the Focus Item should be unpublished
   * - ``dateAdded``
     - datetime
     - Date/time the Focus Item was created
   * - ``createdBy``
     - int
     - ID of the user that created the Focus Item
   * - ``createdByUser``
     - string
     - Name of the user that created the Focus Item
   * - ``dateModified``
     - datetime/null
     - Date/time the Focus Item was last modified
   * - ``modifiedBy``
     - int
     - ID of the user that last modified the Focus Item
   * - ``modifiedByUser``
     - string
     - Name of the user that last modified the Focus Item

.. vale on

.. vale off

List Focus Items
****************

.. vale on

Retrieves a list of Focus Items.

.. code-block:: php

   <?php
   // ...

   $focus = $focusApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

HTTP request
============

.. vale on

``GET /focus``

Query parameters
----------------

.. vale off

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Name
     - Description
   * - ``search``
     - String or search command to filter entities by
   * - ``start``
     - Starting row for the returned entities - defaults to 0
   * - ``limit``
     - Maximum number of entities to return - defaults to the system configuration for pagination (30)
   * - ``orderBy``
     - Column to sort by. Any column in the response is valid.
   * - ``orderByDir``
     - Order direction - ``asc`` or ``desc``
   * - ``publishedOnly``
     - Returns only currently published entities
   * - ``minimal``
     - Returns only an array of entities without additional lists in it

.. vale on

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Focus Items list.

.. code-block:: json

   {
       "total": 30,
       "focus": [
           {
               "isPublished": true,
               "dateAdded": "2016-06-20T11:26:51+00:00",
               "createdBy": 1,
               "createdByUser": "John Doe",
               "dateModified": "2016-08-08T16:36:27+00:00",
               "modifiedBy": 1,
               "modifiedByUser": "John Doe",
               "category": null,
               "publishUp": null,
               "publishDown": null,
               "id": 1,
               "name": "Focus Bar",
               "type": "notice",
               "website": "",
               "htmlMode": "0",
               "html": "<div><strong style=\"color:red\">your html code</strong></div>",
               "css": ".mf-bar-collapser {border-radius: 0 !important}",
               "properties": {
                   "bar": {
                       "allow_hide": 1,
                       "sticky": 1,
                       "size": "large",
                       "placement": "top"
                   },
                   "modal": {
                       "placement": "top"
                   },
                   "notification": {
                       "placement": "top"
                   },
                   "colors": {
                       "primary": "27184e"
                   },
                   "content": {
                       "headline": "",
                       "tagline": "",
                       "link_text": "",
                       "link_url": "",
                       "font": "Arial, Helvetica, sans-serif"
                   },
                   "animate": "1",
                   "link_activation": "1",
                   "when": "immediately",
                   "frequency": "everypage",
                   "stop_after_conversion": "1",
                   "form": ""
               }
           }
       ]
   }

Properties
----------

For the properties of each Focus Item, refer to :ref:`Focus Item properties <get Focus Item properties>`.

.. vale off

Create Focus Item
*****************

.. vale on

Creates a new Focus Item.

.. code-block:: php

   <?php

   $data = [
       'name'        => 'Focus Item',
       'isPublished' => 1,
   ];

   $focus = $focusApi->create($data);

.. vale off

HTTP request
============

.. vale on

``POST /focus/new``

POST parameters
---------------

.. vale off

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Name
     - Type
     - Description
   * - ``name``
     - string
     - Name of the Focus Item
   * - ``description``
     - string/null
     - Description of the Focus Item
   * - ``isPublished``
     - boolean
     - Published state
   * - ``publishUp``
     - datetime/null
     - Date/time when the Focus Item should be published
   * - ``publishDown``
     - datetime/null
     - Date/time the Focus Item should be unpublished

.. vale on

Response
========

* Returns ``201 Created`` when the request successfully creates a Focus Item.

Properties
----------

Refer to :ref:`Focus Item properties <get Focus Item properties>`.

.. vale off

Edit Focus Item
***************

.. vale on

Edits a Focus Item.

This operation supports ``PUT`` or ``PATCH`` depending on the desired behavior:

* ``PUT``: **full replacement**. The request creates a new Focus Item if the ID doesn't exist. If the ID exists, the request clears all existing data and replaces it with the provided values.
* ``PATCH``: **partial update**. The request only updates field values based on the request data. The request fails when the Focus Item ID doesn't exist.

.. code-block:: php

   <?php

   $id   = 1;
   $data = [
       'name'        => 'New Focus Item name',
       'isPublished' => 0,
   ];

   // Create a new Focus Item if ID 1 isn't found?
   $createIfNotFound = true;

   $focus = $focusApi->edit($id, $data, $createIfNotFound);

.. vale off

HTTP request
============

.. vale on

* ``PUT /focus/ID/edit``: updates an existing Focus Item or creates a new one when the ID doesn't exist.
* ``PATCH /focus/ID/edit``: updates an existing Focus Item. The request fails when the ID doesn't exist.

POST parameters
---------------

.. vale off

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Name
     - Type
     - Description
   * - ``name``
     - string
     - Name of the Focus Item
   * - ``description``
     - string/null
     - Description of the Focus Item
   * - ``isPublished``
     - boolean
     - Published state
   * - ``publishUp``
     - datetime/null
     - Date/time when the Focus Item should be published
   * - ``publishDown``
     - datetime/null
     - Date/time the Focus Item should be unpublished

.. vale on

Response
========

* ``PUT``: returns ``200 OK`` when the request successfully updates the Focus Item or ``201 Created`` when the request creates a Focus Item.
* ``PATCH``: returns ``200 OK`` when the request successfully updates the Focus Item or ``404 Not Found`` error when the Focus Item ID doesn't exist.

Properties
----------

Refer to :ref:`Focus Item properties <get Focus Item properties>`.

.. vale off

Delete Focus Item
*****************

.. vale on

Deletes a Focus Item.

.. code-block:: php

   <?php

   $focus = $focusApi->delete($id);

.. vale off

HTTP request
============

.. vale on

``DELETE /focus/ID/delete``

Response
========

* Returns ``200 OK`` when the request successfully deletes the Focus Item.

Properties
----------

Refer to :ref:`Focus Item properties <get Focus Item properties>`.
