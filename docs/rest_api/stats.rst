Stats
#####

Use this endpoint to obtain statistical data from Mautic's database tables.

Using the Mautic API library
****************************

.. vale off

You can interact with this API using the :xref:`Mautic API Library` as below, or the various HTTP endpoints described in this document.

.. vale on

.. code-block:: php

   <?php
   use Mautic\MauticApi;
   use Mautic\Auth\ApiAuth;

   // ...
   $initAuth = new ApiAuth();
   $auth     = $initAuth->newAuth($settings);
   $apiUrl   = "https://example.com";
   $api      = new MauticApi();
   $statsApi = $api->newApi("stats", $auth, $apiUrl);

Get available stat tables
*************************

Retrieves a list of all available stat tables and their columns.

.. code-block:: php

   <?php

   //...
   $tables = $statsApi->get();

.. vale off

HTTP request
============

.. vale on

``GET /stats``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the stat tables.

.. code-block:: json

   {
      "availableTables": [
          "asset_downloads",
          "audit_log",
          "campaign_lead_event_log",
          "campaign_leads",
          "channel_url_trackables",
          "companies_leads",
          "dynamic_content_lead_data",
          "dynamic_content_stats",
          "email_stat_replies",
          "email_stats",
          "email_stats_devices",
          "form_submissions",
          "ip_addresses",
          "lead_categories",
          "lead_companies_change_log",
          "lead_devices",
          "lead_donotcontact",
          "lead_event_log",
          "lead_frequencyrules",
          "lead_lists_leads",
          "lead_points_change_log",
          "lead_stages_change_log",
          "lead_utmtags",
          "page_hits",
          "page_redirects",
          "point_lead_action_log",
          "point_lead_event_log",
          "push_notification_stats",
          "sms_message_stats",
          "stage_lead_action_log",
          "video_hits",
          "webhook_logs"
      ],
      "tableColumns": {
          "asset_downloads": [
              "asset_id",
              "code",
              "date_download",
              "email_id",
              "id",
              "ip_id",
              "lead_id",
              "referer",
              "source",
              "source_id",
              "tracking_id"
          ],
          "audit_log": [
              "action",
              "bundle",
              "date_added",
              "details",
              "id",
              "ip_address",
              "object",
              "object_id",
              "user_id",
              "user_name"
          ],
          "campaign_lead_event_log": [
              "campaign_id",
              "channel",
              "channel_id",
              "date_triggered",
              "event_id",
              "id",
              "ip_id",
              "is_scheduled",
              "lead_id",
              "metadata",
              "non_action_path_taken",
              "rotation",
              "system_triggered",
              "trigger_date"
          ],
          "campaign_leads": [
              "campaign_id",
              "date_added",
              "date_last_exited",
              "lead_id",
              "manually_added",
              "manually_removed",
              "rotation"
          ],
          "channel_url_trackables": [
              "channel",
              "channel_id",
              "hits",
              "redirect_id",
              "unique_hits"
          ],
          "companies_leads": [
              "company_id",
              "date_added",
              "is_primary",
              "lead_id",
              "manually_added",
              "manually_removed"
          ],
          "dynamic_content_lead_data": [
              "date_added",
              "dynamic_content_id",
              "id",
              "lead_id",
              "slot"
          ],
          "dynamic_content_stats": [
              "date_sent",
              "dynamic_content_id",
              "id",
              "last_sent",
              "lead_id",
              "sent_count",
              "sent_details",
              "source",
              "source_id",
              "tokens"
          ],
          "email_stat_replies": [
              "date_replied",
              "id",
              "message_id",
              "stat_id"
          ],
          "email_stats": [
              "copy_id",
              "date_read",
              "date_sent",
              "email_address",
              "email_id",
              "id",
              "ip_id",
              "is_failed",
              "is_read",
              "last_opened",
              "lead_id",
              "list_id",
              "open_count",
              "open_details",
              "retry_count",
              "source",
              "source_id",
              "tokens",
              "tracking_hash",
              "viewed_in_browser"
          ],
          "email_stats_devices": [
              "date_opened",
              "device_id",
              "id",
              "ip_id",
              "stat_id"
          ],
          "form_submissions": [
              "date_submitted",
              "form_id",
              "id",
              "ip_id",
              "lead_id",
              "page_id",
              "referer",
              "tracking_id"
          ],
          "ip_addresses": [
              "id",
              "ip_address",
              "ip_details"
          ],
          "lead_categories": [
              "category_id",
              "date_added",
              "id",
              "lead_id",
              "manually_added",
              "manually_removed"
          ],
          "lead_companies_change_log": [
              "action_name",
              "company_id",
              "date_added",
              "event_name",
              "id",
              "lead_id",
              "type"
          ],
          "lead_devices": [
              "client_info",
              "date_added",
              "device",
              "device_brand",
              "device_fingerprint",
              "device_model",
              "device_os_name",
              "device_os_platform",
              "device_os_shortname",
              "device_os_version",
              "id",
              "lead_id",
              "tracking_id"
          ],
          "lead_donotcontact": [
              "channel",
              "channel_id",
              "comments",
              "date_added",
              "id",
              "lead_id",
              "reason"
          ],
          "lead_event_log": [
              "action",
              "bundle",
              "date_added",
              "id",
              "lead_id",
              "object",
              "object_id",
              "properties",
              "user_id",
              "user_name"
          ],
          "lead_frequencyrules": [
              "channel",
              "date_added",
              "frequency_number",
              "frequency_time",
              "id",
              "lead_id",
              "pause_from_date",
              "pause_to_date",
              "preferred_channel"
          ],
          "lead_lists_leads": [
              "date_added",
              "leadlist_id",
              "lead_id",
              "manually_added",
              "manually_removed"
          ],
          "lead_points_change_log": [
              "action_name",
              "date_added",
              "delta",
              "event_name",
              "id",
              "ip_id",
              "lead_id",
              "type"
          ],
          "lead_stages_change_log": [
              "action_name",
              "date_added",
              "event_name",
              "id",
              "lead_id",
              "stage_id"
          ],
          "lead_utmtags": [
              "date_added",
              "id",
              "lead_id",
              "query",
              "referer",
              "remote_host",
              "url",
              "user_agent",
              "utm_campaign",
              "utm_content",
              "utm_medium",
              "utm_source",
              "utm_term"
          ],
          "page_hits": [
              "browser_languages",
              "city",
              "code",
              "country",
              "date_hit",
              "date_left",
              "device_id",
              "email_id",
              "id",
              "ip_id",
              "isp",
              "lead_id",
              "organization",
              "page_id",
              "page_language",
              "query",
              "redirect_id",
              "referer",
              "region",
              "remote_host",
              "source",
              "source_id",
              "tracking_id",
              "url",
              "url_title",
              "user_agent"
          ],
          "page_redirects": [
              "checked_out",
              "checked_out_by",
              "checked_out_by_user",
              "created_by",
              "created_by_user",
              "date_added",
              "date_modified",
              "hits",
              "id",
              "is_published",
              "modified_by",
              "modified_by_user",
              "redirect_id",
              "unique_hits",
              "url"
          ],
          "point_lead_action_log": [
              "date_fired",
              "ip_id",
              "lead_id",
              "point_id"
          ],
          "point_lead_event_log": [
              "date_fired",
              "event_id",
              "ip_id",
              "lead_id"
          ],
          "push_notification_stats": [
              "click_count",
              "click_details",
              "date_clicked",
              "date_read",
              "date_sent",
              "id",
              "ip_id",
              "is_clicked",
              "last_clicked",
              "lead_id",
              "list_id",
              "notification_id",
              "retry_count",
              "source",
              "source_id",
              "tokens",
              "tracking_hash"
          ],
          "sms_message_stats": [
              "date_sent",
              "id",
              "ip_id",
              "lead_id",
              "list_id",
              "sms_id",
              "source",
              "source_id",
              "tokens",
              "tracking_hash"
          ],
          "stage_lead_action_log": [
              "date_fired",
              "ip_id",
              "lead_id",
              "stage_id"
          ],
          "video_hits": [
              "browser_languages",
              "channel",
              "channel_id",
              "city",
              "code",
              "country",
              "date_hit",
              "date_left",
              "duration",
              "guid",
              "id",
              "ip_id",
              "isp",
              "lead_id",
              "organization",
              "page_language",
              "query",
              "referer",
              "region",
              "remote_host",
              "time_watched",
              "url",
              "user_agent"
          ],
          "webhook_logs": [
              "date_added",
              "id",
              "note",
              "runtime",
              "status_code",
              "webhook_id"
          ]
      }
   }

