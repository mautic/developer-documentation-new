Checkbox template
#################

The ``checkbox.html.twig`` template renders one or more checkboxes in Mautic's checkbox style. Use it when your template outputs checkboxes, so they look and behave like the checkboxes in Mautic's own list views, filters, and settings.

The template wraps the checkboxes in a ``<fieldset>``. Each checkbox is a ``<div class="form-check">`` that contains an ``<input class="form-check-input" type="checkbox">`` and, when you pass a label, a ``<label class="form-check-label">``.

Checkboxes rendered with ``form_row()``
****************************************

Mautic's layout template for Symfony fields, ``mautic_form_layout.html.twig``, already uses the Checkbox Component in the ``checkbox_row`` block, and in the ``choice_row`` block for ``ChoiceType`` fields with ``expanded`` and ``multiple`` set to ``true``. When you render these fields with ``form_row()``, you don't need to include the template yourself. This layout template passes the field's ``label``, ``label_html``, ``translation_domain``, ``label_translation_parameters``, and ``attr`` options to the template, and adds the ``required`` attribute to a ``checkbox_row`` checkbox when the field sets ``required``.

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

.. list-table::
    :header-rows: 1
    :widths: 25 10 15 50

    * - Option
      - Type
      - Default
      - Description
    * - ``items``
      - array
      - Empty array
      - The checkboxes to render. See :ref:`Item options <checkbox item options>` for the keys each item accepts.
    * - ``name``
      - string
      - Empty string
      - The ``name`` attribute for checkboxes that don't set their own. The template also uses it to build default ``id`` values. When neither this option nor the item sets a name, the checkbox has no ``name`` attribute, so the browser doesn't submit it, and default ``id`` values start with ``checkbox``.
    * - ``legend``
      - string
      - None
      - Text for a ``<legend>`` element before the checkboxes. The template omits the legend when you don't set it.
    * - ``helpText``
      - string
      - None
      - Help text shown below the checkboxes. Each checkbox references it through ``aria-describedby``, so screen readers announce it.
    * - ``wrapperClass``
      - string
      - Empty string
      - Extra CSS classes for the ``<fieldset>``.
    * - ``inline``
      - boolean
      - ``false``
      - Set to ``true`` to show the checkboxes on one line. This adds the ``form-check-inline`` class.
    * - ``reverse``
      - boolean
      - ``false``
      - Set to ``true`` to place each label before its checkbox. This adds the ``form-check-reverse`` class.
    * - ``required``
      - boolean
      - ``false``
      - Set to ``true`` to add the ``required`` attribute to every checkbox.

.. _checkbox item options:

Item options
============

Each entry in ``items`` accepts these keys. All of them are optional.

.. list-table::
    :header-rows: 1
    :widths: 30 10 15 45

    * - Key
      - Type
      - Default
      - Description
    * - ``id``
      - string
      - Built from the template's ``name`` option
      - The checkbox ``id``. When you don't set it, the template builds one from the template's ``name`` option, or ``checkbox`` when that option is empty, followed by the item's zero-based position and its ``value``. The item's own ``name`` key doesn't affect the ``id``. For example, an item with ``name: 'foo'`` and ``value: 'bar'`` in a group without a ``name`` option gets the ``id`` ``checkbox-0-bar``. The template normalizes both parts. In the ``name`` option, it replaces ``[``, spaces, and periods with hyphens and removes ``]``. In the ``value``, it also replaces underscores with hyphens and converts the result to lowercase. For example, the value ``Some_Value`` in the first item of a group named ``channels[]`` gives the ``id`` ``channels--0-some-value``. Set an explicit ``id`` when JavaScript or a ``<label>`` elsewhere needs to find the checkbox.
    * - ``name``
      - string
      - The template's ``name`` option
      - The ``name`` attribute for this checkbox. The template omits the attribute when neither the item nor the template sets a name.
    * - ``value``
      - string
      - The item's zero-based position in ``items``
      - The ``value`` attribute.
    * - ``label``
      - string or ``false``
      - Empty string
      - The label text, or a translation key. The template renders no ``<label>`` when the label is an empty string or ``false``.
    * - ``label_html``
      - boolean
      - ``false``
      - Set to ``true`` to render HTML in the label, such as a link. The template sanitizes the translated label with the ``purify`` filter instead of escaping it.
    * - ``translation_domain``
      - string
      - ``messages``
      - The translation domain for the label.
    * - ``label_translation_parameters``
      - map
      - Empty map
      - Parameters for the label's translation string.
    * - ``checked``
      - boolean
      - ``false``
      - Set to ``true`` to add the ``checked`` attribute.
    * - ``disabled``
      - boolean
      - ``false``
      - Set to ``true`` to add the ``disabled`` attribute.
    * - ``className``
      - string
      - None
      - Extra CSS classes for the ``<input>``, added after ``form-check-input``.
    * - ``attributes``
      - map
      - Empty map
      - Extra HTML attributes for the ``<input>``, such as ``data-*`` attributes or an ``onclick`` handler. The template escapes each name and value. Set a value to ``true`` to render a boolean attribute without a value, or to ``false`` or ``null`` to omit the attribute. A ``class`` entry adds its classes to the ``<input>`` after ``form-check-input`` and ``className``.
    * - ``labelAttributes``
      - map
      - Empty map
      - Extra HTML attributes for the ``<label>``.
