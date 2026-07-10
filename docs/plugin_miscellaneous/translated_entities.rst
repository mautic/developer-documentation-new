Implementing translation support to entities
############################################

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Mautic provides helper interfaces and traits that add translated-content support to an entity. Use them so your entity can store a language, relate to a translation parent, and resolve the correct translation at runtime.

``Mautic\CoreBundle\Entity\TranslationEntityInterface``
    Implement this interface to declare that an entity supports translations. It defines the methods Mautic needs to handle an entity's translations correctly.

``Mautic\CoreBundle\Entity\TranslationEntityTrait``
    This trait provides the properties and methods that define an entity's language and its relationships to its translation parent and children. In the entity's ``loadMetadata()`` method, call ``self::addTranslationMetadata($builder, self::class)`` to map the translation columns and relationships.

``Mautic\CoreBundle\Model\TranslationModelTrait``
    Use this trait in the entity's model. It provides ``getTranslatedEntity()``, which determines the entity to use as the translation based on the Contact and/or the request's ``Accept-Language`` header, and ``postTranslationEntitySave()``, which you call at the end of the model's ``saveEntity()`` method to persist the translation relationship.

.. vale off

Translated entity Form
**********************

.. vale on

Add ``language`` and ``translationParent`` fields to the entity's Form type so Users can set an entity's language and link it to a translation parent. Use an ``IdToEntityModelTransformer`` to convert the submitted parent ID back to an entity:

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/Form/Type/WorldType.php

    use Mautic\CoreBundle\Form\DataTransformer\IdToEntityModelTransformer;
    use Symfony\Component\Form\Extension\Core\Type\LocaleType;

    $transformer = new IdToEntityModelTransformer($this->entityManager, World::class);

    $builder->add(
        $builder->create('translationParent', WorldListType::class, [
            'label'       => 'mautic.core.form.translation_parent',
            'label_attr'  => ['class' => 'control-label'],
            'attr'        => [
                'class'   => 'form-control',
                'tooltip' => 'mautic.core.form.translation_parent.help',
            ],
            'required'    => false,
            'multiple'    => false,
            'placeholder' => 'mautic.core.form.translation_parent.empty',
            'top_level'   => 'translation',
            'ignore_ids'  => [(int) $options['data']->getId()],
        ])->addModelTransformer($transformer)
    );

    $builder->add('language', LocaleType::class, [
        'label'      => 'mautic.core.language',
        'label_attr' => ['class' => 'control-label'],
        'attr'       => [
            'class'   => 'form-control',
            'tooltip' => 'mautic.page.form.language.help',
        ],
        'required'   => false,
    ]);
