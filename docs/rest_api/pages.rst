Landing Pages
#############

Use this endpoint to manipulate and obtain details on Mautic's Landing Pages.

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
   $pageApi  = $api->newApi("pages", $auth, $apiUrl);

.. vale off

Get Landing Page
****************

.. vale on

Retrieves an individual Landing Page.

.. code-block:: php

   <?php

   //...
   $page = $pageApi->get($id);

.. vale off

HTTP request
============

.. vale on

``GET /pages/ID``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Landing Page.

.. _get Landing Page response:

.. code-block:: json

   {
       "page": {
           "isPublished": true,
           "dateAdded": "2015-07-15T15:06:02+00:00",
           "dateModified": "2015-07-20T13:11:56+00:00",
           "createdBy": 1,
           "createdByUser": "Joe Smith",
           "modifiedBy": 1,
           "modifiedByUser": "Joe Smith",
           "id": 3,
           "title": "Webinar Landing Page",
           "alias": "webinar-landing-page",
           "language": "en",
           "publishUp": null,
           "publishDown": null,
           "hits": 0,
           "uniqueHits": 0,
           "variantHits": 0,
           "revision": 1,
           "metaDescription": null,
           "redirectType": null,
           "redirectUrl": null,
           "isPreferenceCenter": false,
           "noIndex": false,
           "variantSettings": [],
           "variantStartDate": null,
           "variantParent": null,
           "variantChildren": [],
           "translationParent": null,
           "translationChildren": [],
           "template": "blank",
           "customHtml": "<!DOCTYPE html> ...",
           "category": null
       }
   }

.. _get Landing Page properties:

.. vale off

Landing Page properties
-----------------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``isPublished``
     - boolean
     - Landing Page publication status
   * - ``dateAdded``
     - datetime
     - Landing Page creation date and time
   * - ``dateModified``
     - datetime/null
     - Landing Page last modification date and time
   * - ``createdBy``
     - integer
     - ID of the User who created the Landing Page
   * - ``createdByUser``
     - string
     - Name of the User who created the Landing Page
   * - ``modifiedBy``
     - integer
     - ID of the User who last modified the Landing Page
   * - ``modifiedByUser``
     - string
     - Name of the User who last modified the Landing Page
   * - ``id``
     - integer
     - ID of the Landing Page
   * - ``title``
     - string
     - Title of the Landing Page
   * - ``alias``
     - string
     - Alias used to generate the URL for the Landing Page
   * - ``language``
     - string
     - Language locale of the Landing Page, such as ``en``
   * - ``publishUp``
     - datetime/null
     - Activation date and time for the Landing Page
   * - ``publishDown``
     - datetime/null
     - Deactivation date and time for the Landing Page
   * - ``hits``
     - integer
     - Total Landing Page hit count
   * - ``uniqueHits``
     - integer
     - Unique Landing Page hit count
   * - ``variantHits``
     - integer
     - Hit count since ``variantStartDate``
   * - ``revision``
     - integer
     - Revision number of the Landing Page
   * - ``metaDescription``
     - string/null
     - Meta description for the Landing Page's ``<head>``
   * - ``redirectType``
     - integer/null
     - When unpublished, the redirect status code to use, such as ``301`` or ``302``
   * - ``redirectUrl``
     - string/null
     - When unpublished, the URL to redirect to when ``redirectType`` is set
   * - ``isPreferenceCenter``
     - boolean
     - Preference center status. When set to ``true``, Mautic marks the Landing Page as a preference center page that recipients see when they select the ``{unsubscribe_url}`` link in an Email.
   * - ``noIndex``
     - boolean
     - Search indexing status. When set to ``true``, Mautic turns off search engine indexing for the Landing Page.
   * - ``variantSettings``
     - array
     - Properties of the A/B test
   * - ``variantStartDate``
     - datetime/null
     - Date and time the A/B test began
   * - ``variantParent``
     - object
     - The parent Landing Page when this Landing Page is a variant, such as an A/B test
   * - ``variantChildren``
     - array
     - Array of Landing Page entities that are variants of this Landing Page
   * - ``translationParent``
     - object
     - The parent Landing Page when this Landing Page is a translation
   * - ``translationChildren``
     - array
     - Array of Landing Page entities that are translations of this Landing Page
   * - ``template``
     - string
     - Theme used to style the Landing Page
   * - ``customHtml``
     - string
     - Static HTML content of the Landing Page
   * - ``category``
     - object/null
     - Object with the Category details

.. vale on

.. vale off

List Landing Pages
******************

.. vale on

Retrieves a list of Landing Pages.

.. code-block:: php

   <?php
   // ...

   $pages = $pageApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

HTTP request
============

.. vale on

``GET /pages``

