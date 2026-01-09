Users
#####

Use this endpoint to manipulate and obtain details on Mautic's Users.

**Using Mautic's API Library**

You can interact with this API through the :xref:`Mautic API Library` as follows, or use the various http endpoints as described in this document.

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

.. code-block:: php

   <?php

   //...
   $user = $userApi->get($id);

Get an individual User by ID.

.. vale off

**HTTP Request**

.. vale on

``GET /users/ID``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "user": {
           "id": 1,
           "dateAdded": "2024-01-15T10:30:00+00:00",
           "dateModified": "2024-02-20T14:45:00+00:00",
           "createdBy": 1,
           "createdByUser": "System Administrator",
           "modifiedBy": 1,
           "modifiedByUser": "System Administrator",
           "username": "admin",
           "firstName": "John",
           "lastName": "Doe",
           "email": "john.doe@example.com",
           "position": "System Administrator",
           "timezone": "America/New_York",
           "locale": "en_US",
           "lastLogin": "2024-02-20T09:15:00+00:00",
           "lastActive": "2024-02-20T14:45:00+00:00",
           "role": {
               "id": 1,
               "name": "Administrator",
               "description": "Full system access",
               "isAdmin": true
           },
           "preferences": {
               "theme": "default",
               "language": "en_US"
           },
           "signature": "<p>Best regards,<br>John Doe</p>"
       }
   }

**User Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the User
   * - ``username``
     - string
     - Username for login (unique)
   * - ``firstName``
     - string
     - User's first name
   * - ``lastName``
     - string
     - User's last name
   * - ``email``
     - string
     - User's email address (unique)
   * - ``position``
     - string
     - User's job position/title
   * - ``timezone``
     - string
     - User's timezone preference
   * - ``locale``
     - string
     - User's language/locale preference
   * - ``lastLogin``
     - datetime
     - Timestamp of user's last login
   * - ``lastActive``
     - datetime
     - Timestamp of user's last activity
   * - ``role``
     - object
     - User's assigned role with permissions
   * - ``preferences``
     - array
     - User's system preferences
   * - ``signature``
     - string
     - User's email signature (HTML)
   * - ``dateAdded``
     - datetime
     - Date/time when the User was created
   * - ``dateModified``
     - datetime
     - Date/time when the User was last modified
   * - ``createdBy``
     - int
     - ID of the User who created this User
   * - ``modifiedBy``
     - int
     - ID of the User who last modified this User

.. vale off

List Users
**********

.. vale on

.. code-block:: php

   <?php

   //...
   $users = $userApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

Get a list of Users.

.. vale off

**HTTP Request**

.. vale on

``GET /users``

**Query Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - ``search``
     - String or search command to filter entities by.
   * - ``start``
     - Starting row for the entities returned. Defaults to 0.
   * - ``limit``
     - Limit number of entities to return. Defaults to the system configuration for pagination (30).
   * - ``orderBy``
     - Column to sort by. Can use any column listed in the response.
   * - ``orderByDir``
     - Sort direction: ``asc`` or ``desc``.
   * - ``publishedOnly``
     - Only return currently published entities.
   * - ``minimal``
     - Return only array of entities without additional lists in it.

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "total": 2,
       "users": [
           {
               "id": 1,
               "username": "admin",
               "firstName": "John",
               "lastName": "Doe",
               "email": "john.doe@example.com",
               "position": "System Administrator",
               "role": {
                   "id": 1,
                   "name": "Administrator"
               }
           },
           {
               "id": 2,
               "username": "manager",
               "firstName": "Jane",
               "lastName": "Smith",
               "email": "jane.smith@example.com",
               "position": "Marketing Manager",
               "role": {
                   "id": 2,
                   "name": "Manager"
               }
           }
       ]
   }

.. vale off

Create User
***********

.. vale on

.. code-block:: php

   <?php

   $data = array(
       'username'      => 'newuser',
       'firstName'     => 'John',
       'lastName'      => 'Doe',
       'email'         => 'john.doe@example.com',
       'plainPassword' => array(
           'password' => 'SecurePassword123!',
           'confirm'  => 'SecurePassword123!'
       ),
       'role'          => 1,
       'position'      => 'Marketing Specialist',
       'timezone'      => 'America/New_York',
       'locale'        => 'en_US'
   );

   $user = $userApi->create($data);

