
Companies
*********

Use this endpoint to obtain details on Mautic's Companies or to manipulate Contact-Company memberships.

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
       "company":{  
           "isPublished":true,
           "dateAdded":"2016-10-25T09:46:36+00:00",
           "createdBy":1,
           "createdByUser":"John Doe",
           "dateModified":null,
           "modifiedBy":null,
           "modifiedByUser":null,
           "id":176,
           "fields":{  
               "core":{  
                   "companywebsite":{  
                       "id":"91",
                       "label":"Website",
                       "alias":"companywebsite",
                       "type":"url",
                       "group":"core",
                       "field_order":"8",
                       "object":"company",
                       "value":null
                   }
               },
               "professional":{  
                   "companyannual_revenue":{  
                       "id":"90",
                       "label":"Annual Revenue",
                       "alias":"companyannual_revenue",
                       "type":"number",
                       "group":"professional",
                       "field_order":"10",
                       "object":"company",
                       "value":null
                   }
               },
               "other":[],
               "all":{  
                   "companywebsite":null,
                   "companycountry":null,
                   "companyzipcode":null,
                   "companystate":null,
                   "companycity":"Raleigh",
                   "companyphone":null,
                   "companyemail":"test@company.com",
                   "companyaddress2":null,
                   "companyaddress1":null,
                   "companyname":"test",
                   "companyannual_revenue":null,
                   "companyfax":null,
                   "companynumber_of_employees":null,
                   "companydescription":null
               }
           }
       }
   }

**Company Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Company
   * - ``isPublished``
     - boolean
     - Published state
   * - ``dateAdded``
     - ``datetime``
     - Company creation date/time
   * - ``createdBy``
     - int
     - ID of the User that created the Company
   * - ``createdByUser``
     - string
     - Name of the User that created the Company
   * - ``dateModified``
     - datetime/null
     - Date/time Company was last modified
   * - ``modifiedBy``
     - int
     - ID of the User that last modified the Company
   * - ``modifiedByUser``
     - string
     - Name of the User that last modified the Company
   * - ``fields``
     - array
     - Custom fields for the Company

.. vale off

List Contact Companies
**********************

.. vale on

.. code-block:: php

   <?php

   //...
   $companies = $companyApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

Returns a list of Contact Companies available to the User. This list isn't filterable.

.. vale off

**HTTP Request**

.. vale on

``GET /companies``

**Query Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - ``search``
     - String or search command to filter entities by.
   * - ``start``
     - Starting row for the entities returned. Defaults to 0.
   * - ``limit``
     - Limit number of entities to return. Defaults to the system configuration for pagination - defaults to 30.
   * - ``orderBy``
     - Column to sort by. Can use any column listed in the response.
   * - ``orderByDir``
     - Sort direction: ``asc`` or ``desc``.


**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
     "total": 13,
     "companies": {
       "176": {  
         "isPublished":true,
         "dateAdded":"2016-10-25T09:46:36+00:00",
         "createdBy":1,
         "createdByUser":"John Doe",
         "dateModified":null,
         "modifiedBy":null,
         "modifiedByUser":null,
         "id":176,
         "fields":{  
           "core":{  
               "companywebsite":{  
                   "id":"91",
                   "label":"Website",
                   "alias":"companywebsite",
                   "type":"url",
                   "group":"core",
                   "field_order":"8",
                   "object":"company",
                   "value":null
               }
           },
           "professional":{  
               "companyannual_revenue":{  
                   "id":"90",
                   "label":"Annual Revenue",
                   "alias":"companyannual_revenue",
                   "type":"number",
                   "group":"professional",
                   "field_order":"10",
                   "object":"company",
                   "value":null
               }
           },
           "other":[],
           "all":{  
               "companywebsite":null,
               "companycountry":null,
               "companyzipcode":null,
               "companystate":null,
               "companycity":"Raleigh",
               "companyphone":null,
               "companyemail":"test@company.com",
               "companyaddress2":null,
               "companyaddress1":null,
               "companyname":"test",
               "companyannual_revenue":null,
               "companyfax":null,
               "companynumber_of_employees":null,
               "companydescription":null
           }
       }
     }
   }

