
Fields
######

Use this endpoint to work with Mautic's Contact/Company fields.

**Using Mautic's API Library**

You can interact with this API through the :xref:`Mautic API Library` as follows, or use the various http endpoints as described in this document.

.. code-block:: php

   <?php
   use Mautic\MauticApi;
   use Mautic\Auth\ApiAuth;

   // ...
   $initAuth = new ApiAuth();
   $auth     = $initAuth->newAuth($settings);
   $apiUrl   = "https://example.com";
   $api      = new MauticApi();
   $assetApi = $api->newApi("assets", $auth, $apiUrl);

   // Get Contact field context:
   $fieldApi = $api->newApi("contactFields", $auth, $apiUrl);

   // Or use 'companyFields' for company fields:
   $fieldApi = $api->newApi("companyFields", $auth, $apiUrl);


Get field
*********


.. code-block:: php

   <?php

   //...
   $field = $fieldApi->get($id);


Get an individual field by ID.

.. vale off

**HTTP Request**

.. vale on

``GET /fields/contact/ID`` or ``GET /fields/company/ID``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {  
     "field":{  
       "isPublished":true,
       "dateAdded":"2016-11-10T13:02:52+00:00",
       "createdBy":1,
       "createdByUser":"Sharru-Ukin Kumar",
       "dateModified":null,
       "modifiedBy":null,
       "modifiedByUser":null,
       "id":165,
       "label":"API test field",
       "alias":"api_test_field11",
       "type":"text",
       "group":null,
       "order":36,
       "object":"lead",
       "defaultValue":null,
       "isRequired":false,
       "isPubliclyUpdatable":false,
       "isUniqueIdentifier":0,
       "properties":[]
     }
   }

**Field Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the field
   * - ``isPublished``
     - boolean
     - Published state
   * - ``publishUp``
     - datetime/null
     - Field publish date/time
   * - ``publishDown``
     - datetime/null
     - Field unpublish date/time
   * - ``dateAdded``
     - ``datetime``
     - Field creation date/time
   * - ``createdBy``
     - int
     - ID of the User that created the field
   * - ``createdByUser``
     - string
     - Name of the User that created the field
   * - ``dateModified``
     - datetime/null
     - Field modified date/time
   * - ``modifiedBy``
     - int
     - ID of the User that last modified the field
   * - ``modifiedByUser``
     - string
     - Name of the User that last modified the field
   * - ``label``
     - string
     - Name of the field
   * - ``alias``
     - string
     - Unique alias of the field used in the Form Field name attributes
   * - ``description``
     - string/null
     - Description of the field
   * - ``type``
     - string
     - Field type
   * - ``group``
     - string
     - Group of the fields where the field belongs 
   * - ``order``
     - int
     - Order number of the field
   * - ``object``
     - string
     - Which object uses the field, Contact or Company
   * - ``defaultValue``
     - string
     - Default value of the field
   * - ``isRequired``
     - boolean
     - ``true`` if this is a required field
   * - ``isPubliclyUpdatable``
     - boolean
     - ``true`` if public requests can change the field value - the tracking pixel query for example
   * - ``isUniqueIdentifier``
     - boolean
     - ``true`` if the field is a unique identifier, therefore Contacts should merge if the value of this field is the same
   * - ``properties``
     - array
     - Field options if the field type needs some. 

.. vale off

List Contact fields
*******************

.. vale on

.. code-block:: php

   <?php

   //...
   $fields = $fieldApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. code-block:: json

   {  
     "total":71,
     "fields":[  
       {  
         "isPublished":true,
         "dateAdded":"2016-10-12T11:31:13+00:00",
         "createdBy":1,
         "createdByUser":"Judith Czinege",
         "dateModified":"2016-10-12T11:31:30+00:00",
         "modifiedBy":1,
         "modifiedByUser":"Judith Czinege",
         "id":100,
         "label":"Multiselect test",
         "alias":"multiselect_test",
         "type":"multiselect",
         "group":"core",
         "order":3,
         "object":"lead",
         "defaultValue":null,
         "isRequired":false,
         "isPubliclyUpdatable":false,
         "isUniqueIdentifier":false,
         "properties":{  
           "list":[  
             {  
               "label":"PHP",
               "value":"php"
             },
             {  
               "label":"JS",
               "value":"js"
             },
             {  
               "label":"English",
               "value":"en"
             }
           ]
         }
       },
     ]
   }

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
     - Limit number of entities to return, defaults to the system configuration for pagination - defaults to 30
   * - ``orderBy``
     - Column to sort by, can use any column listed in the response
   * - ``orderByDir``
     - Sort direction: ``asc`` or ``desc``
   * - ``publishedOnly``
     - Only return currently published entities
   * - ``minimal``
     - Return only array of entities without additional lists in it


.. vale off

**HTTP Request**

.. vale on

``GET /fields/contact`` or ``GET /fields/company``

**Response**

``Expected Response Code: 200``

See JSON code example.

