Stages
#######

Use this API to manage and retrieve details about Contact stages in Mautic.

.. .. code-block:: php

..     <?php
..     use Mautic\MauticApi;
..     use Mautic\Auth\ApiAuth;

..     // ...
..     $initAuth = new ApiAuth();
..     $auth     = $initAuth->newAuth($settings);
..     $apiUrl   = "https://your-mautic.com";
..     $api      = new MauticApi();
..     $stageApi = $api->newApi("stages", $auth, $apiUrl);


.. vale off

Get a Stage
************

Get a specific Stage by ID.

.. vale on

.. code-block:: php

   <?php

   //...
   $stage = $stageApi->get($id);

.. vale off

**HTTP Request**

.. vale on

``GET /stages/ID``

**Response**

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

**Stage Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - The ID of the Stage.
   * - ``isPublished``
     - boolean
     - Whether the Stage is published.
   * - ``dateAdded``
     - datetime
     - The date or time the Stage was created.
   * - ``createdBy``
     - int
     - The ID of the user that created the Stage.
   * - ``createdByUser``
     - string
     - The name of the user that created the Stage.
   * - ``dateModified``
     - datetime/null
     - The date and time, the Stage was last modified.
   * - ``modifiedBy``
     - int
     - The ID of the user that last modified the Stage.
   * - ``modifiedByUser``
     - string
     - The name of the user that last modified the Stage.
   * - ``name``
     - string
     - The name of the Stage.
   * - ``category``
     - int
     - The category ID of the Stage category.
   * - ``description``
     - string
     - The description of the Stage.
   * - ``weight``
     - int
     - The weight of the Stage.
   * - ``publishUp``
     - datetime
     - The date and time the Stage should be published.
   * - ``publishDown``
     - datetime
     - The date and time, the stage should be unpublished.

.. vale off

List Contact Stages
*********************

Get a list of all stages.

.. vale on

.. code-block:: php

   <?php

   //...
   $stages = $stageApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

**HTTP Request**

.. vale on

``GET /stages``

**Response**

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

**Stage Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``total``
     - int
     - The total number of all the Stages.
   * - ``id``
     - int
     - The ID of the Stage.
   * - ``isPublished``
     - boolean
     - Whether the stage is published.
   * - ``dateAdded``
     - datetime
     - The date and time the Stage was created.
   * - ``createdBy``
     - int
     - The ID of the user that created the Stage.
   * - ``createdByUser``
     - string
     - The name of the user that created the Stage.
   * - ``dateModified``
     - datetime
     - The date and time the Stage was last modified.
   * - ``modifiedBy``
     - int
     - The ID of the user that last modified the Stage.
   * - ``modifiedByUser``
     - string
     - The name of the user that last modified the Stage.
   * - ``name``
     - string
     - The name of the Stage.
   * - ``category``
     - int
     - The category ID of the Stage.
   * - ``description``
     - string
     - The description of the Stage.
   * - ``weight``
     - int
     - The weight of the Stage.
   * - ``publishUp``
     - datetime
     - The date and time the Stage should be published.
   * - ``publishDown``
     - datetime
     - The date and time the Stage should be unpublished.

.. vale off

Create Stage
**************

Create a new stage.

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

**HTTP Request**

.. vale on

``POST /stages/new``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``name``
     - String
     - (Required) The Stage name..
   * - ``weight``
     - int
     - The weight of the Stage.
   * - ``description``
     - string
     - A description of the stage.
   * - ``isPublished``
     - boolean
     - Whether the Stage is published.


**Response**

``Expected Response Code: 201``

**Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - The ID of the Stage.
   * - ``isPublished``
     - boolean
     - Whether the Stage is published.
   * - ``dateAdded``
     - datetime
     - The date or time the Stage was created.
   * - ``createdBy``
     - int
     - The ID of the user that created the Stage.
   * - ``createdByUser``
     - string
     - The name of the user that created the Stage.
   * - ``dateModified``
     - datetime/null
     - The date and time, the Stage was last modified.
   * - ``modifiedBy``
     - int
     - The ID of the user that last modified the Stage.
   * - ``modifiedByUser``
     - string
     - The name of the user that last modified the Stage.
   * - ``name``
     - string
     - The name of the Stage.
   * - ``category``
     - int
     - The category ID of the Stage category.
   * - ``description``
     - string
     - The description of the Stage.
   * - ``weight``
     - int
     - The weight of the Stage.
   * - ``publishUp``
     - datetime
     - The date and time the Stage should be published.
   * - ``publishDown``
     - datetime
     - The date and time, the stage should be unpublished.

