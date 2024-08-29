Quick filters for searches
==========================

Quick filters provide an efficient way to search using existing search commands. This documentation outlines how to create and implement new quick filters for Mautic searches.

Implementation overview
-----------------------

Quick filters are implemented using a combination of JavaScript and Twig templates. The process involves three main components:

1. JavaScript function for applying the filter
2. Twig template for rendering filter buttons
3. Array of PHP code for defining filter options

JavaScript functionality
------------------------

The ``Mautic.listQuickFilter`` function is responsible for applying the quick filter:

.. code-block:: javascript

   Mautic.listQuickFilter = function (element) {
       const filterValue = element.dataset.filter;
       const searchInput = document.getElementById('list-search');
       searchInput.value = filterValue;
       const enterKeyEvent = new KeyboardEvent('keyup', {
           keyCode: 13
       });
       searchInput.dispatchEvent(enterKeyEvent);
   }

This function performs the following actions:

1. Retrieves the filter value from the clicked element's ``data-filter`` attribute
2. Sets the search input field's value to the filter value
3. Simulates an Enter key press to trigger the search

Twig template
-------------

The quick filter buttons are rendered using a Twig template:

.. code-block:: twig

   {% if quickFilters is defined and quickFilters is not empty %}
   <div class="d-flex gap-xs">
       {% for quickFilter in quickFilters %}
           <a class="label label-outline"
              data-filter="{{ quickFilter.search }}"
              onclick="Mautic.listQuickFilter(this)"
              data-toggle="tooltip"
              data-placement="top"
              data-original-title="{{ quickFilter.tooltip|trans }}">
               <i class="{{ quickFilter.icon }}"></i>
               {{ quickFilter.label|trans }}
           </a>
       {% endfor %}
   </div>
   {% endif %}

This template iterates through the provided quick filters and creates clickable labels for each one on the toolbar.

Implementing quick filters
--------------------------

To add quick filters to a list view, include the ``list_toolbar.html.twig`` template and pass the ``quickFilters`` option:

.. code-block:: twig

   {{ include('@MauticCore/Helper/list_toolbar.html.twig', {
       'searchValue': searchValue,
       'searchHelp': 'mautic.form.form.help.searchcommands',
       'searchId': 'list-search',
       'action': currentRoute,
       'quickFilters': [
           {
               'search': 'has:results',
               'label': 'mautic.core.search.quickfilter.form_results',
               'tooltip': 'mautic.core.search.quickfilter.form_results.tooltip',
               'icon': 'ri-file-list-2-line'
           }
       ]
   }) }}

Quick filter options
--------------------

Each quick filter is defined as an associative array with the following keys:

- ``search``: The search query to be applied
- ``label``: The displayed text for the filter button
- ``tooltip``: The tooltip text shown on hover
- ``icon``: The CSS class for the icon displayed on the button

Multiple quick filters
----------------------

You can define multiple quick filters by adding more items to the ``quickFilters`` array:

.. code-block:: php

   'quickFilters': [
       {
           'search': 'is:admin',
           'label': 'mautic.user.role.form.isadmin',
           'tooltip': 'mautic.core.search.quickfilter.is_admin',
           'icon': 'ri-admin-line'
       },
       {
           'search': 'is:published',
           'label': 'mautic.core.form.active',
           'tooltip': 'mautic.core.search.quickfilter.is_published',
           'icon': 'ri-check-line'
       },
       {
           'search': 'is:unpublished',
           'label': 'mautic.core.form.inactive',
           'tooltip': 'mautic.core.search.quickfilter.is_unpublished',
           'icon': 'ri-close-line'
       }
   ]
