Getting started with themes
==========================================================

Themes can be used to create default content and layouts for emails and landing pages. Content is written in the `Twig templating language <https://twig.symfony.com/>`__.

They can also be used to customize form pages (when visiting /form/ID) or using an iframe to embed a form into a 3rd party page. One can also customize the form structure and fields but this must be done with PHP files which disqualifies the theme from being installable through Mautic's Theme manager and manually uploaded to the server.

Finally, a special ``system`` theme can be used to override system templates to avoid customizing core code that could be lost with future upgrades.

Directory Structure
==========================================================

A theme is made of three components: the config, twig files (HTML content), and thumbnails::

    config.json
        html/
            email.html.twig
            form.html.twig
            message.html.twig
            page.html.twig
    thumbnail.png
    thumbnail_email.png
    thumbnail_form.png
    thumbnail_page.png

Config File
-----------

The config file tells Mautic how to utilize the theme.

.. code-block:: json

    {
      "name": "Theme Name",
      "author": "John Doe",
      "authorUrl": "https://john-doe-the-mautic-theme-builder.com",
      "features": [
        "email",
        "form",
        "page"
      ],
      "builder": ["legacy", "grapesjsbuilder"]
    }

name
    This is the name of the theme as displayed in Mautic.
author
    This displays in the theme manager as credit to the author of the theme.
authorUrl
    URL used for the author link.
features
    An array of strings that tells Mautic which features the theme supports. Currently recognized values are ``email`` (email builder template), ``form`` (formatting the form page) and ``page`` (page builder template). A corresponding ``html/[feature].html.twig`` file is required for each feature supported. For example, if the theme supports ``email``, then there should be a ``html/email.html.twig`` file. See Twig Files more information on each feature.
builder
    Array of strings for which builder the theme supports. Currently only applies to themes that support ``page`` or ``email``. By default, themes without this will only be recognized by Mautic's legacy builder. New themes built should declare the specific builders it supports.

Twig Files
-------------------------

html/message.html.twig
^^^^^^^^^^^^^^^^^^^^^^

This file is a simple message file mainly used as the landing page for when a lead unsubscribes or resubscribes to the system’s emails. But may be used by other areas so should be included in all themes.

It requires echoing two variables: ``message`` and ``content``. ``message`` contains the string message such as "You have been unsubscribed..." content will either be empty or contain the HTML of a form that's been associated with the email as an unsubscribe form.

.. code-block:: twig

    <html>
        <head></head>
        <body>
            <div>
                <h2>{{ message|raw }}</h2>
                {% if content is defined %}
                <div>{{ content|raw }}</div>
                {% endif %}
            </div>
        </body>
    </html>

html/email.html.twig
^^^^^^^^^^^^^^^^^^^^^^

This file defines the base template when creating a new email and should contain HTML suited for email clients.

The GrapesJs builder supports the `mjml email framework <https://mjml.io/>`__.

.. code-block:: html

    <mjml>
      <mj-body>
        <mj-raw>
          <!-- Company Header -->
        </mj-raw>
        <mj-section background-color="#f0f0f0">
          <mj-column>
            <mj-text font-style="bold" font-size="24px" color="#6f6f6f">My Company</mj-text>
          </mj-column>
        </mj-section>
        <mj-raw>
          <!-- Confirm  text -->
        </mj-raw>
        <mj-section background-color="#fafafa">
          <mj-column width="400px">
            <mj-text font-style="bold" font-size="22px" font-family="Helvetica Neue" color="#626262">Please confirm your subscription!</mj-text>
            <mj-button background-color="#F45E43" font-style="bold" href="#">Yes, subscribe me to the list</mj-button>
            <mj-text color="#525252" font-size="16" line-height="1.5">If you received this email by mistake, simply delete it. You won't be subscribed if you don't click the confirmation link above.<br/><br/>For questions about this list, please contact:
    email@email.com</mj-text>
          </mj-column>
        </mj-section>
            <mj-raw>
          <!-- Confirm  text -->
        </mj-raw>
            <mj-section background-color="#fafafa">
          <mj-column width="400px">
            <mj-text color="#525252" line-height="1.2">
              <p>Company Name<br/>111 Amazing Street<br/>
                Beautiful City</p></mj-text>

          </mj-column>
        </mj-section>
      </mj-body>
    </mjml>

html/page.html.twig
^^^^^^^^^^^^^^^^^^^^^^

This file defines the base template when creating a new landing page and can contain advanced HTML for browsers.

.. code-block:: twig

    <!DOCTYPE html>
    <html>
        <head>
            {% if page is defined %}
            <title>{pagetitle}</title>
            <meta name="description" content="{pagemetadescription}">
            {% endif %}
            {{ outputHeadDeclarations() }}
        </head>
        <body>
            {{ outputScripts('bodyOpen') }}
            {% block content %}{% endblock %}
            {{ outputScripts('bodyClose') }}
        </body>
    </html>


html/form.html.twig
^^^^^^^^^^^^^^^^^^^^^^

This is used to format the page a form is embedded into when viewing the form at /form/ID or when using the iframe method of embedding a form into a 3rd party page.

This should output the variables ``message``, ``header``, and ``content``.

See Customizing Forms on how to customize form fields.

.. code-block:: twig

    <html>
        <head></head>
        <body>
            {% if message is defined %}
                <div>
                    <h2>{{ message|raw }}</h2>
                </div>
            {% endif %}

            <div>
                {% if header is defined %}
                <h4>{{ header }}</h4>
                {% endif %}
                {{ content|raw }}
            </div>
        </body>
    </html>

Thumbnails
----------

The thumbnail should be a screenshot of the theme with demo content. The width x height should be 575 x 600 px. This thumbnail will be available for Mautic users for quick theme preview in the Email edit form, Landing Page edit form and the Theme Manager.

Mautic will look for ``thumbnail.png`` as default but if you want a specific image for different templates, you can add a ``thumbnail_[feature].png`` per feature with a custom thumbnail. For example, ``thumbnail_email.png``, ``thumbnail_page.png`` or ``thumbnail_form.png``.
