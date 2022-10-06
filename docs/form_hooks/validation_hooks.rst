Validation hooks
################

.. js:method:: onValidate()

    Called prior to default Form validation. This is useful if you want to execute custom code prior to the Form being submitted, or if you want to do your own validation.

    :returns: bool|NULL|void Return TRUE to skip the default validation and continue with submitting the Form. Return FALSE to skip the default validation and prevent the Form submission. Return NULL to still proceed with default validation.

.. code-block:: javascript

    MauticFormCallback['formname'] = {
        onValidate: function () {
            var email = document.getElementById('mauticform_input_formname1_email').value;
            if (email.includes('@gmail.com')) {
                alert('Please use a work email address.');

                // return FALSE to stop the form submission
                return FALSE;
            }

            // return NULL|void to continue with default validation or return TRUE to skip it
        },
    };

.. js:method:: onValidateStart()

    Called at the beginning of the default Form validation.

    :returns: void

.. code-block:: javascript

    MauticFormCallback['formname'] = {
        onValidateStart: function () {
            // do some custom stuff
        },
    };

.. Note:: This isn't called if an onValidate hook returns TRUE.


.. js:method:: onValidateEnd()

    Called after the Form has been validated by either the default validation or the onValidate hook.

    :param bool isFormValid: TRUE if the Form was successfully validated or FALSE if not.
    :returns: void

.. code-block:: javascript

    MauticFormCallback['formname'] = {
        onValidateEnd: function (isFormValid) {
            // do some custom stuff
        },
    };

.. js:method:: onErrorMark()

    Called before updating a field's element with a validation error.

    :param object fieldValidationObject:
        * ``fieldValidationObject.containerId`` The ID of the field's container element.
        * ``fieldValidationObject.valid`` TRUE|FALSE
        * ``fieldValidationObject.validationMessage`` The error message.

    :returns: bool|NULL|void Return TRUE to skip the default behavior of appending the validation message to the field container's element with the ``.mauticform-errormsg`` class.

.. code-block:: javascript

    var fieldValidationObject = {
        containerId: 'mauticform_formname_email',
        valid: FALSE,
        validationMessage: 'Email is required!'
    };

    MauticFormCallback['formname'] = {
        onErrorMark: function (fieldValidationObject) {
            if ('mauticform_formname_email' == fieldValidationObject.containerId && !fieldValidationObject.valid) {
                 // do something custom
            }
        },
    };

.. js:method:: onErrorClear()

    Called prior to clearing a field's validation error.

    :param string fieldContainerId: The ID of the field's container element.

    :returns: bool|NULL|void Return TRUE to skip the default behavior of clearing the validation message from the field container's element with the ``.mauticform-errormsg`` class.

.. code-block:: javascript

    MauticFormCallback['formname'] = {
        onErrorClear: function (fieldContainerId) {
            if ('mauticform_formname_email' == fieldContainerId) {
                 // do something custom
            }
        },
    };
