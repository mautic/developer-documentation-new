MVC
###

Mautic uses a **Model-View-Controller - MVC** structure to manage how users interact with the frontend - **views** and how the backend handles those interactions - **controllers and models**.

In Symfony, and thus Mautic, the **controller** is the central part of the MVC structure. The route determines which controller method executes when a user makes a request. The controller then interacts with the **model** to retrieve or manipulate data, and finally renders a **view** to display the results to the user.

Controllers
***********

Matching Routes to controller methods
=====================================

The :ref:`route defined in the config</plugins/config>` determines which controller method is called. Take this example:

.. code-block:: php

    'plugin_helloworld_admin' => [
        'path'       => '/hello/admin',
        'controller' => 'MauticPlugin\HelloWorldBundle\Controller\DefaultController:adminAction'
    ],

Thus, when a browser calls up ``/hello/admin``, ``\MauticPlugin\HelloWorldBundle\Controller\DefaultController::adminAction()`` will be called.

Route placeholders
==================

Symfony automatically passes route placeholders into the controller’s method as arguments. The method’s parameters must match the placeholder names.

Example:

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

If the route looked like this instead:

.. code-block:: php

    'plugin_helloworld_world' => [
        'path'       => '/hello/{world}',
        'controller' => 'MauticPlugin\HelloWorldBundle\Controller\DefaultController::worldAction',
        'requirements' => [
            'world' => 'earth|mars'
        ]
    ],

Then the method must be:

.. code-block:: php

   public function worldAction(string $world)

Extending Mautic’s controllers
==============================

Mautic has several controllers that provide some helper functions.

\1. CommonController - ``Mautic\CoreBundle\Controller\CommonController``
------------------------------------------------------------------------


The ``CommonController`` also provides the following helper methods:

1.1 ``delegateView($args)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mautic is AJAX-driven, so it must support both standard http and AJAX requests. The ``delegateView`` method acts as a wrapper that detects the request type and returns the appropriate response—either a full DOM for http or a partial one for AJAX.

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
     - Array of variables returned as part of the AJAX response used by Mautic and/or the Plugin’s onLoad JS callback.

Due to the use of AJAX, Mautic uses some elements of the ``passthroughVars`` array to manipulate the user interface.

For responses that include main content - for example, routes a user would click to - you should set at least ``activeLink`` and ``route``.

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
     - This pushes the route to the browser’s address bar to match AJAX response.
   * - ``mauticContent``
     - OPTIONAL
     - string
     - It generates the JS method to call after Mautic injects AJAX content into the DOM. If set as ``helloWorldDetails``, Mautic checks for and execute ``Mautic.helloWorldDetailsOnLoad()``.
   * - callback
     - OPTIONAL
     - string
     - Mautic executes a namespaced JS function before injecting the response. If set, Mautic passes the response to this function and does not process content.
   * - redirect
     - OPTIONAL
     - string
     - The URL to force a page redirect instead of injecting AJAX content.
   * - target
     - OPTIONAL
     - string
     - jQuery selector to inject the content into. Defaults to app’s main content selector.
   * - replaceContent
     - OPTIONAL
     - string
     - If set to `'true'`, Mautic replaces the target selector with AJAX content.

1.2 ``delegateRedirect($url)`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Delegates the appropriate response for redirects.

* **If AJAX request**: returns a json response with ``{redirect: $url}``.  
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
     - Array of flash messages to display after redirecting. See :doc:`Flash Messages <rest_api/assets>` for more information.
   * - ``forwardController``
     - OPTIONAL
     - bool
     - If true (default), forwards to a controller method (``BundleName:ControllerName:method``). Set to ``false`` to load a view template (``BundleName:ViewName:template.html.php``) directly.


\2. FormController - ``Mautic\CoreBundle\Controller\FormController``
====================================================================

This controller extends ``CommonController`` and provides helper methods for managing :doc:`Forms <components/forms>`.

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


\3. AjaxController - ``Mautic\CoreBundle\Controller\AjaxController``
====================================================================

This controller also extends ``CommonController`` and is a companion to some of the built-in JavaScript helpers. See *JavaScript methods* for more information.

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

Base Model Classes
==================

You can extend either of the following base classes to make use of Mautic's helper methods:

\1. AbstractCommonModel - ``\Mautic\CoreBundle\Model\AbstractCommonModel``
--------------------------------------------------------------------------

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
      - Provides access to the current user and permission checks.
    * - ``$this->dispatcher``
      - Event dispatcher
      - Dispatches and listens for Mautic events.
    * - ``$this->translator``
      - Translator service
      - Handles language translations.

\2. FormModel - ``\Mautic\CoreBundle\Model\FormModel``
------------------------------------------------------

This extends ``AbstractCommonModel`` and includes helper methods for working with entities and repositories. For more information, see the :doc:`Database <components/entities>` section.

Getting model objects
=====================

To retrieve a model object in a controller use :xref:`Symfony's autowiring`.

If using a model inside another service or model, inject the model service as a dependency instead of using the helper method.

Views
*****

Views in Mautic take data passed from the controller and display it to the user. You can render templates from within controllers or other templates.

The controller uses the ``delegateView()`` method to render views, which relies on the ``contentTemplate`` to determine which view to render.

View notation follows this format:

.. code-block:: none

    @BundleName/ViewName/template.html.twig

For example, ``@HelloWorld/Contact/form.html.twig`` points to the file ``/path/to/mautic/plugins/HelloWorldBundle/Resources/views/Contact/form.html.twig``

To use views inside subfolders under ``Resources/views``:

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

Some variables are always available and shouldn't be overridden:

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

There are a number of template helper objects and helper view templates built into Mautic.

Slots helper
============

