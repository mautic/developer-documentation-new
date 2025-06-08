Companies
#########

Use this endpoint to manipulate and obtain details on Mautic's Companies.

**Using Mautic's API Library**

You can interact with this API through the :xref:`Mautic API Library` as follows, or use the various http endpoints as described in this document.

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

.. code-block:: php

   <?php

   //...
   $company = $companyApi->get($id);

Get an individual Company by ID.

.. vale off

**HTTP Request**

.. vale on

``GET /companies/ID``

**Response**

``Expected Response Code: 200``

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

**Company Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - id
     - int
     - ID of the company
   * - isPublished
     - bool
     - Published state
   * - dateAdded
     - datetime
     - Date/time company was created
   * - dateModified
     - datetime
     - Date/time company was last modified
   * - createdBy
     - int
     - ID of the user that created the company
   * - createdByUser
     - string
     - Name of the user that created the company
   * - modifiedBy
     - int
     - ID of the user that last modified the company
   * - modifiedByUser
     - string
     - Name of the user that last modified the company
   * - fields
     - array
     - Custom fields and values for the company
   * - score
     - int
     - Company score
   * - owner
     - object
     - User object for the company owner

**Company Field Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - companyname
     - string
     - Company name
   * - companyemail
     - string
     - Company email address
   * - companyaddress1
     - string
     - Company address line 1
   * - companyaddress2
     - string
     - Company address line 2
   * - companycity
     - string
     - Company city
   * - companystate
     - string
     - Company state/province
   * - companyzipcode
     - string
     - Company zip/postal code
   * - companycountry
     - string
     - Company country
   * - companyphone
     - string
     - Company phone number
   * - companywebsite
     - string
     - Company website URL
   * - companyindustry
     - string
     - Company industry
   * - companydescription
     - string
     - Company description

.. vale off

List Companies
**************

.. vale on

.. code-block:: php

   <?php

   //...
   $companies = $companyApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. note::

   The ``$companies`` array will be an array of individual Company arrays like the above example.

**HTTP Request**

``GET /companies``

**Query Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - search
     - String or search command to filter entities by.
   * - start
     - Starting row for the entities returned. Defaults to 0.
   * - limit
     - Limit number of entities to return. Defaults to the system configuration for pagination (30).
   * - orderBy
     - Column to sort by. Can use any column listed in the response.
   * - orderByDir
     - Sort direction: asc or desc.
   * - publishedOnly
     - Only return currently published entities.
   * - minimal
     - Return only array of entities without additional lists in it.

**Response**

``Expected Response Code: 200``

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

.. vale off

Create Company
**************

.. vale on

.. code-block:: php

   <?php

   $data = array(
       'companyname' => 'Acme Corporation',
       'companyemail' => 'info@acme.com',
       'companywebsite' => 'https://acme.com',
   );

   $company = $companyApi->create($data);

Create a new Company.

**HTTP Request**

``POST /companies/new``

**Post Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - companyname
     - string
     - Company name (required)
   * - companyemail
     - string
     - Company email address
   * - companyaddress1
     - string
     - Company address line 1
   * - companyaddress2
     - string
     - Company address line 2
   * - companycity
     - string
     - Company city
   * - companystate
     - string
     - Company state/province
   * - companyzipcode
     - string
     - Company zip/postal code
   * - companycountry
     - string
     - Company country
   * - companyphone
     - string
     - Company phone number
   * - companywebsite
     - string
     - Company website URL
   * - companyindustry
     - string
     - Company industry
   * - companydescription
     - string
     - Company description
   * - isPublished
     - boolean
     - Published state (default: 1)
   * - owner
     - int
     - ID of a Mautic user to assign this company to

**Response**

``Expected Response Code: 201``

**Properties**

Same as `Get Company`_.

.. vale off