Stats properties
----------------

.. list-table::
   :header-rows: 1
   :widths: 25 10 65

   * - Name
     - Type
     - Description
   * - ``availableTables``
     - array
     - List of available tables available for query through this endpoint
   * - ``tableColumns``
     - object
     - Object containing each table name as a key with an array of column names as the value

Get stats from a table
**********************

Retrieves rows from the specified statistical table.

.. code-block:: php

   <?php

   $table = 'asset_downloads';
   $start = 0;
   $limit = 50;
   $order = [
       [
           'col' => 'id',
           'dir' => 'asc'
       ]
   ];
   $where = [
       [
           'col' => 'id',
           'expr' => 'gt',
           'val' => 3,
       ]
   ];

   $stats = $statsApi->get($table, $start, $limit, $order, $where);

.. vale off

HTTP request
============

.. vale on

``GET /stats/TABLE``

Query parameters
----------------

.. list-table::
   :header-rows: 1
   :widths: 15 10 75

   * - Name
     - Type
     - Description
   * - ``start``
     - int
     - Row offset to start from. Defaults to 0.
   * - ``limit``
     - int
     - Number of rows to return. Defaults to 30.
   * - ``order``
     - array
     - Array of sorting definitions. Each definition has ``col`` for column name and ``dir`` for direction - ``asc`` or ``desc``.
   * - ``where``
     - array
     - Array of filter conditions. Each condition has ``col`` for column name, ``expr`` for expression type, and ``val`` for the value.

