Plugin dependencies
=====================

You have a couple of options when it comes to dependencies.

The first is to include dependencies with your distributable plugin package. However, this isn't recommended as other plugins may also include the same dependencies and conflict with your own.

The recommended approach is to use Composer and make the plugin available through the new Marketplace.

Preparing your Plugin for the Marketplace by leveraging :xref:`Mautic's Composer plugin`. For detailed instructions, refer to the :ref:`Marketplace documentation<Step 1: checking your composer.json file>`.