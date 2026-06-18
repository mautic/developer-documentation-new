Themes
######

Use this endpoint to manipulate and obtain details on Mautic's Themes.

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
   $initAuth  = new ApiAuth();
   $auth      = $initAuth->newAuth($settings);
   $apiUrl    = "https://example.com";
   $api       = new MauticApi();
   $themesApi = $api->newApi("themes", $auth, $apiUrl);

.. vale off

Get Theme
*********

.. vale on

Retrieves the Theme as a ZIP file with the ``application/zip`` header on success, or a JSON response with error messages on failure. The PHP API library saves the ZIP file to the system's temporary directory and retrieves the path.

.. code-block:: php

   <?php

   //...
   $response = $themesApi->get($themeName);

.. vale off

HTTP request
============

.. vale on

``GET /themes/THEME_NAME``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Theme ZIP file.

.. code-block:: json

   {
       "file": "/absolute/path/to/the/system/temp/dir/with/the/theme/zip/file"
   }

.. vale off

Set temporary file path
***********************

.. vale on

Changes the default temporary directory where the PHP API library creates the ZIP file. Creates the directory if it doesn't exist.

.. code-block:: php

   <?php

   //...
   $themesApi->setTemporaryFilePath("/absolute/path/to/a/different/temp/dir");
   $response = $themesApi->get($themeName);

Response
========

* Returns ``200 OK`` when the request successfully changes or creates the default temporary directory.

.. code-block:: json

   {
       "file": "/absolute/path/to/a/different/temp/dir/zipfile"
   }

.. vale off

List Themes
***********

.. vale on

Lists all installed Themes with details from their ``config.json`` files.

.. code-block:: php

   <?php

   //...
   $response = $themesApi->getList();

.. vale off

HTTP request
============

.. vale on

``GET /themes``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Themes list.

.. code-block:: json

   {
       "themes": {
           "blank": {
               "name": "Blank",
               "key": "blank",
               "config": {
                   "name": "Blank",
                   "author": "Mautic team",
                   "authorUrl": "https://mautic.org",
                   "features": [
                       "page",
                       "email",
                       "form"
                   ]
               }
           }
       }
   }

Properties
----------

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Name
     - Type
     - Description
   * - ``themes``
     - array
     - List of installed Themes and their configurations

Theme object properties
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Name
     - Type
     - Description
   * - ``name``
     - string
     - Display name of the Theme
   * - ``key``
     - string
     - Directory name and unique identifier of the Theme
   * - ``config``
     - object
     - Theme configuration from ``config.json``

.. vale off

Config object properties
------------------------

.. vale on

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Name
     - Type
     - Description
   * - ``name``
     - string
     - Theme name
   * - ``author``
     - string
     - Theme author
   * - ``authorUrl``
     - string
     - Author's website URL
   * - ``features``
     - array
     - List of supported features such as ``page``, ``email``, or ``form``
   * - ``builder``
     - array
     - Optional list of compatible builders such as ``legacy`` or ``grapeJs``

.. vale off

Create Theme
************

.. vale on

Creates a new Theme or updates an existing one from the provided ZIP file. The Theme name comes from the ZIP filename.

.. code-block:: php

   <?php

   //...
   $data = array(
       'file' => dirname(__DIR__) . '/' . 'mytheme.zip'
   );

   $response = $themesApi->create($data);

Mautic sends the file through a standard POST files array, the same way a browser sends files during upload.

.. vale off

HTTP request
============

.. vale on

``POST /themes/new``

POST parameters
---------------

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Name
     - Type
     - Description
   * - ``file``
     - file
     - The ZIP file containing the Theme - **required**

Response
========

* Returns ``200 OK`` when the request successfully creates a Theme.

.. code-block:: json

   {
       "success": true
   }

Error responses
---------------

The API returns error messages if:

* The request includes no uploaded file
* The uploaded file doesn't have a ``.zip`` extension
* The ZIP file is missing required files - ``config.json`` and ``html/message.html.twig``
* The ZIP file contains disallowed file extensions

.. note::

   **Form style-only Themes:** A Theme that declares the ``form`` feature and includes a Form style override file - ``html/MauticFormBundle/Builder/_style.html.twig`` or ``html/MauticFormBundle/Builder/style.html.twig`` - doesn't require ``html/message.html.twig``.

.. vale off

Delete Theme
************

.. vale on

Deletes a Theme. The system prevents deletion of stock Themes.

.. code-block:: php

   <?php

   //...
   $response = $themesApi->delete($themeName);

.. vale off

HTTP request
============

.. vale on

``DELETE /themes/THEME_NAME/delete``

Response
========

* Returns ``200 OK`` when the request successfully deletes the Theme.

.. code-block:: json

   {
       "success": true
   }

.. note::

   Mautic prevents permanent deletion of default Themes bundled with the app. Attempting to delete a default Theme hides it instead. Use the Theme visibility toggle in the Mautic UI to restore hidden default Themes.