Where expressions
~~~~~~~~~~~~~~~~~

The ``expr`` parameter supports most methods from Doctrine's ExpressionBuilder:

- ``eq`` - equals
- ``neq`` - not equals
- ``lt`` - less than
- ``lte`` - less than or equal
- ``gt`` - greater than
- ``gte`` - greater than or equal
- ``isNull`` - is null
- ``isNotNull`` - isn't null
- ``like`` - like pattern matching
- ``notLike`` - not like pattern matching
- ``in`` - in array of values
- ``notIn`` - not in array of values
- ``between`` - between two values

Response
========

* Returns ``200 OK`` when the request successfully retrieves the stats from the table.

.. code-block:: json

   {
      "total": 1,
      "stats": [
          {
              "id": "1",
              "asset_id": "1",
              "ip_id": "1",
              "lead_id": "31",
              "date_download": "2023-06-30 08:51:22",
              "code": "200",
              "tracking_id": "b3259e7709f35b7428b7bffcbb3d1d713ac1526c"
          }
      ]
   }

Stats from a table properties
-----------------------------

.. list-table::
   :header-rows: 1
   :widths: 15 10 75

   * - Name
     - Type
     - Description
   * - ``total``
     - int
     - Total number of matching rows
   * - ``stats``
     - array
     - Array of row objects. Columns vary by table.

cURL example
============

When using cURL, encode the array parameters as query string. For example, to filter by ``id = 3``:

.. code-block:: bash

   curl "https://example.com/api/stats/asset_downloads?where%5B0%5D%5Bcol%5D=id&where%5B0%5D%5Bexpr%5D=eq&where%5B0%5D%5Bval%5D=3"

This query string is equivalent to:

.. code-block:: php

   <?php

   $where = [
       [
           'col'  => 'id',
           'expr' => 'eq',
           'val'  => 3,
       ]
   ];

Available tables
================

The following tables are available through the Stats API. Tables require appropriate User permissions to access.

Contact statistics
------------------

.. vale off

.. list-table::
   :header-rows: 1

   * - Table
     - Description
   * - ``companies_leads``
     - Association between Contacts and Companies
   * - ``lead_categories``
     - Category assignments for Contacts
   * - ``lead_companies_change_log``
     - History of Contact and Company associations
   * - ``lead_devices``
     - Device information tracked for Contacts
   * - ``lead_donotcontact``
     - Do-not-contact preferences by Contact and Channel
   * - ``lead_event_log``
     - Activity log for Contact events
   * - ``lead_frequencyrules``
     - Contact frequency and Channel preferences
   * - ``lead_lists_leads``
     - Contact membership in Segments
   * - ``lead_points_change_log``
     - History of Contact Points changes
   * - ``lead_stages_change_log``
     - History of Contact Stage transitions
   * - ``lead_utmtags``
     - UTM parameters tracked for Contacts

.. vale on

``companies_leads``
~~~~~~~~~~~~~~~~~~~

Association between Contacts and Companies.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``company_id``
     - int
     - ID of the Company
   * - ``date_added``
     - datetime
     - Date and time when Mautic created the association
   * - ``is_primary``
     - boolean
     - Primary status - ``1`` or ``true`` indicates the primary Company for the Contact
   * - ``lead_id``
     - int
     - ID of the Contact
   * - ``manually_added``
     - boolean
     - Whether a User added the association manually
   * - ``manually_removed``
     - boolean
     - Whether a User removed the association manually

``lead_categories``
~~~~~~~~~~~~~~~~~~~

Category assignments for Contacts.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``category_id``
     - int
     - ID of the Category
   * - ``date_added``
     - datetime
     - Date and time when Mautic assigned the Category
   * - ``id``
     - int
     - Primary key
   * - ``lead_id``
     - int
     - ID of the Contact
   * - ``manually_added``
     - boolean
     - Whether a User added the Category manually
   * - ``manually_removed``
     - boolean
     - Whether a User removed the Category manually

``lead_companies_change_log``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

History of Contact and Company associations.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``action_name``
     - string
     - Name of the action performed
   * - ``company_id``
     - int
     - ID of the Company
   * - ``date_added``
     - datetime
     - Date and time of the change
   * - ``event_name``
     - string
     - Name of the event that triggered the change
   * - ``id``
     - int
     - Primary key
   * - ``lead_id``
     - int
     - ID of the Contact
   * - ``type``
     - string
     - Type of change

``lead_devices``
~~~~~~~~~~~~~~~~

