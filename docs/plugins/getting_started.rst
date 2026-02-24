Getting started with Plugins
############################

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Plugins are Symfony bundles that can extend the capability of Mautic. They can be very simple or complex and have access to leverage nearly all that Symfony offers. Just as a reminder, this covers the basics. If you require more advanced features of Symfony, the :xref:`Symfony documentation` is a valuable resource.

.. note:: Plugins install into the ``plugins/`` directory. Namespace all classes with ``MauticPlugin\[Plugin Folder Name]\``.

.. warning:: Avoid using Symfony's ability to override core classes with hacked versions in a Plugin. Doing so creates compatibility challenges with future upgrades and/or may conflict with another Plugin that's doing the same thing. Rather, build into core the support you need to enable what you are wanting to accomplish with your Plugin then contribute it to the :xref:`project as a PR<Contributing to Mautic>`.