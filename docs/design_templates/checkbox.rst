Checkbox component
##################

The ``checkbox.html.twig`` template renders one or more checkboxes in Mautic's checkbox style. Use it when your template outputs checkboxes, so they look and behave like the checkboxes in Mautic's own list views, filters, and settings.

The template wraps the checkboxes in a ``<fieldset>``. Each checkbox is a ``<div class="form-check">`` that contains an ``<input class="form-check-input" type="checkbox">`` and, when you pass a label, a ``<label class="form-check-label">``.

Checkboxes in Symfony forms
***************************

Mautic's form layout template, ``mautic_form_layout.html.twig``, already uses the Checkbox Component in the ``checkbox_row`` block, and in the ``choice_row`` block for ``ChoiceType`` fields with ``expanded`` and ``multiple`` set to ``true``. When you render these fields with ``form_row()``, you don't need to include the template yourself.

Including the template
**********************

Include ``@MauticCore/Components/checkbox.html.twig`` and pass an ``items`` array with one entry per checkbox:

.. code-block:: twig

   {% include '@MauticCore/Components/checkbox.html.twig' with {
       name: 'helloworld_channels[]',
       legend: 'plugin.helloworld.channels',
       helpText: 'plugin.helloworld.channels.help',
       items: [
           { value: 'email', label: 'plugin.helloworld.channel.email', checked: true },
           { value: 'sms', label: 'plugin.helloworld.channel.sms' }
       ]
   } %}

The template passes ``legend``, ``helpText``, and each item's ``label`` through Twig's ``trans`` filter, so you can pass translation keys or plain strings.

To render a single checkbox, such as the bulk-select checkbox in a list header, pass one item and add any extra HTML attributes the checkbox needs:

.. code-block:: twig

   {% include '@MauticCore/Components/checkbox.html.twig' with {
       name: 'customcheckbox-one',
       items: [{
           id: 'customcheckbox-one0',
           value: '1',
           className: 'checkall',
           attributes: { 'data-toggle': 'checkall', 'data-target': target }
       }]
   } %}

Template options
================

These options apply to the whole group of checkboxes. All of them are optional.

``items``
    An array of checkboxes to render. Defaults to an empty array. See :ref:`Item options <checkbox item options>` for the keys each item accepts.

``name``
    The ``name`` attribute for checkboxes that don't set their own. The template also uses it to build default ``id`` values. Defaults to ``checkbox``.

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
    The ``name`` attribute for this checkbox. Defaults to the template's ``name`` option.

``value``
    The ``value`` attribute. Defaults to the item's zero-based position in ``items``.

``label``
    The label text. The template renders no ``<label>`` when you don't set it.

``checked``
    Set to ``true`` to add the ``checked`` attribute. Defaults to ``false``.

``disabled``
    Set to ``true`` to add the ``disabled`` attribute. Defaults to ``false``.

``className``
    Extra CSS classes for the ``<input>``, added after ``form-check-input``.

``attributes``
    A map of extra HTML attributes for the ``<input>``, such as ``data-*`` attributes or an ``onclick`` handler.

``labelAttributes``
    A map of extra HTML attributes for the ``<label>``.
