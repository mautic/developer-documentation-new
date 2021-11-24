Getting started with Plugins
==========================================================

Plugins are Symfony bundles that can extend the functionality of Mautic. They can be very simple or complex and have access to leverage nearly all that Symfony offers. Just as as reminder, the basics are covered in this documentation. If more advanced processes are required, the :xref:`Symfony 4 documentation` will be a valuable resource.

.. note:: Mautic plugins are located in the plugins/ directory and must be namespaced with ``MauticPlugin\[Plugin Folder Name]\``.

.. warning:: Avoid using Symfony's ability to override core classes with hacked versions in a plugin. Doing so creates compatibility challenges with future upgrades and/or may conflict with another plugin that is doing the same thing. It is recommended instead that you build into core the support you need to enable what you are wanting to accomplish with your plugin then contribute it to the :xref:`project as a PR<Contributing to Mautic>`.