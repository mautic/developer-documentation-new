Data table template
###################

The ``data-table.html.twig`` template renders rows of structured data in Mautic's table style. Use it when your template lists records that readers compare or act on across columns, so the table looks and behaves like Mautic's own Segments list.

You describe the table with its columns and its rows, and the template renders the header, the cells, and the controls you turn on. It supports column sorting, row selection with batch actions, per-row actions in an overflow menu, expandable rows, a search box, row sizes from extra small to extra large, zebra rows, a sticky header, a loading state, and an empty state.

Including the template
**********************

Include ``@MauticCore/Components/data-table.html.twig`` with the ``only`` keyword, and pass ``columns`` and ``rows``. Each row holds its cells in ``cells``, keyed by the column's ``key``.

.. code-block:: twig

   {% include '@MauticCore/Components/data-table.html.twig' with {
       id: 'helloworld-worlds',
       label: 'plugin.helloworld.worlds',
       columns: [
           { key: 'name', label: 'mautic.core.name', sortable: true },
           { key: 'visits', label: 'plugin.helloworld.visits', sortable: true, align: 'end' }
       ],
       rows: [
           { id: 1, cells: { name: 'Earth', visits: 42 } },
           { id: 2, cells: { name: 'Mars', visits: 7 } }
       ]
   } only %}

Without ``only``, Twig also passes every variable of the including template to the Component. The Component reads its options, such as ``size``, ``selection``, and ``title``, from those variables, so a parent variable with the same name overrides the option's default. With ``only``, the Component receives just the variables you pass.

The template passes ``title``, ``description``, ``label``, each column's ``label``, ``searchPlaceholder``, and ``emptyMessage`` through Twig's ``trans`` filter, so you can pass translation keys or plain strings.

Sorting rows
============

A column can sort in two ways:

* Set ``sortable`` to ``true`` to sort the rendered rows in the browser. Selecting the header cycles through ascending, descending, and the original order. The sort compares numbers as numbers.
* Set ``sortHref`` to a URL that returns the list sorted on the server, as Mautic's list views do. Mautic loads the response into the element that the ``target`` option names, ``.page-list`` by default. Set ``sort`` to ``asc`` or ``desc`` on the column that the server sorted the list by, so the header shows the current direction.

Selecting rows and running batch actions
========================================

Set ``selection`` to ``multi`` to add a checkbox to each row and a checkbox in the header that selects every visible row. Set it to ``single`` to add a radio button to each row instead.

With ``multi`` selection, pass ``batchActions`` to show buttons for the selected rows. While the reader has at least one row selected, the buttons replace the toolbar at the top of the table, next to the number of selected rows and a **Cancel** button that clears the selection. Each selection input's ``value`` is the row's ``id``, so your batch action's JavaScript can read the selected rows from the checked inputs.

.. code-block:: twig

   {% include '@MauticCore/Components/data-table.html.twig' with {
       id: 'helloworld-worlds',
       label: 'plugin.helloworld.worlds',
       selection: 'multi',
       batchActions: [
           { label: 'plugin.helloworld.worlds.export', attributes: { 'data-helloworld-export': '' } }
       ],
       columns: columns,
       rows: rows
   } only %}

``batchActions`` and ``toolbarActions`` take the same button entries as the ``buttons`` option of ``@MauticCore/Helper/button.html.twig``.

Adding row actions and expandable rows
======================================

Give a row an ``actions`` array to show its actions in an overflow menu at the end of the row.

To show extra detail for a row only when the reader asks for it, set ``expandable`` to ``true`` on the table and give the row an ``expansion``. The row gets a button that shows and hides the detail. Set ``batchExpansion`` to ``true`` to add a button in the header that expands or collapses every row.

.. code-block:: twig

   {% set rows = [{
       id: 1,
       cells: { name: 'Earth', visits: 42 },
       expansion: '<p>Third planet from the Sun.</p>',
       actions: [
           { label: 'mautic.core.form.edit', href: path('helloworld_world_action', {objectAction: 'edit', objectId: 1}), icon: 'ri-edit-line', attr: { 'data-toggle': 'ajax' } },
           { label: 'mautic.core.form.delete', href: '#', icon: 'ri-delete-bin-line', danger: true }
       ]
   }] %}

