Notes
#####

Use this endpoint to obtain details on Mautic's Contact notes.

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
   $noteApi  = $api->newApi("notes", $auth, $apiUrl);

.. vale off

Get Note
********

.. vale on

.. code-block:: php

   <?php

   //...
   $note = $noteApi->get($id);

Get an individual note by ID.

.. vale off

**HTTP Request**

.. vale on

``GET /notes/ID``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {  
     "note":{  
       "id":39,
       "text":"Contact note created via API request",
       "type":"general",
       "dateTime":null,
       "lead":{  
         "id":1405,
         "points":0,
         "color":null,
         "fields":{  
           "core":{  
             "firstname":{  
               "id":"2",
               "label":"First Name",
               "alias":"firstname",
               "type":"text",
               "group":"core",
               "field_order":"42",
               "object":"lead",
               "value":"Note API test"
             },
             "lastname":{  
               "id":"3",
               "label":"Last Name",
               "alias":"lastname",
               "type":"text",
               "group":"core",
               "field_order":"44",
               "object":"lead",
               "value":null
             }
           },
         }
       }
     }
   }


**Note Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the note
   * - ``lead``
     - array
     - data of the Contact
   * - ``text``
     - string
     - Note text
   * - ``type``
     - string
     - Note type
   * - ``datetime``
     - ``datetime``
     - Date and time related to the note.

.. vale off

List Contact Notes
******************

.. vale on

.. code-block:: php

   <?php

   //...
   $notes = $noteApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

**HTTP Request**

.. vale on

``GET /notes``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {  
     "total":24,
     "notes":[  
       {  
         "id":1,
         "text":"A test note",
         "type":"general",
         "dateTime":"2016-06-14T18:07:00+00:00",
         "lead":{  
           "id":1,
           "points":0,
           "color":null,
           "fields":[]
         }
       }
     ]
   }

**Note Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the note
   * - ``lead``
     - array
     - data of the Contact
   * - ``text``
     - string
     - Note text
   * - ``type``
     - string
     - Note type
   * - ``datetime``
     - ``datetime``
     - Date and time related to the note.

.. vale off

Create Note
***********

.. vale on

.. code-block:: php

   <?php 

   $contactID = 1;

   $data = array(
       'lead' => $contactID,
       'text' => 'Note A',
       'type' => 'general',
   );

   $note = $noteApi->create($data);

Create a new note.

.. vale off

**HTTP Request**

.. vale on

``POST /notes/new``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``text``
     - string
     - Note text
   * - ``type``
     - string
     - Note type
   * - ``datetime``
     - ``datetime``
     - Date and time related to the note.


**Response**

``Expected Response Code: 201``

**Properties**

Same as `Get Note <#get-note>`_.

.. vale off

Edit Note
*********

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'text' => 'Note B',
       'type' => 'general',
   );

   // Create new a note of ID 1 isn't found?
   $createIfNotFound = true;

   $note = $noteApi->edit($id, $data, $createIfNotFound);

Edit a new note. Note that this supports PUT or PATCH depending on the desired behavior.

**PUT** creates a note if the given ID doesn't exist and clears all the note information, adds the information from the request.

**PATCH** fails if the note with the given ID doesn't exist and updates the note field values with the values from the request.

.. vale off

**HTTP Request**

.. vale on

To edit a note and return a 404 if the note isn't found:

``PATCH /notes/ID/edit``

To edit a note and create a new one if the note isn't found:

``PUT /notes/ID/edit``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``text``
     - string
     - Note text
   * - ``type``
     - string
     - Note type
   * - ``datetime``
     - ``datetime``
     - Date and time related to the note.


**Response**

If ``PUT``, the expected response code is ``200`` if editing the note or ``201`` if created.

If ``PATCH``, the expected response code is ``200``.

**Properties**

Same as `Get Note <#get-note>`_.

.. vale off

Delete Note
***********

.. vale on

.. code-block:: php

   <?php

   $note = $noteApi->delete($id);

Delete a note.

.. vale off

**HTTP Request**

.. vale on

``DELETE /notes/ID/delete``

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get Note <#get-note>`_.
