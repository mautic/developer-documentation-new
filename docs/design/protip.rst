ProTip template to enhancing user experience
============================================

The ProTip template is a powerful feature that displays helpful tips to users, guiding them on how to use the platform like a pro. This template is implemented using Twig. Here's how this template works and how to effectively use it in Mautic.

Template structure and functionality
------------------------------------

The ProTip template is structured to conditionally render a tip when provided. Here's a breakdown of its key components:

.. code-block:: twig

    {% if tip is defined and tip is not empty %}
    <div class="col-xs-12 ai-center mt-md mb-md">
        <div class="text-muted">
            <i class="ri-lightbulb-line ri-lg"></i>
            <span class="fw-b">{{ 'mautic.core.protip'|trans }}</span>
            {{ tip|trans|raw }}
        </div>
    </div>
    {% endif %}

This template checks if a ``tip`` variable's defined and not empty. If these conditions are met, it renders a div containing the tip. The tip's displayed with a lightbulb icon, a "ProTip" label (translated), and the tip content itself.

The ``tip`` parameter's passed through Twig's ``trans`` filter, allowing for internationalization. The ``raw`` filter's also applied, enabling the use of HTML tags within the tip content. This is particularly useful for including elements like ``<kbd>`` tags to highlight keyboard shortcuts.

To include a ProTip in Mautic, one can use the following syntax:

.. code-block:: twig

    {{ include('@MauticCore/Helper/protip.html.twig', {tip: 'mautic.core.protip.contacts.view'}) }}

In this example, the ProTip template's included and a translation key (``mautic.core.protip.contacts.view``) is passed as the tip content. This specific tip informs users about using the ``V`` key to switch between card and table views.

The use of a translation key instead of a hardcoded string allows for easy localization of tips. It also promotes consistency across Mautic, as the same tip can be reused in multiple places by referencing its key.

Use the ProTip template to enhance the user experience of Mautic. These tips provide contextual help, highlighting shortcuts and features that users might otherwise overlook. It's important to keep tips concise, relevant, and actionable to maximize their effectiveness in guiding users to become power users.