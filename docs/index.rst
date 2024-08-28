Welcome to Mautic's developer documentation
===========================================

.. note::
    Work is ongoing bringing over some of the content from the old documentation, which you can find at :xref:`Mautic Developer Portal`. Please see the :xref:`Mautic Dev Docs Issues` if you'd like to help with completing this work.

Welcome to the Mautic Developer Documentation. The documentation broadly covers building custom Plugins for Mautic which extends its features, building custom Themes, and how to integrate applications outside of Mautic using the REST API.

This documentation has multiple versions for different releases of Mautic starting from Mautic 4.x - the switcher is in the bottom left which allows you to change between versions.

Submitting code to Mautic
*************************

Development is open and available to any member of the Mautic community. All fixes and improvements happen through pull requests to the code on :xref:`Mautic's GitHub Repo`. This code is open source and publicly available.

Read all about contributing to Mautic as a Developer in the :xref:`Mautic Developer Contribution Guide`.

Read more about Mautic's :xref:`Mautic Code Governance` and the :xref:`Mautic Project Governance` model.

Your code must follow the :xref:`Symfony coding standards`. You can find details about where Mautic deviates from these standards documented in the :doc:`/plugins/mautic_vs_symfony` section.

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

   design/feedback

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
   plugins/translations
   plugins/continuous-integration
   plugins/from-4-to-5

.. toctree::
   :maxdepth: 2
   :caption: Extending Mautic
   :hidden:

   components/api
   components/cache
   components/campaigns
   components/categories
   components/channels
   components/config
   components/contacts
   components/core
   components/emails
   components/forms
   components/forms_advanced
   components/integrations
   components/ip_lookups
   components/landing_pages
   components/maintenance
   components/points
   components/queue
   components/reports
   components/security
   components/tracking_script
   components/translator
   components/ui

.. toctree::
   :maxdepth: 2
   :caption: REST API
   :hidden:

   rest_api/assets
   rest_api/campaigns
   rest_api/categories
   rest_api/contacts
   rest_api/fields
   rest_api/notifications
   rest_api/point_groups
   rest_api/reports
   rest_api/text_messages

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
