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
     - Contact Category assignments
   * - ``lead_companies_change_log``
     - Log of Contact Company association changes
   * - ``lead_devices``
     - Device information tracked for Contacts
   * - ``lead_donotcontact``
     - Do-not-contact preferences by Contact and Channel
   * - ``lead_event_log``
     - Generic Contact event activity log
   * - ``lead_frequencyrules``
     - Contact frequency and Channel preferences
   * - ``lead_lists_leads``
     - Contact membership in Segments
   * - ``lead_points_change_log``
     - Log of Contact Points changes
   * - ``lead_stages_change_log``
     - Log of Contact Stage transitions
   * - ``lead_utmtags``
     - UTM parameters tracked for Contacts

.. vale on

Asset statistics
----------------

.. list-table::
   :header-rows: 1

   * - Table
     - Description
   * - ``asset_downloads``
     - Asset download events

Campaign statistics
-------------------

.. list-table::
   :header-rows: 1

   * - Table
     - Description
   * - ``campaign_leads``
     - Contacts in Campaigns
   * - ``campaign_lead_event_log``
     - Campaign Event execution log

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

Form statistics
---------------

.. list-table::
   :header-rows: 1

   * - Table
     - Description
   * - ``form_submissions``
     - Form submission records


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

Point statistics
----------------

.. list-table::
   :header-rows: 1

   * - Table
     - Description
   * - ``point_lead_action_log``
     - Point Action execution log
   * - ``point_lead_event_log``
     - Point Trigger Event execution log

Stage statistics
----------------

.. list-table::
   :header-rows: 1

   * - Table
     - Description
   * - ``stage_lead_action_log``
     - Stage assignment log

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

Notification statistics
-----------------------

.. list-table::
   :header-rows: 1

   * - Table
     - Description
   * - ``push_notification_stats``
     - Push Notification delivery and engagement

SMS statistics
--------------

.. list-table::
   :header-rows: 1

   * - Table
     - Description
   * - ``sms_message_stats``
     - SMS delivery statistics

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
