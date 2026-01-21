Stages
######

Use this endpoint to obtain details on Mautic's Contact Stages.

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
***********

Get an individual Stage.

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

* Returns ``200`` when the request successfully gets a Stage.

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
     - Stage creation date and time
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

Get a list of Stages.

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

* Returns ``200`` when the request successfully gets the list of Stages.

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
       }
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
     - Stage creation date and time
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

Create a new Stage.

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

* Returns ``201`` when the request successfully creates a Stage.

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
     - Stage creation date and time
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

Edit a Stage. This operation supports ``PUT`` or ``PATCH`` depending on the desired behavior:

* ``PUT``: creates a Stage when the ID doesn't exist. If the ID exists, the request clears the Stage data and adds the request values.
* ``PATCH``: updates field values for an existing Stage using the request data. The request fails when the ID doesn't exist.

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

* ``PATCH /stages/ID/edit``: edits an existing Stage. The request fails with a 404 error when the ID doesn't exist.
* ``PUT /stages/ID/edit``: edits an existing Stage or creates a new one when the ID doesn't exist.

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
     - Stage description
   * - ``isPublished``
     - boolean
     - Stage publication status
   * - ``weight``
     - int
     - Stage weight

Response
========

* ``PUT``: returns ``200`` when the request successfully edits a Stage or ``201`` when the request creates a Stage.
* ``PATCH``: returns ``200`` when the request successfully edits a Stage.

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
     - Stage creation date and time
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

Delete a Stage.

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

* Returns ``200`` when the request successfully deletes a Stage.

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
     - Stage creation date and time
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

Add a Contact to a Stage manually.

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

* Returns ``200`` when the request successfully adds the Contact to the Stage.

.. code-block:: json

   {
     "success": true
   }

.. vale off

Remove Contact from a Stage
***************************

.. vale on

Remove a Contact from a Stage manually.

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

* Returns ``200`` when the request successfully removes the Contact from the Stage.

.. code-block:: json

   {
     "success": true
   }