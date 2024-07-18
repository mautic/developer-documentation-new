Accordion Component
===================

Introduction
------------

The Accordion component allows developers to create collapsible sections within their Mautic templates. This component is useful for organizing content into expandable and collapsible panels, enhancing the user experience by making large amounts of content more manageable.

Template Structure
------------------

This accordion component is defined in the ``accordion.html.twig`` template. It uses a list structure (``<ul>``) where each item (``<li>``) represents an accordion panel. Each panel consists of a heading and a collapsible content section.

Key features
^^^^^^^^^^^^

- Each accordion item can be expanded or collapsed by clicking on the heading.
- The component includes ARIA attributes to improve accessibility.
- The content of each accordion panel can be customized using Twig variables.

Applying the Accordion Component
--------------------------------

To use the accordion component, include it in your template and pass the necessary data.

Define the content you want to include in the accordion. For example, if you want to include a group of UTM tags fields, you can define the content as follows:

.. code-block:: twig

   {% set utmTagsContent %}
       {% for i, utmTag in form.utmTags %}
           {{ form_row(utmTag) }}
       {% endfor %}
   {% endset %}

.. note::
   For instance, you can loop over form fields or any other data to generate the content dynamically.

Include the accordion.html.twig template in your main template and pass an array of items. Each item should have:

- ``id``: A unique identifier.
- ``title``: The title of the accordion item.
- ``padding_inline``: (Optional) Boolean to control padding within the content. Defaults to true if not defined.
- ``content``: The content to be displayed when the item is expanded.

Example:

.. code-block:: twig

   {% include '@MauticCore/Helper/accordion.html.twig' with {
       'items': [
           {
               'id': 'UTM',
               'title': 'mautic.email.utm_tags',
               'padding_inline': false,
               'content': utmTagsContent,
           }
       ]
   } %}

While defining a ``set`` block separately is not strictly necessary, it can be helpful to ensure that operations relying on Twig functions keep working correctly. The ``set`` block allows you to predefine complex content or operations, making your template cleaner and more maintainable.

Example without the ``set`` Block
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If your content is simple, you can directly include it within the ``items`` array without using a ``set`` block. Here's an example:

.. code-block:: twig

   {% include '@MauticCore/Helper/accordion.html.twig' with {
       'items': [
           {
               'id': 'Example',
               'title': 'Example Title',
               'padding_inline': true,
               'content': '<p>This is a simple content example.</p>',
           }
       ]
   } %}

This flexibility allows you to choose the best approach based on each case.

Automatic CSS handling
----------------------

When using the component, all necessary CSS styles are automatically handled for you. This means that the component comes pre-styled with classes such as ``accordion-heading``, ``accordion-wrapper``, and ``accordion-content``, ensuring a consistent and visually appealing appearance out of the box.

- The component includes predefined CSS classes that manage the layout, spacing, and interactive elements of the accordion.
- You do not need to add any extra CSS to make the accordion functional and visually appealing.
- It uses the existing Bootstrap functionality for collapsing panels.
- Avoid overriding these classes in your own CSS.

The accordion is designed to be easy to implement, with all essential CSS styles already in place. This allows you to focus on integrating and using the component without worrying about additional styling.

Complete example
----------------

Here is a complete example that demonstrates how to use the accordion component in a Mautic template:

.. code-block:: twig

   {% set utmTagsContent %}
       {% for i, utmTag in form.utmTags %}
           {{ form_row(utmTag) }}
       {% endfor %}
   {% endset %}

   {% include '@MauticCore/Helper/accordion.html.twig' with {
       'items': [
           {
               'id': 'UTM',
               'title': 'mautic.email.utm_tags',
               'padding_inline': false,
               'content': utmTagsContent,
           }
       ]
   } %}

For more complex structures, with dozens of accordion items, you might prefer to copy the structure and build something unique, but the best approach would be to place each content under a set block.