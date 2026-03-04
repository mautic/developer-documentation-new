Forms
#####

Use this endpoint to manipulate and obtain details on Mautic's Forms.

Using the Mautic API library
****************************

.. vale off

You can interact with this API using the :xref:`Mautic API Library` as below, or the various HTTP endpoints described in this document.

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
   $formApi  = $api->newApi("forms", $auth, $apiUrl);

.. vale off

Get Form
********

.. vale on

Retrieves an individual Form.

.. code-block:: php

   <?php

   //...
   $form = $formApi->get($id);

.. vale off

HTTP request
============

.. vale on

``GET /forms/ID``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Form.

.. _get Form response:

.. code-block:: json

   {
      "form": {
          "isPublished": true,
          "dateAdded": "2026-02-19T07:06:12+00:00",
          "dateModified": "2026-02-19T07:10:06+00:00",
          "createdBy": 1,
          "createdByUser": "Admin Mautic",
          "modifiedBy": 1,
          "modifiedByUser": "Admin Mautic",
          "id": 2,
          "name": "Acme Global Conference Registration",
          "alias": "acme_globa",
          "category": {
              "createdByUser": "Admin Mautic",
              "modifiedByUser": null,
              "id": 1,
              "title": "Company attendees",
              "alias": "company-attendees",
              "description": null,
              "color": null,
              "bundle": "form"
          },
          "description": "<p><span style=\"color:rgb(186,33,33);\"><span class=\"s2\" style=\"box-sizing:border-box;\">Acme Global Conference registration.</span></span></p>",
          "cachedHtml": "\n<style type=\"text/css\" scoped>\n    .mauticform_wrapper { max-width: 600px; margin: 10px auto; }\n    .mauticform-innerform {}\n    .mauticform-post-success {}\n    .mauticform-name { font-weight: bold; font-size: 1.5em; margin-bottom: 3px; }\n    .mauticform-description { margin-top: 2px; margin-bottom: 10px; }\n    .mauticform-error { margin-bottom: 10px; color: red; }\n    .mauticform-message { margin-bottom: 10px; color: green; }\n    .mauticform-row { display: block; margin-bottom: 20px; }\n    .mauticform-label { font-size: 1.1em; display: block; font-weight: bold; margin-bottom: 5px; }\n    .mauticform-row.mauticform-required .mauticform-label:after { color: #e32; content: \" *\"; display: inline; }\n    .mauticform-helpmessage { display: block; font-size: 0.9em; margin-bottom: 3px; }\n    .mauticform-errormsg { display: block; color: red; margin-top: 2px; }\n    .mauticform-selectbox, .mauticform-input, .mauticform-textarea { width: 100%; padding: 0.5em 0.5em; border: 1px solid #CCC; background: #fff; box-shadow: 0px 0px 0px #fff inset; border-radius: 4px; box-sizing: border-box; }\n    .mauticform-checkboxgrp-row {}\n    .mauticform-checkboxgrp-label { font-weight: normal; }\n    .mauticform-checkboxgrp-checkbox {}\n    .mauticform-radiogrp-row {}\n    .mauticform-radiogrp-label { font-weight: normal; }\n    .mauticform-radiogrp-radio {}\n    .mauticform-button-wrapper .mauticform-button.btn-ghost, .mauticform-pagebreak-wrapper .mauticform-pagebreak.btn-ghost { color: #5d6c7c;background-color: #ffffff;border-color: #dddddd;}\n    .mauticform-button-wrapper .mauticform-button, .mauticform-pagebreak-wrapper .mauticform-pagebreak { display: inline-block;margin-bottom: 0;font-weight: 600;text-align: center;vertical-align: middle;cursor: pointer;background-image: none;border: 1px solid transparent;white-space: nowrap;padding: 6px 12px;font-size: 13px;line-height: 1.3856;border-radius: 3px;-webkit-user-select: none;-moz-user-select: none;-ms-user-select: none;user-select: none;}\n    .mauticform-button-wrapper .mauticform-button.btn-ghost[disabled], .mauticform-pagebreak-wrapper .mauticform-pagebreak.btn-ghost[disabled] { background-color: #ffffff; border-color: #dddddd; opacity: 0.75; cursor: not-allowed; }\n    .mauticform-pagebreak-wrapper .mauticform-button-wrapper {  display: inline; }\n\n    /**\n    * @see https://github.com/TarekRaafat/autoComplete.js/blob/master/dist/css/autoComplete.02.css.\n    */\n    .autoComplete_wrapper {position: relative;}\n    .autoComplete_wrapper > input::placeholder {transition: all 0.3s ease;}\n    .autoComplete_wrapper > ul {position: absolute;max-height: 226px;overflow-y: scroll;top: 100%;left: 0;right: 0;padding: 0;margin: 0.5rem 0 0 0;border-radius: 4px;background-color: #fff;border: 1px solid rgba(33, 33, 33, 0.1);z-index: 1000;outline: none;}\n    .autoComplete_wrapper > ul > li {padding: 10px 20px;list-style: none;text-align: left;font-size: 16px;color: #212121;transition: all 0.1s ease-in-out;border-radius: 3px;background-color: rgba(255, 255, 255, 1);white-space: nowrap;overflow: hidden;text-overflow: ellipsis;transition: all 0.2s ease;}\n    .autoComplete_wrapper > ul > li > span {float: right;}\n    .autoComplete_wrapper > ul > li::selection {color: rgba(#ffffff, 0);background-color: rgba(#ffffff, 0);}\n    .autoComplete_wrapper > ul > li:hover {cursor: pointer;background-color: rgba(123, 123, 123, 0.1);}\n    .autoComplete_wrapper > ul > li mark {background-color: transparent;font-weight: bold;}\n    .autoComplete_wrapper > ul > li mark::selection {background-color: rgba(#ffffff, 0);}\n    .autoComplete_wrapper > ul > li[aria-selected=\"true\"] {background-color: rgba(123, 123, 123, 0.1);}\n    @media only screen and (max-width: 600px) {\n      .autoComplete_wrapper > input {width: 18rem;}\n    }\n</style>\n\n<style type=\"text/css\" scoped>\n    .mauticform-field-hidden { display:none }\n</style>\n<div id=\"mauticform_wrapper_acmeglobalconferenceregistration\" class=\"mauticform_wrapper\">\n    <form autocomplete=\"false\" role=\"form\" method=\"post\" action=\"https://m5-tester.ddev.site/form/submit?formId=2\" id=\"mauticform_acmeglobalconferenceregistration\" data-mautic-form=\"acmeglobalconferenceregistration\" enctype=\"multipart/form-data\" ><div class=\"mauticform-error\" id=\"mauticform_acmeglobalconferenceregistration_error\"></div>\n            <div class=\"mauticform-message\" id=\"mauticform_acmeglobalconferenceregistration_message\"></div><div class=\"mauticform-innerform\">\n            <div class=\"mauticform-page-wrapper mauticform-page-1\" data-mautic-form-page=\"1\" >\n                  \n\n\n      \n\n    \n\n\n    \n\n\n<div id=\"mauticform_acmeglobalconferenceregistration_topic_preference\"class=\"mauticform-row mauticform-text mauticform-field-1\">\n  <label id=\"mauticform_label_acmeglobalconferenceregistration_topic_preference\"for=\"mauticform_input_acmeglobalconferenceregistration_topic_preference\"class=\"mauticform-label\">Topic preference</label>\n  <span class=\"mauticform-helpmessage\">The talk that you're looking forward to</span>\n      <textarea name=\"mauticform[topic_preference]\"id=\"mauticform_input_acmeglobalconferenceregistration_topic_preference\"class=\"mauticform-textarea\"></textarea>\n  \n  <span class=\"mauticform-errormsg\" style=\"display:none;\"></span>\n</div>\n                  \n      \n  \n    \n    \n<div id=\"mauticform_acmeglobalconferenceregistration_submit\"class=\"mauticform-row mauticform-button-wrapper mauticform-field-2\">\n  <button class=\"btn btn-ghost mauticform-button\"name=\"mauticform[submit]\"value=\"1\"id=\"mauticform_input_acmeglobalconferenceregistration_submit\"type=\"submit\">Submit</button>\n</div>\n                  </div></div><input type=\"hidden\" name=\"mauticform[formId]\" id=\"mauticform_acmeglobalconferenceregistration_id\" value=\"2\"/>\n        <input type=\"hidden\" name=\"mauticform[return]\" id=\"mauticform_acmeglobalconferenceregistration_return\" value=\"\"/>\n        <input type=\"hidden\" name=\"mauticform[formName]\" id=\"mauticform_acmeglobalconferenceregistration_name\" value=\"acmeglobalconferenceregistration\"/>\n        \n    </form>\n</div>\n",
          "publishUp": "2026-02-19T07:00:00+00:00",
          "publishDown": "2026-03-06T08:05:00+00:00",
          "fields": [
              {
                  "id": 2,
                  "label": "Topic preference",
                  "showLabel": true,
                  "alias": "topic_preference",
                  "type": "textarea",
                  "defaultValue": null,
                  "isRequired": false,
                  "validationMessage": null,
                  "helpMessage": "The talk that you're looking forward to",
                  "order": 1,
                  "properties": [],
                  "validation": [],
                  "parent": null,
                  "conditions": [],
                  "labelAttributes": null,
                  "inputAttributes": null,
                  "containerAttributes": null,
                  "leadField": null,
                  "saveResult": true,
                  "isAutoFill": true,
                  "mappedObject": "company",
                  "mappedField": null
              },
              {
                  "id": 3,
                  "label": "Submit",
                  "showLabel": true,
                  "alias": "submit",
                  "type": "button",
                  "defaultValue": null,
                  "isRequired": false,
                  "validationMessage": null,
                  "helpMessage": null,
                  "order": 2,
                  "properties": [],
                  "validation": [],
                  "parent": null,
                  "conditions": [],
                  "labelAttributes": null,
                  "inputAttributes": "class=\"btn btn-ghost\"",
                  "containerAttributes": null,
                  "leadField": null,
                  "saveResult": true,
                  "isAutoFill": false,
                  "mappedObject": null,
                  "mappedField": null
              }
          ],
          "actions": [
              {
                  "id": 13,
                  "name": "Add company score",
                  "description": null,
                  "type": "lead.scorecontactscompanies",
                  "order": 1,
                  "properties": {
                      "score": 5
                  }
              }
          ],
          "template": "goldstar",
          "inKioskMode": true,
          "renderStyle": true,
          "formType": "standalone",
          "postAction": "message",
          "postActionProperty": "Thank you for registering and see you there!",
          "noIndex": false,
          "formAttributes": null,
          "language": "en_US"
      }
   }

