Quick filters for searches
##########################

Quick filters provide an efficient way to search using existing search commands. This documentation outlines how to create and implement new quick filters for Mautic searches.

Implementation overview
***********************

Mautic implements quick filters using a combination of JavaScript and Twig templates. The process involves three main components:

#. JavaScript functions for selecting and applying filters
#. Twig template for rendering filter buttons
#. Array of PHP code for defining filter options

.. vale off

JavaScript functionality
========================

.. vale on

Each quick filter button has a ``data-filter-action`` attribute. Mautic handles clicks on any element with this attribute through a single delegated listener:

.. code-block:: javascript

   mQuery(document).on('click', '[data-filter-action]', function () {
       const action = this.dataset.filterAction;

       if ('toggle' === action) {
           Mautic.toggleFilter(this);
       } else if ('apply' === action) {
           Mautic.applyFilters();
       } else if ('reset' === action) {
           Mautic.resetFilters();
       }
   });

The value of ``data-filter-action`` selects the function that runs:

* ``toggle`` - ``Mautic.toggleFilter`` marks the clicked filter as active or inactive. If the filter has a ``data-conflict-group`` attribute, Mautic deactivates the other filters in the same group, so only one status filter or one ownership filter is active at a time.
* ``apply`` - ``Mautic.applyFilters`` adds the ``data-filter`` value of each active filter to the search input, then simulates an Enter key press to run the search. The **Apply selected** button uses this action.
* ``reset`` - ``Mautic.resetFilters`` removes the filter commands from the search input, deactivates all filters, and runs the search again. The **Reset** button uses this action.

Twig template
=============

Mautic renders the quick filter buttons using a Twig template:

.. code-block:: twig

   {% if quickFilters is defined and quickFilters is not empty %}
   <div class="d-flex gap-xs">
       {% for quickFilter in quickFilters %}
           <a class="label label-outline"
              data-filter="{{ quickFilter.search }}"
              data-filter-action="toggle"
              data-bs-toggle="tooltip"
              data-bs-placement="top"
              data-bs-title="{{ quickFilter.tooltip|trans }}">
               <i class="{{ quickFilter.icon }}"></i>
               {{ quickFilter.label|trans }}
           </a>
       {% endfor %}
   </div>
   {% endif %}

This template iterates through the provided quick filters and creates clickable labels for each one on the toolbar.

Implementing quick filters
==========================

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
====================

You define each quick filter as an associative array with the following keys:

- ``search``: the search query to apply
- ``label``: the displayed text for the filter button
- ``tooltip``: the tooltip text shown on hover
- ``icon``: the CSS class for the icon displayed on the button

Multiple quick filters
======================

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
