Files
#####

.. vale off

.. note::

  The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

  If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

  Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Use this endpoint to work with files of images and Assets.

.. note::

   Assets doesn't have nor support subdirectories.

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
   $filesApi = $api->newApi("files", $auth, $apiUrl);

.. vale off

Get List of files
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

.. code-block:: json

   {
     "files":{
       "3":"0b0f20185251d1c0cd5ff17950213fc9.png",
       "4":"0f530efdf837d3005bd2ab81cc30e878.jpeg",
       "5":"162a694f4101cb06c27c0a0699bd87c4.png",
       "6":"16ada2e2ecfa3f1d8cbb5d633f0bd8c6.png"
     }
   }

Get a list of files.

.. vale off

**HTTP Request**

``GET /files/images`` to get root images directory

``GET /files/images?subdir=flags`` to get images/flags directory

``GET /files/assets`` to get root assets directory

**Response**

.. vale on

``Expected Response Code: 200``

See JSON code example.

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
   $response = $filesApi->create($data);

   // Create a file in some sub-directory (flags in this case) of media/images:
   $filesApi->setFolder('images/flags');
   $response = $filesApi->create($data);

   // Create a file in media/files directory where the asset files are stored:
   $files = $filesApi->setFolder('assets');
   $response = $filesApi->create($data);

Creates a file. Mautic sends the file through a standard POST files array, the same way a browser sends files during upload.

.. vale off

**HTTP Request**

.. vale on

``POST /files/DIR/new``

.. vale off

**Response**

.. vale on

``Expected Response Code: 200``

.. code-block:: json

   {
     "file":{
       "link":"https://example.com/media/images/2b912b934dd2a4da49a226d0bf68bfea.png",
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
   $response = $filesApi->delete($fileName);

   // Delete a file from some sub-directory (flags in this case) of media/images:
   $filesApi->setFolder('images/flags');
   $response = $filesApi->delete($fileName);

   // Delete a file from media/files directory where the asset files are stored:
   $files = $filesApi->setFolder('assets');
   $response = $filesApi->delete($fileName);

Delete a file.

.. vale off

**HTTP Request**

.. vale on

``DELETE /files/DIR/FILE/delete``

.. vale off

**Response**

.. vale on

``Expected Response Code: 200``

.. code-block:: json

   {
     "success": true
   }