.. _get Form properties:

Form properties
---------------

.. vale off

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``isPublished``
     - boolean
     - Form publication status
   * - ``dateAdded``
     - datetime
     - Form record creation date and time
   * - ``dateModified``
     - datetime
     - Form record last modification date and time
   * - ``createdBy``
     - integer
     - ID of the User who created the Form
   * - ``createdByUser``
     - string
     - Name of the User who created the Form
   * - ``modifiedBy``
     - integer
     - ID of the User who last modified the Form
   * - ``modifiedByUser``
     - string
     - Name of the User who last modified the Form
   * - ``id``
     - integer
     - ID of the Form
   * - ``name``
     - string
     - Form name
   * - ``alias``
     - string
     - The auto-generated alias or slug of the Form
   * - ``category``
     - object
     - The Category assigned to the Form
   * - ``description``
     - string
     - Description of the Form
   * - ``cachedHtml``
     - string
     - The auto-generated HTML and CSS of the Form
   * - ``publishUp``
     - datetime
     - Activation date and time for the Form
   * - ``publishDown``
     - datetime
     - Deactivation date and time for the Form
   * - ``fields``
     - associative array
     - Associative array of Form Fields. The keys must correspond to the field aliases described in the :ref:`Form Field properties <get Form Field properties>`
   * - ``actions``
     - associative array
     - Associative array of Form actions. The keys must correspond to the action aliases described in the :ref:`Form action properties <get Form action properties>`
   * - ``template``
     - string
     - Theme used to style the Form
   * - ``inKioskMode``
     - boolean
     - Kiosk mode status - set to ``1`` or ``true`` to turn off cookie tracking and IP association for submissions. When not set, it defaults to track visitor data
   * - ``renderStyle``
     - boolean
     - Render style status - set to ``0`` or ``false`` to turn off the inclusion of template CSS in the Form output. When not set, it defaults to on
   * - ``formType``
     - string
     - Type of the Form - ``standalone`` or ``campaign``
   * - ``postAction``
     - string
     - Action to perform after submission. Must be one of:
     
       * ``return``: no action taken
       * ``redirect``: redirects to a specified URL
       * ``message``: displays a success message
   * - ``postActionProperty``
     - string
     - The data associated with the ``postAction``. Contains the redirect URL when set to ``redirect``, or the success message when set to ``message``
   * - ``noIndex``
     - boolean
     - Search indexing status - set to ``1`` or ``true`` to send a ``noindex`` HTTP header. When not set, it defaults to indexing
   * - ``formAttributes``
     - string
     - Custom HTML attributes to add to the opening ``<form>`` tag
   * - ``language``
     - string
     - The language code for the Form, such as ``en_US``, ``fr``, and so on

