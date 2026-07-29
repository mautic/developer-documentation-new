Building CSS and frontend files
###############################

Mautic uses SCSS for styling core UI Components and the SymfonyCasts Sass Bundle to compile them during development and for production builds.

.. vale off

Building SCSS during development
================================

.. vale on

To compile Sass files, run:

.. code-block:: bash

    composer sass:build

To automatically rebuild on file changes during development:

.. code-block:: bash

    composer sass:watch

The SCSS source files live in ``app/bundles/CoreBundle/Assets/css/``. The watch command rebuilds CSS automatically when files in this directory change.

.. vale off

Building assets for production
==============================

.. vale on

.. vale off

To build all frontend assets for production:

.. vale on

.. code-block:: bash

    composer generate-assets

.. vale off

This builds the Sass files, compiles assets through Asset Mapper to ``var/assets/`` and ``public/assets/``, and generates minified CSS and JavaScript files in the ``media/`` directory.

.. vale on

You can also run the console command directly:

.. code-block:: bash

    bin/console mautic:assets:generate

Running ``composer install`` automatically compiles the Sass files, so fresh installations include built CSS by default.

.. vale off

The production build also generates ``css/offline.css``, a compatibility stylesheet that combines the compiled Sass output with ``app.css``. Standalone pages that can't load assets through Asset Mapper's normal page head, such as the offline page, link to this single style sheet directly.

.. vale on

Bootstrap framework
===================

Mautic uses Bootstrap 3.4.1 for its UI framework. The Bootstrap source files come from the ``twbs/bootstrap-sass`` Composer package and are available for importing in your SCSS files.

.. vale off

Asset Mapper architecture
=========================

.. vale on

Mautic uses Symfony Asset Mapper and Importmap for managing frontend JavaScript modules. The Asset Mapper configuration lives in ``app/config/config.php`` and the import map in ``importmap.php``.

.. vale off

Compiled CSS outputs to ``var/sass/``. Asset Mapper serves it through Symfony's asset system in development. Production builds copy finalized assets to ``media/css/``.

.. vale on
