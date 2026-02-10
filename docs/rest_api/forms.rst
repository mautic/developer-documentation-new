Forms
#####

Use this endpoint to manipulate and obtain details on Mautic's Forms.

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

HTTP request
============

.. vale on

``GET /forms/ID``

Response
========

``Expected Response Code: 200``

.. code-block:: json

   {
       "form": {
           "isPublished": true,
           "dateAdded": "2017-02-03T16:51:06+00:00",
           "dateModified": "2017-02-03T19:11:54+00:00",
           "createdBy": 1,
           "createdByUser": "John Doe",
           "modifiedBy": 1,
           "modifiedByUser": "John Doe",
           "id": 1,
           "name": "API Test Form",
           "description": "Form created via API",
           "alias": "api-test-form",
           "formType": "standalone",
           "cachedHtml": "<form id=\"mauticform_apitestform\">...</form>",
           "template": null,
           "inKioskMode": false,
           "renderStyle": false,
           "formAttributes": null,
           "noIndex": false,
           "progressiveProfilingLimit": null,
           "postAction": "return",
           "postActionProperty": null,
           "publishUp": null,
           "publishDown": null,
           "language": "en",
           "category": {
               "createdByUser": "John Doe",
               "modifiedByUser": "John Doe",
               "id": 1,
               "title": "Test Category",
               "alias": "test-category",
               "description": "Test category description",
               "color": "ab5959",
               "bundle": "form"
           },
           "fields": [
               {
                   "id": 1,
                   "label": "Email",
                   "alias": "email",
                   "type": "text",
                   "defaultValue": null,
                   "isRequired": true,
                   "validationMessage": null,
                   "helpMessage": null,
                   "order": 1,
                   "properties": {
                       "placeholder": "Enter your email"
                   },
                   "labelAttributes": null,
                   "inputAttributes": null,
                   "containerAttributes": null,
                   "leadField": "email",
                   "saveResult": true,
                   "isAutoFill": false,
                   "showWhenValueExists": false,
                   "showAfterXSubmissions": 0,
                   "isConditionallyHidden": false,
                   "parent": null,
                   "conditions": null,
                   "mappedField": "email",
                   "mappedObject": "contact"
               }
           ],
           "actions": [
               {
                   "id": 1,
                   "type": "email",
                   "name": "Send notification",
                   "description": "Send email notification",
                   "order": 1,
                   "properties": {
                       "subject": "New form submission",
                       "message": "A new form submission has been received.",
                       "email": "admin@example.com"
                   }
               }
           ]
       }
   }

Form properties
---------------

.. list-table::
   :widths: 25 25 50
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
     - string
     - Description of the Form
   * - ``alias``
     - string
     - Alias/slug of the Form
   * - ``formType``
     - string
     - Type of the Form - ``standalone`` or ``campaign``
   * - ``cachedHtml``
     - string
     - Cached HTML of the Form
   * - ``template``
     - string/null
     - Template used for the Form
   * - ``inKioskMode``
     - boolean
     - Whether the Form is in kiosk mode
   * - ``renderStyle``
     - boolean
     - Whether to render form with style
   * - ``formAttributes``
     - string/null
     - Custom form attributes
   * - ``noIndex``
     - boolean
     - Whether the Form should not be indexed by search engines
   * - ``progressiveProfilingLimit``
     - int/null
     - Progressive profiling limit
   * - ``postAction``
     - string
     - Action to take after form submission - ``return``, ``redirect``, or ``message``
   * - ``postActionProperty``
     - string/null
     - Additional property for post action - URL for redirect, message for message
   * - ``publishUp``
     - datetime/null
     - Date/time when the Form should be published
   * - ``publishDown``
     - datetime/null
     - Date/time when the Form should be unpublished
   * - ``language``
     - string
     - Language of the Form
   * - ``category``
     - object/null
     - Category the Form belongs to
   * - ``fields``
     - array
     - Array of Form fields
   * - ``actions``
     - array
     - Array of Form actions/submit actions
   * - ``isPublished``
     - boolean
     - Published state
   * - ``dateAdded``
     - datetime
     - Date/time Form was created
   * - ``createdBy``
     - int
     - ID of the User that created the Form
   * - ``createdByUser``
     - string
     - Name of the User that created the Form
   * - ``dateModified``
     - datetime/null
     - Date/time Form was last modified
   * - ``modifiedBy``
     - int
     - ID of the User that last modified the Form
   * - ``modifiedByUser``
     - string
     - Name of the User that last modified the Form

