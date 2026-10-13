Config file
###########

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Mautic leverages a simple array based config file to register routes, menu items, Categories, and configuration parameters.

General config items
********************
Mautic recognizes the Plugin through the general config options.

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/Config/config.php

    return [
        'name'        => 'Hello World',
        'description' => 'This is an example config file for a simple Hello World plugin.',
        'author'      => 'Someone Awesome',
        'version'     => '1.0.0',

    // ...

.. list-table::
    :header-rows: 1
    :widths: 15 15 40 

    * - Key
      - Type
      - Description
    * - ``name``
      - string
      - Human readable name for the Plugin that displays in the Plugin Manager.
    * - ``description``
      - string
      - Optional description of the Plugin. This is currently not displayed in the UI.
    * - ``author``
      - string
      - Author of the Plugin for attribution purposes.
    * - ``version``
      - string
      - The version should be in a format compatible with :xref:`PHP's standardized version strings<PHP standardized version strings>`. The Plugin Manager uses PHP's ``version_compare()`` to determine if the Plugin is eligible for an upgrade.

.. _routing config items:

Routing config items
********************

Routes define the URL paths that execute the specified controller action. Register routes with Mautic through the ``routes`` key in the Plugin's config. Define each route under one of Mautic's :ref:`supported firewalls<plugins/config:Routing firewalls>` with a uniquely identifying key and the :ref:`route's definition<plugins/config:Route definitions>`.

.. code-block:: php

    <?php

    // ...

    'routes' => [
        'main'   => [
            'plugin_helloworld_world' => [
                'path'         => '/hello/{world}',
                'controller'   => [MauticPlugin\HelloWorldBundle\Controller\DefaultController::class, 'world'],
                'defaults'     => [
                    'world' => 'earth',
                ],
                'requirements' => [
                    'world' => 'earth|mars',
                ],
            ],
            'plugin_helloworld_list'  => [
                'path'       => '/hello/{page}',
                'controller' => [MauticPlugin\HelloWorldBundle\Controller\DefaultController::class, 'index'],
            ],
            'plugin_helloworld_admin' => [
                'path'       => '/hello/admin',
                'controller' => [MauticPlugin\HelloWorldBundle\Controller\DefaultController::class, 'admin']
            ],
        ],
        'public' => [
            'plugin_helloworld_goodbye' => [
                'path'       => '/hello/goodbye',
                'controller' => MauticPlugin\HelloWorldBundle\Controller\GoodbyeController::class, // assumes an invokable class
            ],
            'plugin_helloworld_contact' => [
                'path'       => '/hello/contact',
                'controller' => MauticPlugin\HelloWorldBundle\Controller\ContactController::class, // assumes an invokable class
            ],
        ],
        'api'    => [
            'plugin_helloworld_api' => [
                'path'       => '/hello',
                'controller' => MauticPlugin\HelloWorldBundle\Controller\Api\HelloController::class, // assumes an invokable class
                'method'     => 'GET',
            ],
        ],
    ],

    // ...

Routing firewalls
=================

The following firewalls are available to routes.

.. list-table::
    :header-rows: 1
    :widths: 15 20 65 

    * - Key
      - URL prefix
      - Description
    * - ``api``
      - ``/api/*``
      - Routes that require API User authentication such as OAuth 2.0.
    * - ``main``
      - ``/s/*``
      - Routes that require standard User authentication to access secure parts of the UI.
    * - ``public``
      - ``/*``
      - Routes that are public facing and don't require any User authentication.
    * - ``catchall``
      - ``/*``
      - A special public firewall compiled after all other routes and namely used by Landing Pages to recognize custom Landing Page URLs.

Each firewall accepts an array of defined routes. Each key, the route's name, must be unique across all bundles and firewalls. Paths must be unique across the same firewall.  **Order does matter** as Symfony uses the first matching route.

.. warning:: Each route's name must be unique across all bundles and firewalls and paths must be unique within the same firewall.

.. warning:: Order of routes matters as Symfony uses the first route that matches the URL.

Route definitions
=================

Route definitions define the route's method, path, controller, parameters, and others defined below.

.. list-table::
    :header-rows: 1
    :widths: 28 20 25 60

    * - Key
      - Is required?
      - Type
      - Description
    * - ``path``
      - yes
      - string
      - Defines the URL path for the route. Define placeholders for parameters using curly brackets. Symfony passes values for parameters into the controller method arguments that match by name. For example, ``/hello/{world}`` matches ``/hello/earth``, ``/hello/mars``, ``/hello/jupiter``, and so forth. Symfony assigns ``earth``, ``mars``, and ``jupiter`` to the argument ``string $world`` if declared in the controller's method.
    * - ``controller``
      - yes
      - string|array
      - Defines the controller and method to call when the path matches. Use one of these formats:

        * ``[MauticPlugin\HelloWorldBundle\Controller\WorldController::class, 'hello']`` or the string ``'MauticPlugin\HelloWorldBundle\Controller\WorldController::hello'`` executes ``WorldController::hello()``.
        * ``MauticPlugin\HelloWorldBundle\Controller\WorldController::class`` executes ``WorldController::__invoke()``.

        Symfony doesn't resolve bundle notation, such as ``HelloWorldBundle:World:hello``, so a route that uses it fails to load its controller.
    * - ``method``
      - no
      - string
      - Restricts the route to a specific method. For example GET, POST, PATCH, PUT, OPTIONS. Symfony recognizes all methods by default.
    * - ``defaults``
      - no
      - array
      - Defines the default values for path placeholders as key/value pairs. For example, given the path, ``/hello/{world}``, where ``world`` defaults to ``earth``, define this as an array ``['world' => 'earth'],``. Visiting ``/hello`` is now the same as visiting ``/hello/earth``.
    * - ``requirements``
      - no
      - array
      - Defines regular expression patterns for placeholders as key/value pairs that the URL path must match. For example, visiting ``/hello/jupiter`` is ignored when given the path, ``/hello/{world}`` and a ``requirements`` of ``['world' => 'earth|mars'],``.
    * - ``format``
      - no
      - string
      - Sets the "request format" of the Request object such as ``Content-Type`` of the response. For example, a json format translates into a ``Content-Type`` of ``application/json``.
    * - ``standard_entity``
      - no
      - boolean
      - If the firewall is ``api``, setting this to ``TRUE`` automatically registers GET, POST, PUT, PATCH, and DELETE API endpoints for single and batch handling of entities.

Special routing parameters
--------------------------

Mautic defaults the following route definitions if not declared otherwise by the Plugin.

.. list-table::
    :header-rows: 1
    :widths: 15 20 50

    * - Parameter
      - Default value
      - Description
    * - ``{page}``
      - ``['requirements' => ['{page}' => '\d+']]``
      - Recognizes only digits for page parameters - used in pagination.
    * - ``{objectId}``
      - ``['defaults' => ['{objectId' => 0]]``
      - Routes that views or edits a specific entity may leverage this.
    * - ``{id}``
      - ``['requirements' => ['{id}' => '\d+']]``
      - Requires a digit if using the ``api`` firewall.

Advanced routing
================

Configure custom routes by writing a listener for the ``Mautic\CoreBundle\Event\RouteEvent`` event. Listeners to this event receive the ``RouteEvent`` object. Mautic dispatches an event for each firewall when compiling routes. Key your subscriber on ``RouteEvent::class``.

To update a subscriber that uses ``CoreEvents`` constants, see :ref:`CoreBundle <Mautic 8 corebundle>`.

.. php:class:: Mautic\CoreBundle\Event\RouteEvent

  .. php:method:: getType()

      :returns: The :ref:`route firewall<plugins/config:Routing firewalls>` for the given route collection.
      :returntype: string

  .. php:method:: getCollection()

      :returns: Returns a RouteCollection object that can be used to manually define custom routes.
      :returntype: \\Symfony\\Component\\Routing\\RouteCollection

  .. php:method:: addRoutes(string $path)

      Load custom routes through a resource file such as yaml or XML.

      :param string $path: Path to the resource file. For example, ``@FMElfinderBundle/Resources/config/routing.yaml``.
      :returntype: void

Debugging routes
================

Use the follow commands to help debug routes:

.. list-table::
    :header-rows: 1

    * - Command
      - Description
    * - ``php bin/console debug:router``
      - Lists all registered routes.
    * - ``php bin/console debug:router article_show``
      - Lists the definition for the route ``article_show``.
    * - ``php bin/console router:match /blog/my-latest-post``
      - Lists the route that matches the URL path ``/blog/my-latest-post``.

Menu config items
*****************

Plugins define items for Mautic's varying menus through the ``menu`` config array keyed by the menu supported. Each menu can either be an array of menu items that assume default priority, see ``admin`` below for an example, or defined under an ``items`` array with an optional ``priority`` inherited by all defined items, see ``main`` below for an example.

.. code-block:: php

    <?php
    // ...

    'menu' => [
        'main'  => [
            'priority' => 4,
            'items'    => [
                'plugin.helloworld.index' => [
                    'id'        => 'plugin_helloworld_index',
                    'iconClass' => 'fa-globe',
                    'access'    => 'plugin:helloworld:worlds:view',
                    'parent'    => 'mautic.core.channels',
                    'children'  => [
                        'plugin.helloworld.manage_worlds' => [
                            'route' => 'plugin_helloworld_list',
                        ],
                        'mautic.category.menu.index'      => [
                            'bundle' => 'plugin:helloWorld',
                        ],
                    ],
                    'checks'    => [
                        'integration' => [
                            'HelloWorld' => [
                                'enabled'  => true,
                                'features' => [
                                    'sync',
                                ],
                            ],
                        ],
                    ],
                ],
            ],
        ],
        'admin' => [
            'plugin.helloworld.admin' => [
                'route'     => 'plugin_helloworld_admin',
                'iconClass' => 'fa-gears',
                'access'    => 'admin',
                'checks'    => [
                    'parameters' => [
                        'helloworld_api_enabled' => true,
                    ],
                ],
                'priority'  => 60,
            ],
        ],
    ],

    // ...

Available menus
===============

There are currently four menus built into Mautic.

.. list-table::
    :header-rows: 1
    :widths: 25 50

    * - Key
      - Description
    * - ``main``
      - Main app navigation.
    * - ``admin``
      - Menu for administration tasks such as Configuration, Webhooks, Custom Fields, and others.
    * - ``profile``
      - Menu for User specific tasks such as Profile and Logout.
    * - ``extra``
      - Menu not used by Core but available to Plugins.

A Plugin can also register its own top-level menu instead of adding items to these. See :ref:`Plugins/config:Registering a custom menu`.

Menu definitions
================

Menu item priority
------------------

The ``priority`` determines the position in the parent menu where items display relative to other items defined by Core and Plugins. This can be in the root of the menu's array to set the priority for all items defined or in a specific item's definition. It can be negative to position the items lower than others or positive to position them higher. The default is ``9999`` if not defined.

.. note:: You aren't able to control the exact position of items in menus.

Menu item definitions
---------------------

Define items in an ``items`` array along with ``priority`` or at the root of the menu's array.

Key each item with its respective :ref:`language string key<plugins/translations:Translating plugins>`.

.. list-table::
    :header-rows: 1
    :widths: 25 15 25 50 

    * - Key
      - Is required?
      - Type
      - Description
    * - ``route``
      - conditional
      - string
      - Name of the :ref:`Routing config items<plugins/config:Route definitions>` for this item. Leave undefined if the item is a placeholder for a sub-menu or if you define a ``uri`` instead.
    * - ``routeParameters``
      - no
      - array
      - Key/value pairs of :ref:`path parameters<plugins/config:Route definitions>` for the given ``route``.
    * - ``uri``
      - conditional
      - string
      - Explicit URL for the menu item's link, used instead of a ``route``. Use this to link to an external or static URL, for example, ``https://mautic.org``. Mautic keeps any item that defines a ``route``, a ``uri``, or ``children``; items that define only a ``uri`` render starting in Mautic 7.2.
    * - ``parent``
      - no
      - string
      - Name of a parent menu to display this item under. For example, ``mautic.core.channels``, ``mautic.core.components``, or any parent defined by a Plugin.
    * - ``priority``
      - no
      - ``int``
      - Determines the position of this item relative to it's sibling items. See :ref:`plugins/config:Menu item priority`.
    * - ``access``
      - no
      - string
      - The :ref:`permission<security-roles-and-permissions>` required to display this menu item. For example, ``category:categories:view`` or ``admin`` to restrict to only Administrators.
    * - ``checks``
      - no
      - array
      - Define checks that must evaluate to ``TRUE`` to display the item. See :ref:`plugins/config:Menu item checks` for more details.
    * - ``id``
      - no
      - string
      - ID for the menu item's link element, ``<a />``. Uses the value for ``route`` by default.
    * - ``iconClass``
      - no
      - string
      - Font Awesome class to set the icon for the menu item.
    * - ``linkAttributes``
      - no
      - array
      - Key/value pairs of HTML attributes to add to the item's link element, ``<a />``. For example, set ``['target' => '_blank', 'rel' => 'noopener noreferrer']`` to open the link in a new tab.

Menu item checks
----------------

Supported checks are ``parameters``, ``request``, and ``integration``.

``parameters`` is an array of key/value pairs that matches the same key/value pair in Mautic's Configuration. For example:

.. code-block:: php

    <?php
    // ...

    [
        'parameters' => [
            'sysinfo_disabled' => false,
        ],
    ],

    // ...

``request`` is an array of key/value pairs that matches the same key/value pair in Symfony's Request. For example:

.. code-block:: php

    <?php
    // ...

    [
        'request' => [
            'show-something' => 1,
        ],
    ],

    // ...

``integration`` contains key/value pairs with the Integration name as the key with an array of configuration options. Supported keys are ``enabled`` and ``features``. Define ``TRUE`` or ``FALSE`` for ``enabled`` to only show the menu item if the specified Integration's enabled state matches. Define an array of ``features`` enabled for the Integration to show the menu item. For example:

.. code-block:: php

    <?php
    // ...

    [
        'integration' => [
            'OneSignal' => [
                'enabled'  => true,
                'features' => [
                    'mobile',
                ],
            ],
        ],
    ],

    // ...

Of course, you can also combine multiple checks. All must evaluate to TRUE to display the item.

.. code-block:: php

    <?php
    // ...

    [
        'parameters' => [
            'sysinfo_disabled' => false,
        ],
        'request' => [
            'show-something' => 1,
        ],
        'integration' => [
            'OneSignal' => [
                'enabled'  => true,
                'features' => [
                    'mobile',
                ],
            ],
        ],
    ],

    // ...

Registering a custom menu
*************************

The :ref:`Plugins/config:Menu config items` section adds items to Mautic's four built-in menus through the ``menu`` config array. This section covers the opposite direction: registering a Plugin's own top-level menu, with its own template and renderer.

Registering a custom menu takes two services in your Plugin's ``Config/services.php``:

* A ``Knp\Menu\MenuItem`` tagged ``knp_menu.menu``.
* A ``Mautic\CoreBundle\Menu\MenuRenderer`` tagged ``knp_menu.renderer``.

Give each tag an ``['alias' => '<alias>']`` argument so Mautic pairs the item with its renderer.

The following partial example registers the menu item and renderer. Its ``use`` statements go at the top of ``Config/services.php``, and the ``$services->set(...)`` definitions go inside its configurator closure. :ref:`plugins/autowiring:Autowiring` describes the bundle Extension and this ``$services`` configurator setup:

.. code-block:: php

    <?php

    use Knp\Menu\MenuItem;
    use Mautic\CoreBundle\Menu\MenuBuilder;
    use Mautic\CoreBundle\Menu\MenuRenderer;

    use function Symfony\Component\DependencyInjection\Loader\Configurator\service;

    // ... inside the configurator closure, using the same $services

    $services->set('mautic.menu.mybundle', MenuItem::class)
        ->factory([service(MenuBuilder::class), 'mybundleMenu'])
        ->tag('knp_menu.menu', ['alias' => 'mybundle']);

    $services->set('mautic.menu_renderer.mybundle', MenuRenderer::class)
        ->args([service('knp_menu.matcher'), service('twig'), ['template' => '@MyBundle/Menu/mybundle.html.twig']])
        ->tag('knp_menu.renderer', ['alias' => 'mybundle']);

Reference the menu builder by class through ``service(Mautic\CoreBundle\Menu\MenuBuilder::class)``.

These two services register and render the menu, while the ``<alias>Menu`` method the factory calls on the menu builder, here ``mybundleMenu``, supplies the menu's contents.

If your bundle has several menus, register them in a loop. ``$menuTemplates`` is the alias-to-options array you supply:

.. code-block:: php

    foreach ($menuTemplates as $alias => $options) {
        $services->set('mautic.menu.'.$alias, MenuItem::class)
            ->factory([service(MenuBuilder::class), $alias.'Menu'])
            ->tag('knp_menu.menu', ['alias' => $alias]);

        $services->set('mautic.menu_renderer.'.$alias, MenuRenderer::class)
            ->args([service('knp_menu.matcher'), service('twig'), $options])
            ->tag('knp_menu.renderer', ['alias' => $alias]);
    }

To update a menu that a Plugin registers through ``Config/config.php``, see :ref:`Menu registration <Mautic 8 menu registration>`.

Service config items
********************

Register the Plugin's services in its ``Config/services.php`` file. Mautic doesn't read a ``services`` group in ``Config/config.php``. :ref:`Autowiring <Plugin Autowiring>` describes the ``services.php`` file and the bundle Extension that loads it.

With ``autowire()`` and ``autoconfigure()`` enabled, Symfony registers the classes that ``$services->load()`` finds and tags them by the interface or base class they implement, such as event subscribers, Form types, console commands, and ``AbstractPermissions`` subclasses. Define a service explicitly when it needs an argument that Symfony can't resolve from the parameter type, or a tag that autoconfiguration doesn't add, such as the :ref:`plugins/config:Mautic service tags`:

.. code-block:: php

    <?php

    declare(strict_types=1);

    use Mautic\CoreBundle\DependencyInjection\MauticCoreExtension;
    use MauticPlugin\HelloWorldBundle\Sms\HelloWorldTransport;
    use Symfony\Component\DependencyInjection\Loader\Configurator\ContainerConfigurator;

    use function Symfony\Component\DependencyInjection\Loader\Configurator\service;

    return function (ContainerConfigurator $configurator): void {
        $services = $configurator->services()
            ->defaults()
            ->autowire()
            ->autoconfigure()
            ->public();

        $services->load('MauticPlugin\\HelloWorldBundle\\', '../')
            ->exclude('../{'.implode(',', MauticCoreExtension::DEFAULT_EXCLUDES).'}');

        $services->set(HelloWorldTransport::class)
            ->arg('$logger', service('monolog.logger.mautic'))
            ->tag('mautic.sms_transport', ['integrationAlias' => 'HelloWorld']);
    };

To update services that a Plugin defines in ``Config/config.php``, see :ref:`Services array <Mautic 8 config php services array>`.

Mautic service tags
===================

Mautic uses the follow tags to register services as described below.

**Channel tags**

.. list-table::
    :header-rows: 1
    :widths: 35 27 50 

    * - Tag
      - Supported tag arguments
      - Description
    * - ``mautic.sms_transport``
      - ``['integrationAlias' => 'Name to display in the UI for this transport.']``
      - Register this service as a Text Message transport.
    * - ``mautic.sms_callback_handler``
      - none
      - Registers this service to handle Webhooks from a Text Message transport.
    * - ``mautic.email_transport``
      - Key/value pairs to configure fields required to authenticate with the transport's service. See :ref:`components/emails:Email transports`.
      - Registers the service as an :ref:`Email transport<components/emails:Email transports>`.
    * - ``mautic.email_stat_helper``
      - none
      - Registers the service as a stat helper for Email charts. See :ref:`components/emails:Email stat helpers`.

**Core tags**

.. list-table::
    :header-rows: 1
    :widths: 25 15 50 

    * - Tag
      - Supported tag arguments
      - Description
    * - ``mautic.permissions``
      - none
      - Registers the service as a permission object that must extend ``\Mautic\CoreBundle\Security\Permissions\AbstractPermissions``. See :ref:`security-Roles-and-permissions`. Mautic adds this tag automatically to every ``AbstractPermissions`` subclass registered with ``autoconfigure()``.

**Integration tags**

.. list-table::
    :header-rows: 1
    :widths: 40 20 50 

    * - Tag
      - Supported tag arguments
      - Description
    * - ``mautic.basic_integration``
      - none
      - Registers the service as an :ref:`Integration<components/integrations:Integrations>`.
    * - ``mautic.builder_integration``
      -  none
      - Registers the service as a :ref:`Builder<components/integrations:Integration Builders>`.
    * - ``mautic.authentication_integration``
      - none
      - Registers the service to :ref:`authenticate with the Integration's service<components/integrations:Integration authentication>`.
    * - ``mautic.config_integration``
      - none
      - Registers the service to :ref:`configure the Integration<components/integrations:Integration configuration>`.
    * - ``mautic.sync_integration``
      - none
      - Registers the service to :ref:`sync with Mautic objects with the Integration's service<components/integrations:Integration sync engine>`.
    * - ``mautic.sync.notification_handler``
      - none
      - Registers the service to handle sync notifications.

Category config items
*********************

Use ``categories`` to define Category types available to the Category manager. See :ref:`components/categories:Categories`.

.. code-block:: php

    <?php
    // ...

   'categories' => [
        'plugin:helloWorld' => 'mautic.helloworld.world.categories',
    ],

    // ...

Parameters config items
***********************

Configure parameters that are consumable through Mautic's ``CoreParameterHelper``, passed into services with ``%mautic.key%``, or read from the environment via ``MAUTIC_KEY``. See :ref:`components/config:Configuration parameters` for more information.

.. code-block:: php

    <?php

    // ...

    'parameters' => [
        'helloworld_api_enabled'      => false,
        'helloworld_supported_worlds' => ['earth', 'mars', 'jupiter',],
    ],

    // ...

.. note:: The default value must match the value's type for Mautic to typecast and transform appropriately. For example, if there isn't a specific default value to declare, define an empty array, ``[]``, for an array type; zero, ``0``, for an integer type; ``TRUE`` or ``FALSE`` for boolean types; and so forth. Services leveraging parameters should accept and handle ``NULL`` for integer and string types, excluding ``0``.

.. note:: Parameters aren't exposed to the UI by default. See :ref:`components/config:Configuration` for more information.

Custom config parameters
************************

You can define custom configuration parameters in your Plugin to support configurable features, such as enabling or disabling functions.

Mautic Plugins allow you to define these parameters for use within your Plugin’s code. Store these parameters in ``config/local.php``, and define their default values in the Plugin’s own config file to ensure stability and avoid errors.

To avoid errors during cache compilation or when accessing parameters directly from the container without checking for their existence, always define custom parameters in the :ref:`plugins/config:Parameters config items`. This guarantees that the parameter exists and has a fallback value.

To add these configuration options in Mautic's configuration section, you’ll need:

- An :doc:`event subscriber </plugins/event_listeners>` to register the configuration.
- A :doc:`Form type </components/forms>` that defines the fields. 
- A specific view for rendering the form.

.. note::

   To translate the Plugin’s tab label in the configuration form, include a translation key like ``mautic.config.tab.helloworld_config`` in the Plugin’s ``messages.ini`` file. Replace ``helloworld_config`` with the ``formAlias`` used when registering the form in the event subscriber.

Config event subscriber
=======================

A config event subscriber adds the Plugin's settings to Mautic's configuration UI and processes the submitted values. Mautic dispatches the configuration events by their event class, so the subscriber keys ``getSubscribedEvents()`` on ``ConfigBuilderEvent::class`` and ``ConfigPreSaveEvent::class``.

To update a subscriber that uses ``ConfigEvents`` constants, see :ref:`ConfigBundle <Mautic 8 configbundle>`.

The following code example shows how a Plugin structures its event subscriber.

.. code-block:: php

    <?php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\EventListener;
    use Mautic\ConfigBundle\Event\ConfigBuilderEvent;
    use Mautic\ConfigBundle\Event\ConfigPreSaveEvent;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    final class ConfigSubscriber implements EventSubscriberInterface
    {
        /**
         * @return mixed[]
         */
        static public function getSubscribedEvents(): array
        {
            return [
                ConfigBuilderEvent::class => ['onConfigGenerate', 0],
                ConfigPreSaveEvent::class => ['onConfigSave', 0],
            ];
        }

        public function onConfigGenerate(ConfigBuilderEvent $event): void
        {
            $event->addForm(
                [
                    'formAlias'  => 'helloworld_config',
                    'formTheme'  => '@HelloWorldBundle/FormTheme/Config/_config_helloworld_config_widget.html.twig',
                    'parameters' => $event->getParametersFromConfig('HelloWorldBundle')
                ]
            );
        }

        public function onConfigSave(ConfigPreSaveEvent $event): void
        {
            /** @var array $values */
            $values = $event->getConfig();
            // Manipulate the values
            if (!empty($values['helloworld_config']['custom_config_option'])) {
                $values['helloworld_config']['custom_config_option'] = htmlspecialchars($values['helloworld_config']['custom_config_option']);
            }
            // Set updated values 
            $event->setConfig($values);
        }
    }

