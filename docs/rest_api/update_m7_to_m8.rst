Update REST API integrations for Mautic 8
#########################################

Read this page if you maintain an app or script that calls the Mautic REST API, and you're upgrading the Mautic instance it connects to from Mautic 7 to Mautic 8. Each section describes an API change in Mautic 8 and how to update your app or script for it. For the complete list of changes in Mautic 8, including changes that only affect Plugins, see the :xref:`UPGRADE_GUIDE_8`.

.. _mautic 8 rest api forms:

Forms
*****

Mautic 8 removes the ``formType`` property from Forms. In Mautic 7, a Form response includes ``formType`` with the value ``standalone`` or ``campaign``. Mautic deprecated the property in Mautic 7.1, because all Forms work the same way and Mautic doesn't use Form types.

In Mautic 8, the API handles the property as follows:

* Form responses don't include ``formType``. This applies to the Form endpoints, such as :ref:`Get Form <get Form response>`, and to Form data in API v2 responses.
* Mautic ignores a ``formType`` value in a request that creates or edits a Form.

To update your app or script:

#. Remove code that reads ``formType`` from Form responses. All Forms work the same way, so no other property replaces it.
#. Optional. Remove ``formType`` from the requests that create or edit Forms.
