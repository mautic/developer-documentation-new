Disabling interface elements
=======================================

The state of interface elements is a crucial aspect of user interface design, providing visual feedback and preventing interaction when certain actions aren't allowed.

Disabling tabs
--------------

We use the following CSS code to style disabled tabs:

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

* Sets the cursor to ``not-allowed`` for disabled tabs, indicating that interaction is prohibited.
* Changes the text color to a predefined disabled state color.
* Modifies the background color of the tab to visually represent its disabled state.
* Prevent click events on the tab using ``pointer-events: none``.

To dynamically disable tabs, we use JavaScript to add or remove the ``disabled`` class. Here's an example function:

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

To implement disabled states for tabs:

1. Assign unique IDs to your tab elements.
2. Use JavaScript to toggle the ``disabled`` class on the appropriate ``<li>`` elements.

.. note::
   Always use disabled states instead of hiding elements.