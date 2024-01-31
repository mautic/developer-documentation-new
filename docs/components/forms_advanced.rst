Forms - advanced
################

Sometimes you might have more complex requirements for your Forms. You might already be aware that Mautic builds upon the Symfony framework, so there's lots of Form-related features available to you.
You can read more about this here: :xref:`Symfony 4 form classes`. This section highlights a few complex but common use cases:

- Custom Form Types that deviate from Symfony's wide array of standard Form types, like text fields, choice fields, etc.
- Data sanitizing
- Dynamic Form modification
- Data validation

.. vale off

Custom Form types
*****************

.. vale on

As stated in Symfony's documentation as referenced in the preceding section, Form type classes are the best way to go.
Mautic makes it easy to register :xref:`Form type services<Symfony 4 custom Form field type>` through the bundle's config file.
Refer to the :ref:`plugins/config:Service config items` section.

Data sanitizing
***************

Form data isn't automatically sanitized. Mautic provides a Form event subscriber to handle this. 

In your :xref:`Form type class<Symfony 4 form classes>`, register the ``Mautic\CoreBundle\Form\EventListener\CleanFormSubscriber`` event subscriber. 
 
The array provided to ``CleanFormSubscriber`` should contain the names of the Form Fields as keys and the values the masks to use to sanitize the data. Any unspecified Form Field uses the ``clean`` mask by default.

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/Form/Type/WorldType.php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\Form\Type;

    use Mautic\CoreBundle\Form\EventListener\CleanFormSubscriber;
    use Symfony\Component\Form\AbstractType;
    use Symfony\Component\Form\FormBuilderInterface;

    class WorldType extends AbstractType
    {
        public function buildForm(FormBuilderInterface $builder, array $options)
        {
            $builder->addEventSubscriber(
                new CleanFormSubscriber(
                    [
                        'content'    => 'html',
                        'customHtml' => 'html'
                    ]
                )
            );
        }
    }

.. vale off

Dynamic Form modification
*************************

.. vale on

If you need to manipulate a Form based on submitted data, use a Form event listener.
This is useful in cases like changing defined fields, adjust constraints, or changing select choices based on submitted values.
Refer to Symfony's documentation on this: :xref:`Symfony 4 dynamic form modification`

Data validation
***************

Review Symfony's Form validation documentation for a general overview: :xref:`Symfony 4 form validation`

There are two common means of validating Form data.

Using entity static callback
============================

If the underlying data of a Form is an Entity object you can define a static method ``loadValidatorMetadata`` in the Entity class.
This automatically gets called when Symfony is processing Form data.

A Form can also use :xref:`validation_groups<Symfony 4 Form validation groups>` to change the order of data to validate or only validate if certain criteria is true.
For example, only validate a password confirmation field if the first password field passes validation.
When registering a validation group in the Form type class, you can use a static callback to determine what validation groups Symfony should use.

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/Form/Type/WorldType.php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\Form\Type;

    use Symfony\Component\Form\AbstractType;
    use Symfony\Component\Form\Form;
    use Symfony\Component\Form\FormBuilderInterface;
    use Symfony\Component\OptionsResolver\OptionsResolver;
    use Symfony\Component\Validator\Constraints\NotBlank;
    use Symfony\Component\Validator\Mapping\ClassMetadata;

    class WorldType extends AbstractType
    {
        public function configureOptions(OptionsResolver $resolver)
        {
            $resolver->setDefaults(array(
                'data_class'        => 'MauticPlugin\HelloWorld\Entity\World',
                'validation_groups' => array(
                    'MauticPlugin\HelloWorld\Entity\World',
                    'determineValidationGroups',
                )
            ));
        }

        public static function loadValidatorMetadata(ClassMetadata $metadata)
        {
            $metadata->addPropertyConstraint(
                'name',
                new NotBlank(
                    array(
                        'message' => 'mautic.core.name.required'
                    )
                )
            );
            
            $metadata->addPropertyConstraint(
                'population', 
                new NotBlank(
                    array(
                        'message' => 'mautic.core.value.required',
                        'groups'  => array('VisitedWorld')
                    )
                
                )
            );
        }

        public static function determineValidationGroups(Form $form)
        {
            $data   = $form->getData();
            $groups = array('AllWorlds');

            if (!$data->getId() || ($data->getId() && $data->getVisitCount() > 0)) {
                $groups[] = 'VisitedWorld';
            }

            return $groups;
        }
    }


Using constraints
=================

A :xref:`Form type service<Symfony 4 custom Form field type>` can also register :xref:`Constraints<Symfony 4 Form constraints>` when defining the Form Fields.

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/Form/Type/WorldType.php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\Form\Type;

    use Symfony\Component\Form\AbstractType;
    use Symfony\Component\Form\Form;
    use Symfony\Component\Form\FormBuilderInterface;
    use Symfony\Component\Validator\Constraints\NotBlank;

    class WorldType extends AbstractType
    {
        public function buildForm(FormBuilderInterface $builder, array $options)
        {
            $builder->add(
                'name',
                'text',
                array(
                    'label'       => 'mautic.core.name',
                    'label_attr'  => array('class' => 'control-label'),
                    'attr'        => array(
                        'class'   => 'form-control'
                    ),
                    'constraints' => array(
                        new NotBlank(
                            array(
                                'message' => 'mautic.core.value.required'
                            )
                        )
                    )
                )
            );
        }
    }
