.. vale off

Point Groups
############

.. vale on

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

.. vale off

Get Point Group
***************

.. vale on

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

.. vale off

**HTTP Request**

.. vale on

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
   * - ``id``
     - int
     - ID of the Point Group
   * - ``name``
     - ``string``
     - Point Group name
   * - ``description``
     - ``string``
     - Point Group description
   * - ``isPublished``
     - ``boolean``
     - Whether the Point Group is published
   * - ``dateAdded``
     - ``datetime``
     - Date/time Point Group was created
   * - ``createdBy``
     - ``int``
     - ID of the user that created the Point Group
   * - ``createdByUser``
     - ``string``
     - Name of the user that created the Point Group
   * - ``dateModified``
     - ``datetime/null``
     - Date/time Point Group was last modified
   * - ``modifiedBy``
     - ``int``
     - ID of the user that last modified the Point Group
   * - ``modifiedByUser``
     - ``string``
     - Name of the user that last modified the Point Group

.. vale off

List Contact Point Groups
*************************

.. vale on

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

.. vale off

**HTTP Request**

.. vale on


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
   * - ``total``
     - ``int``
     - Count of all Point Groups
   * - ``id``
     - ``int``
     - ID of the Point Group
   * - ``name``
     - ``string``
     - Point Group name
   * - ``description``
     - ``string``
     - Point Group description
   * - ``isPublished``
     - ``boolean``
     - Whether the Point Group is published
   * - ``dateAdded``
     - ``datetime``
     - Date/time Point Group was created
   * - ``createdBy``
     - ``int``
     - ID of the user that created the Point Group
   * - ``createdByUser``
     - ``string``
     - Name of the user that created the Point Group
   * - ``dateModified``
     - ``datetime/null``
     - Date/time Point Group was last modified
   * - ``modifiedBy``
     - ``int``
     - ID of the user that last modified the Point Group
   * - ``modifiedByUser``
     - ``string``
     - Name of the user that last modified the Point Group


.. vale off

Create Point Group
******************

.. vale on

.. code-block:: php

   <?php

   $data = [
       'name'        => 'Group A',
       'description' => 'This is my first Point Group created via API.'
   ];

   $pointGroup = $pointGroupApi->create($data);

.. vale off

**HTTP Request**

.. vale on


``POST /points/groups/new``

.. vale off

**Post Parameters**

.. vale on

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

.. vale off

Edit Point Group
****************

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = [
       'name'        => 'New Point Group name',
       'description' => 'Updated description of the Point Group.'
   ];

   $pointGroup = $pointGroupApi->edit($id, $data);

.. vale off

**HTTP Request**

.. vale on

``PATCH /points/groups/ID/edit``

.. vale off

**Post Parameters**

.. vale on

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

.. vale off

Delete Point Group
******************

.. vale on

.. code-block:: php

   <?php

   $pointGroup = $pointGroupApi->delete($id);

Delete a Point Group.

.. vale off

**HTTP Request**

.. vale on


``DELETE /points/groups/ID/delete``

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get Point Group`.