Form field properties
---------------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Field
   * - ``label``
     - string
     - Label of the Field
   * - ``alias``
     - string
     - Alias/name of the Field
   * - ``type``
     - string
     - Type of the Field, for example ``text``, ``email``, ``select``, ``textarea``
   * - ``defaultValue``
     - string/null
     - Default value of the Field
   * - ``isRequired``
     - boolean
     - Whether the Field is required
   * - ``validationMessage``
     - string/null
     - Custom validation message
   * - ``helpMessage``
     - string/null
     - Help message for the Field
   * - ``order``
     - int
     - Order of the Field in the Form
   * - ``properties``
     - object
     - Additional properties specific to the Field type
   * - ``labelAttributes``
     - string/null
     - Custom attributes for the Field label
   * - ``inputAttributes``
     - string/null
     - Custom attributes for the Field input
   * - ``containerAttributes``
     - string/null
     - Custom attributes for the Field container
   * - ``leadField``
     - string
     - Contact field the Form field maps to (deprecated, use mappedField/mappedObject)
   * - ``saveResult``
     - boolean
     - Whether to save the Field result
   * - ``isAutoFill``
     - boolean
     - Whether to auto-fill the Field
   * - ``showWhenValueExists``
     - boolean
     - Whether to show field when value exists
   * - ``showAfterXSubmissions``
     - int
     - Show field after X submissions
   * - ``isConditionallyHidden``
     - boolean
     - Whether the Field is conditionally hidden
   * - ``parent``
     - int/null
     - ID of the parent Field for conditional fields
   * - ``conditions``
     - object/null
     - Conditions for showing the Field
   * - ``mappedField``
     - string
     - Contact/Company field the Form field maps to
   * - ``mappedObject``
     - string
     - Object the Field maps to - ``contact`` or ``company``

Form action properties
----------------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Action
   * - ``type``
     - string
     - Type of the Action, for example ``email``, ``lead.changetags``, ``lead.pointschange``
   * - ``name``
     - string
     - Name of the Action
   * - ``description``
     - string
     - Description of the Action
   * - ``order``
     - int
     - Order of the Action execution
   * - ``properties``
     - object
     - Properties specific to the Action type

.. vale off

List Forms
**********

.. vale on

.. code-block:: php

   <?php

   //...
   $forms = $formApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

Returns a list of Forms available to the User. This list is filterable and sortable.

.. vale off

HTTP request
============

.. vale on

``GET /forms``

Query parameters
----------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Name
     - Description
   * - ``search``
     - String or search command to filter entities by.
   * - ``start``
     - Starting row for the entities returned. Defaults to 0.
   * - ``limit``
     - Limit number of entities to return. Defaults to the system configuration for pagination, which is 30 by default.
   * - ``orderBy``
     - Column to sort by. Can use any column listed in the response. However, you need to change all properties in the response written in ``camelCase`` a bit. Before every capital, add an underscore ``_`` and then change the capital letters to non-capital letters. So ``dateAdded`` becomes ``date_added``, ``modifiedBy`` becomes ``modified_by``, etc.
   * - ``orderByDir``
     - Sort direction: ``asc`` or ``desc``.
   * - ``publishedOnly``
     - Only return currently published entities.
   * - ``minimal``
     - Return only array of entities without additional lists in it.