Subscribed events
-----------------

The event subscriber listens to the following events:

* ``ConfigBuilderEvent::class`` - Mautic dispatches this event when it builds the configuration UI. The Plugin uses it to add its own tab and configuration options.
* ``ConfigPreSaveEvent::class`` - Mautic dispatches this event before it saves the submitted values to the ``local.php`` file. The Plugin uses it to clean up or modify the data before Mautic writes it.
* ``ConfigPostSaveEvent::class`` - Mautic dispatches this event after it writes the values to ``local.php``. Subscribe to it to react to saved configuration changes. The example subscriber doesn't use it.

All three classes live in the ``Mautic\ConfigBundle\Event`` namespace. ``ConfigPreSaveEvent`` and ``ConfigPostSaveEvent`` extend ``ConfigEvent``, so a listener method that type-hints ``ConfigEvent`` still receives either event. After saving, Mautic creates a separate ``ConfigPostSaveEvent`` object. It carries the saved configuration values, including any changes that ``ConfigPreSaveEvent`` listeners made with ``setConfig()``.

Generate Plugin configuration
-----------------------------

To register the Plugin's configuration details during the ``ConfigBuilderEvent`` event, call the ``addForm()`` method on the ``ConfigBuilderEvent`` object. The method expects an array with the following elements:

