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

Mautic uses Bootstrap 5.3.8 for its UI framework. The Bootstrap SCSS source files come from the ``twbs/bootstrap`` Composer package. Mautic adds ``vendor/twbs/bootstrap/scss`` to the Sass load path, so you can import Bootstrap partials in your SCSS files.

Build new Plugin templates, styles, and JavaScript with Bootstrap 5 classes, ``data-bs-*`` attributes, and the Bootstrap 5 JavaScript API.

A temporary compatibility layer keeps existing Plugin code written for Bootstrap 3 working in the Mautic UI:

* ``app/bundles/CoreBundle/Assets/css/libraries/bootstrap/_bootstrap-3-compatibility.scss`` provides the Bootstrap 3 classes and styles on top of Bootstrap 5.
* ``app/bundles/CoreBundle/Assets/js/1.bootstrap-compatibility.js`` maps Bootstrap 3 data attributes, such as ``data-toggle`` and ``data-target``, to their Bootstrap 5 ``data-bs-*`` equivalents, and keeps Bootstrap 3 jQuery calls, such as ``$(element).modal('show')``, working.

.. note::

   Mautic 8 removes the Bootstrap 3 compatibility layer. Update existing Plugin code to Bootstrap 5 before you upgrade to Mautic 8. For other changes in Mautic 8, see the :xref:`Mautic 8 UPGRADE-8.0.md`.

.. vale off

Asset Mapper architecture
=========================

.. vale on

Mautic uses Symfony Asset Mapper and Importmap for managing frontend JavaScript modules. The Asset Mapper configuration lives in ``app/config/config.php`` and the import map in ``importmap.php``.

.. vale off

Compiled CSS outputs to ``var/sass/``. Asset Mapper serves it through Symfony's asset system in development. Production builds copy finalized assets to ``media/css/``.

.. vale on
