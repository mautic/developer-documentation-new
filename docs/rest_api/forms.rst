
Forms API
#########

Use this endpoint to obtain details on Mautic's Forms.

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
   $formApi  = $api->newApi("forms", $auth, $apiUrl);

.. vale off

Get Form
********

.. vale on

.. code-block:: php

   <?php

   //...
   $form = $formApi->get($id);

Get an individual Form by ID.

.. vale off

**HTTP Request**

.. vale on

``GET /forms/ID``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "form": {
           "id": 3,
           "name": "Newlsetter",
           "alias": "newsletter",
           "description": null,
           "isPublished": true,
           "publishUp": null,
           "publishDown": null,
           "dateAdded": "2015-07-15T15:06:02-05:00",
           "createdBy": 1,
           "createdByUser": "Joe Smith",
           "dateModified": "2015-07-20T13:11:56-05:00",
           "modifiedBy": 1,
           "modifiedByUser": "Joe Smith",
           "category": null,
           "cachedHtml": "\n\n<script...",
           "template": null,
           "fields": {
               "26": {
                   "id": 26,
                   "label": "Email",
                   "showLabel": false,
                   "alias": "email",
                   "type": "text",
                   "defaultValue": null,
                   "isRequired": true,
                   "validationMessage": "Email is required",
                   "helpMessage": null,
                   "order": 1,
                   "properties": {
                       "placeholder": "Email address"
                   },
                   "labelAttributes": null,
                   "inputAttributes": null,
                   "containerAttributes": null
               },
               "27": {
                   "id": 27,
                   "label": "Submit",
                   "showLabel": true,
                   "alias": "submit",
                   "type": "button",
                   "defaultValue": null,
                   "isRequired": false,
                   "validationMessage": null,
                   "helpMessage": null,
                   "order": 4,
                   "properties": [],
                   "labelAttributes": null,
                   "inputAttributes": null,
                   "containerAttributes": null
               }
           },
           "actions": {
               "4": {
                   "id": 4,
                   "type": "email.send.lead",
                   "name": "Send thank you email",
                   "description": null,
                   "order": 1,
                   "properties": {
                       "email": 21
                   }
               }
           }
       }
   }

**Form Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Form
   * - ``name``
     - string
     - Name of the Form
   * - ``description``
     - string/null
     - Description of the Form
   * - ``alias``
     - string
     - Used to generate the URL for the Form
   * - ``isPublished``
     - booleanean
     - Published state
   * - ``publishUp``
     - datetime/null
     - Form publish date/time
   * - ``publishDown``
     - datetime/null
     - Form unpublish date/time
   * - ``dateAdded``
     - ``datetime``
     - Form creation date/time
   * - ``createdBy``
     - int
     - ID of the User that created the Form
   * - ``createdByUser``
     - string
     - Name of the User that created the Form
   * - ``dateModified``
     - datetime/null
     - Form modified date/time
   * - ``modifiedBy``
     - int
     - ID of the User that last modified the Form
   * - ``modifiedByUser``
     - string
     - Name of the User that last modified the Form
   * - ``cachedHtml``
     - string
     - Cached HTML for the Form
   * - ``template``
     - string/null
     - Name of the template used to generate the HTML
   * - ``fields``
     - array
     - Array of Field entities for the Form. See below.
   * - ``actions``
     - array
     - Array of Action entities for the Form. See below.

**Field Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the field
   * - ``label``
     - string
     - Label of the field
   * - ``showLabel``
     - boolean
     - Display the label of the field
   * - ``alias``
     - string
     - Used as the database column
   * - ``type``
     - string
     - Field type
   * - ``defaultValue``
     - string
     - Default value
   * - ``isRequired``
     - boolean
     - Is this field required?
   * - ``validationMessage``
     - string
     - Validation message if the required field isn't filled out
   * - ``helpMessage``
     - string
     - Help message for the field
   * - ``order``
     - int
     - Order of the field
   * - ``properties``
     - array
     - Configured properties for the field
   * - ``labelAttributes``
     - string/null
     - Custom HTML attributes for the label
   * - ``inputAttributes``
     - string/null
     - Custom HTML attributes for the input
   * - ``containerAttributes``
     - string/null
     - Custom HTML attributes for the container


**Action Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the action
   * - ``type``
     - string
     - Action type
   * - ``name``
     - string
     - Name of the action
   * - ``description``
     - string/null
     - Description of the action
   * - ``order``
     - int
     - Action order
   * - ``properties``
     - array
     - Configured properties for the action

.. vale off

List Forms
**********

.. vale on

.. code-block:: php

   <?php
   // ...

   $forms = $formApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

**HTTP Request**

.. vale on

