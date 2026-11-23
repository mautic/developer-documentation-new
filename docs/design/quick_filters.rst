Quick filters for searches
##########################

Quick filters provide an efficient way to search using existing search commands. You can add quick filters to any list view that includes the list toolbar.

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

* ``search``: the search query to apply
* ``label``: the displayed text for the filter button
* ``tooltip``: the tooltip text shown on hover
* ``icon``: the CSS class for the icon displayed on the button

Multiple quick filters
======================

You can define multiple quick filters by adding more items to the ``quickFilters`` array:

.. code-block:: twig

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
