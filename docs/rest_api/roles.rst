Roles
#####

Use this endpoint to obtain details on Mautic's Roles, like administrators.

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
   $roleApi  = $api->newApi("roles", $auth, $apiUrl);

.. vale off

Get Role
********

.. vale on

.. code-block:: php

   <?php

   //...
   $role = $roleApi->get($id);



Get an individual Role by ID.

.. vale off

**HTTP Request**

.. vale on

``GET /roles/ID``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {  
     "role":{  
       "isPublished":true,
       "dateAdded":"2016-11-09T15:24:32+00:00",
       "createdBy":1,
       "createdByUser":"John Doe",
       "dateModified":null,
       "modifiedBy":null,
       "modifiedByUser":null,
       "id":13,
       "name":"API test role",
       "description":"created via AIP",
       "isAdmin":false,
       "rawPermissions":{  
         "email:emails":[  
           "viewown",
           "viewother"
         ]
       }
     }
   }

**Role Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Role
   * - ``dateAdded``
     - ``datetime``
     - Role creation date/time
   * - ``createdBy``
     - int
     - ID of the Role that created the Contact
   * - ``createdByRole``
     - string
     - Name of the Role that created the Contact
   * - ``dateModified``
     - datetime/null
     - Date/time Contact was last modified
   * - ``modifiedBy``
     - int
     - ID of the Role that last modified the Contact
   * - ``modifiedByRole``
     - string
     - Name of the Role that last modified the Contact
   * - ``name``
     - string
     - Name of the Role
   * - ``description``
     - string
     - Description of the Role
   * - ``isAdmin``
     - boolean
     - Whether the Role has full access or only some
   * - ``rawPermissions``
     - array
     - List of Roles

.. vale off

List Contact Roles
******************

.. vale on

.. code-block:: php

   <?php

   //...
   $roles = $roleApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

**HTTP Request**

.. vale on

``GET /roles``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {  
     "total":9,
     "roles":[  
       {  
         "isPublished":true,
         "dateAdded":"2016-08-01T11:51:32+00:00",
         "createdBy":1,
         "createdByUser":"John Doe",
         "dateModified":null,
         "modifiedBy":null,
         "modifiedByUser":null,
         "id":2,
         "name":"view email",
         "description":null,
         "isAdmin":false,
         "rawPermissions":{  
           "email:emails":[  
             "viewown",
             "viewother"
           ]
         }
       }
     ]
   }

**Role Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Role
   * - ``dateAdded``
     - ``datetime``
     - Role creation date/time
   * - ``createdBy``
     - int
     - ID of the Role that created the Contact
   * - ``createdByRole``
     - string
     - Name of the Role that created the Contact
   * - ``dateModified``
     - datetime/null
     - Date/time Contact was last modified
   * - ``modifiedBy``
     - int
     - ID of the Role that last modified the Contact
   * - ``modifiedByRole``
     - string
     - Name of the Role that last modified the Contact
   * - ``name``
     - string
     - Name of the Role
   * - ``description``
     - string
     - Description of the Role
   * - ``isAdmin``
     - boolean
     - Whether the Role has full access or only some
   * - ``rawPermissions``
     - array
     - List of Roles

.. vale off

Create Role
***********

.. vale on

.. code-block:: php

   <?php 

   $data = array(
       'name' => 'API test role',
       'description' => 'created via API',
       'rawPermissions' => array (
           'email:emails' => 
           array (
               'viewown',
               'viewother',
           ),
       )
   );

   $role = $roleApi->create($data);

Create a new Role.

.. vale off

**HTTP Request**

.. vale on

``POST /roles/new``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``name``
     - string
     - Name of the Role
   * - ``description``
     - string
     - Description of the Role
   * - ``isAdmin``
     - boolean
     - Whether the Role has full access or only some
   * - ``rawPermissions``
     - array
     - List of Roles

**Response**

``Expected Response Code: 201``

**Properties**

Same as `Get Role <#get-role>`_.

.. vale off

Edit Role
*********

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'name' => 'API test role',
       'description' => 'created via API',
       'rawPermissions' => array (
           'email:emails' => 
           array (
               'editown',
               'editother',
           ),
       )
   );

   // Create new a Role of ID 1 isn't found?
   $createIfNotFound = true;

   $role = $roleApi->edit($id, $data, $createIfNotFound);

Edit a new Role. Note that this supports PUT or PATCH depending on the desired behavior.

**PUT** creates a Role if the given ID doesn't exist and clears all the Role information, adds the information from the request.
**PATCH** fails if the Role with the given ID doesn't exist and updates the Role field values with the values from the request.

.. vale off

**HTTP Request**

.. vale on

To edit a Role and return a 404 if the Role isn't found:

``PATCH /roles/ID/edit``

To edit a Role and create a new one if the Role isn't found:

``PUT /roles/ID/edit``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``name``
     - string
     - Name of the Role
   * - ``description``
     - string
     - Description of the Role
   * - ``isAdmin``
     - boolean
     - Whether the Role has full access or only some
   * - ``rawPermissions``
     - array
     - List of Roles


**Response**

If ``PUT``, the expected response code is ``200`` if editing a Role or ``201`` if creating a new one.

If ``PATCH``, the expected response code is ``200``.

**Properties**

Same as `Get Role <#get-role>`_.

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

Same as `Get Role <#get-role>`_.