``GET /forms``

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
     - Limit number of entities to return. Defaults to the system configuration for pagination - default of 30.
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
       "total": 1,
       "forms": [
           {
               "id": 3,
               "name": "Newlsetter",
               "alias": "newsletter",
               "description": null,
               "isPublished": true,
               "publishUp": null,
               "publishDown": null,
               "dateAdded": "2015-07-15T15:06:02-05:00",
               "createdBy": 1,
               "createdByUser": "Joe Smith",
               "dateModified": "2015-07-20T13:11:56-05:00",
               "modifiedBy": 1,
               "modifiedByUser": "Joe Smith",
               "category": null,
               "cachedHtml": "\n\n<script...",
               "template": null,
               "fields": {
                   "26": {
                       "id": 26,
                       "label": "Email",
                       "showLabel": false,
                       "alias": "email",
                       "type": "text",
                       "defaultValue": null,
                       "isRequired": true,
                       "validationMessage": "Email is required",
                       "helpMessage": null,
                       "order": 1,
                       "properties": {
                           "placeholder": "Email address"
                       },
                       "labelAttributes": null,
                       "inputAttributes": null,
                       "containerAttributes": null
                   },
                   "27": {
                       "id": 27,
                       "label": "Submit",
                       "showLabel": true,
                       "alias": "submit",
                       "type": "button",
                       "defaultValue": null,
                       "isRequired": false,
                       "validationMessage": null,
                       "helpMessage": null,
                       "order": 4,
                       "properties": [],
                       "labelAttributes": null,
                       "inputAttributes": null,
                       "containerAttributes": null
                   }
               },
               "actions": {
                   "4": {
                       "id": 4,
                       "type": "email.send.lead",
                       "name": "Send thank you email",
                       "description": null,
                       "order": 1,
                       "properties": {
                           "email": 21
                       }
                   }
               }
           }
       ]
   }

**Properties**

Same as `Get Form <#get-form>`_.

.. vale off

Create Form
***********

.. vale on

.. code-block:: php

   <?php

   $data = array(
       'name' => 'test',
       'formType' => 'standalone',
       'description' => 'API test',
       'fields' => array(
           array(
               'label' => 'field name',
               'type' => 'text'
           )
       ),
       'actions' => array(
           array(
               'name' => 'action name',
               'description' => 'action desc',
               'type' => 'lead.pointschange',
               'properties' => array(
                   'operator' => 'plus',
                   'points' => 2
               )
           )
       )
   );

   $form = $formApi->create($data);

Create a new Form.

.. vale off

**HTTP Request**

.. vale on

``POST /forms/new``

**POST Parameters**

Same as `Get Form <#get-form>`_. You can create or edit Form fields and actions via the Forms/actions arrays in the Form array.

**Response**

``Expected Response Code: 201``

**Properties**

Same as `Get Form <#get-form>`_.

.. vale off

Edit Form
*********

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'name' => 'test',
       'formType' => 'standalone',
       'description' => 'API test',
       'fields' => array(
           array(
               'label' => 'A field that will be added',
               'type' => 'text'
           ),
           array(
               'id' => 1,
               'label' => 'A field that will be edited',
               'type' => 'text'
           )
       ),
       'actions' => array(
           array(
               'name' => 'action name',
               'description' => 'action desc',
               'type' => 'lead.pointschange',
               'properties' => array(
                   'operator' => 'plus',
                   'points' => 2
               )
           )
       )
   );

   // Create new a Form of ID 1 isn't found?
   $createIfNotFound = true;

   $form = $formApi->edit($id, $data, $createIfNotFound);

Edit a new Form. Note that this supports ``PUT`` or ``PATCH`` depending on the desired behavior.

Make sure that whenever you want to edit a Form field that you include the Form field id in the request. If you don't provide an ID for the Field, a new one gets created.

**PUT** creates a Form if the given ID doesn't exist and clears all the Form information, adds the information from the request. Form fields and actions also get deleted if not present in the request.
**PATCH** fails if the Form with the given ID doesn't exist and updates the Form field values with the values Form the request.

.. vale off

**HTTP Request**

.. vale on

To edit a Form and return a 404 if the Form isn't found:

``PATCH /forms/ID/edit``

To edit a Form and create a new one if the Form isn't found:

``PUT /forms/ID/edit``

**POST Parameters**

Same as `Get Form <#get-form>`_. You can create or edit Form fields and actions via the Forms/actions arrays in the Form array.

**Response**

If ``PUT``, the expected response code is ``200`` when editing the Form or ``201`` if created.
If ``PATCH``, the expected response code is ``200``.

**Properties**

Same as `Get Form <#get-form>`_.

.. vale off

Delete Form
***********

.. vale on

.. code-block:: php

   <?php

   $form = $formApi->delete($id);

Delete a Form.

.. vale off

**HTTP Request**

.. vale on

``DELETE /forms/ID/delete``

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get Form <#get-form>`_.

.. vale off

Delete Form Fields
******************

