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

The ``CommonController`` also provides the following helper methods:

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
     - Defines the view template to load. This should be in view notation of ``BundleName:ViewName:template.html.php``. Refer to :ref:`Views` for more info.
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
     - If ``true`` - **default**, forwards to a controller method - ``BundleName:ControllerName:method``. Set to ``false`` to load a view template - ``BundleName:ViewName:template.html.php`` - directly.

.. vale off

\2. FormController - ``Mautic\CoreBundle\Controller\FormController``
====================================================================

This controller extends ``CommonController`` and provides helper methods for managing Forms.

.. vale on

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/Controller/DefaultController.php

    namespace MauticPlugin\HelloWorldBundle\Controller;

    use Mautic\CoreBundle\Controller\FormController;

    class DefaultController extends FormController
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
                    'contentTemplate' => 'HelloWorldBundle:World:details.html.php',
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
                            'contentTemplate' => 'MauticPlugin\HelloWorldBundle\Controller\DefaultController:worldAction',
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
                    ),
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
====================================================================

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

    use Mautic\CoreBundle\Model\CommonModel;

    final class ContactModel extends CommonModel
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

Avoid overriding these reserved variables, as Mautic provides them by default:

* ``$view``: contains helper objects for extending or rendering templates.
* ``$app``: provides access to request and session objects via ``$app->getRequest()`` and ``$app->getSession()``.

Extending views
===============

Please refer to the ``extends`` tag section in :xref:`Twig documentation` to learn how to extend views.

Rendering views within views
============================

You can render one view inside another:

.. code-block:: php

    echo $view->render('BundleName:ViewName:template.html.php', array('parameter' => 'value'));

Template helpers
****************

There are several template helper objects and helper view templates built into Mautic.

The ``slots`` helper
====================

The ``slots`` helper allows sub-templates to pass content up to parent templates. Since Mautic templates render **inside-out**, a sub-template can define slot content that the parent template can access. However, sub-templates don't have access to content defined in a parent template.

Setting slot content
--------------------

Use ``set()`` to define the content of a slot. If the slot already exists, the new content overwrites the existing one.

.. code-block:: php

    // Set a slot with content
    $view['slots']->set('name', 'the content');

Appending slot content
----------------------

Use ``append()`` to add to an existing ``slot`` rather than replacing its content. This is useful for aggregating content across templates.

.. code-block:: php

    // Append string content
    $view['slots']->append('name', ' and more content');

    // Append array content
    $view['slots']->append('existingArray', array(
        'append' => 'me'
    ));

Retrieving slot content
-----------------------

To get the content of a slot, use ``get()``. If the slot doesn't exist, you can define a default value.

.. code-block:: php

    // Retrieve slot content or fallback to default
    $content = $view['slots']->get('name', 'default value');

Outputting slot content
-----------------------

The ``output()`` method renders slot content. It allows parent templates to pull in and display content from sub-templates.

.. code-block:: php

    // Render the slot content; no echo required
    $view['slots']->output('name');

Checking slot existence
-----------------------

You can confirm if a slot exists using ``has()`` before performing actions on it.

.. code-block:: php

    // Check if a slot is defined
    if ($view['slots']->has('name')) {
        // Perform some action
    }

The ``slots`` are central to how Mautic handles nested views and Dynamic Content flow. Use them to build modular, reusable templates where the child view defines what's shown and the parent controls the layout.

The ``assets`` helper
=====================

The ``assets`` helper - accessed via ``$view['assets']`` - loads various Assets into the DOM, such as images, scripts, and stylesheets.

.. note::

   Use ``$view['assets']`` to ensure your Assets work across environments. This allows Assets to load correctly whether you install Mautic in the web root or a subdirectory, and whether you run it in development - ``index_dev.php`` - or production environments.

The ``assets`` helper also provides a way to insert scripts and stylesheets into the head for AJAX-loaded content using ``$view['assets']->includeScript()`` and ``$view['assets']->includeStylesheet()``.

Loading images
--------------

Use ``getUrl()`` to generate the correct relative URL to an Asset, such as an image.

.. code-block:: php

    // Generate relative URL to image
    echo '<img src="' . $view['assets']->getUrl('plugins/HelloWorldBundle/assets/images/earth.png') . '" />';

Inserting JavaScript
--------------------

Use ``includeScript()`` to dynamically insert a JavaScript file into the head. This is especially useful for AJAX-loaded views where scripts need to be re-injected.

