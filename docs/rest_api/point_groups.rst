Point Groups
############

Use this endpoint to manage Contact Point Groups in Mautic.

.. code-block:: php

   <?php
   use Mautic\MauticApi;
   use Mautic\Auth\ApiAuth;

   // ...
   $initAuth = new ApiAuth();
   $auth     = $initAuth->newAuth($settings);
   $apiUrl   = "https://your-mautic.com";
   $api      = new MauticApi();
   $pointGroupApi = $api->newApi("pointGroups", $auth, $apiUrl);

Get Point Group
***************

.. code-block:: php

   <?php

   //...
   $pointGroup = $pointGroupApi->get($id);

.. code-block:: json

    "pointGroup": {
        "id": 47,
        "name": "Group A",
        "description": "This is my first Point Group created via API.",
        "isPublished": true,
        "dateAdded": "2024-02-29T12:17:52+00:00",
        "dateModified": null,
        "createdBy": 2,
        "createdByUser": "Admin User",
        "modifiedBy": null,
        "modifiedByUser": null,
    }

Get an individual Point Group by ID.

**HTTP Request**

``GET /points/groups/ID``

**Response**

``Expected Response Code: 200``

See JSON code example.

**Point Group Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - id
     - int
     - ID of the Point Group
   * - name
     - string
     - Point Group name
   * - description
     - string
     - Point Group description
   * - isPublished
     - boolean
     - Whether the Point Group is published
   * - dateAdded
     - datetime
     - Date/time Point Group was created
   * - createdBy
     - int
     - ID of the user that created the Point Group
   * - createdByUser
     - string
     - Name of the user that created the Point Group
   * - dateModified
     - datetime/null
     - Date/time Point Group was last modified
   * - modifiedBy
     - int
     - ID of the user that last modified the Point Group
   * - modifiedByUser
     - string
     - Name of the user that last modified the Point Group

List Contact Point Groups
*************************

.. code-block:: php

   <?php

   //...
   $pointGroups = $pointGroupApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. code-block:: json

    {
      "total": 4,
      "pointGroups": [
        {
            "id": 47,
            "name": "Group A",
            "description": "This is my first Point Group created via API.",
            "isPublished": true,
            "dateAdded": "2024-02-29T12:17:52+00:00",
            "dateModified": null,
            "createdBy": 2,
            "createdByUser": "Admin User",
            "modifiedBy": null,
            "modifiedByUser": null
        },
        ...
      ]
    }

**HTTP Request**

``GET /points/groups``

**Response**

``Expected Response Code: 200``

See JSON code example.

**Point Group Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - total
     - int
     - Count of all Point Groups
   * - id
     - int
     - ID of the Point Group
   * - name
     - string
     - Point Group name
   * - description
     - string
     - Point Group description
   * - isPublished
     - boolean
     - Whether the Point Group is published
   * - dateAdded
     - datetime
     - Date/time Point Group was created
   * - createdBy
     - int
     - ID of the user that created the Point Group
   * - createdByUser
     - string
     - Name of the user that created the Point Group
   * - dateModified
     - datetime/null
     - Date/time Point Group was last modified
   * - modifiedBy
     - int
     - ID of the user that last modified the Point Group
   * - modifiedByUser
     - string
     - Name of the user that last modified the Point Group

Create Point Group
******************

.. code-block:: php

   <?php

   $data = [
       'name'        => 'Group A',
       'description' => 'This is my first Point Group created via API.'
   ];

   $pointGroup = $pointGroupApi->create($data);

Create a new Point Group.

**HTTP Request**

``POST /points/groups/new``

**Post Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - name
     - Point Group name is the only required field
   * - description
     - A description of the Point Group.

**Response**

``Expected Response Code: 201``

**Properties**

Same as `Get Point Group`.

Edit Point Group
****************

.. code-block:: php

   <?php

   $id   = 1;
   $data = [
       'name'        => 'New Point Group name',
       'description' => 'Updated description of the Point Group.'
   ];

   $pointGroup = $pointGroupApi->edit($id, $data);

Edit a Point Group.

**HTTP Request**

``PATCH /points/groups/ID/edit``

**Post Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - name
     - Point Group name is the only required field
   * - description
     - A description of the Point Group.

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get Point Group`.

Delete Point Group
******************

.. code-block:: php

   <?php

   $pointGroup = $pointGroupApi->delete($id);

Delete a Point Group.

**HTTP Request**

``DELETE /points/groups/ID/delete``

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get Point Group`.