Getting started with webhooks
==========================================================

Webhooks are a universal way to send data about Contacts and their activity to a third party in either real-time - as the change/activity happens - or queued - to be sent in batches through background cron jobs.

The structure of Webhook payloads are as follows. ``WebhookEventType`` would be the event's actual type and `WebhookEventPayload` will contain the event's data.

.. code-block:: javascript

    {
        "WebhookEventType": [
            { WebhookEventPayload }
        ]
    }

Mautic aggregates event types and payloads when using the :ref:`Background workflow`.

.. code-block:: javascript

    {
        "WebhookEventType1": [
            { WebhookEventPayload1 },
            { WebhookEventPayload2 },
            { WebhookEventPayload3 }
        ],
        "WebhookEventType2": [
            { WebhookEventPayload4 },
            { WebhookEventPayload5 },
            { WebhookEventPayload6 }
        ]
    }

Review :ref:`Webhook events and payloads` for a list of event types and the structure of their payloads.

Webhook workflows
-----------------

The example workflows below describe an example for how Webhooks can be used.

Let’s imagine you have a project management system (PMS) and you want to create a new issue when a Contact submits a Form.

Real-time workflow
^^^^^^^^^^^^^^^^^^^

1. A Contact submits a Mautic Form.
2. Mautic saves the Form Submission.
3. Mautic checks if there is a Webhook with the Form submit event.
4. If there is, Mautic generates a ``Webhook-Signature`` header based on the payload's raw body and secret key then delivers the data to the URL address defined in the Webhook.
5. The PMS receives the data and creates a new issue from it.

Background workflow
^^^^^^^^^^^^^^^^^^^

1. A Contact submits a Mautic Form.
2. Mautic saves the Form Submission.
3. Mautic checks if there is a Webhook with the Form submit event.
4. If there is, Mautic queues the event in the database.
5. When the background cron job runs, Mautic aggregates the events, generates a ``Webhook-Signature`` header based on the payload's raw body and secret key, then delivers the data to the URL address defined in the Webhook.
6. The PMS receives the data and creates new issues from it.

Configuring Webhooks
---------------------

Edit Mautic's Configuration to change some of the behaviors for Webhooks.

1. Click ``Configuration`` from the Admin Menu, displayed by clicking the cog icon in the top right corner.
2. Click the ``Webhook Settings`` tab.
3. Change the settings per the definitions below.
4. Click `Save & Close` or `Apply`

Queue Mode
    Configure how Mautic delivers events. Options are:

        * ``Process Events Immediately`` - delivers the single event in real-time
        * ``Queue Events Only - Process Via CLI Command`` - queues events to the database and delivers in batches using the :xref:`Webhook Cron Job`
Order of the queued events
    Configure the order of events when batched together when queuing. Options are:

        * ``Chronological`` - ordered from oldest to newest
        * ``Reverse Chronological`` - ordered from newest to oldest

Creating a Webhook
-------------------
Each app or script should have its own Webhook configured to minimize the number of places the :ref:`secret key<Securing a Webhook>` is exposed.

1. Click ``Webhooks`` from the Admin Menu, displayed by clicking the cog icon in the top right corner.
2. Click New.
3. Fill in a Name, Webhook POST URL, and select which Events should trigger this Webhook. You can also customize the signature if you want or leave set as the default that is uniquely and randomly generated.
4. Click Apply.
5. :ref:`Test the Webhook<Testing a Webhook>`.

Testing a Webhook
-----------------

If you don't already have somewhere to send the Webhook, you can use a service like :xref:`RequestBin`.

If following the instructions to :ref:`create a Webhook<Creating a Webhook>`, you should be on the form to edit your Webhook. If otherwise, go to Webhooks in the Admin Menu, click the Webhook, then click Edit.

You should see a `Send Test Payload` button when editing a Webhook. Click it and Mautic sends an example request to the POST URL configured.

You can also test the Webhook by testing a live workflow in Mautic.

Securing a Webhook
------------------

Mautic generates a **base64 encoded HMAC-SHA256** signature based on the request's *raw* body and a secret key that's configurable when creating the Webhook. It sets the signature as the value of the ``Webhook-Signature`` header of the request it sends to the third party application. The application should generate its own **base64 encoded HMAC-SHA256** signature based on the received request's *raw* body with the secret key then compare it to the value of the ``Webhook-Signature`` header.

.. Warning:: Only Mautic and the app should know the secret key.

.. Warning:: Requests with signatures that don't match should be ignored as unsafe.