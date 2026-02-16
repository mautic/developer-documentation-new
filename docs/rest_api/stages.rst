.. vale off

.. note::

  The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

  If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

  Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Stages
######

Use this endpoint to manipulate and obtain details on Mautic's Contact Stages.

Using Mautic API library
************************

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
   $apiUrl   = "https://your-mautic.com";
   $api      = new MauticApi();
   $stageApi = $api->newApi("stages", $auth, $apiUrl);

.. vale off

Get Stage
*********

Retrieves an individual Stage.

.. vale on

.. code-block:: php

   <?php

   //...
   $stage = $stageApi->get($id);

.. vale off

HTTP request
============

.. vale on

``GET /stages/ID``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Stage.

.. _get Stage response:

.. code-block:: json

   {
      "stage": {
          "isPublished": true,
          "dateAdded": "2026-02-13T16:11:07+00:00",
          "dateModified": null,
          "createdBy": 1,
          "createdByUser": "Joe Smith",
          "modifiedBy": 1,
          "modifiedByUser": "Joe Smith",
          "id": 7,
          "name": "Stage A",
          "category": null,
          "weight": 0,
          "description": "This is my first stage created via API.",
          "publishUp": "2026-02-13T17:00:00+00:00",
          "publishDown": "2026-02-20T17:00:00+00:00"
      }
   }

.. _get Stage properties:

Stage properties
----------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``isPublished``
     - boolean
     - Stage publication status
   * - ``dateAdded``
     - datetime
     - Stage record creation date and time
   * - ``dateModified``
     - datetime or null
     - Stage record last modification date and time
   * - ``createdBy``
     - integer
     - ID of the User who created the Stage
   * - ``createdByUser``
     - string
     - Name of the User who created the Stage
   * - ``modifiedBy``
     - integer or null
     - ID of the User who last modified the Stage
   * - ``modifiedByUser``
     - string or null
     - Name of the User who last modified the Stage
   * - ``id``
     - integer
     - ID of the Stage
   * - ``name``
     - string
     - Stage name - **required**
   * - ``category``
     - object or null
     - The Category assigned to the Stage
   * - ``weight``
     - integer
     - Stage weight
   * - ``description``
     - string or null
     - Description of the Stage
   * - ``publishUp``
     - datetime or null
     - Activation date and time for the Stage
   * - ``publishDown``
     - datetime or null
     - Deactivation date and time for the Stage

.. vale off

List Stages
***********

Retrieves a list of Stages.

.. vale on

.. code-block:: php

   <?php

   //...
   $stages = $stageApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

HTTP request
============

.. vale on

``GET /stages``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the list of Stages.

.. code-block:: json

   {
     "total": 4,
     "stages": [
       {
          "isPublished": true,
          "dateAdded": "2026-02-13T16:11:07+00:00",
          "dateModified": null,
          "createdBy": 1,
          "createdByUser": "Joe Smith",
          "modifiedBy": 1,
          "modifiedByUser": "Joe Smith",
          "id": 7,
          "name": "Stage A",
          "category": null,
          "weight": 0,
          "description": "This is my first stage created via API.",
          "publishUp": "2026-02-13T17:00:00+00:00",
          "publishDown": "2026-02-20T17:00:00+00:00"
       },
       //...
     ]
   }

Stage properties
----------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``total``
     - integer
     - Total count of Stages

For the rest of the Stage properties, refer to :ref:`Get Stage <get Stage properties>`.

.. vale off

Create Stage
************

Creates a new Stage.

.. vale on

.. code-block:: php

   <?php 

   $data = array(
     'name'        => 'Stage A',
     'weight'      => 5,
     'description' => 'This is my first stage created via API.',
     'isPublished' => 1
   );

   $stage = $stageApi->create($data);

.. vale off

HTTP request
============

.. vale on

``POST /stages/new``

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
     - Stage name - **required**
   * - ``weight``
     - integer
     - Stage weight
   * - ``description``
     - string
     - Description of the Stage
   * - ``isPublished``
     - boolean
     - Stage publication status - set to ``0`` or ``false`` to inactive. When not set, it defaults to active.

Response
========

* Returns ``201 Created`` when the request successfully creates a Stage.

Response is the same as :ref:`Get Stage <get Stage response>`.

Properties
----------

Refer to :ref:`Get Stage <get Stage properties>`.

.. vale off

Edit Stage
**********

.. vale on

Edits a Stage. This operation supports ``PUT`` or ``PATCH`` depending on the desired behavior:

* ``PUT``: **full replacement**. The request creates a new Stage if the ID is missing. If the ID exists, the request clears all existing data and replaces it with the provided values.
* ``PATCH``: **partial update**. The request only updates field values based on the request data. The request fails when the ID doesn't exist.

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
     'name'        => 'New stage name',
     'isPublished' => 0
   );

   // Create new a stage if ID 1 is not found?
   $createIfNotFound = true;

   $stage = $stageApi->edit($id, $data, $createIfNotFound);

.. vale off

HTTP request
============

.. vale on

* ``PUT /stages/ID/edit``: updates an existing Stage or creates a new one when the ID doesn't exist.
* ``PATCH /stages/ID/edit``: updates an existing Stage. The request fails when the ID doesn't exist.

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
     - Stage name - **required**
   * - ``alias``
     - string
     - Stage alias - generated automatically if not set
   * - ``description``
     - string
     - Description of the Stage
   * - ``isPublished``
     - boolean
     - Stage publication status
   * - ``weight``
     - int
     - Stage weight

Response
========

* ``PUT``: returns ``200 OK`` when the request successfully updates the Stage or ``201 Created`` when the request creates a Stage.
* ``PATCH``: returns ``200 OK`` when the request successfully updates the Stage or ``404 Not Found`` when the ID doesn't exist.

Response is the same as :ref:`Get Stage <get Stage response>`.

Properties
----------

Refer to :ref:`Get Stage <get Stage properties>`.

.. vale off

Delete Stage
************

Deletes a Stage.

.. vale on

.. code-block:: php

   <?php

   $stage = $stageApi->delete($id);

.. vale off

HTTP request
============

.. vale on

``DELETE /stages/ID/delete``

Response
========

* Returns ``200 OK`` when the request successfully deletes the Stage.

Response is the same to :ref:`Get Stage <get Stage response>`, but with the deleted Stage.

Properties
----------

Refer to :ref:`Get Stage <get Stage properties>`.

.. vale off

Add Contact to Stage
********************

.. vale on

Adds a Contact to a Stage.

.. code-block:: php

   <?php

   //...
   $response = $stageApi->addContact($stageId, $contactId);
   if (!isset($response['success'])) {
     // handle error
   }

.. vale off

HTTP request
============

.. vale on

``POST /stages/STAGE_ID/contact/CONTACT_ID/add``

Response
========

* Returns ``200 OK`` when the request successfully adds the Contact to the Stage.

.. code-block:: json

   {
     "success": 1
   }

.. vale off

Remove Contact from Stage
*************************

.. vale on

Removes a Contact from a Stage.

.. code-block:: php

   <?php

   //...
   $response = $stageApi->removeContact($stageId, $contactId);
   if (!isset($response['success'])) {
     // handle error
   }

.. vale off

HTTP request
============

.. vale on

``POST /stages/STAGE_ID/contact/CONTACT_ID/remove``

Response
========

* Returns ``200 OK`` when the request successfully removes the Contact from the Stage.

.. code-block:: json

   {
     "success": 1
   }