Response
========

``Expected Response Code: 200``

.. code-block:: json

   {
       "total": 1,
       "forms": {
           "1": {
               "isPublished": true,
               "dateAdded": "2017-02-03T16:51:06+00:00",
               "dateModified": "2017-02-03T19:11:54+00:00",
               "createdBy": 1,
               "createdByUser": "John Doe",
               "modifiedBy": 1,
               "modifiedByUser": "John Doe",
               "id": 1,
               "name": "API Test Form",
               "description": "Form created via API",
               "alias": "api-test-form",
               "formType": "standalone",
               "cachedHtml": "<form id=\"mauticform_apitestform\">...</form>",
               "template": null,
               "inKioskMode": false,
               "renderStyle": false,
               "postAction": "return",
               "postActionProperty": null,
               "publishUp": null,
               "publishDown": null,
               "language": "en",
               "category": null,
               "fields": [],
               "actions": []
           }
       }
   }

Properties
----------

Same as :ref:`rest_api/forms:Get Form`.

.. vale off

Create Form
***********

.. vale on

.. code-block:: php

   <?php

   $data = array(
       'name'        => 'Form created via API',
       'formType'    => 'standalone',
       'description' => 'This is a test form created via API',
       'fields'      => array(
           array(
               'label'        => 'Email',
               'type'         => 'text',
               'alias'        => 'email',
               'mappedObject' => 'contact',
               'mappedField'  => 'email',
               'isRequired'   => true,
           ),
           array(
               'label' => 'Submit',
               'type'  => 'button',
           ),
       ),
       'actions' => array(
           array(
               'name'        => 'Send notification',
               'type'        => 'email',
               'description' => 'Send email notification',
               'properties'  => array(
                   'subject' => 'New form submission',
                   'message' => 'A new form submission has been received.',
                   'email'   => 'admin@example.com'
               ),
           ),
       ),
       'postAction' => 'return',
   );

   $form = $formApi->create($data);

Create a new Form.

.. vale off

HTTP request
============

.. vale on

``POST /forms/new``

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
     - Form name is the only required field
   * - ``description``
     - string
     - Description of the Form
   * - ``alias``
     - string
     - Alias/slug of the Form (auto-generated if not provided)
   * - ``formType``
     - string
     - Type of the Form - ``standalone`` or ``campaign``
   * - ``template``
     - string
     - Template to use for the Form
   * - ``inKioskMode``
     - boolean
     - Whether the Form should be in kiosk mode
   * - ``renderStyle``
     - boolean
     - Whether to render form with style
   * - ``formAttributes``
     - string
     - Custom form attributes
   * - ``noIndex``
     - boolean
     - Whether the Form should not be indexed by search engines
   * - ``progressiveProfilingLimit``
     - int
     - Progressive profiling limit
   * - ``postAction``
     - string
     - Action after form submission - ``return``, ``redirect``, or ``message``
   * - ``postActionProperty``
     - string
     - Additional property for post action
   * - ``publishUp``
     - datetime
     - Date/time when the Form should be published
   * - ``publishDown``
     - datetime
     - Date/time when the Form should be unpublished
   * - ``language``
     - string
     - Language of the Form
   * - ``category``
     - int
     - ID of the category to assign the Form to
   * - ``fields``
     - array
     - Array of Form fields to create
   * - ``actions``
     - array
     - Array of Form actions to create
   * - ``isPublished``
     - boolean
     - Published state

Response
========

``Expected Response Code: 201``

Properties
----------

Same as :ref:`rest_api/forms:Get Form`.

.. vale off