Create a new User.

.. vale off

**HTTP Request**

.. vale on

``POST /users/new``

**Post Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``username``
     - string
     - **Required.** Username for login (must be unique)
   * - ``firstName``
     - string
     - **Required.** User's first name
   * - ``lastName``
     - string
     - **Required.** User's last name
   * - ``email``
     - string
     - **Required.** User's email address (must be unique)
   * - ``plainPassword``
     - array
     - **Required.** Array with 'password' and 'confirm' keys
   * - ``role``
     - int
     - **Required.** ID of the role to assign to the user
   * - ``position``
     - string
     - User's job position/title
   * - ``timezone``
     - string
     - User's timezone preference
   * - ``locale``
     - string
     - User's language/locale preference
   * - ``signature``
     - string
     - User's email signature (HTML)

**Response**

``Expected Response Code: 201``

.. code-block:: json

   {
       "user": {
           "id": 3,
           "username": "newuser",
           "firstName": "John",
           "lastName": "Doe",
           "email": "john.doe@example.com",
           "position": "Marketing Specialist",
           "timezone": "America/New_York",
           "locale": "en_US",
           "role": {
               "id": 1,
               "name": "Administrator"
           },
           "dateAdded": "2024-02-20T15:30:00+00:00",
           "createdBy": 1,
           "createdByUser": "System Administrator"
       }
   }

.. vale off

Edit User
*********

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'firstName' => 'John Updated',
       'position'  => 'Senior Marketing Specialist',
       'timezone'  => 'Europe/London'
   );

   // Create new a User if one isn't found with the given ID
   $createIfNotFound = true;

   $user = $userApi->edit($id, $data, $createIfNotFound);

Edit an existing User. Note that this supports PUT or PATCH depending on the desired behavior.

- **PUT** creates a User if the given ID does not exist and clears all the User information, adds the information from the request. User username and password cannot be changed via PUT.
- **PATCH** fails if the User with the given ID does not exist and updates the User field values with the values from the request. User username and password cannot be changed via PATCH.

.. vale off

**HTTP Request**

.. vale on

To edit a User and return a 404 if the User is not found:

``PATCH /users/ID/edit``

To edit a User and create a new one if the User is not found:

``PUT /users/ID/edit``

**Post Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``firstName``
     - string
     - User's first name
   * - ``lastName``
     - string
     - User's last name
   * - ``email``
     - string
     - User's email address (must be unique)
   * - ``role``
     - int
     - ID of the role to assign to the user
   * - ``position``
     - string
     - User's job position/title
   * - ``timezone``
     - string
     - User's timezone preference
   * - ``locale``
     - string
     - User's language/locale preference
   * - ``signature``
     - string
     - User's email signature (HTML)

**Response**

If ``PUT``: ``Expected Response Code: 200`` (if the User was edited) or ``201`` (if the User was created).

If ``PATCH``: ``Expected Response Code: 200``

.. code-block:: json

   {
       "user": {
           "id": 1,
           "username": "admin",
           "firstName": "John Updated",
           "lastName": "Doe",
           "email": "john.doe@example.com",
           "position": "Senior Marketing Specialist",
           "timezone": "Europe/London",
           "role": {
               "id": 1,
               "name": "Administrator"
           },
           "dateModified": "2024-02-20T16:00:00+00:00",
           "modifiedBy": 1,
           "modifiedByUser": "System Administrator"
       }
   }

.. vale off

Delete User
***********

.. vale on

.. code-block:: php

   <?php

   $user = $userApi->delete($id);

Delete a User.

.. vale off

**HTTP Request**

.. vale on

``DELETE /users/ID``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "user": {
           "id": 3,
           "username": "deleteduser",
           "firstName": "John",
           "lastName": "Doe",
           "email": "john.doe@example.com"
       }
   }

.. vale off

Get Current User
****************

.. vale on

.. code-block:: php

   <?php

   $currentUser = $userApi->getSelf();

Get the currently authenticated User's information.

.. vale off

**HTTP Request**

.. vale on

