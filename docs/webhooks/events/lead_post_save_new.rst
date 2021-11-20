Contact identified event
------------------------
Triggered when Mautic identifies a Contact.

Event type
""""""""""""""""""

``mautic.lead_post_save_new``

.. Contact identified event properties:

Event properties
""""""""""""""""""

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``contact``
      - object
      - :ref:`Contact object<Contact properties>`
    * - ``timestamp``
      - string
      - Date/time the event occurred in ISO 8601 format.

.. _Contact properties:

Contact properties
"""""""""""""""""""

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``id``
      - int
      - ID of the Contact
    * - ``isPublished``
      - boolean
      - Always true.
    * - ``dateAdded``
      - string
      - Date/time the Contact was created in ISO 8601 format.
    * - ``createdBy``
      - int|null
      - The ID of the User who created the Contact or null if unknown. For example, visitor tracking.
    * - ``createdByUser``
      - string|null
      - Name of the User that created the Contact if applicable. Otherwise null.
    * - ``dateIdentified``
      - string|null
      - Date/time the Contact was identified in ISO 8601 format or null if it's a visitor.
    * - ``dateModified``
      - string|null
      - Date/time the Contact was last modified in ISO 8601 format or null if it has not been modified.
    * - ``modifiedBy``
      - int|null
      - The ID of the User who last modified the Contact or null if unknown. For example, visitor tracking.
    * - ``modifiedByUser``
      - string|null
      - Name of the User that last modified the Contact if applicable. Otherwise null.
    * - ``points``
      - int
      - The Contact's Points, also known as a Behavior Score.
    * - ``color``
      - string|null
      - Hex code for the Point Trigger color configured for the range of Points the Contact currently has.
    * - ``preferredProfileImage``
      - string
      - Preferred image to display for the Contact. Defaults to ``gravatar``.
    * - ``fields``
      - object|array
      -  Fields are grouped by Field Groups keyed as one of ``core``, ``social``, ``personal``, and ``professional``. Each ``fieldGroup`` has an object of Fields keyed by the Field's API name. See :ref:`Custom field object<Custom field properties>` for each Field's properties. Note that this could be an object if there are Fields available. Otherwise, an empty array is set. For example, ``$firstname = $contact['fields']['core']['firstname']['value'];``.
    * - ``lastActive``
      - string|null
      - Date/time the Contact was last active in ISO 8601 format or null if it has not been active.
    * - ``owner``
      - object|null
      - :ref:`User object<Owner properties>` or null if no Owner is assigned to the Contact.
    * - ``ipAddresses``
      - object
      - :ref:`IP Address object<IP address properties>`.
    * - ``tags``
      - object
      - :ref:`Tag object<Tag properties>`.
    * - ``doNotContact``
      - array of objects
      - Array of :ref:`Channel subscription objects<Channel subscription properties>`.
    * - ``frequencyRules``
      - array
      - Currently not populated for Webhooks.
    * - ``utmtags``
      - array
      - Currently not populated for Webhooks.
    * - ``stage``
      - object
      - Currently not fully populated for Webhooks.

.. _Custom field properties:

Custom field properties
""""""""""""""""""""""""""

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``id``
      - int
      - ID of the Field.
    * - ``group``
      - string
      - The group the Field belongs to. Current options are ``core``, ``social``, ``personal`` and ``professional``.
    * - ``label``
      - string
      - Label for the Field.
    * - ``alias``
      - string
      - API name for the Field.
    * - ``type``
      - string
      - Field type. Current options are ``boolean``, ``date``, ``datetime``, ``email``, ``country``, ``locale``, ``number``, ``tel``, ``region``, ``select``, ``multiselect``, ``text``, ``textarea``, ``time``, ``timezone``, and ``url``.
    * - ``properties``
      - object
      - Properties for the given Field type. This will vary based on the Field's configuration.
    * - ``value``
      - mixed
      - Field's value for the Contact.
    * - ``normalizedValue``
      - mixed
      - Field's normalized value for the Contact.

.. Owner properties:

Owner properties
""""""""""""""""""""""""""

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``id``
      - int
      - User's ID.
    * - ``username``
      - string
      - User's username.
    * - ``firstname``
      - string
      - User's first name or given name.
    * - ``lastname``
      - string
      - User's last name or surname.

.. IP Address properties:

IP Address properties
""""""""""""""""""""""""""

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``id``
      - int
      - IP Address' ID.
    * - ``ipAddress``
      - string
      - IP Address.
    * - ``ipDetails``
      - object
      - Details of the IP Address such as city, region, latitude, longitude, etc.
    * - ``ipDetails.city``
      - string
      - City where the IP is located.
    * - ``ipDetails.region``
      - string
      - Region where the IP is located.
    * - ``ipDetails.zipcode``
      - string
      - Zip code where the IP is located.
    * - ``ipDetails.latitude``
      - string
      - Latitude for where the IP is located.
    * - ``ipDetails.longitude``
      - string
      - Longitude for where the IP is located.
    * - ``ipDetails.isp``
      - string
      - ISP that owns the IP.
    * - ``ipDetails.organization``
      - string
      - Organization the IP is assigned to.
    * - ``ipDetails.timezone``
      - string
      - Timezone the IP location belongs to.
    * - ``ipDetails.extra``
      - mixed
      - Stores extra data given by the configured IP lookup service.

.. _Tag properties:

Tag properties
""""""""""""""""""""""""""

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``id``
      - int
      - ID of the Tag.
    * - ``tag``
      - string
      - Tag name.

.. _Channel subscription properties:

Channel subscription properties
""""""""""""""""""""""""""

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``id``
      - int
      - ID of the channel subscription entry.
    * - ``reason``
      - int
      - Reason code for the unsubscription. ``1`` is unsubscribed by the Contact, ``2`` is bounced, and ``3`` is manually marked as unsubscribed by the Marketer.
    * - ``channel``
      - string
      - Channel the Contact unsubscribed from. Examples are ``email`` and ``sms``.
    * - ``channelId``
      - int|null
      - ID of the specific channel entity the Contact clicked to unsubscribe from.