Query parameters
----------------

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``search``
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

       **Note**: convert ``camelCase`` properties to ``snake_case``. For example, ``dateAdded`` becomes ``date_added``, ``redirectUrl`` becomes ``redirect_url``, and so on
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

* Returns ``200 OK`` when the request successfully retrieves the Landing Pages list.

.. code-block:: json

   {
       "total": 1,
       "pages": [
           {
               "isPublished": true,
               "dateAdded": "2015-07-15T15:06:02+00:00",
               "dateModified": "2015-07-20T13:11:56+00:00",
               "createdBy": 1,
               "createdByUser": "Joe Smith",
               "modifiedBy": 1,
               "modifiedByUser": "Joe Smith",
               "id": 3,
               "title": "Webinar Landing Page",
               "alias": "webinar-landing-page",
               "category": null
           }
       ]
   }

Properties
----------

Refer to :ref:`Landing Page properties <get Landing Page properties>`.

.. vale off

Create Landing Page
*******************

.. vale on

Creates a new Landing Page.

.. code-block:: php

   <?php

   $data = array(
       'title'       => 'Page A',
       'isPublished' => 1,
   );

   $page = $pageApi->create($data);

.. vale off

HTTP request
============

.. vale on

``POST /pages/new``

.. _create Landing Page POST parameters:

POST parameters
---------------

.. vale off

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``title``
     - string
     - **Required.**

       Title of the Landing Page
   * - ``alias``
     - string
     - Alias used to generate the URL for the Landing Page. Mautic generates the alias automatically when not set.
   * - ``isPublished``
     - boolean
     - Published state - a value of ``0`` or ``1``
   * - ``language``
     - string
     - Language locale of the Landing Page, such as ``en``
   * - ``template``
     - string
     - Theme used to style the Landing Page
   * - ``customHtml``
     - string
     - Static HTML content of the Landing Page
   * - ``metaDescription``
     - string
     - Meta description for the Landing Page's ``<head>``
   * - ``isPreferenceCenter``
     - boolean
     - Set to ``true`` to mark the Landing Page as a preference center page
   * - ``noIndex``
     - boolean
     - Set to ``true`` to turn off search engine indexing for the Landing Page
   * - ``redirectType``
     - integer
     - When unpublished, the redirect status code to use, such as ``301`` or ``302``
   * - ``redirectUrl``
     - string
     - When unpublished, the URL to redirect to when ``redirectType`` is set

.. vale on

Response
========

* Returns ``201 Created`` when the request successfully creates a Landing Page.

The response is a JSON object similar to :ref:`Get Landing Page <get Landing Page response>`.

Properties
----------

Refer to :ref:`Landing Page properties <get Landing Page properties>`.

.. vale off

Edit Landing Page
*****************

.. vale on

Edits a Landing Page.

This operation supports ``PUT`` or ``PATCH``, depending on the desired behavior:

* ``PUT``: **full replacement**. Creates a new Landing Page when the ID is missing. When the ID exists, the request clears all existing data and replaces it with the values you provide.
* ``PATCH``: **partial update**. Updates only the field values in the request data. The request fails when the Landing Page ID doesn't exist.

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'title'       => 'New page title',
       'isPublished' => 0,
   );

   // Create a new Landing Page if ID 1 isn't found
   $createIfNotFound = true;

   $page = $pageApi->edit($id, $data, $createIfNotFound);

.. vale off

HTTP request
============

.. vale on

* ``PUT /pages/ID/edit``: updates an existing Landing Page or creates a new one when the ID doesn't exist.
* ``PATCH /pages/ID/edit``: updates an existing Landing Page. The request fails when the ID doesn't exist.

POST parameters
---------------

Accepts the same parameters as those described in :ref:`Create Landing Page <create Landing Page POST parameters>`. All parameters are optional.

Response
========

* ``PUT``: returns ``200 OK`` when the request successfully updates the Landing Page or ``201 Created`` when the request creates a Landing Page.
* ``PATCH``: returns ``200 OK`` when the request successfully updates the Landing Page or ``404 Not Found`` error when the Landing Page ID doesn't exist.

The response is a JSON object similar to :ref:`Get Landing Page <get Landing Page response>`.

Properties
----------

Refer to :ref:`Landing Page properties <get Landing Page properties>`.

.. vale off

Delete Landing Page
*******************

.. vale on

Deletes a Landing Page.

.. code-block:: php

   <?php

   $page = $pageApi->delete($id);

.. vale off

HTTP request
============

.. vale on

``DELETE /pages/ID/delete``

Response
========

* Returns ``200 OK`` when the request successfully deletes the Landing Page.

The response is a JSON object containing the data of the deleted Landing Page, similar to :ref:`Get Landing Page <get Landing Page response>`.

Properties
----------

Refer to :ref:`Landing Page properties <get Landing Page properties>`.
