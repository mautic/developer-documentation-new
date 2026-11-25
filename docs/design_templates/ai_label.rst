AI label template
#################

The ``ai-label.html.twig`` template renders a small 'AI' label that tells Users that a value or a piece of content comes from AI. Use it when your Plugin fills a field, a Tile, a Tag, or a table cell with AI-generated content, so Users can tell that content apart from content that people entered.

By default, the label is a button. When a User selects it, a popover opens with a title and an optional explanation, for example which model produced the content and from which data. Mautic initializes the popover for you, so you don't need any JavaScript.

Adding the label to a Component
*******************************

Several Mautic Components accept an ``aiLabel`` option. When you don't set it, the Component renders as before, without a label. Set ``aiLabel`` to ``true`` to show the label with its default text, or pass a map of :ref:`AI label options <ai label template options>` to customize it.

.. code-block:: twig

   {% include '@MauticCore/Components/text-input.html.twig' with {
       name: 'helloworld_summary',
       labelText: 'plugin.helloworld.summary',
       aiLabel: {
           content: 'plugin.helloworld.summary.ai_explanation'
       }
   } only %}

These Components accept ``aiLabel``:

.. list-table::
    :header-rows: 1
    :widths: 35 65

    * - Component
      - Where the label appears
    * - ``@MauticCore/Components/text-input.html.twig`` and ``@MauticCore/Components/form-control.html.twig``
      - Inside the field, at its end. The field also gets an AI border and background.
    * - ``@MauticCore/Components/checkbox.html.twig``
      - Next to the ``legend`` text, as a small inline label. The template only renders the label when you set ``legend``.
    * - ``@MauticCore/Components/tile.html.twig``
      - In the top-right corner of the Tile, which also gets an AI gradient and shadow. Clickable, mini, and expandable Tiles show a static label, because the label can't be a button inside the Tile's link or button.
    * - ``@MauticCore/Components/modal.html.twig``
      - In the modal header. The modal also gets an AI gradient and shadow.
    * - ``@MauticCore/Helper/_tag.html.twig``
      - Inside read-only, dismissible, and selectable Tags, as a small inline label. Set ``aiLabel`` on the Tag item, not on the include. Selectable Tags and Tags with an ``href`` attribute always show a static label, even when ``aiLabel`` sets ``static`` to ``false``.
    * - ``@MauticCore/Helper/table.html.twig``
      - Next to a header or cell value, as a small inline label. See :ref:`Table headers and cells <ai label tables>`.

Tags
====

The ``_tag.html.twig`` helper reads ``aiLabel`` from each Tag item, along with the Tag's ``label`` and other keys.

.. code-block:: twig

   {% include '@MauticCore/Helper/_tag.html.twig' with {
       tags: [
           { label: 'plugin.helloworld.tag.suggested', color: 'blue', aiLabel: true }
       ]
   } %}

.. _ai label tables:

Table headers and cells
=======================

In the ``table.html.twig`` helper, a header item can be a map with a ``label`` key instead of a string. Add ``aiLabel`` to that map to label the column header. To label a cell, add ``aiLabel`` to a body item that's a map, such as one with a ``value`` key or a link cell that sets ``type`` to ``link``. The label appears before the cell's value or link.

.. code-block:: twig

   {% include '@MauticCore/Helper/table.html.twig' with {
       headItems: [
           'mautic.core.name',
           { label: 'plugin.helloworld.score', aiLabel: true }
       ],
       bodyItems: [
           ['Jane Doe', { value: '87', aiLabel: { content: 'plugin.helloworld.score.ai_explanation' } }]
       ]
   } %}

Including the template directly
*******************************

To place the label somewhere the Components don't cover, include ``@MauticCore/Components/ai-label.html.twig`` with the ``only`` keyword.

.. code-block:: twig

   <h3 class="d-flex align-items-center gap-2">
       {{ 'plugin.helloworld.summary'|trans }}
       {% include '@MauticCore/Components/ai-label.html.twig' with {
           inline: true,
           size: 'md',
           content: 'plugin.helloworld.summary.ai_explanation'
       } only %}
   </h3>

The template passes ``label``, ``additionalText``, ``title``, ``content``, and ``aria_label`` through Twig's ``trans`` filter, so you can pass translation keys or plain strings. The popover shows ``title`` and ``content`` as plain text, so it doesn't render HTML in them.

.. _ai label template options:

Template options
================

All options are optional. The Components that accept ``aiLabel`` pass a map of these options to the template.

.. list-table::
    :header-rows: 1
    :widths: 20 10 20 50

    * - Option
      - Type
      - Default
      - Description
    * - ``label``
      - string
      - ``mautic.core.ai.label``
      - The label text. The default translation is 'AI'.
    * - ``additionalText``
      - string
      - None
      - Extra text after the label, such as the name of the model. The label widens to fit it.
    * - ``title``
      - string
      - ``mautic.core.ai.explainability.title``
      - The popover title. The default translation is 'AI generated'.
    * - ``content``
      - string
      - None
      - The popover text that explains the AI content. Without it, the popover shows only the title.
    * - ``placement``
      - string
      - ``bottom``
      - Where the popover opens relative to the label: ``top``, ``bottom``, ``left``, ``right``, or ``auto``.
    * - ``trigger``
      - string
      - ``click focus``
      - The Bootstrap popover trigger. With ``click focus``, the popover opens when a User selects the label or moves focus to it.
    * - ``aria_label``
      - string
      - ``mautic.core.ai.explainability``
      - The accessible name of the label button. On a static label, it replaces the ``label`` text as the accessible name.

        .. vale off

        The default translation is 'Show AI explainability'.

        .. vale on
    * - ``inline``
      - boolean
      - ``false``
      - Set to ``true`` to show a label without a border, with a small square before the text, for use next to text such as headings, legends, Tags, and table values.
    * - ``size``
      - string
      - ``md`` when ``inline`` is ``true``, otherwise ``xs``
      - The label size. Square labels accept ``mini``, ``2xs``, ``xs``, ``sm``, ``md``, ``lg``, and ``xl``, from 16 to 64 pixels. Inline labels accept ``sm``, ``md``, and ``lg``.
    * - ``static``
      - boolean
      - ``false``
      - Set to ``true`` to render the label as an image instead of a button, with no popover. Use it inside links and buttons. Screen readers announce the ``label`` text, 'AI' by default, followed by any ``additionalText``.
    * - ``className``
      - string
      - None
      - Extra CSS classes for the wrapper ``<span>``.
