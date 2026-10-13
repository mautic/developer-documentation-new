Implementing variant - A/B test - support to entities
#####################################################

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Mautic provides helper methods for creating variants of an entity, which is especially useful for A/B testing. Use the interfaces and traits below to add variant support to your Plugin's entities.

.. vale off

VariantInterface
****************

.. vale on

The ``\Mautic\CoreBundle\Entity\VariantInterface`` entity interface ensures an entity has everything Mautic needs to handle its variants correctly.

.. vale off

VariantEntityTrait
******************

.. vale on

The ``\Mautic\CoreBundle\Entity\VariantEntityTrait`` trait provides the properties needed to define an entity's relationship to other items. In the entity's ``loadMetadata()`` method, call ``$this->addVariantMetadata()``.

.. vale off

VariantModelTrait
*****************

.. vale on

The ``\Mautic\CoreBundle\VariantModelTrait`` trait provides the ``preVariantSaveEntity()``, ``postVariantSaveEntity()``, and ``convertVariant()`` methods. Call ``preVariantSaveEntity()`` before ``saveEntity()``, then call ``postVariantSaveEntity()`` afterwards, as in the following example:

.. code-block:: php

   <?php
   // plugins/HelloWorldBundle/Model/WorldModel.php

   // Reset A/B test if applicable
   $variantStartDate = new \DateTime();
   // setVariantHits is the stat tracker property for this variant
   $resetVariants    = $this->preVariantSaveEntity($entity, ['setVariantHits'], $variantStartDate);

   parent::saveEntity($entity, $unlock);

   $this->postVariantSaveEntity($entity, $resetVariants, $entity->getRelatedEntityIds(), $variantStartDate);

.. vale off

VariantMigrationTrait
*********************

.. vale on

To generate schema that matches the entity, use the ``\Mautic\CoreBundle\Doctrine\VariantMigrationTrait`` trait and call ``$this->addVariantSchema()``.

.. vale off

Translated entity Form
**********************

.. vale on

Add a ``variantParent`` field as shown in the following example. Here, the controller sets the ``variantParent`` value because someone clicked an 'Add A/B Test' button. Your Plugin might need a select list rather than a hidden field, so adapt the code to your needs.

.. code-block:: php

   <?php
   // plugins/HelloWorldPlugin/Form/Type/WorldType.php

   $transformer = new \Mautic\CoreBundle\Form\Transformer\IdToEntityModelTransformer($this->em, 'HelloWorldBundle:World');
   $builder->add(
       $builder->create(
           'variantParent',
           'hidden'
       )->addModelTransformer($transformer)
   );
