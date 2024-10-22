Webhook events and payloads
===========================
Webhook events are specific actions that occur in the system, such as when a Contact is added or when a Form is submitted. When an event occurs, a payload containing data about the event is sent to the registered Webhook URL. 

Below is a list of documented events with their event types and the structure of their payloads:

* :ref:`webhooks/events/lead_post_save_new:Contact identified event`
* :ref:`webhooks/events/lead_post_save_update:Contact updated event`
* :ref:`webhooks/events/lead_points_change:Contact Points changed event`
* :ref:`webhooks/events/lead_post_delete:Contact deleted event`
* :ref:`webhooks/events/lead_channel_subscription_changed:Contact Channel subscription change event`
* :ref:`webhooks/events/lead_company_change:Contact Company subscription change event`
* :ref:`webhooks/events/company_post_save:Company created/updated event`
* :ref:`webhooks/events/company_post_delete:Company deleted event`
* :ref:`webhooks/events/email_on_send:Email send event`
* :ref:`webhooks/events/email_on_open:Email open event`
* :ref:`webhooks/events/form_on_submit:Form submit event`
* :ref:`webhooks/events/page_on_hit:Page hit event`
* :ref:`webhooks/events/sms_on_send:Text send event`
