Files
#####

This endpoint is useful for working with files of images and Assets.

.. note::

  Assets don't support subdirectories.

**Using Mautic's API Library**

You can interact with this API through the :xref:`Mautic API Library` as follows, or use the various http endpoints as described in this document.

.. code-block:: php

   <?php
   use Mautic\MauticApi;
   use Mautic\Auth\ApiAuth;

   $initAuth = new ApiAuth();
   $auth     = $initAuth->newAuth($settings);
   $apiUrl   = "https://example.com";
   $api      = new MauticApi();
   $filesApi = $api->newApi("files", $auth, $apiUrl);

.. vale off

Get list of files
*****************

.. vale on

.. code-block:: php

   <?php

   // Get list of root media/images directory:
   $files = $filesApi->getList();

   // Get list of some sub-directory (flags in this case) of media/images:
   $filesApi->setFolder('images/flags');
   $files = $filesApi->getList();

   // Get list of root media/files directory where the asset files are stored:
   $files = $filesApi->setFolder('assets');
   $files = $filesApi->getList();

.. vale off

**HTTP Request**

.. vale on

``GET /files/images`` to get root images directory
``GET /files/images?subdir=flags`` to get images/flags directory
``GET /files/assets`` to get root Assets directory

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {  
     "files":{  
       "3":"0b0f20185251d1c0cd5ff17950213fc9.png",
       "4":"0f530efdf837d3005bd2ab81cc30e878.jpeg",
       "5":"162a694f4101cb06c27c0a0699bd87c4.png",
       "6":"16ada2e2ecfa3f1d8cbb5d633f0bd8c6.png"
     }
   }

**Response Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``files``
     - array
     - List of requested files and directories

.. vale off

Create File
***********

.. vale on

.. code-block:: php

   <?php
   $data = array(
       'file' => dirname(__DIR__).'/'.'mauticlogo.png' // Must be a path to an existing file
   );

   // Create a file in root media/images directory:
   $response = $fileApi->create($data);

   // Create a file in some sub-directory (flags in this case) of media/images:
   $filesApi->setFolder('images/flags');
   $response = $fileApi->create($data);

   // Create a file in media/files directory where the asset files are stored:
   $files = $filesApi->setFolder('assets');
   $response = $fileApi->create($data);

Creates a file. The file gets sent through a regular POST files array like a browser sends it during file upload.

.. vale off

**HTTP Request**

.. vale on

``POST /files/DIR/new``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {  
     "file":{  
       "link":"http:\/\/yourmautic\/media\/images\/2b912b934dd2a4da49a226d0bf68bfea.png",
       "name":"2b912b934dd2a4da49a226d0bf68bfea.png"
     }
   }

**Response Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``link``
     - string
     - Appears only for files in image directory, not for Assets
   * - ``name``
     - string
     - File name of newly created file

.. vale off

Delete File
***********

.. vale on

.. code-block:: php

   <?php
   // Delete a file from root media/images directory:
   $response = $fileApi->delete($fileName);

   // Delete a file from some sub-directory (flags in this case) of media/images:
   $filesApi->setFolder('images/flags');
   $response = $fileApi->delete($fileName);

   // Delete a file from media/files directory where the asset files are stored:
   $files = $filesApi->setFolder('assets');
   $response = $fileApi->delete($fileName);

Delete a file.

.. vale off

**HTTP Request**

.. vale on

``DELETE /files/DIR/FILE/delete``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "success": true
   }
