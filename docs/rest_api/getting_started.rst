Getting started
###############

Mautic provides several ``REST API`` endpoints that you can use. In the navigation menu on the left, you can find the available endpoints.

.. warning:: 

    By default, Mautic's ``REST API`` isn't enabled. The Mautic administrator can enable the API in the Mautic UI under ``Configuration -> API Settings``, or by setting ``'api_enabled' => 1`` in ``app/config/local.php`` directly.

.. note:: 

    Mautic has an API library available for PHP. You can :xref:`find it on GitHub<Mautic API Library>`.

Authentication
**************

Mautic supports Basic Authentication and OAuth2. Please see :ref:`Authentication` for more details.

Error handling
**************

In case of OAuth errors, the response is a JSON encoded array similar to:

.. code-block:: json

    {
        "error": "invalid_grant",
        "error_description": "The access token provided has expired."
   }

In case of system errors, the response is a JSON encoded array similar to:

.. code-block:: json

    {
       "error": {
           "message": "You do not have access to the requested area/action.",
           "code": 403
       }
   }

.. vale off

Mautic version check
********************

.. vale on

In case your API service wants to support several Mautic versions with different features, you might need to validate the version of Mautic you communicate with. Since Mautic 2.4.0, the version number is in all API response headers. The header name is ``Mautic-Version``.

With Mautic's PHP API library, you can get the Mautic version like this:

.. code-block:: php

    <?php

    // Make any API request:
    $api = $this->getContext('contacts');
    $response = $api->getList('', 0, 1);

    // Get the version number from the response header:
    $version = $api->getMauticVersion();

``$version`` is in a semantic versioning format: ``[major].[minor].[patch]``. For example: ``2.4.0``. If you'll try it on the latest GitHub version, the version has ``-dev`` at the end. Like ``2.5.1-dev``.

.. vale off

API Rate limiter cache
**********************

.. vale on

You can configure rate limiter cache in ``config/local.php``, which defaults to the filesystem:

.. code-block:: php

    <?php

    'api_rate_limiter_cache' => [ 
        'adapter' => 'cache.adapter.filesystem',
    ],

You can also configure a ``memcached`` server for improved performance, like this:

.. code-block:: php

    <?php

    'api_rate_limiter_cache' => [
        'adapter'  => 'cache.adapter.memcached',
        'provider' => 'memcached://memcached.local:12345'
    ],

For more examples of supported cache adapters, please visit the :xref:`Symfony Cache Documentation<Symfony Cache>`.
