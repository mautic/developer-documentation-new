Toggle template
###############

The ``toggle.html.twig`` template renders a toggle switch for a choice between two values, such as on or off. Mautic uses it for yes or no settings such as **Active** and **Allow contacts to restart the campaign**. Use it when your template needs the same switch, so it looks and behaves like the toggles elsewhere in Mautic.

The switch shows the text for its current value next to it, such as 'No' or 'Yes'. Users change the value by clicking the switch, or by focusing it with Tab and pressing Space or Enter. The switch has ``role="switch"`` and an ``aria-checked`` attribute that follows its value, so screen readers announce it as a switch that's on or off. Two hidden radio buttons hold the value, so the browser submits it like any other field.

Toggles in Symfony forms
************************

To add a toggle to a Symfony form in your Plugin, add a field with the ``Mautic\CoreBundle\Form\Type\YesNoButtonGroupType`` type.

.. code-block:: php

   <?php

   declare(strict_types=1);

   namespace MauticPlugin\HelloWorldBundle\Form\Type;

   use Mautic\CoreBundle\Form\Type\YesNoButtonGroupType;
   use Symfony\Component\Form\AbstractType;
   use Symfony\Component\Form\FormBuilderInterface;

   final class WorldType extends AbstractType
   {
       public function buildForm(FormBuilderInterface $builder, array $options): void
       {
           $builder->add('isVisited', YesNoButtonGroupType::class, [
               'label' => 'plugin.helloworld.world.visited',
               'data'  => false,
           ]);
       }
   }

When you render the field with ``form_row()``, Mautic's layout template for Symfony fields, ``mautic_form_layout.html.twig``, shows the field's label and includes the toggle template for you. The switch uses the field's label as its accessible name, so screen readers announce the label with the switch.

When the field has no value, such as a new entity whose property is ``null``, the layout leaves the toggle unset. The layout then selects neither radio button and shows no text next to the switch, so the browser submits no value for the field. The first time the User switches the toggle, it turns on and selects ``yes_value``. To show the switch as on or off from the start, give the field a value, for example with the ``data`` option as in the preceding example.

``YesNoButtonGroupType`` sets these options, which you can override:

* ``label`` defaults to ``mautic.core.form.active``, which shows **Active**.
* ``yes_label`` and ``no_label`` set the text shown next to the switch for each value. They default to ``mautic.core.form.yes`` and ``mautic.core.form.no``.
* ``yes_value`` and ``no_value`` set the values the browser submits. They default to ``1`` and ``0``.

The layout passes the field's ``attr`` options to both radio buttons. Use these ``attr`` keys to change the toggle:

* Set ``'size' => 'sm'`` to show a smaller switch.
* Set ``'readonly' => 'readonly'`` to show the value without letting Users change it. The browser still submits the value.
* Set ``'disabled' => 'disabled'`` to show the switch as unavailable. Pressing Tab skips the switch, and the browser doesn't submit the value.

When the field's ``id`` contains ``Publish``, such as a field named ``isPublished``, the text next to the switch also shows the publishing schedule. The text follows the ``publishUp`` and ``publishDown`` fields of the same form, for example to say that the item is active until its scheduled end.

Including the template
**********************

To render a toggle outside a Symfony form, include ``@MauticCore/Components/toggle.html.twig`` with the ``only`` keyword. Give each toggle on the page its own ``id``, because the template builds the ``id`` values of the radio buttons from it.

.. code-block:: twig

   {% include '@MauticCore/Components/toggle.html.twig' with {
       id: 'helloworld_notifications',
       name: 'helloworld[notifications]',
       label: 'plugin.helloworld.notifications',
       checked: world.notificationsEnabled,
   } only %}

Without ``only``, Twig also passes every variable of the including template to the Component. The Component reads its options, such as ``id``, ``checked``, and ``disabled``, from those variables, so a parent variable with the same name overrides the option's default. With ``only``, the Component receives just the variables you pass.

The template passes ``label``, ``ariaLabel``, ``labelOn``, and ``labelOff`` through Twig's ``trans`` filter, so you can pass translation keys or plain strings.

Give every toggle an accessible name with one of these options. When you set more than one, the template uses the first in this order:

#. ``label`` shows the text before the switch and uses it as the name. Set ``hideLabel`` to ``true`` to hide the text on screen while screen readers still announce it.
#. ``labelledby`` takes the ``id`` of an element on the page, such as a heading or a ``<label>``, and uses that element's text as the name.
#. ``ariaLabel`` sets the name without showing any text.

Template options
================

All options are optional.

.. list-table::
    :header-rows: 1
    :widths: 20 10 15 55

    * - Option
      - Type
      - Default
      - Description
    * - ``id``
      - string
      - ``toggle``
      - The ``id`` of the toggle. The radio buttons get this ``id`` followed by an underscore and their value, such as ``helloworld_notifications_1``.
    * - ``name``
      - string
      - The ``id``
      - The ``name`` attribute of the radio buttons. The browser submits the toggle's value under this name.
    * - ``checked``
      - boolean or null
      - ``false``
      - Set to ``true`` to turn the switch on, which selects ``valueOn``. Set to ``null`` to leave the toggle unset. The template then selects neither radio button and shows no text next to the switch, and the browser submits no value until the User switches it on.
    * - ``label``
      - string
      - None
      - Text shown before the switch and used as its accessible name.
    * - ``hideLabel``
      - boolean
      - ``false``
      - Set to ``true`` to hide ``label`` on screen. Screen readers still announce it.
    * - ``labelledby``
      - string
      - None
      - The ``id`` of an element whose text names the switch. The template uses it only when you don't set ``label``.
    * - ``ariaLabel``
      - string
      - None
      - The switch's ``aria-label``. The template uses it only when you set neither ``label`` nor ``labelledby``.
    * - ``labelOn``
      - string
      - ``mautic.core.form.yes``
      - The text shown next to the switch when it's on.
    * - ``labelOff``
      - string
      - ``mautic.core.form.no``
      - The text shown next to the switch when it's off.
    * - ``valueOn``
      - string
      - ``1``
      - The value the browser submits when the switch is on.
    * - ``valueOff``
      - string
      - ``0``
      - The value the browser submits when the switch is off.
    * - ``size``
      - string
      - None
      - Set to ``sm`` to show a smaller switch.
    * - ``disabled``
      - boolean
      - ``false``
      - Set to ``true`` to show the switch as unavailable. Users can't change it, pressing Tab skips it, and the browser doesn't submit its value.
    * - ``readonly``
      - boolean
      - ``false``
      - Set to ``true`` to stop Users from changing the value. Users can still focus the switch, and the browser submits its value.
    * - ``attributes``
      - map
      - Empty map
      - Extra HTML attributes for both radio buttons, such as ``data-*`` attributes. The template escapes each name and value. Set a value to ``true`` to render a boolean attribute without a value, or to ``false`` or ``null`` to omit the attribute. Use the ``disabled`` and ``readonly`` options instead of ``disabled`` and ``readonly`` keys here.

Reacting to changes with JavaScript
***********************************

The switch works without any JavaScript setup, including in content that your Plugin loads with AJAX. When the User switches the toggle, Mautic updates the radio buttons and the switch, then triggers a jQuery ``change`` event on the radio button for ``valueOn``. Listen for it with ``mQuery`` and read that radio button's ``checked`` property to get the new state.

.. code-block:: javascript

   mQuery('#helloworld_notifications_1').on('change', function () {
       Mautic.helloWorldSetNotifications(this.checked);
   });
