Webhook events and payloads
===========================
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

