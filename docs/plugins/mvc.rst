MVC
###

Mautic uses a **Model-View-Controller (MVC)** structure to manage how users interact with the frontend (**views**) and how those interactions are handled by the backend (**controllers and models**). Additionally, **Entity** and **Repository** classes are used to manage interactions with the database.

In Symfony — and therefore in Mautic — the **controller** is the central part of the MVC structure. When a user makes a request, the route determines which controller method is executed. The controller then interacts with the **model** to retrieve or manipulate data, and finally renders a **view** to display the results to the user.

Controllers
===========
Matching Routes to controller methods
-------------------------------------

The controller method called is determined by the route defined in the config. Take this example:

.. code-block:: php

    'plugin_helloworld_admin' => array(
        'path'       => '/hello/admin',
        'controller' => 'HelloWorldBundle:Default:admin'
    ),

The controller is noted as ``HelloWorldBundle:Default:admin``. Broken down, that translates to:

- ``HelloWorldBundle`` → ``\MauticPlugin\HelloWorldBundle\Controller``
- ``Default`` → ``DefaultController``
- ``admin`` → ``adminAction()``

Controller notation follows the format: ::

    BundleName:ControllerName:controllerMethod

To use a controller within a subfolder of ``Controller``, use this format: ::

    BundleName:Subdirectory\ControllerName:controllerMethod

Thus, when a browser calls up ``/hello/admin``, ``\MauticPlugin\HelloWorldBundle\Controller\DefaultController::adminAction()`` will be called.

Route placeholders
------------------

Symfony automatically passes route placeholders into the controller’s method as arguments. The method’s parameters must match the placeholder names.

Example:

.. code-block:: php

    'plugin_helloworld_world' => array(
        'path'       => '/hello/{world}',
        'controller' => 'HelloWorldBundle:Default:world',
        'defaults'    => array(
            'world' => 'earth'
        ),
        'requirements' => array(
            'world' => 'earth|mars'
        )
    ),

The matching method:

.. code-block:: php

    public function worldAction($world = 'earth')

Notice: Since the route defines a default for ``world``, the controller method must also reflect this default.

If the route looked like this instead:

.. code-block:: php

    'plugin_helloworld_world' => array(
        'path'       => '/hello/{world}',
        'controller' => 'HelloWorldBundle:Default:world',
        'requirements' => array(
            'world' => 'earth|mars'
        )
    ),

Then the method must be:

.. code-block:: php

    public function worldAction($world)

Extending Mautic’s Controllers
------------------------------

Mautic has several controllers that provide some helper functions.

``Mautic\CoreBundle\Controller\CommonController``
-------------------------------------------------

Controllers extending this will make ``MauticFactory`` available via ``$this->factory`` and ``Request`` via ``$this->request``.

It also provides the following helper methods:

**delegateView($args)**  
Mautic is ajax driven and thus must support both http requests and ajax requests for content.  
``delegateView`` is a wrapper method that determines if the request is for ajax content or the full DOM, then generates and returns the appropriate response.

The ``$args`` argument is an array with the required elements for generating the view, ajax or http.  
It will accept the following parameters:

.. list-table:: Parameters for ``delegateView()``
   :widths: 20 10 10 60
   :header-rows: 1

   * - Key
     - Required
     - Type
     - Description
   * - contentTemplate
     - REQUIRED
     - string
     - Defines the view template to load. This should be in view notation of ``BundleName:ViewName:template.html.php``. Refer to views for more info.
   * - viewParameters
     - OPTIONAL
     - array
     - Array of variables with values made available to the template. Each key will be a variable available to the template.
   * - passthroughVars
     - OPTIONAL
     - array
     - Array of variables returned as part of the ajax response used by Mautic and/or the plugin’s onLoad JS callback.

Due to the use of ajax, there are some elements of the ``passthroughVars`` array that Mautic will use internally to manipulate the user interface.  
For responses that include main content (i.e., routes a user would click to), you should set at least ``activeLink`` and ``route``.