Device information tracked for Contacts.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``client_info``
     - string
     - Client application information
   * - ``date_added``
     - datetime
     - Date and time when Mautic first tracked the device
   * - ``device``
     - string
     - Device type
   * - ``device_brand``
     - string
     - Device manufacturer or brand
   * - ``device_fingerprint``
     - string
     - Unique device fingerprint
   * - ``device_model``
     - string
     - Device model name
   * - ``device_os_name``
     - string
     - Operating system name
   * - ``device_os_platform``
     - string
     - Operating system platform
   * - ``device_os_shortname``
     - string
     - Abbreviated operating system name
   * - ``device_os_version``
     - string
     - Operating system version
   * - ``id``
     - int
     - Primary key
   * - ``lead_id``
     - int
     - ID of the Contact
   * - ``tracking_id``
     - string
     - Tracking identifier for the device

``lead_donotcontact``
~~~~~~~~~~~~~~~~~~~~~

Do-not-contact preferences by Contact and Channel.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``channel``
     - string
     - Communication Channel such as ``email`` or ``sms``
   * - ``channel_id``
     - int
     - ID of the specific Channel item
   * - ``comments``
     - string
     - Additional comments about the do-not-contact entry
   * - ``date_added``
     - datetime
     - Date and time when Mautic added the preference
   * - ``id``
     - int
     - Primary key
   * - ``lead_id``
     - int
     - ID of the Contact
   * - ``reason``
     - int
     - Reason code for the do-not-contact status

``lead_event_log``
~~~~~~~~~~~~~~~~~~

Activity log for Contact events.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``action``
     - string
     - Action that the system performed
   * - ``bundle``
     - string
     - Mautic bundle that triggered the event
   * - ``date_added``
     - datetime
     - Date and time of the event
   * - ``id``
     - int
     - Primary key
   * - ``lead_id``
     - int
     - ID of the Contact
   * - ``object``
     - string
     - Object type involved in the event
   * - ``object_id``
     - int
     - ID of the object
   * - ``properties``
     - string
     - Additional event properties in JSON format
   * - ``user_id``
     - int
     - ID of the User who triggered the event
   * - ``user_name``
     - string
     - Name of the User who triggered the event

``lead_frequencyrules``
~~~~~~~~~~~~~~~~~~~~~~~

Contact frequency and Channel preferences.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``channel``
     - string
     - Communication Channel
   * - ``date_added``
     - datetime
     - Date and time when Mautic created the rule
   * - ``frequency_number``
     - int
     - Maximum number of messages allowed
   * - ``frequency_time``
     - string
     - Time period for the frequency limit
   * - ``id``
     - int
     - Primary key
   * - ``lead_id``
     - int
     - ID of the Contact
   * - ``pause_from_date``
     - datetime
     - Start date for communication pause
   * - ``pause_to_date``
     - datetime
     - End date for communication pause
   * - ``preferred_channel``
     - boolean
     - Preferred Channel for the Contact

``lead_lists_leads``
~~~~~~~~~~~~~~~~~~~~

Contact membership in Segments.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``date_added``
     - datetime
     - Date and time when Mautic added the Contact to the Segment
   * - ``leadlist_id``
     - int
     - ID of the Segment
   * - ``lead_id``
     - int
     - ID of the Contact
   * - ``manually_added``
     - boolean
     - Whether a User added the Contact manually
   * - ``manually_removed``
     - boolean
     - Whether a User removed the Contact manually

``lead_points_change_log``
~~~~~~~~~~~~~~~~~~~~~~~~~~

History of Contact Points changes.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``action_name``
     - string
     - Name of the action that changed the Points
   * - ``date_added``
     - datetime
     - Date and time of the Points change
   * - ``delta``
     - int
     - Number of Points added or removed
   * - ``event_name``
     - string
     - Name of the event that triggered the change
   * - ``id``
     - int
     - Primary key
   * - ``ip_id``
     - int
     - ID of the IP address associated with the change
   * - ``lead_id``
     - int
     - ID of the Contact
   * - ``type``
     - string
     - Type of Points change

``lead_stages_change_log``
~~~~~~~~~~~~~~~~~~~~~~~~~~

History of Contact Stage transitions.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``action_name``
     - string
     - Name of the action that changed the Stage
   * - ``date_added``
     - datetime
     - Date and time of the Stage change
   * - ``event_name``
     - string
     - Name of the event that triggered the change
   * - ``id``
     - int
     - Primary key
   * - ``lead_id``
     - int
     - ID of the Contact
   * - ``stage_id``
     - int
     - ID of the Stage

``lead_utmtags``
~~~~~~~~~~~~~~~~

