Depicting availability of interface elements
############################################

The state of interface elements is a crucial aspect of user interface design, providing visual feedback and preventing interaction when certain actions aren't allowed.

Working with tabs
*****************

Mautic uses the following CSS code to style tabs which aren't available for interaction:

.. code-block:: css

   .nav-tabs.nav-tabs-contained > li.disabled {
     cursor: not-allowed;
     color: var(--text-disabled);
   }

   .nav-tabs.nav-tabs-contained > li.disabled > a {
     background-color: var(--button-disabled);
     pointer-events: none;
   }

This CSS accomplishes the following:

* Sets the cursor to ``not-allowed`` for tabs which can't be interacted with, indicating that interaction is prohibited.
* Changes the text color to a predefined inactive state color.
* Modifies the background color of the tab to visually represent its inactive state.
* Prevent click events on the tab using ``pointer-events: none``.

To dynamically deactivate tabs, use JavaScript to add or remove the ``disabled`` class. Here's an example function:

.. code-block:: javascript

   Mautic.togglePermissionVisibility = function () {
       setTimeout(function () {
           if (mQuery('#role_isAdmin_0').prop('checked')) {
               mQuery('#permissions-tab').removeClass('disabled');
           } else {
               mQuery('#permissions-tab').addClass('disabled');
           }
       }, 10);
   };

This function:

* Checks the state of a checkbox - ``#role_isAdmin_0``.
* Adds or removes the ``disabled`` class from the permissions tab based on the checkbox state.

To implement inactive states for tabs:

#. Assign unique IDs to your tab elements.
#. Use JavaScript to toggle the ``disabled`` class on the appropriate ``<li>`` elements.

Tabs rendered with the tabs template
====================================

When you render tabs with the :doc:`/design_templates/tabs`, set a tab's ``disabled`` key to ``true`` to show it as unavailable. The template adds the ``disabled`` class to the tab's ``<li>`` and its ``<button>``, and the ``disabled`` attribute to the ``<button>``, so Users can't select the tab.

To deactivate one of these tabs with JavaScript, toggle the ``disabled`` class and the ``disabled`` property on its ``<button>``. Mautic styles the ``<button>`` rather than the ``<li>``.

.. code-block:: javascript

   const $tab = mQuery('[data-bs-target="#helloworld-history"]');
   $tab.toggleClass('disabled', !isAvailable).prop('disabled', !isAvailable);

.. note::
   Always use inactive states instead of hiding elements.