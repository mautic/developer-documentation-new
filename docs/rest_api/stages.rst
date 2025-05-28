Stages
#######

Use this endpoint to obtain details on Mautic’s Contact Stages.

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

.. code-block:: php

   <?php

   //...
   $stage = $stageApi->get($id);



Get an individual Stage by ID.

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
     - ID of the Stage
   * - ``isPublished``
     - boolean
     - Whether the Stage is published
   * - ``dateAdded``
     - datetime
     - Date/time Stage was created
   * - ``createdBy``
     - int
     - ID of the user that created the Stage
   * - ``createdByUser``
     - string
     - Name of the user that created the Stage
   * - ``dateModified``
     - datetime/null
     - Date/time Stage was last modified
   * - ``modifiedBy``
     - int
     - ID of the user that last modified the Stage
   * - ``modifiedByUser``
     - string
     - Name of the user that last modified the Stage
   * - ``name``
     - string`
     - Stage name
   * - ``category``
     - int
     - Stage category ID
   * - ``description``
     - string
     - Stage description
   * - ``weight``
     - int
     - Stage's weight
   * - ``publishUp``
     - datetime
     - Date/time stage should be published
   * - ``publishDown``
     - datetime
     - Date/time stage should be unpublished

.. vale off

List Contact Stages
*********************

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
    ...
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
     - Count of all stages
   * - ``id``
     - int
     - ID of the stage
   * - ``isPublished``
     - boolean
     - Whether the stage is published
   * - ``dateAdded``
     - datetime
     - Date/time stage was created
   * - ``createdBy``
     - int
     - ID of the user that created the stage
   * - ``createdByUser``
     - string
     - Name of the user that created the stage
   * - ``dateModified``
     - datetime
     - Date/time stage was last modified
   * - ``modifiedBy``
     - int
     - ID of the user that last modified the stage
   * - ``modifiedByUser``
     - string
     - Name of the user that last modified the stage
   * - ``name``
     - string`
     - Stage name
   * - ``category``
     - int
     - Stage category ID
   * - ``description``
     - string
     - Stage description
   * - ``weight``
     - int
     - Stage's weight
   * - ``publishUp``
     - datetime
     - Date/time stage should be published
   * - ``publishDown``
     - datetime
     - Date/time stage should be unpublished

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
     - Description
   * - ``name``
     - Stage name is the only required field
   * - ``weight``
     - int
   * - ``description``
     - A description of the stage.
   * - ``isPublished``
     - A value of 0 or 1


**Response**

``Expected Response Code: 201``

**Properties**

Same as `Get Stage <#get-stage>`_.

.. vale off

Edit Stage
************

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

Edit a new Stage. Note that this supports PUT or PATCH depending on the desired behavior.

**PUT** creates a stage if the given ID does not exist and clears all the stage information, adds the information from the request. 
**PATCH** fails if the stage with the given ID does not exist and updates the stage field values with the values form the request.

.. vale off

**HTTP Request**

.. vale on

To edit a Stage and return a 404 if the Stage isn't found:

``PATCH /stages/ID/edit``

To edit a Asset and create a new one if the Asset isn't found:

``PUT /stages/ID/edit``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - ``name``
     - Stage name is the only required field
   * - ``alias``
     - Name alias generated automatically if not set
   * - ``description``
     - A description of the stage.
   * - ``isPublished``
     - A value of 0 or 1.
   * - ``weight``
     - int

**Response**

If ``PUT``\ , the expected response code if editing the Asset is ``200`` or ``201`` if created.

If using ``PATCH``\ , the expected response code is ``200``.

**Properties**

Same as `Get Stage <#get-stage>`_.

.. vale off

Delete Stage
**************

.. vale on

.. code-block:: php

  <?php

  $stage = $stageApi->delete($id);

Delete a stage.

.. vale off

**HTTP Request**

.. vale on

``DELETE /stages/ID/delete``

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get Stage <#get-stage>`_.

.. vale off

Add Contact to a Stage
************************

.. vale on

.. code-block:: php

  <?php

  //...
  $response = $stageApi->addContact($stageId, $contactId);
  if (!isset($response['success'])) {
    // handle error
  }

Manually add a contact to a specific stage.

.. vale off

**HTTP Request**

.. vale on

``POST /stages/STAGE_ID/contact/CONTACT_ID/add``

**Response**

``Expected Response Code: 200``

.. code-block:: json
  {
    "success": true
  }


.. vale off

Remove Contact from a Stage
*****************************

.. vale on

.. code-block:: php

  <?php

  //...
  $response = $stageApi->removeContact($stageId, $contactId);
  if (!isset($response['success'])) {
    // handle error
  }

Manually remove a contact from a specific stage.

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