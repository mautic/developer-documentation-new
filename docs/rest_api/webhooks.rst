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
   $initAuth        = new ApiAuth();
   $auth            = $initAuth->newAuth($settings);
   $apiUrl          = "https://mautic.example.com";
   $api             = new MauticApi();
   $webhookApi      = $api->newApi("webhooks", $auth, $apiUrl);

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

**HTTP Request**

.. vale on

``GET /hooks/ID``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
     "hook": {
       "isPublished": false,
       "dateAdded": "2017-06-07T08:54:46+00:00",
       "dateModified": "2017-06-09T07:16:23+00:00",
       "createdBy": 1,
       "createdByUser": "John Doe",
       "modifiedBy": null,
       "modifiedByUser": " ",
       "id": 31,
       "name": "test",
       "description": "Created via API",
       "webhookUrl": "https:\/\/johndoe.com",
       "secret": "webhookSecretKey",
       "eventsOrderbyDir": "DESC",
       "category": {
         "createdByUser": "John Doe",
         "modifiedByUser": "John Doe",
         "id": 1,
         "title": "Important",
         "alias": "important",
         "description": null,
         "color": null,
         "bundle": "Webhook"
       },
       "triggers": [
         "mautic.lead_post_delete",
         "mautic.lead_points_change",
         "mautic.lead_post_save_new",
         "mautic.lead_post_save_update"
       ]
     }
   }

**Webhook Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Webhook
   * - ``name``
     - string
     - Title of the Webhook
   * - ``description``
     - string
     - Description of the Webhook
   * - ``webhookUrl``
     - string
     - URL to send the Webhook payload to
   * - ``secret``
     - string
     - Secret key used for authenticity verification
   * - ``eventsOrderbyDir``
     - string
     - Order direction for queued events in one Webhook. Can be ``desc`` or ``asc``
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
     - ``datetime``
     - Webhook creation date/time
   * - ``createdBy``
     - int
     - ID of the User that created the Webhook
   * - ``createdByUser``
     - string
     - Name of the User that created the Webhook
   * - ``dateModified``
     - datetime/null
     - Date/time Webhook was last modified
   * - ``modifiedBy``
     - int
     - ID of the User that last modified the Webhook
   * - ``modifiedByUser``
     - string
     - Name of the User that last modified the Webhook
   * - ``category``
     - null/object
     - Category
   * - ``triggers``
     - array
     - List of triggers available in Mautic

.. vale off

List Webhooks
*************

.. vale on

.. code-block:: php

   <?php
   // ...

   $webhooks = $webhookApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

**HTTP Request**

.. vale on

``GET /hooks``

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
     - Limit number of entities to return. Defaults to the system configuration for pagination - defaults to 30.
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
     "hooks": {
       "31": {
         "isPublished": false,
         "dateAdded": "2017-06-07T08:54:46+00:00",
         "dateModified": "2017-06-09T07:16:23+00:00",
         "createdBy": 1,
         "createdByUser": "John Doe",
         "modifiedBy": null,
         "modifiedByUser": " ",
         "id": 31,
         "name": "Deleted contact",
         "description": "Notify me when a contact is deleted",
         "webhookUrl": "https:\/\/johndoe.com",
         "secret": "webhookSecretKey",
         "eventsOrderbyDir": "DESC",
         "category": null,
         "triggers": [
           "mautic.lead_post_delete",
         ]
       }
     }
   }

**Properties**

Same as `Get Webhook <#get-webhook>`_.

.. vale off

Create Webhook
**************

.. vale on

.. code-block:: php

   <?php

   $data = array(
       'name' => 'test',
       'description' => 'Created via API',
       'webhookUrl' => 'http://some.url',
       'secret': 'webhookSecretKey',
       'eventsOrderbyDir' => "ASC",
       'triggers' => array(
           'mautic.lead_post_save_update',
           'mautic.lead_post_save_new',
       )
   );

   $webhook = $webhookApi->create($data);

