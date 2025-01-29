Getting started with Themes
###########################

You can use Themes to create default content and layouts for Emails and Landing Pages written in the :xref:`Twig documentation`.

.. vale off

You can use Themes to also customize Mautic Forms, for example when visiting ``/form/ID``, or using an iframe to embed a Form into a third party page. You can customize the Form structure and fields but need to use PHP files, which disqualifies the Theme from being installable through Mautic's Theme manager. It must therefore be manually uploaded to the server.

.. vale on

Finally, use a special ``system`` Theme to override system templates to avoid losing core code changes with future upgrades.

Directory structure
*******************

A Theme consists of three components: the configuration, Twig files with content, and thumbnails.

.. code-block:: json

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

Configuration file
==================

The configuration file tells Mautic how to utilize the Theme.

.. code-block:: javascript

    {
      "name": "Theme Name",
      "author": "John Doe",
      "authorUrl": "https://example.com",
      "features": [
        "email",
        "form",
        "page"
      ],
      "builder": ["legacy", "grapesjsbuilder"]
    }

**name**
    This is the name of the Theme as displayed in Mautic.

**author**
    This displays in the Theme manager as credit to the author of the Theme. Any Themes added to Mautic Core use 'Mautic Team' as the author.

**authorUrl**
    This enables the author to provide a URL displayed in the Theme manager.

**features**
    An array of strings that tells Mautic which features the Theme supports. Currently recognized values are:

    ``email`` The Theme is compatible with the Email Builder. See :ref:`themes/getting_started:html/email.html.twig`.

.. vale off

    ``form`` The Theme is compatible with the customizing Forms. See :ref:`themes/getting_started:html/form.html.twig`.

.. vale on

    ``page`` The Theme is compatible with the Page Builder. See :ref:`themes/getting_started:html/page.html.twig`.

    A corresponding ``html/[feature].html.twig`` file is required for each feature supported. For example, if the Theme supports ``email``, then there should be a ``html/email.html.twig`` file. See :ref:`themes/getting_started:Twig files` more information on each feature.
builder
    This contains an array of strings declaring which Builder the Theme supports. This currently only applies to Themes that support ``page`` or ``email``. By default, Themes without this line are only recognized by Mautic's Legacy Builder. New Themes built should declare the specific Builders it supports.

Twig files
==========

``html/message.html.twig``
--------------------------

This file is mainly used as the Landing Page for when a Contact unsubscribes or resubscribes to the system's Emails. Other areas use this so all Themes should include it.

It requires echoing two variables: ``message`` and ``content``.

``message`` contains the string message such as "You have been unsubscribed."

.. vale off

``content`` is empty or contains the HTML of a Form associated with the Email as an unsubscribe Form.

.. vale on

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

``html/email.html.twig``
------------------------

This file defines the base template when creating a new Email and should contain HTML suited for email clients.

The GrapesJS Builder supports the :xref:`MJML email framework`.

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
    email@example.com</mj-text>
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

``html/page.html.twig``
-----------------------

This file defines the base template when creating a new Landing Page and can contain advanced HTML for browsers.

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


``html/form.html.twig``
-----------------------
.. vale off

Mautic uses this file when accessing the form at /form/ID, embedding a Form in a Landing Page, or using the iframe method of embedding a Form into a third party page.

This should output the variables ``message``, ``header``, and ``content``.

See :ref:`themes/forms:Customizing forms` on how to customize Form fields.

.. vale on

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
==========

.. vale off

The thumbnail should be a screenshot of the Theme with demo content. The dimensions should be 575x600px. Mautic displays thumbnails in the Email edit Form, Landing Page edit Form, and the Theme Manager.

.. vale on

Mautic looks for ``thumbnail.png`` by default, however if you want a specific image for different feature, you can add a ``thumbnail_[feature].png`` with a custom thumbnail. For example, ``thumbnail_email.png``, ``thumbnail_page.png`` or ``thumbnail_form.png``.

Preparing your Theme for Packagist
**********************************

Mautic uses Packagist to distribute Themes and Plugins. There are certain steps you must take to ensure readiness of your Theme for distribution.

1. Ensure there is a ``composer.json`` file in the root of your Theme directory. Ensure it contains the following information, inn particular verifying the minimum supported version of Mautic:

.. code-block:: json

  {
    "name": "mautic/theme-yourthemename",
    "description": "A theme for Mautic",
    "type": "mautic-theme",
    "keywords": ["mautic", "theme"],
    "extra": {
      "install-directory-name": "yourthemename"
    },
    "minimum-stability": "dev",
    "require": {
      "mautic/core": "^5.0"
    }
  }

1. Ensure that you add a ``close_pull_requests.yml`` file in the ``.github/workflows`` folder of your Theme. This file automatically close pull requests opened in the Theme repository. Please review other Themes for examples.

2. Ensure that you add your Theme to, or create, the following files:
  
    - ``.github/subtree-splitter-config.json`` - this file sets up the connection between the folder in the Mautic GitHub repository and the theme's individual repository. When merging changes into Core which impact this theme or making releases, GitHub pushes into the theme's repository automatically.  Add your Theme at the end of the list.
    - ``.github/workflows/gitsplit/theme-yourthemename.json`` - GitHub Actions uses this file to sync changes to the theme's repository. Create one for each new theme added to the Mautic repository.
    - ``.githu/workflows/split-monorepo-in-multi-repo.yml`` - this file is used by the GitHub Action to create the matrix used when splitting up the repository and pushing changes out to the theme repositories. Update this file with the new theme names.

3. Make the Pull Request with your Theme and the relevant files from previous steps to the Mautic repository. Once merged, the GitHub Action automatically pushes the changes out to your Theme repository.

4. Ask the core team to create a new repository in the Mautic GitHub organization for your Theme. They must add the core team to the repository for GitHub Actions to work. The repository naming convention is ``theme-yourthemename``.

5. Once merged, ask the Core Team to create a Packagist package for your Theme. Once created, make another PR, adding the package to the ``composer.json`` file. Ensure that you also run ``composer require mautic/theme-yourthemename`` which updates the ``composer.lock`` file, adding your new theme. Then, review the ``composer.json`` file and move the package from the 'require' section to the 'replace' section, using ``self.version``. Commit both the ``composer.json`` and ``composer.lock`` files. 

6. Once merged, make your final PR to the :xref:`Recommended Project` repository where you add your Theme to the end of the list in ``composer.json``.

7. Celebrate, you made it - congratulations 🥳.