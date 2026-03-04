Users
#####

Use this endpoint to manipulate and obtain details on Mautic's Users.

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
   $userApi  = $api->newApi("users", $auth, $apiUrl);

.. vale off

Get User
********

.. vale on

Retrieves an individual User.

.. code-block:: php

   <?php

   //...
   $user = $userApi->get($id);

.. vale off

HTTP request
============

.. vale on

``GET /users/ID``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the User.

.. _get User response:

.. code-block:: json

   {
      "user": {
          "isPublished": true,
          "dateAdded": "2026-02-21T05:19:56+00:00",
          "dateModified": "2026-02-21T05:20:13+00:00",
          "createdBy": 1,
          "createdByUser": "Admin Mautic",
          "modifiedBy": 1,
          "modifiedByUser": "Admin Mautic",
          "id": 3,
          "username": "r.green",
          "firstName": "Rachel",
          "lastName": "Green",
          "email": "rachel.green@acme.com",
          "position": "Marketing Staff",
          "role": {
              "createdByUser": "Admin Mautic",
              "modifiedByUser": null,
              "id": 2,
              "name": "Email Permissions",
              "description": null,
              "isAdmin": false,
              "rawPermissions": {
                  "email:categories": [
                      "full"
                  ],
                  "email:emails": [
                      "full"
                  ]
              }
          },
          "timezone": "Europe/Paris",
          "locale": null,
          "lastLogin": "2026-02-22T04:28:00+00:00",
          "lastActive": "2026-02-22T04:28:00+00:00",
          "signature": "Best regards, \r\nRachel Green"
      }
   }

.. _get User properties:

User properties
===============

.. vale off

.. list-table:: 
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``isPublished``
     - boolean
     - User publication status
   * - ``dateAdded``
     - datetime
     - User record creation date and time
   * - ``dateModified``
     - datetime
     - User record last modification date and time
   * - ``createdBy``
     - integer
     - ID of the User who created the User record
   * - ``createdByUser``
     - string
     - Name of the User who created the User record
   * - ``modifiedBy``
     - integer
     - ID of the User who last modified the User record
   * - ``modifiedByUser``
     - string
     - Name of the User who last modified the User record
   * - ``id``
     - integer
     - ID of the User
   * - ``username``
     - string
     - Username for login - **unique**
   * - ``firstName``
     - string
     - First name of the User
   * - ``lastName``
     - string
     - Last name of the User
   * - ``email``
     - string
     - Email address of the User - **unique**
   * - ``position``
     - string
     - Job position or title of the User
   * - ``role``
     - object
     - The Role and permissions assigned to the User. Refer to :ref:`User Role properties <get User Role properties>` for details
   * - ``timezone``
     - string
     - Timezone preference of the User
   * - ``locale``
     - string
     - Language or locale preference of the User
   * - ``lastLogin``
     - datetime
     - Date and time of the last login
   * - ``lastActive``
     - datetime
     - Date and time of the last activity
   * - ``signature``
     - string
     - Email signature in HTML format

.. _get User Role properties:

User Role properties
--------------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``isPublished``
     - boolean
     - Role publication status
   * - ``dateAdded``
     - datetime
     - Role record creation date and time
   * - ``dateModified``
     - datetime
     - Role record last modification date and time
   * - ``createdBy``
     - integer
     - ID of the User who created the Role record
   * - ``createdByUser``
     - string
     - Name of the User who created the Role record
   * - ``modifiedBy``
     - integer
     - ID of the User who last modified the Role record
   * - ``modifiedByUser``
     - string
     - Name of the User who last modified the Role record
   * - ``id``
     - integer
     - ID of the Role
   * - ``name``
     - string
     - Name of the Role
   * - ``description``
     - string
     - Description of the Role
   * - ``isAdmin``
     - boolean
     - Admin status - ``true`` if the Role has full system access
   * - ``rawPermissions``
     - object
     - A collection of granular permission sets for Mautic bundles

.. vale off

List Users
**********

.. vale on

Retrieves a list of Users.

.. code-block:: php

   <?php

   //...
   $users = $userApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

HTTP request
============

.. vale on

``GET /users``

