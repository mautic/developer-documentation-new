Stages
######

Use this endpoint to obtain details on Mautic's Contact Stages.

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
   $stageApi = $api->newApi("stages", $auth, $apiUrl);

.. vale off

Get Stage
*********

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
      "description": "This is my first Stage created via API.",
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
     - Published state
   * - ``dateAdded``
     - ``datetime``
     - Stage creation date/time
   * - ``createdBy``
     - int
     - ID of the User that created the Stage
   * - ``createdByUser``
     - string
     - Name of the User that created the Stage
   * - ``dateModified``
     - datetime/null
     - Date/time Stage was last modified
   * - ``modifiedBy``
     - int
     - ID of the User that last modified the Stage
   * - ``modifiedByUser``
     - string
     - Name of the User that last modified the Stage
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
     - Stage's weight
   * - ``publishUp``
     - ``datetime``
     - Stage publish date/time
   * - ``publishDown``
     - ``datetime``
     - Stage unpublish date/time

.. vale off

List Contact Stages
*******************

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
           "description": "This is my first Stage created via API.",
           "weight": 0,
           "publishUp": "2015-07-21T14:12:03-05:00",
           "publishDown": "2015-07-21T14:12:03-05:00"
       }
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
     - Count of all Stages
   * - ``id``
     - int
     - ID of the Stage
   * - ``isPublished``
     - boolean
     - Published state
   * - ``dateAdded``
     - ``datetime``
     - Stage creation date/time
   * - ``createdBy``
     - int
     - ID of the User that created the Stage
   * - ``createdByUser``
     - string
     - Name of the User that created the Stage
   * - ``dateModified``
     - datetime/null
     - Date/time Stage was last modified
   * - ``modifiedBy``
     - int
     - ID of the User that last modified the Stage
   * - ``modifiedByUser``
     - string
     - Name of the User that last modified the Stage
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
     - Stage's weight
   * - ``publishUp``
     - ``datetime``
     - Stage publish date/time
   * - ``publishDown``
     - ``datetime``
     - Stage unpublish date/time

.. vale off

Create Stage
************

.. vale on

.. code-block:: php

   <?php 

   $data = array(
       'name'        => 'Stage A',
       'weight'      => 5,
       'description' => 'This is my first Stage created via API.',
       'isPublished' => 1
   );

   $stage = $stageApi->create($data);

Create a new Stage.

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
     - string
     - Stage name is the only required field
   * - ``weight``
     - int
     - Stage's weight
   * - ``description``
     - string
     - A description of the Stage.
   * - ``isPublished``
     - int
     - A value of 0 or 1


**Response**

``Expected Response Code: 201``

**Properties**

Same as `Get Stage <#get-stage>`_.

.. vale off

Edit Stage
**********

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'name'        => 'New Stage name',
       'isPublished' => 0
   );

   // Create new a Stage of ID 1 isn't found?
   $createIfNotFound = true;

   $stage = $stageApi->edit($id, $data, $createIfNotFound);

Edit a new Stage. Note that this supports PUT or PATCH depending on the desired behavior.

**PUT** creates a Stage if the given ID doesn't exist and clears all the Stage information, adds the information from the request.
**PATCH** fails if the Stage with the given ID doesn't exist and updates the Stage field values with the values from the request.

.. vale off

**HTTP Request**

.. vale on

To edit a Stage and return a 404 if the Stage isn't found:

``PATCH /stages/ID/edit``

To edit a Stage and create a new one if the Stage isn't found:

``PUT /stages/ID/edit``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``name``
     - string
     - Stage name is the only required field
   * - ``alias``
     - string
     - Name alias generated automatically if not set
   * - ``description``
     - string
     - A description of the Stage.
   * - ``isPublished``
     - int
     - A value of 0 or 1
   * - ``weight``
     - int
     - Stage's weight


**Response**

If ``PUT``, the expected response code is ``200`` if editing a Stage or ``201`` if creating a new one.

If ``PATCH``, the expected response code is ``200``.

**Properties**

Same as `Get Stage <#get-stage>`_.

.. vale off

Delete Stage
************

.. vale on

.. code-block:: php

   <?php

   $stage = $stageApi->delete($id);

Delete a Stage.

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
**********************

.. vale on

.. code-block:: php

   <?php

   //...
   $response = $stageApi->addContact($stageId, $contactId);
   if (!isset($response['success'])) {
       // handle error
   }

Manually add a Contact to a specific Stage.

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
***************************

.. vale on

.. code-block:: php

   <?php

   //...
   $response = $stageApi->removeContact($stageId, $contactId);
   if (!isset($response['success'])) {
       // handle error
   }

.. code-block:: json

   {
       "success": true
   }

Manually remove a Contact from a specific Stage.

.. vale off

**HTTP Request**

.. vale on

``POST /stages/STAGE_ID/contact/CONTACT_ID/remove``

**Response**

``Expected Response Code: 200``

See JSON code example.
