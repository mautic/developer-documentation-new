Webhooks
########

Use this endpoint to obtain details on Mautic's Webhooks.

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
   $initAuth   = new ApiAuth();
   $auth       = $initAuth->newAuth($settings);
   $apiUrl     = "https://example.com";
   $api        = new MauticApi();
   $webhookApi = $api->newApi("hooks", $auth, $apiUrl);

.. vale off

Get Webhook
***********

.. vale on

Retrieves an individual Webhook.

.. code-block:: php

   <?php

   //...
   $webhook = $webhookApi->get($id);

.. vale off

HTTP request
============

.. vale on

``GET /hooks/ID``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Webhook.

.. _get Webhook response:

.. code-block:: json

   {
      "hook": {
          "isPublished": true,
          "dateAdded": "2026-02-24T04:21:16+00:00",
          "dateModified": "2026-02-24T04:22:03+00:00",
          "createdBy": 1,
          "createdByUser": "John Doe",
          "modifiedBy": 1,
          "modifiedByUser": "John Doe",
          "id": 2,
          "name": "Change Contact Points",
          "description": "Change contact points.",
          "webhookUrl": "https://mysite.com/webhook/contact-points-changed",
          "secret": "mySecret",
          "eventsOrderbyDir": null,
          "category": {
              "createdByUser": "John Doe",
              "modifiedByUser": null,
              "id": 2,
              "title": "Important",
              "alias": "important",
              "description": null,
              "color": null,
              "bundle": "Webhook"
          },
          "triggers": [
              "mautic.lead_points_change"
          ]
      }
   }

.. _get Webhook properties:

Webhook properties
------------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``isPublished``
     - boolean
     - Webhook publication status
   * - ``dateAdded``
     - datetime
     - Webhook record creation date and time
   * - ``dateModified``
     - datetime
     - Webhook record last modification date and time
   * - ``createdBy``
     - integer
     - ID of the User who created the Webhook record
   * - ``createdByUser``
     - string
     - Name of the User who created the Webhook record
   * - ``modifiedBy``
     - integer
     - ID of the User who last modified the Webhook record
   * - ``modifiedByUser``
     - string
     - Name of the User who last modified this Webhook record
   * - ``id``
     - integer
     - ID of the Webhook
   * - ``name``
     - string
     - Webhook name
   * - ``description``
     - string
     - Description of the Webhook
   * - ``webhookUrl``
     - string
     - The URL that receives the Webhook payload
   * - ``secret``
     - string
     - Secret used for Webhook authentication or verification
   * - ``eventsOrderbyDir``
     - string
     - Order direction for events - ``asc`` or ``desc``
   * - ``category``
     - object
     - The Category assigned to the Webhook
   * - ``triggers``
     - array
     - Array of event types that trigger the Webhook

.. vale off

List Webhooks
*************

.. vale on

Retrieves a list of Webhooks.

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
   * - ``publishedOnly``
     - boolean
     - Returns only currently published entities
   * - ``minimal``
     - boolean
     - Returns only a simple mapped object of entities without additional lists in it

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Webhooks list.