.. vale on

The following examples show how to delete fields with ID 56 and 59.

.. code-block:: php

   <?php

   $form = $formApi->deleteFields($formId, array(56, 59));

Delete a Form fields.

.. vale off

**HTTP Request**

.. vale on

``DELETE /forms/ID/fields/delete?fields[]=56&fields[]=59``

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get Form <#get-form>`_.

.. vale off

Delete Form Actions
*******************

.. vale on

The following examples show how to delete actions with ID 56 and 59.

.. code-block:: php

   <?php

   $form = $formApi->deleteActions($formId, array(56, 59));

Delete a Form actions.

.. vale off

**HTTP Request**

.. vale on

``DELETE /forms/ID/actions/delete?actions[]=56&actions[]=59``

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get Form <#get-form>`_.

.. vale off

List Form Submissions
*********************

.. vale on

.. code-block:: php

   <?php

   $submissions = $formApi->getSubmissions($formId, $searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

**HTTP Request**

.. vale on

``GET /forms/FORM_ID/submissions``

**Query Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - ``formId``
     - ID of the Form you want to get submissions for
   * - ``search``
     - String or search command to filter entities by.
   * - ``start``
     - Starting row for the entities returned. Defaults to 0.
   * - ``limit``
     - Limit number of entities to return. Defaults to the system configuration for pagination - default of 30.
   * - ``orderBy``
     - Column to sort by. Can use any column listed in the response, also can use column of joined table with prefix. Sort by submitted date is ``s.date_submitted``
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
     "total": "1",
     "submissions": [
       {
         "id": 1,
         "ipAddress": {
           "ip": "127.0.0.1"
         },
         "form": {
           "id": 25,
           "name": "test",
           "alias": "test",
           "category": null
         },
         "lead": {
           "id": 2183,
           "points": 0,
           "color": null,
           "title": null,
           "firstname": null,
           "lastname": null,
           "company": null,
           "position": null,
           "email": "test@test.test",
           "phone": null,
           "mobile": null,
           "address1": null,
           "address2": null,
           "city": null,
           "state": null,
           "zipcode": null,
           "timezone": null,
           "country": null
         },
         "trackingId": null,
         "dateSubmitted": "2017-07-17T09:52:29+00:00",
         "referer": "http:\/\/mautic.dev\/s\/forms\/preview\/25",
         "page": null,
         "results": {
           "email": "test@test.test"
         }
       }
     ]
   }

**Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the submission
   * - ``ipAddress``
     - array
     - Associative array containing IP address of the client who made the submission
   * - ``form``
     - array
     - Simplified associative array of the Form containing id, name, alias and Category
   * - ``lead``
     - array
     - Associative array of the Contact containing the core values as well as custom fields
   * - ``dateSubmitted``
     - string
     - Date time string holding the ``UTC`` date and time when the submission took place
   * - ``referer``
     - string
     - ``HTTP`` referrer info
   * - ``results``
     - array
     - Associative array of the Form fields as the keys and submission values

.. vale off

List Form Submissions for a Contact
***********************************

.. vale on

.. code-block:: php

   <?php

   $submissions = $formApi->getSubmissionsForContact($formId, $contactId, $searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

**HTTP Request**

.. vale on

``GET /forms/FORM_ID/submissions/contact/CONTACT_ID``

Response and properties same as `Get Form Submissions <#get-form-submissions>`_. Parameters too except the ContactId got added.

.. vale off

Get Form Submission
*******************

.. vale on

.. code-block:: php

   <?php

   //...
   $form = $formApi->getSubmission($formId, $submissionId);

.. code-block:: json

   {
     "submission": {
       "id": 1,
       "ipAddress": {
         "ip": "127.0.0.1"
       },
       "form": {
         "id": 25,
         "name": "test",
         "alias": "test",
         "category": null
       },
       "lead": {
         "id": 2183,
         "points": 0,
         "color": null,
         "title": null,
         "firstname": null,
         "lastname": null,
         "company": null,
         "position": null,
         "email": "test@test.test",
         "phone": null,
         "mobile": null,
         "address1": null,
         "address2": null,
         "city": null,
         "state": null,
         "zipcode": null,
         "timezone": null,
         "country": null
       },
       "trackingId": null,
       "dateSubmitted": "2017-07-17T09:52:29+00:00",
       "referer": "http:\/\/mautic.dev\/s\/forms\/preview\/25",
       "page": null,
       "results": {
         "form_id": "25",
         "email": "test@test.test"
       }
     }
   }

Get an individual Form submission by ID.

.. vale off

**HTTP Request**

.. vale on

``GET /forms/FORM_ID/submissions/SUBMISSION_ID``

**Response**

``Expected Response Code: 200``

See JSON code example.

**Form Properties**

Same as `Get Form Submissions <#get-form-submissions>`_.
