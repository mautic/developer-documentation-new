Companies
#########

Use this endpoint to manipulate and obtain details on Mautic's Companies.

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
   $initAuth   = new ApiAuth();
   $auth       = $initAuth->newAuth($settings);
   $apiUrl     = "https://example.com";
   $api        = new MauticApi();
   $companyApi = $api->newApi("companies", $auth, $apiUrl);

.. vale off

Get Company
***********

.. vale on

Retrieves an individual Company.

.. code-block:: php

   <?php

   //...
   $company = $companyApi->get($id);

.. vale off

HTTP request
============

.. vale on

``GET /companies/ID``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Company.

.. _get Company response:

.. code-block:: json

   {
      "company": {
          "id": 1,
          "score": 150,
          "fields": {
              "core": {
                  "companyaddress1": {
                      "id": "29",
                      "label": "Address 1",
                      "alias": "companyaddress1",
                      "type": "text",
                      "group": "core",
                      "object": "company",
                      "is_fixed": "1",
                      "properties": "a:0:{}",
                      "default_value": null,
                      "value": "123 Main St",
                      "normalizedValue": "123 Main St"
                  },
                  "companyaddress2": {
                      "id": "30",
                      "label": "Address 2",
                      "alias": "companyaddress2",
                      "type": "text",
                      "group": "core",
                      "object": "company",
                      "is_fixed": "1",
                      "properties": "a:0:{}",
                      "default_value": null,
                      "value": "Suite 100",
                      "normalizedValue": "Suite 100"
                  },
                  "companyemail": {
                      "id": "31",
                      "label": "Company Email",
                      "alias": "companyemail",
                      "type": "email",
                      "group": "core",
                      "object": "company",
                      "is_fixed": "1",
                      "properties": "a:0:{}",
                      "default_value": null,
                      "value": "info@acme.com",
                      "normalizedValue": "info@acme.com"
                  },
                  "companyphone": {
                      "id": "32",
                      "label": "Phone",
                      "alias": "companyphone",
                      "type": "tel",
                      "group": "core",
                      "object": "company",
                      "is_fixed": "1",
                      "properties": "a:0:{}",
                      "default_value": null,
                      "value": "+1-555-123-4567",
                      "normalizedValue": "+1-555-123-4567"
                  },
                  "companycity": {
                      "id": "33",
                      "label": "City",
                      "alias": "companycity",
                      "type": "text",
                      "group": "core",
                      "object": "company",
                      "is_fixed": "1",
                      "properties": "a:0:{}",
                      "default_value": null,
                      "value": "Anytown",
                      "normalizedValue": "Anytown"
                  },
                  "companystate": {
                      "id": "34",
                      "label": "State",
                      "alias": "companystate",
                      "type": "region",
                      "group": "core",
                      "object": "company",
                      "is_fixed": "1",
                      "properties": "a:0:{}",
                      "default_value": null,
                      "value": "New York",
                      "normalizedValue": "New York"
                  },
                  "companyzipcode": {
                      "id": "35",
                      "label": "Zip Code",
                      "alias": "companyzipcode",
                      "type": "text",
                      "group": "core",
                      "object": "company",
                      "is_fixed": "1",
                      "properties": "a:0:{}",
                      "default_value": null,
                      "value": "12345",
                      "normalizedValue": "12345"
                  },
                  "companycountry": {
                      "id": "36",
                      "label": "Country",
                      "alias": "companycountry",
                      "type": "country",
                      "group": "core",
                      "object": "company",
                      "is_fixed": "1",
                      "properties": "a:0:{}",
                      "default_value": null,
                      "value": "United States",
                      "normalizedValue": "United States"
                  },
                  "companyname": {
                      "id": "37",
                      "label": "Company Name",
                      "alias": "companyname",
                      "type": "text",
                      "group": "core",
                      "object": "company",
                      "is_fixed": "1",
                      "properties": "a:0:{}",
                      "default_value": null,
                      "value": "Acme Corporation",
                      "normalizedValue": "Acme Corporation"
                  },
                  "companywebsite": {
                      "id": "38",
                      "label": "Website",
                      "alias": "companywebsite",
                      "type": "url",
                      "group": "core",
                      "object": "company",
                      "is_fixed": "1",
                      "properties": "a:0:{}",
                      "default_value": null,
                      "value": "https://acme.com",
                      "normalizedValue": "https://acme.com"
                  }
              },
              "professional": {
                  "companynumber_of_employees": {
                      "id": "39",
                      "label": "Number of Employees",
                      "alias": "companynumber_of_employees",
                      "type": "number",
                      "group": "professional",
                      "object": "company",
                      "is_fixed": "0",
                      "properties": "a:2:{s:9:\"roundmode\";i:4;s:5:\"scale\";i:0;}",
                      "default_value": null,
                      "value": 300,
                      "normalizedValue": 300
                  },
                  "companyfax": {
                      "id": "40",
                      "label": "Fax",
                      "alias": "companyfax",
                      "type": "tel",
                      "group": "professional",
                      "object": "company",
                      "is_fixed": "0",
                      "properties": "a:0:{}",
                      "default_value": null,
                      "value": "+1-555-123-7890",
                      "normalizedValue": "+1-555-123-7890"
                  },
                  "companyannual_revenue": {
                      "id": "41",
                      "label": "Annual Revenue",
                      "alias": "companyannual_revenue",
                      "type": "number",
                      "group": "professional",
                      "object": "company",
                      "is_fixed": "0",
                      "properties": "a:2:{s:9:\"roundmode\";i:4;s:5:\"scale\";i:2;}",
                      "default_value": null,
                      "value": 1000000.0,
                      "normalizedValue": 1000000.0
                  },
                  "companyindustry": {
                      "id": "42",
                      "label": "Industry",
                      "alias": "companyindustry",
                      "type": "select",
                      "group": "professional",
                      "object": "company",
                      "is_fixed": "1",
                      "properties": "a:1:{s:4:\"list\";a:41:{i:0;a:2:{s:5:\"label\";s:19:\"Aerospace & Defense\";s:5:\"value\";s:19:\"Aerospace & Defense\";}i:1;a:2:{s:5:\"label\";s:11:\"Agriculture\";s:5:\"value\";s:11:\"Agriculture\";}i:2;a:2:{s:5:\"label\";s:7:\"Apparel\";s:5:\"value\";s:7:\"Apparel\";}i:3;a:2:{s:5:\"label\";s:21:\"Automotive & Assembly\";s:5:\"value\";s:21:\"Automotive & Assembly\";}i:4;a:2:{s:5:\"label\";s:7:\"Banking\";s:5:\"value\";s:7:\"Banking\";}i:5;a:2:{s:5:\"label\";s:13:\"Biotechnology\";s:5:\"value\";s:13:\"Biotechnology\";}i:6;a:2:{s:5:\"label\";s:9:\"Chemicals\";s:5:\"value\";s:9:\"Chemicals\";}i:7;a:2:{s:5:\"label\";s:14:\"Communications\";s:5:\"value\";s:14:\"Communications\";}i:8;a:2:{s:5:\"label\";s:12:\"Construction\";s:5:\"value\";s:12:\"Construction\";}i:9;a:2:{s:5:\"label\";s:23:\"Consumer Packaged Goods\";s:5:\"value\";s:23:\"Consumer Packaged Goods\";}i:10;a:2:{s:5:\"label\";s:9:\"Education\";s:5:\"value\";s:9:\"Education\";}i:11;a:2:{s:5:\"label\";s:11:\"Electronics\";s:5:\"value\";s:11:\"Electronics\";}i:12;a:2:{s:5:\"label\";s:6:\"Energy\";s:5:\"value\";s:6:\"Energy\";}i:13;a:2:{s:5:\"label\";s:11:\"Engineering\";s:5:\"value\";s:11:\"Engineering\";}i:14;a:2:{s:5:\"label\";s:13:\"Entertainment\";s:5:\"value\";s:13:\"Entertainment\";}i:15;a:2:{s:5:\"label\";s:13:\"Environmental\";s:5:\"value\";s:13:\"Environmental\";}i:16;a:2:{s:5:\"label\";s:7:\"Finance\";s:5:\"value\";s:7:\"Finance\";}i:17;a:2:{s:5:\"label\";s:15:\"Food & Beverage\";s:5:\"value\";s:15:\"Food & Beverage\";}i:18;a:2:{s:5:\"label\";s:10:\"Government\";s:5:\"value\";s:10:\"Government\";}i:19;a:2:{s:5:\"label\";s:10:\"Healthcare\";s:5:\"value\";s:10:\"Healthcare\";}i:20;a:2:{s:5:\"label\";s:11:\"Hospitality\";s:5:\"value\";s:11:\"Hospitality\";}i:21;a:2:{s:5:\"label\";s:9:\"Insurance\";s:5:\"value\";s:9:\"Insurance\";}i:22;a:2:{s:5:\"label\";s:9:\"Machinery\";s:5:\"value\";s:9:\"Machinery\";}i:23;a:2:{s:5:\"label\";s:13:\"Manufacturing\";s:5:\"value\";s:13:\"Manufacturing\";}i:24;a:2:{s:5:\"label\";s:5:\"Media\";s:5:\"value\";s:5:\"Media\";}i:25;a:2:{s:5:\"label\";s:15:\"Metals & Mining\";s:5:\"value\";s:15:\"Metals & Mining\";}i:26;a:2:{s:5:\"label\";s:14:\"Not for Profit\";s:5:\"value\";s:14:\"Not for Profit\";}i:27;a:2:{s:5:\"label\";s:9:\"Oil & Gas\";s:5:\"value\";s:9:\"Oil & Gas\";}i:28;a:2:{s:5:\"label\";s:17:\"Packaging & Paper\";s:5:\"value\";s:17:\"Packaging & Paper\";}i:29;a:2:{s:5:\"label\";s:36:\"Private Equity & Principal Investors\";s:5:\"value\";s:36:\"Private Equity & Principal Investors\";}i:30;a:2:{s:5:\"label\";s:10:\"Recreation\";s:5:\"value\";s:10:\"Recreation\";}i:31;a:2:{s:5:\"label\";s:11:\"Real Estate\";s:5:\"value\";s:11:\"Real Estate\";}i:32;a:2:{s:5:\"label\";s:6:\"Retail\";s:5:\"value\";s:6:\"Retail\";}i:33;a:2:{s:5:\"label\";s:14:\"Semiconductors\";s:5:\"value\";s:14:\"Semiconductors\";}i:34;a:2:{s:5:\"label\";s:8:\"Shipping\";s:5:\"value\";s:8:\"Shipping\";}i:35;a:2:{s:5:\"label\";s:13:\"Social Sector\";s:5:\"value\";s:13:\"Social Sector\";}i:36;a:2:{s:5:\"label\";s:10:\"Technology\";s:5:\"value\";s:10:\"Technology\";}i:37;a:2:{s:5:\"label\";s:18:\"Telecommunications\";s:5:\"value\";s:18:\"Telecommunications\";}i:38;a:2:{s:5:\"label\";s:14:\"Transportation\";s:5:\"value\";s:14:\"Transportation\";}i:39;a:2:{s:5:\"label\";s:9:\"Utilities\";s:5:\"value\";s:9:\"Utilities\";}i:40;a:2:{s:5:\"label\";s:5:\"Other\";s:5:\"value\";s:5:\"Other\";}}}",
                      "default_value": null,
                      "value": "Technology",
                      "normalizedValue": "Technology"
                  },
                  "companydescription": {
                      "id": "43",
                      "label": "Description",
                      "alias": "companydescription",
                      "type": "text",
                      "group": "professional",
                      "object": "company",
                      "is_fixed": "1",
                      "properties": "a:0:{}",
                      "default_value": null,
                      "value": "Leading software company",
                      "normalizedValue": "Leading software company"
                  }
              },
              "other": [],
              "all": {
                  "id": 1,
                  "companyaddress1": "123 Main St",
                  "companyaddress2": "Suite 100",
                  "companyemail": "info@acme.com",
                  "companyphone": "+1-555-123-4567",
                  "companycity": "Anytown",
                  "companystate": "New York",
                  "companyzipcode": "12345",
                  "companycountry": "United States",
                  "companyname": "Acme Corporation",
                  "companywebsite": "https://acme.com",
                  "companynumber_of_employees": 300,
                  "companyfax": "+1-555-123-7890",
                  "companyannual_revenue": 1000000.0,
                  "companyindustry": "Technology",
                  "companydescription": "Leading software company"
              }
          }
      }
   }

