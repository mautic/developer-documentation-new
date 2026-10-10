Model-View-Controller - MVC
###########################

Mautic uses an **MVP** structure to manage how Users interact with the frontend - **views** - and how the backend handles those interactions - **controllers and models**.

In Symfony, and thus Mautic, the **controller** is the central part of the MVC structure. The route determines which controller method executes when a User makes a request. The controller then interacts with the **model** to retrieve or manipulate data, and finally renders a **view** to display the results to the User.

Controllers
***********

Matching routes to controller methods
=====================================

.. vale off

The :ref:`route defined in the config <routing config items>` determines the controller method. Take this example:

.. vale on

.. code-block:: php

    'plugin_helloworld_admin' => [
        'path'       => '/hello/admin',
        'controller' => 'MauticPlugin\HelloWorldBundle\Controller\DefaultController:adminAction'
    ],

In the example, a browser call to ``/hello/admin`` triggers ``MauticPlugin\HelloWorldBundle\Controller\DefaultController::adminAction()``.

Route placeholders
==================

Symfony automatically passes route placeholders into the controller’s method as arguments. The method’s parameters must match the placeholder names.

For example:

.. code-block:: php

    'plugin_helloworld_world' => [
        'path'       => '/hello/{world}',
        'controller' => 'MauticPlugin\HelloWorldBundle\Controller\DefaultController::worldAction',
        'defaults'    => [
            'world' => 'earth'
        ],
        'requirements' => [
            'world' => 'earth|mars'
        ]
    ],

The matching method:

.. code-block:: php

    public function worldAction(string $world = 'earth')

.. note::

   Since the route defines a default for ``world``, the controller method must also reflect this default.

Without a defined default value, the placeholder becomes a required argument:

.. code-block:: php

    'plugin_helloworld_world' => [
        'path'       => '/hello/{world}',
        'controller' => 'MauticPlugin\HelloWorldBundle\Controller\DefaultController::worldAction',
        'requirements' => [
            'world' => 'earth|mars'
        ]
    ],

The corresponding controller method reflects this by omitting the default value:

.. code-block:: php

   public function worldAction(string $world)

Extending Mautic’s controllers
==============================

Mautic has several controllers that provide some helper functions.

.. vale off

\1. CommonController - ``Mautic\CoreBundle\Controller\CommonController``
------------------------------------------------------------------------

.. vale on

The ``CommonController`` also provides the following helper methods. Mautic declares them with PHP's ``protected`` visibility keyword, so call them through ``$this`` from your controller's actions.

1.1 ``delegateView($args)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. vale off

Mautic is AJAX-driven, so it must support both standard HTTP and AJAX requests. The ``delegateView`` method acts as a wrapper that detects the request type and returns the appropriate response—either a complete DOM for HTTP or a partial one for AJAX.

.. vale on

The ``$args`` array contains the required elements for generating either type of response.

It accepts the following parameters for ``delegateView()``:

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - Key
     - Required
     - Type
     - Description
   * - ``contentTemplate``
     - REQUIRED
     - string
     - Defines the view template to load. This should be in view notation of ``@BundleName/ViewName/template.html.twig``. Refer to :ref:`Views` for more info.
   * - ``viewParameters``
     - OPTIONAL
     - array
     - Array of variables with values made available to the template. Each key becomes a variable available to the template.
   * - ``passthroughVars``
     - OPTIONAL
     - array
     - Array of variables returned as part of the AJAX response used by Mautic and/or the Plugin’s ``onload`` JavaScript callback.

.. vale off

Because it uses AJAX, Mautic uses elements of the ``passthroughVars`` array to manipulate the user interface.

.. vale on

For responses that include main content - for example, routes a User would click to - you should set at least ``activeLink`` and ``route``.

.. vale off