.. vale on

.. _get Form Field properties:

.. vale off
   
Form Field properties
---------------------

.. vale on

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - integer
     - ID of the field
   * - ``label``
     - string
     - Label displayed for the field
   * - ``showLabel``
     - boolean
     - Label visibility status - ``0`` or ``false`` hides the label on the Form. When not set, the system shows the label by default
   * - ``alias``
     - string
     - The auto-generated alias or slug of the field
   * - ``type``
     - string
     - Type of field, such as ``text``, ``email``, ``select``, and so on. Refer to :ref:`Form Field types <Form Field types>` for details
   * - ``defaultValue``
     - string
     - Initial value assigned to the field
   * - ``isRequired``
     - boolean
     - Required status - ``1`` or ``true`` indicates the field is mandatory for submission. When not set, it defaults to optional
   * - ``validationMessage``
     - string
     - Custom message that appears when a User leaves a required field empty
   * - ``helpMessage``
     - string
     - Text provided to assist Users in completing the field
   * - ``order``
     - integer
     - Numerical position of the field within the Form
   * - ``properties``
     - object
     - Specific configuration options based on the field type
   * - ``validation``
     - object
     - List of validation rules applied to the field
   * - ``parent``
     - integer
     - ID of the parent field for conditional logic
   * - ``conditions``
     - object
     - Configuration for conditional logic, containing:
      
       * ``expr``: comparison operator. Accepts include - ``in`` or exclude - ``notIn``
       * ``values``: array of values to match against the parent field
       * ``any``: match logic, where ``1`` matches any value and ``0`` matches only the specific values provided
   * - ``labelAttributes``
     - string
     - HTML attributes for the label element
   * - ``inputAttributes``
     - string
     - HTML attributes for the input element
   * - ``containerAttributes``
     - string
     - HTML attributes for the field wrapper or container
   * - ``leadField``
     - string
     - Internal reference name for the mapped field on the target object
   * - ``saveResult``
     - boolean
     - Result storage status - ``0`` or ``false`` prevents Mautic from storing the submitted value in the database. When not set, it defaults to save the submission
   * - ``isAutoFill``
     - boolean
     - Auto-fill status - ``0`` or ``false`` prevents the field from pre-filling with known data and prevents Mautic from saving the value to the database. Mautic pre-fills and saves the data by default
   * - ``mappedObject``
     - string
     - The object type that the field maps to - ``contact`` or ``company``
   * - ``mappedField``
     - string
     - The specific Contact or Company field that the Form Field maps to

.. _get Form action properties:
    
Form action properties
----------------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - integer
     - ID of the action
   * - ``name``
     - string
     - Name of the action
   * - ``description``
     - string
     - Description of the action
   * - ``type``
     - string
     - Type of action, such as ``lead.scorecontactscompanies``, ``email.send.lead``, and so on. Refer to :ref:`Form action types <Form action types>` for details
   * - ``order``
     - integer
     - The numerical position of the action within the Form
   * - ``properties``
     - object
     - The settings for the specific action type

.. vale off

List Forms
**********

.. vale on

Retrieves a list of Forms.

.. code-block:: php

   <?php

   //...
   $forms = $formApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

HTTP request
============

