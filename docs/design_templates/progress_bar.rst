Progress bar template
#####################

The ``progress-bar.html.twig`` template renders a progress bar in Mautic's style. Use it when your template shows the progress of a long-running action, such as sending Emails or importing Contacts, so the progress looks and behaves like Mautic's own progress bars.

.. vale Google.Acronyms = NO

The progress bar has a label that names the action, a bar that fills as the action progresses, and optional helper text below the bar, such as '2000 of 5000'. It has active, finished, and error states. When you don't pass a value yet, for example while the first batch is still loading, it shows an indeterminate bar that slides instead of filling. The template also adds ``role="progressbar"`` and the ARIA - Accessible Rich Internet Applications - attributes that screen readers need.

.. vale Google.Acronyms = YES

Including the template
**********************

Include ``@MauticCore/Components/progress-bar.html.twig`` with the ``only`` keyword, and pass a ``label`` and the current progress.

.. code-block:: twig

   {% include '@MauticCore/Components/progress-bar.html.twig' with {
       label: 'plugin.helloworld.sync.progress',
       value: 40,
       max: 80,
       helperText: 'mautic.core.progress_bar.count'|trans({'%current%': 40, '%total%': 80}),
       id: 'helloworld-sync'
   } only %}

Without ``only``, Twig also passes every variable of the including template to the Component. The Component reads its options, such as ``status``, ``type``, and ``id``, from those variables, so a parent variable with the same name overrides the option's default. With ``only``, the Component receives just the variables you pass.

The template passes ``label`` and ``helperText`` through Twig's ``trans`` filter, so you can pass translation keys or plain strings. Mautic provides these translation keys for helper text:

.. vale off

* ``mautic.core.progress_bar.preparing`` - 'Preparing...'
* ``mautic.core.progress_bar.count`` - '%current% of %total%'
* ``mautic.core.progress_bar.done`` - 'Done'
* ``mautic.core.progress_bar.error`` - 'Error'

.. vale on

To show an action that's starting, leave out ``value`` and pass the preparing text. The bar stays indeterminate until a value arrives.

.. code-block:: twig

   {% include '@MauticCore/Components/progress-bar.html.twig' with {
       label: 'plugin.helloworld.sync.progress',
       max: 80,
       helperText: 'mautic.core.progress_bar.preparing',
       id: 'helloworld-sync'
   } only %}

To show a completed action, set ``status`` to ``finished``. The bar fills completely and shows a checkmark icon next to the label.

.. code-block:: twig

   {% include '@MauticCore/Components/progress-bar.html.twig' with {
       label: 'plugin.helloworld.sync.progress',
       status: 'finished',
       helperText: 'mautic.core.progress_bar.done'
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
      - The action in progress, for example sending Emails. The template escapes the text as HTML.
    * - ``value``
      - number
      - None
      - The current progress. The template limits it to the range from ``0`` to ``max``. When you don't set it, the bar is indeterminate. A value of ``0`` shows an empty bar, not an indeterminate one.
    * - ``max``
      - number
      - ``100``
      - The value that represents a complete action, such as the total number of Contacts to process. When it's ``0`` or less, the template uses ``100``.
    * - ``status``
      - string
      - ``active``
      - The state of the action. Set it to ``active``, ``finished``, or ``error``. ``finished`` fills the bar and shows a checkmark icon. ``error`` fills the bar in the error color and shows a warning icon. In both states, the template ignores ``value``.
    * - ``size``
      - string
      - ``big``
      - The bar's height. ``big`` is 8 pixels high and ``small`` is 4 pixels high.
    * - ``type``
      - string
      - ``default``
      - The layout. ``default`` places the label on its own line before the bar. ``inline`` places the label next to the bar, hides the helper text visually, and hides the bar when ``status`` is ``finished`` or ``error``. ``indented`` adds horizontal padding to the label and helper text.
    * - ``helperText``
      - string
      - Empty string, or ``mautic.core.progress_bar.error`` when ``status`` is ``error``
      - Text below the bar that describes the progress, such as '12 of 40'. The template links it to the bar through ``aria-describedby``. When you don't set it, an error bar shows 'Error' and any other bar renders no helper text, so ``Mautic.updateProgressBar()`` can't show a count.
    * - ``hideLabel``
      - boolean
      - ``false``
      - Set to ``true`` to hide the label visually. Screen readers still announce it.
    * - ``className``
      - string
      - None
      - Extra CSS classes for the wrapper ``<div>``, such as spacing classes.
    * - ``id``
      - string
      - ``progress-bar-`` followed by a random number
      - The base for the ``id`` attributes of the label and helper text, which get the ``-label`` and ``-helper`` suffixes. Set it when your JavaScript or CSS needs to find these elements.

Updating the progress with JavaScript
*************************************

When your view loads progress in batches, for example through AJAX requests, call ``Mautic.updateProgressBar()`` with each response. The bar updates without a reload. The template's ``id`` option doesn't set an ``id`` on the wrapper, so wrap the include in an element your JavaScript can select.

.. code-block:: twig

   <div id="helloworld-sync-progress">
       {% include '@MauticCore/Components/progress-bar.html.twig' with {
           label: 'plugin.helloworld.sync.progress',
           max: 80,
           helperText: 'mautic.core.progress_bar.preparing',
           id: 'helloworld-sync'
       } only %}
   </div>

.. code-block:: javascript

   Mautic.updateProgressBar('#helloworld-sync-progress', response.done, response.percent, response.total);

The function takes these arguments:

* ``container`` - a selector or element for the progress bar's wrapper, or for an element that contains it.
* ``value`` - the current progress.
* ``percent`` - the width of the bar, as a percentage from ``0`` to ``100``.
* ``max`` - the value that represents a complete action.

The function removes the indeterminate state, updates the bar's width and its ``aria-valuemin``, ``aria-valuemax``, and ``aria-valuenow`` attributes, and sets the helper text to the translated 'current of total' count. It doesn't change ``status``, so render the template again with ``status`` set to ``finished`` or ``error`` when the action ends.

Mautic's own Email send and Contact import views use this template and function.
