Tabs template
#############

The ``tabs.html.twig`` template renders a tab list and its tab panels in Mautic's tab style. Use it when your template splits content into tabs, so the tabs look and behave like the tabs on Mautic's own detail and edit screens, such as the Contact, Segment, Report, and Campaign views.

The template wraps the tabs in a ``<div class="tabs-container">``. It renders the tab list as a ``<ul class="nav nav-tabs">`` with one ``<li class="nav-item">`` per tab. Each tab is a ``<button>`` with ``data-bs-toggle="tab"`` and a ``data-bs-target`` attribute that identifies its panel. The panels follow in a ``<div class="tab-content">``, each as a ``<div class="tab-pane">``.

Including the template
**********************

Include ``@MauticCore/Components/tabs.html.twig`` and pass a ``tabs`` array with one entry per tab. Each entry's ``content`` is the HTML of its panel, so render the panel content first, for example with ``include()`` or a ``{% set %}`` block.

.. code-block:: twig

   {% set settingsContent %}
       {{ form_row(form.name) }}
       {{ form_row(form.description) }}
   {% endset %}

   {{ include('@MauticCore/Components/tabs.html.twig', {
       variant: 'contained',
       tabs: [
           {
               id: 'helloworld-settings',
               label: 'plugin.helloworld.tab.settings',
               className: 'pa-md',
               content: settingsContent
           },
           {
               id: 'helloworld-history',
               label: 'plugin.helloworld.tab.history',
               className: 'pa-md',
               renderTag: {label: historyCount, attributes: {id: 'HelloWorldHistoryCount'}},
               content: include('@HelloWorld/World/history.html.twig', {world: world})
           }
       ]
   }) }}

The template passes each tab's ``label`` through Twig's ``trans`` filter, so you can pass translation keys or plain strings. It outputs ``content`` with the ``raw`` filter and doesn't escape it, so escape any User-supplied values when you build the content.

Mautic remembers the last tab a User opened in each tab list and opens it again when the User reloads the page. Pages whose path ends in ``/new``, such as the page for creating a Segment, always open the tab that ``selectedIndex`` sets.

Template options
================

These options apply to the whole tab list. All of them are optional except ``tabs``.

.. list-table::
    :header-rows: 1
    :widths: 25 10 15 50

    * - Option
      - Type
      - Default
      - Description
    * - ``tabs``
      - array
      - None
      - The tabs to render, in order. See :ref:`Tab options <tabs tab options>` for the keys each tab accepts.
    * - ``variant``
      - string
      - ``line``
      - The tab style. Use ``line`` for tabs with an underline, ``contained`` for tabs with a background, such as the tabs on the Contact detail view, ``iconOnly`` for tabs that show only an icon or a tag, or ``vertical`` for contained tabs stacked in a column.
    * - ``selectedIndex``
      - integer
      - ``0``
      - The zero-based position of the tab that's open when the page loads.
    * - ``layer``
      - string
      - ``two``
      - The background layer for the panels of ``contained`` and ``vertical`` tabs. The template adds it to each panel as the ``layer-{layer}`` class.
    * - ``iconSize``
      - string
      - None
      - Set to ``lg`` to show larger icons in ``iconOnly`` and ``vertical`` tabs.

.. _tabs tab options:

Tab options
===========

Each entry in ``tabs`` accepts these keys. All of them are optional, but each tab needs a ``label`` and usually ``content``.

