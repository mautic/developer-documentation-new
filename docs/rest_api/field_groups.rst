Field Groups
############

Use this endpoint to manage Custom Field Groups in Mautic. Custom Field Groups organize Contact and Company Custom Fields into named tabs, alongside the built-in groups such as 'core', 'social', 'personal', and 'professional'.

.. code-block:: php

   <?php
   use Mautic\MauticApi;
   use Mautic\Auth\ApiAuth;

   // ...
   $initAuth = new ApiAuth();
   $auth     = $initAuth->newAuth($settings);
   $apiUrl   = "https://your-mautic.com";
   $api      = new MauticApi();
   $fieldGroupApi = $api->newApi("fieldGroups", $auth, $apiUrl);

.. note::

   Mautic generates a group's ``alias`` from its ``name`` when you create the group, and the alias never changes after that. The API ignores any ``alias`` you send in a create or edit payload. This way, renaming a group never orphans the Contact and Company Fields that reference it by alias.

.. vale off

Get Field Group
***************

.. vale on

Retrieves an individual Field Group.

.. code-block:: php

   <?php

   //...
   $fieldGroup = $fieldGroupApi->get($id);

.. code-block:: json

   {
     "fieldGroup": {
       "id": 12,
       "name": "Billing",
       "alias": "billing",
       "description": "Invoicing fields",
       "order": 5
     }
   }

.. vale off

HTTP request
============

.. vale on

``GET /field-groups/ID``

Response
========

``Expected Response Code: 200``

When the ID doesn't exist, the endpoint returns an ``HTTP 404 (Not Found)`` response.

See the JSON code example.

.. vale off

Field Group properties
======================

.. vale on

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Field Group
   * - ``name``
     - string
     - Field Group name
   * - ``alias``
     - string
     - Unique, auto-generated alias used by Custom Fields to reference the group. Immutable after creation.
   * - ``description``
     - string/null
     - Field Group description
   * - ``order``
     - int
     - Position of the group in the tab order on Contact and Company views

.. vale off

List Field Groups
*****************

.. vale on

Retrieves a list of Field Groups.

.. code-block:: php

   <?php

   //...
   $fieldGroups = $fieldGroupApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. code-block:: json

   {
     "total": 2,
     "fieldGroups": [
       {
         "id": 12,
         "name": "Billing",
         "alias": "billing",
         "description": "Invoicing fields",
         "order": 5
       },
       {
         "id": 13,
         "name": "Logistics",
         "alias": "logistics",
         "description": null,
         "order": 6
       }
     ]
   }

.. vale off

HTTP request
============

.. vale on

``GET /field-groups``

Response
========

``Expected Response Code: 200``

See the JSON code example.

Properties
==========

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``total``
     - int
     - Count of all Field Groups
   * - ``id``
     - int
     - ID of the Field Group
   * - ``name``
     - string
     - Field Group name
   * - ``alias``
     - string
     - Unique, auto-generated alias used by Custom Fields to reference the group
   * - ``description``
     - string/null
     - Field Group description
   * - ``order``
     - int
     - Position of the group in the tab order on Contact and Company views

.. vale off

Create Field Group
******************

.. vale on

Creates a new Field Group. Mautic generates the ``alias`` from the ``name``, so you don't need to send one.

.. code-block:: php

   <?php

   $data = [
       'name'        => 'Billing',
       'description' => 'Invoicing fields'
   ];

   $fieldGroup = $fieldGroupApi->create($data);

.. vale off

HTTP request
============

.. vale on

``POST /field-groups/new``

.. vale off

POST parameters
===============

.. vale on

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``name``
     - string
     - Field Group name. This is the only required parameter, and can only contain letters, numbers, and spaces.
   * - ``description``
     - string/null
     - Field Group description
   * - ``order``
     - int
     - Optional position of the group in the tab order. Defaults to the end of the list when omitted.

Response
========

``Expected Response Code: 201``

When the ``name`` is missing, the endpoint returns a validation error response.

Properties
==========

Same as `Get Field Group`_.

.. vale off

Edit Field Group
****************

.. vale on

Edits a Field Group.

This operation supports ``PUT`` or ``PATCH`` depending on the desired behavior:

* ``PUT``: **full replacement**. The request creates a new Field Group if the ID is missing. If the ID exists, the request clears all existing data and replaces it with the provided values.
* ``PATCH``: **partial update**. The request only updates field values based on the request data. The request fails when the Field Group ID doesn't exist.

.. code-block:: php

   <?php

   $id   = 12;
   $data = [
       'name'        => 'Billing Updated',
       'description' => 'Updated description'
   ];

   $fieldGroup = $fieldGroupApi->edit($id, $data);

The ``alias`` stays the same when you rename a group, and Mautic ignores any ``alias`` value in the payload.

.. vale off

HTTP request
============

.. vale on

* ``PUT /field-groups/ID/edit``: updates an existing Field Group or creates a new one when the ID doesn't exist.
* ``PATCH /field-groups/ID/edit``: updates an existing Field Group. The request fails when the ID doesn't exist.

.. vale off

POST parameters
===============

.. vale on

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``name``
     - string
     - Field Group name. Can only contain letters, numbers, and spaces.
   * - ``description``
     - string/null
     - Field Group description
   * - ``order``
     - int
     - Position of the group in the tab order on Contact and Company views

Response
========

* ``PUT``: returns ``200 OK`` when the request successfully updates the Field Group or ``201 Created`` when the request creates a Field Group.
* ``PATCH``: returns ``200 OK`` when the request successfully updates the Field Group or ``404 Not Found`` error when the Field Group ID doesn't exist.

Properties
==========

Same as `Get Field Group`_.

.. vale off

Delete Field Group
******************

.. vale on

Deletes a Field Group.

.. code-block:: php

   <?php

   $fieldGroup = $fieldGroupApi->delete($id);

.. vale off

HTTP request
============

.. vale on

``DELETE /field-groups/ID/delete``

Response
========

``Expected Response Code: 200``

Properties
==========

Same as `Get Field Group`_.
