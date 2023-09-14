Reports
#######

Use this endpoint to obtain details on Mautic's Reports.

**Using Mautic's API Library**

You can interact with this API through the :xref:`Mautic API Library` as follows, or use the various http endpoints as described in this document.

.. code-block:: php

   <?php
   use Mautic\MauticApi;
   use Mautic\Auth\ApiAuth;

   // ...
   $initAuth  = new ApiAuth();
   $auth      = $initAuth->newAuth($settings);
   $apiUrl    = "https://example.com";
   $api       = new MauticApi();
   $reportApi = $api->newApi("reports", $auth, $apiUrl);

.. vale off

Get report
**********

.. vale on

.. code-block:: php

   <?php

   //...
   // Get all with default options:
   $report = $reportApi->get($id);

   // Or define exactly what rows you want:
   $limit    = 100;
   $page     = 2;
   $dateFrom = \DateTime('1 week ago');
   $dateTo   = \DateTime('now');
   $report   = $reportApi->get($id, $limit, $page, $dateFrom, $dateTo);

Get an individual Report by ID.

.. vale off

**HTTP Request**

.. vale on

``GET /reports/ID``

Or define query parameters like this:

``GET /reports/3?dateFrom=2017-01-01&dateTo=2018-01-01&limit=5&page=3``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
     "totalResults": 3990,
     "data": [
       {
         "id2": "12",
         "email1": "john@example.com",
         "firstname1": "",
         "lastname1": ""
       },
       {
         "id2": "23",
         "email1": "alex@example.com",
         "firstname1": "",
         "lastname1": ""
       },
       {
         "id2": "24",
         "email1": "amal@example.com",
         "firstname1": "",
         "lastname1": ""
       },
       {
         "id2": "25",
         "email1": "ariel@example.com",
         "firstname1": "",
         "lastname1": ""
       },
       {
         "id2": "26",
         "email1": "bola@example.com",
         "firstname1": "",
         "lastname1": ""
       }
     ],
     "dataColumns": {
       "address11": "l.address1",
       "address21": "l.address2",
       "attribution1": "l.attribution",
       "attribution_date1": "l.attribution_date",
       "city1": "l.city",
       "company1": "l.company",
       "companyaddress11": "comp.companyaddress1",
       "companyaddress21": "comp.companyaddress2",
       "companycity1": "comp.companycity",
       "companyemail1": "comp.companyemail",
       "companyname1": "comp.companyname",
       "companycountry1": "comp.companycountry",
       "companydescription1": "comp.companydescription",
       "companyfax1": "comp.companyfax",
       "id1": "comp.id",
       "companyphone1": "comp.companyphone",
       "companystate1": "comp.companystate",
       "companywebsite1": "comp.companywebsite",
       "companyzipcode1": "comp.companyzipcode",
       "id2": "l.id",
       "country1": "l.country",
       "custom_select1": "l.custom_select",
       "date_identified1": "l.date_identified",
       "email1": "l.email",
       "facebook1": "l.facebook",
       "fax1": "l.fax",
       "firstname1": "l.firstname",
       "foursquare1": "l.foursquare",
       "gender1": "l.gender",
       "googleplus1": "l.googleplus",
       "ip_address1": "i.ip_address",
       "instagram1": "l.instagram",
       "is_primary1": "companies_lead.is_primary",
       "lastname1": "l.lastname",
       "linkedin1": "l.linkedin",
       "mobile1": "l.mobile",
       "multiline1": "l.multiline",
       "multiselect1": "l.multiselect",
       "owner_id1": "l.owner_id",
       "first_name1": "u.first_name",
       "last_name1": "u.last_name",
       "phone1": "l.phone",
       "points1": "l.points",
       "position1": "l.position",
       "preferred_locale1": "l.preferred_locale",
       "timezone1": "l.timezone",
       "skype1": "l.skype",
       "state1": "l.state",
       "title1": "l.title",
       "twitter1": "l.twitter",
       "website1": "l.website",
       "zipcode1": "l.zipcode",
     },
     "limit": 5,
     "page": 3,
     "dateFrom": "2017-01-01T00:00:00+00:00",
     "dateTo": "2018-10-24T11:55:29+00:00",
   }

