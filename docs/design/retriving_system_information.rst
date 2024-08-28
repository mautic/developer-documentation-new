Retrieving Mautic settings in Twig
=============================================

Mautic allows you to access configuration settings directly in Twig templates using the ``configGetParameter`` function. This feature is particularly useful for creating display conditions or showing existing data in your templates.

Basic usage
-----------

To retrieve a setting, use the ``configGetParameter`` function with the parameter name as its argument:

.. code-block:: twig

   {{ configGetParameter('parameter_name') }}

Display conditions
------------------

You can use ``configGetParameter`` in conditional statements to control the display of content based on configuration settings:

.. code-block:: twig

   {% if configGetParameter('ip_lookup_auth') %}
       <!-- Content to display if ip_lookup_auth is enabled or has a filled value -->
   {% endif %}

Displaying configuration values
-------------------------------

To directly display a configuration value in your template, use the following syntax:

.. code-block:: twig

   {{ configGetParameter('parameter_name') }}

For example, to display the API OAuth2 access token lifetime:

.. code-block:: twig

   API OAuth2 Access Token Lifetime: {{ configGetParameter('api_oauth2_access_token_lifetime') }}

Finding available parameters
----------------------------

All available configuration parameters can be found in the ``/config/local.php`` file once you save the global configuration form for the first time. This file contains the complete list of settings that can be accessed using ``configGetParameter``.

Identifying parameter names
---------------------------

To find the correct parameter name for a specific setting:

1. Inspect the HTML of the setting field in the Mautic interface.
2. Look for the ``name`` attribute of the input field.
3. The parameter name will be the last part of the ``name`` attribute value.

For example, if you see:

.. code-block:: html

   <input name="config[apiconfig][api_oauth2_access_token_lifetime]" ...>

The corresponding parameter name would be ``api_oauth2_access_token_lifetime``.

Additional information
----------------------

- Be cautious when displaying sensitive configuration data in templates.
- Avoid excessive use of ``configGetParameter`` in loops or frequently rendered templates to prevent performance issues.
- Always consider providing default values when using configuration parameters to handle cases where the setting might not be defined.

Using the ``configGetParameter`` function in Twig, you can create new interactive experiences in Mautic.