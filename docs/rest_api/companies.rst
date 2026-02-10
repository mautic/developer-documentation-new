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

* Returns ``200`` when the request successfully retrieves the Company.

.. _get Company response:

.. code-block:: json

   {
       "company": {
           "isPublished": true,
           "dateAdded": "2017-02-03T16:51:06+00:00",
           "dateModified": "2017-02-03T19:11:54+00:00",
           "createdBy": 1,
           "createdByUser": "John Doe",
           "modifiedBy": 1,
           "modifiedByUser": "John Doe",
           "id": 1,
           "fields": {
               "all": {
                   "companyname": "Acme Corporation",
                   "companyemail": "info@acme.com",
                   "companyaddress1": "123 Main St",
                   "companyaddress2": "Suite 100",
                   "companycity": "Anytown",
                   "companystate": "NY",
                   "companyzipcode": "12345",
                   "companycountry": "United States",
                   "companyphone": "+1-555-123-4567",
                   "companywebsite": "https://acme.com",
                   "companyindustry": "Technology",
                   "companydescription": "Leading software company"
               }
           },
           "score": 150,
           "owner": {
               "id": 1,
               "username": "admin",
               "firstName": "John",
               "lastName": "Doe"
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
     - int
     - ID of the Company
   * - ``isPublished``
     - boolean
     - Company publication status - set to ``1`` or ``true`` to publish
   * - ``dateAdded``
     - datetime
     - Company record creation date and time
   * - ``dateModified``
     - datetime
     - Company record last modification date and time
   * - ``createdBy``
     - int
     - ID of the User who created the Company
   * - ``createdByUser``
     - string
     - Name of the User who created the Company
   * - ``modifiedBy``
     - int
     - ID of the User who last modified the Company
   * - ``modifiedByUser``
     - string
     - Name of the User who last modified the Company
   * - ``fields``
     - array
     - Custom :ref:`fields <get Company field properties>` and values for the Company
   * - ``score``
     - int
     - Company score
   * - ``owner``
     - object
     - Object for the Mautic User who assigns this Company to

.. _get Company field properties:

Company field properties
------------------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``companyname``
     - string
     - Company name
   * - ``companyemail``
     - string
     - Company Email address
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
   * - ``companyphone``
     - string
     - Company phone number
   * - ``companywebsite``
     - string
     - Company website URL
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

.. note::

   The ``$companies`` array contains individual Company arrays.

.. vale off

HTTP request
============

.. vale on

``GET /companies``

Query parameters
----------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Name
     - Description
   * - ``searchFilter``
     - String or search command to filter entities
   * - ``start``
     - Starting row for the returned entities - defaults to 0
   * - ``limit``
     - Maximum number of entities to return - defaults to 30
   * - ``orderBy``
     - Column to sort by. Any column in the response is valid
   * - ``orderByDir``
     - Sort direction - ``asc`` or ``desc``
   * - ``publishedOnly``
     - Returns only currently published entities
   * - ``minimal``
     - Returns only a simple array of entities without additional lists in it

Response
========

* Returns ``200`` when the request successfully retrieves the Companies list.

.. code-block:: json

   {
       "total": 25,
       "companies": [
           {
               "isPublished": true,
               "dateAdded": "2017-02-03T16:51:06+00:00",
               "dateModified": "2017-02-03T19:11:54+00:00",
               "createdBy": 1,
               "createdByUser": "John Doe",
               "modifiedBy": 1,
               "modifiedByUser": "John Doe",
               "id": 1,
               "fields": {
                   "all": {
                       "companyname": "Acme Corporation",
                       "companyemail": "info@acme.com"
                   }
               },
               "score": 150
           }
       ]
   }

Properties
----------

Refer to :ref:`Company properties <get Company properties>`.

.. vale off

Create Company
**************

.. vale on

Creates a new Company.

.. code-block:: php

   <?php

   $data = array(
       'companyname' => 'Acme Corporation',
       'companyemail' => 'info@acme.com',
       'companywebsite' => 'https://acme.com',
   );

   $company = $companyApi->create($data);

.. vale off

HTTP request
============

.. vale on

``POST /companies/new``

POST parameters
---------------

A Company array. The array contains the same fields as described in the :ref:`Company field properties <get Company field properties>`.

Response
========

* Returns ``201`` when the request successfully creates a Company.

Response is the same as :ref:`Get Company <get Company response>`.

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
* ``PATCH``: **partial update**. The request only updates field values based on the request data. The request fails when the ID doesn't exist.

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'companyname' => 'Updated Company Name',
       'companyemail' => 'updated@acme.com',
   );

   // Create a new company if ID 1 is not found?
   $createIfNotFound = true;

   $company = $companyApi->edit($id, $data, $createIfNotFound);

.. vale off

HTTP request
============

.. vale on

* ``PUT /companies/ID/edit``: updates an existing Company or creates a new one when the ID doesn't exist.
* ``PATCH /companies/ID/edit``: updates an existing Company. The request fails with a ``404`` error when the ID doesn't exist.

POST parameters
---------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Company
   * - ``array``
     - array
     - Company array. The array contains the same fields as described in the :ref:`Company field properties <get Company field properties>`.

Response
========

* ``PUT``: returns ``200`` when the request successfully updates the Company or ``201`` when the request creates a Company.
* ``PATCH``: returns ``200`` when the request successfully updates the Company.

Response is the same as :ref:`Get Company <get Company response>`.

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

* Returns ``200`` when the request successfully deletes the Company.

Response is similar to :ref:`Get Company <get Company response>`, but with the deleted Company.

Properties
----------

Refer to :ref:`Company properties <get Company properties>`. 

.. _batch create Companies:

.. vale off

Batch create Companies
**********************

.. vale on

Creates multiple Companies in a single request.

.. code-block:: php

   <?php

   $data = array(
       array(
           'companyname' => 'Acme Corporation',
           'companyemail' => 'info@acme.com',
       ),
       array(
           'companyname' => 'Beta LLC',
           'companyemail' => 'info@beta.com',
       ),
   );

   $companies = $companyApi->createBatch($data);

.. note::

   If there's an existing Company with the same unique identifier fields as configured in Mautic, the system updates the existing Company instead of creating a new one.

.. vale off

HTTP request
============

.. vale on

``POST /companies/batch/new``

POST parameters
---------------

An array of Company arrays. Each Company array contains the same fields as described in the :ref:`Company field properties <get Company field properties>`.

.. _batch create Companies response:

Response
========

* Returns ``201`` when the request successfully creates new Companies.

.. code-block:: json

   {
       "statusCodes": [201, 201],
       "companies": [
           {
               "isPublished": true,
               "dateAdded": "2017-02-03T16:51:06+00:00",
               "dateModified": "2017-02-03T19:11:54+00:00",
               "createdBy": 1,
               "createdByUser": "John Doe",
               "modifiedBy": 1,
               "modifiedByUser": "John Doe",
               "id": 1,
               "fields": {
                   "all": {
                       "companyname": "Acme Corporation",
                       "companyemail": "info@acme.com"
                   }
               },
               "score": 0
           },
           {
               "isPublished": true,
               "dateAdded": "2017-02-03T16:51:06+00:00",
               "dateModified": "2017-02-03T19:11:54+00:00",
               "createdBy": 1,
               "createdByUser": "John Doe",
               "modifiedBy": 1,
               "modifiedByUser": "John Doe",
               "id": 2,
               "fields": {
                   "all": {
                       "companyname": "Beta LLC",
                       "companyemail": "info@beta.com"
                   }
               },
               "score": 0
           }
       ]
   }

Properties
----------

Refer to :ref:`Company properties <get Company properties>`.

.. vale off

Batch edit Companies
********************

.. vale on

Edits multiple Companies in a single request.

.. code-block:: php

   <?php

   $data = array(
       array(
           'id' => 1,
           'companyname' => 'Updated Acme Corporation',
       ),
       array(
           'id' => 2,
           'companyname' => 'Updated Beta LLC',
       ),
   );

   $companies = $companyApi->editBatch($data);

.. note::

   Each Company in the array must include an ``id`` field.

.. vale off

HTTP request
============

.. vale on

``PATCH /companies/batch/edit``

POST parameters
---------------

An array of Company arrays. Each Company array should contain an ``id`` field and the fields to update as described in the :ref:`Company field properties <get Company field properties>`.

Response
========

* Returns ``200`` when the request successfully updates the Companies.
* Returns an error when the request fails to update a Company in the batch.

Response is similar to :ref:`batch create Companies <batch create Companies response>`.

Properties
----------

Refer to :ref:`Company properties <get Company properties>`.

.. vale off

Batch delete Companies
**********************

.. vale on

Deletes multiple Companies in a single request.

.. code-block:: php

   <?php

   $ids = array(1, 2, 3);
   $companies = $companyApi->deleteBatch($ids);

.. vale off

HTTP request
============

.. vale on

``DELETE /companies/batch/delete?ids=1,2,3``

Query parameters
----------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Name
     - Description
   * - ``ids``
     - Comma-separated list of Company IDs to delete

Response
========

* Returns ``200`` when the request successfully deletes the Companies.

Response is similar to :ref:`batch create Companies <batch create Companies response>`, but with the deleted Companies.

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

* Returns ``200`` when the request successfully adds the Contact to the Company.

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

* Returns ``200`` when the request successfully removes the Contact from the Company.

.. code-block:: json

   {
       "success": 1
   }