.. list-table:: Common passthroughVars
   :widths: 20 10 10 60
   :header-rows: 1

   * - Key
     - Required
     - Type
     - Description
   * - activeLink
     - OPTIONAL
     - string
     - The ID of the menu item that should be activated dynamically to match ajax response.
   * - route
     - OPTIONAL
     - string
     - The route that should be pushed to the browser’s address bar to match ajax response.
   * - mauticContent
     - OPTIONAL
     - string
     - Used to generate the JS method to call after ajax content is injected into the DOM. If set as ``helloWorldDetails``, Mautic will check for and execute ``Mautic.helloWorldDetailsOnLoad()``.
   * - callback
     - OPTIONAL
     - string
     - A Mautic namespaced JS function executed before response is injected. If set, Mautic passes the response to this function and does not process content.
   * - redirect
     - OPTIONAL
     - string
     - The URL to force a page redirect instead of injecting ajax content.
   * - target
     - OPTIONAL
     - string
     - jQuery selector to inject the content into. Defaults to app’s main content selector.
   * - replaceContent
     - OPTIONAL
     - string
     - If set to `'true'`, Mautic will replace the target selector with ajax content.

**delegateRedirect($url)**  
Delegates the appropriate response for redirects.  
If ajax request: returns a json response with ``{redirect: $url}``.  
If http request: performs a standard redirect header.

**postActionRedirect($args)**  
Similar to ``delegateView()``, but used after an action like saving a form.  
Accepts the same ``$args`` as ``delegateView()``, plus:

.. list-table:: Additional Parameters for ``postActionRedirect()``
   :widths: 20 10 10 60
   :header-rows: 1

   * - Key
     - Required
     - Type
     - Description
   * - returnUrl
     - OPTIONAL
     - string
     - URL to redirect to. Defaults to ``/s/dashboard``. Auto-populates ``passthroughVars[route]`` if not set.
   * - flashes
     - OPTIONAL
     - array
     - Array of flash messages to display after redirecting.
   * - forwardController
     - OPTIONAL
     - bool
     - If true (default), forwards to a controller method. If false, directly loads a view template.


FormController
--------------

Extends ``CommonController``.

``Mautic\CoreBundle\Controller\FormController``. This controller extends ``CommonController`` and provides helper methods for managing forms :doc:`Forms <components/forms>`.

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/Controller/DefaultController.php

    namespace MauticPlugin\HelloWorldBundle\Controller;

    use Mautic\CoreBundle\Controller\FormController;

    class DefaultController extends FormController
    {
        /**
         * Display the world view
         *
         * @param string $world
         *
         * @return JsonResponse|\Symfony\Component\HttpFoundation\Response
         */
        public function worldAction($world = 'earth')
        {
            /** @var \MauticPlugin\HelloWorldBundle\Model\WorldModel $model */
            $model = $this->getModel('helloworld.world');

            // Retrieve details about the world
            $worldDetails = $model->getWorldDetails($world);

            return $this->delegateView(
                array(
                    'viewParameters'  => array(
                        'world'   => $world,
                        'details' => $worldDetails
                    ),
                    'contentTemplate' => 'HelloWorldBundle:World:details.html.php',
                    'passthroughVars' => array(
                        'activeLink'    => 'plugin_helloworld_world',
                        'route'         => $this->generateUrl('plugin_helloworld_world', array('world' => $world)),
                        'mauticContent' => 'helloWorldDetails'
                    )
                )
            );
        }

        /**
         * Contact form
         *
         * @return JsonResponse|\Symfony\Component\HttpFoundation\Response
         */
        public function contactAction()
        {
            // Create the form object
            $form = $this->get('form.factory')->create('helloworld_contact');

            // Handle form submission if POST        
            if ($this->request->getMethod() == 'POST') {
                $flashes = array();

                // isFormCancelled() checks if the cancel button was clicked
                if ($cancelled = $this->isFormCancelled($form)) {

                    // isFormValid() will bind the request to the form object and validate the data
                    if ($valid = $this->isFormValid($form)) {

                        /** @var \MauticPlugin\HelloWorldBundle\Model\ContactModel $model */
                        $model = $this->getModel('helloworld.contact');

                        // Send the email
                        $model->sendContactEmail($form->getData());

                        // Set success flash message
                        $flashes[] = array(
                            'type'    => 'notice',
                            'msg'     => 'plugin.helloworld.notice.thank_you',
                            'msgVars' => array(
                                '%name%' => $form['name']->getData()
                            )
                        );
                    }
                }

                if ($cancelled || $valid) {
                    // Redirect to /hello/world

                    return $this->postActionRedirect(
                        array(
                            'returnUrl'       => $this->generateUrl('plugin_helloworld_world'),
                            'contentTemplate' => 'HelloWorldBundle:Default:world',
                            'flashes'         => $flashes
                        )
                    );
                } // Otherwise show the form again with validation error messages
            }

            // Display the form
            return $this->delegateView(
                array(
                    'viewParameters'  => array(
                        'form' => $form->createView()
                    ),
                    'contentTemplate' => 'HelloWorldBundle:Contact:form.html.php',
                    'passthroughVars' => array(
                        'activeLink' => 'plugin_helloworld_contact',
                        'route'      => $this->generateUrl('plugin_helloworld_contact')
                    )
                )
            );
        }
    }


