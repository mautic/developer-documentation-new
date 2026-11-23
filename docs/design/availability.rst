Depicting availability of interface elements
############################################

The state of interface elements is a crucial aspect of user interface design, providing visual feedback and preventing interaction when certain actions aren't allowed.

Working with tabs
*****************

To show that a tab isn't available for interaction, add the ``disabled`` class to its ``<li>`` element. To deactivate tabs dynamically, use JavaScript to add or remove the ``disabled`` class:

#. Assign unique IDs to your tab elements.
#. Use JavaScript to toggle the ``disabled`` class on the appropriate ``<li>`` elements.

.. note::

   Always use inactive states instead of hiding elements.
