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
           "dateAdded": "2024-08-15T10:30:00+00:00",
           "createdBy": 1,
           "createdByUser": "Joe Smith",
           "dateModified": "2024-08-20T14:22:00+00:00",
           "modifiedBy": 1,
           "modifiedByUser": "Joe Smith",
           "id": 42,
           "fields": {
               "core": {
                   "companyname": {
                       "id": "1",
                       "label": "Company Name",
                       "alias": "companyname",
                       "type": "text",
                       "group": "core",
                       "value": "Acme Inc."
                   },
                   "companyemail": {
                       "id": "2",
                       "label": "Email",
                       "alias": "companyemail",
                       "type": "email",
                       "group": "core",
                       "value": "contact@acme.com"
                   },
                   "companyaddress1": {
                       "id": "3",
                       "label": "Address Line 1",
                       "alias": "companyaddress1",
                       "type": "text",
                       "group": "core",
                       "value": "123 Main Street"
                   },
                   "companycity": {
                       "id": "4",
                       "label": "City",
                       "alias": "companycity",
                       "type": "text",
                       "group": "core",
                       "value": "Boston"
                   },
                   "companystate": {
                       "id": "5",
                       "label": "State",
                       "alias": "companystate",
                       "type": "text",
                       "group": "core",
                       "value": "MA"
                   },
                   "companycountry": {
                       "id": "6",
                       "label": "Country",
                       "alias": "companycountry",
                       "type": "text",
                       "group": "core",
                       "value": "United States"
                   },
                   "companyzipcode": {
                       "id": "7",
                       "label": "Zip Code",
                       "alias": "companyzipcode",
                       "type": "text",
                       "group": "core",
                       "value": "02101"
                   },
                   "companyphone": {
                       "id": "8",
                       "label": "Phone",
                       "alias": "companyphone",
                       "type": "tel",
                       "group": "core",
                       "value": "+1 555-123-4567"
                   },
                   "companywebsite": {
                       "id": "9",
                       "label": "Website",
                       "alias": "companywebsite",
                       "type": "url",
                       "group": "core",
                       "value": "https://acme.com"
                   }
               },
               "all": {
                   "companyname": "Acme Inc.",
                   "companyemail": "contact@acme.com",
                   "companyaddress1": "123 Main Street",
                   "companycity": "Boston",
                   "companystate": "MA",
                   "companycountry": "United States",
                   "companyzipcode": "02101",
                   "companyphone": "+1 555-123-4567",
                   "companywebsite": "https://acme.com"
               }
           },
           "score": 50,
           "tags": [
               {
                   "id": 1,
                   "tag": "Enterprise"
               },
               {
                   "id": 2,
                   "tag": "VIP"
               }
           ]
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
     - ``true`` if the Company has the status of published
   * - ``dateAdded``
     - datetime
     - Date/time Company got created
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
     - Custom field values grouped by field group
   * - ``score``
     - int
     - Company's current score
   * - ``tags``
     - array
     - Array of Tag objects associated with the Company

.. vale off

List Companies
**************

.. vale on

.. code-block:: php

   <?php
   // ...

   $companies = $companyApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

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
     - String or search command to filter entities by
   * - ``start``
     - Starting row for the entities returned, defaults to 0
   * - ``limit``
     - Limit number of entities to return, defaults to the system configuration for pagination - default of 30
   * - ``orderBy``
     - Column to sort by, can use any column listed in the response
   * - ``orderByDir``
     - Sort direction: ``asc`` or ``desc``
   * - ``published``
     - Only return currently published entities
   * - ``minimal``
     - Return only array of entities without additional lists in it


**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "total": 2,
       "companies": {
           "42": {
               "isPublished": true,
               "dateAdded": "2024-08-15T10:30:00+00:00",
               "createdBy": 1,
               "createdByUser": "Joe Smith",
               "dateModified": null,
               "modifiedBy": null,
               "modifiedByUser": null,
               "id": 42,
               "fields": {
                   "all": {
                       "companyname": "Acme Inc.",
                       "companyemail": "contact@acme.com"
                   }
               },
               "score": 50,
               "tags": [
                   {
                       "id": 1,
                       "tag": "Enterprise"
                   }
               ]
           },
           "43": {
               "isPublished": true,
               "dateAdded": "2024-08-16T09:00:00+00:00",
               "createdBy": 1,
               "createdByUser": "Joe Smith",
               "dateModified": null,
               "modifiedBy": null,
               "modifiedByUser": null,
               "id": 43,
               "fields": {
                   "all": {
                       "companyname": "TechCorp",
                       "companyemail": "info@techcorp.com"
                   }
               },
               "score": 25,
               "tags": []
           }
       }
   }

**Properties**

Same as `Get Company <#get-company>`_.

.. vale off

Create Company
**************

.. vale on

.. code-block:: php

   <?php

   $data = array(
       'companyname'    => 'Acme Inc.',
       'companyemail'   => 'contact@acme.com',
       'companycity'    => 'Boston',
       'companycountry' => 'United States',
       'overwriteWithBlank' => true,
       'tags'           => ['Enterprise', 'VIP']
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
     - Type
     - Description
   * - ``companyname``
     - string
     - Company name is the only required field
   * - ``companyemail``
     - string
     - Company's email address
   * - ``companyaddress1``
     - string
     - Address line 1
   * - ``companyaddress2``
     - string
     - Address line 2
   * - ``companycity``
     - string
     - City
   * - ``companystate``
     - string
     - State or province
   * - ``companyzipcode``
     - string
     - Postal/ZIP code
   * - ``companycountry``
     - string
     - Country
   * - ``companyphone``
     - string
     - Phone number
   * - ``companywebsite``
     - string
     - Website URL
   * - ``tags``
     - array
     - Array of tag names to assign to the Company
   * - ``overwriteWithBlank``
     - boolean
     - If ``true``, empty values overwrite existing values. Default is ``false``.

You can also set any custom Company fields by including them in the request body using their field alias as the key.

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

   $id   = 42;
   $data = array(
       'companyname' => 'Updated Company Name',
       'tags'        => ['-Enterprise', 'Strategic']
   );

   // Create new a Company if ID 42 isn't found?
   $createIfNotFound = true;

   $company = $companyApi->edit($id, $data, $createIfNotFound);

Edit an existing Company. Note that this supports PUT or PATCH depending on the desired behavior.

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

Same parameters as `Create Company <#create-company>`_.

**Modifying Tags**

When editing a Company, you can add or remove tags using the ``tags`` parameter:

- To add tags, include the tag names in the array: ``['NewTag', 'AnotherTag']``
- To remove tags, prefix the tag name with a minus sign: ``['-OldTag']``
- You can combine additions and removals: ``['-OldTag', 'NewTag']``

.. code-block:: php

   <?php

   // Remove 'Enterprise' tag and add 'Strategic' tag
   $data = array(
       'tags' => ['-Enterprise', 'Strategic']
   );

   $company = $companyApi->edit($id, $data);

**Response**

If using ``PUT``, the expected response code is ``200`` if editing the Company, or ``201`` if creating a Company.

If using ``PATCH``, the expected response code is ``200``.

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

HTTP request
============

.. vale on

``POST /companies/COMPANY_ID/contact/CONTACT_ID/add``

Response
========

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
   $response = $companyApi->removeContact($companyId, $contactId);
   if (!isset($response['success'])) {
       // handle error
   }

Manually remove a Contact from a specific Company.

.. vale off

HTTP request
============

.. vale on

``POST /companies/COMPANY_ID/contact/CONTACT_ID/remove``

Response
========

``Expected Response Code: 200``

.. code-block:: json

   {
       "success": true
   }
