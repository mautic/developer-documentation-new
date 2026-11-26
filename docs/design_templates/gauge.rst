Gauge template
##############

The ``gauge.html.twig`` template renders a gauge in Mautic's style. A gauge shows one value as a ring or a half ring that fills from ``0`` to ``100`` percent, with the value as text. Use it when your template shows a share, a score, or progress toward a total, so the value looks like the gauges in Mautic's own views. For example, the **Campaign share** tab of a Segment shows each Campaign's share of the Segment as a small ring.

The gauge comes in five sizes. It can show the value as a percentage or as an amount out of a total, such as '42/50'. When you don't pass a value yet, for example while an AJAX request is still loading it, the gauge shows an empty ring in a loading state. The template also adds ``role="meter"`` and the ARIA - Accessible Rich Internet Applications - attributes that screen readers need.

The ring fills with a short animation when the gauge appears and when its value changes. Browsers set to reduce motion show the filled ring without the animation.

Including the template
**********************

Include ``@MauticCore/Components/gauge.html.twig`` with the ``only`` keyword, and pass a ``label`` and a ``value``.

.. code-block:: twig

   {% include '@MauticCore/Components/gauge.html.twig' with {
       label: 'plugin.helloworld.open_rate'|trans,
       type: 'full',
       size: 'sm',
       value: 64.5
   } only %}

Without ``only``, Twig also passes every variable of the including template to the Component. The Component reads its options, such as ``value``, ``size``, and ``id``, from those variables, so a parent variable with the same name overrides the option's default. With ``only``, the Component receives just the variables you pass.

The template doesn't translate ``label``, so pass it through the ``trans`` filter yourself, as in the example.

To show an amount out of a total, pass ``total``. The ring fills to the share of ``value`` in ``total``, and the text shows both numbers, such as '42/50'. Screen readers announce '42 of 50'.

.. code-block:: twig

   {% include '@MauticCore/Components/gauge.html.twig' with {
       label: 'plugin.helloworld.contacts_synced'|trans,
       size: 'lg',
       value: 42,
       total: 50
   } only %}

Template options
================

You must set ``label``. All other options are optional.

.. list-table::
    :header-rows: 1
    :widths: 20 10 15 55

    * - Option
      - Type
      - Default
      - Description
    * - ``label``
      - string
      - None
      - What the gauge measures. Screen readers announce it, but it doesn't appear on screen. The template escapes the text but doesn't translate it.
    * - ``value``
      - number
      - None
      - A percentage from ``0`` to ``100``, or the amount out of ``total`` when you set ``total``. The template limits the filled part of the ring to the range from ``0`` to ``100`` percent and rounds it to one decimal place. When you don't set it, the gauge shows its loading state. A value of ``0`` shows an empty ring, not the loading state.
    * - ``total``
      - number
      - None
      - The amount that fills the ring. When it's greater than ``0``, the ring shows ``value`` as a share of ``total``, and the text shows ``value``, a slash, and ``total`` instead of a percentage. The template then ignores ``unit``.
    * - ``type``
      - string
      - ``semi``
      - The shape. ``full`` draws a ring and ``semi`` draws a half ring. The template uses ``semi`` for any other value.
    * - ``size``
      - string
      - ``md``
      - The width of the gauge. ``xs`` is 16 pixels wide, ``sm`` is 32 pixels, ``md`` is 64 pixels, ``lg`` is 96 pixels, and ``xl`` is 160 pixels. In the ``xs``, ``sm``, and ``md`` sizes, the value appears next to the gauge. In the ``lg`` and ``xl`` sizes, it appears inside the ring, or along the bottom of a half ring.
    * - ``color``
      - string
      - ``default``
      - The color of the filled part. ``default`` uses the Theme's active layer color and ``color`` uses its interactive color.
    * - ``status``
      - string
      - None
      - Set it to ``danger``, ``warning``, or ``success`` to fill the ring in the Theme's error, warning, or success color instead of the ``color`` option.
    * - ``unit``
      - string
      - ``%``
      - The unit shown after the value. Set it to an empty string to show the number alone.
    * - ``showValue``
      - boolean
      - ``true``
      - Set to ``false`` to show the gauge without its value text.
    * - ``delta``
      - number
      - None
      - A change in percent to show below the gauge, with an up arrow for ``0`` and higher or a down arrow for negative values. Positive values get a ``+`` sign.
    * - ``font``
      - string
      - None
      - Set to ``plex`` to show the value in the ``IBM Plex Sans`` font family.
    * - ``className``
      - string
      - None
      - Extra CSS classes for the wrapper ``<div>``.
    * - ``id``
      - string
      - ``gauge-`` followed by a random number
      - The ``id`` of the wrapper ``<div>``. Set it when your JavaScript or CSS needs to find the gauge.

Updating the gauge with JavaScript
**********************************

When your view loads the value after Mautic renders the view, for example through an AJAX request, render the gauge without ``value`` so it starts in the loading state. Then call ``Mautic.updateGauge()`` with the response. The gauge updates without a reload.

.. code-block:: javascript

   Mautic.updateGauge('#helloworld-open-rate', response.openRate);

The function takes these arguments:

* ``container`` - a selector or element for the gauge's wrapper, or for an element that contains it.
* ``value`` - a percentage from ``0`` to ``100``, or the amount out of ``total``.
* ``total`` - optional. The amount that fills the ring, as in the template's ``total`` option.

The function removes the loading state, fills the ring, updates the ARIA values, and replaces the value text. It keeps the gauge's ``unit``. It doesn't change the ``delta`` text.

The **Campaign share** tab of a Segment uses this template and function. It renders an ``xs`` ring for each Campaign, in the loading state until Mautic returns its share. When the tab opens, or when the Segment view loads with that tab already active, it requests the missing shares and fills each ring with ``Mautic.updateGauge()``.
