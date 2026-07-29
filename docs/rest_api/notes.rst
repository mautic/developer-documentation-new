Notes
#####

Use this endpoint to manipulate and obtain details on Contact Notes in Mautic.

.. vale off

Permissions
***********

.. vale on

The Notes API uses the ``lead:notes`` permission set, which is separate from the ``lead:leads`` - Contact on UI - permission set. However, ``lead:notes`` permissions don't grant access to the associated Contact: any operation involving a Contact still requires the appropriate ``lead:leads`` permission.

For the standalone ``/notes`` endpoints, Mautic evaluates ``viewown``/``viewother``, ``editown``/``editother``, and ``deleteown``/``deleteother`` against the User who created the Note, not the owner of the associated Contact. The Note's ``createdBy`` field determines ownership.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Permission
     - Description
   * - ``lead:notes:viewown``
     - View Notes created by the authenticated User
   * - ``lead:notes:viewother``
     - View Notes created by other Users
   * - ``lead:notes:editown``
     - Edit Notes created by the authenticated User
   * - ``lead:notes:editother``
     - Edit Notes created by other Users
   * - ``lead:notes:create``
     - Create new Notes
   * - ``lead:notes:deleteown``
     - Delete Notes created by the authenticated User
   * - ``lead:notes:deleteother``
     - Delete Notes created by other Users
   * - ``lead:notes:full``
     - Full access to all Note operations

.. vale off

Using the Mautic API library
****************************

.. vale off

You can interact with this API using the :xref:`Mautic API Library` as below, or the various HTTP endpoints described in this document.

.. vale on

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
   $noteApi  = $api->newApi("notes", $auth, $apiUrl);

.. vale off

Get Note
********

.. vale on

Retrieves an individual Note.

.. code-block:: php

   <?php

   //...
   $note = $noteApi->get($id);

.. vale off

HTTP request
============

.. vale on

``GET /notes/ID``

**Required permissions:** ``lead:notes:viewown`` or ``lead:notes:viewother``

.. _get Note response:

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Note.

.. code-block:: json

   {
       "note": {
           "id": 1,
           "text": "<p>Discussed product demo requirements. Follow-up scheduled for next week.</p>",
           "type": "general",
           "dateTime": "2015-07-23T13:14:00-05:00",
           "lead": {
               "id": 47
           },
           "dateAdded": "2015-07-23T13:14:00-05:00",
           "createdBy": 1,
           "createdByUser": "Joe Smith"
       }
   }

.. _get Note properties:

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
     - ID of the Note
   * - ``text``
     - string
     - Body content of the Note - supports HTML
   * - ``type``
     - string
     - Type of Note: ``general``, ``email``, ``call``, or ``meeting``
   * - ``dateTime``
     - datetime
     - Date and time associated with the Note
   * - ``lead``
     - object
     - The Contact associated with this Note
   * - ``dateAdded``
     - datetime
     - Note creation date and time
   * - ``createdBy``
     - integer
     - ID of the User who created the Note
   * - ``createdByUser``
     - string
     - Name of the User who created the Note

.. vale off

List Notes
**********

.. vale on

Retrieves a list of Notes.

.. code-block:: php

   <?php

   //...
   $notes = $noteApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir);

.. vale off

HTTP request
============

.. vale on

``GET /notes``

**Required permissions:** ``lead:notes:viewown`` or ``lead:notes:viewother``

Query parameters
----------------

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Name
     - Description
   * - ``search``
     - String or search command to filter entities by
   * - ``start``
     - Starting row for the entities returned - defaults to ``0``
   * - ``limit``
     - Limit number of entities to return - defaults to the system configuration for pagination
   * - ``orderBy``
     - Column to sort by. Any column in the response is valid.

       **Note**: convert ``camelCase`` properties to ``snake_case``. For example, ``dateAdded`` becomes ``date_added``, ``webhookUrl`` becomes ``webhook_url``, and so on
   * - ``orderByDir``
     - Sort direction - ``asc`` or ``desc``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Notes list.