UTM parameters tracked for Contacts.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``date_added``
     - datetime
     - Date and time when Mautic tracked the UTM data
   * - ``id``
     - int
     - Primary key
   * - ``lead_id``
     - int
     - ID of the Contact
   * - ``query``
     - string
     - Full query string from the URL
   * - ``referer``
     - string
     - Referring URL
   * - ``remote_host``
     - string
     - Remote host name
   * - ``url``
     - string
     - Full URL visited
   * - ``user_agent``
     - string
     - Browser user agent string
   * - ``utm_campaign``
     - string
     - UTM Campaign parameter value
   * - ``utm_content``
     - string
     - UTM Content parameter value
   * - ``utm_medium``
     - string
     - UTM Medium parameter value
   * - ``utm_source``
     - string
     - UTM Source parameter value
   * - ``utm_term``
     - string
     - UTM Term parameter value

Asset statistics
----------------

.. list-table::
   :header-rows: 1

   * - Table
     - Description
   * - ``asset_downloads``
     - Asset download events

``asset_downloads``
~~~~~~~~~~~~~~~~~~~

Asset download events.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``asset_id``
     - int
     - ID of the downloaded Asset
   * - ``code``
     - string
     - HTTP response code
   * - ``date_download``
     - datetime
     - Date and time of the download
   * - ``email_id``
     - int
     - ID of the Email containing the Asset link
   * - ``id``
     - int
     - Primary key
   * - ``ip_id``
     - int
     - ID of the IP address
   * - ``lead_id``
     - int
     - ID of the Contact who downloaded the Asset
   * - ``referer``
     - string
     - Referring URL
   * - ``source``
     - string
     - Source of the download
   * - ``source_id``
     - int
     - ID of the source item
   * - ``tracking_id``
     - string
     - Tracking identifier

Campaign statistics
-------------------

.. list-table::
   :header-rows: 1

   * - Table
     - Description
   * - ``campaign_leads``
     - Contacts in Campaigns
   * - ``campaign_lead_event_log``
     - Execution log for Campaign Events

``campaign_leads``
~~~~~~~~~~~~~~~~~~

Contacts in Campaigns.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``campaign_id``
     - int
     - ID of the Campaign
   * - ``date_added``
     - datetime
     - Date and time when Mautic added the Contact to the Campaign
   * - ``date_last_exited``
     - datetime
     - Date and time when the Contact last exited the Campaign
   * - ``lead_id``
     - int
     - ID of the Contact
   * - ``manually_added``
     - boolean
     - Whether a User added the Contact manually
   * - ``manually_removed``
     - boolean
     - Whether a User removed the Contact manually
   * - ``rotation``
     - int
     - Number of times the Contact has been through the Campaign

``campaign_lead_event_log``
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Execution log for Campaign Events.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``campaign_id``
     - int
     - ID of the Campaign
   * - ``channel``
     - string
     - Communication Channel used
   * - ``channel_id``
     - int
     - ID of the Channel item
   * - ``date_triggered``
     - datetime
     - Date and time when Mautic triggered the event
   * - ``event_id``
     - int
     - ID of the Campaign Event
   * - ``id``
     - int
     - Primary key
   * - ``ip_id``
     - int
     - ID of the IP address
   * - ``is_scheduled``
     - boolean
     - Scheduling status - ``1`` or ``true`` indicates Mautic scheduled the Event execution
   * - ``lead_id``
     - int
     - ID of the Contact
   * - ``metadata``
     - string
     - Additional event metadata in JSON format
   * - ``non_action_path_taken``
     - boolean
     - Path status - ``1`` or ``true`` indicates the Contact took the non-action path
   * - ``rotation``
     - int
     - Number of times the Contact went through the Campaign
   * - ``system_triggered``
     - boolean
     - Whether the system automatically triggered the event
   * - ``trigger_date``
     - datetime
     - Scheduled trigger date and time

Email statistics
----------------

.. list-table::
   :header-rows: 1

   * - Table
     - Description
   * - ``email_stats``
     - Email send, open, and click statistics
   * - ``email_stats_devices``
     - Device information for Email opens
   * - ``email_stat_replies``
     - Email reply tracking

``email_stats``
~~~~~~~~~~~~~~~

Email send, open, and click statistics.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``copy_id``
     - int
     - ID of the Email copy
   * - ``date_read``
     - datetime
     - Date and time when the Contact first read the Email
   * - ``date_sent``
     - datetime
     - Date and time when Mautic sent the Email
   * - ``email_address``
     - string
     - Recipient Email address
   * - ``email_id``
     - int
     - ID of the Email
   * - ``id``
     - int
     - Primary key
   * - ``ip_id``
     - int
     - ID of the IP address that opened the Email
   * - ``is_failed``
     - boolean
     - Delivery status - ``1`` or ``true`` indicates the Email delivery failed
   * - ``is_read``
     - boolean
     - Read status - ``1`` or ``true`` indicates the Contact read the Email
   * - ``last_opened``
     - datetime
     - Date and time when the Contact last opened the Email
   * - ``lead_id``
     - int
     - ID of the Contact
   * - ``list_id``
     - int
     - ID of the Segment that received the Email
   * - ``open_count``
     - int
     - Number of times the Contact opened the Email
   * - ``open_details``
     - string
     - Details about Email opens in JSON format
   * - ``retry_count``
     - int
     - Number of delivery retry attempts
   * - ``source``
     - string
     - Source of the Email send
   * - ``source_id``
     - int
     - ID of the source item
   * - ``tokens``
     - string
     - Token values used in the Email in JSON format
   * - ``tracking_hash``
     - string
     - Unique hash for tracking this Email send
   * - ``viewed_in_browser``
     - boolean
     - Browser view status - ``1`` or ``true`` indicates the Contact viewed the Email in a browser