.. _get Company properties:

Company properties
------------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - integer
     - ID of the Company
   * - ``score``
     - integer
     - Score assigned to the Company
   * - ``fields``
     - object
     - Contains grouped Company data:

       * ``all``: associative array of field aliases and values. This is the primary way to access :ref:`Company field properties <get Company field properties>`.

       * ``core`` and ``professional``: these contain the same :ref:`fields <get Company field properties>`, but bundled with additional metadata.

.. _get Company field properties:

Company field properties
------------------------

Core fields
~~~~~~~~~~~

.. list-table::
   :widths: 30 20 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``companyaddress1``
     - string
     - Company primary address line, such as street name and number
   * - ``companyaddress2``
     - string
     - Supplemental Company address details, such as suite, unit, building, or floor
   * - ``companyemail``
     - string
     - Company Email address
   * - ``companyphone``
     - string
     - Company phone number
   * - ``companycity``
     - string
     - Company city name
   * - ``companystate``
     - string
     - Company state, province, or region
   * - ``companyzipcode``
     - string
     - Company zip or postal code
   * - ``companycountry``
     - string
     - Company country name
   * - ``companyname``
     - string
     - Company name
   * - ``companywebsite``
     - string
     - Company website URL
   
Professional fields
~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 30 20 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``companynumber_of_employees``
     - integer
     - Total number of employees in the Company
   * - ``companyfax``
     - string
     - Company fax number
   * - ``companyannual_revenue``
     - number
     - Annual revenue of the Company - for example, ``1000000.0``
   * - ``companyindustry``
     - string
     - Company business sector or vertical
   * - ``companydescription``
     - string
     - Summary of the Company

