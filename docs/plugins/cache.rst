Cache
#####

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Symfony makes heavy use of a filesystem cache. When developing for Mautic, clearing the cache is a regular occurrence. By default, Mautic instances have the cache located in ``var/cache/ENV`` where ``ENV`` is the environment currently accessed - ``dev`` or ``prod``. To rebuild the cache, delete the relevant ``ENV`` folder within the cache directory, or run the Symfony command ``php bin/console cache:clear --env=ENV``. If a specific environment isn't passed to the command via ``--env=ENV``, Mautic uses the ``dev`` environment by default.


.. vale off

In the ``dev`` environment, Mautic doesn't cache translations, views, and assets. However, changes to these files require clearing the cache for them to take effect in the ``prod`` environment. Changes to Mautic config files, Symfony config files, etc., require clearing of the cache regardless of the environment.

.. vale on

The typical rule of thumb is, if Mautic isn't acting as you expect after making changes, try clearing your cache. If you get ``class could not be found`` or ``cannot redeclare class`` errors when using the ``cache:clear`` command, manually delete the ``var/cache/ENV`` folder - replacing ENV with the environment e.g ``dev`` or ``prod`` - then run the command and/or browse to the site to rebuild.

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
.. vale off

- ``mautic.cache.adapter.filesystem``
- ``mautic.cache.adapter.memcached``

.. code-block:: php
    
    'cache_adapter_memcached' => [
        'servers' => ['memcached://localhost'],
        'options' => [
            'compression' => true,
            'libketama_compatible' => true,
            'serializer' => 'igbinary',
        ],
    ],
    
- ``mautic.cache.adapter.redis``

Redis configuration in ``local.php``:

.. code-block:: PHP
    
    'cache_adapter_redis' => [
        'dsn' => 'redis://localhost:6379/0',
        'options' => [
            'lazy' => false,
            'persistent' => 0,
            'persistent_id' => null,
            'timeout' => 30,
            'read_timeout' => 0,
            'retry_interval' => 0
        ],
    ],
    
In order to use another adapter, just set it up as a service.

Clearing the cache
------------------

The ``cache:clear`` command clears Mautic's cache. Use this command:

.. code-block:: bash

    bin/console mautic:cache:clear

Migrating to CacheBundle in Mautic 8
************************************

Mautic 8 removes the deprecated ``CacheStorageHelper``. Developers who inject it, extend ``Mautic\PluginBundle\Integration\AbstractIntegration``, or subscribe to Dashboard Widget events must update their code as shown here.

Replacing CacheStorageHelper
============================

Mautic 8 removes the ``mautic.helper.cache_storage`` service and the ``Mautic\CoreBundle\Helper\CacheStorageHelper`` class. Inject ``Mautic\CacheBundle\Cache\CacheProviderInterface`` — the same provider registered as the ``mautic.cache.provider`` service — instead, and call ``getSimpleCache()`` to get the PSR-16 cache. The ``get()``, ``set()``, ``has()``, and ``delete()`` methods keep the same signatures.

.. warning::

   Two behaviors change with the new provider:

   * A cache miss now returns ``null`` instead of ``false``, so any ``false === $value`` checks must become ``null === $value``.
   * Cached data now lives in the adapter set by the ``cache_adapter`` parameter — filesystem by default — instead of the ``cache_items`` database table, so a cache clear now drops it. The ``cache_items`` table and ``Mautic\CoreBundle\Entity\Cache`` entity remain, but Mautic no longer writes to them.

See the :ref:`plugins/cache:Configuration` and :ref:`plugins/cache:Delivered adapters` sections for how to set up and override the adapter.

Before, in Mautic 7:

.. code-block:: php

    use Mautic\CoreBundle\Helper\CacheStorageHelper;

    class MyService
    {
        public function __construct(
            private CacheStorageHelper $cacheStorageHelper
        ) {
        }

        public function fetch(string $key)
        {
            $value = $this->cacheStorageHelper->get($key);

            if (false === $value) {
                // Rebuild and store the value.
            }

            return $value;
        }
    }

After, in Mautic 8:

.. code-block:: php

    use Mautic\CacheBundle\Cache\CacheProviderInterface;

    class MyService
    {
        public function __construct(
            private CacheProviderInterface $cacheProvider
        ) {
        }

        public function fetch(string $key)
        {
            $cache = $this->cacheProvider->getSimpleCache();
            $value = $cache->get($key);

            if (null === $value) {
                // Rebuild and store the value.
            }

            return $value;
        }
    }

Integration cache
=================

``Mautic\PluginBundle\Integration\AbstractIntegration::getCache()`` now returns ``Psr\SimpleCache\CacheInterface``. It previously returned ``Mautic\CoreBundle\Helper\CacheStorageHelper``. Its second constructor argument is now ``Mautic\CacheBundle\Cache\CacheProviderInterface``.

Keys stay namespaced per Integration, so existing calls such as ``$this->getCache()->get($key)`` and ``$this->cache->set(...)`` keep working unchanged. The one exception is the change where a cache miss now returns ``null`` instead of ``false``, described in the :ref:`plugins/cache:Replacing CacheStorageHelper` section, which now applies here too.

The base method signature is now:

.. code-block:: php

    public function getCache(): \Psr\SimpleCache\CacheInterface
    {
        // ...
    }

    // Existing usage stays valid:
    $fields = $this->getCache()->get('leadFields');

WidgetDetailEvent changes
=========================

These changes apply to subscribers of the dispatched ``Mautic\DashboardBundle\Event\WidgetDetailEvent``:

* The ``setCacheDir()`` method is removed; the legacy filesystem Widget cache is gone.
* ``WidgetDetailEvent`` now requires the ``$cacheProvider`` constructor argument and types it ``Mautic\CacheBundle\Cache\CacheProviderTagAwareInterface`` — previously ``?CacheProviderTagAwareInterface $cacheProvider = null``.
* The ``setTemplateData()`` method no longer accepts the second ``$skipCache`` parameter. The signature is now ``setTemplateData(array $templateData)``.

``WidgetDetailEvent`` caches Widget data only through ``CacheProviderTagAwareInterface``.

Before, in Mautic 7:

.. code-block:: php

    use Mautic\CacheBundle\Cache\CacheProviderTagAwareInterface;

    class MyDashboardWidgetSubscriber
    {
        public function __construct(
            ?CacheProviderTagAwareInterface $cacheProvider = null
        ) {
        }

        public function onWidgetDetail(WidgetDetailEvent $event): void
        {
            $event->setCacheDir($this->cacheDir);
            $event->setTemplateData($templateData, $skipCache);
        }
    }

After, in Mautic 8:

.. code-block:: php

    use Mautic\CacheBundle\Cache\CacheProviderTagAwareInterface;

    class MyDashboardWidgetSubscriber
    {
        public function __construct(
            CacheProviderTagAwareInterface $cacheProvider
        ) {
        }

        public function onWidgetDetail(WidgetDetailEvent $event): void
        {
            $event->setTemplateData($templateData);
        }
    }