``email_stats_devices``
~~~~~~~~~~~~~~~~~~~~~~~

Device information for Email opens.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``date_opened``
     - datetime
     - Date and time when the Contact opened the Email on the device
   * - ``device_id``
     - int
     - ID of the device
   * - ``id``
     - int
     - Primary key
   * - ``ip_id``
     - int
     - ID of the IP address
   * - ``stat_id``
     - int
     - ID of the Email stat record

``email_stat_replies``
~~~~~~~~~~~~~~~~~~~~~~

Email reply tracking.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``date_replied``
     - datetime
     - Date and time when Mautic received the reply
   * - ``id``
     - int
     - Primary key
   * - ``message_id``
     - string
     - Email message ID from the reply
   * - ``stat_id``
     - int
     - ID of the Email stat record

Form statistics
---------------

.. list-table::
   :header-rows: 1

   * - Table
     - Description
   * - ``form_submissions``
     - Form submission records

``form_submissions``
~~~~~~~~~~~~~~~~~~~~

Form submission records.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``date_submitted``
     - datetime
     - Date and time when the Contact submitted the Form
   * - ``form_id``
     - int
     - ID of the Form
   * - ``id``
     - int
     - Primary key
   * - ``ip_id``
     - int
     - ID of the IP address
   * - ``lead_id``
     - int
     - ID of the Contact who submitted the Form
   * - ``page_id``
     - int
     - ID of the Landing Page containing the Form
   * - ``referer``
     - string
     - Referring URL
   * - ``tracking_id``
     - string
     - Tracking identifier


.. vale off

Page statistics
---------------

.. vale on

.. vale off

.. list-table::
   :header-rows: 1

   * - Table
     - Description
   * - ``page_hits``
     - Web page visit tracking
   * - ``page_redirects``
     - Redirect URL hit tracking
   * - ``video_hits``
     - Video viewing analytics
   * - ``channel_url_trackables``
     - Cross-Channel URL tracking

.. vale on

``page_hits``
~~~~~~~~~~~~~

Web page visit tracking.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``browser_languages``
     - string
     - Browser language preferences
   * - ``city``
     - string
     - City from geolocation
   * - ``code``
     - string
     - HTTP response code
   * - ``country``
     - string
     - Country from geolocation
   * - ``date_hit``
     - datetime
     - Date and time of the page visit
   * - ``date_left``
     - datetime
     - Date and time when the visitor left the page
   * - ``device_id``
     - int
     - ID of the device
   * - ``email_id``
     - int
     - ID of the Email that contained the page link
   * - ``id``
     - int
     - Primary key
   * - ``ip_id``
     - int
     - ID of the IP address
   * - ``isp``
     - string
     - Internet service provider
   * - ``lead_id``
     - int
     - ID of the Contact
   * - ``organization``
     - string
     - Organization from IP lookup
   * - ``page_id``
     - int
     - ID of the Landing Page
   * - ``page_language``
     - string
     - Language of the page
   * - ``query``
     - string
     - Query string from the URL
   * - ``redirect_id``
     - int
     - ID of the redirect if applicable
   * - ``referer``
     - string
     - Referring URL
   * - ``region``
     - string
     - Region or state from geolocation
   * - ``remote_host``
     - string
     - Remote host name
   * - ``source``
     - string
     - Source of the page hit
   * - ``source_id``
     - int
     - ID of the source item
   * - ``tracking_id``
     - string
     - Tracking identifier
   * - ``url``
     - string
     - Full URL visited
   * - ``url_title``
     - string
     - Title of the visited page
   * - ``user_agent``
     - string
     - Browser user agent string

``page_redirects``
~~~~~~~~~~~~~~~~~~

Redirect URL hit tracking.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``checked_out``
     - datetime
     - Date and time when a User checked out the redirect for editing
   * - ``checked_out_by``
     - int
     - ID of the User who checked out the redirect
   * - ``checked_out_by_user``
     - string
     - Name of the User who checked out the redirect
   * - ``created_by``
     - int
     - ID of the User who created the redirect
   * - ``created_by_user``
     - string
     - Name of the User who created the redirect
   * - ``date_added``
     - datetime
     - Date and time when a User created the redirect
   * - ``date_modified``
     - datetime
     - Date and time when a User last modified the redirect
   * - ``hits``
     - int
     - Total number of hits
   * - ``id``
     - int
     - Primary key
   * - ``is_published``
     - boolean
     - Published status - ``1`` or ``true`` turns on the redirect
   * - ``modified_by``
     - int
     - ID of the User who last modified the redirect
   * - ``modified_by_user``
     - string
     - Name of the User who last modified the redirect
   * - ``redirect_id``
     - string
     - Unique redirect identifier
   * - ``unique_hits``
     - int
     - Number of unique hits
   * - ``url``
     - string
     - Target URL for the redirect