.. code-block:: php

    // Dynamically insert script into head
    echo $view['assets']->includeScript('plugins/HelloWorldBundle/assets/helloworld.js');

Inserting stylesheets
---------------------

Use ``includeStylesheet()`` to dynamically include a CSS file into the head.

.. code-block:: php

    // Dynamically insert stylesheet into head
    echo $view['assets']->includeStylesheet('plugins/HelloWorldBundle/assets/helloworld.css');

These methods enable you to handle your Assets properly, regardless of Mautic’s installation location or environment. They also support dynamic inclusion for content loaded via AJAX.

The ``router`` helper
=====================

The ``router`` helper - accessed via ``$view['router']`` - generates URLs for named routes within views.

.. code-block:: php

    <a href="<?php echo $view['router']->generate(
        'plugin_helloworld_world',
        array('world' => 'mars')
    ); ?>" data-toggle="ajax">Mars</a>

This generates a link to the route ``plugin_helloworld_world`` with the dynamic parameter ``world`` set to ``mars``.

The ``translator`` helper
=========================

The ``translator`` helper, accessed via ``$view['translator']``, is used to translate strings within views using Mautic's translation system.

.. code-block:: php

    <h1>
        <?php echo $view['translator']->trans(
            'plugin.helloworld.worlds',
            array('%world%' => 'Mars')
        ); ?>
    </h1>

This example replaces the ``%world%`` placeholder with ``Mars``, and outputs the translated string.

.. vale off

For more on how to handle translations, see :doc:`Translator </components/translators>`.

.. vale on

The ``$view['translator']`` follows the same conventions described in the :doc:`Translator documentation </components/translators>`, allowing dynamic, localized content in templates.

The ``date`` helper
===================

The ``date`` helper - accessed via ``$view['date']`` - formats dates according to system and User settings.

.. code-block:: php

    // Can be a string or \DateTime object. If a string, it's assumed to be in local time
    $datetime = '2015-04-12 20:56:00';

    // Format using full date-time format from system settings
    $fullDateTime = $view['date']->toFull($datetime);

    // Format using short date-time format
    $shortDateTime = $view['date']->toShort($datetime);

    // Format using date-only format
    $date = $view['date']->toDate($datetime);

    // Format using time-only format
    $time = $view['date']->toTime($datetime);

    // Combine date-only and time-only formats
    $datetime = $view['date']->toFullConcat($datetime);

    // Format as relative time: 'Yesterday, 8:02 pm' or 'x days ago'
    $text = $view['date']->toText($datetime);

    // Format a date string in a different timezone
    $fullDateTime = $view['date']->toFull($datetime, 'Y-m-d H:i:s', 'UTC');

The first argument to each method can be a ``\DateTime`` object or a string formatted as ``Y-m-d H:i:s``. If the date is not already in local time, pass the expected format as the second argument and the timezone as the third.

The ``form`` helper
===================

The ``form`` helper, accessed via ``$view['form']``, is used to render Form objects passed from the controller.

.. code-block:: php

    <?php echo $view['form']->form($form); ?>

This helper outputs the complete HTML Form using the Form object - typically a Symfony Form - passed to the view.

AJAX Integration
****************

Mautic provides several helpers and conventions for handling AJAX-driven UI features, including links, modals, Forms, and lifecycle callbacks.

AJAX links
==========

To enable AJAX for a link, set the attribute ``data-toggle="ajax"``.

.. vale off

.. code-block:: html+php

    <a href="<?php echo $view['router']->generate('plugin_helloworld_world', ['world' => 'mars']); ?>" data-toggle="ajax">
        Mars
    </a>

.. vale on

AJAX modals
===========

Mautic uses Bootstrap modals, but Bootstrap alone doesn't support dynamically retrieving content more than once. To address this, Mautic provides the ``data-toggle="ajaxmodal"`` attribute.

.. vale off

.. code-block:: html+php

    <a href="<?php echo $view['router']->generate('plugin_helloworld_world', ['world' => 'mars']); ?>"
       data-toggle="ajaxmodal"
       data-target="#MauticSharedModal"
       data-header="<?php echo $view['translator']->trans('plugin.helloworld.worlds', ['%world%' => 'Mars']); ?>">
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

Ensure the correct ``onload`` function triggers on full page refresh by setting the ``mauticContent`` slot in the view using:

.. vale on

.. code-block:: php

    $view['slots']->set('mauticContent', 'helloWorldDetails');