.. list-table::
    :header-rows: 1
    :widths: 15 50 

    * - Key
      - Description
    * - ``formAlias``
      - The alias of the Symfony ``FormType`` class that defines the expected configuration fields.
    * - ``formTheme``
      - The full Twig template path that formats the configuration fields, for example, ``@HelloWorldBundle/FormTheme/Config/_config_helloworld_config_widget.html.twig``.
    * - ``parameters``
      - An array of custom configuration elements. ``Use $event->getParametersFromConfig('HelloWorldBundle')`` to retrieve them from the plugin’s configuration file.

Modify configuration before saving
----------------------------------

To modify the submitted values before saving, subscribe to ``ConfigPreSaveEvent::class``. Mautic dispatches this event just before it writes them to the ``local.php`` file, so the Plugin can adjust them with ``$event->setConfig()``.

Register the event subscriber
-----------------------------

Load the subscriber's directory in the Plugin's ``Config/services.php`` with ``autoconfigure()`` enabled, as described in :ref:`Autowiring <Plugin Autowiring>`. Symfony then tags any class that implements ``EventSubscriberInterface`` as an event subscriber, so the Plugin listens for the event without further configuration.

Config form
===========

The form type is used to generate the form fields in the main configuration form. See the :doc:`Forms documentation</components/forms>` for more information about using form types.