Query parameters
----------------

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``searchFilter``
     - string
     - String or search command to filter entities
   * - ``start``
     - integer
     - Starting row for the returned entities - defaults to 0
   * - ``limit``
     - integer
     - Maximum number of entities to return - defaults to 30
   * - ``orderBy``
     - string
     - Column to sort by. Any column in the response is valid.
       
       **Note**: convert ``camelCase`` properties to ``snake_case``. For example, ``dateAdded`` becomes ``date_added``, ``webhookUrl`` becomes ``webhook_url``, and so on
   * - ``orderByDir``
     - string
     - Order direction - ``asc`` or ``desc``
   * - ``publishedOnly``
     - boolean
     - Returns only currently published entities
   * - ``minimal``
     - boolean
     - Returns only a simple mapped object of entities without additional lists in it

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Users list.

.. code-block:: json

   {
      "total": 3,
      "users": [
          {
              "isPublished": true,
              "dateAdded": "2026-02-21T05:19:56+00:00",
              "dateModified": "2026-02-21T05:20:13+00:00",
              "createdBy": 1,
              "createdByUser": "Admin Mautic",
              "modifiedBy": 1,
              "modifiedByUser": "Admin Mautic",
              "id": 3,
              "username": "r.green",
              "firstName": "Rachel",
              "lastName": "Green",
              "email": "rachel.green@acme.com",
              "position": "Marketing Staff",
              "role": {
                  "createdByUser": "Admin Mautic",
                  "modifiedByUser": null,
                  "id": 2,
                  "name": "Email Permissions",
                  "description": null,
                  "isAdmin": false,
                  "rawPermissions": {
                      "email:categories": [
                          "full"
                      ],
                      "email:emails": [
                          "full"
                      ]
                  }
              },
              "timezone": "Europe/Paris",
              "locale": null,
              "lastLogin": "2026-02-22T04:28:00+00:00",
              "lastActive": "2026-02-22T04:28:00+00:00",
              "signature": "Best regards, \r\nRachel Green"
          },
          // ...
      ]
   }

Properties
----------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``total``
     - integer
     - Total count of Users
   * - ``users``
     - array
     - Array of Users

.. vale off

For the rest of the properties, refer to :ref:`User properties <get User properties>`.

.. vale on

.. vale off

Create User
***********

.. vale on

Creates a new User.

.. code-block:: php

   <?php

   $data = array(
       'firstName'     => 'John',                 // Required
       'lastName'      => 'Doe',                  // Required
       'username'      => 'newuser',              // Required
       'email'         => 'john.doe@example.com', // Required
       'plainPassword' => array(                  // Required
           'password' => 'SecurePassword123!',
           'confirm'  => 'SecurePassword123!'
       ),
       'role'          => 1,                      // Required
       'timezone'      => 'America/New_York',     // Required
       'locale'        => 'en_US',                // Required
       'position'      => 'Marketing Specialist',
   );

   $user = $userApi->create($data);

.. vale off

HTTP request
============

.. vale on

``POST /users/new``

.. _create User POST parameters:

POST parameters
---------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``firstName``
     - string
     - **Required.**
       
       First name of the User
   * - ``lastName``
     - string
     - **Required.**
       
       Last name of the User
   * - ``username``
     - string
     - **Required. Must be unique.**
       
       Username for login
   * - ``email``
     - string
     - **Required. Must be unique.**
       
       Email address of the User
   * - ``plainPassword``
     - array
     - **Required.**
       
       Array containing ``password`` and ``confirm`` keys
   * - ``role``
     - integer
     - **Required.**
       
       ID of the Role assigned to the User
   * - ``timezone``
     - string
     - **Required.**
       
       Timezone preference of the User
   * - ``locale``
     - string
     - **Required.**
       
       Language or locale preference of the User
   * - ``isPublished``
     - boolean
     - User publication status. Set to ``0`` or ``false`` to turn off the User account - defaults to ``1``
   * - ``position``
     - string
     - Job position or title
   * - ``signature``
     - string
     - Email signature in HTML format

Response
========

* Returns ``201 Created`` when the request successfully creates a User.

The response is a JSON object similar to :ref:`Get User <get User response>`.

Properties
----------

Refer to :ref:`User properties <get User properties>`.

.. vale off

Edit User
*********

.. vale on

Edits a User. 

This operation supports ``PUT`` or ``PATCH`` depending on the desired behavior:

* ``PUT``: **full replacement**. The request creates a new User if the ID is missing. If the ID exists, the request clears all existing data and replaces it with the provided values.
* ``PATCH``: **partial update**. The request only updates field values based on the request data. The request fails when the User ID doesn't exist.

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'firstName' => 'John Updated',
       'position'  => 'Senior Marketing Specialist',
       'timezone'  => 'Europe/London'
   );

   // Create a new User if ID 1 isn't found
   $createIfNotFound = true;

   $user = $userApi->edit($id, $data, $createIfNotFound);

