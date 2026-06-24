Field Groups
############

Use this endpoint to manage Custom Field Groups in Mautic. Custom Field Groups organize Contact and Company Custom Fields into named tabs, alongside the built-in groups such as 'core', 'social', 'personal', and 'professional'.

.. note::

   * The Mautic API Library doesn't support the Field Groups API yet, so use the http endpoints described in this document instead.
   * Mautic generates a group's ``alias`` from its ``name`` when you create the group, and the alias never changes after that. The API ignores any ``alias`` you send in a create or edit payload. This way, renaming a group never orphans the Contact and Company Fields that reference it by alias.

.. vale off

Get Field Group
***************

.. vale on

Retrieves an individual Field Group.

.. vale off

HTTP request
============

.. vale on

``GET /field-groups/ID``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Field Group.

When the ID doesn't exist, the endpoint returns a ``404 Not Found`` error.

.. _get Field Group response:

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

.. _get Field Group properties:

.. vale off

Field Group properties
----------------------

.. vale on

.. list-table::
   :widths: 25 25 50
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
     - Unique, auto-generated alias used by Custom Fields to reference the group. Immutable after creation
   * - ``description``
     - string or null
     - Field Group description
   * - ``order``
     - int
     - Position of the group in the tab order on Contact and Company views

.. vale off

List Field Groups
*****************

.. vale on

Retrieves a list of Field Groups.

.. vale off

HTTP request
============

.. vale on

``GET /field-groups``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Field Groups list.

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

Properties
----------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``total``
     - int
     - Total count of Field Groups
   * - ``fieldGroups``
     - array
     - Array of Field Groups

.. vale off

For the rest of the properties, refer to :ref:`Field Group properties <get Field Group properties>`.

.. vale on

.. vale off

Create Field Group
******************

.. vale on

Creates a new Field Group. Mautic generates the ``alias`` from the ``name``, so you don't need to send one.

.. code-block:: json

   {
       "name": "Billing",
       "description": "Invoicing fields"
   }

.. vale off

HTTP request
============

.. vale on

``POST /field-groups/new``

.. _create Field Group POST parameters:

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
     - **Required.**

       Field Group name. Can only contain letters, numbers, and spaces
   * - ``description``
     - string or null
     - Field Group description
   * - ``order``
     - int
     - Position of the group in the tab order. Defaults to the end of the list when omitted

Response
========

* Returns ``201 Created`` when the request successfully creates a Field Group.

When the ``name`` is missing, the endpoint returns a validation error response.

Properties
----------

Refer to :ref:`Field Group properties <get Field Group properties>`.

.. vale off

Edit Field Group
****************

.. vale on

Edits a Field Group.

This operation supports ``PUT`` or ``PATCH`` depending on the desired behavior:

* ``PUT``: **full replacement**. The request creates a new Field Group if the ID is missing. If the ID exists, the request clears all existing data and replaces it with the provided values.
* ``PATCH``: **partial update**. The request only updates field values based on the request data. The request fails when the Field Group ID doesn't exist.

.. code-block:: json

   {
       "name": "Billing Updated",
       "description": "Updated description"
   }

The ``alias`` stays the same when you rename a group, and Mautic ignores any ``alias`` value in the payload.

.. vale off

HTTP request
============

.. vale on

* ``PUT /field-groups/ID/edit``: updates an existing Field Group, or creates a new one when the ID doesn't exist.
* ``PATCH /field-groups/ID/edit``: updates an existing Field Group. The request fails when the ID doesn't exist.

POST parameters
---------------

Accepts the same parameters as those described in :ref:`Create Field Group <create Field Group POST parameters>`. All parameters are optional.

Response
========

* ``PUT``: returns ``200 OK`` when the request successfully updates the Field Group, or ``201 Created`` when the request creates a Field Group.
* ``PATCH``: returns ``200 OK`` when the request successfully updates the Field Group, or a ``404 Not Found`` error when the Field Group ID doesn't exist.

Properties
----------

Refer to :ref:`Field Group properties <get Field Group properties>`.

.. vale off

Delete Field Group
******************

.. vale on

Deletes a Field Group.

.. vale off

HTTP request
============

.. vale on

``DELETE /field-groups/ID/delete``

Response
========

* Returns ``200 OK`` when the request successfully deletes the Field Group.

The response is a JSON object containing the data of the deleted Field Group, similar to :ref:`Get Field Group <get Field Group response>`.

Properties
----------

Refer to :ref:`Field Group properties <get Field Group properties>`.
