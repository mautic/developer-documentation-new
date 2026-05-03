Themes
######

Use this endpoint to work with Mautic Themes.

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
   $themesApi = $api->newApi("themes", $auth, $apiUrl);

.. vale off

Get Theme
*********

.. vale on

Returns the Theme as a zip file with the ``application/zip`` header on success, or a JSON response with error messages on failure. The PHP API library saves the zip file to the system's temporary directory and returns the path.

.. code-block:: php

   <?php

   //...
   $response = $themesApi->get($themeName);

.. code-block:: json

   {
       "file": "/absolute/path/to/the/system/temp/dir/with/the/theme/zip/file"
   }

.. vale off

**HTTP Request**

.. vale on

``GET /themes/THEME_NAME``

**Response**

``Expected Response Code: 200``

.. vale off

Set Temporary File Path
***********************

.. vale on

Changes the default temporary directory where the PHP API library creates the zip file. Creates the directory if it doesn't exist.

.. code-block:: php

   <?php

   //...
   $themesApi->setTemporaryFilePath("/absolute/path/to/a/different/temp/dir");
   $response = $themesApi->get($themeName);

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

**HTTP Request**

.. vale on

``GET /themes``

**Response**

``Expected Response Code: 200``

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

**Response Properties**

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Name
     - Type
     - Description
   * - ``themes``
     - array
     - List of installed Themes and their configurations

**Theme Object Properties**

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

**Config Object Properties**

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

Creates a new Theme or updates an existing one from the provided zip file. The Theme name comes from the zip file name.

.. code-block:: php

   <?php

   //...
   $data = array(
       'file' => dirname(__DIR__) . '/' . 'mytheme.zip'
   );

   $response = $themesApi->create($data);

The file is sent through a standard POST files array, the same way a browser sends files during upload.

.. vale off

**HTTP Request**

.. vale on

``POST /themes/new``

**POST Parameters**

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Name
     - Type
     - Description
   * - ``file``
     - file
     - The zip file containing the Theme (required)

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "success": true
   }

**Error Responses**

The API returns error messages if:

- No file is uploaded
- The uploaded file doesn't have a ``.zip`` extension
- The zip file is missing required files (``config.json``, ``html/message.html.twig``)
- The zip file contains disallowed file extensions

.. vale off

Delete Theme
************

.. vale on

Deletes a Theme. You can't delete stock Themes; they become hidden instead.

.. code-block:: php

   <?php

   //...
   $response = $themesApi->delete($themeName);

.. vale off

**HTTP Request**

.. vale on

``DELETE /themes/THEME_NAME/delete``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "success": true
   }

.. note::

   Default Themes bundled with Mautic can't be permanently deleted. Attempting to delete a default Theme hides it instead. Use the Theme visibility toggle in the Mautic UI to restore hidden default Themes.