.. code-block:: json

   {
       "total": 2,
       "notes": [
           {
               "id": 1,
               "text": "<p>Discussed product demo requirements. Follow-up scheduled for next week.</p>",
               "type": "general",
               "dateTime": "2015-07-23T13:14:00-05:00",
               "lead": {
                   "id": 47
               }
           },
           // ...
       ]
   }

.. vale off

Create Note
***********

.. vale on

Creates a new Note for a Contact.

.. code-block:: php

   <?php

   $data = [
       'lead' => 47,
       'text' => 'Note content here',
       'type' => 'general',
   ];

   $note = $noteApi->create($data);

.. vale off

HTTP request
============

.. vale on

``POST /notes/new``

**Required permissions:** ``lead:notes:create``

.. note::

   In addition to ``lead:notes:create``, the User must have permission to view the associated Contact - ``lead:leads:viewown`` or ``lead:leads:viewother``. Mautic checks view access against the Contact owner before creating the Note.

.. _create Note POST parameters:

POST parameters
---------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Required
     - Description
   * - ``lead``
     - Yes
     - ID of the Contact to associate the Note with
   * - ``text``
     - Yes
     - Body content of the Note - supports HTML
   * - ``type``
     - No
     - Type of Note: ``general`` - default, ``email``, ``call``, or ``meeting``
   * - ``dateTime``
     - No
     - Date and time associated with the Note - auto-set to current time if not provided

Response
========

* Returns ``201 Created`` when the Note is successfully created.

The response is a JSON object similar to :ref:`Get Note <get Note response>`.

.. vale off

Edit Note
*********

.. vale on

Edits a Note. This operation supports ``PUT`` or ``PATCH`` depending on the desired behavior:

* ``PUT``: **full replacement**. The request creates a new Note if the ID is missing. If the ID exists, the request clears all existing data and replaces it with the provided values.
* ``PATCH``: **partial update**. The request only updates field values based on the request data. The request fails when the Note ID doesn't exist.

.. code-block:: php

   <?php

   $id   = 1;
   $data = [
       'text' => 'Updated note content',
       'type' => 'call',
   ];

   // Using PATCH - update specific fields only
   $note = $noteApi->edit($id, $data);

   // Using PUT - create or completely replace
   $note = $noteApi->edit($id, $data, true);

.. vale off

HTTP request
============

.. vale on

* ``PUT /notes/ID/edit``: updates an existing Note or creates a new one when the ID doesn't exist.
* ``PATCH /notes/ID/edit``: updates an existing Note. The request fails when the ID doesn't exist.

**Required permissions:** ``lead:notes:editown`` or ``lead:notes:editother``

POST parameters
---------------

Accepts the same parameters as those described in :ref:`Create Note <create Note POST parameters>`. All parameters are optional.

Response
========

* ``PUT``: returns ``200 OK`` when the request successfully updates the Note or ``201 Created`` when the request creates a Note.
* ``PATCH``: returns ``200 OK`` when the request successfully updates the Note or ``404 Not Found`` error when the Note ID doesn't exist.

The response is a JSON object similar to :ref:`Get Note <get Note response>`.

.. vale off

Delete Note
***********

.. vale on

Deletes a Note.

.. code-block:: php

   <?php

   $note = $noteApi->delete($id);

.. vale off

HTTP request
============

.. vale on

``DELETE /notes/ID/delete``

**Required permissions:** ``lead:notes:deleteown`` or ``lead:notes:deleteother``

Response
========

* Returns ``200 OK`` when the Note is successfully deleted.

The response is a JSON object containing the data of the deleted Note, similar to :ref:`Get Note <get Note response>`.

.. code-block:: json

   {
       "note": {
           "id": 1,
           "text": "<p>Discussed product demo requirements. Follow-up scheduled for next week.</p>",
           "type": "general",
           "dateTime": "2015-07-23T13:14:00-05:00",
           "lead": {
               "id": 47
           },
           "dateAdded": "2015-07-23T13:14:00-05:00",
           "createdBy": 1,
           "createdByUser": "Joe Smith"
       }
   }

Properties
----------

Refer to :ref:`Note properties <get Note properties>`.
