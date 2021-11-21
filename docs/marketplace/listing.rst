===================================
Listing a Plugin in the Marketplace
===================================

.. note::
    Do you already have a Plugin that you developed for previous versions of Mautic? Please see the :ref:`Updating existing Plugins for usage with the Marketplace` section below.

Preparing your Plugin for the Marketplace
=========================================

.. warning::
    It's critical that you follow the steps below carefully. Things like typos in the bundle name can crash Mautic and require users to issue some command line commands to get back into a working state.

When you create a Plugin, there's a few requirements to verify before it can be listed in the Mautic Marketplace.

Step 1: checking your composer.json file
----------------------------------------

The first important step is to check whether your ``composer.json`` file has all the required information in it.

Here's an example composer.json file:

.. code-block:: json

    {
        "name": "example-vendor/plugin-example",
        "description": "Example Plugin",
        "type": "mautic-plugin",
        "version": "1.0",
        "keywords": ["mautic","plugin","integration"],
        "extra": {
            "install-directory-name": "ExampleBundle"
        },
        "require": {
            "php": ">=7.4.0 <8.1",
            "ext-zip": "^1.15",
            "mautic/core-lib": "^4.0"
        }
    }

In addition to the information you already have in the composer.json for your Plugin, please add:

- ``type`` must have value ``mautic-plugin``. The Marketplace is filtering PHP packages by this tag. It's required to show up in the Marketplace.
- ``extra.install-directory-name`` specifies the directory name for the bundle. Correct directory name is important for PSR4 autoloading. It must be the same as in the namespace in your PHP classes.
- ``require.php`` be sure to specify the PHP version range that you test the Plugin against. Ideally it should be the same as the Mautic's :xref:`Mautic supported PHP versions`. Don't allow users to install the Plugin on versions that are not supported.
- ``require.ext-*`` if your Plugin require some PHP extension, please list them in the require section too. As servers can have a wide variety of extensions enabled, this ensures that the correct extensions are available.
- ``require.mautic/core-lib`` it's important to specify which Mautic versions your Plugin supports. Include only the versions you or your community have tested and confirmed the Plugin works with.

Step 2: verify best practices
----------------------------

There's a few things which are highly recommend when creating Plugins for Mautic. Please refer to the :doc:`./best_practices` page for more details.

Step 3: publish to Composer
---------------------------

When the composer.json is ready, follow the :xref:`Packagist` section directly in Packagist.

Step 4: apply for the allowlist
-------------------------------

While the Mautic Marketplace is still in beta, you'll have to apply for our allowlist in order to show up in the Marketplace. It is expected that the Marketplace will move from beta to stable release with Mautic 4.2 in February 2022, after which the allowlist may be deprecated in favour of a blocklist. Please refer to the :doc:`./allowlist_what_and_why` page for more details.

Updating existing Plugins for usage with the Marketplace
========================================================

If you required ``mautic/composer-plugin`` in your plugin's dependencies in the past, please remove it. Support for Mautic plugins is now built into Composer, so you only have to set the type to ``mautic-plugin`` and Composer will automatically install your plugin into the ``plugins`` folder.

Next to that, if you built your plugin for Mautic 3 originally, please check the :xref:`UPGRADE-4.0.md guide` for the breaking changes in Mautic 4.

When you're done, you can go back to the :ref:`Preparing your plugin for the Marketplace` section in this document and proceed from there.