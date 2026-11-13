Utilities
#########

Introduction
************

Mautic offers a set of CSS utility classes designed to facilitate efficient implementation of flexible layouts using CSS flex-box. These utilities provide a systematic approach to constructing responsive and dynamic new areas for its User interface, enabling you to rapidly prototype and build complex layouts while minimizing custom CSS.

The utility classes seek to encompass a great spectrum of flex-box properties, including:

- Display settings
- Flex direction
- Wrapping behavior
- Justification and alignment
- Spacing and gap management
- Item ordering

Key aspects
***********

1. **Abbreviated Nomenclature**: class names follow a logical, short and easy-to-remember convention.
2. **Most Common Uses Coverage**: utilities address the full range of flex-box properties and behaviors.
3. **Responsive Design**: includes variations for different view port sizes, enabling fine-grained control over layout across devices.
4. **Composability**: you can combine classes to create sophisticated layout patterns.
5. **Consistent Spacing**: standardized options for managing padding, margin and gap properties.

This documentation clearly explains each utility class, its function, and its app. It includes practical examples and best practices for combining utilities to achieve complex layout requirements.

The following sections detail the individual utility classes, their usage, and advanced implementation strategies. This resource helps front-end developers efficiently leverage flex-box in their projects.

Abbreviation keys
=================

- ``d``: display
- ``fd``: flex-direction
- ``fw``: flex-wrap
- ``jc``: justify-content
- ``ai``: align-items
- ``ac``: align-content
- ``as``: align-self
- ``fg``: flex-grow
- ``fs``: flex-shrink
- ``fb``: flex-basis
- ``fo``: order

Flex container properties
*************************

Display properties
==================

- ``.d-flex``: Sets an element to be a flex container by setting its display property to flex. It allows the direct children of the element to be laid out in a flex context.

Direction properties
====================

- ``.fd-row``: Sets the direction of the flex items in the container to a row. The items are laid out from left to right.
- ``.fd-row-reverse``: Sets the direction of the flex items in the container to a row, but in reverse. The items are laid out from right to left.
- ``.fd-column``: Sets the direction of the flex items in the container to a column. The items are laid out from top to bottom.
- ``.fd-column-reverse``: Sets the direction of the flex items in the container to a column, but in reverse. The items are laid out from bottom to top.

Wrap properties
===============

- ``.fw-wrap``: Allows the flex items to wrap onto multiple lines if there isn't enough room for them on one line.
- ``.fw-nowrap``: Prevents the flex items from wrapping onto multiple lines, even if there isn't enough room for them on one line.
- ``.fw-wrap-reverse``: Allows the flex items to wrap onto multiple lines if there isn't enough room for them on one line, but in reverse.

Justify properties
==================

- ``.jc-start``: Aligns the flex items along the start of the main axis. In a row direction, this is the left edge, and in a column direction, this is the top edge.
- ``.jc-end``: Aligns the flex items along the end of the main axis. In a row direction, this is the right edge, and in a column direction, this is the bottom edge.
- ``.jc-center``: Aligns the flex items along the center of the main axis.
- ``.jc-space-between``: Evenly distributes the flex items along the main axis, with the first item at the start and the last item at the end.
- ``.jc-space-around``: Evenly distributes the flex items along the main axis, with equal space around each item.
- ``.jc-space-evenly``: Evenly distributes the flex items along the main axis, with equal space between each item, including the first and last items.

Align properties
================

Align items
-----------

- ``.ai-start``: Aligns the flex items along the start of the cross axis. In a row direction, this is the top edge, and in a column direction, this is the left edge.
- ``.ai-end``: Aligns the flex items along the end of the cross axis. In a row direction, this is the bottom edge, and in a column direction, this is the right edge.
- ``.ai-center``: Aligns the flex items along the center of the cross axis.
- ``.ai-baseline``: Aligns the flex items along their baseline. The baseline is the line upon which the letters in a line of text would rest.
- ``.ai-stretch``: Stretches the flex items to fill the container along the cross axis.

Align content
-------------

