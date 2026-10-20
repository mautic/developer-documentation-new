Checkbox component
##################

The ``checkbox.html.twig`` template renders one or more checkboxes in Mautic's checkbox style. Use it when your template outputs checkboxes, so they look and behave like the checkboxes in Mautic's own list views, filters, and settings.

The template wraps the checkboxes in a ``<fieldset>``. Each checkbox is a ``<div class="form-check">`` that contains an ``<input class="form-check-input" type="checkbox">`` and, when you pass a label, a ``<label class="form-check-label">``.

Checkboxes in Symfony forms
***************************

Mautic's form layout template, ``mautic_form_layout.html.twig``, already uses the Checkbox Component in the ``checkbox_row`` block, and in the ``choice_row`` block for ``ChoiceType`` fields with ``expanded`` and ``multiple`` set to ``true``. When you render these fields with ``form_row()``, you don't need to include the template yourself. The form layout passes the field's ``label``, ``label_html``, ``translation_domain``, ``label_translation_parameters``, and ``attr`` options to the template, and adds the ``required`` attribute to a ``checkbox_row`` checkbox when the field sets ``required``.

Including the template
**********************

Include ``@MauticCore/Components/checkbox.html.twig`` with the ``only`` keyword, and pass an ``items`` array with one entry per checkbox.

.. code-block:: twig

   {% include '@MauticCore/Components/checkbox.html.twig' with {
       name: 'helloworld_channels[]',
       legend: 'plugin.helloworld.channels',
       helpText: 'plugin.helloworld.channels.help',
       items: [
           { value: 'email', label: 'plugin.helloworld.channel.email', checked: true },
           { value: 'sms', label: 'plugin.helloworld.channel.sms' }
       ]
   } only %}

Without ``only``, Twig also passes every variable of the including template to the Component. The Component reads its options, such as ``required``, ``name``, and ``items``, from those variables, so a parent variable with the same name overrides the option's default. For example, an include inside a Twig block that defines ``required``, such as a Symfony field's row block, adds the ``required`` attribute to every checkbox. With ``only``, the Component receives just the variables you pass.

The template passes ``legend``, ``helpText``, and each item's ``label`` through Twig's ``trans`` filter, so you can pass translation keys or plain strings. It escapes label text as HTML unless you set the item's ``label_html`` key.

To render a single checkbox, such as the bulk-select checkbox in a list header, pass one item and add any extra HTML attributes the checkbox needs.

.. code-block:: twig

   {% include '@MauticCore/Components/checkbox.html.twig' with {
       items: [{
           id: 'customcheckbox-one0',
           value: '1',
           className: 'checkall',
           attributes: { 'data-toggle': 'checkall', 'data-target': target }
       }]
   } only %}

Template options
================

These options apply to the whole group of checkboxes. All of them are optional.

``items``
    An array of checkboxes to render. Defaults to an empty array. See :ref:`Item options <checkbox item options>` for the keys each item accepts.

``name``
    The ``name`` attribute for checkboxes that don't set their own. The template also uses it to build default ``id`` values. When neither this option nor the item sets a name, the checkbox has no ``name`` attribute, so the browser doesn't submit it, and default ``id`` values start with ``checkbox``.

``legend``
    Text for a ``<legend>`` element before the checkboxes. The template omits the legend when you don't set it.

``helpText``
    Help text shown below the checkboxes. Each checkbox references it through ``aria-describedby``, so screen readers announce it.

``wrapperClass``
    Extra CSS classes for the ``<fieldset>``.

``inline``
    Set to ``true`` to show the checkboxes on one line. This adds the ``form-check-inline`` class. Defaults to ``false``.

``reverse``
    Set to ``true`` to place each label before its checkbox. This adds the ``form-check-reverse`` class. Defaults to ``false``.

``required``
    Set to ``true`` to add the ``required`` attribute to every checkbox. Defaults to ``false``.

.. _checkbox item options:

Item options
============

Each entry in ``items`` accepts these keys. All of them are optional.

``id``
    The checkbox ``id``. When you don't set it, the template builds one from ``name``, the item's position, and its ``value``. Set an explicit ``id`` when JavaScript or a ``<label>`` elsewhere needs to find the checkbox.

``name``
    The ``name`` attribute for this checkbox. Defaults to the template's ``name`` option. The template omits the attribute when neither sets a name.

``value``
    The ``value`` attribute. Defaults to the item's zero-based position in ``items``.

``label``
    The label text, or a translation key. The template renders no ``<label>`` when you don't set it, or when you set it to an empty string or ``false``.

``label_html``
    Set to ``true`` to render HTML in the label, such as a link. The template sanitizes the translated label with the ``purify`` filter instead of escaping it. Defaults to ``false``.

``translation_domain``
    The translation domain for the label. Defaults to Symfony's default ``messages`` domain.

``label_translation_parameters``
    A map of parameters for the label's translation string. Defaults to an empty map.

``checked``
    Set to ``true`` to add the ``checked`` attribute. Defaults to ``false``.

``disabled``
    Set to ``true`` to add the ``disabled`` attribute. Defaults to ``false``.

``className``
    Extra CSS classes for the ``<input>``, added after ``form-check-input``.

``attributes``
    A map of extra HTML attributes for the ``<input>``, such as ``data-*`` attributes or an ``onclick`` handler. The template escapes each name and value. Set a value to ``true`` to render a boolean attribute without a value, or to ``false`` or ``null`` to omit the attribute. A ``class`` entry adds its classes to the ``<input>`` after ``form-check-input`` and ``className``.

``labelAttributes``
    A map of extra HTML attributes for the ``<label>``.
