===========
Marketplace
===========

Mautic 4 comes with a Marketplace directly in the Mautic administration user interface and command line interface as well.

- In **Mautic 4.0.0**, the read-only Marketplace was introduced, which only lists available plugins. Installing plugins isn't possible in this version.
- In **Mautic 4.1.0**, the ability to install and remove plugins through the Marketplace was introduced.

TODO add screenshots here.

Getting your Plugin listed in the Marketplace
==============================================

There are two steps involved in listing your Plugin in the Marketplace:

1. Create and test your Plugin locally - see LINK for more details.
2. :doc:`Prepare your Plugin for listing in the Marketplace <./listing>` 

Marketplace under the hood
===========================

The Marketplace uses Packagist and Composer v2 under the hood. Packagist's API lists the Mautic Plugins and finds the Plugin details. Composer v2 installs and updates the Plugins. Composer takes care of the dependencies of your Plugin, and also compatibility with different Mautic and PHP versions.