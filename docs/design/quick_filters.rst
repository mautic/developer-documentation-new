Quick filters for searches
##########################

Quick filters let Users filter a list view by selecting predefined search commands instead of typing them. This documentation outlines how to add quick filters to a list view and organize them into named groups.

Implementation overview
***********************

Mautic implements quick filters using a combination of Twig templates and JavaScript:

* The ``list_toolbar.html.twig`` template accepts a ``quickFilters`` option that defines the filters for a list view.
* The ``list_quickfilters.html.twig`` template renders those filters as selectable labels in the **Quick filters** popover, under a header for each group.
* JavaScript in ``1a.content.js`` toggles the selected labels and adds their search commands to the search box when the User clicks **Apply selected**.

Implementing quick filters
==========================

To add quick filters to a list view, include the ``list_toolbar.html.twig`` template and pass the ``quickFilters`` option. Define ``quickFilters`` as a mapping of groups. Each key is the translation key for the group's header, and each value holds the group's filters:

.. code-block:: twig

   {{ include('@MauticCore/Helper/list_toolbar.html.twig', {
       'searchValue': searchValue,
       'action': currentRoute,
       'quickFilters': {
           'mautic.core.quick_filters.status': {
               'conflictGroup': true,
               'filters': [
                   {
                       'search': 'mautic.core.searchcommand.ispublished',
                       'label': 'mautic.core.form.active',
                       'tooltip': 'mautic.core.search.quickfilter.is_published',
                       'icon': 'ri-check-line'
                   },
                   {
                       'search': 'mautic.core.searchcommand.isunpublished',
                       'label': 'mautic.core.form.inactive',
                       'tooltip': 'mautic.core.search.quickfilter.is_unpublished',
                       'icon': 'ri-close-line'
                   }
               ]
           },
           'mautic.core.quick_filters.ownership': {
               'conflictGroup': true,
               'filters': [
                   {
                       'search': 'mautic.core.searchcommand.ismine',
                       'label': 'mautic.core.searchcommand.ismine.label',
                       'tooltip': 'mautic.core.searchcommand.ismine.description',
                       'icon': 'ri-user-line'
                   }
               ]
           },
           'mautic.core.quick_filters.others': {
               'filters': [
                   {
                       'search': 'has:results',
                       'label': 'mautic.core.search.quickfilter.form_results',
                       'tooltip': 'mautic.core.search.quickfilter.form_results.tooltip',
                       'icon': 'ri-file-list-2-line'
                   }
               ]
           }
       }
   }) }}

Mautic shows the groups in the order you define them and skips any group without filters. Core provides these group keys and headers:

* ``mautic.core.quick_filters.status`` shows **Statuses**
* ``mautic.core.quick_filters.ownership`` shows **Ownership**
* ``mautic.core.quick_filters.others`` shows **Others**

To add a group of your own, use a translation key from your Plugin as the group key, and define its header text in your Plugin's translations.

Group options
=============

Each group accepts the following keys:

* ``filters``: the list of quick filters in the group. Each filter uses the options described in the following section.
* ``conflictGroup``: optional. Set it to ``true`` when the group's filters exclude each other, such as **Active** and **Inactive**. Selecting one filter in a conflict group deselects the other filters in that group. Mautic uses the last part of the group key as the conflict group's name, for example ``status`` for ``mautic.core.quick_filters.status``.

Leave ``conflictGroup`` out when Users can combine the group's filters.

Quick filter options
====================

You define each quick filter as an associative array with the following keys:

* ``search``: the search command to apply, either as a translation key or as a literal command such as ``has:results``
* ``label``: the displayed text for the filter label
* ``tooltip``: the tooltip text shown on hover
* ``icon``: the CSS class for the icon displayed on the label

Quick filters without groups
============================

Mautic still accepts ``quickFilters`` as a flat list of filters without groups. In that case, the template sorts each filter into a group by its ``search`` value:

* **Statuses**: commands that contain ``ispublished``, ``isunpublished``, ``isexpired``, or ``ispending``
* **Ownership**: commands that contain ``ismine`` or ``isunowned``
* **Others**: every other command

Use the grouped format when a list view needs its own group or a different grouping.

How Mautic applies quick filters
================================

The ``list_quickfilters.html.twig`` template renders each filter as a label with the following attributes:

* ``data-filter``: the translated search command
* ``data-filter-action="toggle"``: marks the label as a selectable quick filter
* ``data-conflict-group``: the conflict group's name, when the filter's group sets ``conflictGroup``

When a User clicks a label, ``Mautic.toggleFilter`` toggles the label's ``active`` class and deactivates the other labels with the same ``data-conflict-group`` value. When the User clicks **Apply selected**, ``Mautic.applyFilters`` appends the ``data-filter`` value of each active label to the search box and runs the search. **Reset** removes the quick filter commands from the search box.
