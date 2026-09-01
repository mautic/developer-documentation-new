Roles
#####

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Use this endpoint to obtain details on Mautic's Roles.

.. code-block:: php

   <?php
   use Mautic\MauticApi;
   use Mautic\Auth\ApiAuth;

   // ...
   $initAuth = new ApiAuth();
   $auth     = $initAuth->newAuth($settings);
   $apiUrl   = "https://your-mautic.com";
   $api      = new MauticApi();
   $roleApi  = $api->newApi("roles", $auth, $apiUrl);

.. vale off

Get Role
********

.. vale on

.. code-block:: php

   <?php

   //...
   $role = $roleApi->get($id);

.. code-block:: json

   {
     "role": {
       "isPublished": true,
       "dateAdded": "2016-11-09T15:24:32+00:00",
       "createdBy": 1,
       "createdByUser": "John Doe",
       "dateModified": null,
       "modifiedBy": null,
       "modifiedByUser": null,
       "id": 13,
       "name": "API test role",
       "description": "created via API",
       "isAdmin": false,
       "rawPermissions": {
         "email:emails": [
           "viewown",
           "viewother"
         ]
       }
     }
   }

Get an individual Role by ID.

.. vale off

**HTTP Request**

.. vale on

``GET /roles/ID``

**Response**

``Expected Response Code: 200``

See JSON code example.

**Role Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - ``int``
     - ID of the Role
   * - ``name``
     - ``string``
     - Role name
   * - ``description``
     - ``string``
     - Role description
   * - ``isPublished``
     - ``boolean``
     - Whether the Role is published
   * - ``isAdmin``
     - ``boolean``
     - Whether the Role has full access or only specific permissions
   * - ``rawPermissions``
     - ``array``
     - Permissions granted to the Role, keyed by bundle and permission name
   * - ``dateAdded``
     - ``datetime``
     - Date/time the Role was created
   * - ``createdBy``
     - ``int``
     - ID of the User that created the Role
   * - ``createdByUser``
     - ``string``
     - Name of the User that created the Role
   * - ``dateModified``
     - ``datetime/null``
     - Date/time the Role was last modified
   * - ``modifiedBy``
     - ``int``
     - ID of the User that last modified the Role
   * - ``modifiedByUser``
     - ``string``
     - Name of the User that last modified the Role

.. vale off

List Roles
**********

.. vale on

.. code-block:: php

   <?php

   //...
   $roles = $roleApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. code-block:: json

   {
     "total": 9,
     "roles": [
       {
         "isPublished": true,
         "dateAdded": "2016-08-01T11:51:32+00:00",
         "createdBy": 1,
         "createdByUser": "John Doe",
         "dateModified": null,
         "modifiedBy": null,
         "modifiedByUser": null,
         "id": 2,
         "name": "view email",
         "description": null,
         "isAdmin": false,
         "rawPermissions": {
           "email:emails": [
             "viewown",
             "viewother"
           ]
         }
       },
       ...
     ]
   }

.. vale off

**HTTP Request**

.. vale on

``GET /roles``

**Response**

``Expected Response Code: 200``

See JSON code example.

**Role Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``total``
     - ``int``
     - Count of all Roles
   * - ``id``
     - ``int``
     - ID of the Role
   * - ``name``
     - ``string``
     - Role name
   * - ``description``
     - ``string``
     - Role description
   * - ``isPublished``
     - ``boolean``
     - Whether the Role is published
   * - ``isAdmin``
     - ``boolean``
     - Whether the Role has full access or only specific permissions
   * - ``rawPermissions``
     - ``array``
     - Permissions granted to the Role, keyed by bundle and permission name
   * - ``dateAdded``
     - ``datetime``
     - Date/time the Role was created
   * - ``createdBy``
     - ``int``
     - ID of the User that created the Role
   * - ``createdByUser``
     - ``string``
     - Name of the User that created the Role
   * - ``dateModified``
     - ``datetime/null``
     - Date/time the Role was last modified
   * - ``modifiedBy``
     - ``int``
     - ID of the User that last modified the Role
   * - ``modifiedByUser``
     - ``string``
     - Name of the User that last modified the Role

.. vale off

Create Role
***********

.. vale on

.. code-block:: php

   <?php

   $data = [
       'name'           => 'API test role',
       'description'    => 'created via API',
       'rawPermissions' => [
           'email:emails' => [
               'viewown',
               'viewother',
           ],
       ],
   ];

   $role = $roleApi->create($data);

Create a new Role.

.. vale off

**HTTP Request**

.. vale on

``POST /roles/new``

.. vale off

**Post Parameters**

.. vale on

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``name``
     - ``string``
     - Role name is the only required field
   * - ``description``
     - ``string``
     - Role description
   * - ``isAdmin``
     - ``boolean``
     - Whether the Role has full access or only specific permissions
   * - ``rawPermissions``
     - ``array``
     - Permissions granted to the Role, keyed by bundle and permission name

**Response**

``Expected Response Code: 201``

**Properties**

Same as `Get Role`.

.. vale off

Edit Role
*********

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = [
       'name'           => 'API test role',
       'description'    => 'created via API',
       'rawPermissions' => [
           'email:emails' => [
               'editown',
               'editother',
           ],
       ],
   ];

   // Create a new Role if the Role with the given ID isn't found?
   $createIfNotFound = true;

   $role = $roleApi->edit($id, $data, $createIfNotFound);

Edit a Role. This endpoint supports ``PUT`` or ``PATCH`` depending on the desired behavior.

``PUT`` creates the Role if the given ID doesn't exist, clears all Role information, and applies the values from the request.

``PATCH`` fails if the Role with the given ID doesn't exist, and updates the Role's field values with the values from the request.

.. vale off

**HTTP Request**

.. vale on

To edit a Role and return an ``HTTP 404 (Not Found)`` if the Role isn't found:

``PATCH /roles/ID/edit``

To edit a Role and create a new one if the Role isn't found:

``PUT /roles/ID/edit``

.. vale off

**Post Parameters**

.. vale on

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``name``
     - ``string``
     - Role name is the only required field
   * - ``description``
     - ``string``
     - Role description
   * - ``isAdmin``
     - ``boolean``
     - Whether the Role has full access or only specific permissions
   * - ``rawPermissions``
     - ``array``
     - Permissions granted to the Role, keyed by bundle and permission name

**Response**

If ``PUT``, the expected response code is ``200`` if the Role was edited or ``201`` if created.

If ``PATCH``, the expected response code is ``200``.

**Properties**

Same as `Get Role`.

.. vale off

Delete Role
***********

.. vale on

.. code-block:: php

   <?php

   $role = $roleApi->delete($id);

Delete a Role.

.. vale off

**HTTP Request**

.. vale on

``DELETE /roles/ID/delete``

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get Role`.