.. vale on

``GET /forms``

Query parameters
----------------

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``searchFilter``
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
       
       **Note**: convert ``camelCase`` properties to ``snake_case``. For example, ``dateAdded`` becomes ``date_added``, ``webhookUrl`` becomes ``webhook_url``, and so on
   * - ``orderByDir``
     - string
     - Order direction - ``asc`` or ``desc``
   * - ``publishedOnly``
     - boolean
     - Returns only currently published entities
   * - ``minimal``
     - boolean
     - Returns only a simple mapped object of entities without additional lists in it

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Forms list.

.. code-block:: json

   {
      "total": 2,
      "forms": [
          {
              "isPublished": true,
              "dateAdded": "2026-02-19T07:06:12+00:00",
              "dateModified": "2026-02-19T07:10:06+00:00",
              "createdBy": 1,
              "createdByUser": "Admin Mautic",
              "modifiedBy": 1,
              "modifiedByUser": "Admin Mautic",
              "id": 2,
              "name": "Acme Global Conference Registration",
              "alias": "acme_globa",
              "category": {
                  "createdByUser": "Admin Mautic",
                  "modifiedByUser": null,
                  "id": 1,
                  "title": "Company attendees",
                  "alias": "company-attendees",
                  "description": null,
                  "color": null,
                  "bundle": "form"
              },
              "description": "<p><span style=\"color:rgb(186,33,33);\"><span class=\"s2\" style=\"box-sizing:border-box;\">Acme Global Conference registration.</span></span></p>",
              "cachedHtml": "\n<style type=\"text/css\" scoped>\n    .mauticform_wrapper { max-width: 600px; margin: 10px auto; }\n    .mauticform-innerform {}\n    .mauticform-post-success {}\n    .mauticform-name { font-weight: bold; font-size: 1.5em; margin-bottom: 3px; }\n    .mauticform-description { margin-top: 2px; margin-bottom: 10px; }\n    .mauticform-error { margin-bottom: 10px; color: red; }\n    .mauticform-message { margin-bottom: 10px; color: green; }\n    .mauticform-row { display: block; margin-bottom: 20px; }\n    .mauticform-label { font-size: 1.1em; display: block; font-weight: bold; margin-bottom: 5px; }\n    .mauticform-row.mauticform-required .mauticform-label:after { color: #e32; content: \" *\"; display: inline; }\n    .mauticform-helpmessage { display: block; font-size: 0.9em; margin-bottom: 3px; }\n    .mauticform-errormsg { display: block; color: red; margin-top: 2px; }\n    .mauticform-selectbox, .mauticform-input, .mauticform-textarea { width: 100%; padding: 0.5em 0.5em; border: 1px solid #CCC; background: #fff; box-shadow: 0px 0px 0px #fff inset; border-radius: 4px; box-sizing: border-box; }\n    .mauticform-checkboxgrp-row {}\n    .mauticform-checkboxgrp-label { font-weight: normal; }\n    .mauticform-checkboxgrp-checkbox {}\n    .mauticform-radiogrp-row {}\n    .mauticform-radiogrp-label { font-weight: normal; }\n    .mauticform-radiogrp-radio {}\n    .mauticform-button-wrapper .mauticform-button.btn-ghost, .mauticform-pagebreak-wrapper .mauticform-pagebreak.btn-ghost { color: #5d6c7c;background-color: #ffffff;border-color: #dddddd;}\n    .mauticform-button-wrapper .mauticform-button, .mauticform-pagebreak-wrapper .mauticform-pagebreak { display: inline-block;margin-bottom: 0;font-weight: 600;text-align: center;vertical-align: middle;cursor: pointer;background-image: none;border: 1px solid transparent;white-space: nowrap;padding: 6px 12px;font-size: 13px;line-height: 1.3856;border-radius: 3px;-webkit-user-select: none;-moz-user-select: none;-ms-user-select: none;user-select: none;}\n    .mauticform-button-wrapper .mauticform-button.btn-ghost[disabled], .mauticform-pagebreak-wrapper .mauticform-pagebreak.btn-ghost[disabled] { background-color: #ffffff; border-color: #dddddd; opacity: 0.75; cursor: not-allowed; }\n    .mauticform-pagebreak-wrapper .mauticform-button-wrapper {  display: inline; }\n\n    /**\n    * @see https://github.com/TarekRaafat/autoComplete.js/blob/master/dist/css/autoComplete.02.css.\n    */\n    .autoComplete_wrapper {position: relative;}\n    .autoComplete_wrapper > input::placeholder {transition: all 0.3s ease;}\n    .autoComplete_wrapper > ul {position: absolute;max-height: 226px;overflow-y: scroll;top: 100%;left: 0;right: 0;padding: 0;margin: 0.5rem 0 0 0;border-radius: 4px;background-color: #fff;border: 1px solid rgba(33, 33, 33, 0.1);z-index: 1000;outline: none;}\n    .autoComplete_wrapper > ul > li {padding: 10px 20px;list-style: none;text-align: left;font-size: 16px;color: #212121;transition: all 0.1s ease-in-out;border-radius: 3px;background-color: rgba(255, 255, 255, 1);white-space: nowrap;overflow: hidden;text-overflow: ellipsis;transition: all 0.2s ease;}\n    .autoComplete_wrapper > ul > li > span {float: right;}\n    .autoComplete_wrapper > ul > li::selection {color: rgba(#ffffff, 0);background-color: rgba(#ffffff, 0);}\n    .autoComplete_wrapper > ul > li:hover {cursor: pointer;background-color: rgba(123, 123, 123, 0.1);}\n    .autoComplete_wrapper > ul > li mark {background-color: transparent;font-weight: bold;}\n    .autoComplete_wrapper > ul > li mark::selection {background-color: rgba(#ffffff, 0);}\n    .autoComplete_wrapper > ul > li[aria-selected=\"true\"] {background-color: rgba(123, 123, 123, 0.1);}\n    @media only screen and (max-width: 600px) {\n      .autoComplete_wrapper > input {width: 18rem;}\n    }\n</style>\n\n<style type=\"text/css\" scoped>\n    .mauticform-field-hidden { display:none }\n</style>\n<div id=\"mauticform_wrapper_acmeglobalconferenceregistration\" class=\"mauticform_wrapper\">\n    <form autocomplete=\"false\" role=\"form\" method=\"post\" action=\"https://m5-tester.ddev.site/form/submit?formId=2\" id=\"mauticform_acmeglobalconferenceregistration\" data-mautic-form=\"acmeglobalconferenceregistration\" enctype=\"multipart/form-data\" ><div class=\"mauticform-error\" id=\"mauticform_acmeglobalconferenceregistration_error\"></div>\n            <div class=\"mauticform-message\" id=\"mauticform_acmeglobalconferenceregistration_message\"></div><div class=\"mauticform-innerform\">\n            <div class=\"mauticform-page-wrapper mauticform-page-1\" data-mautic-form-page=\"1\" >\n                  \n\n\n      \n\n    \n\n\n    \n\n\n<div id=\"mauticform_acmeglobalconferenceregistration_topic_preference\"class=\"mauticform-row mauticform-text mauticform-field-1\">\n  <label id=\"mauticform_label_acmeglobalconferenceregistration_topic_preference\"for=\"mauticform_input_acmeglobalconferenceregistration_topic_preference\"class=\"mauticform-label\">Topic preference</label>\n  <span class=\"mauticform-helpmessage\">The talk that you're looking forward to</span>\n      <textarea name=\"mauticform[topic_preference]\"id=\"mauticform_input_acmeglobalconferenceregistration_topic_preference\"class=\"mauticform-textarea\"></textarea>\n  \n  <span class=\"mauticform-errormsg\" style=\"display:none;\"></span>\n</div>\n                  \n      \n  \n    \n    \n<div id=\"mauticform_acmeglobalconferenceregistration_submit\"class=\"mauticform-row mauticform-button-wrapper mauticform-field-2\">\n  <button class=\"btn btn-ghost mauticform-button\"name=\"mauticform[submit]\"value=\"1\"id=\"mauticform_input_acmeglobalconferenceregistration_submit\"type=\"submit\">Submit</button>\n</div>\n                  </div></div><input type=\"hidden\" name=\"mauticform[formId]\" id=\"mauticform_acmeglobalconferenceregistration_id\" value=\"2\"/>\n        <input type=\"hidden\" name=\"mauticform[return]\" id=\"mauticform_acmeglobalconferenceregistration_return\" value=\"\"/>\n        <input type=\"hidden\" name=\"mauticform[formName]\" id=\"mauticform_acmeglobalconferenceregistration_name\" value=\"acmeglobalconferenceregistration\"/>\n        \n    </form>\n</div>\n",
              "publishUp": "2026-02-19T07:00:00+00:00",
              "publishDown": "2026-03-06T08:05:00+00:00",
              "fields": [
                  {
                      "id": 2,
                      "label": "Topic preference",
                      "showLabel": true,
                      "alias": "topic_preference",
                      "type": "textarea",
                      "defaultValue": null,
                      "isRequired": false,
                      "validationMessage": null,
                      "helpMessage": "The talk that you're looking forward to",
                      "order": 1,
                      "properties": [],
                      "validation": [],
                      "parent": null,
                      "conditions": [],
                      "labelAttributes": null,
                      "inputAttributes": null,
                      "containerAttributes": null,
                      "leadField": null,
                      "saveResult": true,
                      "isAutoFill": true,
                      "mappedObject": "company",
                      "mappedField": null
                  },
                  {
                      "id": 3,
                      "label": "Submit",
                      "showLabel": true,
                      "alias": "submit",
                      "type": "button",
                      "defaultValue": null,
                      "isRequired": false,
                      "validationMessage": null,
                      "helpMessage": null,
                      "order": 2,
                      "properties": [],
                      "validation": [],
                      "parent": null,
                      "conditions": [],
                      "labelAttributes": null,
                      "inputAttributes": "class=\"btn btn-ghost\"",
                      "containerAttributes": null,
                      "leadField": null,
                      "saveResult": true,
                      "isAutoFill": false,
                      "mappedObject": null,
                      "mappedField": null
                  }
              ],
              "actions": [
                  {
                      "id": 13,
                      "name": "Add company score",
                      "description": null,
                      "type": "lead.scorecontactscompanies",
                      "order": 1,
                      "properties": {
                          "score": 5
                      }
                  }
              ],
              "template": "goldstar",
              "inKioskMode": true,
              "renderStyle": true,
              "formType": "standalone",
              "postAction": "message",
              "postActionProperty": "Thank you for registering and see you there!",
              "noIndex": false,
              "formAttributes": null,
              "language": "en_US"
          },
          // ...
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
     - Total count of Forms
   * - ``forms``
     - array
     - Array of Forms

.. vale off

For the rest of the properties, refer to :ref:`Form properties <get Form properties>`.

.. vale on

.. vale off

Create Form
***********

.. vale on

Creates a new Form.

.. code-block:: php

   <?php

   $data = array(
       'name'               => 'Form created via API',           // Required
       'postActionProperty' => 'Thank you for your submission!', // Required
       'fields'             => array(                            // Required
           array(
               'label'        => 'Email',                        // Required
               'type'         => 'text',
               'alias'        => 'email',
               'mappedObject' => 'contact',
               'mappedField'  => 'email',
               'isRequired'   => true,
           ),
           array(
               'label' =>    'Submit',                           // Required
               'type'  => 'button',
           ),
       ),
       'actions' => array(                                       // Required
           array(
               'properties'  => array(                           // Required
                   'subject' => 'New form submission',
                   'message' => 'A new form submission has been received.',
                   'email'   => 'admin@example.com'
               ),
               'name'        => 'Send notification',
               'type'        => 'email.send.lead',
           ),
       ),
       'formType'           => 'standalone',
       'postAction'         => 'message',
       'description'        => 'This is a test form created via API',
   );

   $form = $formApi->create($data);

.. vale off

HTTP request
============

.. vale on

``POST /forms/new``

.. _create Form POST parameters:

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
       
       Form name
   * - ``postActionProperty``
     - string
     - **Required.**
       
       The data associated with the ``postAction``. Contains the redirect URL when set to ``redirect``, or the success message when set to ``message``
   * - ``fields``
     - array
     - **Required.**
       
       Array of Form Fields. Refer to the :ref:`Field parameters` table for available options
   * - ``actions``
     - array
     - **Required.**
       
       Array of Form actions. Refer to the :ref:`Action parameters` table for available options
   * - ``formType``
     - string
     - Type of the Form - ``standalone`` or ``campaign``
   * - ``postAction``
     - string
     - Action to perform after submission. Must be one of:
     
       * ``return``: no action taken
       * ``redirect``: redirects to a specified URL
       * ``message``: displays a success message
   * - ``isPublished``
     - boolean
     - Form publication status

.. _Field parameters:

Field parameters
~~~~~~~~~~~~~~~~

These parameters reside within the ``fields`` array.

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``label``
     - string
     - **Required.**
       
       Label displayed for the field
   * - ``type``
     - string
     - Type of field, such as ``text``, ``email``, or ``select``
   * - ``mappedObject``
     - string
     - The object type that the field maps to - ``contact`` or ``company``
   * - ``mappedField``
     - string
     - The specific Contact or Company field that the Form Field maps to
   * - ``isRequired``
     - boolean
     - Mandatory status for the field

.. _Action parameters:

Action parameters
~~~~~~~~~~~~~~~~~

These parameters reside within the ``actions`` array.

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``properties``
     - array
     - **Required.**
       
       The settings for the specific action type - for example, the Email ID or subject
   * - ``name``
     - string
     - Action name
   * - ``type``
     - string
     - Type of action, such as ``email.send.lead``

Response
========

* Returns ``201 Created`` when the request successfully creates a Form.

The response is a JSON object similar to :ref:`Get Form <get Form response>`.

Properties
----------

Refer to :ref:`Form properties <get Form properties>`.

.. vale off

Edit Form
*********

.. vale on

Edits a Form. 

This operation supports ``PUT`` or ``PATCH`` depending on the desired behavior:

* ``PUT``: **full replacement**. The request creates a new Form if the ID is missing. If the ID exists, the request clears all existing data and replaces it with the provided values.
* ``PATCH``: **partial update**. The request only updates field values based on the request data. The request fails when the Form ID doesn't exist.

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

   // Create a new Form if ID 1 isn't found
   $createIfNotFound = true;

   $form = $formApi->edit($id, $data, $createIfNotFound);

.. vale off

HTTP request
============

.. vale on

* ``PUT /forms/ID/edit``: updates an existing Form or creates a new one when the ID doesn't exist.
* ``PATCH /forms/ID/edit``: updates an existing Form. The request fails when the ID doesn't exist.

POST parameters
---------------

Accepts the same parameters as those described in :ref:`Create Form <create Form POST parameters>`. All parameters are optional.

Response
========

* ``PUT``: returns ``200 OK`` when the request successfully updates the Form or ``201 Created`` when the request creates a Form.
* ``PATCH``: returns ``200 OK`` when the request successfully updates the Form or ``404 Not Found`` error when the Form ID doesn't exist.

The response is a JSON object similar to :ref:`Get Form <get Form response>`.

Properties
----------

Refer to :ref:`Form properties <get Form properties>`.

.. vale off

Delete Form
***********

.. vale on

Deletes a Form.

.. code-block:: php

   <?php

   $form = $formApi->delete($id);

.. vale off

HTTP request
============

.. vale on

``DELETE /forms/ID/delete``

Response
========

* Returns ``200 OK`` when the request successfully deletes the Form.

The response is a JSON object containing the data of the deleted Form, similar to :ref:`Get Form <get Form response>`.

Properties
----------

Refer to :ref:`Form properties <get Form properties>`.

.. vale off

Delete Form fields
******************

.. vale on

Deletes specific fields from a Form.

.. code-block:: php

   <?php

   $formApi->deleteFields($formId, array(1, 2, 3));

.. vale off

HTTP request
============

.. vale on

``DELETE /forms/ID/fields/delete``

Parameters
----------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``fields``
     - array
     - **Required.**
       
       Array of Form Field IDs to delete

Response
========

* Returns ``200 OK`` when the request successfully deletes the Form Fields.

The response is a JSON object containing the data of the deleted Form Fields, similar to :ref:`Get Form <get Form response>`.

Properties
----------

Refer to :ref:`Form properties <get Form properties>`.

.. vale off

Delete Form actions
*******************

.. vale on

Deletes specific actions from a Form.

.. code-block:: php

   <?php

   $formApi->deleteActions($formId, array(1, 2));

.. vale off

HTTP request
============

.. vale on

``DELETE /forms/ID/actions/delete``

Parameters
----------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``actions``
     - array
     - **Required.**
       
       Array of Form action IDs to delete

Response
========

* Returns ``200 OK`` when the request successfully deletes the Form actions.

The response is a JSON object containing the data of the deleted Form actions, similar to :ref:`Get Form <get Form response>`.

Properties
----------

Refer to :ref:`Form properties <get Form properties>`.

.. vale off

Get Form submission
*******************

.. vale on

Get an individual submission for a specific Form.

.. code-block:: php

   <?php

   $submission = $formApi->getSubmission($formId, $submissionId);

.. vale off

HTTP request
============

.. vale on

``GET /forms/FORM_ID/submissions/SUBMISSION_ID``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Form submission.

.. _get Form submission response:

.. code-block:: json

   {
      "submission": {
          "id": 2,
          "ipAddress": {
              "ipAddress": "127.0.0.1"
          },
          "form": {
              "id": 2,
              "name": "Acme Global Conference Registration",
              "alias": "acme_globa",
              "category": {}
          },
          "lead": {
              "id": 3,
              "points": 0,
              "color": null,
              "title": null,
              "firstname": "Jack",
              "lastname": "Smith",
              "company": "Beta Inc.",
              "position": null,
              "email": null,
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
          "dateSubmitted": "2026-02-19T07:27:18+00:00",
          "referer": "https://example.com/forms/2",
          "page": null,
          "results": {
                "form_id": "2",
                "topic_preference": "The Rising of Open Source",
                "company_name": "Beta Inc.",
                "availability": "2026-02-20",
                "email": null,
                "first_name": "Jack",
                "last_name": "Smith"
          }
      }
   }

.. _get Form submission properties:

Form submission properties
--------------------------

.. vale off

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - integer
     - ID of the Form submission
   * - ``ipAddress``
     - object
     - Information about the IP address used for the submission
   * - ``form``
     - object
     - Information about the Form that received the submission
   * - ``lead``
     - object
     - The Contact record associated with the submission
   * - ``trackingId``
     - string
     - ID used for tracking the submission source
   * - ``dateSubmitted``
     - datetime
     - Date and time of the submission
   * - ``referer``
     - string
     - The URL of the page where the User submitted the Form
   * - ``page``
     - object
     - The specific Mautic Landing Page where the submission occurred
   * - ``results``
     - object
     - The values submitted for each Form Field

.. vale on

.. vale off

List Form submissions
*********************

.. vale on

Retrieves a list of submissions for a specific Form.

.. code-block:: php

   <?php

   $submissions = $formApi->getSubmissions($formId, $searchFilter, $start, $limit, $orderBy, $orderByDir);

.. vale off

HTTP request
============

.. vale on

``GET /forms/ID/submissions``

Query parameters
----------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``searchFilter``
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
     - Column to sort by. Any column in the response is valid
       
       **Note**: convert ``camelCase`` properties to ``snake_case``. For example, ``dateAdded`` becomes ``date_added``, ``webhookUrl`` becomes ``webhook_url``, and so on
   * - ``orderByDir``
     - string
     - Order direction - ``asc`` or ``desc``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Form submissions.

.. code-block:: json

   {
      "total": "4",
      "submissions": [
          {
              "id": 2,
              "ipAddress": {
                  "ipAddress": "127.0.0.1"
              },
              "form": {
                  "id": 2,
                  "name": "Acme Global Conference Registration",
                  "alias": "acme_globa",
                  "category": {}
              },
              "lead": {
                  "id": 3,
                  "points": 0,
                  "color": null,
                  "title": null,
                  "firstname": "Jack",
                  "lastname": "Smith",
                  "company": "Beta Inc.",
                  "position": null,
                  "email": null,
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
              "dateSubmitted": "2026-02-19T07:27:18+00:00",
              "referer": "https://example.com/forms/2",
              "page": null,
              "results": {
                  "first_name": "Jack",
                  "last_name": "Smith",
                  "company_name": "Beta Inc.",
                  "availability": "2026-02-20",
                  "topic_preference": "The Rising of Open Source"
              }
          },
          // ...
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
     - Total count of Form submissions
   * - ``forms``
     - array
     - Array of Form submissions

.. vale off

For the rest of the Form properties, refer to :ref:`get Form submission properties`.

.. vale on

.. vale off

Get Contact Form submissions
****************************

.. vale on

Retrieves a Contact from a specific Form submission.

.. code-block:: php

   <?php

   $submissions = $formApi->getContactSubmissions($formId, $contactId, $searchFilter, $start, $limit, $orderBy, $orderByDir);

.. vale off

HTTP request
============

.. vale on

``GET /forms/FORM_ID/submissions/contact/CONTACT_ID``

Query parameters
----------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``searchFilter``
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
       
       **Note**: convert ``camelCase`` properties to ``snake_case``. For example, ``dateAdded`` becomes ``date_added``, ``webhookUrl`` becomes ``webhook_url``, and so on
   * - ``orderByDir``
     - string
     - Order direction - ``asc`` or ``desc``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Contact from the Form submission.

.. code-block:: json

   {
      "total": "1",
      "submissions": [
          {
              "id": 2,
              "ipAddress": {
                  "ipAddress": "127.0.0.1"
              },
              "form": {
                  "id": 2,
                  "name": "Acme Global Conference Registration",
                  "alias": "acme_globa",
                  "category": {}
              },
              "lead": {
                  "id": 3,
                  "points": 0,
                  "color": null,
                  "title": null,
                  "firstname": "Jack",
                  "lastname": "Smith",
                  "company": "Beta Inc.",
                  "position": null,
                  "email": null,
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
              "dateSubmitted": "2026-02-19T07:27:18+00:00",
              "referer": "https://example.com/forms/2",
              "page": null,
              "results": {
                  "first_name": "Jack",
                  "last_name": "Smith",
                  "company_name": "Beta Inc.",
                  "availability": "2026-02-20",
                  "topic_preference": "The Rising of Open Source"
              }
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
     - Total count of Form submissions
   * - ``submissions``
     - array
     - Array of Form submissions

.. vale off

For the rest of the Form properties, refer to :ref:`get Form submission properties`.

.. vale on

.. _Form Field types:

.. vale off

Form Field types
****************

.. vale on

Mautic supports various Form Field types to collect and validate Contact data. Each field type serves a specific purpose during Form submission:

.. vale off

.. list-table::
   :widths: 20 30 50
   :header-rows: 1

   * - Field type
     - Description
     - Properties
   * - ``captcha``
     - CAPTCHA field
     - ``placeholder``, ``captcha``, ``errorMessage``
   * - ``checkboxgrp``
     - Checkbox group
     - ``syncList``, ``optionlist`` - an object of ``list`` arrays, ``labelAttributes``
   * - ``companyLookup``
     - Company lookup
     - None
   * - ``date``
     - Date picker
     - ``format``, ``placeholder``
   * - ``datetime``
     - Date and time picker
     - ``format``
   * - ``freetext``
     - Description area
     - ``text``
   * - ``email``
     - Email input with validation
     - ``placeholder``
   * - ``file``
     - File upload
     - ``allowed_file_size``, ``allowed_file_extensions``, ``public``, ``profile_image``
   * - ``freehtml``
     - HTML area
     - ``text``
   * - ``hidden``
     - Hidden field
     - None
   * - ``number``
     - Number input
     - ``placeholder``, ``precision``
   * - ``pagebreak``
     - Page break for multi-page Forms
     - ``next_page_label``, ``prev_page_label``
   * - ``password``
     - Password
     - None
   * - ``tel``
     - Telephone input
     - ``placeholder``
   * - ``radiogrp``
     - Radio group
     - ``syncList``, ``optionlist`` - an object of ``list`` arrays, ``labelAttributes``
   * - ``country``
     - Country selection dropdown
     - ``placeholder``, ``multiple``
   * - ``select``
     - Dropdown selection
     - ``placeholder``, ``syncList``, ``list`` - an object of ``list`` arrays, ``multiple``
   * - ``textarea``
     - Multi-line text input
     - ``placeholder``, ``rows``, ``maxlength``
   * - ``text``
     - Single line text input
     - ``placeholder``, ``maxlength``
   * - ``url``
     - URL input with validation
     - ``placeholder``
   * - ``button``
     - Submit button
     - None

.. _Form action types:

.. vale on

Form action types
*****************

Form actions execute specific tasks immediately after a Contact submits a Form. Mautic supports the following action types:

.. vale off

.. list-table::
   :widths: 30 30 40
   :header-rows: 1

   * - Action type
     - Description
     - Properties
   * - ``lead.scorecontactscompanies``
     - Add to Company's score
     - ``score``
   * - ``lead.pointschange``
     - Adjust Contact's Points
     - ``operator``, ``points``, ``group``
   * - ``lead.changelist``
     - Modify Contact's Segments
     - ``addToLists``, ``removeFromLists``
   * - ``lead.changetags``
     - Modify Contact's tags
     - ``add_tags``, ``remove_tags``
   * - ``lead.addutmtags``
     - Record UTM Tags
     - None
   * - ``lead.remove_do_not_contact``
     - Remove Contact from Do Not Contact list
     - None
   * - ``asset.download``
     - Download an Asset
     - ``asset``, ``category``
   * - ``form.repost``
     - Forwards submission results to an external URL or Form
     - ``post_url``, ``authorization_header``, ``failure_email``
   * - ``plugin.leadpush``
     - Push Contact to Integration
     - ``integration``
   * - ``email.send.lead``
     - Send Email to Contact
     - ``email``
   * - ``email.send.user``
     - Send Email to User
     - ``useremail``, ``user_id``
   * - ``form.email``
     - Send Form results
     - ``subject``, ``immediately``, ``set_replyto``, ``message``, ``email_to_owner``, ``copy_lead``, ``templates``, ``to``, ``cc``, ``bcc``

.. vale on

Progressive profiling
*********************

Progressive profiling collects more information from Contacts over time by showing different fields based on previous submissions. To enable progressive profiling:

#. Set ``progressiveProfilingLimit`` on the Form
#. Configure fields with ``showAfterXSubmissions`` property
#. Use ``showWhenValueExists`` to hide fields if a value already exists for that Contact

Conditional fields
******************

Mautic shows fields conditionally based on other field values:

#. Set the ``parent`` field ID
#. Configure ``conditions`` with expression type - ``eq``, ``neq``, ``in``, and ``!in``
#. Set ``isConditionallyHidden`` to true

Mapped fields
*************

Mautic can map Form Fields to Contact or Company fields:

* Use ``mappedObject`` to specify ``contact`` or ``company``
* Use ``mappedField`` to specify the target field name
* Mautic still supports the deprecated ``leadField`` property for backward compatibility