.. vale off

List Companies
**************

.. vale on

Retrieves a list of Companies.

.. code-block:: php

   <?php

   //...
   $companies = $companyApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

HTTP request
============

.. vale on

``GET /companies``

Query parameters
----------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``searchFilter``
     - string
     - String or search command to filter entities
   * - ``start``
     - integer
     - Starting row for the returned entities - defaults to 0
   * - ``limit``
     - integer
     - Maximum number of entities to return - defaults to 30
   * - ``orderBy``
     - string
     - Column to sort by. Any column in the response is valid.
       
       **Note**: convert ``camelCase`` properties to ``snake_case``. For example, ``dateAdded`` becomes ``date_added``, ``webhookUrl`` becomes ``webhook_url``, and so on
   * - ``orderByDir``
     - string
     - Order direction - ``asc`` or ``desc``
   * - ``publishedOnly``
     - boolean
     - Returns only currently published entities
   * - ``minimal``
     - boolean
     - Returns only a simple mapped object of entities without additional lists in it

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Companies list.

.. code-block:: json

   {
      "total": "2",
      "companies": {
          "1": {
              "id": 1,
              "score": 150,
              "fields": {
                  "core": {
                      "companyemail": {
                          "id": "31",
                          "label": "Company Email",
                          "alias": "companyemail",
                          "type": "email",
                          "group": "core",
                          "object": "company",
                          "is_fixed": "1",
                          "properties": "a:0:{}",
                          "default_value": null,
                          "value": "info@acme.com",
                          "normalizedValue": "info@acme.com"
                      },
                      "companyaddress1": {
                          "id": "29",
                          "label": "Address 1",
                          "alias": "companyaddress1",
                          "type": "text",
                          "group": "core",
                          "object": "company",
                          "is_fixed": "1",
                          "properties": "a:0:{}",
                          "default_value": null,
                          "value": "123 Main St",
                          "normalizedValue": "123 Main St"
                      },
                      "companyaddress2": {
                          "id": "30",
                          "label": "Address 2",
                          "alias": "companyaddress2",
                          "type": "text",
                          "group": "core",
                          "object": "company",
                          "is_fixed": "1",
                          "properties": "a:0:{}",
                          "default_value": null,
                          "value": "Suite 100",
                          "normalizedValue": "Suite 100"
                      },
                      "companyphone": {
                          "id": "32",
                          "label": "Phone",
                          "alias": "companyphone",
                          "type": "tel",
                          "group": "core",
                          "object": "company",
                          "is_fixed": "1",
                          "properties": "a:0:{}",
                          "default_value": null,
                          "value": "+1-555-123-4567",
                          "normalizedValue": "+1-555-123-4567"
                      },
                      "companycity": {
                          "id": "33",
                          "label": "City",
                          "alias": "companycity",
                          "type": "text",
                          "group": "core",
                          "object": "company",
                          "is_fixed": "1",
                          "properties": "a:0:{}",
                          "default_value": null,
                          "value": "Anytown",
                          "normalizedValue": "Anytown"
                      },
                      "companystate": {
                          "id": "34",
                          "label": "State",
                          "alias": "companystate",
                          "type": "region",
                          "group": "core",
                          "object": "company",
                          "is_fixed": "1",
                          "properties": "a:0:{}",
                          "default_value": null,
                          "value": "New York",
                          "normalizedValue": "New York"
                      },
                      "companyzipcode": {
                          "id": "35",
                          "label": "Zip Code",
                          "alias": "companyzipcode",
                          "type": "text",
                          "group": "core",
                          "object": "company",
                          "is_fixed": "1",
                          "properties": "a:0:{}",
                          "default_value": null,
                          "value": "12345",
                          "normalizedValue": "12345"
                      },
                      "companycountry": {
                          "id": "36",
                          "label": "Country",
                          "alias": "companycountry",
                          "type": "country",
                          "group": "core",
                          "object": "company",
                          "is_fixed": "1",
                          "properties": "a:0:{}",
                          "default_value": null,
                          "value": "United States",
                          "normalizedValue": "United States"
                      },
                      "companyname": {
                          "id": "37",
                          "label": "Company Name",
                          "alias": "companyname",
                          "type": "text",
                          "group": "core",
                          "object": "company",
                          "is_fixed": "1",
                          "properties": "a:0:{}",
                          "default_value": null,
                          "value": "Acme Corporation",
                          "normalizedValue": "Acme Corporation"
                      },
                      "companywebsite": {
                          "id": "38",
                          "label": "Website",
                          "alias": "companywebsite",
                          "type": "url",
                          "group": "core",
                          "object": "company",
                          "is_fixed": "1",
                          "properties": "a:0:{}",
                          "default_value": null,
                          "value": "https://acme.com",
                          "normalizedValue": "https://acme.com"
                      }
                  },
                  "professional": {
                      "companyindustry": {
                          "id": "42",
                          "label": "Industry",
                          "alias": "companyindustry",
                          "type": "select",
                          "group": "professional",
                          "object": "company",
                          "is_fixed": "1",
                          "properties": "a:1:{s:4:\"list\";a:41:{i:0;a:2:{s:5:\"label\";s:19:\"Aerospace & Defense\";s:5:\"value\";s:19:\"Aerospace & Defense\";}i:1;a:2:{s:5:\"label\";s:11:\"Agriculture\";s:5:\"value\";s:11:\"Agriculture\";}i:2;a:2:{s:5:\"label\";s:7:\"Apparel\";s:5:\"value\";s:7:\"Apparel\";}i:3;a:2:{s:5:\"label\";s:21:\"Automotive & Assembly\";s:5:\"value\";s:21:\"Automotive & Assembly\";}i:4;a:2:{s:5:\"label\";s:7:\"Banking\";s:5:\"value\";s:7:\"Banking\";}i:5;a:2:{s:5:\"label\";s:13:\"Biotechnology\";s:5:\"value\";s:13:\"Biotechnology\";}i:6;a:2:{s:5:\"label\";s:9:\"Chemicals\";s:5:\"value\";s:9:\"Chemicals\";}i:7;a:2:{s:5:\"label\";s:14:\"Communications\";s:5:\"value\";s:14:\"Communications\";}i:8;a:2:{s:5:\"label\";s:12:\"Construction\";s:5:\"value\";s:12:\"Construction\";}i:9;a:2:{s:5:\"label\";s:23:\"Consumer Packaged Goods\";s:5:\"value\";s:23:\"Consumer Packaged Goods\";}i:10;a:2:{s:5:\"label\";s:9:\"Education\";s:5:\"value\";s:9:\"Education\";}i:11;a:2:{s:5:\"label\";s:11:\"Electronics\";s:5:\"value\";s:11:\"Electronics\";}i:12;a:2:{s:5:\"label\";s:6:\"Energy\";s:5:\"value\";s:6:\"Energy\";}i:13;a:2:{s:5:\"label\";s:11:\"Engineering\";s:5:\"value\";s:11:\"Engineering\";}i:14;a:2:{s:5:\"label\";s:13:\"Entertainment\";s:5:\"value\";s:13:\"Entertainment\";}i:15;a:2:{s:5:\"label\";s:13:\"Environmental\";s:5:\"value\";s:13:\"Environmental\";}i:16;a:2:{s:5:\"label\";s:7:\"Finance\";s:5:\"value\";s:7:\"Finance\";}i:17;a:2:{s:5:\"label\";s:15:\"Food & Beverage\";s:5:\"value\";s:15:\"Food & Beverage\";}i:18;a:2:{s:5:\"label\";s:10:\"Government\";s:5:\"value\";s:10:\"Government\";}i:19;a:2:{s:5:\"label\";s:10:\"Healthcare\";s:5:\"value\";s:10:\"Healthcare\";}i:20;a:2:{s:5:\"label\";s:11:\"Hospitality\";s:5:\"value\";s:11:\"Hospitality\";}i:21;a:2:{s:5:\"label\";s:9:\"Insurance\";s:5:\"value\";s:9:\"Insurance\";}i:22;a:2:{s:5:\"label\";s:9:\"Machinery\";s:5:\"value\";s:9:\"Machinery\";}i:23;a:2:{s:5:\"label\";s:13:\"Manufacturing\";s:5:\"value\";s:13:\"Manufacturing\";}i:24;a:2:{s:5:\"label\";s:5:\"Media\";s:5:\"value\";s:5:\"Media\";}i:25;a:2:{s:5:\"label\";s:15:\"Metals & Mining\";s:5:\"value\";s:15:\"Metals & Mining\";}i:26;a:2:{s:5:\"label\";s:14:\"Not for Profit\";s:5:\"value\";s:14:\"Not for Profit\";}i:27;a:2:{s:5:\"label\";s:9:\"Oil & Gas\";s:5:\"value\";s:9:\"Oil & Gas\";}i:28;a:2:{s:5:\"label\";s:17:\"Packaging & Paper\";s:5:\"value\";s:17:\"Packaging & Paper\";}i:29;a:2:{s:5:\"label\";s:36:\"Private Equity & Principal Investors\";s:5:\"value\";s:36:\"Private Equity & Principal Investors\";}i:30;a:2:{s:5:\"label\";s:10:\"Recreation\";s:5:\"value\";s:10:\"Recreation\";}i:31;a:2:{s:5:\"label\";s:11:\"Real Estate\";s:5:\"value\";s:11:\"Real Estate\";}i:32;a:2:{s:5:\"label\";s:6:\"Retail\";s:5:\"value\";s:6:\"Retail\";}i:33;a:2:{s:5:\"label\";s:14:\"Semiconductors\";s:5:\"value\";s:14:\"Semiconductors\";}i:34;a:2:{s:5:\"label\";s:8:\"Shipping\";s:5:\"value\";s:8:\"Shipping\";}i:35;a:2:{s:5:\"label\";s:13:\"Social Sector\";s:5:\"value\";s:13:\"Social Sector\";}i:36;a:2:{s:5:\"label\";s:10:\"Technology\";s:5:\"value\";s:10:\"Technology\";}i:37;a:2:{s:5:\"label\";s:18:\"Telecommunications\";s:5:\"value\";s:18:\"Telecommunications\";}i:38;a:2:{s:5:\"label\";s:14:\"Transportation\";s:5:\"value\";s:14:\"Transportation\";}i:39;a:2:{s:5:\"label\";s:9:\"Utilities\";s:5:\"value\";s:9:\"Utilities\";}i:40;a:2:{s:5:\"label\";s:5:\"Other\";s:5:\"value\";s:5:\"Other\";}}}",
                          "default_value": null,
                          "value": "Technology",
                          "normalizedValue": "Technology"
                      },
                      "companydescription": {
                          "id": "43",
                          "label": "Description",
                          "alias": "companydescription",
                          "type": "text",
                          "group": "professional",
                          "object": "company",
                          "is_fixed": "1",
                          "properties": "a:0:{}",
                          "default_value": null,
                          "value": "Leading software company",
                          "normalizedValue": "Leading software company"
                      },
                      "companynumber_of_employees": {
                          "id": "39",
                          "label": "Number of Employees",
                          "alias": "companynumber_of_employees",
                          "type": "number",
                          "group": "professional",
                          "object": "company",
                          "is_fixed": "0",
                          "properties": "a:2:{s:9:\"roundmode\";i:4;s:5:\"scale\";i:0;}",
                          "default_value": null,
                          "value": 300,
                          "normalizedValue": 300
                      },
                      "companyfax": {
                          "id": "40",
                          "label": "Fax",
                          "alias": "companyfax",
                          "type": "tel",
                          "group": "professional",
                          "object": "company",
                          "is_fixed": "0",
                          "properties": "a:0:{}",
                          "default_value": null,
                          "value": "+1-555-123-7890",
                          "normalizedValue": "+1-555-123-7890"
                      },
                      "companyannual_revenue": {
                          "id": "41",
                          "label": "Annual Revenue",
                          "alias": "companyannual_revenue",
                          "type": "number",
                          "group": "professional",
                          "object": "company",
                          "is_fixed": "0",
                          "properties": "a:2:{s:9:\"roundmode\";i:4;s:5:\"scale\";i:2;}",
                          "default_value": null,
                          "value": 1000000.0,
                          "normalizedValue": 1000000.0
                      }
                  },
                  "other": [],
                  "all": {
                      "id": 1,
                      "companyemail": "info@acme.com",
                      "companyaddress1": "123 Main St",
                      "companyaddress2": "Suite 100",
                      "companyphone": "+1-555-123-4567",
                      "companycity": "Anytown",
                      "companystate": "New York",
                      "companyzipcode": "12345",
                      "companycountry": "United States",
                      "companyname": "Acme Corporation",
                      "companywebsite": "https://acme.com",
                      "companyindustry": "Technology",
                      "companydescription": "Leading software company",
                      "companynumber_of_employees": 300,
                      "companyfax": "+1-555-123-7890",
                      "companyannual_revenue": 1000000.0
                  }
              }
          },
          // ...
      }
   }

