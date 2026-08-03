Focus Item scripts
##################

Focus Items can be embedded on external sites. Mautic splits the embed JavaScript into consent-aware parts so a site can render a Focus Item before consent and add tracking only after consent.

.. note::

   For guidance on creating and configuring Focus Items in the Mautic UI, see the :xref:`Mautic User Documentation<Mautic End User Docs>`. This page documents only the developer-facing split scripts.

The Focus split scripts follow the same scope model described in :ref:`Script scopes and split scripts<mauticjs_api/tracking_script:Script scopes and split scripts>`. The scopes below apply that same model to Focus Items.

.. vale off

Split Focus scripts and scope model
***********************************

.. vale on

Focus embedding is split into three scopes:

* ``RUNTIME`` - the anonymous bootstrap that the other scopes depend on. It performs no tracking.
* ``DISPLAY`` - loads and renders the Focus Item. It adds no tracking pixel, no Contact tokens, and no ``mauticform[focusId]`` marker.
* ``TRACKING`` - resolves the tracked Contact, generates the trackable redirect, and installs the view pixel and the Form focus-id marker.

These are Focus-specific scope labels. They mirror the ``BuildJsScope`` model documented on the tracking script page, but they aren't the same ``enum``.

.. vale off

Generated scripts and endpoints
*******************************

.. vale on

Mautic serves the scopes through separate endpoints so a site can load only what it needs before consent, then add tracking later. Each endpoint path resolves against your Mautic instance's base URL.

.. list-table::
   :header-rows: 1

   * - Endpoint
     - Included scopes
     - Purpose
   * - ``/focus/{id}/display.js``
     - ``RUNTIME`` and ``DISPLAY``
     - Renders the Focus Item with no tracking.
   * - ``/focus/{id}/tracking.js``
     - ``TRACKING``
     - Adds the tracking layer for a Focus Item that's already displayed.
   * - ``/focus/{id}.js``
     - ``RUNTIME``, ``DISPLAY``, and ``TRACKING``
     - The legacy aggregate script. Unchanged and backward compatible; still returns the full combined script.

All three endpoints send the ``Cache-Control: private, no-store`` response header.

.. vale off

Client-side runtime globals
***************************

.. vale on

The split scripts expose a small set of client-side global variables, a callback, and an event so a site can control when tracking activates:

* ``window.MauticFocusItems`` - a registry keyed by Focus Item id. Each entry is the runtime for that Focus Item and exposes methods to load and activate the tracking layer. The display script uses it to lazily inject and activate tracking.
* ``window.MauticFocusTrackingQueue`` - a queue that bridges consent. Activation requests made before the tracking layer is ready are queued and flushed once it loads.
* ``window.MauticFocusUseMauticTrackingConsent`` - when set to ``true``, the Focus display script auto-activates tracking as soon as Mautic website tracking becomes enabled, instead of waiting for a manual or CMP activation. The copied website-tracking snippet sets it to ``true`` when an administrator turns on the 'Use Mautic consent for Focus tracking' option.
* ``enableMauticFocusTracking{id}()`` - the per-Focus-Item activation callback a site wires into its consent-management platform (CMP). Calling it activates the tracking layer for that Focus Item.
* ``mautic:tracking-enabled`` - a document event the tracking layer dispatches once tracking initializes. The Focus runtime listens for it to bridge consent, mirroring how browser code can listen for the tracking layer's readiness signals described under :ref:`Client-side runtime globals<mauticjs_api/tracking_script:Client-side runtime globals>`.

.. vale off

Activating tracking after consent
*********************************

.. vale on

Wire the per-Focus-Item callback into your CMP so it runs on the visitor's consent event. Use native JavaScript, since ``jQuery`` and other libraries aren't guaranteed to be available on third party sites:

.. code-block:: js

   // called by your consent-management platform once the visitor consents
   window.enableMauticFocusTracking123();

If the tracking layer hasn't loaded yet, the activation request is queued in ``window.MauticFocusTrackingQueue`` and flushed once the layer loads.

Alternatively, set ``window.MauticFocusUseMauticTrackingConsent`` to ``true`` to let the Focus display script auto-activate tracking as soon as Mautic website tracking becomes enabled. On that path the Focus runtime activates in response to the ``mautic:tracking-enabled`` document event rather than waiting for a manual or CMP call.

.. vale off

Dynamic Web Content injection behavior
**************************************

.. vale on

The Dynamic Web Content build-JS subscriber now parses Dynamic Web Content through the DOM rather than treating it as opaque markup. It injects only same-origin Focus scripts. It always allows ``/focus/{id}/display.js`` so a Focus Item renders regardless of consent state. It injects the legacy ``/focus/{id}.js`` only when ``MauticJS.trackingEnabled`` is ``true``, so the combined tracking-capable script loads through Dynamic Web Content only once tracking is active.
