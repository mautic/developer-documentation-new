Themes
######

This endpoint is useful for working with Mautic Themes.

**Using Mautic's API Library**

You can interact with this API through the :xref:`Mautic API Library` as follows, or use the various http endpoints as described in this document.

.. code-block:: php

   <?php
   use Mautic\MauticApi;
   use Mautic\Auth\ApiAuth;

   $initAuth = new ApiAuth();
   $auth     = $initAuth->newAuth($settings);
   $apiUrl   = "https://mautic.example.com";
   $api      = new MauticApi();
   $themesApi = $api->newApi("themes", $auth, $apiUrl);

.. vale off

Get Theme
*********

.. vale on

Returns directly the ZIP file in the response with the ``application/ZIP`` header on success or a JSON response body with error messages on fail. The PHP API library saves the ZIP file to the system's temporary directory and provides you with the path.

.. code-block:: php

   <?php
   $response = $themesApi->get($themeName);

.. code-block:: json

   {
       "file": "/absolute/path/to/the/system/temp/dir/with/the/theme/ZIP/file"
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

Changes the default temporary directory where the ZIP file gets created. The directory gets created if it doesn't exist.

.. code-block:: php

   <?php
   $themesApi->setTemporaryFilePath("/absolute/path/to/a/different/temp/dir");
   $response = $themesApi->get($themeName);

.. code-block:: json

   {
       "file": "/absolute/path/to/a/different/temp/dir/ZIPfile"
   }

.. vale off

Get List of Themes
******************

.. vale on

Lists all installed Themes with the details stored in their ``config.json`` files.

.. code-block:: php

   <?php
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
                   "authorUrl": "https:\/\/mautic.org",
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

   * - Name
     - Type
     - Description
   * - ``themes``
     - array
     - List of installed Themes and their configs

.. vale off

Create Theme
************

.. vale on

Creates a new Theme or updates an existing one, based on the filename of the provided ZIP file.

.. code-block:: php

   <?php
   $data = array(
       'file' => dirname(__DIR__).'/'.'mytheme.ZIP' // Must be a path to an existing file
   );

   $response = $themeApi->create($data);

The file gets sent through a regular POST files array like a browser sends it during file upload.

.. vale off

**HTTP Request**

.. vale on

``POST /themes/new``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {  
     "success": true
   }

.. vale off

Delete File
***********

.. vale on

.. code-block:: php

   <?php
   $response = $themeApi->delete($themeName);

Delete a Theme. You can't delete stock Themes.

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
