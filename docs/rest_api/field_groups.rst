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

   Mautic generates a group's ``alias`` from its ``name`` when you create the group, and the alias never changes after that. The API ignores any ``alias`` you send in a create or edit payload. This keeps Contact and Company Fields that reference a group by alias from being orphaned when you rename the group.

Get Field Group
***************

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

Get an individual Field Group by ID.

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

Field Group properties
======================

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

List Field Groups
*****************

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

Create Field Group
******************

.. code-block:: php

   <?php

   $data = [
       'name'        => 'Billing',
       'description' => 'Invoicing fields'
   ];

   $fieldGroup = $fieldGroupApi->create($data);

Create a new Field Group. Mautic generates the ``alias`` from the ``name``, so you don't need to send one.

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

Edit Field Group
****************

.. code-block:: php

   <?php

   $id   = 12;
   $data = [
       'name'        => 'Billing Updated',
       'description' => 'Updated description'
   ];

   $fieldGroup = $fieldGroupApi->edit($id, $data);

.. vale off

HTTP request
============

.. vale on

``PATCH /field-groups/ID/edit``

The ``alias`` stays the same when you rename a group, and Mautic ignores any ``alias`` value in the payload.

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

``Expected Response Code: 200``

Properties
==========

Same as `Get Field Group`_.

Delete Field Group
******************

.. code-block:: php

   <?php

   $fieldGroup = $fieldGroupApi->delete($id);

Delete a Field Group.

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
