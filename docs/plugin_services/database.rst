Database or entity manager
##########################

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Doctrine provides both an ORM and a DBAL layer. To work with a bundle's repositories and entities, use the entity manager by injecting ``Doctrine\ORM\EntityManagerInterface`` into your service:

.. code-block:: php

    <?php

    use Doctrine\ORM\EntityManagerInterface;

    final class ExampleService
    {
        public function __construct(private EntityManagerInterface $entityManager)
        {
        }

        public function incrementVisits(): void
        {
            $repository = $this->entityManager->getRepository(World::class);
            $worlds     = $repository->getEntities();

            foreach ($worlds as $world) {
                $world->upVisitCount();
            }

            $repository->saveEntities($worlds);
        }
    }

For direct database access, inject the DBAL connection, ``Doctrine\DBAL\Connection``, instead. In a controller, you can also reach the entity manager through the injected ``Doctrine\Persistence\ManagerRegistry``.