The ``slots`` helper allows sub-templates to pass content up to parent templates. Since Mautic templates render *inside-out*, a sub-template can define slot content that the parent template can access. However, sub-templates don't have access to content defined in a parent template.

Setting slot content
--------------------

Use ``set()`` to define the content of a slot. If the slot already exists, the new content overwrites the existing one.

.. code-block:: php

    // Set a slot with content
    $view['slots']->set('name', 'the content');

Appending slot content
----------------------

Use ``append()`` to add to an existing slot rather than replacing its content. This is useful for aggregating content across templates.

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

To output the slot content, use ``output()``. This is typically used in parent templates where you want to inject content from a sub-template.

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

``slots`` are central to how Mautic handles nested views and dynamic content flow. Use them to build modular, reusable templates where the child view defines what's shown and the parent controls the layout.

Asset helper
============

The ``assets`` helper, accessed via ``$view['assets']``, is used to load assets into the DOM including images, script and stylesheets.

.. note::

   ``$view['assets']`` should always be used to ensure that assets work with Mautic installed in the web root, installed in a subdirectory, ran under the dev environment - ``index_dev.php`` - and/or ran under the prod environment.

The asset helper also provides a way to insert scripts and stylesheets into the head for AJAX loaded content using ``$view['assets']->includeScript()`` and ``$view['assets']->includeStylesheet()``.

Loading images
--------------

Use ``getUrl()`` to generate the correct relative URL to an asset like an image.

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

These methods ensure that your assets are properly handled regardless of Mautic’s installation location or environment. They also support dynamic inclusion for content loaded via AJAX.

Router helper
=============

The ``router`` helper, accessed via ``$view['router']``, is used to generate URLs to named routes within views.

.. code-block:: php

    <a href="<?php echo $view['router']->generate(
        'plugin_helloworld_world',
        array('world' => 'mars')
    ); ?>" data-toggle="ajax">Mars</a>

This generates a link to the route ``plugin_helloworld_world`` with the dynamic parameter ``world`` set to ``mars``.

For more details on defining and using routes, see :doc:`Router </plugins/config>`.

Translation helper
==================

The ``translator`` helper, accessed via ``$view['translator']``, is used to translate strings within views using Mautic's translation system.

.. code-block:: php

    <h1>
        <?php echo $view['translator']->trans(
            'plugin.helloworld.worlds',
            array('%world%' => 'Mars')
        ); ?>
    </h1>

This example replaces the ``%world%`` placeholder with ``Mars``, and output the translated string.

For more on how to handle translations, see :doc:`Translator </developer/translations>`.

``$view['translator']`` follows the same conventions described in the Translator documentation, allowing dynamic, localized content in templates.

Date helper
===========

The ``date`` helper, accessed via ``$view['date']``, is used to format dates according to system and/or user settings.

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

Form helper
===========

The ``form`` helper, accessed via ``$view['form']``, is used to render form objects passed from the controller.

.. code-block:: php

    <?php echo $view['form']->form($form); ?>

This helper outputs the full HTML Form using the Form object - typically a Symfony Form - passed to the view.

For detailed usage, see :doc:`Forms <components/forms>`.

AJAX integration
****************

Mautic provides several helpers and conventions for handling AJAX-driven UI features including links, modals, forms, and lifecycle callbacks.

AJAX links
==========

To enable AJAX for a link, set the attribute ``data-toggle="ajax"``.

.. code-block:: html+php

    <a href="<?php echo $view['router']->generate('plugin_helloworld_world', ['world' => 'mars']); ?>" data-toggle="ajax">
        Mars
    </a>

AJAX modals
===========

Mautic uses Bootstrap modals, but Bootstrap alone doesn't support dynamically retrieving content more than once. To address this, Mautic provides the ``data-toggle="ajaxmodal"`` attribute.

.. code-block:: html+php

    <a href="<?php echo $view['router']->generate('plugin_helloworld_world', ['world' => 'mars']); ?>"
       data-toggle="ajaxmodal"
       data-target="#MauticSharedModal"
       data-header="<?php echo $view['translator']->trans('plugin.helloworld.worlds', ['%world%' => 'Mars']); ?>">
        Mars
    </a>

* ``data-target`` should be the selector for the modal where content will be injected. Mautic provides a shared modal with the ID ``#MauticSharedModal``.
* ``data-header`` sets the modal’s title/header.

AJAX Forms
==========

When using Symfony’s Form services, Mautic automatically enables AJAX the Form. No additional configuration is necessary.

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

The system executes these callbacks when it injects or removes content via AJAX. This is useful for initializing dynamic components such as charts, inputs with autocomplete, or other JS-driven features.

To use this feature, pass the ``mauticContent`` key through the controller's ``delegateView()`` method. For example, the method ``Mautic.helloWorldDetailsOnLoad()`` calls for the following:

.. code-block:: php

    'passthroughVars' => [
        'activeLink'    => 'plugin_helloworld_world',
        'route'         => $this->generateUrl('plugin_helloworld_world', ['world' => $world]),
        'mauticContent' => 'helloWorldDetails'
    ]

Loading content triggers ``Mautic.helloWorldDetailsOnLoad()`` and ``Mautic.helloWorldDetailsOnUnload()`` when the user browses away from the page. It also gives the opportunity to destroy objects if necessary.

Both callbacks receive two arguments:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Argument
     - Description
   * - ``container``
     - The selector used as the AJAX content target.
   * - ``response``
     - The response object from the AJAX call (from ``passthroughVars``).

Page refresh support
====================

Ensure the correct ``OnLoad`` function triggers on full page refresh by setting the ``mauticContent`` slot in the view using:

.. code-block:: php

    $view['slots']->set('mauticContent', 'helloWorldDetails');