``GET /users/self``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "id": 1,
       "username": "admin",
       "firstName": "John",
       "lastName": "Doe",
       "email": "john.doe@example.com",
       "position": "System Administrator",
       "timezone": "America/New_York",
       "locale": "en_US",
       "lastLogin": "2024-02-20T09:15:00+00:00",
       "lastActive": "2024-02-20T14:45:00+00:00",
       "role": {
           "id": 1,
           "name": "Administrator",
           "isAdmin": true
       }
   }

.. vale off

Check User Permissions
**********************

.. vale on

.. code-block:: php

   <?php

   $permissions = array('user:users:view', 'user:users:edit');
   $result = $userApi->checkPermission($userId, $permissions);

Check if a User has specific permissions.

.. vale off

**HTTP Request**

.. vale on

``POST /users/ID/permissioncheck``

**Post Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``permissions``
     - array
     - **Required.** Array of permission strings to check

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "user:users:view": true,
       "user:users:edit": true
   }

.. vale off

Get User Roles
**************

.. vale on

.. code-block:: php

   <?php

   $roles = $userApi->getRoles();

Get a list of available User roles for user creation/editing.

.. vale off

**HTTP Request**

.. vale on

``GET /users/list/roles``

**Query Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - ``filter``
     - String to filter roles by name
   * - ``limit``
     - Limit number of roles to return

**Response**

``Expected Response Code: 200``

.. code-block:: json

   [
       {
           "id": 1,
           "name": "Administrator",
           "description": "Full system access",
           "isAdmin": true
       },
       {
           "id": 2,
           "name": "Manager",
           "description": "Limited administrative access",
           "isAdmin": false
       },
       {
           "id": 3,
           "name": "User",
           "description": "Basic user access",
           "isAdmin": false
       }
   ]

.. vale off

Batch Operations
****************

.. vale on

**Batch Delete Users**

.. code-block:: php

   <?php

   $userIds = array(1, 2, 3);
   $result = $userApi->deleteBatch($userIds);

Delete multiple Users in a single request.

.. vale off

**HTTP Request**

.. vale on

``DELETE /users/batch/delete?ids=1,2,3``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "users": [
           {
               "id": 1,
               "username": "user1"
           },
           {
               "id": 2,
               "username": "user2"
           }
       ]
   }

**Batch Edit Users**

.. code-block:: php

   <?php

   $data = array(
       array(
           'id'       => 1,
           'position' => 'Senior Developer'
       ),
       array(
           'id'       => 2,
           'timezone' => 'Europe/London'
       )
   );

   $result = $userApi->editBatch($data);

Edit multiple Users in a single request.

.. vale off

**HTTP Request**

.. vale on

``PATCH /users/batch/edit``

**Post Parameters**

Send an array of User data with each item containing the User ID and the fields to update.

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "users": [
           {
               "id": 1,
               "username": "user1",
               "position": "Senior Developer"
           },
           {
               "id": 2,
               "username": "user2",
               "timezone": "Europe/London"
           }
       ]
   }

.. vale off

Error Responses
***************

.. vale on

**Common Error Responses**

.. list-table::
   :header-rows: 1

   * - HTTP Code
     - Error
     - Description
   * - ``400``
     - Bad Request
     - Invalid data provided, for example weak password or duplicate username/email
   * - ``401``
     - Unauthorized
     - Authentication required or weak password detected
   * - ``403``
     - Forbidden
     - User doesn't have permission to perform this action
   * - ``404``
     - Not Found
     - User with the specified ID was not found
   * - ``422``
     - Unprocessable Entity
     - Validation errors in the submitted data

**Password Policy Errors**

When creating or updating users, password validation errors may occur:

.. code-block:: json

   {
       "error": {
           "code": 400,
           "message": "Validation Failed",
           "details": {
               "plainPassword": [
                   "The password is too weak. It must be at least 6 characters long and contain a mix of letters, numbers, and special characters."
               ]
           }
       }
   }

**Permission Errors**

When checking permissions on non-existent users:

.. code-block:: json

   {
       "error": {
           "code": 404,
           "message": "Item was not found."
       }
   }

**Role Assignment Errors**

When assigning invalid roles:

.. code-block:: json

   {
       "error": {
           "code": 400,
           "message": "role: The selected choice is invalid."
       }
   }