Properties
----------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``total``
     - string
     - Total count of Companies
   * - ``companies``
     - object
     - A mapped collection of Companies indexed by their ID

.. vale off

For the rest of the properties, refer to :ref:`Company properties <get Company properties>`.

.. vale on

.. vale off

Create Company
**************

.. vale on

Creates a new Company.

.. code-block:: php

   <?php

   $data = array(
       'companyname'                => 'Acme Corporation', // Required
       'companyemail'               => 'info@acme.com',
       'companywebsite'             => 'https://acme.com',
       'score'                      => 10,
       'companynumber_of_employees' => 50,
       'companyannual_revenue'      => 1000000.0,
   );

   $company = $companyApi->create($data);

.. vale off

HTTP request
============

.. vale on

``POST /companies/new``

.. _create Company POST parameters:

POST parameters
---------------

.. list-table::
   :widths: 30 20 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``companyname``
     - string
     - **Required.**
     
       Company name
   * - ``companyemail``
     - string
     - Company Email address
   * - ``companyphone``
     - string
     - Company phone number
   * - ``companywebsite``
     - string
     - Company website URL
   * - ``companyaddress1``
     - string
     - Company primary address line - such as street name and number
   * - ``companyaddress2``
     - string
     - Supplemental Company address details - such as suite, unit, building, or floor
   * - ``companycity``
     - string
     - Company city name
   * - ``companystate``
     - string
     - Company state, province, or region
   * - ``companyzipcode``
     - string
     - Company zip or postal code
   * - ``companycountry``
     - string
     - Company country name
   * - ``companynumber_of_employees``
     - integer
     - Total number of employees in the Company
   * - ``companyfax``
     - string
     - Company fax number
   * - ``companyannual_revenue``
     - number
     - Annual revenue of the Company - for example, ``1000000.0``
   * - ``companyindustry``
     - string
     - Company business sector or vertical
   * - ``companydescription``
     - string
     - Summary of the Company
   * - ``score``
     - integer
     - Score assigned to the Company

