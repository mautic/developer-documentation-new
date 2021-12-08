Entities and schema
=====================

Mautic uses :xref:`Doctrine ORM` to define the schema. Plugins define their schema using entity classes stored in its ``Entity`` directory. Schema is defined for the entity through Doctrine's :xref:`PHP static function mapping<Doctrine ORM PHP mapping>` or :xref:`annotations<Doctrine ORM annotations>`.

.. warning:: You use the PHP mapping or annotations. It cannot use a mix of the two.

Entity PHP static function mapping
-----------------------------------

You can build the schema through Doctrine's ``Doctrine\ORM\Mapping\Builder\ClassMetadataBuilder`` class. Refer to :xref:`Doctrine ORM PHP mapping` for methods available. Mautic also provides a decorated ``ClassMetadataBuilder`` class through ``Mautic\CoreBundle\Doctrine\Mapping\ClassMetadataBuilder`` that is described below.

.. code-block:: php

    <?php

    declare(strict_types=1);

    namespace Mautic\UserBundle\Entity;

    use Doctrine\ORM\Mapping as ORM;
    use Mautic\CoreBundle\Doctrine\Mapping\ClassMetadataBuilder;
    use Ramsey\Uuid\Uuid;

    class World
    {
        /**
         * @var string
         */
        private $uuid;

        /**
         * @var string
         */
        private $name;

        public function __construct()
        {
            $this->uuid = Uuid::uuid4()->toString();
        }

        public static function loadMetadata(ORM\ClassMetadata $metadata)
        {
            $builder = new ClassMetadataBuilder($metadata);

            $builder->setTable('worlds');

            $builder->addUuid();

            $builder->createField('name', 'string')
                ->length(191)
                ->build();
        }

        public function getUuid(): string
        {
            return $this->uuid;
        }

        public function getName(): string
        {
            return $this->name;
        }

        public function setName(string $name): void
        {
            $this->name = $name;
        }
    }


.. php:class:: Mautic\CoreBundle\Doctrine\Mapping\ClassMetadataBuilder

.. php:method:: addBigIntIdField()

    :returns:
    :returntype:

.. php:method:: addCategory()

    :returns:
    :returntype:

.. php:method:: addContact()

    :returns:
    :returntype:

.. php:method:: addDateAdded()

    :returns:
    :returntype:

.. php:method:: addField()

    :returns:
    :returntype:

.. php:method:: addId()

    :returns:
    :returntype:

.. php:method:: addIdColumns()

    :returns:
    :returntype:

.. php:method:: addIpAddress()

    :returns:
    :returntype:

.. php:method:: addNamedField()

    :returns:
    :returntype:

.. php:method:: addNullableField()

    :returns:
    :returntype:

.. php:method:: addPartialIndex()

    :returns:
    :returntype:

.. php:method:: addPublishDates()

    :returns:
    :returntype:

.. php:method:: addUuid()

    :returns:
    :returntype:

.. php:method:: createField()

    :returns:
    :returntype:

.. php:method:: createManyToMany()

    :returns:
    :returntype:

.. php:method:: createManyToOne()

    :returns:
    :returntype:

.. php:method:: createOneToMany()

    :returns:
    :returntype:

.. php:method:: createOneToOne()

    :returns:
    :returntype:

.. php:method:: isIndexedVarchar()

    :returns:
    :returntype:

Entity annotations
---------------------

You can choose to use annotations instead of the PHP static method. Refer to :xref:`Doctrine's documentation on available annotations<Doctrine ORM annotations>`.

.. code-block:: php

    <?php

    declare(strict_types=1);

    namespace Mautic\UserBundle\Entity;

    use Doctrine\ORM\Mapping as ORM;
    use Ramsey\Uuid\Uuid;

    /**
     * @ORM\Table (name="worlds")
     */
    class World
    {
        /**
         * @ORM\Column(type="guid")
         * @ORM\Id
         */
        private $id;

        /**
         * @ORM\Column(type="string", length=191)
         */
        private $name;

        public function __construct()
        {
            $this->id = Uuid::uuid4()->toString();
        }

        public function getId(): string
        {
            return $this->id;
        }

        public function getName(): string
        {
            return $this->name;
        }

        public function setName(string $name): void
        {
            $this->name = $name;
        }
    }


Plugin migrations
------------------