AjaxController
--------------

``Mautic\CoreBundle\Controller\AjaxController``. This controller also extends ``CommonController`` and is a companion to some of the built-in Javascript helpers. See *Javascript methods* for more information.

Models
======

Models are used to retrieve and process data between controllers and views. While not required in plugins, Mautic provides convenient ways to access model objects and use commonly needed methods if you choose to use them.

Model Example
-------------

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/Model/ContactModel.php

    namespace MauticPlugin\HelloWorldBundle\Model;

    use Mautic\CoreBundle\Model\CommonModel;

    class ContactModel extends CommonModel
    {
        /**
         * Send contact email
         * 
         * @param array $data
         */
        public function sendContactEmail($data)
        {
            // Get mailer helper - pass the mautic.helper.mailer service as a dependency
            $mailer = $this->mailer;

            $mailer->message->addTo(
                $this->factory->getParameter('mailer_from_email')
            );

            $this->message->setFrom(
                array($data['email'] => $data['name'])
            );

            $mailer->message->setSubject($data['subject']);

            $mailer->message->setBody($data['message']);

            $mailer->send();
        }
    }

Registering Model Classes
-------------------------

Models should be registered as model services. The service name must follow the format:

``mautic.UNIQUE_BUNDLE_IDENTIFIER.model.MODEL_IDENTIFIER``

- ``UNIQUE_BUNDLE_IDENTIFIER``: Any unique name for your plugin or bundle
- ``MODEL_IDENTIFIER``: A name unique within the bundle

For example, the model shown above could be registered as:

``mautic.helloworld.model.contact``

This allows Mautic’s helper functions to retrieve the model using the `getModel()` method.

Base Model Classes
------------------

You can extend either of the following base classes to make use of Mautic's helper methods:

**\Mautic\CoreBundle\Model\AbstractCommonModel**

This base class offers access to services commonly used in models:

.. list-table::
    :header-rows: 1

    * - Property
      - Service
      - Description
    * - ``$this->factory``
      - Factory service
      - Provides access to other Mautic services. *Deprecated as of Mautic 2.0*; use dependency injection instead.
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


**\Mautic\CoreBundle\Model\FormModel**

This extends ``AbstractCommonModel`` and includes helper methods for working with entities and repositories. For more information, see the :doc:`Database <components/entities>` section.

Getting Model Objects
---------------------

To retrieve a model object in a controller:

.. code-block:: php

    <?php

    /** @var \Mautic\LeadBundle\Model\LeadModel $leadModel */
    $leadModel = $this->getModel('lead'); // Shortcut for lead.lead

    /** @var \Mautic\LeadBundle\Model\ListModel $leadListModel */
    $leadListModel = $this->getModel('lead.list');

    /** @var \MauticPlugin\HelloWorldBundle\Model\ContactModel $contactModel */
    $contactModel = $this->getModel('helloworld.contact');

If using a model inside another service or model, inject the model service as a dependency instead of using the helper method.

Views
=====

Views in Mautic take data passed from the Controller and display it to the user. Templates can be rendered from within controllers or other templates.

Example Template Files
----------------------

**`details.html.php`**

.. code-block:: php

    // plugins/HelloWorldBundle/Views/World/details.html.php

    if (!$app->getRequest()->isXmlHttpRequest()) {
        $view['slots']->set('tmpl', 'Details');
        $view->extend('HelloWorldBundle:World:index.html.php');
    }
    
    <div>
        <!-- Desired content/markup -->
    </div>

**`index.html.php`**

