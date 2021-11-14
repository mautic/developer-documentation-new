===========
Marketplace
===========

Mautic 4 comes with a Marketplace directly in the Mautic administration user interface and command line interface as well.

- In **Mautic 4.0.0**, we introduced the read-only Marketplace which only lists available plugins. Installing plugins is not possible in this version.
- In **Mautic 4.1.0**, we introduced the ability to install and remove plugins through the Marketplace.

TODO add screenshots here.

Getting your plugin listed in the Marketplace
==============================================

There are basically two steps involved in listing your plugin in the Marketplace:

1. Create and test your plugin locally (see LINK for more details)
2. :doc:`Prepare your plugin for listing in the Marketplace <./listing>` 

Marketplace under the hood
===========================

The Marketplace uses Packagist and Composer v2 under the hood. Packagist's API is used to list the Mautic plugins and find the plugin details. Composer v2 is used to install and update the plugins. Composer will take care of the dependencies of your plugin and also compatibility with different Mautic and PHP versions.