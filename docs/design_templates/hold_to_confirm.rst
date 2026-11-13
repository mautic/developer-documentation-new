Hold-to-confirm template
########################

The ``hold-to-confirm.html.twig`` template renders a button that runs its action only after the User presses and holds it. Use it for actions that are hard to undo, such as deleting or resetting data, so a stray click doesn't trigger them.

While the User holds the button, a progress ring fills around its icon. When the ring is full, the button shows a checkmark and its confirmed label, and then returns to its original state. Releasing the button, moving the pointer off it, or moving focus away before the ring fills cancels the action. Users can also hold the button with the Space or Enter key.

Including the template
**********************

Include ``@MauticCore/Components/hold-to-confirm.html.twig`` with the ``only`` keyword. This example renders the **Restart all dismissed tips** button and its hint in the User's **Account** settings.

.. code-block:: twig

   {% include '@MauticCore/Components/hold-to-confirm.html.twig' with {
       id: 'reset-dismissed-tips',
       label: 'mautic.user.config.title.experience_and_learning.reset_dismissed',
       confirmedLabel: 'mautic.user.config.title.experience_and_learning.tips_restarted',
       variant: 'danger',
       size: 'sm',
       icon: 'ri-refresh-line',
   } only %}
   <div class="form-text">{{ 'mautic.core.hold_to_confirm.hint'|trans }}</div>

Add a visible hint below the button so Users know to press and hold it, because the template doesn't render one. The example uses the ``mautic.core.hold_to_confirm.hint`` translation key, which reads 'Press and hold to confirm.'

The template passes ``label`` and ``confirmedLabel`` through Twig's ``trans`` filter, so you can pass translation keys or plain strings. It builds the button's ``aria-label`` from the label and the hold duration, for example 'Restart all dismissed tips. Press and hold for 1.2 seconds to confirm', and announces the confirmed label to screen readers.

Running the action
******************

The button has no click handler. When the User completes the hold, the Component dispatches a bubbling ``mautic:hold-to-confirm:confirm`` event on its wrapper element, which has the ``data-component="hold-to-confirm"`` attribute. The ``id`` option sets the ``id`` of the ``<button>`` inside that wrapper, so find the wrapper with ``closest()`` and listen for the event there.

.. code-block:: javascript

   Mautic.helloWorldOnLoad = function (container) {
       mQuery(container + ' #helloworld-reset').closest('[data-component="hold-to-confirm"]')
           .off('mautic:hold-to-confirm:confirm.helloWorld')
           .on('mautic:hold-to-confirm:confirm.helloWorld', function () {
               Mautic.helloWorldReset();
           });
   };

Mautic sets up every hold-to-confirm button when it loads, including buttons that AJAX content adds later. To change a button after it renders, get its controller with ``MauticUI.HoldToConfirmButton.get(wrapperElement)`` and call ``update()`` with the options to change, such as ``label``, ``disabled``, or ``duration``.

Template options
================

All options are optional.

.. list-table::
    :header-rows: 1
    :widths: 20 10 20 50

    * - Option
      - Type
      - Default
      - Description
    * - ``id``
      - string
      - None
      - The ``id`` attribute of the ``<button>``.
    * - ``label``
      - string
      - 'Hold to delete'
      - The button text, or a translation key.
    * - ``confirmedLabel``
      - string
      - 'Confirmed'
      - The text the button shows after the User completes the hold, or a translation key.
    * - ``variant``
      - string
      - ``danger``
      - Set to ``danger`` for a destructive action, which adds the ``btn-danger`` class, or ``neutral`` for any other action. The template also accepts ``destructive`` as another name for ``danger``, and uses ``danger`` for any other value.
    * - ``size``
      - string
      - ``md``
      - The button size, ``sm``, ``md``, or ``lg``. The template uses ``md`` for any other value.
    * - ``icon``
      - string
      - ``ri-delete-bin-line``
      - The CSS class of the Remix Icon inside the progress ring.
    * - ``duration``
      - integer
      - ``1200``
      - How long, in milliseconds, the User must hold the button.
    * - ``resetDelay``
      - integer
      - ``1500``
      - How long, in milliseconds, the button shows its confirmed state before it returns to its original state. Set to ``0`` to keep the confirmed state.
    * - ``className``
      - string
      - None
      - Extra CSS classes for the ``<button>``.
    * - ``disabled``
      - boolean
      - ``false``
      - Set to ``true`` to add the ``disabled`` attribute to the ``<button>``.