- ``.ac-start``: Aligns the lines of flex items along the start of the cross axis when there is extra space in the cross axis.
- ``.ac-end``: Aligns the lines of flex items along the end of the cross axis when there is extra space in the cross axis.
- ``.ac-center``: Aligns the lines of flex items along the center of the cross axis when there is extra space in the cross axis.
- ``.ac-space-between``: Evenly distributes the lines of flex items along the cross axis, with the first line at the start and the last line at the end, when there is extra space in the cross axis.
- ``.ac-space-around``: Evenly distributes the lines of flex items along the cross axis, with equal space around each line, when there is extra space in the cross axis.
- ``.ac-stretch``: Stretches the lines of flex items to fill the container along the cross axis when there is extra space in the cross axis.

Align self
----------

- ``.as-start``: Aligns a single flex item along the start of the cross axis.
- ``.as-end``: Aligns a single flex item along the end of the cross axis.
- ``.as-center``: Aligns a single flex item along the center of the cross axis.
- ``.as-baseline``: Aligns a single flex item along the baseline.
- ``.as-stretch``: Stretches a single flex item to fill the container along the cross axis.

Flex item properties
=====================

Flex grow properties
--------------------

- ``.fg-1``: Sets the flex grow factor of a flex item to 1. This means the item will grow to fill any remaining space in the container.
- ``.fg-0``: Sets the flex grow factor of a flex item to 0. This means the item will not grow to fill any remaining space in the container.

Flex shrink properties
----------------------

- ``.fs-1``: Sets the flex shrink factor of a flex item to 1. This means the item can shrink if necessary to fit into the container.
- ``.fs-0``: Sets the flex shrink factor of a flex item to 0. This means the item cannot shrink to fit into the container.

Flex basis properties
---------------------

- ``.fb-auto``: Sets the flex basis of a flex item to auto. This means the browser will calculate the size of the item based on its content.
- ``.fb-0``: Sets the flex basis of a flex item to 0. This means the item will have a size of 0 before any growing or shrinking takes place.

Flex order properties
---------------------

- ``.fo-auto``: Sets the order of a flex item to auto. This means the item will be laid out in the order it appears in the source code.
- ``.fo-0``, ``.fo-1``, ``.fo-2``, ``.fo-3``, ``.fo-4``, ``.fo-5``: Sets the order of a flex item to the specified number. This means the item will be laid out in that order, regardless of where it appears in the source code.

Gap properties
--------------

* ``.gap-{size}``: Sets the gap between flex items. For example, ``.gap-12`` sets a 12px gap.
* ``.row-gap-{size}``: Sets the gap between rows of flex items.
* ``.column-gap-{size}``: Sets the gap between columns of flex items.

The ``{size}`` value is one of the sizes listed in :ref:`Size options <design/utilities:Size options>`, such as ``0``, ``5``, ``12``, or ``24``. The gap classes also support the ``10``, ``15``, and ``20`` sizes and the ``xs``, ``sm``, ``md``, and ``lg`` aliases, which existing custom templates may use.

Responsive variations
=====================

The utilities follow a mobile-first responsive design principle, becoming active at specific minimum screen sizes. You create these responsive variations by appending ``-sm``, ``-md``, or ``-lg`` to the end of the utility class name.

- Base utility no suffix: applies to all screen sizes
- ``-sm`` suffix: Applies from the small breakpoint and up
- ``-md`` suffix: Applies from the medium breakpoint and up
- ``-lg`` suffix: Applies from the large breakpoint and up

For example:

- ``.d-flex`` applies to all screen sizes
- ``.d-flex-sm`` applies from the small breakpoint and up
- ``.d-flex-md`` applies from the medium breakpoint and up
- ``.d-flex-lg`` applies from the large breakpoint and up

This approach allows for progressive enhancement of layouts as the view-port size increases, providing fine-grained control over the responsiveness of your design.


Responsive examples
===================

Here are some example scenarios that illustrate how to use these utilities in practice:

.. code-block:: html

    <div class="d-flex jc-space-between ai-center">
      <div>Left content</div>
      <div>Center content</div>
      <div>Right content</div>
    </div>

