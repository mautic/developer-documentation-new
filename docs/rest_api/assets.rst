
Assets
######

Use this endpoint to obtain details on Mautic's Assets.

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
   $assetApi = $api->newApi("Assets", $auth, $apiUrl);

.. vale off

Get Asset
**********

.. vale on

.. code-block:: php

   <?php

   //...
   $asset = $assetApi->get($id);



Get an individual Asset by ID.

.. vale off

**HTTP Request**

.. vale on

``GET /assets/ID``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "asset": {
           "id": 1,
           "title": "Product Whitepaper",
           "description": "Some description",
           "alias": "whitepaper",
           "language": "en",
           "isPublished": true,
           "publishUp": "2015-06-07T06:28:27+00:00",
           "publishDown": "2015-06-30T06:28:27+00:00",
           "dateAdded": "2015-06-07T06:28:27+00:00",
           "createdBy": 1,
           "createdByUser": "Rahel Herschel",
           "dateModified": "2015-06-010T09:30:47+00:00",
           "modifiedBy": 1,
           "modifiedByUser": "Rahel Herschel",
           "downloadCount": 10,
           "uniqueDownloadCount": 8,
           "revision": 1,
           "category": {
               "createdByUser": "Yoav Andrysiak",
               "modifiedByUser": "Yoav Andrysiak",
               "id": 19,
               "title": "test",
               "alias": "test",
               "description": null,
               "color": null,
               "bundle": "asset"
           },
           "extension": "pdf",
           "mime": "application/pdf",
           "size": 269128,
           "downloadUrl": "https://example.com/asset/1:whitepaper"
       }
   }

**Asset Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Asset
   * - ``title``
     - string
     - Title/name of the Asset
   * - ``description``
     - string/null
     - Description of the Asset
   * - ``alias``
     - string
     - Used to generate the URL for the Asset
   * - ``language``
     - string
     - Locale of the Asset
   * - ``isPublished``
     - boolean
     - Published state
   * - ``publishUp``
     - datetime/null
     - Asset publish date/time
   * - ``publishDown``
     - datetime/null
     - Asset unpublish date/time
   * - ``dateAdded``
     - ``datetime``
     - Asset creation date/time
   * - ``createdBy``
     - int
     - ID of the User that created the Asset
   * - ``createdByUser``
     - string
     - Name of the User that created the Asset
   * - ``dateModified``
     - datetime/null
     - Asset modified date/time
   * - ``modifiedBy``
     - int
     - ID of the User that last modified the Asset
   * - ``modifiedByUser``
     - string
     - Name of the User that last modified the Asset
   * - ``downloadCount``
     - int
     - Total number of downloads
   * - ``uniqueDownloadCount``
     - int
     - Unique number of downloads
   * - ``revision``
     - int
     - Revision version
   * - ``category``
     - object/null
     - Object with the Category details
   * - ``extension``
     - string
     - Extension of the Asset
   * - ``mime``
     - string
     - Mime type of the Asset
   * - ``size``
     - int
     - File size of the Asset in bytes
   * - ``downloadUrl``
     - string
     - Public download URL for the Asset

.. vale off

List assets
***********

.. vale on

.. code-block:: php

   <?php
   // ...

   $assets = $assetApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

**HTTP Request**

.. vale on

``GET /assets``

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
   * - ``publishedOnly``
     - Only return currently published entities
   * - ``minimal``
     - Return only array of entities without additional lists in it


**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "total": 1,
       "assets": [
           {
               "id": 1,
               "title": "Product Whitepaper",
               "description": "Some description",
               "alias": "whitepaper",
               "language": "en",
               "isPublished": true,
               "publishUp": "2015-06-07T06:28:27+00:00",
               "publishDown": "2015-06-30T06:28:27+00:00",
               "dateAdded": "2015-06-07T06:28:27+00:00",
               "createdBy": 1,
               "createdByUser": "Wayne Costa",
               "dateModified": "2015-06-010T09:30:47+00:00",
               "modifiedBy": 1,
               "modifiedByUser": "Wayne Costa",
               "downloadCount": 10,
               "uniqueDownloadCount": 8,
               "revision": 1,
               "category": null,
               "extension": "pdf",
               "mime": "application/pdf",
               "size": 269128,
               "downloadUrl": "https://example.com/asset/1:whitepaper"
           }
       ]
   }

**Properties**

Same as `Get Asset <#get-asset>`_.

.. vale off

Create Asset
************

.. vale on

.. code-block:: php

   <?php 

   /**
    * Local Asset example
    */
   // Upload a local file first
   $apiContextFiles = $this->getContext('files');
   $apiContextFiles->setFolder('assets');
   $fileRequest = array(
       'file' => dirname(__DIR__).'/'.'mauticlogo.png'
   );
   $response = $apiContextFiles->create($fileRequest);

   $data = array(
       'title' => 'Mautic Logo sent as a API request',
       'storageLocation' => 'local',
       'file' => $response['file']['name']
   );

   $asset = $assetApi->create($data);


   /**
    * Remote Asset example
    */
   $data = array(
       'title' => 'PDF sent as a API request',
       'storageLocation' => 'remote',
       'file' => 'https://www.mautic.org/media/logos/logo/Mautic_Logo_DB.pdf'
   );

   $asset = $assetApi->create($data);

Create a new Asset. There are 2 options: local or remote Asset.

.. vale off

**HTTP Request**

.. vale on

``POST /assets/new``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``title``
     - string
     - Asset title
   * - ``storageLocation``
     - string
     - Storage location can be local or remote
   * - ``file``
     - string
     - Either URL for remote file or filename for local file


**Response**

``Expected Response Code: 201``

**Properties**

Same as `Get Asset <#get-asset>`_.

.. vale off

Edit Asset
**********

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'type' => 'general',
   );

   // Create new a Asset if ID 1 isn't found?
   $createIfNotFound = true;

   $asset = $assetApi->edit($id, $data, $createIfNotFound);

Edit a new Asset. This supports PUT or PATCH depending on the desired behavior.

**PUT** creates a Asset if the given ID doesn't exist and clears all the Asset information, adding the information from the request.
**PATCH** fails if the Asset with the given ID doesn't exist and updates the Asset field values with the values from the request.

.. vale off

**HTTP Request**

.. vale on

To edit a Asset and return a 404 if the Asset isn't found:

``PATCH /assets/ID/edit``

To edit a Asset and create a new one if the Asset isn't found:

``PUT /assets/ID/edit``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``title``
     - string
     - Asset title
   * - ``storageLocation``
     - string
     - Storage location can be local or remote
   * - ``file``
     - string
     - Either URL for remote file or filename for local file


**Response**

If ``PUT``\ , the expected response code if editing the Asset is ``200`` or ``201`` if created.

If using ``PATCH``\ , the expected response code is ``200``.

**Properties**

Same as `Get Asset <#get-asset>`_.

.. vale off

Delete Asset
************

.. vale on

.. code-block:: php

   <?php

   $asset = $assetApi->delete($id);

Delete a Asset. In case of local storage location, the local file gets deleted as well.

.. vale off

**HTTP Request**

.. vale on

``DELETE /assets/ID/delete``

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get Asset <#get-asset>`_.
