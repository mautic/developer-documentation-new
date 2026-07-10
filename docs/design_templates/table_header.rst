Table header template
#####################

Introduction
************

The ``tableheader.html.twig`` template renders the ``<th>`` header cells for Mautic's list views. It handles the bulk-select checkbox column, plain non-sortable columns, and sortable or filterable columns, wiring up the sort links, per-column filter inputs, and session-persisted sort state for you. Include it once per column when you build a list table, rather than writing the header markup by hand.

Adding a header tooltip
***********************

Pass an optional ``tooltip`` key to show a tooltip when a User hovers over a column header. The tooltip works on plain non-sortable columns and on sortable or filterable columns, as well as the bulk-select checkbox column, which already supported it.

.. code-block:: twig

   {{ include('@MauticCore/Helper/tableheader.html.twig', {
       text: 'mautic.lead.list.header',
       tooltip: 'mautic.lead.list.header.tooltip',
       sessionVar: 'contact',
       orderBy: 'l.name',
   }) }}

Mautic passes ``tooltip`` through the ``trans`` filter, so you can supply either a translation key or a literal string. Reload the list view and hover over the column header to see the tooltip.

Columns that don't pass ``tooltip`` render as before, with no tooltip markup, so existing list views stay unaffected until you opt in.

You don't need any JavaScript setup. Mautic initializes tooltips globally for any element carrying ``data-toggle="tooltip"``, so emitting the attribute is enough for the tooltip to appear. Mautic escapes the value you pass with the ``html_attr`` filter before rendering it into the ``data-original-title`` attribute.

Common parameters
*****************

Configure the header by passing keys when you include the template. The most commonly used keys are:

* ``text``: the column label. Passed through the ``trans`` filter, so it accepts a translation key or a literal string.
* ``tooltip``: optional tooltip text shown on hover. Passed through the ``trans`` filter.
* ``sessionVar``: the session namespace for the list. When set, the header renders as a sortable or filterable column, and Mautic persists the sort and filter state under this key.
* ``orderBy``: the field to sort by. When set, the label becomes a clickable sort link; when omitted, it renders as a static label.
* ``class``: extra CSS class or classes to add to the ``<th>`` element.
* ``filterBy``: the field to filter by. When set, the header renders a per-column filter input.
* ``target``: the CSS selector for the table container that receives the sort and filter updates. Defaults to ``.page-list``.
