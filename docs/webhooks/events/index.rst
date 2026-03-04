Webhook events and payloads
###########################

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Webhook events are specific actions that occur in the system, such as when a Contact creates a new account. When an event occurs, Mautic sends a payload containing data about the event to the registered Webhook URL. 

Below is a list of documented events with their event types and the structure of their payloads:

.. toctree::
   :caption: Events
   :titlesonly: 
    
   lead_post_save_new
   lead_post_save_update
   lead_points_change
   lead_post_delete
   lead_channel_subscription_changed
   lead_company_change
   company_post_save
   company_post_delete
   email_on_send
   email_on_open
   form_on_submit
   page_on_hit
   sms_on_send