Create a new Webhook.

.. vale off

**HTTP Request**

.. vale on

``POST /hooks/new``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Webhook
   * - ``name``
     - string
     - Title of the Webhook
   * - ``description``
     - string
     - Description of the Webhook
   * - ``webhookUrl``
     - string
     - URL to send the Webhook payload to
   * - ``secret``
     - string
     - Secret key used for authenticity verification - optional
   * - ``eventsOrderbyDir``
     - string
     - Order direction for queued events in one Webhook. Can be ``desc`` or ``asc``
   * - ``isPublished``
     - boolean
     - Published state


**Response**

``Expected Response Code: 201``

**Properties**

Same as `Get Webhook <#get-webhook>`_.

.. vale off

Edit Webhook
************

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'name' => 'Rename Webhook 1 to this',
   );

   // Create new a Webhook of ID 1 isn't found?
   $createIfNotFound = true;

   $webhook = $webhookApi->edit($id, $data, $createIfNotFound);

Edit a new Webhook. Note that this supports PUT or PATCH depending on the desired behavior.

**PUT** creates a Webhook if the given ID doesn't exist and clears all the Webhook information, adds the information from the request.

**PATCH** fails if the Webhook with the given ID doesn't exist and updates the Webhook field values with the values from the request.

.. vale off

**HTTP Request**

.. vale on

To edit a Webhook and return a 404 if the Webhook isn't found:

``PATCH /hooks/ID/edit``

To edit a Webhook and create a new one if the Webhook isn't found:

``PUT /hooks/ID/edit``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Webhook
   * - ``name``
     - string
     - Title of the Webhook
   * - ``description``
     - string
     - Description of the Webhook
   * - ``webhookUrl``
     - string
     - URL to send the Webhook payload to
   * - ``secret``
     - string
     - Secret key used for authenticity verification
   * - ``eventsOrderbyDir``
     - string
     - Order direction for queued events in one Webhook. Can be ``desc`` or ``asc``
   * - ``isPublished``
     - boolean
     - Published state


**Response**

If ``PUT``, the expected response code is ``200`` if editing a Webhook or ``201`` if creating a new one.

If ``PATCH``, the expected response code is ``200``.

**Properties**

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

**HTTP Request**

.. vale on

``DELETE /hooks/ID/delete``

**Response**

``Expected Response Code: 200``

Same as `Get Webhook <#get-webhook>`_.

.. vale off

List available Webhook triggers
*******************************

.. vale on

.. code-block:: php

   <?php

   $webhook = $webhookApi->getTriggers();

List Webhook triggers

.. vale off

**HTTP Request**

.. vale on

``GET /hooks/triggers``

**Response**

``Expected Response Code: 200``

.. code-block:: json

  {
    "triggers": {
      "mautic.lead_post_delete": {
        "label": "Contact Delete Event",
        "description": "mautic.lead.webhook.event.lead.deleted_desc"
      },
      "mautic.lead_points_change": {
        "label": "Contact Point Change (Increase \/ Decrease) Event",
        "description": "mautic.lead.webhook.event.lead.points_desc"
      },
      "mautic.lead_post_save_update": {
        "label": "Contact Updated Event",
        "description": "mautic.lead.webhook.event.lead.update_desc"
      },
      "mautic.email_on_open": {
        "label": "Email Open Event",
        "description": "mautic.email.webhook.event.open_desc"
      },
      "mautic.form_on_submit": {
        "label": "Form Submit Event",
        "description": "mautic.form.webhook.event.form.submit_desc"
      },
      "mautic.lead_post_save_new": {
        "label": "New Contact Event",
        "description": "mautic.lead.webhook.event.lead.new_desc"
      },
      "mautic.page_on_hit": {
        "label": "Page Hit Event",
        "description": "mautic.page.webhook.event.hit_desc"
      }
    }
  }
