Views
=====

Views in Mautic follow a common naming pattern.

- list: This is the table view, where the list of objects is displayed. These are high level pages (for example, Contacts, Campaigns, etc)
- details: This is the view for a single object (for example, a Contact profile)
- form: This is the form view, where the form for creating or editing a single object is displayed (for example, the New Contact page)

These templates might have parts splitted into different files, for example, the list template might have a ``_list.html.twig`` file for the table and a ``_list_actions.html.twig`` file for the actions.
Details templates might have an associated Details folder with files for each tab contents to help with organization and maintainability.

Platform templates
------------------

There are several Twig templates available on the platform code to help developers streamline developemnt.

These templates are organized in folders depending on their purpose and functionality.

The main folders are:

- ``@MauticCore/Helper``: Templates that help with common tasks (rendering buttons for page actions, for example)
- ``@MauticCore/Components``: Templates that implement design patterns coming from the design system, suitable for any kind of content
- ``@MauticCore/Modules``: Templates that can be reused across several bundles for specific types of contents, built on top of Components (for example, to render a stats panel by using tile components)

Module folders can also be found within specific bundles. These folders contain templates that are specific to the bundle they are in, and are not reusable across other bundles. 

.. note::

   Always use platform templates for existing components to avoid code duplication and to ensure consistency across the platform. 

Modifying templates
^^^^^^^^^^^^^^^^^^^

Using attributes
""""""""""""""""

Before considering adding, removing or changing variables from a template, check if your needs could be addressed by allowing custom attributes if the template doesn't support it yet.

For example:

.. code-block:: twig

    {% if attributes is defined and attributes is not empty %}{% for attr_key, attr_value in attributes %}{{ attr_key }}="{{ attr_value }}" {% endfor %}{% endif %}

This snippet allows you to pass custom attributes to the template, which can be used to modify the behavior or appearance of the component. It's a common pattern in Mautic templates and is used in several platform templates, becoming useful for integrating with JS libraries such as Bootstrap. 

When including your template, you could pass the attributes as follows:

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
        
Changing existing structure from templates
""""""""""""""""""""""""""""""""""""""

Templates were created to power functionalities across the entire platform. You might find that a template is being applied more than 60 times in different scenarios across the UI. If you change a variable being used by a template, it will affect all the places where it is being used. 

Your options are:
1. Refactor or update all the places where it is being used to ensure they work with the new structure. 
2. Create a new template if you have a really good reason to do so and use it instead of the old one, adding a deprecation notice to the old template. 
3. Check if adding a custom attribute to the template would be enough to address your needs. 

.. note::

   Avoid creating custom HTML when a template is available. If a pull request is adding a button using raw HTML, reviewers must request changes to use a platform template instead. 

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

   You'll find that the new organization standard is not yet applied to all templates. This is a work in progress and will be completed in the future.
