Views
=====

Views in Mautic use a consistent naming pattern to help you organize and locate templates efficiently.

- list: This is the table view, where the list of objects is displayed. These are high level pages (for example, Contacts, Campaigns, etc)
- details: This is the view for a single object (for example, a Contact profile)
- form: This is the form view, where the form for creating or editing a single object is displayed (for example, the New Contact page)

These templates might have parts splitted into different files, for example, the list template might have a ``_list.html.twig`` file for the table and a ``_list_actions.html.twig`` file for the actions.
Details templates might have an associated Details folder with files for each tab contents to help with organization and maintainability.

Platform templates
------------------

Mautic provides several Twig templates to help you streamline development and maintain consistency. Templates are organized by their purpose and functionality.

You will find these main folders:

- ``@MauticCore/Helper`` contains templates for common tasks, such as rendering buttons for page actions.
- ``@MauticCore/Components`` includes templates that implement design patterns from the design system for a wide variety of content.
- ``@MauticCore/Modules`` provides templates that combine Components for specific content types, such as using tile components to display statistics.

You will also find module folders inside specific bundles for templates unique to that bundle. These templates are not intended for reuse across other bundles.

.. note::

   Use existing platform templates to maintain consistency and reduce code duplication.

Modifying templates
^^^^^^^^^^^^^^^^^^^

Allowing custom attributes
""""""""""""""""""""""""""

Before you add, remove, or change variables in a template, first check whether you can accomplish your goal by supporting custom attributes. Many Mautic templates already allow you to pass custom attributes, which lets you adapt behavior or appearance without changing the template’s structure. This approach works well when you need to integrate with JavaScript libraries such as Bootstrap.

You can allow custom attributes by adding this snippet to your template:

.. code-block:: twig

    {% if attributes is defined and attributes is not empty %}
        {% for attr_key, attr_value in attributes %}
            {{ attr_key }}="{{ attr_value }}" 
        {% endfor %}
    {% endif %}

When you include your template, pass the attributes as follows:

.. code-block:: twig

    {% include '@MauticCore/Components/clickable-component.html.twig' with {
        'content': 'Open Modal',
        'icon': 'fa fa-external-link',
        'attributes': {
            'data-toggle': 'ajaxmodal',
            'data-target': '#HelpModal',
            'data-header': 'Modal Title'
        }
    } %}

Changing template structure
"""""""""""""""""""""""""""

Templates power features throughout the platform. When you change a variable or structure in a template, you affect every place that uses it. Consider the impact before making changes.

You have several options:

1. Update all usages to work with the new structure.
2. Create a new template with your changes, and add a deprecation notice to the old template. Use the new template instead of the original.
3. Add support for custom attributes if that satisfies your needs.

.. note::

   Use a platform template instead of custom HTML whenever possible. If a pull request adds a button with raw HTML, reviewers require you to switch to a platform template.

Naming and organization of templates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When naming templates, it's important to follow the same naming pattern used by the platform. This makes it easier for other developers to understand the purpose of the template and to find it when needed. 

Names must indicate the part of the UI they're responsible for.

Before, the naming standard worked this way (example):

The folder ``@MauticPage/Page/`` had these files:
- list.html.twig
- form.html.twig
- details.html.twig
- _list.html.twig

_list.html.twig was a partial template included in list.html.twig at the same folder level, used to render a table for the list of pages in the list view. 
Names usually started with an underscore to indicate it was a partial template.

Now, the folder ``@MauticPage/Page/`` would have this structure:
- list.html.twig
- form.html.twig
- details.html.twig
- List/list--table.html.twig

_list.html.twig was renamed to list--table.html.twig and moved to the List subfolder. The new organization standard involves creating a subfolder to group partial elements from different views. This makes it easier to find and understand the purpose of each template when searching files in IDEs, mainly when a single view has dozens of partial templates.

Other examples:
- For tabs, you can use names such as ``Details/details--tab-overview.html.twig``
- For modules, create a folder named ``@MauticBundle/Modules/`` (considering full path app/bundles/[Name]Bundle/Resources/views/Modules/) and use names such as ``module--preview.html.twig``

.. note::

   Mautic is actively updating templates to follow this organization standard. Some templates still use the older structure, and the transition will continue over time.
