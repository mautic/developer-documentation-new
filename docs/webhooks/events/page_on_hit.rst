Page hit event
##############

Triggered when a Contact visits a Landing Page or Mautic tracked third party webpage.

Event type
**********

``mautic.page_on_hit``

Event properties
****************

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``hit``
      - object
      - :ref:`Page visit object<Page visit properties>`
    * - ``timestamp``
      - string
      - Date/time the event occurred in ISO 8601 format.

Page visit properties
*********************

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``id``
      - int
      - ID of the Page visit.
    * - ``dateHit``
      - string
      - Date/time the visit occurred in ISO 8601 format.
    * - ``dateHit``
      - null
      - Always ``null`` for Webhook events.
    * - ``page``
      - object
      - :ref:`Landing Page basic object<Landing Page basic properties>`.
    * - ``lead``
      - object
      - :ref:`Contact object<Contact properties>`.
    * - ``ipAddress``
      - object
      - :ref:`IP address basic object<IP address basic properties>` for the Contact when they visited the Page.
    * - ``country``
      - string
      - Country gleaned from tracked IP address.
    * - ``region``
      - string
      - Region gleaned from tracked IP address.
    * - ``city``
      - string
      - City gleaned from tracked IP address.
    * - ``isp``
      - string
      - ISP gleaned from tracked IP address.
    * - ``organization``
      - string
      - Organization gleaned from tracked IP address.
    * - ``code``
      - int
      - Response code from the Page visit.
    * - ``referer``
      - string
      - Referrer for the Page visit.
    * - ``url``
      - string
      - URL for the Page visit.
    * - ``urlTitle``
      - string
      - Page title for the visited the tracked URL.
    * - ``userAgent``
      - string
      - User agent for the browser that visited the tracked URL.
    * - ``remoteHost``
      - string|null
      - Fully qualified domain name of the client sending the request to the server.
    * - ``pageLanguage``
      - string
      - Locale configured for the Landing Page assuming the visit was to a Landing Page.
    * - ``browserLanguages``
      - array
      - Array of languages as configured in the browser.
    * - ``trackingId``
      - string
      - Generated ID for the tracking session.
    * - ``source``
      - string
      - Source that generated the URL if known. For example, ``email`` or ``sms``.
    * - ``sourceId``
      - mixed
      - ID of the specific source that generated the URL if known. For example, ``source`` equaling ``email`` and ``sourceID`` equaling 1 means that Email ID 1 generated the URL that the Contact clicked.
    * - ``query``
      - array
      - Key/value pair of query parameters for the visited URL.
    * - ``redirect``
      - object|null
      -
    * - ``email``
      - object
      - Deprecated. Use ``source`` and ``sourceId`` where ``source`` equals ``email``.

.. vale off

Landing Page basic properties
*****************************

.. vale on

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``id``
      - int
      - ID of the Landing Page.
    * - ``title``
      - string
      - Name of the Landing Page.
    * - ``alias``
      - string
      - API name for the Landing Page.
    * - ``category``
      - object
      - :ref:`Category object<Category properties>`.