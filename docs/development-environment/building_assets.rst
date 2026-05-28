Building CSS and frontend assets
################################

Mautic uses SCSS for styling core UI components and the SymfonyCasts Sass Bundle to compile them during development and for production builds.

Building SCSS during development
================================

To compile Sass files, run:

.. code-block:: bash

    composer sass:build

To automatically rebuild on file changes during development:

.. code-block:: bash

    composer sass:watch

The SCSS source files live in ``app/bundles/CoreBundle/Assets/css/``. The watch command recompiles when files in this directory change.

Building assets for production
==============================

To build all frontend assets for production:

.. code-block:: bash

    composer generate-assets

This builds the Sass files, compiles Asset Mapper assets, and generates minified CSS and JavaScript files in the ``media/`` directory.

You can also run the console command directly:

.. code-block:: bash

    bin/console mautic:assets:generate

Running ``composer install`` automatically compiles the Sass files, so fresh installations include built CSS by default.

Bootstrap framework
===================

Mautic uses Bootstrap 3.4.1 for its UI framework. The Bootstrap source files come from the ``twbs/bootstrap-sass`` Composer package and are available for importing in your SCSS files.

Asset architecture
==================

Mautic uses Symfony Asset Mapper and Importmap for managing frontend JavaScript modules. The Asset Mapper configuration lives in ``app/config/config.php`` and the import map in ``importmap.php``.

Compiled CSS outputs to ``var/sass/``. Asset Mapper serves it through Symfony's asset system in development. Production builds copy finalized assets to ``media/css/``.
