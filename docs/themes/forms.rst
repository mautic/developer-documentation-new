Customizing Forms
==========================================================

To provide custom Form field templates or to manipulate the Form body, create the following directory structure::

    html/
        MauticFormBundle
            Builder <– for customizing the form structure itself
            Field <– for customizing form field types

Copy from ``app/bundles/FormBundle/Views/Builder/form.html.php`` into the theme’s Builder directory and/or one or more of the fields templates in ``app/bundles/FormBundle/Views/Field/*.html.php`` into the theme’s Field directory. Then customize to the desired layout. Note that these must be PHP templates.

You can add a custom stylesheet to the form by adding a ``style.html.twig`` with your custom CSS to ``html/MauticFormBundle/Builder``. The best way is to copy the content of the default form styles and modify them to your needs.