**Field properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the field
   * - ``isPublished``
     - boolean
     - Published state
   * - ``publishUp``
     - datetime/null
     - Field publish date/time
   * - ``publishDown``
     - datetime/null
     - Field unpublish date/time
   * - ``dateAdded``
     - ``datetime``
     - Field creation date/time
   * - ``createdBy``
     - int
     - ID of the User that created the field
   * - ``createdByUser``
     - string
     - Name of the User that created the field
   * - ``dateModified``
     - datetime/null
     - Field modified date/time
   * - ``modifiedBy``
     - int
     - ID of the User that last modified the field
   * - ``modifiedByUser``
     - string
     - Name of the User that last modified the field
   * - ``label``
     - string
     - Name of the field
   * - ``alias``
     - string
     - Unique alias of the field used in the Form Field name attributes
   * - ``description``
     - string/null
     - Description of the field
   * - ``type``
     - string
     - Field type
   * - ``group``
     - string
     - Group of the fields where the field belongs 
   * - ``order``
     - int
     - Order number of the field
   * - ``object``
     - string
     - Which object uses the field\ Contact or Company
   * - ``defaultValue``
     - string
     - Default value of the field
   * - ``isRequired``
     - boolean
     - ``true`` if this is a required field
   * - ``isPubliclyUpdatable``
     - boolean
     - ``true`` if public requests can change the field value - the tracking pixel query for example
   * - ``isUniqueIdentifier``
     - boolean
     - ``true`` if the field is a unique identifier therefore Contacts should merge if the value of this field is the same
   * - ``properties``
     - array
     - Field options if the field type needs some

.. vale off

Create field
************

.. vale on

.. code-block:: php

   <?php 

   $data = array(
       'label' => 'API test field',
       'type' => 'text',
   );

   $field = $fieldApi->create($data);

**Multiselect field**

.. code-block:: php

   <?php

   $data = array(
       'label' => 'API test field',
       'type' => 'multiselect',
       'isPubliclyUpdatable' => true,
       'properties' => array(
          'list' => array(
             array(
               'label' => 'label 1',
               'value' => 'value 1'
             ),
             array(
               'label' => 'label 2',
               'value' => 'value 2'
             )
           )
       )
   );

   $field = $fieldApi->create($data);

Create a new field.

.. vale off

**HTTP Request**

.. vale on

``POST /fields/contact/new`` or ``POST /fields/company/new``

**POST parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``label``
     - string
     - Name of the field
   * - ``alias``
     - string
     - Unique alias of the field used in the Form Field name attributes
   * - ``description``
     - string/null
     - Description of the field
   * - ``type``
     - string
     - Field type
   * - ``group``
     - string
     - Group of the fields where the field belongs 
   * - ``order``
     - int
     - Order number of the field
   * - ``object``
     - string
     - Which object uses the field, Contact or Company
   * - ``defaultValue``
     - string
     - Default value of the field
   * - ``isRequired``
     - boolean
     - ``true`` if this is a required field
   * - ``isPubliclyUpdatable``
     - boolean
     - ``true`` if public requests can change the field value - the tracking pixel query for example
   * - ``isUniqueIdentifier``
     - boolean
     - ``true`` if the field is unique identifier and so the Contacts should merge if the value of this field is the same
   * - ``properties``
     - array
     - Field options if the field type needs some


**Response**

``Expected Response Code: 201``

**Properties**

Same as `Get Field <#get-field>`_.

.. vale off

Edit field
**********

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'label' => 'API test field',
       'type' => 'text',
   );

   // Create new a field if ID 1 isn't found?
   $createIfNotFound = true;

   $field = $fieldApi->edit($id, $data, $createIfNotFound);

Edit a new field. Field that this supports PUT or PATCH depending on the desired behavior.

**PUT** creates a field if the given ID doesn't exist.
**PATCH** fails if the field with the given ID doesn't exist and updates the field values with the values field the request.

.. vale off

**HTTP Request**

.. vale on

To edit a field and return a 404 if the field isn't found:

``PATCH /fields/contact/ID/edit`` or ``PATCH /fields/company/ID/edit``

To edit a field and create a new one if the field isn't found:

``PUT /fields/contact/ID/edit`` or ``PUT /fields/company/ID/edit``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``label``
     - string
     - Name of the field
   * - ``alias``
     - string
     - Unique alias of the field used in the Form Field name attributes
   * - ``description``
     - string/null
     - Description of the field
   * - ``type``
     - string
     - Field type
   * - ``group``
     - string
     - Group of the fields where the field belongs 
   * - ``order``
     - int
     - Order number of the field
   * - ``object``
     - string
     - Which object uses the field, Contact or Company
   * - ``defaultValue``
     - string
     - Default value of the field
   * - ``isRequired``
     - boolean
     - ``true`` if this is a required field
   * - ``isPubliclyUpdatable``
     - boolean
     - ``true`` if public requests can change the field value - the tracking pixel query for example
   * - ``isUniqueIdentifier``
     - boolean
     - ``true`` if the field is a unique identifier and therefore Contacts should merge if the value of this field is the same
   * - ``properties``
     - array
     - Field options if the field type needs some.


**Response**

If using ``PUT``, the expected response code is ``200`` if editing the field or ``201`` if creating the field.

If using ``PATCH``, the expected response code is ``200``.

**Properties**

Same as `Get Field <#get-field>`_.

.. vale off

Delete field
************

.. vale on

.. code-block:: php

   <?php

   $field = $fieldApi->delete($id);

Delete a field.

.. vale off

**HTTP Request**

.. vale on

``DELETE /fields/contact/ID/delete`` or ``DELETE /fields/company/ID/delete``

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get Field <#get-field>`_.