.. list-table::
    :header-rows: 1
    :widths: 25 10 20 45

    * - Key
      - Type
      - Default
      - Description
    * - ``label``
      - string
      - Empty string
      - The tab's text, or a translation key. ``iconOnly`` tabs use it as the tab's ``title``.
    * - ``id``
      - string
      - Built from ``label``
      - The panel ``id``. The tab's ``data-bs-target`` is ``#{id}``, and the tab button's ``id`` is ``{id}-tab``. When you don't set it, the template joins the last two dot-separated parts of ``label`` with a hyphen and converts the result to lowercase. For example, ``plugin.helloworld.tab.settings`` gives ``tab-settings``. Set an explicit ``id`` so that tab IDs are unique on the page and JavaScript can find them.
    * - ``content``
      - string
      - None
      - The panel's HTML.
    * - ``className``
      - string
      - None
      - Extra CSS classes for the panel, such as ``pa-md`` for padding.
    * - ``paneAttributes``
      - map
      - Empty map
      - Extra HTML attributes for the panel.
    * - ``itemClass``
      - string
      - None
      - Extra CSS classes for the ``<li>``, such as ``hide`` to hide the tab.
    * - ``itemAttributes``
      - map
      - Empty map
      - Extra HTML attributes for the ``<li>``.
    * - ``attributes``
      - map
      - Empty map
      - Extra HTML attributes for the tab ``<button>``, such as ``data-*`` attributes. An ``id`` entry replaces the button's default ``id``.
    * - ``renderIcon``
      - string
      - None
      - The CSS class of an icon to show next to the label, such as ``ri-mail-line``.
    * - ``renderTag``
      - map
      - None
      - A tag to show next to the label, such as a counter. The template passes the map to ``@MauticCore/Helper/_tag.html.twig``, so it accepts that template's keys, such as ``label`` and ``attributes``. The tag's ``color`` defaults to ``primary`` and its ``size`` to ``sm``. When you set both ``renderTag`` and ``renderIcon``, the tab shows only the tag.
    * - ``secondaryLabel``
      - string
      - None
      - A second line of text, or a translation key, below the label of a ``contained`` or ``vertical`` tab.
    * - ``hasError``
      - boolean
      - ``false``
      - Set to ``true`` to show the tab's label in the danger color with an alert icon, for example when the tab contains a Form Field that failed validation.
    * - ``disabled``
      - boolean
      - ``false``
      - Set to ``true`` to show the tab as unavailable. Users can't select it. See :doc:`/design/availability`.

Working with tabs in JavaScript
*******************************

Each tab is a ``<button>`` without an ``href``, so find a tab by its ``data-bs-target`` attribute. For example, this code opens the panel with the ``id`` ``helloworld-history``.

.. code-block:: javascript

   mQuery('[data-bs-target="#helloworld-history"]').tab('show');

To run code when a User opens a tab, listen for Bootstrap's ``shown.bs.tab`` event. The event's ``target`` is the tab button, so read the panel from its ``data-bs-target`` attribute.

.. code-block:: javascript

   mQuery('[data-bs-target="#helloworld-history"]').on('shown.bs.tab', function (e) {
       const panelId = mQuery(e.target).attr('data-bs-target');
       // Load the panel's content, for example with an AJAX request.
   });

Adding tabs to the Contact detail view
**************************************

The Contact detail view, ``@MauticLead/Lead/lead.html.twig``, renders its own tabs with this template. A Plugin can add tabs to it through the ``tabs`` and ``tabs.content`` contexts of the ``customContent`` Twig function, which dispatches the ``\Mautic\CoreBundle\CoreEvents::VIEW_INJECT_CUSTOM_CONTENT`` event. For how to subscribe to the event and confirm the context, see :ref:`Injecting custom content <plugin_extensions/ui:Injecting custom content>`.

* Content added to the ``tabs`` context renders inside a separate ``<ul class="nav nav-tabs nav-tabs--contained">`` below the core tabs. Add each tab as an ``<li class="nav-item">`` that contains a ``<button>`` with ``data-bs-toggle="tab"`` and ``data-bs-target``.
* Content added to the ``tabs.content`` context renders inside a separate ``<div class="tab-content">``. Add each panel as a ``<div class="tab-pane">`` with the ``id`` the tab targets.

.. code-block:: twig

   {# @HelloWorld/Contact/tab.html.twig, added to the 'tabs' context #}
   <li class="nav-item" role="presentation">
       <button type="button" id="helloworld-container-tab" class="nav-link tabs__nav-item" data-bs-toggle="tab" data-bs-target="#helloworld-container" role="tab" aria-controls="helloworld-container" aria-selected="false">
           <span class="tabs__nav-item-label">{{ 'plugin.helloworld.tab.worlds'|trans }}</span>
       </button>
   </li>

   {# @HelloWorld/Contact/tab_content.html.twig, added to the 'tabs.content' context #}
   <div class="tab-pane fade pa-md" id="helloworld-container" role="tabpanel" aria-labelledby="helloworld-container-tab">
       {# The tab's content #}
   </div>

Because Plugin tabs sit in their own tab list, they don't switch together with the core tabs.