Template options
================

You must set ``columns`` and ``rows`` to show data. All other options are optional.

.. list-table::
    :header-rows: 1
    :widths: 20 10 15 55

    * - Option
      - Type
      - Default
      - Description
    * - ``columns``
      - array
      - Empty array
      - The table's columns, in display order. See :ref:`Column options <data table column options>`.
    * - ``rows``
      - array
      - Empty array
      - The table's rows. See :ref:`Row options <data table row options>`.
    * - ``id``
      - string
      - ``data-table-`` followed by a random number
      - The ``id`` of the wrapper element, and the base for the ``id`` attributes inside the table. Set it when your JavaScript or CSS needs to find the table.
    * - ``title``
      - string
      - None
      - A heading at the top of the table. Screen readers use it as the table's name.
    * - ``description``
      - string
      - None
      - Text below the title. The template shows it only when you set ``title``.
    * - ``label``
      - string
      - The value of ``title``
      - The table's name for screen readers. Set it when the table has no visible title.
    * - ``size``
      - string
      - ``md``
      - The row height. Set it to ``xs``, ``sm``, ``md``, ``lg``, or ``xl`` to match the density of the content.
    * - ``selection``
      - string
      - None
      - ``multi`` for a checkbox on each row, or ``single`` for a radio button on each row. Leave it out for rows that readers don't select.
    * - ``batchActions``
      - array
      - Empty array
      - Buttons for the selected rows. The template shows them only when ``selection`` is ``multi``.
    * - ``toolbarActions``
      - array
      - Empty array
      - Buttons in the toolbar at the top of the table, such as a button that creates a record.
    * - ``searchable``
      - boolean
      - ``false``
      - Set to ``true`` to add a search box that hides the rendered rows whose text doesn't match.
    * - ``searchPlaceholder``
      - string
      - ``mautic.core.search.placeholder``
      - The placeholder text of the search box.
    * - ``expandable``
      - boolean
      - ``false``
      - Set to ``true`` to let rows with an ``expansion`` show and hide their detail.
    * - ``batchExpansion``
      - boolean
      - ``false``
      - Set to ``true`` to add a header button that expands or collapses every row. Requires ``expandable``.
    * - ``loading``
      - boolean
      - ``false``
      - Set to ``true`` while the data loads. The table shows placeholder rows instead of ``rows``.
    * - ``emptyMessage``
      - string
      - ``mautic.core.data_table.empty``
      - The text shown when ``rows`` is empty or no row matches the search. The default key shows 'No data to display'.
    * - ``zebra``
      - boolean
      - ``false``
      - Set to ``true`` to shade every other row.
    * - ``stickyHeader``
      - boolean
      - ``false``
      - Set to ``true`` to keep the header visible while the rows scroll.
    * - ``maxHeight``
      - string
      - ``30rem``
      - The height at which the rows start to scroll, as a CSS length. Applies only when ``stickyHeader`` is ``true``.
    * - ``topAligned``
      - boolean
      - ``false``
      - Set to ``true`` to align cell content to the top of the row, for rows with cells of different heights.
    * - ``target``
      - string
      - ``.page-list``
      - The CSS selector of the element that Mautic loads the sorted list into when the reader selects a ``sortHref`` header.
    * - ``className``
      - string
      - None
      - Extra CSS classes for the wrapper element.

.. _data table column options:

Column options
==============

Each entry in ``columns`` accepts these keys. You must set ``key`` and ``label``.

.. list-table::
    :header-rows: 1
    :widths: 20 10 15 55

    * - Key
      - Type
      - Default
      - Description
    * - ``key``
      - string
      - None
      - The name of the column. Each row's ``cells`` uses it to give the column's value.
    * - ``label``
      - string
      - None
      - The column header text, or a translation key.
    * - ``sortable``
      - boolean
      - ``false``
      - Set to ``true`` to sort the rendered rows by this column in the browser.
    * - ``sortHref``
      - string
      - None
      - A URL that loads the list sorted by this column. The header becomes a link that Mautic loads through AJAX. When you set it, the template ignores ``sortable``.
    * - ``sort``
      - string
      - None
      - The column's current sort direction, ``asc`` or ``desc``. Use it with ``sortHref``.
    * - ``align``
      - string
      - ``start``
      - Set to ``end`` to align the header and cells to the end of the column, for numbers.
    * - ``width``
      - string
      - None
      - The column width, as a CSS length.
    * - ``className``
      - string
      - None
      - Extra CSS classes for the column's header and cells, such as ``visible-md visible-lg`` to hide the column on small screens.

