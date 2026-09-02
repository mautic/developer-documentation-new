Focus Item scripts
##################

You can embed Focus Items on external sites. Mautic splits the embed JavaScript into consent-aware parts so a site can render a Focus Item before consent and add tracking only after consent.

.. note::

   For guidance on creating and configuring Focus Items in the Mautic UI, see the :xref:`Mautic User Documentation<Mautic End User Docs>`. This documentation covers only the developer-facing split scripts.

The Focus split scripts follow an analogous but entirely separate scope model to the one described in :ref:`Script scopes and split scripts<mauticjs_api/tracking_script:Script scopes and split scripts>`. The scopes below apply that analogous but separate model to Focus Items.

.. vale off

Split Focus scripts and scope model
***********************************

.. vale on

Mautic splits Focus embedding into three scopes:

* ``RUNTIME`` - the anonymous bootstrap that the other scopes depend on. It performs no tracking.
* ``DISPLAY`` - loads and renders the Focus Item. It adds no tracking pixel, no Contact tokens, and no ``mauticform[focusId]`` marker.
* ``TRACKING`` - resolves the tracked Contact, generates the trackable redirect, and installs the view pixel and the Form focus-id marker.

These are Focus-specific scope labels. They mirror the ``BuildJsScope`` model documented on the tracking script reference, but they aren't the same ``enum`` and share no code path: ``BuildJsScope`` pairs ``RUNTIME`` and ``TRACKING`` with ``ESSENTIAL`` rather than ``DISPLAY``, and gates the ``mtc.js`` / ``mautic-tracking.js`` / ``mautic-essential.js`` script family, whereas these Focus scopes gate only the Focus scripts. Don't gate Focus code on ``BuildJsScope`` cases or vice versa.

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

The split scripts expose a small set of client-side global variables, a public method, and an event so a site can control when tracking activates:

* ``window.MauticFocus.enableTracking(<id>)`` - the public API for activating tracking on a displayed Focus Item after consent. If the Focus Item is registered in ``window.MauticFocusItems[id]``, it calls that item's ``loadTracking()``; otherwise it sets ``window.MauticFocusTrackingQueue[id] = true``, which the display script consumes once it registers the item.
* ``window.MauticFocusItems`` - a registry keyed by Focus Item ID. Each entry is the runtime for that Focus Item and exposes methods to load and activate the tracking layer. The display script uses it to lazily inject and activate tracking.
* ``window.MauticFocusTrackingQueue`` - a queue that bridges consent. The queue holds activation requests made before the tracking layer is ready and flushes them once it loads.
* ``window.MauticFocusUseMauticTrackingConsent`` - when set to ``true``, the Focus display script auto-activates tracking as soon as Mautic website tracking becomes enabled, instead of waiting for a manual or consent-management platform activation. The copied website-tracking snippet sets it to ``true`` when an administrator turns on the 'Use Mautic consent for Focus tracking' option.
* ``mautic:tracking-enabled`` - a document event the tracking layer dispatches once tracking initializes. The Focus runtime listens for it to bridge consent, mirroring the tracking layer's own dispatch of this event, documented in the ``mautic:tracking-enabled`` bullet under :ref:`Client-side runtime globals<mauticjs_api/tracking_script:Client-side runtime globals>`. This is the event-dispatch signal, not the ``mauticEssentialReady`` / ``MauticJS.runtimeReady`` readiness-guard pattern.

.. code-block:: js

   // check whether a Focus Item's runtime has registered yet
   if (window.MauticFocusItems && window.MauticFocusItems[123]) {
       window.MauticFocus.enableTracking(123);
   } else {
       // not ready yet — queue activation for when the display script loads
       window.MauticFocusTrackingQueue = window.MauticFocusTrackingQueue || {};
       window.MauticFocusTrackingQueue[123] = true;
   }

.. vale off

Activating tracking after consent
*********************************

.. vale on

Call the public ``window.MauticFocus.enableTracking(<id>)`` API from your consent-management platform's consent event. Use native JavaScript, since ``jQuery`` and other libraries aren't guaranteed to be available on third party sites:

.. code-block:: js

   // called by your consent-management platform once the visitor consents
   window.MauticFocus.enableTracking(123);

The copied 'Consent-managed' snippet calls this same public API inline: it invokes ``window.MauticFocus.enableTracking(<id>)`` when available, and otherwise queues the request in ``window.MauticFocusTrackingQueue`` for the display script to flush once it loads.

If the tracking layer hasn't loaded yet, ``window.MauticFocusTrackingQueue`` holds the activation request and flushes it once the layer loads.

Alternatively, set ``window.MauticFocusUseMauticTrackingConsent`` to ``true`` to let the Focus display script auto-activate tracking as soon as Mautic website tracking becomes enabled. On that path the Focus runtime activates in response to the ``mautic:tracking-enabled`` document event rather than waiting for a manual or consent-management platform call.

.. vale off

Dynamic Web Content injection behavior
**************************************

.. vale on

The Dynamic Web Content build-JS subscriber now parses Dynamic Web Content through the DOM rather than treating it as opaque markup. It injects only same-origin Focus scripts through two independent allow-rules. It always allows ``/focus/{id}/display.js`` so a Focus Item renders regardless of consent state. When ``MauticJS.trackingEnabled`` is ``true``, it additionally allows the legacy ``/focus/{id}.js`` — this injection is added on top of the always-allowed display script, not in place of it — so the combined tracking-capable script loads through Dynamic Web Content only once tracking is active.
