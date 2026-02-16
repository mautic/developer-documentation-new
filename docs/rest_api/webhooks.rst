.. vale off

.. note::

  The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

  If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

  Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Webhooks
########

Use this endpoint to obtain details on Mautic's Webhooks.

**Using Mautic's API Library**

You can interact with this API through the :xref:`Mautic API Library` as follows, or use the various http endpoints as described in this document.

.. code-block:: php

   <?php
   use Mautic\MauticApi;
   use Mautic\Auth\ApiAuth;

   // ...
   $initAuth   = new ApiAuth();
   $auth       = $initAuth->newAuth($settings);
   $apiUrl     = "https://example.com";
   $api        = new MauticApi();
   $webhookApi = $api->newApi("hooks", $auth, $apiUrl);

.. vale off

Get Webhook
***********

.. vale on

.. code-block:: php

   <?php

   //...
   $webhook = $webhookApi->get($id);

Get an individual Webhook by ID.

.. vale off

HTTP request
============

.. vale on

``GET /hooks/ID``

Response
========

``Expected Response Code: 200``

.. code-block:: json

   {
       "hook": {
           "id": 31,
           "name": "Lead Created Webhook",
           "description": "Webhook to notify when a new lead is created",
           "webhookUrl": "https://mysite.com/webhook/lead-created",
           "secret": "mySecret",
           "eventsOrderbyDir": null,
           "isPublished": true,
           "publishUp": null,
           "publishDown": null,
           "dateAdded": "2017-06-02T08:54:46+00:00",
           "createdBy": 1,
           "createdByUser": "John Doe",
           "dateModified": "2017-06-02T09:28:56+00:00",
           "modifiedBy": 1,
           "modifiedByUser": "John Doe",
           "category": {
               "id": 1,
               "title": "Important",
               "alias": "important",
               "description": null,
               "color": null,
               "bundle": "webhook"
           },
           "triggers": [
               "mautic.lead_post_save_new",
               "mautic.lead_post_save_update"
           ]
       }
   }

Webhook properties
------------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Webhook
   * - ``name``
     - string
     - Title/name of the Webhook
   * - ``description``
     - string/null
     - Description of the Webhook
   * - ``webhookUrl``
     - string
     - The URL that will receive the webhook payload
   * - ``secret``
     - string/null
     - Secret used for webhook authentication/verification
   * - ``eventsOrderbyDir``
     - string/null
     - Order direction for events - ASC or DESC, null means use global default
   * - ``isPublished``
     - boolean
     - Published state
   * - ``publishUp``
     - datetime/null
     - Webhook publish date/time
   * - ``publishDown``
     - datetime/null
     - Webhook unpublish date/time
   * - ``dateAdded``
     - datetime
     - Webhook creation date/time
   * - ``createdBy``
     - int
     - ID of the User that created the Webhook
   * - ``createdByUser``
     - string
     - Name of the User that created the Webhook
   * - ``dateModified``
     - datetime/null
     - Webhook modified date/time
   * - ``modifiedBy``
     - int
     - ID of the User that last modified the Webhook
   * - ``modifiedByUser``
     - string
     - Name of the User that last modified the Webhook
   * - ``category``
     - object/null
     - Object with the Category details
   * - ``triggers``
     - array
     - Array of event types that trigger this webhook

.. vale off

List Webhooks
*************

.. vale on

.. code-block:: php

   <?php
   // ...

   $webhooks = $webhookApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

HTTP request
============

.. vale on

``GET /hooks``

Query parameters
----------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Name
     - Description
   * - ``search``
     - String or search command to filter entities by
   * - ``start``
     - Starting row for the entities returned, defaults to 0
   * - ``limit``
     - Limit number of entities to return, defaults to the system configuration for pagination - default of 30
   * - ``orderBy``
     - Column to sort by, can use any column listed in the response
   * - ``orderByDir``
     - Sort direction: ``asc`` or ``desc``
   * - ``publishedOnly``
     - Only return currently published entities
   * - ``minimal``
     - Return only array of entities without additional lists in it

Response
========

``Expected Response Code: 200``

.. code-block:: json

   {
       "total": 4,
       "hooks": [
           {
               "id": 31,
               "name": "Lead Created Webhook",
               "description": "Webhook to notify when a new lead is created",
               "webhookUrl": "https://mysite.com/webhook/lead-created",
               "secret": "mySecret",
               "eventsOrderbyDir": null,
               "isPublished": true,
               "publishUp": null,
               "publishDown": null,
               "dateAdded": "2017-06-02T08:54:46+00:00",
               "createdBy": 1,
               "createdByUser": "John Doe",
               "dateModified": "2017-06-02T09:28:56+00:00",
               "modifiedBy": 1,
               "modifiedByUser": "John Doe",
               "category": null,
               "triggers": [
                   "mautic.lead_post_save_new"
               ]
           }
       ]
   }

Properties
----------

Same as `Get Webhook <#get-webhook>`_.

.. vale off

Create Webhook
**************

.. vale on

.. code-block:: php

   <?php 

   $data = array(
       'name'        => 'test',
       'description' => 'Created via API',
       'webhookUrl'  => 'http://mysite.com/webhook/test',
       'secret'      => 'mySecret',
       'triggers'    => array(
           'mautic.lead_post_save_new',
           'mautic.lead_post_save_update'
       )
   );

   $webhook = $webhookApi->create($data);

Create a new Webhook.

