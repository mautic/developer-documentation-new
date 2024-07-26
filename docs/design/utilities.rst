Utilities
===============================

Introduction
------------

Mautic offers a set of CSS utility classes designed to facilitate efficient implementation of flexible layouts using CSS flexbox. These utilities provide a systematic approach to constructing responsive and dynamic new areas for its user interface, enabling you to rapidly prototype and build complex layouts while minimizing custom CSS.

The utility classes seek to encompass a great spectrum of glexbox properties, including:

- Display settings
- Flex direction
- Wrapping behavior
- Justification and alignment
- Spacing and gap management
- Item ordering

Key Aspects
^^^^^^^^^^^^

1. **Abbreviated Nomenclature**: Class names follow a logical, short and easy-to-remember convention.
2. **Most Common Uses Coverage**: Utilities address the full range of Flexbox properties and behaviors.
3. **Responsive Design**: Includes variations for different viewport sizes, enabling fine-grained control over layout across devices.
4. **Composability**: Classes can be combined to create sophisticated layout patterns.
5. **Consistent Spacing**: Standardized options for managing padding, margin and gap properties.

This documentation is structured to provide a clear understanding of each utility class, its function, and its application. It includes practical examples and best practices for combining utilities to achieve complex layout requirements.

The following sections detail the individual utility classes, their usage, and advanced implementation strategies. This resource is intended for front-end developers seeking to leverage Flexbox efficiently in their projects.


Abbreviation keys
----------------

.. vale off

- **d**: display
- **fd**: flex-direction
- **fw**: flex-wrap
- **jc**: justify-content
- **ai**: align-items
- **ac**: align-content
- **as**: align-self
- **fg**: flex-grow
- **fs**: flex-shrink
- **fb**: flex-basis
- **fo**: order

.. vale on

Flex container properties
-------------------------

.. vale off

- ``.d-flex``: Sets an element to be a flex container by setting its display property to flex. It allows the direct children of the element to be laid out in a flex context.
- ``.fd-row``: Sets the direction of the flex items in the container to a row. The items are laid out from left to right.
- ``.fd-row-reverse``: Sets the direction of the flex items in the container to a row, but in reverse. The items are laid out from right to left.
- ``.fd-column``: Sets the direction of the flex items in the container to a column. The items are laid out from top to bottom.
- ``.fd-column-reverse``: Sets the direction of the flex items in the container to a column, but in reverse. The items are laid out from bottom to top.
- ``.fw-wrap``: Allows the flex items to wrap onto multiple lines if there isn't enough room for them on one line.
- ``.fw-nowrap``: Prevents the flex items from wrapping onto multiple lines, even if there isn't enough room for them on one line.
- ``.fw-wrap-reverse``: Allows the flex items to wrap onto multiple lines if there isn't enough room for them on one line, but in reverse.
- ``.jc-start``: Aligns the flex items along the start of the main axis. In a row direction, this is the left edge, and in a column direction, this is the top edge.
- ``.jc-end``: Aligns the flex items along the end of the main axis. In a row direction, this is the right edge, and in a column direction, this is the bottom edge.
- ``.jc-center``: Aligns the flex items along the center of the main axis.
- ``.jc-space-between``: Evenly distributes the flex items along the main axis, with the first item at the start and the last item at the end.
- ``.jc-space-around``: Evenly distributes the flex items along the main axis, with equal space around each item.
- ``.jc-space-evenly``: Evenly distributes the flex items along the main axis, with equal space between each item, including the first and last items.
- ``.ai-start``: Aligns the flex items along the start of the cross axis. In a row direction, this is the top edge, and in a column direction, this is the left edge.
- ``.ai-end``: Aligns the flex items along the end of the cross axis. In a row direction, this is the bottom edge, and in a column direction, this is the right edge.
- ``.ai-center``: Aligns the flex items along the center of the cross axis.
- ``.ai-baseline``: Aligns the flex items along their baseline. The baseline is the line upon which the letters in a line of text would rest.
- ``.ai-stretch``: Stretches the flex items to fill the container along the cross axis.
- ``.ac-start``: Aligns the lines of flex items along the start of the cross axis when there is extra space in the cross axis.
- ``.ac-end``: Aligns the lines of flex items along the end of the cross axis when there is extra space in the cross axis.
- ``.ac-center``: Aligns the lines of flex items along the center of the cross axis when there is extra space in the cross axis.
- ``.ac-space-between``: Evenly distributes the lines of flex items along the cross axis, with the first line at the start and the last line at the end, when there is extra space in the cross axis.
- ``.ac-space-around``: Evenly distributes the lines of flex items along the cross axis, with equal space around each line, when there is extra space in the cross axis.
- ``.ac-stretch``: Stretches the lines of flex items to fill the container along the cross axis when there is extra space in the cross axis.
- ``.as-start``: Aligns a single flex item along the start of the cross axis.
- ``.as-end``: Aligns a single flex item along the end of the cross axis.
- ``.as-center``: Aligns a single flex item along the center of the cross axis.
- ``.as-baseline``: Aligns a single flex item along the baseline.
- ``.as-stretch``: Stretches a single flex item to fill the container along the cross axis.
- ``.fg-1``: Sets the flex grow factor of a flex item to 1. This means the item will grow to fill any remaining space in the container.
- ``.fg-0``: Sets the flex grow factor of a flex item to 0. This means the item will not grow to fill any remaining space in the container.
- ``.fs-1``: Sets the flex shrink factor of a flex item to 1. This means the item can shrink if necessary to fit into the container.
- ``.fs-0``: Sets the flex shrink factor of a flex item to 0. This means the item cannot shrink to fit into the container.
- ``.fb-auto``: Sets the flex basis of a flex item to auto. This means the browser will calculate the size of the item based on its content.
- ``.fb-0``: Sets the flex basis of a flex item to 0. This means the item will have a size of 0 before any growing or shrinking takes place.
- ``.fo-auto``: Sets the order of a flex item to auto. This means the item will be laid out in the order it appears in the source code.
- ``.fo-0``, ``.fo-1``, ``.fo-2``, ``.fo-3``, ``.fo-4``, ``.fo-5``: Sets the order of a flex item to the specified number. This means the item will be laid out in that order, regardless of where it appears in the source code.
- ``.gap-20``, ``.gap-lg``: Sets the gap between flex items to 20px.
- ``.gap-15``, ``.gap-md``: Sets the gap between flex items to 15px.
- ``.gap-10``, ``.gap-sm``: Sets the gap between flex items to 10px.
- ``.gap-5``, ``.gap-xs``: Sets the gap between flex items to 5px.
- ``.gap-4``: Sets the gap between flex items to 4px.
- ``.gap-3``: Sets the gap between flex items to 3px.
- ``.gap-2``: Sets the gap between flex items to 2px.
- ``.gap-1``: Sets the gap between flex items to 1px.
- ``.gap-0``: Sets the gap between flex items to 0px.

