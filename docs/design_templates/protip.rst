ProTip template to enhancing user experience
############################################

The ProTip template displays a helpful tip to Users, guiding them on how to use the platform like a pro.

To include a ProTip in Mautic, use the following syntax:

.. code-block:: twig

    {{ include('@MauticCore/Modules/protip.html.twig', {tip: 'mautic.protip.contacts.view'}) }}

In this example, it includes the ProTip template and passes a translation key - ``mautic.protip.contacts.view`` - as the tip content. This specific tip informs Users about using the ``V`` key to switch between card and table views.