This example creates a flex container with items spread across the container and vertically centered.

.. code-block:: html

    <div class="d-flex fd-column ai-stretch gap-12">
      <div>Top item</div>
      <div>Middle item</div>
      <div>Bottom item</div>
    </div>

This example creates a vertical stack of items that stretch to fill the container's width, with a 12px gap between them.

Combining utilities
===================

Note that you can combine these utilities to create complex layouts. For example:

.. code-block:: html

    <div class="d-flex fd-row-md fd-column fw-wrap jc-center ai-center gap-16">
      <!-- Flex items here -->
    </div>

This combination creates a flex container that:

- Is a column on small screens and a row on medium screens and up
- Wraps items if they don't fit
- Centers items both horizontally and vertically
- Has a 16px gap between items

Padding and margin utilities
****************************

Mautic provides the Bootstrap 5 spacing utilities for padding and margin, alongside its own spacing classes. Both sets use one pixel scale, so the number in a class name is the size in pixels. For example, ``mt-16`` sets a 16px top margin.

Naming convention
=================

The Bootstrap 5 spacing classes use these prefixes:

* ``p-``, ``m-``: padding or margin on all sides
* ``pt-``, ``mt-``: padding or margin top
* ``pb-``, ``mb-``: padding or margin bottom
* ``ps-``, ``ms-``: padding or margin start - the left side in left-to-right layouts
* ``pe-``, ``me-``: padding or margin end - the right side in left-to-right layouts
* ``px-``, ``mx-``: padding or margin on the start and end
* ``py-``, ``my-``: padding or margin top and bottom

Mautic's own spacing classes add these prefixes:

* ``pa-``, ``ma-``: padding or margin on all sides
* ``pl-``, ``ml-``: padding or margin left
* ``pr-``, ``mr-``: padding or margin right

Mautic's core templates use ``ps-``, ``pe-``, ``ms-``, and ``me-`` for left and right spacing. Use them in your templates too, because they follow the text direction.

To set a margin to ``auto``, use ``ma-a``, ``mt-a``, ``mb-a``, ``ml-a``, ``mr-a``, or a Bootstrap ``-auto`` class such as ``ms-auto``.

Size options
============

All spacing classes support these sizes, in pixels:

.. vale off

``0``, ``1``, ``2``, ``3``, ``4``, ``5``, ``8``, ``12``, ``16``, ``24``, ``32``, ``40``, ``48``, ``64``, ``80``, ``96``, ``160``

.. vale on

For example, ``me-1`` sets a 1px end margin and ``pb-24`` sets a 24px bottom padding.

Mautic's own spacing classes also support the ``10``, ``15``, and ``20`` sizes, and these named aliases:

* ``xs``: 5px
* ``sm``: 10px
* ``md``: 15px
* ``lg``: 20px
* ``xl``: 32px

The aliases and the ``pl-``, ``pr-``, ``ml-``, and ``mr-`` classes remain available so that existing custom templates keep working. Mautic's core templates use the sizes ``5``, ``12``, ``16``, and ``24`` instead of ``xs``, ``sm``, ``md``, and ``lg``.

Padding and margin examples
===========================

.. code-block:: html

    <div class="p-5">Padding 5px on all sides</div>
    <div class="pt-12 pb-12">Padding 12px on top and bottom</div>
    <div class="ps-16 pe-16">Padding 16px on left and right</div>
    <div class="m-24">Margin 24px on all sides</div>
    <div class="mt-32 mb-32">Margin 32px on top and bottom</div>

Variable-based sizes
====================

In Mautic's own spacing classes, the sizes from ``8`` to ``160`` - except ``10``, ``15``, and ``20`` - use CSS variables for spacing, allowing for easy theming and consistent spacing across your app:

* ``var(--spacing-03)`` to ``var(--spacing-13)``

These correspond to specific pixel values - for example, ``var(--spacing-03)`` is 8px, ``var(--spacing-13)`` is 160px.

.. note::
   All padding and margin utilities use the ``!important`` declaration to ensure they take precedence over other styles. Use these utilities judiciously to maintain the integrity of your CSS architecture.
