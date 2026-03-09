Implementing flash messages
###########################

.. vale off

Flash messages are temporary notifications that appear at the top of the page to inform Users about the result of an action.

.. vale on

Backend implementation - PHP
****************************

#. Add translation strings to ``{bundle}/Translations/en_US/flashes.ini``.
#. Use the following code in your controllers:

   .. code-block:: php

      // Success message
      $this->addFlashMessage('mautic.core.notice.created', [
          '%name%' => $entity->getName()
      ]);

      // Error message
      $this->addFlashMessage('mautic.core.error.generic', [], 'error');

The ``addFlashMessage()`` method accepts three parameters:

* **Translation key**: the unique string identifier from your ``.ini`` file. For example, ``mautic.core.notice.created``.
* **Parameters**: an array of values that replace placeholders - such as ``%name%`` - within the translation string.
* **Message type**: the type of message to display. The default is ``notice``.

Frontend implementation - JavaScript
************************************

#. Add translation strings to ``{bundle}/Translations/en_US/flashes.ini``:

   .. code-block:: ini

      mautic.core.notice.my_success_message="Success message here!"
      mautic.core.error.my_error_message="Error message here!"

#. Create the flash message using one of these helper functions:

   * ``Mautic.addFlashMessage(message)``: creates a generic flash message.
   * ``Mautic.addInfoFlashMessage(message)``: creates an info or success flash message.
   * ``Mautic.addErrorFlashMessage(message)``: creates an error flash message.

#. Pass the result to ``Mautic.setFlashes()`` to display the message.

   .. code-block:: javascript

      // Display a success message
      var successMsg = Mautic.translate('mautic.core.notice.my_success_message');
      Mautic.setFlashes(Mautic.addInfoFlashMessage(successMsg));

      // Display an error message
      var errorMsg = Mautic.translate('mautic.core.error.my_error_message');
      Mautic.setFlashes(Mautic.addErrorFlashMessage(errorMsg));
