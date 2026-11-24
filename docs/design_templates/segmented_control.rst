Segmented control template
##########################

The ``segmented-control.html.twig`` template renders a segmented control, a row of mutually exclusive options shown side by side. Use it for a choice between two to four short options that fit on one line, such as Contact or Company, so Users see every option without opening a drop-down. Mautic uses it for settings such as **Storage Location** on Assets and **Fetch Interactions From** in the Campaign settings.

For a single yes or no choice, use ``YesNoButtonGroupType`` instead. For more than four options, or options with long labels, use a select field.

Each option is a radio button with a label, and a sliding indicator marks the selected option. Users select an option by clicking it, by moving through the options with the arrow keys, or by pressing the selected option and dragging the indicator to another option. The control has ``role="radiogroup"``, so screen readers announce it as a group of options.

Segmented controls in Symfony forms
***********************************

To add a segmented control to a Symfony form in your Plugin, add a field with the ``Mautic\CoreBundle\Form\Type\SegmentedControlType`` type. The field is a Symfony ``ChoiceType`` field that allows one choice, so it accepts options such as ``choices``, ``label``, ``data``, and ``disabled``.

.. code-block:: php

   <?php

   declare(strict_types=1);

   namespace MauticPlugin\HelloWorldBundle\Form\Type;

   use Mautic\CoreBundle\Form\Type\SegmentedControlType;
   use Symfony\Component\Form\AbstractType;
   use Symfony\Component\Form\FormBuilderInterface;

   final class WorldType extends AbstractType
   {
       public function buildForm(FormBuilderInterface $builder, array $options): void
       {
           $builder->add('visibility', SegmentedControlType::class, [
               'label'   => 'plugin.helloworld.world.visibility',
               'choices' => [
                   'plugin.helloworld.world.visibility.private' => 'private',
                   'plugin.helloworld.world.visibility.public'  => 'public',
               ],
               'data'    => 'private',
           ]);
       }
   }

When you render the field with ``form_row()``, Mautic's layout template for Symfony fields, ``mautic_form_layout.html.twig``, shows the field's label and includes the segmented control template for you. The control also uses the label as its ``aria-label``. The browser submits the value of the selected option as the field's value, so the field works like any other single-choice field when you handle the submitted form.

The layout passes the field's ``attr`` options to every radio button, except ``class`` and ``tooltip``. It adds ``class`` to the control's wrapper ``<div>`` instead. You don't need to set a ``class`` such as ``form-control`` on the field.

To show the field's value without letting Users change it, set ``'attr' => ['readonly' => 'readonly']``. Users can't select another option by clicking, dragging, or using the keyboard, and pressing Tab skips the control. The browser still submits the selected option's value. The ``disabled`` option also stops changes, but the browser doesn't submit the value of a field with ``disabled`` set to ``true``.

``SegmentedControlType`` adds one option, ``draggable``, which defaults to ``true``. Set it to ``false`` to turn off dragging the indicator. Users can still click options and use the arrow keys.

To set the control's size, give options equal widths, show icons, or change how fast the indicator slides, include the template directly as described in the next section.

Including the template
**********************

To render a segmented control outside a Symfony form, include ``@MauticCore/Components/segmented-control.html.twig`` with the ``only`` keyword, and pass an ``options`` array with one entry per option.

.. code-block:: twig

   {% include '@MauticCore/Components/segmented-control.html.twig' with {
       name: 'helloworld_view',
       label: 'plugin.helloworld.view',
       value: 'list',
       options: [
           { value: 'list', label: 'plugin.helloworld.view.list', icon: 'ri-list-check' },
           { value: 'grid', label: 'plugin.helloworld.view.grid', icon: 'ri-layout-grid-line' }
       ]
   } only %}

Without ``only``, Twig also passes every variable of the including template to the Component. The Component reads its options, such as ``value``, ``size``, and ``id``, from those variables, so a parent variable with the same name overrides the option's default. With ``only``, the Component receives just the variables you pass.

