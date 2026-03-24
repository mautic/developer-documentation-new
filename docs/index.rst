Welcome to Mautic's developer documentation
###########################################

.. vale off

.. note::

   The content for this documentation requires a major update. The legacy documentation contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this documentation, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Welcome to the Mautic Developer Documentation. The documentation broadly covers building custom Plugins for Mautic which extends its features, building custom Themes, and how to integrate applications outside of Mautic using the REST API.

This documentation has multiple versions for different releases of Mautic starting from Mautic 4.x - the switcher is in the bottom left which allows you to change between versions.

.. vale off

Submitting code to Mautic
*************************

.. vale on

Development is open and available to any member of the Mautic community. All fixes and improvements happen through pull requests to the code on :xref:`Mautic's GitHub Repo`. This code is open source and publicly available.

Read all about contributing to Mautic as a Developer in the :xref:`Mautic Developer Contribution Guide`.

Read more about Mautic's :xref:`Mautic Code Governance` and the :xref:`Mautic Project Governance` model.

.. vale off

Your code must follow the :xref:`Symfony coding standards`. You can find details about where Mautic deviates from these standards documented in the :doc:`/plugins/mautic_vs_symfony` section.

.. vale on

Where to get help
*****************

The first place to ask for support is on the :xref:`Developer Forum` - this is where the Product Team monitors, and where most developers look out for posts they can assist with. There is also a Commercial forum if you have paid opportunities or are looking for work.

General development chatter also happens in ``#dev`` on :xref:`Mautic Slack`, and anything to do with contributing - including the weekly Open Source Friday contribution sprints - happen in ``#t-product``.

New major releases also have a dedicated space for discussion - for example ``#mautic-5`` and ``#mautic-6``.

Several areas on the Community Portal could be of interest, including :xref:`Community Portal Roadmap` and the :xref:`Community Portal Product Team`.

Supporting Mautic
*****************

There are several ways to support Mautic other than contributing with code.

1. Help with testing bugs and features using Gitpod in the browser - head to the :xref:`Mautic Tester Docs`
2. Help with improving the documentation on this site, and the :xref:`Mautic End User Docs`.
3. :xref:`Contribute to Mautic` with other skills
4. Become a :xref:`Become a Member of Mautic`
5. Support Mautic on :xref:`Open Collective`

.. toctree::
   :maxdepth: 2
   :caption: Development Environment
   :hidden:

   development-environment/getting_started
   development-environment/how_to_install_with_ddev
   development-environment/setup
   development-environment/environments

.. toctree::
   :maxdepth: 2
   :caption: Design and UX
   :hidden:

   design/availability
   design/displaying_elements_based_on_user_permissions
   design/feedback
   design/labelling
   design/notifications
   design/flash_messages
   design/protip
   design/quick_filters
   design/retrieving_system_information
   design/utilities

.. toctree::
   :maxdepth: 2
   :caption: Design templates
   :hidden:

   design_templates/accordion
   design_templates/protip
   design_templates/tiles

.. toctree::
   :maxdepth: 2
   :caption: Themes
   :hidden:

   themes/getting_started
   themes/grapesjs
   themes/legacy
   themes/forms
   themes/system

.. toctree::
   :maxdepth: 2
   :caption: Form Hooks
   :hidden:

   form_hooks/getting_started
   form_hooks/general_hooks
   form_hooks/validation_hooks
   form_hooks/response_hooks

.. toctree::
   :maxdepth: 2
   :caption: Webhooks
   :hidden:

   webhooks/getting_started
   webhooks/example_scripts
   webhooks/events/index

.. toctree::
   :caption: Mautic Marketplace
   :hidden:

   marketplace/getting_started
   marketplace/listing
   marketplace/allowlist_what_and_why
   marketplace/best_practices

.. toctree::
   :caption: Plugins
   :hidden:

   plugins/getting_started
   plugins/autowiring
   plugins/mautic_vs_symfony
   plugins/dependencies
   plugins/structure
   plugins/config
   plugins/event_listeners
   plugins/installation
   plugins/data
   plugins/cache
   plugins/translations
   plugins/continuous_integration
   plugins/update_m4_to_m5
   plugins/mvc
   plugins/permissions

.. toctree::
   :maxdepth: 3
   :caption: Plugin Extensions
   :hidden:

   plugin_extensions/manipulating_contacts
   plugin_extensions/api
   plugin_extensions/campaigns
   plugin_extensions/categories
   plugin_extensions/channels
   plugin_extensions/contacts
   plugin_extensions/emails
   plugin_extensions/forms
   plugin_extensions/forms_advanced
   plugin_extensions/integrations
   plugin_extensions/landing_pages
   plugin_extensions/maintenance
   plugin_extensions/points
   plugin_extensions/reports
   plugin_extensions/ui
   plugin_extensions/webhooks

.. toctree::
   :maxdepth: 2
   :caption: Plugin Integrations
   :hidden:

   plugin_integrations/integrations

.. toctree::
   :maxdepth: 2
   :caption: Plugin Services
   :hidden:

   plugin_services/cookie_helper
   plugin_services/database
   plugin_services/event_dispatcher
   plugin_services/factory
   plugin_services/ip_lookups
   plugin_services/mail_helper
   plugin_services/model_factory
   plugin_services/parameters
   plugin_services/paths_helper
   plugin_services/plugin_config_helper
   plugin_services/request
   plugin_services/router
   plugin_services/security
   plugin_services/session
   plugin_services/translator
   plugin_services/user

.. toctree::
   :maxdepth: 3
   :caption: Miscellaneous
   :hidden:

   plugin_miscellaneous/commands
   plugin_miscellaneous/events
   plugin_miscellaneous/flash_messages
   plugin_miscellaneous/forms
   plugin_miscellaneous/helpers
   plugin_miscellaneous/translated_entities
   plugin_miscellaneous/variant_entities

.. toctree::
   :maxdepth: 2
   :caption: REST API
   :hidden:

   rest_api/getting_started
   rest_api/authentication
   rest_api/assets
   rest_api/campaigns
   rest_api/categories
   rest_api/companies
   rest_api/contacts
   rest_api/data
   rest_api/dynamic_content
   rest_api/emails
   rest_api/fields
   rest_api/files
   rest_api/focus
   rest_api/forms
   rest_api/messages
   rest_api/notes
   rest_api/notifications
   rest_api/pages
   rest_api/point_actions
   rest_api/point_groups
   rest_api/point_triggers
   rest_api/reports
   rest_api/roles
   rest_api/segments
   rest_api/stages
   rest_api/stats
   rest_api/tags
   rest_api/text_messages
   rest_api/themes
   rest_api/tweets
   rest_api/users
   rest_api/webhooks

.. toctree::
   :maxdepth: 2
   :caption: MauticJS API
   :hidden:

   mauticjs_api/tracking_script

.. toctree::
   :maxdepth: 2
   :caption: Testing
   :hidden:

   testing/e2e_test_suite

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
