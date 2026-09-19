GrapesJS Builder
################

MJML
****

The GrapesJS Builder doesn't require any special HTML syntax to edit content in the Builder. However, for Emails, it supports the :xref:`MJML email framework` to create responsive emails.

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

.. vale off

MJML Theme tokens
*****************

.. vale on

From Mautic 7, the GrapesJS Builder supports MJML Theme tokens. You can define reusable style classes in the ``<mj-head>`` section of your MJML Email templates using ``<mj-class>`` elements inside an ``<mj-attributes>`` block. When Users drop new Components into the Email Builder, Mautic automatically applies the matching Theme tokens, keeping styling consistent across the Email.

.. vale off

Defining Theme tokens
=====================

.. vale on

Define Theme tokens in the ``<mj-head>`` section of your MJML template using ``<mj-class>`` elements wrapped in ``<mj-attributes>``. Each class specifies CSS properties that apply to Components using it. Self-closing syntax - for example ``<mj-class ... />`` - causes parsing issues. Always use explicit open/close pairs.

.. code-block:: html

    <mjml>
      <mj-head>
        <mj-attributes>
          <mj-class name="t-body" color="#333333" font-family="Arial, sans-serif"></mj-class>
          <mj-class name="t-btn" background-color="#007bff" color="#ffffff"></mj-class>
          <mj-class name="t-btn-primary" border-radius="4px"></mj-class>
          <mj-class name="t-section" padding="20px"></mj-class>
          <mj-class name="t-surface-1" background-color="#f8f9fa"></mj-class>
        </mj-attributes>
      </mj-head>
      <mj-body>
        <mj-section mj-class="t-section t-surface-1">
          <mj-column>
            <mj-text mj-class="t-body">Welcome to our newsletter</mj-text>
            <mj-button mj-class="t-btn t-btn-primary" href="#">Click here</mj-button>
          </mj-column>
        </mj-section>
      </mj-body>
    </mjml>

The builder parses these ``<mj-class>`` definitions and applies them to matching Component types automatically.

GrapesJS Builder Plugins
************************

From Mautic 5.1 it's possible to create Plugins for the GrapesJS Builder. This allows you to add custom blocks, Components, and styles to the Builder. It's how the GrapesJS Preset works, which ships with Mautic.

This uses the :xref:`grapesjs-plugins` feature. Read more about the potential this unlocks in the :xref:`grapesjs-api`.

.. vale off

Creating a Plugin for GrapesJS
===============================

.. vale on

To create a Plugin for the GrapesJS Builder, you need to create a new Bundle in Mautic. This contains the Plugin and any other related code.

1. Create a new Bundle in Mautic, for example ``GrapesJSCustomPluginBundle``.
2. Create a GrapesJS Plugin - for example ``.Assets/src/index.ts`` - as follows. Note this uses TypeScript but vanilla JS also works:

.. code-block:: typescript

        import grapesjs from 'grapesjs';

        // declare type for window so TS will not complain during compiling
        declare global {
            interface Window {
                MauticGrapesJsPlugins: object[];
            }
        }

        export type PluginOptions = {
        };

        export type RequiredPluginOptions = Required<PluginOptions>;

        const GrapesJsCustomPlugin: grapesjs.Plugin<PluginOptions> = (editor, opts: Partial<PluginOptions> = {}) => {
            const options: RequiredPluginOptions = {
                ...opts
            };
            console.log('Run GrapesJsCustomPlugin...')
            console.log('Options passed to GrapesJsCustomPlugin:', options)
            editor.on('load', () => {
                console.log('GrapesJsCustomPlugin: editor.onLoad()')
            });
        }

        // export the plugin in case someone wants to use it as source module
        export default GrapesJsCustomPlugin;

        // create a global window-object which holds the information about GrapesJS plugins
        if (!window.MauticGrapesJsPlugins) window.MauticGrapesJsPlugins = [];
        // add the plugin-function with a name to the window-object
        window.MauticGrapesJsPlugins.push({
            name: 'GrapesJsCustomPlugin', // required
            plugin: GrapesJsCustomPlugin, // required
            context: ['page', 'email-mjml'], // optional. default is none/empty, so the plugin is always added; options: [page|email-mjml|email-html]
            pluginOptions: { options: { test: true, hello: 'world'} } // optional
        })

Due to the ``export default``, you can use this Plugin in a fork, customizing the source files with ``import GrapesJSCustomPlugin from 'path'``. But this isn't required - you can also write a plain JS function as described in the :xref:`grapesjs-plugins` documentation.

3. Add the JavaScript file - compiled or source - to the ``AssetSubscriber`` of your Plugin bundle:

.. code-block:: php

      public function injectAssets(CustomAssetsEvent $assetsEvent): void
    {
        if ($this->config->isPublished()) {
            $assetsEvent->addScript('plugins/GrapesJsCustomPluginBundle/Assets/dist/index.js');
        }
    }

The resulting HTML source appears as follows:

.. code-block:: html

  <script src="/plugins/GrapesJsCustomPluginBundle/Assets/dist/index.js?v6e9fccee" data-source="mautic"></script>
  <script src="/plugins/GrapesJsBuilderBundle/Assets/library/js/dist/builder.js?v6e9fccee" data-source="mautic"></script>

.. note:: 
  The Plugin code loads before ``builder.js`` which results in the data registering in the global window object.

You can download a :xref:`GrapesJS Demo Plugin` to get you started.

.. vale off

Building the Builder assets
***************************

From Mautic 7.2, Mautic no longer commits the GrapesJS Builder's compiled JavaScript and CSS to the repository. The build output lives in the Plugin's ``Assets/library/js/dist/`` directory, which ``.gitignore`` now excludes, and Mautic generates it at build time instead - the same way it handles other compiled assets such as ``media/css`` and ``media/js``.

This matters when you work from a git checkout. After a fresh clone, the ``dist/`` directory doesn't exist yet, so the Builder can't load until you build the assets. Missing assets don't cause Mautic to fail. It logs a warning and skips loading the Builder scripts. Build them before you use the GrapesJS Builder.

Building the assets requires Node, and Mautic builds them with Node 24. In most cases, you don't need to run the build by hand because Mautic builds the assets automatically at these points:

* When you run ``composer install`` or ``composer update``. This step is non-fatal - if Node isn't available, Composer prints a warning and continues, so you can build the assets later.
* When DDEV provisions the environment for the first time, not on every start, so for an existing environment, run ``ddev gjs-build`` to rebuild.

To build or rebuild the assets manually with Composer, run:

.. code-block:: bash

    composer gjs-build

With DDEV, run:

.. code-block:: bash

    ddev gjs-build

Both commands install the Plugin's ``npm`` dependencies if needed, then build the assets. Under the hood, the build uses Parcel, which content-hashes the output filenames - for example, ``builder.4f2a.css`` - and writes a ``manifest.json`` that maps the logical asset names to the hashed files. At runtime, the Builder's ``AssetsSubscriber`` reads this manifest to resolve and inject the correct files.

.. vale on