The template passes ``label`` and each option's ``label`` through Twig's ``trans`` filter, so you can pass translation keys or plain strings. To translate an option's label in another domain or with parameters, set the option's ``translation_domain`` and ``label_translation_parameters`` keys.

Template options
================

You must set ``options``. All other options are optional.

.. list-table::
    :header-rows: 1
    :widths: 20 10 15 55

    * - Option
      - Type
      - Default
      - Description
    * - ``options``
      - array
      - None
      - The options to show, in order. See :ref:`Option keys <segmented control option keys>` for the keys each option accepts.
    * - ``value``
      - string
      - The first option's value
      - The value of the selected option.
    * - ``name``
      - string
      - The control's ``id``
      - The ``name`` attribute of the radio buttons. The browser submits the selected option's value under this name.
    * - ``id``
      - string
      - ``segmented-control-`` followed by a random number
      - The ``id`` of the control. Each radio button gets this ``id`` followed by an underscore and its position, starting at ``0``.
    * - ``label``
      - string
      - None
      - The control's ``aria-label``, which tells screen readers what the options choose. The template doesn't show it on the page.
    * - ``translation_domain``
      - string or boolean
      - None
      - The translation domain for ``label``. Set it to ``false`` to use ``label`` without translating it.
    * - ``label_translation_parameters``
      - array
      - Empty array
      - Parameters for the translation of ``label``.
    * - ``size``
      - string
      - ``md``
      - The control's size. Set it to ``sm``, ``md``, or ``lg``.
    * - ``equalWidth``
      - boolean
      - ``false``
      - Set to ``true`` to give every option the width of the widest option.
    * - ``draggable``
      - boolean
      - ``true``
      - Set to ``false`` to turn off dragging the indicator.
    * - ``duration``
      - number
      - None
      - The time in seconds that the indicator takes to slide to the selected option. When you don't set it, the indicator takes 0.35 seconds.
    * - ``attr``
      - array
      - Empty array
      - Extra HTML attributes for every radio button, keyed by attribute name. The template leaves out attributes whose value is ``false``.
    * - ``className``
      - string
      - None
      - Extra CSS classes for the control's wrapper ``<div>``, such as spacing classes.

.. _segmented control option keys:

Option keys
===========

Each entry in ``options`` accepts these keys. You must set ``value`` and ``label``.

.. list-table::
    :header-rows: 1
    :widths: 20 10 70

    * - Key
      - Type
      - Description
    * - ``value``
      - string
      - The value the browser submits when the User selects the option.
    * - ``label``
      - string
      - The option's text. The template escapes it as HTML.
    * - ``icon``
      - string
      - Icon CSS classes, such as ``ri-list-check``, for an icon before the label.
    * - ``disabled``
      - boolean
      - Set to ``true`` to stop Users from selecting the option.
    * - ``required``
      - boolean
      - Set to ``true`` to add the ``required`` attribute to the option's radio button.
    * - ``translation_domain``
      - string or boolean
      - The translation domain for the option's ``label``. Set it to ``false`` to use ``label`` without translating it.
    * - ``label_translation_parameters``
      - array
      - Parameters for the translation of the option's ``label``.

Initializing the control with JavaScript
****************************************

Mautic positions the indicator and turns on dragging when it loads a page or AJAX content. If your JavaScript adds a segmented control to the page in another way, call ``Mautic.initSegmentedControl()`` with the element or selector that contains it. Calling it again for a control that's already initialized moves the indicator back under the selected option.

.. code-block:: javascript

   mQuery('#helloworld-view-container').html(response.html);
   Mautic.initSegmentedControl('#helloworld-view-container');

When the User selects an option, including by dragging, the radio button dispatches a ``change`` event that bubbles. Listen for it to react to the new value.

.. code-block:: javascript

   mQuery('#helloworld-view-container').on('change', 'input[name="helloworld_view"]', function () {
       Mautic.helloWorldSwitchView(this.value);
   });
