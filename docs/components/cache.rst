Cache
#####

Symfony makes heavy use of a filesystem cache. When developing for Mautic, clearing the cache is a regular occurrence. By default, Mautic instances have the cache located in ``var/cache/ENV`` where ``ENV`` is the environment currently accessed (``dev`` or ``prod``). To rebuild the cache, delete the relevant ``ENV`` folder within the cache directory, or run the Symfony command ``php bin/console cache:clear --env=ENV``. If a specific environment isn't passed to the command via ``--env=ENV``, Mautic uses the ``dev`` environment by default.


.. vale off

In the ``dev`` environment, Mautic doesn't cache translations, views, and assets. However, changes to these files require clearing the cache for them to take effect in the ``prod`` environment. Changes to Mautic config files, Symfony config files, etc., require clearing of the cache regardless of the environment.

.. vale on

The typical rule of thumb is, if Mautic isn't acting as you expect after making changes, try clearing your cache. If you get ``class could not be found`` or ``cannot redeclare class`` errors when using the ``cache:clear`` command, manually delete the ``var/cache/ENV`` folder then run the command and/or browse to the site to rebuild.

Cache bundle
************

Enables PSR-6 and PSR-16 caching. Check :xref:`Symfony Cache Component`

Namespace versus tag
====================

This bundle introduces tags to the cache. All its adapters are fully tag aware which makes the use of namespace obsolete for daily use.

Previously, if you wanted to keep control on cache section and didn't want to hold the index of all keys to clear, you would have to use namespace.

The main disadvantage of this approach is that Mautic creates a new adapter for each namespace.

From Symfony 3.4, the cache uses tag-aware adapters. If you want to clear all records related to your Bundle or Component, you just need to tag them.

.. code-block:: php
    /** @var CacheProvider $cache */
    $cache = $this->get('mautic.cache.provider');
    /** @var CacheItemInterface $item */
    $item = $cache->getItem('test_tagged_Item');
    $item->set('yesa!!!');
    $item->tag(['firstTag', 'secondTag']);
    $item->expiresAfter(20000);
All you need to do now is to clear all tagged items:

.. code-block:: php
    $cache->invalidateTags(['firstTag']);
Pools clearing
==============

Removing cache items
--------------------

Cache Pools include methods to delete a cache item, some of them, or all of them. The most common is ``Psr\\Cache\\CacheItemPoolInterface::deleteItem``, which deletes the cache item identified by the given key.

.. code-block:: php
    $isDeleted = $cache->deleteItem('user_'.$userId);
Use the ``Psr\\Cache\\CacheItemPoolInterface::deleteItems`` method to delete several cache items simultaneously - it returns true only if all the items have been deleted, even when any or some of them don't exist.

Configuration
-------------

Plugins come preconfigured to utilize filesystem caching.

These are the default settings:

.. code-block:: php
    'cache_adapter' => 'mautic.cache.adapter.filesystem',
    'cache_prefix' => 'app',
    'cache_lifetime' => 86400
They can be overridden in ``local.php`` like this:

.. code-block:: php
    'cache_adapter'  => 'mautic.cache.adapter.redis',
    'cache_prefix'   => 'app_cache',
    'cache_lifetime' => 86400,
Delivered adapters
------------------

- ``mautic.cache.adapter.filesystem``
- ``mautic.cache.adapter.memcached``

.. code-block:: php
    'memcached' => [
        'servers' => ['memcached://localhost'],
        'options' => [
            'compression' => true,
            'libketama_compatible' => true,
            'serializer' => 'igbinary',
        ],
    ],
- ``mautic.cache.adapter.redis``

Redis configuration in ``local.php``:

.. code-block:: php
    'redis' => [
        'dsn' => 'redis://localhost',
        'options' => [
            'lazy' => false,
            'persistent' => 0,
            'persistent_id' => null,
            'timeout' => 30,
            'read_timeout' => 0,
            'retry_interval' => 0,
        ],
    ],
In order to use another adapter, just set it up as a service.

Clearing the cache
------------------

When the ``cache:clear`` command is run, Mautic's cache is cleared. The cache can be cleared by running:

.. code-block:: bash
    bin/console mautic:cache:clear