.. vale off

HTTP request
============

.. vale on

``POST /hooks/new``

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
     - Webhook name
   * - ``description``
     - string
     - Webhook description
   * - ``webhookUrl``
     - string
     - URL to send webhook payload to
   * - ``secret``
     - string
     - Secret for webhook authentication
   * - ``triggers``
     - array
     - Array of event types that should trigger this webhook
   * - ``isPublished``
     - boolean
     - Whether the webhook is published
   * - ``publishUp``
     - datetime
     - Date/time when the webhook should be published
   * - ``publishDown``
     - datetime
     - Date/time when the webhook should be unpublished
   * - ``eventsOrderbyDir``
     - string
     - Order direction for events - ASC or DESC
   * - ``category``
     - int
     - ID of the category to assign the webhook to

Response
========

``Expected Response Code: 201``

Properties
----------

Same as `Get Webhook <#get-webhook>`_.

.. vale off

Edit Webhook
************

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'name'        => 'test',
       'description' => 'Created via API',
       'webhookUrl'  => 'http://mysite.com/webhook/test',
       'secret'      => 'mySecret',
       'triggers'    => array(
           'mautic.lead_post_save_new',
           'mautic.lead_post_save_update'
       )
   );

   // Create new a Webhook if ID 1 isn't found?
   $createIfNotFound = true;

   $webhook = $webhookApi->edit($id, $data, $createIfNotFound);

Edit an existing Webhook. This supports PUT or PATCH depending on the desired behavior.

**PUT** creates a Webhook if the given ID doesn't exist and clears all the Webhook information, adding the information from the request.
**PATCH** fails if the Webhook with the given ID doesn't exist and updates the Webhook field values with the values from the request.

.. vale off

HTTP request
============

.. vale on

To edit a Webhook and return a 404 if the Webhook isn't found:

``PATCH /hooks/ID/edit``

To edit a Webhook and create a new one if the Webhook isn't found:

``PUT /hooks/ID/edit``

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
     - Webhook name
   * - ``description``
     - string
     - Webhook description
   * - ``webhookUrl``
     - string
     - URL to send webhook payload to
   * - ``secret``
     - string
     - Secret for webhook authentication
   * - ``triggers``
     - array
     - Array of event types that should trigger this webhook
   * - ``isPublished``
     - boolean
     - Whether the webhook is published
   * - ``publishUp``
     - datetime
     - Date/time when the webhook should be published
   * - ``publishDown``
     - datetime
     - Date/time when the webhook should be unpublished
   * - ``eventsOrderbyDir``
     - string
     - Order direction for events - ASC or DESC
   * - ``category``
     - int
     - ID of the category to assign the webhook to

Response
========

If ``PUT``\ , the expected response code if editing the Webhook is ``200`` or ``201`` if created.

If using ``PATCH``\ , the expected response code is ``200``.

Properties
----------

Same as `Get Webhook <#get-webhook>`_.

.. vale off

Delete Webhook
**************

.. vale on

.. code-block:: php

   <?php

   $webhook = $webhookApi->delete($id);

Delete a Webhook.

.. vale off

HTTP request
============

.. vale on

``DELETE /hooks/ID/delete``

Response
========

``Expected Response Code: 200``

Properties
----------

Same as `Get Webhook <#get-webhook>`_.

.. vale off

Get Webhook triggers
********************

.. vale on

.. code-block:: php

   <?php

   $triggers = $webhookApi->getTriggers();

Get a list of available webhook triggers (event types).

.. vale off

HTTP request
============

.. vale on

``GET /hooks/triggers``

Response
========

``Expected Response Code: 200``

.. code-block:: json

   {
       "triggers": {
           "mautic.lead_post_save_new": {
               "label": "Contact created",
               "description": "Triggered when a new contact is created"
           },
           "mautic.lead_post_save_update": {
               "label": "Contact updated", 
               "description": "Triggered when an existing contact is updated"
           },
           "mautic.lead_post_delete": {
               "label": "Contact deleted",
               "description": "Triggered when a contact is deleted"
           },
           "mautic.lead_points_change": {
               "label": "Contact's points changed",
               "description": "Triggered when a contact's point total changes"
           },
           "mautic.lead_channel_subscription_changed": {
               "label": "Contact's channel subscription changed",
               "description": "Triggered when a contact's channel subscription changes"
           },
           "mautic.lead_company_change": {
               "label": "Contact's company changed",
               "description": "Triggered when a contact's company association changes"
           },
           "mautic.company_post_save": {
               "label": "Company created/updated",
               "description": "Triggered when a company is created or updated"
           },
           "mautic.company_post_delete": {
               "label": "Company deleted",
               "description": "Triggered when a company is deleted"
           },
           "mautic.form_on_submit": {
               "label": "Form submitted",
               "description": "Triggered when a form is submitted"
           },
           "mautic.page_on_hit": {
               "label": "Page hit",
               "description": "Triggered when a page is hit/visited"
           },
           "mautic.email_on_send": {
               "label": "Email sent",
               "description": "Triggered when an email is sent"
           },
           "mautic.email_on_open": {
               "label": "Email opened",
               "description": "Triggered when an email is opened"
           }
       }
   }

Response properties
-------------------

The response contains a ``triggers`` object where each key is a trigger event type, and the value contains:

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``label``
     - string
     - Human-readable label for the trigger
   * - ``description``
     - string
     - Description of when this trigger fires