``video_hits``
~~~~~~~~~~~~~~

Video viewing analytics.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``browser_languages``
     - string
     - Browser language preferences
   * - ``channel``
     - string
     - Communication Channel
   * - ``channel_id``
     - int
     - ID of the Channel item
   * - ``city``
     - string
     - City from geolocation
   * - ``code``
     - string
     - HTTP response code
   * - ``country``
     - string
     - Country from geolocation
   * - ``date_hit``
     - datetime
     - Date and time when the Contact accessed the video
   * - ``date_left``
     - datetime
     - Date and time when the viewer left
   * - ``duration``
     - int
     - Total duration of the video in seconds
   * - ``guid``
     - string
     - Global unique identifier for the video
   * - ``id``
     - int
     - Primary key
   * - ``ip_id``
     - int
     - ID of the IP address
   * - ``isp``
     - string
     - Internet service provider
   * - ``lead_id``
     - int
     - ID of the Contact
   * - ``organization``
     - string
     - Organization from IP lookup
   * - ``page_language``
     - string
     - Language of the page containing the video
   * - ``query``
     - string
     - Query string from the URL
   * - ``referer``
     - string
     - Referring URL
   * - ``region``
     - string
     - Region or state from geolocation
   * - ``remote_host``
     - string
     - Remote host name
   * - ``time_watched``
     - int
     - Time spent watching the video in seconds
   * - ``url``
     - string
     - URL of the video
   * - ``user_agent``
     - string
     - Browser user agent string

``channel_url_trackables``
~~~~~~~~~~~~~~~~~~~~~~~~~~

Cross-Channel URL tracking.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``channel``
     - string
     - Communication Channel
   * - ``channel_id``
     - int
     - ID of the Channel item
   * - ``hits``
     - int
     - Total number of hits
   * - ``redirect_id``
     - int
     - ID of the redirect
   * - ``unique_hits``
     - int
     - Number of unique hits

Point statistics
----------------

.. list-table::
   :header-rows: 1

   * - Table
     - Description
   * - ``point_lead_action_log``
     - Execution log for Point Actions
   * - ``point_lead_event_log``
     - Execution log for Point Triggers events

``point_lead_action_log``
~~~~~~~~~~~~~~~~~~~~~~~~~

Execution log for Point Actions.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``date_fired``
     - datetime
     - Date and time when Mautic executed the Point Action
   * - ``ip_id``
     - int
     - ID of the IP address
   * - ``lead_id``
     - int
     - ID of the Contact
   * - ``point_id``
     - int
     - ID of the Point Action

``point_lead_event_log``
~~~~~~~~~~~~~~~~~~~~~~~~

Execution log for Point Triggers events.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``date_fired``
     - datetime
     - Date and time when Mautic executed the Point Trigger Event
   * - ``event_id``
     - int
     - ID of the Point Trigger Event
   * - ``ip_id``
     - int
     - ID of the IP address
   * - ``lead_id``
     - int
     - ID of the Contact

Stage statistics
----------------

.. list-table::
   :header-rows: 1

   * - Table
     - Description
   * - ``stage_lead_action_log``
     - Stage assignment log

``stage_lead_action_log``
~~~~~~~~~~~~~~~~~~~~~~~~~

Stage assignment log.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``date_fired``
     - datetime
     - Date and time when Mautic assigned the Stage
   * - ``ip_id``
     - int
     - ID of the IP address
   * - ``lead_id``
     - int
     - ID of the Contact
   * - ``stage_id``
     - int
     - ID of the Stage

.. vale off

Dynamic Content statistics
--------------------------

.. vale on

.. list-table::
   :header-rows: 1

   * - Table
     - Description
   * - ``dynamic_content_stats``
     - Dynamic Content display statistics
   * - ``dynamic_content_lead_data``
     - Contact-level Dynamic Content interactions

``dynamic_content_stats``
~~~~~~~~~~~~~~~~~~~~~~~~~

Dynamic Content display statistics.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``date_sent``
     - datetime
     - Date and time when Mautic first sent the Dynamic Content
   * - ``dynamic_content_id``
     - int
     - ID of the Dynamic Content item
   * - ``id``
     - int
     - Primary key
   * - ``last_sent``
     - datetime
     - Date and time when Mautic last sent the Dynamic Content
   * - ``lead_id``
     - int
     - ID of the Contact
   * - ``sent_count``
     - int
     - Number of times Mautic sent the Dynamic Content
   * - ``sent_details``
     - string
     - Details about Dynamic Content sends in JSON format
   * - ``source``
     - string
     - Source of the Dynamic Content display
   * - ``source_id``
     - int
     - ID of the source item
   * - ``tokens``
     - string
     - Token values used in JSON format

