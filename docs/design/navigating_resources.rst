Views
#####

Views in Mautic use a consistent naming pattern to help you organize and locate templates efficiently.

* **List**: view and manage all objects in a table format, such as Contacts or Campaigns. This provides an overview and allows you to take actions on multiple items.
* **Details**: access detailed information about a single object, such as a Contact profile. This view displays all available data and related actions for the specific item.
* **Form**: enter or update information for a single object, such as creating or editing a Contact. Use this to fill in required fields and submit changes.

Mautic may split these templates into different files. For example, the List template might use a ``_list.html.twig`` file for the table and a ``_list_actions.html.twig`` file for actions.

Details templates might include an associated ``Details`` folder with files for each tab's content to improve organization and maintainability.

Platform templates
******************

Mautic provides several Twig templates, organized by purpose and feature set, to help you streamline development and maintain consistency.

The system organizes templates into these main folders:

* ``@MauticCore/Helper``: contains templates for common tasks, such as rendering buttons for actions.
* ``@MauticCore/Components``: includes templates that implement design patterns from the design system for various content.
* ``@MauticCore/Modules``: provides templates that combine Components for specific content types, such as using tile Components to display statistics.

You also find module folders inside specific bundles for templates unique to those bundles. Don't reuse these templates across other bundles.

.. note::

   Use existing platform templates to maintain consistency and reduce code duplication.

Modifying templates
===================

Allowing custom attributes
--------------------------

Before you add, remove, or change variables in a template, verify whether you can accomplish your goal by supporting custom attributes. Many Mautic templates already allow you to pass custom attributes. This lets you adapt behavior or appearance without changing the template’s structure, which is useful when integrating with JavaScript libraries, such as Bootstrap.

To allow custom attributes, add this snippet to your template:

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
---------------------------

Templates power features throughout the platform. When you change a variable or structure in a template, you affect every part of Mautic that uses it. Consider the impact before making changes.

You have several options:

#. Update all usages to work with the new structure.
#. Create a new template with your changes and add a deprecation notice to the old template. Use the new template instead of the original.
#. Add support for custom attributes if that satisfies your requirements.

.. note::

   Use a platform template instead of custom HTML whenever possible. If a pull request adds a button with raw HTML, reviewers require you to switch to a platform template.

Naming and organization of templates
====================================

Follow the naming pattern used by the platform when naming templates. This helps other developers understand the template's purpose and locate it quickly. Names must indicate the part of the UI they represent.

Template naming and organization best practices
-----------------------------------------------

Use consistent and descriptive naming for your templates to make them easy to locate and understand. Organize related partial templates into folders to improve clarity, especially when a single view includes multiple partials.

Previous template organizations often placed partial templates in the same folder as their parent view, using a leading underscore to identify partials. For example, the ``@MauticPage/Page/`` folder included:

* ``list.html.twig``
* ``form.html.twig``
* ``details.html.twig``
* ``_list.html.twig``

The file ``_list.html.twig`` served as a partial for rendering tables within the List view.

Current standards require grouping all partials for a specific view inside a folder named after the parent template. Rename partials to follow a clear pattern and remove the leading underscore. For instance, in ``@MauticPage/Page/``, organize files as follows:

* ``list.html.twig``
* ``form.html.twig``
* ``details.html.twig``
* ``List/list--table.html.twig``

Move the partial ``_list.html.twig`` to ``List/list--table.html.twig``. This approach organizes partials for the list view under the ``List`` folder, making it easier to locate and understand their context.

Apply similar patterns to other UI elements. For example, organize tab partials as ``Details/details--tab-overview.html.twig`` within a ``Details`` folder. For module templates, create a ``Modules`` folder under the appropriate bundle, such as ``app/bundles/[Name]Bundle/Resources/views/Modules/``, and use descriptive names such as ``module--preview.html.twig``.

Consistent and descriptive naming conventions help you and your team quickly find and identify templates, which improves maintainability and collaboration.

.. note::

   Mautic is actively updating templates to follow this organization standard. Some templates still use the older structure.
