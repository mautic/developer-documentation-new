Marketplace
###########

Mautic 4 comes with a Marketplace directly in the Mautic administration user interface and command line interface as well.

- **Mautic 4.0.0** introduced the read-only Marketplace, which only lists available Plugins. Installing Plugins isn't possible in this version.
- **Mautic 4.2.0** introduced the ability to install and remove Plugins through the Marketplace.

Todo (SCREENSHOTS) add screenshots here.

Getting your Plugin listed in the Marketplace
*********************************************

There are two steps involved in listing your Plugin in the Marketplace:

1. Create and test your Plugin locally - see Todo (LINK) for more details.
2. :doc:`Prepare your Plugin for listing in the Marketplace <./listing>` 

Marketplace under the hood
**************************

The Marketplace uses Packagist and Composer v2 under the hood. Packagist's API lists the Mautic Plugins and finds the Plugin details. Composer v2 installs and updates the Plugins. Composer takes care of the dependencies of your Plugin, and also compatibility with different Mautic and PHP versions.