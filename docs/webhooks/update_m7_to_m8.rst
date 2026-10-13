Update Webhook integrations for Mautic 8
########################################

Read this page if you maintain an app or script that receives Mautic Webhook payloads, and you're upgrading the Mautic instance that sends them from Mautic 7 to Mautic 8. Each section describes a payload change in Mautic 8 and how to update the code that processes it. For the complete list of changes in Mautic 8, including changes that only affect Plugins, see the :xref:`UPGRADE_GUIDE_8`.

.. _mautic 8 webhook form properties:

Form properties in payloads
***************************

Mautic 8 removes the ``formType`` property from Forms, so Webhook payloads don't include it. Mautic deprecated the property in Mautic 7.1, because all Forms work the same way and Mautic doesn't use Form types.

In Mautic 7, the ``mautic.email_on_send`` payload includes ``formType``, with the value ``standalone`` or ``campaign``, in the Email's ``unsubscribeForm`` object. In Mautic 8, the ``unsubscribeForm`` object doesn't include ``formType``. For the properties it includes, see :ref:`Unsubscribe Form properties <webhooks/events/email_on_send:Unsubscribe Form properties>`.

Other payloads with Form data, such as ``mautic.form_on_submit``, don't include ``formType`` in Mautic 7, so their Form properties stay the same.

To update the code that processes the payload:

* Remove code that reads ``formType`` from the ``unsubscribeForm`` object. All Forms work the same way, so no other property replaces it.
