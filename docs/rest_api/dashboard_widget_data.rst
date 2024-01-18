Dashboard widget data
#####################

Use this endpoint to obtain details on Mautic's dashboard statistical data.

**Using Mautic's API Library**

You can interact with this API through the :xref:`Mautic API Library` as follows, or use the various http endpoints as described in this document.

.. code-block:: php

   <?php
   use Mautic\MauticApi;
   use Mautic\Auth\ApiAuth;

   // ...
   $initAuth   = new ApiAuth();
   $auth       = $initAuth->newAuth($settings);
   $apiUrl     = "https://mautic.example.com";
   $api        = new MauticApi();
   $contactApi = $api->newApi("data", $auth, $apiUrl);

.. vale off

Get list of available widget types
**********************************

.. vale on

.. code-block:: php

   <?php
   $data = $dataApi->getList();

.. vale off

**HTTP Request**

.. vale on

``GET /data``

``Expected Response Code: 200``

.. code-block:: json

   {
       "success":1,
       "types":{
           "Core Widgets":{
               "recent.activity":"Recent Activity"
           },
           "Contact Widgets":{
               "created.leads.in.time":"Created Contacts in time",
               "anonymous.vs.identified.leads":"Anonymous vs identified contacts",
               "map.of.leads":"Map",
               "top.lists":"Top Segments",
               "top.creators":"Top contact creators",
               "top.owners":"Top contact owners",
               "created.leads":"Created contacts"
           },
           "Page Widgets":{
               "page.hits.in.time":"Page visits in time",
               "unique.vs.returning.leads":"Unique vs returning visitors",
               "dwell.times":"Dwell times",
               "popular.pages":"Popular landing pages",
               "created.pages":"Created Landing pages"
           },
           "Point Widgets":{
               "points.in.time":"Points in time"
           },
           "Form Widgets":{
               "submissions.in.time":"Submissions in time",
               "top.submission.referrers":"Top submission referrers",
               "top.submitters":"Top submitters",
               "created.forms":"Created forms"
           },
           "Email Widgets":{
               "emails.in.time":"Emails in time",
               "sent.email.to.contacts":"Sent email to contacts",
               "most.hit.email.redirects":"Most hit email redirects",
               "ignored.vs.read.emails":"Ignored vs read",
               "upcoming.emails":"Upcoming emails",
               "most.sent.emails":"Most sent emails",
               "most.read.emails":"Most read emails",
               "created.emails":"Created emails"
           },
           "Asset Widgets":{
               "asset.downloads.in.time":"Downloads in time",
               "unique.vs.repetitive.downloads":"Unique vs repetitive downloads",
               "popular.assets":"Popular assets",
               "created.assets":"Created assets"
           },
           "Campaign Widgets":{
               "events.in.time":"Events triggered in time",
               "leads.added.in.time":"Leads added in time"
           }
       }
   }

Get individual widget data by type
**********************************

.. code-block:: php

   <?php
   $data = $dataApi->get($type, $options);

.. vale off

**HTTP Request**

.. vale on

``GET /data/{type}?dateFrom={YYYY-mm-dd}&dateTo={YYYY-mm-dd}&timeUnit={m}``

Returns response which can be directly visualized by the `chartJS <http://www.chartjs.org/>`_ library.

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "success":1,
       "cached":false,
       "execution_time":0.043900966644287,
       "data":{
           "chartType":"line",
           "chartHeight":220,
           "chartData":{
               "labels":[
                   "Jan 2016",
                   "Feb 2016",
                   "Mar 2016",
                   "Apr 2016",
                   "May 2016"
               ],
               "datasets":[{
                   "label":"Submission Count",
                   "data":[
                       12,
                       6,
                       0,
                       0,
                       0
                   ],
                   "fillColor":"rgba(78,93,157,0.1)",
                   "strokeColor":"rgba(78,93,157,0.8)",
                   "pointColor":"rgba(78,93,157,0.75)",
                   "pointHighlightStroke":"rgba(78,93,157,1)"
               }]
           }
       }
   }

.. vale off

