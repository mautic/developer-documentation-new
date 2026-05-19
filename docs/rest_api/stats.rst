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
     - Number of rows to return. Defaults to 100.
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

Dynamic Content statistics
--------------------------

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
