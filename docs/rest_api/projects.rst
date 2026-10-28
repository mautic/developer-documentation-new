Projects
########

Use these endpoints to get details on Mautic's Projects and to create, edit, and delete them. You can also link other entities, such as Emails or Campaigns, to a Project. Mautic provides Projects endpoints in both the v1 REST API and the :ref:`API v2 <Projects API v2>`.

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
   * - ``published``
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

Accepts the same parameters as those described in :ref:`Create Project <create Project POST parameters>`. ``PUT`` requests must include ``name`` and clear any parameter you omit. For ``PATCH``, all parameters are optional, and omitted parameters keep their current values.

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

.. _delete Projects in bulk:

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

.. _Projects API v2:

.. vale off

Projects in API v2
******************

.. vale on

Mautic also exposes Projects through the API v2 at ``/api/v2/projects``. API v2 uses the API Platform conventions described in :doc:`/rest_api/api_v2`, so its paths, request formats, and responses differ from the v1 endpoints described earlier.

To see the full schema and try requests from your browser, open ``/api/v2`` while logged in to Mautic.

Request format
==============

Send requests and receive responses in JSON-LD by setting the ``application/ld+json`` media type in the ``Content-Type`` and ``Accept`` headers. API v2 also accepts ``application/json``.

``PATCH`` requests use the ``application/merge-patch+json`` media type in the ``Content-Type`` header.

Permissions
===========

Each operation checks the authenticated User's Project permissions:

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Operation
     - Required permission
   * - List and get Projects
     - ``project:projects:view``
   * - Create a Project
     - ``project:projects:create``
   * - Edit a Project
     - ``project:projects:edit``
   * - Delete a Project
     - ``project:projects:delete``

The API returns ``403 Forbidden`` when the User doesn't have the required permission.

.. _Projects API v2 properties:

Project properties
==================

API v2 reads and writes these Project properties:

.. list-table::
   :widths: 25 20 15 40
   :header-rows: 1

   * - Name
     - Type
     - Access
     - Description
   * - ``id``
     - integer
     - Read only
     - ID of the Project
   * - ``name``
     - string
     - Read and write
     - Name of the Project. Required when creating a Project. The name must be unique, and the comparison ignores case.
   * - ``description``
     - string
     - Read and write
     - Description of the Project
   * - ``properties``
     - object
     - Read and write
     - Additional Project data stored as a JSON object

JSON-LD responses also include the ``@context``, ``@id``, and ``@type`` keys. ``@id`` is the path that identifies the Project, such as ``/api/v2/projects/7``.

.. vale off

List Projects
=============

.. vale on

``GET /api/v2/projects``

Returns a paginated list of Projects. To choose which set of results to return, use the ``page`` query parameter, for example ``GET /api/v2/projects?page=2``.

Response
--------

* Returns ``200 OK`` when the request successfully retrieves the Projects list.

.. code-block:: json

   {
     "@context": "/api/v2/contexts/Project",
     "@id": "/api/v2/projects",
     "@type": "Collection",
     "totalItems": 2,
     "member": [
       {
         "@id": "/api/v2/projects/7",
         "@type": "Project",
         "id": 7,
         "name": "Summer campaign",
         "description": "Assets and Emails for the summer launch.",
         "properties": []
       },
       {
         "@id": "/api/v2/projects/8",
         "@type": "Project",
         "id": 8,
         "name": "Product launch",
         "description": null,
         "properties": []
       }
     ]
   }

The ``member`` array contains the Projects in the current set of results, and ``totalItems`` contains the total number of Projects. When there are more Projects than fit in one response, the response also includes a ``view`` object with links to the first, last, previous, and next sets of results.

.. vale off

Get Project
===========

.. vale on

``GET /api/v2/projects/ID``

Response
--------

* Returns ``200 OK`` when the request successfully retrieves the Project.
* Returns ``404 Not Found`` when no Project has that ID.

.. _Projects API v2 get response:

.. code-block:: json

   {
     "@context": "/api/v2/contexts/Project",
     "@id": "/api/v2/projects/7",
     "@type": "Project",
     "id": 7,
     "name": "Summer campaign",
     "description": "Assets and Emails for the summer launch.",
     "properties": []
   }

.. vale off

Create Project
==============

.. vale on

``POST /api/v2/projects``

Request body
------------

.. code-block:: json

   {
     "name": "Summer campaign",
     "description": "Assets and Emails for the summer launch.",
     "properties": {
       "owner": "Marketing"
     }
   }

You must send ``name``. The other properties are optional. See :ref:`Project properties <Projects API v2 properties>` for the accepted properties.

Response
--------

* Returns ``201 Created`` with the new Project, in the same format as :ref:`Get Project <Projects API v2 get response>`.
* Returns ``422 Unprocessable Entity`` when ``name`` is missing or empty, or when another Project already uses the same name. The response body describes each validation error.

.. vale off

Edit Project
============

.. vale on

This operation supports ``PUT`` or ``PATCH``:

* ``PUT /api/v2/projects/ID``: replaces the Project's writable properties with the values in the request body.
* ``PATCH /api/v2/projects/ID``: updates only the properties in the request body. Send the request with the ``application/merge-patch+json`` media type in the ``Content-Type`` header.

For example, to change only the description of a Project:

.. code-block:: json

   {
     "description": "Assets, Emails, and Landing Pages for the summer launch."
   }

Response
--------

* Returns ``200 OK`` with the updated Project, in the same format as :ref:`Get Project <Projects API v2 get response>`.
* Returns ``404 Not Found`` when no Project has that ID.
* Returns ``422 Unprocessable Entity`` when the new values fail validation, for example when the name is empty or already in use.

.. vale off

Delete Project
==============

.. vale on

``DELETE /api/v2/projects/ID``

Response
--------

* Returns ``204 No Content`` with an empty body when the request successfully deletes the Project.
* Returns ``404 Not Found`` when no Project has that ID.

API v2 doesn't have a bulk delete operation. To delete several Projects in one request, use the v1 ``DELETE /projects/batch/delete`` endpoint described in :ref:`Delete Projects in bulk <delete Projects in bulk>`.
