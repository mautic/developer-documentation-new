Overriding core view templates
==========================================================

You can override any view's template in Mautic by creating a ``themes/system`` directory, copying the core template file into a corresponding directory and customizing the HTML.

For example, to customize the login page. Copy ``app/bundles/UserBundle/Views/Security/login.html.php`` into ``themes/system/MauticUserBundle/Security/login.html.php`` then make the desired changes.

.. Warning:: Future Mautic upgrades may break if core templates were updated. Overridden core templates must be reconciled with changes done in future upgrades.