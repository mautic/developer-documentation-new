Response hooks
==========================================================

.. js:method:: onResponse()

    Called prior to processing the Form submission's response, which handles actions like downloading a file, displaying a success message, and/or redirecting to another URL.

    :param object response: The response object may have the following defined:

        * ``response.download`` URL of a file to download
        * ``response.redirect`` URL to redirect to.
        * ``response.validationErrors`` Array of fields with validation errors.
        * ``response.errorMessage`` String with an error message.
        * ``response.success`` TRUE if the Form was submitted successfully.
        * ``response.successMessage`` String with a success message.

    :returns: bool|NULL|void Return TRUE to skip the default behavior for handling the response.

.. code-block:: javascript

    MauticFormCallback['formname'] = {
        onResponse: function (response) {
            // do something custom
        },
    };

.. js:method:: onResponseStart()

    Called prior to the default processing of the response.

    :param object response: The response object may have the following defined:

        * ``response.download`` URL of a file to download
        * ``response.redirect`` URL to redirect to.
        * ``response.validationErrors`` Array of fields with validation errors.
        * ``response.errorMessage`` String with an error message.
        * ``response.success`` TRUE if the Form was submitted successfully.
        * ``response.successMessage`` String with a success message.

    :returns: void

.. code-block:: javascript

    MauticFormCallback['formname'] = {
        onResponseStart: function (response) {
            // do something custom
        },
    };

.. Note:: This isn't called if an onResponse hook returns TRUE.

.. js:method:: onResponseEnd()

    Called after to the default processing of the response.

    :param object response: The response object may have the following defined:

        * ``response.download`` URL of a file to download
        * ``response.redirect`` URL to redirect to.
        * ``response.validationErrors`` Array of fields with validation errors.
        * ``response.errorMessage`` String with an error message.
        * ``response.success`` TRUE if the Form was submitted successfully.
        * ``response.successMessage`` String with a success message.

    :returns: void

.. code-block:: javascript

    MauticFormCallback['formname'] = {
        onResponseEnd: function (response) {
            // do something custom
        },
    };

.. Note:: This isn't called if an onResponse hook returns TRUE or if the page redirects.