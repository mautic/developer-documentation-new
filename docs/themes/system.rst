Overriding core view templates
##############################

You can override any view's template in Mautic by creating a ``themes/system`` directory, copying the core template file into a corresponding directory and customizing the HTML.

For example, to customize the login page, copy ``app/bundles/UserBundle/Resources/views/Security/login.html.twig`` into ``themes/system/UserBundle/Resources/views/Security/login.html.twig`` then make the desired changes.

.. Warning:: Customizations may break Mautic updates core templates in future versions. It's best practice to review and reconcile customizations with core templates after each upgrade.