.. vale off

HTTP request
============

.. vale on

* ``PUT /users/ID/edit``: updates an existing User or creates a new one when the ID doesn't exist.
* ``PATCH /users/ID/edit``: updates an existing User. The request fails when the ID doesn't exist.

POST parameters
---------------

Accepts the same parameters as those described in :ref:`Create User <create User POST parameters>`. All parameters are optional.

Response
========

* ``PUT``: returns ``200 OK`` when the request successfully updates the User or ``201 Created`` when the request creates a User.
* ``PATCH``: returns ``200 OK`` when the request successfully updates the User or ``404 Not Found`` error when the User ID doesn't exist.

The response is a JSON object similar to :ref:`Get User <get User response>`.

Properties
----------

Refer to :ref:`User properties <get User properties>`.

.. vale off

Delete User
***********

.. vale on

Deletes a User.

.. code-block:: php

   <?php

   $user = $userApi->delete($id);

.. vale off

HTTP request
============

.. vale on

``DELETE /users/ID``

Response
========

* Returns ``200 OK`` when the request successfully deletes the User.

The response is a JSON object containing the data of the deleted User, similar to :ref:`Get User <get User response>`.

Properties
----------

Refer to :ref:`User properties <get User properties>`.

.. vale off

Get current User
****************

.. vale on

Retrieves the profile data of the User associated with the current API credentials.

.. code-block:: php

   <?php

   $currentUser = $userApi->getSelf();

.. vale off

HTTP request
============

.. vale on

``GET /users/self``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the User's information.

.. code-block:: json

   {
      "isPublished": true,
      "dateAdded": "2026-02-21T05:19:56+00:00",
      "dateModified": "2026-02-21T05:20:13+00:00",
      "createdBy": 1,
      "createdByUser": "Admin Mautic",
      "modifiedBy": 1,
      "modifiedByUser": "Admin Mautic",
      "id": 3,
      "username": "r.green",
      "firstName": "Rachel",
      "lastName": "Green",
      "email": "rachel.green@acme.com",
      "position": "Marketing Staff",
      "role": {
          "isPublished": true,
          "dateAdded": "2026-02-21T05:18:04+00:00",
          "dateModified": "2026-02-23T04:02:22+00:00",
          "createdBy": 1,
          "createdByUser": "Admin Mautic",
          "modifiedBy": 1,
          "modifiedByUser": "John Doe",
          "id": 2,
          "name": "Email Permissions",
          "isAdmin": false,
          "rawPermissions": {
              "asset:categories": [
                  "view",
                  "edit",
                  "create",
                  "delete"
              ],
              "asset:assets": [
                  "viewown",
                  "editown",
                  "create",
                  "deleteown"
              ],
              "email:categories": [
                  "full"
              ],
              "email:emails": [
                  "full"
              ],
              "mauticSocial:categories": [
                  "full"
              ],
              "mauticSocial:monitoring": [
                  "full"
              ],
              "mauticSocial:tweets": [
                  "viewown",
                  "editown",
                  "create",
                  "deleteown",
                  "publishown"
              ]
          }
      },
      "timezone": "Europe/Paris",
      "lastLogin": "2026-02-25T08:24:46+00:00",
      "lastActive": "2026-02-25T08:24:46+00:00",
      "signature": "Best regards, \r\nRachel Green"
   }

.. vale off

Current User properties
=======================

.. vale on

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``isPublished``
     - boolean
     - User publication status
   * - ``dateAdded``
     - datetime
     - User record creation date and time
   * - ``dateModified``
     - datetime
     - User record last modification date and time
   * - ``createdBy``
     - integer
     - ID of the User who created the User record
   * - ``createdByUser``
     - string
     - Name of the User who created the User record
   * - ``modifiedBy``
     - integer
     - ID of the User who last modified the User record
   * - ``modifiedByUser``
     - string
     - Name of the User who last modified the User record
   * - ``id``
     - integer
     - ID of the User
   * - ``username``
     - string
     - Username for login - **unique**
   * - ``firstName``
     - string
     - First name of the User
   * - ``lastName``
     - string
     - Last name of the User
   * - ``email``
     - string
     - Email address of the User - **unique**
   * - ``position``
     - string
     - Job position or title of the User
   * - ``role``
     - object
     - The Role and permissions assigned to the User
   * - ``timezone``
     - string
     - Timezone preference of the User
   * - ``lastLogin``
     - datetime
     - Date and time of the last login
   * - ``lastActive``
     - datetime
     - Date and time of the last activity
   * - ``signature``
     - string
     - Email signature in HTML format

