.. It is a reference only page, not a part of doc tree.

:orphan:

.. vale off

Builder Integrations
####################

.. vale on

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Builders can register itself as a "builder" for Email and/or Landing Pages.

----

.. vale off

Register the Integration as a Builder
*************************************

.. vale on

Register the Integration or support class as a service in the Plugin's ``Config/services.php``. Mautic's ``autoconfigure()`` setting tags any service implementing ``\Mautic\IntegrationsBundle\Integration\Interfaces\BuilderInterface`` with ``mautic.builder_integration``, so you don't need to tag it manually.

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/Config/services.php

    declare(strict_types=1);

    use Mautic\CoreBundle\DependencyInjection\MauticCoreExtension;
    use Symfony\Component\DependencyInjection\Loader\Configurator\ContainerConfigurator;

    return function (ContainerConfigurator $configurator): void {
        $services = $configurator->services()
            ->defaults()
            ->autowire()
            ->autoconfigure()
            ->public();

        $services->load('MauticPlugin\\HelloWorldBundle\\', '../')
            ->exclude('../{'.implode(',', MauticCoreExtension::DEFAULT_EXCLUDES).'}');
    };


The ``BuilderSupport`` class must implement::

    \Mautic\IntegrationsBundle\Integration\Interfaces\BuilderInterface

The only method currently defined for the interface is ``isSupported`` which should return a boolean if it supports the given feature. Currently, Mautic supports ``email`` and ``page (Landing Pages)``. This determines what Themes should list as an option for the given builder/feature.