.. vale off


Edit Stage
************

Use this endpoint to update a Stage by ID. You can use either PUT or PATCH:

Use **PUT** to replace the stage if it exists, or create a new one if it doesn’t.

Use **PATCH** to update the stage if it exists. If the stage doesn’t exist, Mautic returns a 404 error.

.. vale on

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


**HTTP Request**

.. vale on
``PATCH /stages/ID/edit``

``PUT /stages/ID/edit``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - ``name``
     - string
     - (Required) The Stage name..
   * - ``alias``
     - string
     - Name alias generated automatically if not set.
   * - ``description``
     - string
     - A description of the stage.
   * - ``isPublished``
     - boolean
     - Whether the Stage is published.
   * - ``weight``
     - int
     - 

**Response**

If ``PUT``\ , the expected response code is ``200`` or ``201`` if created.

If using ``PATCH``\ , the expected response code is ``200``.

**Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - The ID of the Stage.
   * - ``isPublished``
     - boolean
     - Whether the Stage is published.
   * - ``dateAdded``
     - datetime
     - The date or time the Stage was created.
   * - ``createdBy``
     - int
     - The ID of the user that created the Stage.
   * - ``createdByUser``
     - string
     - The name of the user that created the Stage.
   * - ``dateModified``
     - datetime/null
     - The date and time, the Stage was last modified.
   * - ``modifiedBy``
     - int
     - The ID of the user that last modified the Stage.
   * - ``modifiedByUser``
     - string
     - The name of the user that last modified the Stage.
   * - ``name``
     - string
     - The name of the Stage.
   * - ``category``
     - int
     - The category ID of the Stage category.
   * - ``description``
     - string
     - The description of the Stage.
   * - ``weight``
     - int
     - The weight of the Stage.
   * - ``publishUp``
     - datetime
     - The date and time the Stage should be published.
   * - ``publishDown``
     - datetime
     - The date and time, the stage should be unpublished.

.. vale off

Delete Stage
**************

Delete a stage by its ID.

.. vale on

.. code-block:: php

  <?php

  $stage = $stageApi->delete($id);

.. vale off

**HTTP Request**

.. vale on

``DELETE /stages/ID/delete``

**Response**

``Expected Response Code: 200``

**Properties**

.. list-table::
   :header-rows: 1
   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - The ID of the Stage.
   * - ``isPublished``
     - boolean
     - Whether the Stage is published.
   * - ``dateAdded``
     - datetime
     - The date or time the Stage was created.
   * - ``createdBy``
     - int
     - The ID of the user that created the Stage.
   * - ``createdByUser``
     - string
     - The name of the user that created the Stage.
   * - ``dateModified``
     - datetime/null
     - The date and time, the Stage was last modified.
   * - ``modifiedBy``
     - int
     - The ID of the user that last modified the Stage.
   * - ``modifiedByUser``
     - string
     - The name of the user that last modified the Stage.
   * - ``name``
     - string
     - The name of the Stage.
   * - ``category``
     - int
     - The category ID of the Stage category.
   * - ``description``
     - string
     - The description of the Stage.
   * - ``weight``
     - int
     - The weight of the Stage.
   * - ``publishUp``
     - datetime
     - The date and time the Stage should be published.
   * - ``publishDown``
     - datetime
     - The date and time, the Stage should be unpublished.

.. vale off

Add Contact to a Stage
************************

You can manually add a contact to a specific Stage.

.. vale on

.. code-block:: php

  <?php

  //...
  $response = $stageApi->addContact($stageId, $contactId);
  if (!isset($response['success'])) {
    // handle error
  }
.. vale off

**HTTP Request**

.. vale on

``POST/stages/STAGE_ID/contact/CONTACT_ID/add``

**Response**

``Expected Response Code: 200``

.. code-block:: json
  {
    "success": true
  }


.. vale off

Remove Contact from a Stage
*****************************

You can manually remove a contact from a specific Stage.

.. vale on

.. code-block:: php

  <?php

  //...
  $response = $stageApi->removeContact($stageId, $contactId);
  if (!isset($response['success'])) {
    // handle error
  }
.. vale off

**HTTP Request**

.. vale on

``POST /stages/STAGE_ID/contact/CONTACT_ID/remove``

**Response**

``Expected Response Code: 200``

.. code-block:: json
  {
    "success": true
  }