**Report Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``totalResults``
     - int
     - Amount of results in the defined date range. Default date range is from 30 days ago to now
   * - ``data``
     - array
     - Holds rows of the Report specific to each Report's data type and selected columns
   * - ``dataColumns``
     - array
     - Array of supported column names for the Report data type
   * - ``limit``
     - int
     - Currently applied limit
   * - ``page``
     - int
     - Currently applied ``page``
   * - ``dateFrom``
     - ``datetime``
     - Currently applied date from filter
   * - ``dateTo``
     - ``datetime``
     - Currently applied date to filter

.. vale off

List reports
************

.. vale on

.. code-block:: php

   <?php

   //...
   $reports = $reportApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

Returns a list of Contact Reports available to the User. This list isn't filterable.

.. vale off

**HTTP Request**

.. vale on

``GET /reports``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {  
     "total": 8, 
     "reports":[  
       {  
         "id": 1,
         "name": "Contacts",
         "descriptionn": "lists all contacts",
         "system": false,
         "isScheduled": false,
         "source": "leads",
         "columns": [
           "l.id",
           "l.email",
           "l.firstname",
           "l.lastname"
         ],
         "filters": [],
         "tableOrder": [],
         "graphs": [],
         "groupBy": [],
         "settings": {
           "showGraphsAboveTable": 0,
           "showDynamicFilters": 0,
           "hideDateRangeFilter": 0
         },
         "aggregators": [],
         "scheduleUnit": null,
         "toAddress": null,
         "scheduleDay": null,
         "scheduleMonthFrequency": null
       },
     ]
   }

**Report Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Report
   * - ``name``
     - string
     - The Report name
   * - ``description``
     - string
     - The Report description
   * - ``system``
     - boolean
     - If true then the Report is visible to all Users. If ``false`` then only creator can see this Report
   * - ``isScheduled``
     - boolean
     - Scheduled Reports send Report Emails as the User defines
   * - ``source``
     - string
     - Report data source type
   * - ``columns``
     - array
     - List of selected columns for this particular Report
   * - ``filters``
     - array
     - Filters applied on this Report
   * - ``tableOrder``
     - array
     - Ordering applied on this Report
   * - ``graphs``
     - array
     - Graphs defined for this Report. API won't return graphs
   * - ``groupBy``
     - array
     - Group by rules applied for this Report
   * - ``settings``
     - array
     - Additional settings for the UI layout
   * - ``aggregators``
     - array
     - Aggregation rules applied on this Report
   * - ``scheduleUnit``
     - string or null
     - Unit for the scheduler
   * - ``toAddress``
     - string or null
     - Email address for the scheduler
   * - ``scheduleDay``
     - string or null
     - Day for the scheduler
   * - ``scheduleMonthFrequency``
     - string or null
     - Frequency for the scheduler

.. vale off

Create Report
*************

.. vale on

.. code-block:: php

   <?php

   $data = [
       'name'        => 'Segment Members',
       'description' => 'This is my first Report created via API.',
       'isPublished' => 1,
       'source'      => 'segment.membership',
       'columns'     => [
           'l.id',
           'l.email',
           'l.firstname',
           'l.lastname'
       ],
        'filters' => [
          'column' => 'lll.leadlist_id',
          'glue' => 'and',
          'value' => '2',
          'dynamic' => NULL,
          'condition' => 'eq',
        ],
   ];

   $report = $reportApi->create($data);

Create a new Report.

.. vale off

**HTTP Request**

.. vale on

