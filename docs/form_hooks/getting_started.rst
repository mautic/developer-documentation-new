Getting started with Form hooks
###############################

You can use Mautic's support for Form hooks to enhance or customize the Form experience when embedded into your third party websites.

.. Note:: Form hooks are only supported when embedding Forms into your website manually or through the automatic methods. They don't work with iFrames.

The first step is to embed the following JavaScript code once into the head of your website. The ``MauticFormCallback`` object contains the hooks for the named forms.

.. code-block:: javascript

    if (typeof MauticFormCallback == 'undefined') {
        var MauticFormCallback = {};
    }

You can define hooks for multiple Forms using the API name of the Form as follows:

.. code-block:: javascript

    MauticFormCallback['formname1'] = {
        // define hooks here
    };

    MauticFormCallback['formname2'] = {
        // define hooks here
    };

.. Note:: Define the Form hooks somewhere in the DOM before the code that loads the Form.

You'll need to view the HTML of the Form to find its API name. The easiest way to do this is to browse to the Form details in Mautic then click the 'Self-hosted' button. Look for the following in the second box:

.. code-block:: html

    <form autocomplete="false" role="form" method="post" action="https://example.com?formId=1" id="mauticform_thisismytestform" data-mautic-form="thisismytestform" enctype="multipart/form-data">

The API name is the value for the ``data-mautic-form`` attribute which in this case is ``thisismytestform``.

You'll define the Form's hooks as JavaScript methods in the correlated ``MauticFormCallback`` index. For example, to add custom validation, you would script something like the following:

.. code-block:: javascript

    MauticFormCallback['formname1'] = {
        // other hooks

        onValidate: function () {
            var email = document.getElementById('mauticform_input_formname1_email').value;
            if (email.includes('@gmail.com')) {
                alert('Please use a work email address.');

                // return FALSE to stop the Form submission
                return FALSE;
            }

            // return NULL|void to continue with default validation or return TRUE to skip it
        },

        // more hooks
    };