Edit Form
*********

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'name'        => 'Updated form name',
       'description' => 'Updated description',
       'fields'      => array(
           array(
               'id'           => 1, // Existing field
               'label'        => 'Updated Email Label',
               'type'         => 'text',
               'alias'        => 'email',
               'mappedObject' => 'contact',
               'mappedField'  => 'email',
               'isRequired'   => true,
           ),
           array(
               'label'        => 'First Name', // New field
               'type'         => 'text',
               'alias'        => 'first_name',
               'mappedObject' => 'contact',
               'mappedField'  => 'firstname',
           ),
       ),
   );

   // Create new a Form of ID 1 isn't found?
   $createIfNotFound = true;

   $form = $formApi->edit($id, $data, $createIfNotFound);

Edit a Form. Note that this supports PUT or PATCH depending on the desired behavior.

**PUT** creates a Form if the given ID doesn't exist and clears all the Form information, adds the information from the request.
**PATCH** fails if the Form with the given ID doesn't exist and updates the Form field values with the values from the request.

.. vale off

HTTP request
============

.. vale on

To edit a Form and return a 404 if the Form isn't found:

``PATCH /forms/ID/edit``

To edit a Form and create a new one if the Form isn't found:

``PUT /forms/ID/edit``

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
     - Form name
   * - ``description``
     - string
     - Description of the Form
   * - ``alias``
     - string
     - Alias/slug of the Form
   * - ``formType``
     - string
     - Type of the Form - ``standalone`` or ``campaign``
   * - ``template``
     - string
     - Template to use for the Form
   * - ``inKioskMode``
     - boolean
     - Whether the Form should be in kiosk mode
   * - ``renderStyle``
     - boolean
     - Whether to render form with style
   * - ``formAttributes``
     - string
     - Custom form attributes
   * - ``noIndex``
     - boolean
     - Whether the Form should not be indexed by search engines
   * - ``progressiveProfilingLimit``
     - int
     - Progressive profiling limit
   * - ``postAction``
     - string
     - Action after form submission - ``return``, ``redirect``, or ``message``
   * - ``postActionProperty``
     - string
     - Additional property for post action
   * - ``publishUp``
     - datetime
     - Date/time when the Form should be published
   * - ``publishDown``
     - datetime
     - Date/time when the Form should be unpublished
   * - ``language``
     - string
     - Language of the Form
   * - ``category``
     - int
     - ID of the category to assign the Form to
   * - ``fields``
     - array
     - Array of Form fields (include ``id`` for existing fields to update them)
   * - ``actions``
     - array
     - Array of Form actions (include ``id`` for existing actions to update them)
   * - ``isPublished``
     - boolean
     - Published state

Response
========

If ``PUT``, the expected response code is ``200`` if the Form was edited or ``201`` if created.
If ``PATCH``, the expected response code is ``200``.

Properties
----------

Same as :ref:`rest_api/forms:Get Form`.

.. vale off

Delete Form
***********

.. vale on

.. code-block:: php

   <?php

   $form = $formApi->delete($id);

Delete a Form.

.. vale off

HTTP request
============

.. vale on

``DELETE /forms/ID/delete``

Response
========

``Expected Response Code: 200``

Properties
----------

Same as :ref:`rest_api/forms:Get Form`.

.. vale off

Delete Form fields
******************

.. vale on

.. code-block:: php

   <?php

   $formApi->deleteFields($formId, array(1, 2, 3));

Delete specific fields from a Form.

.. vale off

HTTP request
============

.. vale on

``DELETE /forms/ID/fields/delete``

POST parameters
---------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``fields``
     - array
     - Array of field IDs to delete

Response
========

``Expected Response Code: 200``

Properties
----------

Same as :ref:`rest_api/forms:Get Form`.

.. vale off

Delete Form Actions
*******************

.. vale on

.. code-block:: php

   <?php

   $formApi->deleteActions($formId, array(1, 2));

Delete specific actions from a Form.

.. vale off

HTTP request
============

.. vale on

``DELETE /forms/ID/actions/delete``

POST parameters
---------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``actions``
     - array
     - Array of action IDs to delete

Response
========

``Expected Response Code: 200``

Properties
----------

