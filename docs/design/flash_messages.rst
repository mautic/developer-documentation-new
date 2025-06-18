Implementing flash messages
###########################

Flash messages are temporary notifications that appear at the top of the page to inform users about the result of an action.

Backend (PHP) implementation
****************************

**In controllers:**

.. code-block:: php

   // Success message
   $this->addFlashMessage('mautic.core.notice.created', [
       '%name%' => $entity->getName()
   ]);

   // Error message
   $this->addFlashMessage('mautic.core.error.generic', [], 'error');

The first parameter is the translation key, the second is an array of parameters for the translation, and the third is the message type (default is ``notice``).

Frontend (JavaScript) implementation
************************************

1. **Add translation strings**

Add your translation strings to ``{bundle}/Translations/en_US/messages.ini`` (or the relevant locale/domain):

.. code-block:: ini

   mautic.core.notice.my_success_message="Success message here!"
   mautic.core.error.my_error_message="Error message here!"

2. **Create and display translated flash messages**

Create the flash message using one of these helper functions:
- Mautic.addFlashMessage(message) - Generic flash message
- Mautic.addInfoFlashMessage(message) - Info/success flash message
- Mautic.addErrorFlashMessage(message) - Error flash message

Pass the result to Mautic.setFlashes() to display it.

.. code-block:: javascript

   var message = Mautic.translate('mautic.core.notice.my_success_message');
   var flashMessage = Mautic.addInfoFlashMessage(message);
   Mautic.setFlashes(flashMessage);

   var message = Mautic.translate('mautic.core.error.my_error_message');
   var flashMessage = Mautic.addErrorFlashMessage(message);
   Mautic.setFlashes(flashMessage);