``dynamic_content_lead_data``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Contact-level Dynamic Content interactions.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``date_added``
     - datetime
     - Date and time when Mautic recorded the interaction
   * - ``dynamic_content_id``
     - int
     - ID of the Dynamic Content item
   * - ``id``
     - int
     - Primary key
   * - ``lead_id``
     - int
     - ID of the Contact
   * - ``slot``
     - string
     - Slot name where Mautic displayed the Dynamic Content

Notification statistics
-----------------------

.. list-table::
   :header-rows: 1

   * - Table
     - Description
   * - ``push_notification_stats``
     - Push Notification delivery and engagement

``push_notification_stats``
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Push Notification delivery and engagement.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``click_count``
     - int
     - Number of times the Contact clicked the notification
   * - ``click_details``
     - string
     - Details about clicks in JSON format
   * - ``date_clicked``
     - datetime
     - Date and time when the Contact first clicked the notification
   * - ``date_read``
     - datetime
     - Date and time when the Contact read the notification
   * - ``date_sent``
     - datetime
     - Date and time when Mautic sent the notification
   * - ``id``
     - int
     - Primary key
   * - ``ip_id``
     - int
     - ID of the IP address
   * - ``is_clicked``
     - boolean
     - Click status - ``1`` or ``true`` indicates the Contact clicked the notification
   * - ``last_clicked``
     - datetime
     - Date and time when the Contact last clicked the notification
   * - ``lead_id``
     - int
     - ID of the Contact
   * - ``list_id``
     - int
     - ID of the Segment that received the notification
   * - ``notification_id``
     - int
     - ID of the Push Notification
   * - ``retry_count``
     - int
     - Number of delivery retry attempts
   * - ``source``
     - string
     - Source of the notification send
   * - ``source_id``
     - int
     - ID of the source item
   * - ``tokens``
     - string
     - Token values used in JSON format
   * - ``tracking_hash``
     - string
     - Unique hash for tracking this notification send

SMS statistics
--------------

.. list-table::
   :header-rows: 1

   * - Table
     - Description
   * - ``sms_message_stats``
     - SMS delivery statistics

``sms_message_stats``
~~~~~~~~~~~~~~~~~~~~~

SMS delivery statistics.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``date_sent``
     - datetime
     - Date and time when Mautic sent the SMS
   * - ``id``
     - int
     - Primary key
   * - ``ip_id``
     - int
     - ID of the IP address
   * - ``lead_id``
     - int
     - ID of the Contact
   * - ``list_id``
     - int
     - ID of the Segment that received the SMS
   * - ``sms_id``
     - int
     - ID of the SMS message
   * - ``source``
     - string
     - Source of the SMS send
   * - ``source_id``
     - int
     - ID of the source item
   * - ``tokens``
     - string
     - Token values used in JSON format
   * - ``tracking_hash``
     - string
     - Unique hash for tracking this SMS send

System statistics
-----------------

.. list-table::
   :header-rows: 1

   * - Table
     - Description
   * - ``audit_log``
     - System-wide audit trail of User Actions
   * - ``ip_addresses``
     - IP address registry with geolocation data
   * - ``webhook_logs``
     - Webhook execution logs

``audit_log``
~~~~~~~~~~~~~

System-wide audit trail of User Actions.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``action``
     - string
     - Action that the system performed
   * - ``bundle``
     - string
     - Mautic bundle that triggered the action
   * - ``date_added``
     - datetime
     - Date and time of the action
   * - ``details``
     - string
     - Additional details about the action in JSON format
   * - ``id``
     - int
     - Primary key
   * - ``ip_address``
     - string
     - IP address of the User who performed the action
   * - ``object``
     - string
     - Object type affected by the action
   * - ``object_id``
     - int
     - ID of the affected object
   * - ``user_id``
     - int
     - ID of the User who performed the action
   * - ``user_name``
     - string
     - Name of the User who performed the action

``ip_addresses``
~~~~~~~~~~~~~~~~

IP address registry with geolocation data.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``id``
     - int
     - Primary key
   * - ``ip_address``
     - string
     - The IP address
   * - ``ip_details``
     - string
     - Geolocation and other details in JSON format

``webhook_logs``
~~~~~~~~~~~~~~~~

Webhook execution logs.

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Column
     - Type
     - Description
   * - ``date_added``
     - datetime
     - Date and time when Mautic executed the webhook
   * - ``id``
     - int
     - Primary key
   * - ``note``
     - string
     - Notes about the webhook execution
   * - ``runtime``
     - float
     - Execution time in seconds
   * - ``status_code``
     - int
     - HTTP response status code
   * - ``webhook_id``
     - int
     - ID of the Webhook
