Projects
########

Use this endpoint to get details on Mautic's Projects and to create, edit, and delete them. You can also link other entities, such as Emails or Campaigns, to a Project.

Mautic exposes Projects through both the v1 REST API described here and the :ref:`Mautic API v2 <rest_api/api_v2:Mautic API v2>`.

.. vale off

Get Project
***********

Retrieves an individual Project.

.. vale on

.. vale off

HTTP request
============

.. vale on

``GET /projects/ID``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Project.

.. _get Project response:

.. code-block:: json

   {
      "project": {
          "id": 7,
          "name": "Summer campaign",
          "description": "Assets and Emails for the summer launch.",
          "properties": []
      }
   }

.. _get Project properties:

Project properties
------------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - integer
     - ID of the Project
   * - ``name``
     - string
     - Name of the Project
   * - ``description``
     - string
     - Description of the Project
   * - ``properties``
     - object
     - Additional Project data stored as a JSON object

.. note::

   The list view of the Project, returned by ``GET /projects``, includes only the ``id`` and ``name`` properties. The ``description`` and ``properties`` values are available when you retrieve a single Project.

.. vale off

List Projects
*************

Retrieves a list of Projects.

.. vale on

.. vale off

HTTP request
============

.. vale on

``GET /projects``

Query parameters
----------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``search``
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

       **Note**: convert ``camelCase`` properties to ``snake_case``. For example, ``dateModified`` becomes ``date_modified``
   * - ``orderByDir``
     - string
     - Order direction - ``asc`` or ``desc``
   * - ``publishedOnly``
     - boolean
     - Returns only currently active entities
   * - ``minimal``
     - boolean
     - Returns only a simple mapped object of entities without additional lists in it

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Projects list.

.. code-block:: json

   {
     "total": 2,
     "projects": [
       {
          "id": 7,
          "name": "Summer campaign"
       },
       {
          "id": 8,
          "name": "Product launch"
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
     - integer
     - Total count of Projects
   * - ``projects``
     - object
     - A mapped collection of Projects indexed by their ID

.. vale off

Create Project
**************

Creates a new Project.

.. vale on

.. vale off

HTTP request
============

.. vale on

``POST /projects/new``

.. _create Project POST parameters:

POST parameters
---------------

.. list-table::
   :widths: 30 20 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``name``
     - string
     - **Required.**

       Name of the Project. The name must be unique.
   * - ``description``
     - string
     - Description of the Project

Response
========

* Returns ``201 Created`` when the request successfully creates a Project.

The response is a JSON object similar to :ref:`Get Project <get Project response>`.

Properties
----------

Refer to :ref:`Project properties <get Project properties>`.

.. vale off

Edit Project
************

Edits a Project.

.. vale on

This operation supports ``PUT`` or ``PATCH`` depending on the desired behavior:

* ``PUT``: **full replacement**. The request creates a new Project if the ID is missing. If the ID exists, the request clears all existing data and replaces it with the provided values.
* ``PATCH``: **partial update**. The request only updates field values based on the request data. The request fails when the ID doesn't exist.

.. vale off

HTTP request
============

.. vale on

* ``PUT /projects/ID/edit``: updates an existing Project or creates a new one when the ID doesn't exist.
* ``PATCH /projects/ID/edit``: updates an existing Project. The request fails when the ID doesn't exist.

POST parameters
---------------

Accepts the same parameters as those described in :ref:`Create Project <create Project POST parameters>`. All parameters are optional.

Response
========

* ``PUT``: returns ``200 OK`` when the request successfully updates the Project or ``201 Created`` when the request creates a Project.
* ``PATCH``: returns ``200 OK`` when the request successfully updates the Project or ``404 Not Found`` when the ID doesn't exist.

The response is a JSON object similar to :ref:`Get Project <get Project response>`.

Properties
----------

Refer to :ref:`Project properties <get Project properties>`.

.. vale off

Delete Project
**************

Deletes a Project.

.. vale on

.. vale off

HTTP request
============

.. vale on

``DELETE /projects/ID/delete``

Response
========

* Returns ``200 OK`` when the request successfully deletes the Project.

The response is a JSON object containing the data of the deleted Project, similar to :ref:`Get Project <get Project response>`.

Properties
----------

Refer to :ref:`Project properties <get Project properties>`.

.. vale off

Delete Projects in bulk
***********************

Deletes multiple Projects in a single request.

.. vale on

.. vale off

HTTP request
============

.. vale on

``DELETE /projects/batch/delete?ids=1,2,3``

Pass the IDs of the Projects to delete as a comma-separated ``ids`` query parameter.

Response
========

* Returns ``200 OK`` when the request successfully deletes the Projects.

.. code-block:: json

   {
     "projects": [
       {
          "id": 1,
          "name": "Summer campaign",
          "description": "Assets and Emails for the summer launch.",
          "properties": []
       },
       {
          "id": 2,
          "name": "Product launch",
          "description": null,
          "properties": []
       }
     ]
   }

If Mautic can't delete one of the requested Projects, it adds an ``errors`` object to the response describing the failure for that ID.

.. _link Projects to entities:

.. vale off

Link a Project to an entity
***************************

.. vale on

To link entities to a Project, send the ``projects`` property with an array of Project IDs when you create or edit a supported entity. For example, to link Projects ``1``, ``2``, and ``3`` to an Email, send a ``PATCH`` request to ``/emails/1/edit``:

.. code-block:: json

   {
     "name": "Summer newsletter",
     "projects": [1, 2, 3]
   }

To remove a Project link, send the ``projects`` array again with only the IDs you want to keep linked, leaving out the IDs you want to remove. An empty array removes every Project link from the entity.

The entities that support linking to a Project are Assets, Campaigns, Companies, Dynamic Content, Emails, Focus Items, Forms, Landing Pages, Marketing Messages, Points, Point Triggers, Segments, Stages, and Text Messages.

When an entity links to one or more Projects, the API serializes the ``projects`` association with the ``id`` and ``name`` of each linked Project.

Projects in the Mautic API v2
*****************************

Projects are also available through the :ref:`Mautic API v2 <rest_api/api_v2:Mautic API v2>` under the ``/api/v2/projects`` endpoint, which supports retrieving, creating, editing, and deleting Projects. For the full list of operations, parameters, and response formats, use the self-documenting interface at the ``/api/v2`` endpoint as described in :ref:`Mautic API v2 <rest_api/api_v2:Mautic API v2>`.
