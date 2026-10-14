Validation hooks
################

.. js:method:: onValidate()

    Mautic calls this hook before the default Form validation. Use it to run custom code before the Form submits, or to replace the default validation with your own.

    :returns: ``bool|null`` Return ``true`` to skip the default validation and submit the Form. Return ``false`` to skip the default validation and prevent the Form submission. Return ``null`` to continue with the default validation. If the hook returns nothing, Mautic skips the default validation and doesn't submit the Form.

.. code-block:: javascript

    MauticFormCallback['formname'] = {
        onValidate: function () {
            var email = document.getElementById('mauticform_input_formname1_email').value;
            if (email.includes('@gmail.com')) {
                alert('Please use a work email address.');

                // return false to stop the Form submission
                return false;
            }

            // return null to continue with the default validation, or return true to skip it
            return null;
        },
    };

.. js:method:: onValidateStart()

    Mautic calls this hook at the beginning of the default Form validation.

    :returns: void

.. code-block:: javascript

    MauticFormCallback['formname'] = {
        onValidateStart: function () {
            // do some custom stuff
        },
    };

.. note::

   Mautic doesn't call this hook if an :js:meth:`onValidate` hook returns a value other than ``null``.

.. js:method:: onValidateField(fieldValidationObject)

    Mautic calls this hook for each Form Field during the default Form validation, before it validates that field.

    :param object fieldValidationObject:
        * ``fieldValidationObject.fieldKey`` The field's API name.
        * ``fieldValidationObject.field`` Object describing the field, with ``type``, ``name``, and ``multiple`` keys.

    :returns: ``bool|null`` Return ``true`` or ``false`` to skip the default validation for this field and use the returned value as its validation result. Return ``null`` to continue with the default validation for this field. If the hook returns nothing, Mautic skips the default validation for this field and treats the field as invalid.

.. code-block:: javascript

    MauticFormCallback['formname'] = {
        onValidateField: function (fieldValidationObject) {
            if ('email' == fieldValidationObject.fieldKey) {
                // do some custom validation and return true or false
            }

            // return null to run the default validation for other fields
            return null;
        },
    };

.. note::

   When a Contact submits the Form, Mautic doesn't call this hook if an :js:meth:`onValidate` hook returns a value other than ``null``.


.. js:method:: onValidateEnd()

    Mautic calls this hook after the default validation or the :js:meth:`onValidate` hook validates the Form, and before the Form submits.

    :param bool isFormValid: ``true`` if the Form passed validation, or ``false`` if it didn't.
    :returns: ``bool|null|void`` Return ``false`` to prevent the Form submission.

.. code-block:: javascript

    MauticFormCallback['formname'] = {
        onValidateEnd: function (isFormValid) {
            // do some custom stuff
        },
    };

.. js:method:: onErrorMark()

    Mautic calls this hook before it updates a field's element with a validation error.

    :param object fieldValidationObject:
        * ``fieldValidationObject.containerId`` The ID of the field's container element.
        * ``fieldValidationObject.valid`` ``true`` or ``false``.
        * ``fieldValidationObject.validationMessage`` The error message.

    :returns: ``bool|null|void`` Return ``true`` to skip the default behavior of appending the validation message to the field container's element with the ``.mauticform-errormsg`` class.

.. code-block:: javascript

    var fieldValidationObject = {
        containerId: 'mauticform_formname_email',
        valid: false,
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

    Mautic calls this hook before it clears a field's validation error.

    :param string fieldContainerId: The ID of the field's container element.

    :returns: ``bool|null|void`` Return ``true`` to skip the default behavior of clearing the validation message from the field container's element with the ``.mauticform-errormsg`` class.

.. code-block:: javascript

    MauticFormCallback['formname'] = {
        onErrorClear: function (fieldContainerId) {
            if ('mauticform_formname_email' == fieldContainerId) {
                 // do something custom
            }
        },
    };
