Dashboard widget data
#####################

Use this endpoint to retrieve the statistical data that powers Mautic's Dashboard widgets. Each widget type returns a dataset you can visualize directly, or a raw format that's easier to process yourself.

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
   $dataApi  = $api->newApi("data", $auth, $apiUrl);

.. note::

   The Data API only supports read operations. Calling the ``create``, ``edit``, or ``delete`` methods returns an error.

.. _get available widget types:

Get available widget types
**************************

.. vale off

Retrieves the list of available widget types, grouped by category.

.. vale on

.. code-block:: php

   <?php
   $types = $dataApi->getList();

.. vale off

HTTP request
============

.. vale on

``GET /data``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the widget types.

.. code-block:: json

   {
       "success": 1,
       "types": {
           "Core Widgets": {
               "recent.activity": "Recent Activity"
           },
           "Contact Widgets": {
               "created.leads.in.time": "Created contacts in time",
               "anonymous.vs.identified.leads": "Anonymous vs identified contacts",
               "map.of.leads": "Map",
               "top.lists": "Top segments",
               "top.creators": "Top contact creators",
               "top.owners": "Top contact owners",
               "created.leads": "Created contacts"
           },
           "Page Widgets": {
               "page.hits.in.time": "Page visits in time",
               "unique.vs.returning.leads": "Unique vs returning visitors",
               "dwell.times": "Dwell times",
               "popular.pages": "Popular landing pages",
               "created.pages": "Created Landing pages"
           },
           "Point Widgets": {
               "points.in.time": "Points in time"
           },
           "Form Widgets": {
               "submissions.in.time": "Submissions in time",
               "top.submission.referrers": "Top submission referrers",
               "top.submitters": "Top submitters",
               "created.forms": "Created forms"
           },
           "Email Widgets": {
               "emails.in.time": "Emails in time",
               "sent.email.to.contacts": "Sent email to contacts",
               "most.hit.email.redirects": "Most hit email redirects",
               "ignored.vs.read.emails": "Ignored vs read",
               "upcoming.emails": "Upcoming emails",
               "most.sent.emails": "Most sent emails",
               "most.read.emails": "Most read emails",
               "created.emails": "Created emails"
           },
           "Asset Widgets": {
               "asset.downloads.in.time": "Downloads in time",
               "unique.vs.repetitive.downloads": "Unique vs repetitive downloads",
               "popular.assets": "Popular assets",
               "created.assets": "Created assets"
           },
           "Campaign Widgets": {
               "events.in.time": "Events triggered in time",
               "leads.added.in.time": "Leads added in time"
           }
       }
   }

Get widget data by type
***********************

Retrieves the data for a single widget, identified by its type. Use one of the type keys returned by :ref:`Get available widget types <get available widget types>`.

.. code-block:: php

   <?php
   $data = $dataApi->get($type, $options);

.. vale off

HTTP request
============

.. vale on

``GET /data/{type}?dateFrom={YYYY-mm-dd}&dateTo={YYYY-mm-dd}&timeUnit={m}``

By default, the response returns data that the :xref:`ChartJS` library can visualize directly.

Response
========

* Returns ``200 OK`` when the request successfully retrieves the widget data.

.. code-block:: json

   {
       "success": 1,
       "cached": false,
       "execution_time": 0.043900966644287,
       "data": {
           "chartType": "line",
           "chartHeight": 220,
           "chartData": {
               "labels": [
                   "Jan 2016",
                   "Feb 2016",
                   "Mar 2016",
                   "Apr 2016",
                   "May 2016"
               ],
               "datasets": [{
                   "label": "Submission Count",
                   "data": [12, 6, 0, 0, 0],
                   "fillColor": "rgba(78,93,157,0.1)",
                   "strokeColor": "rgba(78,93,157,0.8)",
                   "pointColor": "rgba(78,93,157,0.75)",
                   "pointHighlightStroke": "rgba(78,93,157,1)"
               }]
           }
       }
   }

Get widget data in raw format
*****************************

Add the ``dataFormat=raw`` query parameter to receive the data in a raw format that's easier to process.

.. vale off

HTTP request
============

.. vale on

``GET /data/{type}?dateFrom={YYYY-mm-dd}&dateTo={YYYY-mm-dd}&timeUnit={m}&dataFormat={raw}``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the widget data.

.. code-block:: json

   {
       "success": 1,
       "cached": false,
       "execution_time": 0.039958000183105,
       "data": {
           "Submission Count": {
               "Jan 2016": 12,
               "Feb 2016": 6,
               "Mar 2016": 0,
               "Apr 2016": 0,
               "May 2016": 0
           }
       }
   }

Query parameters
****************

The following query parameters are available for the ``GET /data/{type}`` endpoint.

.. list-table::
   :widths: 20 15 25 40
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
     - ``2016-03-28``
     - Start date in the ``YYYY-mm-dd HH:ii:ss`` format
   * - ``dateTo``
     - string
     - ``2016-04-28``
     - End date in the ``YYYY-mm-dd HH:ii:ss`` format
   * - ``timeUnit``
     - string
     - ``m``
     - Date or time unit. Available options: ``Y``, ``m``, ``W``, ``d``, ``H``
   * - ``limit``
     - int
     - ``10``
     - Limit of the table widget items
   * - ``filter``
     - array
     - ``[lead_id => 23]``
     - Filters to apply to the SQL query

Widget-specific parameters
**************************

Some widget types accept additional filter and dataset parameters.

.. vale off

'Emails in time' widget
=======================

.. vale on

Accepts the following filter parameters.

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``filter[companyId]``
     - int
     - Only include Emails from Contacts assigned to the provided Company
   * - ``filter[campaignId]``
     - int
     - Only include Emails from Contacts in the provided Campaign
   * - ``filter[segmentId]``
     - int
     - Only include Emails from Contacts assigned to the provided Segment

Use the ``dataset`` parameter to request additional datasets in the response. Available values are ``sent``, ``opened``, ``unsubscribed``, ``clicked``, ``bounced``, and ``failed``.

.. vale off

HTTP request
------------

.. vale on

``GET /api/data/emails.in.time?dateFrom={YYYY-mm-dd}&dateTo={YYYY-mm-dd}&timeUnit={m}&filter[campaignId]={int}&filter[companyId]={int}&filter[segmentId]={int}&withCounts&dataset[]=sent&dataset[]=opened&dataset[]=unsubscribed&dataset[]=clicked``

.. vale off

'Sent email to contacts' widget
===============================

.. vale on

Accepts the same ``filter[companyId]``, ``filter[campaignId]``, and ``filter[segmentId]`` parameters as the ``emails.in.time`` widget.

.. vale off

HTTP request
------------

.. vale on

``GET /api/data/sent.email.to.contacts?dateFrom={YYYY-mm-dd}&dateTo={YYYY-mm-dd}&timeUnit={m}&filter[campaignId]={int}&filter[companyId]={int}&filter[segmentId]={int}&limit=10&offset=0``

.. vale off

'Most hit email redirects' widget
==================================

.. vale on

Accepts the same ``filter[companyId]``, ``filter[campaignId]``, and ``filter[segmentId]`` parameters as the ``emails.in.time`` widget.

.. vale off

HTTP request
------------

.. vale on

``GET /api/data/most.hit.email.redirects?dateFrom={YYYY-mm-dd}&dateTo={YYYY-mm-dd}&timeUnit={m}&filter[campaignId]={int}&filter[companyId]={int}&filter[segmentId]={int}&limit=10&offset=0``
