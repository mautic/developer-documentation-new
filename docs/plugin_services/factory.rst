Factory
#######

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

.. warning::

   ``Mautic\Factory\MauticFactory`` is removed in Mautic 7. It was deprecated in Mautic 2.0 and removed in Mautic 3.0. Use dependency injection instead.

Earlier Mautic versions exposed a single ``MauticFactory`` service - available as ``$this->factory`` in controllers and models - that aggregated many dependencies. Mautic 7 relies on autowired dependency injection, so you inject the specific services you need directly through the constructor:

.. code-block:: php

    <?php

    use Doctrine\ORM\EntityManagerInterface;
    use Mautic\CoreBundle\Helper\CoreParametersHelper;
    use Mautic\CoreBundle\Helper\UserHelper;

    final class ExampleService
    {
        public function __construct(
            private EntityManagerInterface $entityManager,
            private CoreParametersHelper $coreParametersHelper,
            private UserHelper $userHelper,
        ) {
        }
    }

To resolve a model whose type isn't known until runtime, inject :doc:`Model factory</plugin_services/model_factory>` instead of the removed factory.
