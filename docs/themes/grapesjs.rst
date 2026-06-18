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

Extending an existing Component type
====================================

.. vale on

Plugins can also extend a Component type that already exists in the Builder instead of registering a new one. This is useful when you want to add traits to a built-in Component, such as an image, or change its HTML output.

Mautic ships an example of this in its ``grapesjs-image-link`` Plugin, which turns images in the Landing Page Builder into clickable links. It extends the built-in ``image`` Component type to add ``href``, ``target``, and ``rel`` traits, then overrides the Component's HTML output so that the Component wraps any image that has an ``href`` in an anchor tag. When the image has no ``href``, it renders as normal.

To extend an existing type, get the current type definition from ``editor.DomComponents``, keep a reference to the methods you want to build on, and re-register the type with ``addType``, using ``extend`` to inherit the original behavior. The ``defaults.traits`` array controls which traits appear in the Component settings panel, ``getAttrToHTML`` controls which attributes render on the element itself, and ``toHTML`` controls the final markup the Component produces.

.. code-block:: javascript

    export default (editor) => {
        const domComponents = editor.DomComponents;
        const imageType = domComponents.getType('image');

        if (!imageType || !imageType.model) {
            return;
        }

        const { model: ImageModel } = imageType;
        const originalGetAttrToHTML = ImageModel.prototype.getAttrToHTML;
        const originalToHTML = ImageModel.prototype.toHTML;

        domComponents.addType('image', {
            extend: 'image',
            model: {
                defaults: {
                    traits: ['alt', 'title', 'href', 'target', 'rel'],
                },

                // Keep the link attributes off the <img> element itself.
                getAttrToHTML() {
                    const attributes = { ...originalGetAttrToHTML.call(this) };
                    delete attributes.href;
                    delete attributes.target;
                    delete attributes.rel;
                    return attributes;
                },

                // Wrap the image in an anchor tag when an href is set.
                toHTML() {
                    const attributes = { ...(this.get('attributes') || {}) };
                    const href = attributes.href;

                    if (!href) {
                        return originalToHTML.call(this);
                    }

                    const imgHtml = originalToHTML.call(this);
                    return `<a href="${href}" style="display:inline-block;">${imgHtml}</a>`;
                },
            },
        });
    };

The Email editor has its own image-linking implementation, so this Plugin targets the Landing Page Builder only.