.. code-block:: json

   {
      "total": 3,
      "hooks": {
          "2": {
              "isPublished": true,
              "dateAdded": "2026-02-24T04:21:16+00:00",
              "dateModified": "2026-02-24T04:22:03+00:00",
              "createdBy": 1,
              "createdByUser": "John Doe",
              "modifiedBy": 1,
              "modifiedByUser": "John Doe",
              "id": 2,
              "name": "Change Contact Points",
              "description": "Change contact points.",
              "webhookUrl": "https://mysite.com/webhook/contact-points-changed",
              "secret": "mySecret",
              "eventsOrderbyDir": null,
              "category": {
                  "createdByUser": "John Doe",
                  "modifiedByUser": null,
                  "id": 2,
                  "title": "Important",
                  "alias": "important",
                  "description": null,
                  "color": null,
                  "bundle": "Webhook"
              },
              "triggers": [
                  "mautic.lead_points_change"
              ]
          },
          // ...
      }
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
     - Total count of Webhooks
   * - ``hooks``
     - array
     - A mapped collection of Webhooks indexed by their ID

.. vale off

For the rest of the properties, refer to :ref:`Webhook properties <get Webhook properties>`.

.. vale on

.. vale off

Create Webhook
**************

.. vale on

Creates a new Webhook.

.. code-block:: php

   <?php

   $data = array(
       'name'        => 'test',                        // Required
       'webhookUrl'  => 'http://mysite.com/webhook/test', // Required
       'triggers'    => array(                         // Required
           'mautic.lead_post_save_new',
           'mautic.lead_post_save_update'
       ),
       'description' => 'Created via API',
       'secret'      => 'mySecret',
       'isPublished' => true,
   );

   $webhook = $webhookApi->create($data);

.. vale off

HTTP request
============

.. vale on

``POST /hooks/new``

.. _create Webhook POST parameters:

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
       
       Name of the Webhook
   * - ``webhookUrl``
     - string
     - **Required.**
       
       The URL that receives the Webhook payload
   * - ``triggers``
     - array
     - **Required.**
       
       Array of event types that trigger the Webhook
   * - ``description``
     - string
     - Description of the Webhook
   * - ``secret``
     - string
     - Secret used for Webhook authentication or verification
   * - ``isPublished``
     - boolean
     - Webhook publication status
   * - ``eventsOrderbyDir``
     - string
     - Order direction for events - ``asc`` or ``desc``
   * - ``category``
     - integer
     - ID of the Category assigned to the Webhook

Response
========

* Returns ``201 Created`` when the request successfully creates a Webhook.

The response is a JSON object similar to :ref:`Get Webhook <get Webhook response>`.

Properties
----------

Refer to :ref:`Webhook properties <get Webhook properties>`.

.. vale off

Edit Webhook
************

.. vale on

Edits a Webhook. 

This operation supports ``PUT`` or ``PATCH`` depending on the desired behavior:

* ``PUT``: **full replacement**. The request creates a new Webhook if the ID is missing. If the ID exists, the request clears all existing data and replaces it with the provided values.
* ``PATCH``: **partial update**. The request only updates field values based on the request data. The request fails when the Webhook ID doesn't exist.

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

   // Create a new Webhook if ID 1 isn't found
   $createIfNotFound = true;

   $webhook = $webhookApi->edit($id, $data, $createIfNotFound);

.. vale off

HTTP request
============

.. vale on

* ``PUT /hooks/ID/edit``: updates an existing Webhook or creates a new one when the ID doesn't exist.
* ``PATCH /hooks/ID/edit``: updates an existing Webhook. The request fails when the ID doesn't exist.

POST parameters
---------------

Accepts the same parameters as those described in :ref:`Create Webhook <create Webhook POST parameters>`. All parameters are optional.

Response
========

* ``PUT``: returns ``200 OK`` when the request successfully updates the Webhook or ``201 Created`` when the request creates a Webhook.
* ``PATCH``: returns ``200 OK`` when the request successfully updates the Webhook or ``404 Not Found`` error when the Webhook ID doesn't exist.

The response is a JSON object similar to :ref:`Get Webhook <get Webhook response>`.

Properties
----------

Refer to :ref:`Webhook properties <get Webhook properties>`.

.. vale off

Delete Webhook
**************

.. vale on

Deletes a Webhook.

.. code-block:: php

   <?php

   $webhook = $webhookApi->delete($id);

.. vale off

HTTP request
============

.. vale on

``DELETE /hooks/ID/delete``

Response
========

* Returns ``200 OK`` when the request successfully deletes the Webhook.

The response is a JSON object containing the data of the deleted Webhook, similar to :ref:`Get Webhook <get Webhook response>`.

Properties
----------

Refer to :ref:`Webhook properties <get Webhook properties>`.

.. vale off

Get Webhook triggers
********************

.. vale on

Retrieves a list of available Webhook triggers.

.. code-block:: php

   <?php

   $triggers = $webhookApi->getTriggers();

.. vale off

HTTP request
============

.. vale on

``GET /hooks/triggers``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the list of Webhook triggers.

.. code-block:: json

   {
      "triggers": {
          "mautic.company_post_save": {
              "label": "Company Create/Update Event",
              "description": "Triggered when a company is created/updated"
          },
          "mautic.company_post_delete": {
              "label": "Company Deleted Event",
              "description": "Triggered when a company is deleted"
          },
          "mautic.lead_channel_subscription_changed": {
              "label": "Contact Channel Subscription Change Event",
              "description": "Triggered when a contact's channel subscription status changes."
          },
          "mautic.lead_company_change": {
              "label": "Contact Company Subscription Change Event",
              "description": "Triggered when a company is added or removed to/from contact"
          },
          "mautic.lead_post_delete": {
              "label": "Contact Deleted Event",
              "description": "Triggered when a contact is deleted."
          },
          "mautic.lead_post_save_new": {
              "label": "Contact Identified Event",
              "description": "Triggered when a contact is identified."
          },
          "mautic.lead_points_change": {
              "label": "Contact Points Changed Event",
              "description": "Triggered when a contact's points are modified."
          },
          "mautic.lead_list_change": {
              "label": "Contact Segment Membership Change Event",
              "description": "Triggered when a contact segment membership is changed"
          },
          "mautic.lead_post_save_update": {
              "label": "Contact Updated Event",
              "description": "Triggered when a contact is updated."
          },
          "mautic.email_on_open": {
              "label": "Email Open Event",
              "description": "mautic.email.webhook.event.open_desc"
          },
          "mautic.email_on_send": {
              "label": "Email Send Event",
              "description": "mautic.email.webhook.event. send_desc"
          },
          "mautic.form_on_submit": {
              "label": "Form Submit Event",
              "description": "mautic.form.webhook.event.form.submit_desc"
          },
          "mautic.page_on_hit": {
              "label": "Page Hit Event",
              "description": "mautic.page.webhook.event.hit_desc"
          },
          "mautic.sms_on_send": {
              "label": "Text Send Event",
              "description": "mautic.sms.webhook.event.send_desc"
          }
      }
   }

Properties
----------

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
     - Description of when the trigger fires