.. vale off

Current User Role properties
----------------------------

.. vale on

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``isPublished``
     - boolean
     - Role publication status
   * - ``dateAdded``
     - datetime
     - Role record creation date and time
   * - ``dateModified``
     - datetime
     - Role record last modification date and time
   * - ``createdBy``
     - integer
     - ID of the User who created the Role record
   * - ``createdByUser``
     - string
     - Name of the User who created the Role record
   * - ``modifiedBy``
     - integer
     - ID of the User who last modified the Role record
   * - ``modifiedByUser``
     - string
     - Name of the User who last modified the Role record
   * - ``id``
     - integer
     - ID of the Role
   * - ``name``
     - string
     - Name of the Role
   * - ``description``
     - string
     - Description of the Role
   * - ``isAdmin``
     - boolean
     - Admin status - ``true`` if the Role has full system access
   * - ``rawPermissions``
     - object
     - A collection of granular permission sets for Mautic bundles

.. vale off

Verify User permissions
***********************

.. vale on

Verifies if a User has specific permissions.

.. code-block:: php

   <?php

   $permissions = array('user:users:view', 'user:users:edit'); // Required
   $result = $userApi->checkPermission($userId, $permissions);

.. vale off

HTTP request
============

.. vale on

``POST /users/ID/permissioncheck``

POST parameters
---------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``permissions``
     - array
     - **Required**.
       
       Array of permission strings to verify

Response
========

* Returns ``200 OK`` when the request successfully verifies the User.

.. code-block:: json

   {
      "user:users:view": true,
      "user:users:edit": true
   }

Properties
----------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``bundle:group:action``
     - boolean
     - Permission status - ``true`` indicates the User has the permission

.. note::

   * ``bundle``: the Mautic bundle name - for example, ``user``, ``email``, ``asset``, and so on.
   * ``group``: the functional group within the bundle - for example, ``users``, ``roles``, ``forms``, and so on.
   * ``action``: the specific operation - for example, ``view``, ``edit``, ``create``, ``delete``, or ``full``.

.. vale off

List User Roles
***************

.. vale on

Retrieves all available User Roles.

.. code-block:: php

   <?php

   $roles = $userApi->getRoles();

.. vale off

HTTP request
============

.. vale on

``GET /users/list/roles``

Query parameters
----------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Name
     - Description
   * - ``filter``
     - String to filter Roles by name
   * - ``limit``
     - Limit number of Roles to return

Response
========

* Returns ``200 OK`` when the request successfully retrieves the list of User Roles.

.. code-block:: json

   [
      {
          "id": 1,
          "name": "Administrator"
      },
      {
          "id": 2,
          "name": "Email Permissions"
      }
   ]

Properties
----------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - integer
     - ID of the Role
   * - ``name``
     - string
     - Name assigned to the Role

Error responses
***************

Common error responses
======================

.. vale off

.. list-table::
   :widths: 20 30 50
   :header-rows: 1

   * - HTTP code
     - Error status
     - Description
   * - ``400``
     - Bad Request
     - Indicates invalid JSON syntax or failed field validation. Examples include missing required fields, weak passwords, or duplicate usernames.
   * - ``401``
     - Unauthorized
     - Authentication required or weak password detected
   * - ``403``
     - Forbidden
     - Insufficient permissions to perform this action
   * - ``404``
     - Not Found
     - User with the specified ID not found
   * - ``500``
     - Internal server error
     - An unexpected error occurred, often due to an invalid data format in the request body

.. vale on

Password validation error
=========================

Password validation error during User creation or updates:

.. code-block:: json

   {
      "errors": [
          {
              "code": 400,
              "message": "password: Please enter a stronger password. Your password must use a combination of upper and lower case, special characters and numbers.",
              "details": {
                  "password": [
                    "Please enter a stronger password. Your password must use a combination of upper and lower case, special characters and numbers."
                  ]
              }
          }
      ]
   }

Permission error
================

Permission error for non-existent Users:

.. code-block:: json

   {
      "errors": [
          {
              "code": 404,
              "message": "Item was not found.",
              "details": []
          }
      ]
   }

Role assignment error
=====================

Error when assigning User's Role:

.. code-block:: json

   {
      "errors": [
          {
              "code": 400,
              "message": "role: This value is not valid.",
              "details": {
                  "role": [
                      "This value is not valid."
                  ]
              }
          }
      ]
   }
