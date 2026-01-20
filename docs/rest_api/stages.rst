Stages
######

Use this API to manage and retrieve details about Contact Stages in Mautic.

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

Get a Stage
************

.. vale on

Get a specific Stage by ID.

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

``Expected Response Code: 200``

.. code-block:: json

   {
       "stage": {
       "id": 47,
       "isPublished": 1,
       "dateAdded": "2015-07-21T12:27:12-05:00",
       "createdBy": 1,
       "createdByUser": "Joe Smith",
       "dateModified": "2015-07-21T14:12:03-05:00",
       "modifiedBy": 1,
       "modifiedByUser": "Joe Smith",
       "name": "Stage A",
       "category": null,
       "description": "This is my first stage created via API.",
       "weight": 0,
       "publishUp": "2015-07-21T14:12:03-05:00",
       "publishDown": "2015-07-21T14:12:03-05:00"
   }

Stage properties
----------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - Stage ID
   * - ``isPublished``
     - boolean
     - Stage publication status
   * - ``dateAdded``
     - datetime
     - Stage creation date or time
   * - ``createdBy``
     - int
     - Stage creator User ID
   * - ``createdByUser``
     - string
     - Stage creator User name
   * - ``dateModified``
     - datetime/null
     - Stage last modification date and time
   * - ``modifiedBy``
     - int
     - Stage last modifier User ID
   * - ``modifiedByUser``
     - string
     - Stage last modifier User name
   * - ``name``
     - string
     - Stage name
   * - ``category``
     - int
     - Stage Category ID
   * - ``description``
     - string
     - Stage description
   * - ``weight``
     - int
     - Stage weight
   * - ``publishUp``
     - datetime
     - Stage publication start date and time
   * - ``publishDown``
     - datetime
     - Stage publication end date and time

.. vale off

List Contact Stages
*******************

.. vale on

Get a list of all Stages.

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

``Expected Response Code: 200``

.. code-block:: json

  {
  "total": 4,
  "stages": [
      {
        "id": 47,
        "isPublished": 1,
        "dateAdded": "2015-07-21T12:27:12-05:00",
        "createdBy": 1,
        "createdByUser": "Joe Smith",
        "dateModified": "2015-07-21T14:12:03-05:00",
        "modifiedBy": 1,
        "modifiedByUser": "Joe Smith",
        "name": "Stage A",
        "category": null,
        "description": "This is my first stage created via API.",
        "weight": 0,
        "publishUp": "2015-07-21T14:12:03-05:00",
        "publishDown": "2015-07-21T14:12:03-05:00"
      },
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
     - int
     - Total Stage count
   * - ``id``
     - int
     - Stage ID
   * - ``isPublished``
     - boolean
     - Stage publication status
   * - ``dateAdded``
     - datetime
     - Stage creation date or time
   * - ``createdBy``
     - int
     - Stage creator User ID
   * - ``createdByUser``
     - string
     - Stage creator User name
   * - ``dateModified``
     - datetime
     - Stage last modification date and time
   * - ``modifiedBy``
     - int
     - Stage last modifier User ID
   * - ``modifiedByUser``
     - string
     - Stage last modifier User name
   * - ``name``
     - string
     - Stage name
   * - ``category``
     - int
     - Stage Category ID
   * - ``description``
     - string
     - Stage description
   * - ``weight``
     - int
     - Stage weight
   * - ``publishUp``
     - datetime
     - Stage publication start date and time
   * - ``publishDown``
     - datetime
     - Stage publication end date and time

.. vale off

Create Stage
************

.. vale on

Create a new Stage.

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
     - Stage name - required
   * - ``weight``
     - int
     - Stage weight
   * - ``description``
     - string
     - Stage description
   * - ``isPublished``
     - boolean
     - Stage publication status

Response
========

``Expected Response Code: 201``

Properties
----------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - Stage ID
   * - ``isPublished``
     - boolean
     - Stage publication status
   * - ``dateAdded``
     - datetime
     - Stage creation date or time
   * - ``createdBy``
     - int
     - Stage creator User ID
   * - ``createdByUser``
     - string
     - Stage creator User name
   * - ``dateModified``
     - datetime/null
     - Stage last modification date and time
   * - ``modifiedBy``
     - int
     - Stage last modifier User ID
   * - ``modifiedByUser``
     - string
     - Stage last modifier User name
   * - ``name``
     - string
     - Stage name
   * - ``category``
     - int
     - Stage Category ID
   * - ``description``
     - string
     - Stage description
   * - ``weight``
     - int
     - Stage weight
   * - ``publishUp``
     - datetime
     - Stage publication start date and time
   * - ``publishDown``
     - datetime
     - Stage publication end date and time

.. vale off

Edit Stage
**********

.. vale on

Use this endpoint to update a Stage by ID. You can use either ``PUT`` or ``PATCH``.

* ``PUT``: to replace the Stage if it exists, or create a new one if it doesn’t.

* ``PATCH``: to update the Stage if it exists. If it doesn’t exist, Mautic returns a 404 error.

.. code-block:: php

  <?php

  $id   = 1;
  $data = array(
    'name'        => 'New stage name',
    'isPublished' => 0
  );

  // Create new a stage of ID 1 is not found?
  $createIfNotFound = true;

  $stage = $stageApi->edit($id, $data, $createIfNotFound);

.. vale off

HTTP request
============

.. vale on

``PATCH /stages/ID/edit``

``PUT /stages/ID/edit``

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
     - Stage name - required
   * - ``alias``
     - string
     - Name alias generated automatically if not set
   * - ``description``
     - string
     - Stage description
   * - ``isPublished``
     - boolean
     - Stage publication status
   * - ``weight``
     - int
     - Stage weight

Response
========

* ``PUT``: the expected response code is ``200`` or ``201`` if created.

* ``PATCH``: the expected response code is ``200``.

Properties
----------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - Stage ID
   * - ``isPublished``
     - boolean
     - Stage publication status
   * - ``dateAdded``
     - datetime
     - Stage creation date or time
   * - ``createdBy``
     - int
     - Stage creator User ID
   * - ``createdByUser``
     - string
     - Stage creator User name
   * - ``dateModified``
     - datetime/null
     - Stage last modification date and time
   * - ``modifiedBy``
     - int
     - Stage last modifier User ID
   * - ``modifiedByUser``
     - string
     - Stage last modifier User name
   * - ``name``
     - string
     - Stage name
   * - ``category``
     - int
     - Stage Category ID
   * - ``description``
     - string
     - Stage description
   * - ``weight``
     - int
     - Stage weight
   * - ``publishUp``
     - datetime
     - Stage publication start date and time
   * - ``publishDown``
     - datetime
     - Stage publication end date and time

.. vale off

Delete Stage
************

.. vale on

Delete a Stage by its ID.

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

``Expected Response Code: 200``

Properties
----------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - Stage ID
   * - ``isPublished``
     - boolean
     - Stage publication status
   * - ``dateAdded``
     - datetime
     - Stage creation date or time
   * - ``createdBy``
     - int
     - Stage creator User ID
   * - ``createdByUser``
     - string
     - Stage creator User name
   * - ``dateModified``
     - datetime/null
     - Stage last modification date and time
   * - ``modifiedBy``
     - int
     - Stage last modifier User ID
   * - ``modifiedByUser``
     - string
     - Stage last modifier User name
   * - ``name``
     - string
     - Stage name
   * - ``category``
     - int
     - Stage Category ID
   * - ``description``
     - string
     - Stage description
   * - ``weight``
     - int
     - Stage weight
   * - ``publishUp``
     - datetime
     - Stage publication start date and time
   * - ``publishDown``
     - datetime
     - Stage publication end date and time

.. vale off

Add Contact to a Stage
**********************

.. vale on

You can manually add a Contact to a specific Stage.

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

``POST/stages/STAGE_ID/contact/CONTACT_ID/add``

Response
========

``Expected Response Code: 200``

.. code-block:: json

   {
     "success": true
   }

.. vale off

Remove Contact from a Stage
***************************

.. vale on

You can manually remove a Contact from a specific Stage.

.. code-block:: php

   <?php

   //...
   $response = $stageApi->removeContact($stageId,  $contactId);
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

``Expected Response Code: 200``

.. code-block:: json
  
   {
     "success": true
   }