Edit Company
************

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'companyname' => 'Updated Company Name',
       'companyemail' => 'updated@acme.com',
   );

   // Create new a company of ID 1 is not found?
   $createIfNotFound = true;

   $company = $companyApi->edit($id, $data, $createIfNotFound);

Edit a new Company. Note that this supports PUT or PATCH depending on the desired behavior.

**PUT** creates a Company if the given ID does not exist and clears all the Company information, adds the information from the request.
**PATCH** fails if the Company with the given ID does not exist and updates the Company field values with the values from the request.

**HTTP Request**

To edit a Company and return a 404 if the Company is not found:

``PATCH /companies/ID/edit``

To edit a Company and create a new one if the Company is not found:

``PUT /companies/ID/edit``

**Post Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - companyname
     - string
     - Company name
   * - companyemail
     - string
     - Company email address
   * - companyaddress1
     - string
     - Company address line 1
   * - companyaddress2
     - string
     - Company address line 2
   * - companycity
     - string
     - Company city
   * - companystate
     - string
     - Company state/province
   * - companyzipcode
     - string
     - Company zip/postal code
   * - companycountry
     - string
     - Company country
   * - companyphone
     - string
     - Company phone number
   * - companywebsite
     - string
     - Company website URL
   * - companyindustry
     - string
     - Company industry
   * - companydescription
     - string
     - Company description
   * - isPublished
     - boolean
     - Published state
   * - owner
     - int
     - ID of a Mautic user to assign this company to

**Response**

If ``PUT``: ``Expected Response Code: 200`` or ``201`` if created

If ``PATCH``: ``Expected Response Code: 200``

**Properties**

Same as `Get Company`_.

.. vale off

Delete Company
**************

.. vale on

.. code-block:: php

   <?php

   $company = $companyApi->delete($id);

Delete a Company.

**HTTP Request**

``DELETE /companies/ID/delete``

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get Company`_.

.. vale off

Batch Create Companies
**********************

.. vale on

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

Create multiple Companies in a single request.

.. note::

   If an existing company is found with the same unique identifier fields (as configured in Mautic), the existing company will be updated instead of creating a new one.

**HTTP Request**

``POST /companies/batch/new``

**Post Parameters**

An array of Company arrays. Each Company array should contain the same fields as described in `Create Company`_.

**Response**

``Expected Response Code: 201``

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

.. vale off

Batch Edit Companies
********************

.. vale on

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

Edit multiple Companies in a single request. Each Company in the array must include an ``id`` field.

**HTTP Request**

``PATCH /companies/batch/edit``

**Post Parameters**

An array of Company arrays. Each Company array should contain an ``id`` field and the fields to update as described in `Edit Company`_.

**Response**

``Expected Response Code: 200``

**Properties**

Similar to `Batch Create Companies`_ but with ``statusCodes`` indicating whether each company was successfully updated (200) or if there was an error.

.. vale off

Batch Delete Companies
**********************

.. vale on

.. code-block:: php

   <?php

   $ids = array(1, 2, 3);
   $companies = $companyApi->deleteBatch($ids);

Delete multiple Companies in a single request.

**HTTP Request**

``DELETE /companies/batch/delete?ids=1,2,3``

**Query Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - ids
     - Comma-separated list of Company IDs to delete

**Response**

``Expected Response Code: 200``

**Properties**

Similar to `Batch Create Companies`_ but with the companies that were deleted.

.. vale off

Add Contact to Company
**********************

.. vale on

.. code-block:: php

   <?php

   $companyApi->addContact($companyId, $contactId);

Add a Contact to a Company.

**HTTP Request**

``POST /companies/COMPANY_ID/contact/CONTACT_ID/add``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "success": 1
   }

.. vale off

Remove Contact from Company
***************************

.. vale on

.. code-block:: php

   <?php

   $companyApi->removeContact($companyId, $contactId);

Remove a Contact from a Company.

**HTTP Request**

``POST /companies/COMPANY_ID/contact/CONTACT_ID/remove``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "success": 1
   }