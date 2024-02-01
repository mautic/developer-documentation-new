Plugin dependencies
###################

You have a couple of options when it comes to dependencies.

The first is to include dependencies with your distributable Plugin package. However, this isn't recommended as other Plugins may also include the same dependencies and conflict with your own.

The recommended approach is to use Composer and make the Plugin available through the new Marketplace.

:ref: `marketplace/listing:Preparing your Plugin for the Marketplace` by leveraging :xref:`Mautic's Composer plugin`. For detailed instructions, refer to the :doc:`/marketplace/listing`.