.. code-block:: php

    // plugins/HelloWorldBundle/Views/World/index.html.php

    $view->extend('MauticCoreBundle:Default:content.html.php');

    $tmpl = $view['slots']->get('tmpl', 'Details');

    $view['slots']->set('mauticContent', 'helloWorld' . $tmpl);

    $header = ($tmpl == 'World')
        ? $view['translator']->trans(
            'plugin.helloworld.worlds',
            array('%world%' => ucfirst($world))
        ) : $view['translator']->trans('plugin.helloworld.manage_worlds');
    $view['slots']->set('headerTitle', $header);
    
    <div class="helloworld-content">
        <?php $view['slots']->output('_content'); ?>
    </div>

View Notation
-------------

View templates follow this format:

.. code-block:: text

    BundleName:ViewName:template.html.php

Nested views can be referenced using backslashes:

.. code-block:: text

    BundleName:ViewName\Subfolder:template.html.php

Rendering Views
---------------

Use the Controller’s ``delegateView()`` method with the ``contentTemplate`` key to render a view. Variables passed in ``viewParameters`` become available in the template:

.. code-block:: php

    'viewParameters' => array(
        'world' => 'mars'
    )

This allows ``$world`` to be used in the view.

Available View Variables
------------------------

- **$view** — Provides access to template helpers and rendering functions.
- **$app** — Provides access to the request and session.

Extending Views
---------------

To extend Mautic’s base templates:

.. code-block:: php

    $view->extend('MauticCoreBundle:Default:content.html.php');

For slim templates (no menu or header):

.. code-block:: php

    $view->extend('MauticCoreBundle:Default:slim.html.php');

For Ajax requests, use:

.. code-block:: php

    $app->getRequest()->isXmlHttpRequest()

Templates render inside-out. So:

1. `details.html.php` is rendered first.
2. Injected into `index.html.php`.
3. Finally into `content.html.php`.

Use ``$view['slots']->output('_content');`` to include sub-template content.

Rendering Views Within Views
----------------------------

You can render one view inside another:

.. code-block:: php

    echo $view->render('BundleName:ViewName:template.html.php', array('parameter' => 'value'));

Template Helpers
================

Slots Helper
------------

.. code-block:: php

    $view['slots']->set('name', 'content');
    $view['slots']->append('name', ' more content');
    $content = $view['slots']->get('name', 'default');
    $view['slots']->output('name');

Asset Helper
------------

.. code-block:: php

    echo '<img src="' . $view['assets']->getUrl('plugins/HelloWorldBundle/assets/images/earth.png') . '" />';
    echo $view['assets']->includeScript('plugins/HelloWorldBundle/assets/helloworld.js');
    echo $view['assets']->includeStylesheet('plugins/HelloWorldBundle/assets/helloworld.css');

Router Helper
-------------

.. code-block:: php

    <a href="<?php echo $view['router']->generate('plugin_helloworld_world', array('world' => 'mars')); ?>" data-toggle="ajax">Mars</a>

Translation Helper
------------------

.. code-block:: php

    <h1><?php echo $view['translator']->trans('plugin.helloworld.worlds', array('%world%' => 'Mars')); ?></h1>

Date Helper
-----------

.. code-block:: php

    $datetime = '2015-04-12 20:56:00';
    $view['date']->toFull($datetime);
    $view['date']->toShort($datetime);
    $view['date']->toDate($datetime);
    $view['date']->toTime($datetime);
    $view['date']->toFullConcat($datetime);
    $view['date']->toText($datetime);
    $view['date']->toFull($datetime, 'Y-m-d H:i:s', 'UTC');

Form Helper
-----------

.. code-block:: php

    <?php echo $view['form']->form($form); ?>

Ajax Integration
============

Ajax Links
----------

.. code-block:: php

    <a href="<?php echo $view['router']->generate('plugin_helloworld_world', array('world' => 'mars')); ?>" data-toggle="ajax">Mars</a>

Ajax Modals
-----------

.. code-block:: php

    <a href="<?php echo $view['router']->generate('plugin_helloworld_world', array('world' => 'mars')); ?>"
       data-toggle="ajaxmodal"
       data-target="#MauticSharedModal"
       data-header="<?php echo $view['translator']->trans('plugin.helloworld.worlds', array('%world%' => 'Mars')); ?>">
       Mars
    </a>

Ajax Forms
----------

Forms rendered with Symfony form services are auto-ajaxified.


