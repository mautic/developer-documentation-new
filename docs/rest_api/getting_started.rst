Getting started
###############

Mautic provides several REST API endpoints. You can find the available endpoints in the navigation menu on the left.

.. warning:: 

   Mautic turns off the REST API by default. The Mautic administrator can turn on the API in the Mautic UI under **Configuration > API Settings**, or by setting ``'api_enabled' => 1`` in ``app/config/local.php`` directly.

.. note:: 

   Mautic provides an API library for PHP. See the :xref:`Mautic API Library` for more information.

Authentication
**************

Mautic supports Basic Authentication and OAuth2. Please see :doc:`authentication` for more details.

Error handling
**************

OAuth errors result in a JSON encoded array. For example:

.. code-block:: json

    {
        "error": "invalid_grant",
        "error_description": "The access token provided has expired."
   }

System errors return a JSON encoded array. For example:

.. code-block:: json

    {
       "error": {
           "message": "You do not have access to the requested area/action.",
           "code": 403
       }
   }

Mautic version verification
***************************

To support multiple Mautic versions with different features, your API service may need to validate the Mautic version it communicates with. Since Mautic ``2.4.0``, the version number is in all API response headers. The header name is ``Mautic-Version``.

With the Mautic PHP API library, you can retrieve the version as follows:

.. code-block:: php

    <?php

    // Make any API request:
    $api = $this->getContext('contacts');
    $response = $api->getList('', 0, 1);

    // Get the version number from the response header:
    $version = $api->getMauticVersion();

The ``$version`` variable uses a semantic versioning format: ``[major].[minor].[patch]``, for example, ``2.4.0``. If you try it on the latest GitHub version, the version has ``-dev`` at the end, such as ``2.5.1-dev``.

API rate limiter cache
**********************

You can configure rate limiter cache in ``config/local.php``, which defaults to the filesystem:

.. code-block:: php

    <?php

    'api_rate_limiter_cache' => [ 
        'adapter' => 'cache.adapter.filesystem',
    ],

You can also configure a ``memcached`` server for improved performance:

.. code-block:: php

    <?php

    'api_rate_limiter_cache' => [
        'adapter'  => 'cache.adapter.memcached',
        'provider' => 'memcached://memcached.local:12345'
    ],

For more examples of supported cache adapters, please visit the :xref:`Symfony Cache Documentation`.