**Company Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Company
   * - ``isPublished``
     - boolean
     - Published state
   * - ``dateAdded``
     - ``datetime``
     - Company creation date/time
   * - ``createdBy``
     - int
     - ID of the User that created the Company
   * - ``createdByUser``
     - string
     - Name of the User that created the Company
   * - ``dateModified``
     - datetime/null
     - Date/time Company was last modified
   * - ``modifiedBy``
     - int
     - ID of the User that last modified the Company
   * - ``modifiedByUser``
     - string
     - Name of the User that last modified the Company
   * - ``fields``
     - array
     - Custom fields for the Company

.. vale off

Create Company
**************

.. vale of

.. code-block:: php

   <?php

   $data = array(
       'companyname' => 'test',
       'companyemail' => 'test@company.com',
       'companycity' => 'Raleigh',
       'overwriteWithBlank' => true
   );

   $company = $companyApi->create($data);

Create a new Company.

.. vale off

**HTTP Request**

.. vale on

``POST /companies/new``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - ``companyname``
     - Company name is the only required field. Other Company fields are optional
   * - ``isPublished``
     - A value of 0 or 1
   * - ``overwriteWithBlank``
     - If true, then fields get filled with empty values. Otherwise empty values get skipped

**Response**

``Expected Response Code: 201``

**Properties**

Same as `Get Company <#get-company>`_.

.. vale off

Edit Company
************

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'companyname' => 'test',
       'companyemail' => 'test@company.com',
       'companycity' => 'Raleigh',
   );

   // Create new a Company of ID 1 isn't found?
   $createIfNotFound = true;

   $company = $companyApi->edit($id, $data, $createIfNotFound);

Edit a new Company. Note that this supports PUT or PATCH depending on the desired behavior.

**PUT** creates a Company if the given ID doesn't exist and clears all the Company information, adds the information from the request.
**PATCH** fails if the Company with the given ID doesn't exist and updates the Company field values with the values from the request.

.. vale off

**HTTP Request**

.. vale on

To edit a Company and return a 404 if the Company isn't found:

``PATCH /companies/ID/edit``

To edit a Company and create a new one if the Company isn't found:

``PUT /companies/ID/edit``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - ``companyname``
     - Company name is the only required field. Other Company fields are optional
   * - ``isPublished``
     - A value of 0 or 1
   * - ``overwriteWithBlank``
     - If true, then fields get filled with empty values. Otherwise empty values get skipped


**Response**

If ``PUT``, the expected response code is ``200`` when editing the Company or ``201`` when creating a new one.
If ``PATCH``, the expected response code is ``200``.

**Properties**

Same as `Get Company <#get-company>`_.

.. vale off

Delete Company
**************

.. vale on

.. code-block:: php

   <?php

   $company = $companyApi->delete($id);

Delete a Company.

.. vale off

**HTTP Request**

.. vale on

``DELETE /companies/ID/delete``

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get Company <#get-company>`_.

.. vale off

Add Contact to a Company
************************

.. vale on

.. code-block:: php

   <?php

   //...
   $response = $companyApi->addContact($companyId, $contactId);
   if (!isset($response['success'])) {
       // handle error
   }

Manually add a Contact to a specific Company.

.. vale off

**HTTP Request**

.. vale on

``POST /companies/COMPANY_ID/contact/CONTACT_ID/add``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "success": true
   }

.. vale off

Remove Contact from a Company
*****************************

.. vale on

.. code-block:: php

   <?php

   //...
   $response = $companyApi->removeContact($contactId, $companyId);
   if (empty($response['success'])) {
       // handle error
   }

Manually remove a Contact to a specific Company.

.. vale off

**HTTP Request**

.. vale on

``POST /companies/COMPANY_ID/contact/CONTACT_ID/remove``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "success": true
   }
