Category template
#################

The ``category.html.twig`` template shows the Category of an item, such as an Asset, Campaign, or Email, in Mautic's style. Use it when your Plugin's list or detail views show an entity's Category, so the Category looks the same as it does in Mautic's own views.

The template has two types:

* ``expanded`` shows a dot in the Category's color followed by the Category's title. Mautic uses it in the Category column of list views.
* ``inline`` shows the Category's color with a folder icon, and the Category's title in a tooltip that appears on hover. Mautic uses it at the top right of detail views.

.. vale off

When the item has no Category, or the Category has no title, the template shows 'Uncategorized' with a gray color. The ``expanded`` type also shows the 'Uncategorized' text in gray instead of the normal text color.

.. vale on

Including the template
**********************

Include ``@MauticCore/Components/category.html.twig`` with the ``only`` keyword, and pass the item's Category as ``category``. Without a ``type``, the template uses the ``expanded`` type.

.. code-block:: twig

   {# In a list view row #}
   {% include '@MauticCore/Components/category.html.twig' with {
       category: item.category
   } only %}

To show the Category in a detail view, set ``type`` to ``inline``.

.. code-block:: twig

   {# In a detail view header #}
   {% include '@MauticCore/Components/category.html.twig' with {
       type: 'inline',
       category: item.category
   } only %}

Without ``only``, Twig also passes every variable of the including template to the Component. A parent variable named ``type`` or ``category`` then overrides the value the Component would otherwise use. With ``only``, the Component receives just the variables you pass.

Template options
================

.. list-table::
    :header-rows: 1
    :widths: 20 15 15 50

    * - Option
      - Type
      - Default
      - Description
    * - ``category``
      - Category entity or ``null``
      - None
      - The Category to show. The template reads its ``title`` and ``color``. When you leave it out or pass ``null``, the template treats the item as having no Category.
    * - ``type``
      - string
      - ``expanded``
      - How the template shows the Category. Use ``expanded`` for list views and ``inline`` for detail views.
