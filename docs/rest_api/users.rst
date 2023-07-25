Users
#####

Use this endpoint to obtain details on Mautic's Users.

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
     "user":{  
       "isPublished":true,
       "dateAdded":"2016-11-09T14:23:44+00:00",
       "createdBy":1,
       "createdByUser":"John Doe",
       "dateModified":null,
       "modifiedBy":null,
       "modifiedByUser":null,
       "id":6,
       "username":"apitest",
       "firstName":"John",
       "lastName":"Doe",
       "email":"john@doe.com",
       "position":null,
       "role":{  
         "createdByUser":null,
         "modifiedByUser":null,
         "id":1,
         "name":"Administrator",
         "description":"Full system access",
         "isAdmin":true,
         "rawPermissions":null
       },
       "timezone":null,
       "locale":null,
       "lastLogin":null,
       "lastActive":null,
       "onlineStatus":"offline",
       "signature":null
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
   * - ``dateAdded``
     - ``datetime``
     - User creation date/time
   * - ``createdBy``
     - int
     - ID of the User that created the User
   * - createdByUser
     - string
     - Name of the User that created the User
   * - ``dateModified``
     - datetime/null
     - Date/time User was last modified
   * - ``lastActive``
     - datetime/null
     - Date/time when the User last active
   * - ``modifiedBy``
     - int
     - ID of the User that last modified the User
   * - ``modifiedByUser``
     - string
     - Name of the User that last modified the User
   * - ``username``
     - string
     - Username that's used to log into Mautic.
   * - ``firstName``
     - string
     - First Name of the User
   * - ``lastName``
     - string
     - Last Name of the User
   * - ``email``
     - string
     - Email of the User
   * - ``position``
     - string
     - User's position title
   * - ``role``
     - object
     - Role details
   * - ``timezone``
     - string
     - Timezone of the User
   * - ``onlineStatus``
     - string
     - Online status of the User
   * - ``signature``
     - string
     - Signature of the User for use in Emails

.. vale off

List Contact Users
^^^^^^^^^^^^^^^^^^

.. vale on

.. code-block:: php

   <?php

   //...
   $users = $userApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

**HTTP Request**

.. vale on

``GET /users``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {  
     "total":2,
     "users":[  
       {  
         "isPublished":true,
         "dateAdded":"2016-08-01T11:52:15+00:00",
         "createdBy":null,
         "createdByUser":" ",
         "dateModified":"2016-09-26T15:02:32+00:00",
         "modifiedBy":null,
         "modifiedByUser":" ",
         "id":2,
         "username":"test",
         "firstName":"John",
         "lastName":"Doe",
         "email":"john@doe.com",
         "position":null,
         "role":{  
           "createdByUser":"John Doe",
           "modifiedByUser":null,
           "id":4,
           "name":"edit own Contacts",
           "description":null,
           "isAdmin":false,
           "rawPermissions":{  
             "lead:leads":[  
               "viewown",
               "editown",
               "create",
               "deleteown"
             ],
             "lead:lists":[  
               "viewother"
             ]
           }
         },
         "timezone":null,
         "locale":null,
         "lastLogin":"2016-09-26T15:03:25+00:00",
         "lastActive":"2016-09-26T15:19:15+00:00",
         "onlineStatus":"offline",
         "signature":"Best regards,&#10;Yours&#10;|FROM_NAME|"
       }
     ]
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
   * - ``dateAdded``
     - ``datetime``
     - User creation date/time
   * - ``createdBy``
     - int
     - ID of the User that created the User
   * - ``createdByUser``
     - string
     - Name of the User that created the User
   * - ``dateModified``
     - datetime/null
     - Date/time User was last modified
   * - ``lastActive``
     - datetime/null
     - Date/time when the User last active
   * - ``modifiedBy``
     - int
     - ID of the User that last modified the User
   * - ``modifiedByUser``
     - string
     - Name of the User that last modified the User
   * - ``username``
     - string
     - Username that's used to log into Mautic.
   * - ``firstName``
     - string
     - First Name of the User
   * - ``lastName``
     - string
     - Last Name of the User
   * - ``email``
     - string
     - Email of the User
   * - ``position``
     - string
     - User's position title
   * - ``role``
     - array
     - List of Roles of the User
   * - ``timezone``
     - string
     - Timezone of the User
   * - ``onlineStatus``
     - string
     - Online status of the User
   * - ``signature``
     - string
     - Signature of the User for use in Emails

.. vale off

Create User
***********

.. vale on

.. code-block:: php

   <?php 

   $data = array(
       'username' => 'apitest',
       'firstName' => 'John',
       'lastName' => 'Doe',
       'email' => 'john@doe.com',
       'plainPassword' => array(
           'password' => 'topSecret007',
           'confirm' => 'topSecret007',
       ),
       'role' => 1,
   );

   $user = $userApi->create($data);

Create a new User.

.. vale off

**HTTP Request**

.. vale on

``POST /users/new``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``username``
     - string
     - Username that's used to log into Mautic.
   * - ``firstName``
     - string
     - First Name of the User
   * - ``lastName``
     - string
     - Last Name of the User
   * - ``email``
     - string
     - Email of the User
   * - ``position``
     - string
     - User's position title
   * - ``role``
     - int
     - Role ID
   * - ``timezone``
     - string
     - Timezone of the User
   * - ``onlineStatus``
     - string
     - Online status of the User
   * - ``signature``
     - string
     - Signature of the User for use in Emails
   * - ``plainPassword``
     - array
     - array of plain password as in the example


**Response**

``Expected Response Code: 201``

**Properties**

Same as `Get User <#get-user>`_.

.. vale off

Edit User
*********

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'lastName' => 'Doeboe',
   );

   // Create new a User of ID 1 isn't found?
   $createIfNotFound = true;

   $user = $userApi->edit($id, $data, $createIfNotFound);

Edit a new User. User that this supports PUT or PATCH depending on the desired behavior.

**PUT** creates a User if the given ID doesn't exist and clears all the User information, adds the information from the request.

**PATCH** fails if the User with the given ID doesn't exist and updates the User field values with the values from the request.

.. vale off

**HTTP Request**

.. vale on

To edit a User and return a 404 if the User isn't found:

``PATCH /users/ID/edit``

To edit a User and create a new one if the User isn't found:

``PUT /users/ID/edit``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``username``
     - string
     - Username that's used to log into Mautic.
   * - ``firstName``
     - string
     - First Name of the User
   * - ``lastName``
     - string
     - Last Name of the User
   * - ``email``
     - string
     - Email of the User
   * - ``position``
     - string
     - User's position title
   * - ``role``
     - int
     - Role ID
   * - ``timezone``
     - string
     - Timezone of the User
   * - ``signature``
     - string
     - Signature of the User for use in Emails

**Response**

If ``PUT``, the expected response code is ``200`` if the User was edited or ``201`` if created.

If ``PATCH``, the expected response code is ``200``.

**Properties**

Same as `Get User <#get-user>`_.

.. vale off

Delete User
************

.. vale on

.. code-block:: php

   <?php

   $user = $userApi->delete($id);

Delete a User.

.. vale off

**HTTP Request**

.. vale on

``DELETE /users/ID/delete``

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get User <#get-user>`_.

.. vale off

Get Self User
*************

.. vale on

.. code-block:: php

   <?php

   $user = $userApi->getSelf();

Get a self User.

.. vale off

**HTTP Request**

.. vale on

``GET /users/self``

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get User <#get-user>`_.

.. vale off

Check User Permissions
**********************

.. vale on

.. code-block:: php

   <?php
   $permission = array('user:users:create', 'user:users:edit');
   $user = $userApi->checkPermission($id, $permission);

Get a self User.

.. vale off

**HTTP Request**

.. vale on

``GET /users/ID/permissioncheck``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
     "user:users:create":true,
     "user:users:edit":true
   }

**Properties**

array of requested permissions of string in case of just one