Same as :ref:`rest_api/forms:Get Form`.

Get Form submissions
********************

.. vale on

.. code-block:: php

   <?php

   $submissions = $formApi->getSubmissions($formId, $searchFilter, $start, $limit, $orderBy, $orderByDir);

Get a list of submissions for a specific Form.

.. vale off

HTTP request
============

.. vale on

``GET /forms/ID/submissions``

Query parameters
----------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Name
     - Description
   * - ``search``
     - String or search command to filter entities by.
   * - ``start``
     - Starting row for the entities returned. Defaults to 0.
   * - ``limit``
     - Limit number of entities to return. Defaults to the system configuration for pagination, which is 30 by default.
   * - ``orderBy``
     - Column to sort by. Can use any column listed in the response.
   * - ``orderByDir``
     - Sort direction: ``asc`` or ``desc``.

Response
========

``Expected Response Code: 200``

.. code-block:: json

   {
       "total": 1,
       "submissions": [
           {
               "id": 1,
               "ipAddress": {
                   "id": 1,
                   "ipAddress": "127.0.0.1"
               },
               "form": {
                   "id": 1,
                   "name": "API Test Form",
                   "alias": "api-test-form"
               },
               "lead": {
                   "id": 1,
                   "points": 0,
                   "color": null,
                   "fields": {
                       "core": {
                           "firstname": {
                               "id": "1",
                               "label": "First Name",
                               "alias": "firstname",
                               "type": "text",
                               "group": "core",
                               "value": "John"
                           },
                           "lastname": {
                               "id": "2",
                               "label": "Last Name",
                               "alias": "lastname",
                               "type": "text",
                               "group": "core",
                               "value": "Doe"
                           },
                           "email": {
                               "id": "3",
                               "label": "Email",
                               "alias": "email",
                               "type": "email",
                               "group": "core",
                               "value": "john@doe.com"
                           }
                       }
                   }
               },
               "trackingId": "abc123def456",
               "dateSubmitted": "2017-02-03T16:51:06+00:00",
               "referer": "https://example.com/form/1",
               "page": null,
               "results": {
                   "email": "john@doe.com",
                   "firstname": "John",
                   "lastname": "Doe"
               }
           }
       ]
   }

.. vale off

Get Form submission
*******************

.. vale on

.. code-block:: php

   <?php

   $submission = $formApi->getSubmission($formId, $submissionId);

Get an individual submission for a specific Form.

.. vale off

HTTP request
============

.. vale on

``GET /forms/FORM_ID/submissions/SUBMISSION_ID``

Response
========

``Expected Response Code: 200``

.. code-block:: json

   {
       "submission": {
           "id": 1,
           "ipAddress": {
               "id": 1,
               "ipAddress": "127.0.0.1"
           },
           "form": {
               "id": 1,
               "name": "API Test Form",
               "alias": "api-test-form"
           },
           "lead": {
               "id": 1,
               "points": 0,
               "color": null,
               "fields": {
                   "core": {
                       "firstname": {
                           "id": "1",
                           "label": "First Name",
                           "alias": "firstname",
                           "type": "text",
                           "group": "core",
                           "value": "John"
                       },
                       "email": {
                           "id": "3",
                           "label": "Email",
                           "alias": "email",
                           "type": "email",
                           "group": "core",
                           "value": "john@doe.com"
                       }
                   }
               }
           },
           "trackingId": "abc123def456",
           "dateSubmitted": "2017-02-03T16:51:06+00:00",
           "referer": "https://example.com/form/1",
           "page": null,
           "results": {
               "email": "john@doe.com",
               "firstname": "John"
           }
       }
   }

.. vale off

Get Contact Form submissions
****************************

.. vale on

.. code-block:: php

   <?php

   $submissions = $formApi->getContactSubmissions($formId, $contactId, $searchFilter, $start, $limit, $orderBy, $orderByDir);

Get submissions for a specific Form and Contact.