``POST /reports/new``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``name``
     - string
     - Report title is one of the required fields
   * - ``source``
     - string
     - Data source for the Report. Available options: ``assets, asset.downloads, campaign_lead_event_log, message.channel, emails, email.stats, forms, form.submissions, contact.dnc, contact.devices, contact.frequencyrules, contact.attribution.multi, contact.attribution.first, contact.attribution.last, lead.pointlog, leads, lead.utmTag, segment.log, segment.membership, group.score, companies, mobile_notifications, mobile_notifications.stats, pages, page.hits, video.hits``
   * - ``description``
     - string
     - A description of the Report.
   * - ``isPublished``
     - int
     - A value of 0 or 1
   * - ``columns``
     - array
     - Which columns to include in the Report. The list of the Reports is different for each data source. Please get the list from the UI by inspecting the ``form`` field. The columns must include the table alias. For example: ``l.id, l.email, l.firstname, l.lastname``
   * - ``filters``
     - array
     - A list of arrays defining filters. Each filter has the following keys: column, glue, value, dynamic, condition. The column must include the table alias. For example: ``l.id, l.email, l.firstname, l.lastname``
   * - ``tableOrder``
     - array
     - List of columns and their order. The column must include the table alias. For example: ``l.id, l.email, l.firstname, l.lastname``. The order must be either ``ASC`` or ``DESC``.
   * - ``groupBy``
     - array
     - List of columns to group by. The column must include the table alias. For example: ``l.id, l.email, l.firstname, l.lastname``

**Response**

``Expected Response Code: 201``

**Properties**

Same as `Get Report <#get-report>`_.

.. vale off

Edit Report
*****************

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = [
       'name'        => 'Segment Members',
       'description' => 'This is my first Report created via API.',
       'isPublished' => 1,
       'source'      => 'segment.membership',
       'columns'     => [
           'l.id',
           'l.email',
           'l.firstname',
           'l.lastname'
       ],
        'filters' => [
          'column' => 'lll.leadlist_id',
          'glue' => 'and',
          'value' => '2',
          'dynamic' => NULL,
          'condition' => 'eq',
        ],
   ];

   // Create new a Report of ID 1 isn't found?
   $createIfNotFound = true;

   $page = $reportApi->edit($id, $data, $createIfNotFound);

Edit a new Report. Note that this supports PUT or PATCH depending on the desired behavior.

**PUT** creates a Report if the given ID doesn't exist and clears all the Report information, adds the information from the request.

**PATCH** fails if the Report with the given ID doesn't exist and updates the Report field values with the values from the request.

.. vale off

**HTTP Request**

.. vale on

To edit a Report and return a 404 if the Report isn't found:

``PATCH /reports/ID/edit``

To edit a Report and create a new one if the Report isn't found:

``PUT /reports/ID/edit``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``name``
     - string
     - Report title is one of the required fields
   * - ``source``
     - string
     - Data source for the Report. Available options: ``assets, asset.downloads, campaign_lead_event_log, message.channel, emails, email.stats, forms, form.submissions, contact.dnc, contact.devices, contact.frequencyrules, contact.attribution.multi, contact.attribution.first, contact.attribution.last, lead.pointlog, leads, lead.utmTag, segment.log, segment.membership, group.score, companies, mobile_notifications, mobile_notifications.stats, pages, page.hits, video.hits``
   * - ``description``
     - string
     - A description of the Report.
   * - ``isPublished``
     - int
     - A value of 0 or 1
   * - ``columns``
     - array
     - Which columns to include in the Report. The list of the Reports is different for each data source. Please get the list from the UI by inspecting the ``form`` field. The columns must include the table alias. For example: ``l.id, l.email, l.firstname, l.lastname``
   * - ``filters``
     - array
     - A list of arrays defining filters. Each filter has the following keys: ``column, glue, value, dynamic, condition``. The column must include the table alias. For example: ``l.id, l.email, l.firstname, l.lastname``
   * - ``tableOrder``
     - array
     - List of columns and their order. The column must include the table alias. For example: ``l.id, l.email, l.firstname, l.lastname``. The order must be either ``ASC`` or ``DESC``.
   * - ``groupBy``
     - array
     - List of columns to group by. The column must include the table alias. For example: ``l.id, l.email, l.firstname, l.lastname``


**Response**

If ``PUT``, the expected response code is ``200`` if editing a Report or ``201`` if creating a new one.

If ``PATCH``, the expected response code is ``200``.

**Properties**

Same as `Get Report <#get-report>`_.

.. vale off

Delete Report
*******************

.. vale on

.. code-block:: php

   <?php

   $page = $reportApi->delete($id);

Delete a Report.

.. vale off

**HTTP Request**

.. vale on

``DELETE /reports/ID/delete``

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get Report <#get-report>`_.
