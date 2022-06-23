Company created/updated event
------------------------------
Triggered when Mautic creates or updates a Company.

.. _Company created/updated event type:

Event type
""""""""""""""""""
``mautic.company_post_save``

.. _Company created/updated event properties:

Event properties
""""""""""""""""""
.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``company``
      - object
      - :ref:`Company object<Company properties>`.
    * - ``timestamp``
      - string
      - Date/time the event occurred in ISO 8601 format.

.. _Company properties:

Company properties
"""""""""""""""""""

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
      - Date/time the Company was created in ISO 8601 format.
    * - ``createdBy``
      - int|null
      - The ID of the User who created the Company or null if unknown.
    * - ``createdByUser``
      - string|null
      - Name of the User that created the Company.
    * - ``dateModified``
      - string|null
      - Date/time the Company was last modified in ISO 8601 format or null if it has not been modified.
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
      - The Company's behavior score (similar to Contact Points).
    * - ``fields``
      - object|array
      -  Fields are grouped by Field Groups keyed as one of ``core``, ``social``, ``personal``, and ``professional``. Each ``fieldGroup`` has an object of Fields keyed by the Field's API name. See :ref:`Custom Field object<Custom Field properties>` for each Field's properties. Note that this could be an object if there are Fields available. Otherwise, an empty array is set. For example, ``$companyCity = $company['fields']['core']['city']['value'];``.