**HTTP Request**

.. vale on

``GET /data/{type}?dateFrom={YYYY-mm-dd}&dateTo={YYYY-mm-dd}&timeUnit={m}&dataFormat={raw}``

Returns raw format which can be more easily processed.

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "success":1,
       "cached":false,
       "execution_time":0.039958000183105,
       "data":{
           "Submission Count":{
               "Jan 2016":12,
               "Feb 2016":6,
               "Mar 2016":0,
               "Apr 2016":0,
               "May 2016":0
           }
       }
   }

"Emails in time" widget
***********************

**Filter parameters**

.. list-table::
   :header-rows: 1

   * - Filter
     - Type
     - Description
   * - ``filter[companyId]``
     - int
     - Filter only Emails from Contacts assigned to provided Company.
   * - ``filter[campaignId]``
     - int
     - Filter only Emails from Contacts that got sent as part of provided Campaign.
   * - ``filter[segmentId]``
     - int
     - Filter only Emails from Contacts assigned to provided Segment.

**Dataset parameter**

You can provide one or more of the following dataset parameters in an array:

* sent
* opened
* unsubscribed
* clicked
* bounced
* failed
  Provide more datasets in response based on request.

.. vale off

**HTTP Request**

.. vale on

``GET /api/data/emails.in.time?dateFrom={YYYY-mm-dd}&dateTo={YYYY-mm-dd}&timeUnit={m}&filter[campaignId]={int}&filter[companyId]={int}&filter[segmentId]={int}&withCounts&dataset[]=sent&dataset[]=opened&dataset[]=unsubscribed&dataset[]=clicked``

.. vale off

"Sent Email to Contacts" Widget
*******************************

.. vale on

**Filter parameters**

.. list-table::
   :header-rows: 1

   * - Filter
     - Type
     - Description
   * - ``filter[companyId]``
     - int
     - Filter only Emails from Contacts assigned to provided Company.
   * - ``filter[campaignId]``
     - int
     - Filter only Emails from Contacts that got sent as part of provided Campaign.
   * - ``filter[segmentId]``
     - int
     - Filter only Emails from Contacts assigned to provided Segment.

.. vale off

**HTTP Request**

.. vale on

``GET /api/data/sent.email.to.contacts?dateFrom={YYYY-mm-dd}&dateTo={YYYY-mm-dd}&timeUnit={m}&filter[campaignId]={int}&filter[companyId]={int}&filter[segmentId]={int}&limit=10&offset=0``

.. vale off

"Most hit Email redirects" widgets
**********************************

.. vale on

**Filter parameters**

.. list-table::
   :header-rows: 1

   * - Filter
     - Type
     - Description
   * - ``filter[companyId]``
     - int
     - Filter only Emails from Contacts assigned to provided Company.
   * - ``filter[campaignId]``
     - int
     - Filter only Emails from Contacts that got sent as part of provided Campaign.
   * - ``filter[segmentId]``
     - int
     - Filter only Emails from Contacts assigned to provided Segment.

.. vale off

**HTTP Request**

.. vale on

``GET /api/data/most.hit.email.redirects?dateFrom={YYYY-mm-dd}&dateTo={YYYY-mm-dd}&timeUnit={m}&filter[campaignId]={int}&filter[companyId]={int}&filter[segmentId]={int}&limit=10&offset=0``

**Available data URL query parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Example
     - Description
   * - ``timezone``
     - string
     - ``America/New_York``
     - PHP timezone
   * - ``dateFrom``
     - string
     - ``2016-28-03``
     - Date from in the ``YYYY-mm-dd HH:ii:ss`` format
   * - ``dateTo``
     - string
     - ``2016-28-04``
     - Date to in the ``YYYY-mm-dd HH:ii:ss`` format
   * - ``timeUnit``
     - string
     - ``m``
     - Date/Time unit. Available options: ``Y, m, W, d, H``
   * - ``limit``
     - int
     - ``10``
     - Limit of the table widget items
   * - ``filter``
     - array
     - ``[lead_id => 23]``
     - filters which should to apply to the SQL query
