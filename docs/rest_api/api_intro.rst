Getting started with REST API
#############################

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. But you can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Mautic provides a REST API to manipulate and retrieve information about various entities in Mautic.

.. warning::

   All Mautic API endpoints require an OAuth1a signature or an OAuth2 access token.

Error handling
**************

If there's an OAuth error, you should see a JSON-encoded array similar to:

.. code-block:: JSON

   {
      "error": "invalid_grant",
      "error_description": "The access token provided has expired."
   }

If a system error occurs, you should see a JSON-encoded array similar to the example below:

.. code-block:: JSON

   {
      "error": {
        "message": "You do not have access to the requested area/action.",
        "code": 403
      }
   }

Mautic version verification
***************************

If your API service supports multiple Mautic versions with different features, you need to verify the Mautic version you're communicating with. Since Mautic ``2.4.0``, the version number appears in all API response headers under the name ``Mautic-Version``.

You can retrieve the Mautic version using the Mautic PHP API library:

.. code-block:: text

   // Make any API request:
   $api = $this->getContext('contacts');
   $response = $api->getList('', 0, 1);

   // Get the version number from the response header:
   $version = $api->getMauticVersion();

The ``$version`` is in a semantic versioning format of ``[major].[minor].[patch]`` - for example, ``2.4.0``. If you try it on the latest GitHub version, the version has a suffix ``-dev``, such as ``2.5.1-dev``.

API endpoints
*************

All responses are JSON encoded.

The base API endpoint is ``https://your-mautic.com/api``.

.. vale off

Mautic API Library
******************

.. vale on

Mautic has a :xref:`Mautic API Library` that you can use in your PHP projects - **recommended**. Other languages need to use custom tools or a third-party library to handle OAuth or request processing.

Install via Composer
--------------------

To install using Composer, run ``composer require mautic/api-library``.

Install manually
----------------

Download :xref:`API library package` from GitHub, extract it, then include the following code in your project and change the path if needed:

.. code-block:: PHP

   require_once __DIR__ . '/lib/Mautic/MauticApi.php';

.. note::

   Refer to the README in the GitHub repository for further instructions on using the library, or review the code examples throughout this documentation.

API rate limiter
****************

You can configure the rate limiter cache in ``local.php``. The default configuration uses the filesystem as follows:

.. code-block:: PHP

   api_rate_limiter_cache => [ 
      'type'      => 'file_system',
   ],

You can configure whatever cache you want as described in :xref:`DoctrineCacheBundle docs` or configure a ``memcached`` server as below:

.. code-block::

   'api_rate_limiter_cache' => [
      'memcached' => [
         'servers' =>
         [
            [
               'host' => 'localhost',
               'port' => 11211
            ]
         ]
      ]
   ],