.. vale on

Responsive Variations
---------------------

The utilities follow a mobile-first responsive design principle. Each responsive variation is associated with a minimum screen size at which it becomes active. These variations are created by appending ``-sm``, ``-md``, or ``-lg`` to the end of the utility class name.

- Base utility (no suffix): Applies to all screen sizes
- ``-sm`` suffix: Applies from the small breakpoint and up
- ``-md`` suffix: Applies from the medium breakpoint and up
- ``-lg`` suffix: Applies from the large breakpoint and up

For example:

- ``.d-flex`` applies to all screen sizes
- ``.d-flex-sm`` applies from the small breakpoint and up
- ``.d-flex-md`` applies from the medium breakpoint and up
- ``.d-flex-lg`` applies from the large breakpoint and up

This approach allows for progressive enhancement of layouts as the viewport size increases, providing fine-grained control over the responsiveness of your design.


Usage Examples
--------------

To illustrate how these utilities can be used in practice, let's add some example scenarios:

.. code-block:: html

    <div class="d-flex jc-space-between ai-center">
      <div>Left content</div>
      <div>Center content</div>
      <div>Right content</div>
    </div>

This example creates a flex container with items spread across the container and vertically centered.

.. code-block:: html

    <div class="d-flex fd-column ai-stretch gap-10">
      <div>Top item</div>
      <div>Middle item</div>
      <div>Bottom item</div>
    </div>

This example creates a vertical stack of items that stretch to fill the container's width, with a 10px gap between them.

Combining Utilities
-------------------

It's worth noting that these utilities can be combined to create complex layouts. For example:

.. code-block:: html

    <div class="d-flex fd-row-md fd-column fw-wrap jc-center ai-center gap-15">
      <!-- Flex items here -->
    </div>

This combination creates a flex container that:

- Is a column on small screens and a row on medium screens and up
- Wraps items if they don't fit
- Centers items both horizontally and vertically
- Has a 15px gap between items

Padding and Margin Utilities
============================

The CSS utility classes for padding and margin provide a comprehensive set of options for controlling spacing within your layouts. These utilities follow a consistent naming convention and offer a range of predefined sizes, including pixel values and variable-based spacing.

Naming Convention
-----------------

The utility classes use the following prefixes:

- ``pa-``: Padding all sides
- ``pt-``: Padding top
- ``pr-``: Padding right
- ``pb-``: Padding bottom
- ``pl-``: Padding left
- ``ma-``: Margin all sides
- ``mt-``: Margin top
- ``mr-``: Margin right
- ``mb-``: Margin bottom
- ``ml-``: Margin left

Size Options
------------

The utilities offer the following size options:

1. Pixel-based sizes: 0, 1, 2, 3, 4, 5, 10, 15, 20 pixels
2. Variable-based sizes: 8, 12, 16, 24, 32, 40, 48, 64, 80, 96, 160 pixels (using CSS variables)
3. Named sizes: xs (5px), sm (10px), md (15px), lg (20px), xl (32px)

Usage Examples
--------------

.. code-block:: html

    <div class="pa-5">Padding 5px on all sides</div>
    <div class="pt-10 pb-10">Padding 10px on top and bottom</div>
    <div class="pl-md pr-md">Padding 15px on left and right</div>
    <div class="ma-lg">Margin 20px on all sides</div>
    <div class="mt-32 mb-32">Margin 32px on top and bottom</div>

Variable-based Sizes
--------------------

Some utilities use CSS variables for spacing, allowing for easy theming and consistent spacing across your application:

- ``var(--spacing-03)`` to ``var(--spacing-13)``

These correspond to specific pixel values (e.g., ``var(--spacing-03)`` is 8px, ``var(--spacing-13)`` is 160px).

.. note::
   All padding and margin utilities use the ``!important`` declaration to ensure they take precedence over other styles. Use these utilities judiciously to maintain the integrity of your CSS architecture.