.. _data table row options:

Row options
===========

Each entry in ``rows`` accepts these keys. All of them are optional.

.. list-table::
    :header-rows: 1
    :widths: 20 10 15 55

    * - Key
      - Type
      - Default
      - Description
    * - ``id``
      - string or number
      - The row's zero-based position in ``rows``
      - The row's identifier. It's the ``value`` of the row's selection input.
    * - ``cells``
      - map
      - Empty map
      - The row's values, keyed by column ``key``. A column without a value renders an empty cell. See :ref:`Cell values <data table cell values>`.
    * - ``isSelected``
      - boolean
      - ``false``
      - Set to ``true`` to render the row as selected.
    * - ``isDisabled``
      - boolean
      - ``false``
      - Set to ``true`` to turn off the row's selection input.
    * - ``name``
      - string
      - The table ``id`` followed by ``-select[]``
      - The ``name`` attribute of the row's checkbox, for a ``<form>`` that submits the selection. Applies only when ``selection`` is ``multi``.
    * - ``selectionClassName``
      - string
      - None
      - Extra CSS classes for the row's selection input.
    * - ``selectionAttr``
      - map
      - None
      - Extra HTML attributes for the row's selection input. Set an attribute to ``false`` to leave it out.
    * - ``className``
      - string
      - None
      - Extra CSS classes for the row.
    * - ``expansion``
      - string
      - None
      - HTML detail for the row, shown when the reader expands it. The template sanitizes it with the ``purify`` filter. Requires the table's ``expandable`` option.
    * - ``isExpanded``
      - boolean
      - ``false``
      - Set to ``true`` to render the row expanded.
    * - ``actions``
      - array
      - Empty array
      - The row's actions, shown in an overflow menu. Each action accepts ``label``, ``href``, ``icon`` - a Remix Icon class - ``danger`` to show it in the error color, and ``attr`` for extra HTML attributes.
    * - ``actionsHtml``
      - string
      - None
      - HTML for the row's actions cell, used instead of ``actions``. The template doesn't escape or sanitize it, so pass only HTML that your template rendered.

.. _data table cell values:

Cell values
===========

A cell value can be a string or a number, which the template escapes as HTML. To format the cell, pass a map with these keys instead:

* ``label`` - the cell text. The template escapes it as HTML.
* ``html`` - HTML content, which the template sanitizes with the ``purify`` filter. It replaces ``label``.
* ``trustedHtml`` - HTML content that the template doesn't escape or sanitize, such as the output of an ``include``. It replaces ``html`` and ``label``. Pass only HTML that your template rendered.
* ``icon`` - an icon class, such as ``ri-mail-line``, shown before the content.
* ``href`` - a URL. The template wraps the content in a link.
* ``className`` and ``attr`` - extra CSS classes and HTML attributes for the cell content. Set an attribute to ``false`` to leave it out.
* ``sortValue`` - the value that browser sorting uses for the cell. Set it when the cell shows HTML or formatted text. Without it, sorting uses ``label``.

.. code-block:: twig

   cells: {
       name: { label: world.name, href: path('helloworld_world_action', {objectAction: 'view', objectId: world.id}), attr: { 'data-toggle': 'ajax' } },
       visits: { label: world.visits|number_format, sortValue: world.visits },
       dateAdded: { label: dateToDate(world.dateAdded), attr: { title: dateToFullConcat(world.dateAdded) } }
   }

Loading tables with JavaScript
******************************

Mautic sets up every data table in content it loads, so tables in your views and in AJAX responses that Mautic renders work without extra JavaScript. When your own JavaScript inserts a table into the document, call ``Mautic.initDataTable()`` with the inserted element, so the selection, the batch actions, and the header's expand-all button match the rows you rendered as selected or expanded.

.. code-block:: javascript

   mQuery('#helloworld-worlds-wrapper').html(response.html);
   Mautic.initDataTable('#helloworld-worlds-wrapper');
