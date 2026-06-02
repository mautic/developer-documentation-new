Company created/updated event
#############################

Triggered when Mautic creates or updates a Company.

.. _company_created_updated_event_type:

Event type
**********

``mautic.company_post_save``

.. _company_created_updated_event_properties:

Event properties
****************

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``company``
      - object
      - :ref:`Company object<webhooks/events/company_post_save:Company properties>`.
    * - ``timestamp``
      - string
      - Date/time the event occurred in ISO 8601 format.

Company properties
******************


.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``id``
      - int
      - ID of the Company
    * - ``isPublished``
      - boolean
      - Always true.
    * - ``dateAdded``
      - string
      - Date/time of Company creation in ISO 8601 format.
    * - ``createdBy``
      - int|null
      - The ID of the User who created the Company or null if unknown.
    * - ``createdByUser``
      - string|null
      - Name of the User that created the Company.
    * - ``dateModified``
      - string|null
      - Date/time the Company was last modified in ISO 8601 format or null if not modified.
    * - ``modifiedBy``
      - int|null
      - The ID of the User who last modified the Company or null if unknown. For example, visitor tracking.
    * - ``modifiedByUser``
      - string|null
      - Name of the User that last modified the Company if applicable. Otherwise null.
    * - ``name``
      - string
      - The Company's name.
    * - ``address1``
      - string|null
      - The Company's address line 1.
    * - ``address2``
      - string|null
      - The Company's address line 2.
    * - ``city``
      - string|null
      - The Company's city.
    * - ``state``
      - string
      - The Company's state.
    * - ``zipcode``
      - string|null
      - The Company's zip code.
    * - ``country``
      - string|null
      - The Company's country.
    * - ``phone``
      - string|null
      - The Company's phone number.
    * - ``website``
      - string|null
      - The Company's website.
    * - ``industry``
      - string|null
      - The Company's industry.
    * - ``score``
      - string|null
      - The Company's behavior score - similar to Contact Points.
    * - ``fields``
      - object|array
      -  Mautic groups fields by Field Groups keyed as one of ``core``, ``social``, ``personal``, and ``professional``. Each ``fieldGroup`` has an object of Fields keyed by the Field's API name. See :ref:`Custom Field object<webhooks/events/lead_post_save_new:Custom Field properties>` for each Field's properties. Note that this could be an object if there are Fields available. Otherwise, Mautic sets an empty array. For example, ``$companyCity = $company['fields']['core']['city']['value'];``.