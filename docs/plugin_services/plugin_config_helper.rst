Plugin config helper
####################

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Use ``Mautic\CoreBundle\Helper\BundleHelper`` to read the configuration array declared in a Plugin's ``Config/config.php`` file. Inject the helper into your service:

.. code-block:: php

    <?php

    use Mautic\CoreBundle\Helper\BundleHelper;

    final class ExampleService
    {
        public function __construct(private BundleHelper $bundleHelper)
        {
        }

        public function readMenu(): array
        {
            return $this->bundleHelper->getBundleConfig('HelloWorldBundle', 'menu', true);
        }
    }

``getBundleConfig(string $bundleName, string $configKey = '', bool $includePlugins = false)`` returns the requested section of a bundle or Plugin's configuration. Omit ``$configKey`` to return the whole configuration array. The method throws an exception when the bundle or the requested key doesn't exist. ``BundleHelper`` also provides ``getMauticBundles()`` and ``getPluginBundles()`` to list the registered bundles and Plugins.