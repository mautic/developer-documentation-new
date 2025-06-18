Views
=====

Views in Mautic use a consistent naming pattern to help you organize and locate templates efficiently.

- list: View and manage all objects in a table format, such as contacts or campaigns. This page provides an overview and allows you to take actions on multiple items.
- details: Access detailed information about a single object, such as a contact profile. You see all available data and related actions for the specific item.
- form: Enter or update information for a single object, such as creating or editing a contact. You fill in required fields and submit your changes.

These templates might have parts splitted into different files, for example, the list template might have a ``_list.html.twig`` file for the table and a ``_list_actions.html.twig`` file for actions.
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

Template naming and organization best practices
"""""""""""""""""""""""""""""""""""""""""""""""

Use consistent and descriptive naming for your templates to make them easy to locate and understand. Organize related partial templates into subfolders to improve clarity, especially when a single view includes multiple partials.

Previous template organizations often placed partial templates in the same folder as their parent view, using a leading underscore to identify partials. For example, the ``@MauticPage/Page/`` folder included:
- list.html.twig
- form.html.twig
- details.html.twig
- _list.html.twig

The file ``_list.html.twig`` served as a partial for rendering tables within the list view.

With the current standard, group all partials for a specific view inside a subfolder named after the parent template. Rename partials to follow a clear pattern, and remove the leading underscore. For instance, in ``@MauticPage/Page/``, organize files as follows:
- list.html.twig
- form.html.twig
- details.html.twig
- List/list--table.html.twig

Move the partial ``_list.html.twig`` to ``List/list--table.html.twig``. This approach organizes partials for the list view under the ``List`` subfolder, making it easier to locate and understand their context.

Apply similar patterns to other UI elements. For example, organize tab partials as ``Details/details--tab-overview.html.twig`` within a ``Details`` subfolder. For module templates, create a ``Modules`` folder under the appropriate bundle, such as ``app/bundles/[Name]Bundle/Resources/views/Modules/``, and use descriptive names like ``module--preview.html.twig``.

Consistent and descriptive naming conventions help you and your team quickly find and identify templates, improving maintainability and collaboration.

.. note::

   Mautic is actively updating templates to follow this organization standard. Some templates still use the older structure, and the transition will continue over time.