Response
========

* Returns ``201 Created`` when the request successfully creates a Company.

The response is a JSON object similar to :ref:`Get Company <get Company response>`.

Properties
----------

Refer to :ref:`Company properties <get Company properties>`.

.. vale off

Edit Company
************

.. vale on

Edits a Company. 

This operation supports ``PUT`` or ``PATCH`` depending on the desired behavior:

* ``PUT``: **full replacement**. The request creates a new Company if the ID is missing. If the ID exists, the request clears all existing data and replaces it with the provided values.
* ``PATCH``: **partial update**. The request only updates field values based on the request data. The request fails when the Company ID doesn't exist.

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'companyname' => 'Updated Company Name',
       'companyemail' => 'updated@acme.com',
   );

   // Create a new Company if ID 1 isn't found
   $createIfNotFound = true;

   $company = $companyApi->edit($id, $data, $createIfNotFound);

.. vale off

HTTP request
============

.. vale on

* ``PUT /companies/ID/edit``: updates an existing Company or creates a new one when the ID doesn't exist.
* ``PATCH /companies/ID/edit``: updates an existing Company. The request fails when the ID doesn't exist.

POST parameters
---------------

Accepts the same parameters as those described in :ref:`Create Company <create Company POST parameters>`. All parameters are optional.

Response
========

