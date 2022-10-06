General hooks
#############

.. js:method:: onSubmitButtonEnable()

    Called prior to default enabling of the submit button.

    :returns: bool|null Return TRUE to skip the default behavior that re-enables the submit button.

.. code-block:: javascript

    MauticFormCallback['formname'] = {
        onSubmitButtonEnable: function () {
             // do some custom stuff
        },
    };

.. js:method:: onSubmitButtonDisable()

    Called prior to default disabling of the submit button after the Form has been submitted.

    :returns: bool|null Return TRUE to skip the default behavior that disables the submit button.

.. code-block:: javascript

    MauticFormCallback['formname'] = {
        onSubmitButtonDisable: function () {
             // do some custom stuff
        },
    };

.. js:method:: onShowNextPage()

    Called prior to displaying the next page in the Form which is useful to adjust the DOM prior to making the page visible.

    :param number pageNumber: The page number to display.
    :returns: void

.. code-block:: javascript

    MauticFormCallback['formname'] = {
        onShowNextPage: function (pageNumber) {
             // do some custom stuff
        },
    };

.. js:method:: onShowPreviousPage()

    Called prior to displaying the previous page in the Form which is useful to adjust the DOM prior to making the page visible.

    :param number pageNumber: The page number to display.
    :returns: void

.. code-block:: javascript

    MauticFormCallback['formname'] = {
        onShowPreviousPage: function (pageNumber) {
             // do some custom stuff
        },
    };

.. js:method:: onMessageSet()

    Called prior to injecting text into the corresponding elements to the message type which happens before Form validation to clear  existing text from previous submissions and after the Form is validated with either the validation error or success message.

    :param object messageObject:
        * ``messageObject.message`` The text to inject.
        * ``messageObject.type``    This will either be ``error`` or ``message``.

    :returns: bool|NULL|void Return TRUE to prevent the default behavior to inject the message into the corresponding element (for example if the hook injected the message elsewhere). Return NULL|void to continue with the default behavior.

.. code-block:: javascript

    MauticFormCallback['replaceWithFormName'] = {
        onMessageSet: function (messageObject) {
            if ('error' == messageObject.type) {
                // do something custom
            }
        },
    };