.. list-table:: Common ``passthroughVars``
   :widths: 20 20 20 40
   :header-rows: 1

   * - Key
     - Required
     - Type
     - Description
   * - ``activeLink``
     - OPTIONAL
     - string
     - Sets the ID of the menu item that Mautic should activate dynamically to match the AJAX response. 
   * - route
     - OPTIONAL
     - string
     - This pushes the route to the browser’s address bar to match the AJAX response.
   * - ``mauticContent``
     - OPTIONAL
     - string
     - It generates the JavaScript method to call after Mautic injects AJAX content into the DOM. If set as ``helloWorldDetails``, Mautic checks for and executes ``Mautic.helloWorldDetailsOnLoad()``.
   * - callback
     - OPTIONAL
     - string
     - Mautic executes namespace - a JavaScript function - before injecting the response. If set, Mautic passes the response to this function and doesn't process content.
   * - redirect
     - OPTIONAL
     - string
     - The URL to force a page redirect instead of injecting AJAX content.
   * - target
     - OPTIONAL
     - string
     - jQuery selector to inject the content into. Defaults to the app’s main content selector.
   * - ``replaceContent``
     - OPTIONAL
     - string
     - If set to ``true``, Mautic replaces the target selector with AJAX content.

.. vale on

1.2 ``delegateRedirect($url)`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Delegates the appropriate response for redirects:

* **If AJAX request**: returns a JSON response with ``{redirect: $url}``.  
* **If http request**: performs a standard redirect header.

1.3 ``postActionRedirect($args)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Similar to ``delegateView()``, but used after an action like saving a Form. Accepts the same ``$args`` as ``delegateView()``, plus:

.. list-table:: Additional Parameters for ``postActionRedirect()``
   :widths: 20 20 20 40
   :header-rows: 1

   * - Key
     - Required
     - Type
     - Description
   * - ``returnUrl``
     - OPTIONAL
     - string
     - URL to redirect to. Defaults to ``/s/dashboard``. Auto-populates ``passthroughVars[route]`` if not set.
   * - flashes
     - OPTIONAL
     - array
     - Array of flash messages to display after redirecting.
   * - ``forwardController``
     - OPTIONAL
     - boolean
     - If ``true`` - **default**, forwards to a controller method - ``MauticPlugin\HelloWorldBundle\Controller\WorldController::method``. Set to ``false`` to load a view template - ``@BundleName/ViewName/template.html.twig`` - directly.

.. vale off

\2. AbstractFormController - ``Mautic\CoreBundle\Controller\AbstractFormController``
------------------------------------------------------------------------------------

.. vale on

This controller extends ``CommonController`` and adds helper methods for handling Symfony ``FormInterface`` objects, such as ``isFormCancelled()``, ``isFormApplied()``, and ``isFormValid()``, plus entity locking through ``isLocked()``. It also gives your controller the ``$this->formFactory`` service for building them.

If your controller manages an entity with the standard list, view, new, edit, clone, and delete actions, extend ``Mautic\CoreBundle\Controller\AbstractStandardFormController`` instead. It extends ``AbstractFormController`` and provides those actions through helpers such as ``indexStandard()``, ``newStandard()``, and ``editStandard()``. Your controller must implement ``getModelName()``, and can override methods such as ``getTemplateBase()``, ``getRouteBase()``, and ``getSessionBase()`` when the defaults derived from the model name don't fit.

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/Controller/DefaultController.php

    namespace MauticPlugin\HelloWorldBundle\Controller;

    use Mautic\CoreBundle\Controller\AbstractFormController;

    class DefaultController extends AbstractFormController
    {
        public function worldAction(string $world = 'earth', WorldModel $model): Response
        {
            // Retrieve details about the world
            $worldDetails = $model->getWorldDetails($world);

            return $this->delegateView(
                [
                    'viewParameters'  => [
                        'world'   => $world,
                        'details' => $worldDetails
                    ],
                    'contentTemplate' => '@HelloWorld/World/details.html.twig',
                    'passthroughVars' => [
                        'activeLink'    => 'plugin_helloworld_world',
                        'route'         => $this->generateUrl('plugin_helloworld_world', ['world' => $world]),
                        'mauticContent' => 'helloWorldDetails'
                    ]
                ]
            );
        }

        public function contactAction(ContactModel $model): Response
        {
            // Create the form object
            $form = $this->formFactory->create(ContactFormType::class);

            // Handle form submission if POST        
            if ($this->request->getMethod() == 'POST') {
                $flashes = [];

                // isFormCancelled() checks if the cancel button was clicked
                if ($cancelled = $this->isFormCancelled($form)) {

                    // isFormValid() will bind the request to the form object and validate the data
                    if ($valid = $this->isFormValid($form)) {

                        // Send the email
                        $model->sendContactEmail($form->getData());

                        // Set success flash message
                        $flashes[] = [
                            'type'    => 'notice',
                            'msg'     => 'plugin.helloworld.notice.thank_you',
                            'msgVars' => [
                                '%name%' => $form['name']->getData()
                            ]
                        ];
                    }
                }

                if ($cancelled || $valid) {
                    // Redirect to /hello/world

                    return $this->postActionRedirect(
                        [
                            'returnUrl'       => $this->generateUrl('plugin_helloworld_world'),
                            'contentTemplate' => 'MauticPlugin\HelloWorldBundle\Controller\DefaultController::worldAction',
                            'flashes'         => $flashes
                        ]
                    );
                } // Otherwise show the form again with validation error messages
            }

            // Display the form
            return $this->delegateView(
                [
                    'viewParameters'  => [
                        'form' => $form->createView()
                    ],
                    'contentTemplate' => '@HelloWorld/Contact/form.html.twig',
                    'passthroughVars' => [
                        'activeLink' => 'plugin_helloworld_contact',
                        'route'      => $this->generateUrl('plugin_helloworld_contact')
                    ]
                ]
            );
        }
    }

.. vale off

\3. AjaxController - ``Mautic\CoreBundle\Controller\AjaxController``
--------------------------------------------------------------------

.. vale on

This controller also extends ``CommonController`` and is a companion to some of the built-in JavaScript helpers.

Models
******

Models retrieve and process data between controllers and views. While not required in Plugins, Mautic provides convenient ways to access model objects and use commonly needed methods if you choose to use them.

Model example
=============

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/Model/ContactModel.php

    namespace MauticPlugin\HelloWorldBundle\Model;

    use Mautic\CoreBundle\Model\AbstractCommonModel;

    final class ContactModel extends AbstractCommonModel
    {
        /**
         * Send contact email
         */
        public function sendContactEmail(array $data): void
        {
            $mailer->message->addTo(
                $this->coreParametersHelper->get('mailer_from_email')
            );

            $this->message->setFrom(
                array($data['email'] => $data['name'])
            );

            $mailer->message->setSubject($data['subject']);

            $mailer->message->setBody($data['message']);

            $mailer->send();
        }
    }

.. _base model classes:

Base model classes
==================

You can extend either of the following base classes to make use of Mautic's helper methods:

.. vale off

\1. ``AbstractCommonModel`` - ``\Mautic\CoreBundle\Model\AbstractCommonModel``
------------------------------------------------------------------------------

.. vale on

This base class offers access to services commonly used in models:

.. list-table::
    :widths: 25 25 50
    :header-rows: 1

    * - Property
      - Service
      - Description
    * - ``$this->em``
      - Entity manager
      - Handles database interactions via Doctrine.
    * - ``$this->security``
      - Security service
      - Provides access to the current User and permission checks.
    * - ``$this->dispatcher``
      - Event dispatcher
      - Dispatches and listens for Mautic events.
    * - ``$this->translator``
      - Translator service
      - Handles language translations.

.. vale off

\2. ``FormModel`` - ``\Mautic\CoreBundle\Model\FormModel``
----------------------------------------------------------

The ``FormModel`` class extends ``AbstractCommonModel`` and includes helper methods for working with entities and repositories. For more information, refer to the :doc:`/plugins/data` section.

.. vale on

Mautic 8 type changes
---------------------

Mautic 8 adds native PHP parameter types to these public methods on the base ``FormModel`` class:

.. code:: diff

   - public function saveEntity($entity, bool $unlock = true): void
   + public function saveEntity(object $entity, bool $unlock = true): void

   - public function saveAndDetachEntity($entity, bool $unlock = true): void
   + public function saveAndDetachEntity(object $entity, bool $unlock = true): void

   - public function lockEntity($entity): void
   + public function lockEntity(object $entity): void

   - public function isLocked($entity): bool
   + public function isLocked(object $entity): bool

   - public function isNewEntity($entity): bool
   + public function isNewEntity(object $entity): bool

   - public function togglePublishStatus($entity): bool
   + public function togglePublishStatus(object $entity): bool

   - public function deleteEntity($entity): void
   + public function deleteEntity(object $entity): void

   - public function deleteEntities($ids): array
   + public function deleteEntities(array $ids): array

This changes no runtime behavior. In practice these methods already worked with objects and arrays. Most declared the type in their ``@param`` annotations, and several guard entity access with ``method_exists()``, so Mautic 8 mainly makes the existing expectation explicit in the signatures.

The upgrade risk is a signature mismatch. If your Plugin's Model subclass overrides one of these methods with a parameter type that's narrower than or incompatible with the new parent type, PHP throws a fatal ``TypeError``. For example, an override that declares a concrete entity class instead of ``object``, or another type instead of ``array``, is incompatible. An override that declares no parameter type stays compatible. To fix an incompatible override, match the parent signature exactly with ``object $entity`` or ``array $ids``, or remove the parameter type.

Mautic types the entity parameter as ``object`` rather than a concrete entity class on purpose, because PHP fails with a fatal error when an inherited signature narrows a parameter type. The method-specific ``@param <Entity>`` annotations stay in place for that specificity.

The core ``saveEntity()`` overrides adopt the ``object`` type in Mautic 8 for the same reason - for example ``AssetModel``, ``EmailModel``, ``LeadModel``, ``PageModel``, and ``UserModel``. If your Plugin extends ``EmailModel`` or ``LeadModel`` rather than ``FormModel`` directly, apply the same rule to your override. ``AssetModel``, ``PageModel``, and ``UserModel`` are ``final`` in Mautic 8, so a Plugin can't extend them. See :ref:`Final classes <Mautic 8 final classes>`.

Mautic 8 also types one public method on the parent ``AbstractCommonModel`` class, which ``FormModel`` and Plugin Models both extend: ``encodeArrayForUrl($array)`` becomes ``encodeArrayForUrl(array $array)``. The same override-compatibility rule applies.

Registering a model
===================

To make a custom model resolvable through ``getModel('yourbundle.yourmodel')`` from a controller, the model class declares a static ``getName()`` method that returns that key string. The model must also implement ``Mautic\CoreBundle\Model\MauticModelInterface``. Extending one of the base classes in :ref:`Base model classes <base model classes>` satisfies that interface requirement, but not the registration. You still declare ``getName()`` on the model to make it resolvable by key. Declaring ``getName()`` only matters for this key-based lookup - a model you always inject or type-hint by its concrete class, as described in :ref:`Getting model objects <getting model objects>`, doesn't need it.

Add the method to a model class that extends ``AbstractCommonModel`` or ``FormModel``. For example, a ``ContactModel`` built on one of those base classes returns ``'helloworld.contact'``:

.. code-block:: php

    public static function getName(): string
    {
        return 'helloworld.contact';
    }

Mautic core follows the same pattern - its ``LeadModel`` returns ``'lead.lead'``.

Declaring ``getName()`` is the whole registration step. There's no separate tag, service alias, or compiler-pass step to add. If a model omits ``getName()``, ``getModel()`` can't resolve it by key.

.. note::

   ``getName()``-based resolution is the Mautic 8 mechanism. It replaces the removed ``mautic.model`` auto-tag, the manual ``mautic.<bundle>.model.<name>`` service-alias convention, and the ``ModelPass`` compiler pass.

``getModel()`` accepts only the ``getName()`` key, not a fully qualified class name. Fetching a model by its class means injecting or type-hinting the concrete class instead, as described in :ref:`Getting model objects <getting model objects>`.

.. _getting model objects:

Getting model objects
=====================

To retrieve a model object in a controller use Symfony's :xref:`fetching services`.

If using a model inside another service or model, inject the model service as a dependency instead of using the helper method.

Views
*****

Views in Mautic take data passed from the controller and display it to the User. You can render templates from within controllers or other templates.

The controller uses the ``delegateView()`` method to render views, which relies on the ``contentTemplate`` to determine which view to render.

The format for view notation is as follows:

.. code-block:: none

    @BundleName/ViewName/template.html.twig

.. vale off

For example, ``@HelloWorld/Contact/form.html.twig`` points to the file ``/path/to/mautic/plugins/HelloWorldBundle/Resources/views/Contact/form.html.twig``.

.. vale on

To use views inside sub-folders under ``Resources/views``:

.. code-block:: none

    @BundleName/ViewName/Subfolder/template.html.twig

View parameters
===============

The array passed as ``viewParameters`` in the controller’s ``delegateView()`` method becomes available as variables in the view.

For example, if the controller passes:

.. code-block:: php

    'viewParameters' => [
        'world' => 'mars'
    ],

Then the variable ``$world`` becomes available in the template with the value ``mars``.

Avoid overriding this reserved variable, as Twig provides it by default:

* ``app`` is Symfony's global Twig variable, providing access to the request and session objects, for example ``app.request`` and ``app.session``.

Extending views
===============

Please refer to the ``extends`` tag section in :xref:`Twig documentation` to learn how to extend views.

Rendering views within views
============================

You can render one view inside another with Twig's ``include`` function:

.. code-block:: twig

    {{ include('@BundleName/ViewName/template.html.twig', {'parameter': 'value'}) }}

Template helpers
****************

There are several template helper objects and helper view templates built into Mautic.

.. note::

   Mautic's templates are Twig, not the old PHP templating engine. There's no ``$view`` array in a Twig template. Use the functions, filters, and tags below instead. See :xref:`Mautic migrating PHP templates to Twig<Migrating PHP templates to Twig>` for the full set of equivalents.

Replacing the ``slots`` helper with Twig blocks
===============================================

Twig's own ``block`` tag replaces the old ``slots`` helper. Since Mautic templates render **inside-out**, a sub-template defines a named block that the parent template reads back with the ``block()`` function. A child template that extends a parent can still read content the parent defined by calling ``{{ parent() }}`` inside its own block of the same name.

Setting block content
----------------------

Define the block's content with Twig's ``block`` tag. If the parent template defines the same block, the child's content overrides it.

.. code-block:: twig

    {% block name %}the content{% endblock %}

Appending to block content
---------------------------

Call ``{{ parent() }}`` inside the overriding block to keep the parent's content and add to it.

.. code-block:: twig

    {% block name %}{{ parent() }} and more content{% endblock %}

Retrieving block content
-------------------------

Use the ``block()`` function to render a named block's content from elsewhere in the same template, for example when a base layout pulls content from the child template that extends it.

.. code-block:: twig

    {{ block('name') }}

Checking block existence
-------------------------

Use ``block('name') is defined`` to confirm a block exists before rendering it, for example to fall back to a default.

.. code-block:: twig

    {{ block('name') is defined ? block('name') : 'default value' }}

Blocks are central to how Mautic handles nested views. Use them to build modular, reusable templates where the child view defines what's shown and the parent controls the layout.

The ``assets`` function
=========================

Use Symfony's standard ``asset()`` Twig function to generate the correct relative URL to an Asset, such as an image, so it resolves correctly whether you install Mautic in the web root or a subdirectory.

Loading images
--------------

.. code-block:: twig

    <img src="{{ asset('plugins/HelloWorldBundle/assets/images/earth.png') }}" />

.. note::

   Flagged for human review: confirm the current Twig equivalent, if any, for dynamically injecting a script or style sheet into AJAX-loaded content - the old ``$view['assets']->includeScript()`` / ``includeStylesheet()`` calls no longer exist.

The ``path()`` and ``url()`` functions
========================================

Symfony's standard ``path()`` and ``url()`` Twig functions generate URLs for named routes within views, replacing the old ``router`` helper.

.. code-block:: twig

    <a href="{{ path('plugin_helloworld_world', {'world': 'mars'}) }}" data-toggle="ajax">Mars</a>

This generates a link to the route ``plugin_helloworld_world`` with the dynamic parameter ``world`` set to ``mars``.

The ``trans`` filter
======================

Twig's standard ``trans`` filter translates strings within views using Mautic's translation system, replacing the old ``translator`` helper.

.. code-block:: twig

    <h1>{{ 'plugin.helloworld.worlds'|trans({'%world%': 'Mars'}) }}</h1>

This example replaces the ``%world%`` placeholder with ``Mars``, and outputs the translated string.

.. vale off

For more on how to handle translations, see :doc:`Translator </components/translators>`.

.. vale on

The ``trans`` filter follows the same conventions described in the :doc:`Translator documentation </components/translators>`, allowing dynamic, localized content in templates.

The ``date`` functions
========================

Mautic registers Twig functions that format dates according to system and User settings, replacing the old ``date`` helper.

.. code-block:: twig

    {# Format using full date-time format from system settings #}
    {{ dateToFull(datetime) }}

    {# Format using short date-time format #}
    {{ dateToShort(datetime) }}

    {# Format using date-only format #}
    {{ dateToDate(datetime) }}

    {# Format using time-only format #}
    {{ dateToTime(datetime) }}

    {# Combine date-only and time-only formats #}
    {{ dateToFullConcat(datetime) }}

    {# Format as relative time: 'Yesterday, 8:02 pm' or 'x days ago' #}
    {{ dateToText(datetime) }}

    {# Format a date string in a different timezone #}
    {{ dateToFull(datetime, 'UTC') }}

The first argument to each function can be a ``\DateTime`` object or a string formatted as ``Y-m-d H:i:s``. If the date isn't already in local time, pass the timezone as the second argument and the source format as the third.

The ``form`` functions
========================

Twig's standard ``form_start()``, ``form_row()``, and ``form_end()`` functions render a Symfony Form object passed from the controller, replacing the old ``form`` helper.

.. code-block:: twig

    {{ form_start(form) }}
    {{ form_row(form.email) }}
    {{ form_end(form) }}

AJAX Integration
****************

Mautic provides several helpers and conventions for handling AJAX-driven UI features, including links, modals, Forms, and lifecycle callbacks.

AJAX links
==========

To enable AJAX for a link, set the attribute ``data-toggle="ajax"``.

.. vale off

.. code-block:: twig

    <a href="{{ path('plugin_helloworld_world', {'world': 'mars'}) }}" data-toggle="ajax">
        Mars
    </a>

.. vale on

AJAX modals
===========

Mautic uses Bootstrap modals, but Bootstrap alone doesn't support dynamically retrieving content more than once. To address this, Mautic provides the ``data-toggle="ajaxmodal"`` attribute.

.. vale off

.. code-block:: twig

    <a href="{{ path('plugin_helloworld_world', {'world': 'mars'}) }}"
       data-toggle="ajaxmodal"
       data-target="#MauticSharedModal"
       data-header="{{ 'plugin.helloworld.worlds'|trans({'%world%': 'Mars'}) }}">
        Mars
    </a>

.. vale on

* ``data-target`` defines the selector for the modal that receives injected content. Mautic provides a shared modal with the ID ``#MauticSharedModal``.
* ``data-header`` sets the modal’s title or header.

.. vale off

AJAX Forms
==========

.. vale on

When using Symfony’s Form services, Mautic automatically enables AJAX for the Form. No additional configuration is necessary.

AJAX content callbacks
======================

Mautic allows you to hook into the lifecycle of AJAX content injection via JavaScript callbacks.

.. code-block:: javascript

    Mautic.helloWorldDetailsOnLoad = function(container, response) {
        // Manipulate content after load
    };

    Mautic.helloWorldDetailsOnUnload = function(container, response) {
        // Clean up or remove bindings before unloading
    };

The system executes these callbacks when it injects or removes content via AJAX. This is useful for initializing dynamic Components such as charts, autocomplete inputs, or other JavaScript-driven features.

To use this feature, pass the ``mauticContent`` key through the controller's ``delegateView()`` method. For example, the method ``Mautic.helloWorldDetailsOnLoad()`` calls for the following:

.. code-block:: php

    'passthroughVars' => [
        'activeLink'    => 'plugin_helloworld_world',
        'route'         => $this->generateUrl('plugin_helloworld_world', ['world' => $world]),
        'mauticContent' => 'helloWorldDetails'
    ]

.. vale off

Loading content triggers ``Mautic.helloWorldDetailsOnLoad()`` and ``Mautic.helloWorldDetailsOnUnload()`` when the User browses away from the page. It also allows destroying objects if necessary.

.. vale on

Both callbacks receive two arguments:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Argument
     - Description
   * - ``container``
     - The selector used as the AJAX content target.
   * - ``response``
     - The response object from the AJAX call - ``passthroughVars``.

.. vale off

Page refresh support
====================

.. vale on

.. vale off

Ensure the correct ``onload`` function triggers on full page refresh by setting the ``mauticContent`` block in the view:

.. vale on

.. code-block:: twig

    {% block mauticContent %}helloWorldDetails{% endblock %}
