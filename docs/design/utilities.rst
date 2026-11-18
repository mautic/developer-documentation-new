Utilities
#########

Introduction
************

Mautic's User interface uses the utility classes from `Bootstrap 5.3 <https://getbootstrap.com/docs/5.3/utilities/api/>`_ for layout, spacing, borders, and alignment. Use these classes in your Plugin templates and Themes to build layouts that match the rest of Mautic without writing custom CSS.

For the full list of classes and how they work, see the Bootstrap documentation for each utility, such as `Flex <https://getbootstrap.com/docs/5.3/utilities/flex/>`_, `Spacing <https://getbootstrap.com/docs/5.3/utilities/spacing/>`_, and `Borders <https://getbootstrap.com/docs/5.3/utilities/borders/>`_. Mautic customizes them in two ways:

* Mautic replaces Bootstrap's default spacing scale with a pixel-based scale.
* Mautic adds a few utility classes that Bootstrap doesn't include.

Spacing scale
*************

The margin, padding, and gap utilities, such as ``.mt-16``, ``.px-8``, and ``.gap-12``, use a pixel-based scale. The number in the class name is the size in pixels.

.. vale off

The scale has the sizes 0, 1, 2, 3, 4, 5, 8, 12, 16, 24, 32, 40, 48, 64, 80, 96, and 160.

.. vale on

Negative margins are available for the same sizes, for example ``.mt-n16``. Grid gutter classes such as ``.g-3`` keep Bootstrap's default scale.

.. code-block:: html

    <div class="p-5">Padding 5px on all sides</div>
    <div class="py-12">Padding 12px on top and bottom</div>
    <div class="ps-16 pe-16">Padding 16px on the start and end sides</div>
    <div class="m-24">Margin 24px on all sides</div>
    <div class="mt-32 mb-32">Margin 32px on top and bottom</div>
    <div class="ms-auto">Pushed to the end of a flex container</div>

Mautic utility classes
**********************

Mautic adds these classes to the Bootstrap utilities:

* ``.w-44``: sets the width to 44px.
* ``.h-32``, ``.h-48``, ``.h-384``: set the height to 32px, 48px, or 384px.
* ``.min-h-256``: sets the minimum height to 256px.
* ``.fb-0``: sets the flex basis to 0, so flex items share the space by their grow factor alone.
* ``.as-1-1``, ``.as-2-1``, ``.as-4-3``, ``.as-16-9``: set the aspect ratio to 1:1, 2:1, 4:3, or 16:9.
* ``.shd-sm``: adds a small box shadow.
* ``.ma-neg-local``, ``.mi-neg-local``: set a negative margin on all sides, or on the inline sides, equal to the local layout density inline padding.

These classes don't have responsive variants.

Layout examples
***************

Bootstrap utilities follow a mobile-first approach. A class without a breakpoint applies to all screen sizes. A class with a breakpoint infix, such as ``.flex-md-row``, applies from that breakpoint and up. For the breakpoints, see `Breakpoints <https://getbootstrap.com/docs/5.3/layout/breakpoints/>`_ in the Bootstrap documentation.

.. code-block:: html

    <div class="d-flex justify-content-between align-items-center">
      <div>Left content</div>
      <div>Center content</div>
      <div>Right content</div>
    </div>

This example creates a flex container with items spread across the container and vertically centered.

.. code-block:: html

    <div class="d-flex flex-column align-items-stretch gap-12">
      <div>Top item</div>
      <div>Middle item</div>
      <div>Bottom item</div>
    </div>

This example creates a vertical stack of items that stretch to fill the container's width, with a 12px gap between them.

.. code-block:: html

    <div class="d-flex flex-column flex-md-row flex-wrap justify-content-center align-items-center gap-16">
      <!-- Flex items here -->
    </div>

This combination creates a flex container that:

* Is a column on small screens and a row on medium screens and up
* Wraps items if they don't fit
* Centers items both horizontally and vertically
* Has a 16px gap between items

.. note::

   Bootstrap utility classes use the ``!important`` declaration, so they take precedence over other styles on the same element.
