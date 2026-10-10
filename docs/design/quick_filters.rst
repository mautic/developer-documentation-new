Quick filters for searches
##########################

Quick filters provide an efficient way to search using existing search commands. This documentation outlines how to create and implement new quick filters for Mautic searches.

Implementation overview
***********************

Mautic implements quick filters using a combination of JavaScript and Twig templates. The process involves three main components:

1. JavaScript function for applying the filter
2. Twig template for rendering filter buttons
3. Array of PHP code for defining filter options

JavaScript functionality
========================

The ``Mautic.toggleFilter`` function toggles a quick filter button's active state, and ``Mautic.applyFilters`` applies all active quick filters to the search input:

.. code-block:: javascript

   Mautic.toggleFilter = function (element) {
       const filterValue = element.dataset.filter;
       const conflictGroup = element.dataset.conflictGroup || null;

       // If the filter is in a conflict group, deactivate other filters in the same group
       if (conflictGroup) {
           const filtersInGroup = document.querySelectorAll(`.label[data-conflict-group="${conflictGroup}"]`);
           filtersInGroup.forEach(function (filterElement) {
               if (filterElement !== element) {
                   filterElement.classList.remove('active');
               }
           });
       }

       // Toggle active class on the clicked element
       element.classList.toggle('active');
   };

This function performs the following actions:

1. Retrieves the filter value from the clicked element's ``data-filter`` attribute.
2. If the filter belongs to a conflict group - for example ``status`` or ``ownership`` - deactivates any other active filter in the same group, so only one filter per group applies at a time.
3. Toggles the ``active`` class on the clicked element.

``Mautic.applyFilters`` then collects every element with the ``active`` class and appends its ``data-filter`` value to the search input before triggering the search.

Twig template
=============

Mautic renders the quick filter buttons using the ``list_quickfilters.html.twig`` Twig template, which groups filters by status and ownership and renders each as a label that toggles active state on click:

.. code-block:: twig

   {% if quickFilters is defined and quickFilters is not empty %}
       {% for filter in quickFilters %}
           <a class="label label-outline label-selectable"
              data-filter="{{ filter.search|trans }}"
              onclick="Mautic.toggleFilter(this)"
              data-toggle="tooltip"
              data-placement="top"
              data-original-title="{{ filter.tooltip|trans }}">
               <i class="{{ filter.icon }}"></i>
               {{ filter.label|trans }}
           </a>
       {% endfor %}
   {% endif %}

This template iterates through the provided quick filters and creates clickable labels that toggle on and off for each one on the toolbar.

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