.. vale off

HTTP request
============

.. vale on

``GET /forms/FORM_ID/submissions/contact/CONTACT_ID``

Query parameters
----------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Name
     - Description
   * - ``search``
     - String or search command to filter entities by.
   * - ``start``
     - Starting row for the entities returned. Defaults to 0.
   * - ``limit``
     - Limit number of entities to return. Defaults to the system configuration for pagination, which is 30 by default.
   * - ``orderBy``
     - Column to sort by. Can use any column listed in the response.
   * - ``orderByDir``
     - Sort direction: ``asc`` or ``desc``.

Response
========

``Expected Response Code: 200``

Same format as :ref:`rest_api/forms:Get Form Submissions`.

Form field types
================

Mautic supports various field types for Forms. Here are the most common types:

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Type
     - Description
     - Properties
   * - ``text``
     - Single line text input
     - ``placeholder``, ``maxlength``
   * - ``textarea``
     - Multi-line text input
     - ``placeholder``, ``rows``, ``maxlength``
   * - ``email``
     - Email input with validation
     - ``placeholder``
   * - ``number``
     - Number input
     - ``placeholder``, ``min``, ``max``, ``step``
   * - ``tel``
     - Telephone input
     - ``placeholder``
   * - ``url``
     - URL input with validation
     - ``placeholder``
   * - ``select``
     - Dropdown selection
     - ``list`` (options), ``multiple``, ``syncList``
   * - ``radio``
     - Radio button group
     - ``list`` (options)
   * - ``checkbox``
     - Checkbox input
     - ``list`` (options)
   * - ``checkboxgrp``
     - Checkbox group
     - ``list`` (options)
   * - ``country``
     - Country selection dropdown
     - None
   * - ``date``
     - Date picker
     - ``format``
   * - ``datetime``
     - Date and time picker
     - ``format``
   * - ``time``
     - Time picker
     - ``format``
   * - ``button``
     - Submit button
     - None
   * - ``hidden``
     - Hidden field
     - None
   * - ``file``
     - File upload
     - ``allowed_file_size``, ``allowed_file_extensions``
   * - ``captcha``
     - CAPTCHA field
     - None
   * - ``pagebreak``
     - Page break for multi-page forms
     - None

Form action types
=================

Forms can have various actions that are executed when the form is submitted:

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Type
     - Description
     - Properties
   * - ``email``
     - Send email notification
     - ``subject``, ``message``, ``email``, ``copy_lead``
   * - ``lead.changetags``
     - Add/remove tags from contact
     - ``add_tags``, ``remove_tags``
   * - ``lead.pointschange``
     - Change contact points
     - ``points``, ``operator``
   * - ``lead.changeowner``
     - Change contact owner
     - ``owner``
   * - ``lead.addtocompany``
     - Add contact to company
     - ``company``
   * - ``asset.download``
     - Trigger asset download
     - ``asset``
   * - ``form.submit.redirect``
     - Redirect to URL
     - ``redirect_url``
   * - ``form.submit.message``
     - Show message
     - ``message``

Progressive profiling
=====================

Progressive profiling allows you to collect more information from Contacts over time by showing different fields based on previous submissions. To enable progressive profiling:

#. Set ``progressiveProfilingLimit`` on the form
#. Configure fields with ``showAfterXSubmissions`` property
#. Use ``showWhenValueExists`` to hide fields when contact already has a value

Conditional fields
==================

Fields can be conditionally shown based on other field values:

#. Set the ``parent`` field ID
#. Configure ``conditions`` with expression type (``eq``, ``neq``, ``in``, ``!in``)
#. Set ``isConditionallyHidden`` to true

Mapped fields
=============

Form fields can be mapped to Contact or Company fields:

* Use ``mappedObject`` to specify ``contact`` or ``company``
* Use ``mappedField`` to specify the target field name
* The deprecated ``leadField`` property is still supported for backward compatibility