Register the form type as a service by loading its directory in the Plugin's ``Config/services.php`` with ``autoconfigure()`` enabled, as described in :ref:`Autowiring <Plugin Autowiring>`. Symfony then tags any class that implements ``FormTypeInterface`` as a form type.

Below is an example of a form type class that adds a custom configuration option to the Plugin's configuration form.

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/Form/Type/ConfigType.php

    namespace MauticPlugin\HelloWorldBundle\Form\Type;

    use Symfony\Component\Form\AbstractType;
    use Symfony\Component\Form\FormBuilderInterface;

    final class ConfigType extends AbstractType
    {
        /**
         * @param mixed[] $options
         */
        public function buildForm(FormBuilderInterface $builder, array $options): void
        {
            $builder->add(
                'custom_config_option',
                'text',
                [
                    'label' => 'plugin.helloworld.config.custom_config_option',
                    'data'  => $options['data']['custom_config_option'],
                    'attr'  => [
                        'tooltip' => 'plugin.helloworld.config.custom_config_option_tooltip'
                    ]
                ]
            );
        }
    }

Config template
===============

``formTheme`` must be the full Twig template path. Mautic passes the string directly to Twig's ``form_theme`` tag and doesn't derive it from ``formAlias`` or the bundle name. By convention, place the template under the Plugin's ``Resources/views/FormTheme/Config`` folder and name it ``_config_{formAlias}_widget.html.twig``, where ``{formAlias}`` matches the ``formAlias`` set in the Plugin's ``ConfigBuilderEvent`` event listener.

The template should be structured in a panel format to match the rest of the configuration UI.

Below is an example of how the template should be structured:

.. code-block:: twig

    {# plugins/HelloWorldBundle/Resources/views/FormTheme/Config/_config_helloworld_config_widget.html.twig #}
    <div class="panel panel-primary">
        <div class="panel-heading">
            <h3 class="panel-title">{{ 'mautic.config.tab.helloworld_config'|trans }}</h3> 
        </div>
        <div class="panel-body">  
            {% for field in form.children %}  
                <div class="row">  
                    <div class="col-md-6">  
                        {{ form_row(field) }}  
                    </div>  
                </div>  
            {% endfor %}  
        </div>  
    </div>  