* ``PUT``: returns ``200 OK`` when the request successfully updates the Company or ``201 Created`` when the request creates a Company.
* ``PATCH``: returns ``200 OK`` when the request successfully updates the Company or ``404 Not Found`` error when the Company ID doesn't exist.

The response is a JSON object similar to :ref:`Get Company <get Company response>`.

Properties
----------

Refer to :ref:`Company properties <get Company properties>`.

.. vale off

Delete Company
**************

.. vale on

Deletes a Company.

.. code-block:: php

   <?php

   $company = $companyApi->delete($id);

.. vale off

HTTP request
============

.. vale on

``DELETE /companies/ID/delete``

Response
========

* Returns ``200 OK`` when the request successfully deletes the Company.

The response is a JSON object containing the data of the deleted Company, similar to :ref:`Get Company <get Company response>`.

Properties
----------

Refer to :ref:`Company properties <get Company properties>`.

.. vale off

Add Contact to Company
**********************

.. vale on

Adds a Contact to a Company.

.. code-block:: php

   <?php

   $companyApi->addContact($companyId, $contactId);

.. vale off

HTTP request
============

.. vale on

``POST /companies/COMPANY_ID/contact/CONTACT_ID/add``

Response
========

* Returns ``200 OK`` when the request successfully adds the Contact to the Company.

.. code-block:: json

   {
       "success": 1
   }

.. vale off

Remove Contact from Company
***************************

.. vale on

Removes a Contact from a Company.

.. code-block:: php

   <?php

   $companyApi->removeContact($companyId, $contactId);

.. vale off

HTTP request
============

.. vale on

``POST /companies/COMPANY_ID/contact/CONTACT_ID/remove``

Response
========

* Returns ``200 OK`` when the request successfully removes the Contact from the Company.

.. code-block:: json

   {
       "success": 1
   }
