Configuration
==============
Mautic leverages a simple array based config file to register routes, menu items, services, categories and configuration parameters.

General config items
--------------------------
The general config options define how the plugin is recognized by Mautic.

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/Config/config.php

    return [
        'name'        => 'Hello World',
        'description' => 'This is an example config file for a simple Hello World plugin.',
        'author'      => 'Someone Awesome',
        'version'     => '1.0.0',

.. list-table::
    :header-rows: 1

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
      - Author of the plugin for attribution purposes.
    * - ``version``
      - string
      - The version should be in a format compatible with :ref:`PHP's standardized version strings<PHP standardized version strings>`. The Plugin Manager uses PHP's ``version_compare()`` to determine if the plugin should be upgraded.

Routing config items
--------------------------

Routes define the URL paths that execute the specified controller action. Register routes with Mautic through the ``routes`` key in the Plugin's config. Define each route under one of Mautic's :ref:`supported firewalls<Routing firewalls>` with a uniquely identifying key and the :ref:`route's definition<Route definitions>`.

.. code-block:: php

    'routes' => [
        'main'   => [
            'plugin_helloworld_world' => [
                'path'         => '/hello/{world}',
                'controller'   => [MauticPlugin\HelloWorldBundle\Controller\DefaultController, 'world'],
                'defaults'     => [
                    'world' => 'earth',
                ],
                'requirements' => [
                    'world' => 'earth|mars',
                ],
            ],
            'plugin_helloworld_list'  => [
                'path'       => '/hello/{page}',
                'controller' => [MauticPlugin\HelloWorldBundle\Controller\DefaultController, 'index'],
            ],
            'plugin_helloworld_admin' => [
                'path'       => '/hello/admin',
                'controller' => [MauticPlugin\HelloWorldBundle\Controller\DefaultController, 'admin']
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

Routing firewalls
^^^^^^^^^^^^^^^^^^

The following firewalls are available to routes.

.. list-table::
    :header-rows: 1

    * - Key
      - URL prefix
      - Description
    * - ``api``
      - ``/api/*``
      - Routes that require API user authentication such as OAuth2.
    * - ``main``
      - ``/s/*``
      - Routes that require standard user authentication to access secure parts of the UI.
    * - ``public``
      - ``/*``
      - Routes that are public facing and do not require any user authentication.
    * - ``catchall``
      - ``/*``
      - A special public firewall compiled after all other routes and namely used by Landing Pages in order to recognize custom Landing Page URLs.

Each firewall accepts an array of defined routes. Each key, the route's name, must be unique across all bundles and firewalls. Paths must be unique across the same firewall.  **Order does matter** as the first matching route will be used.

.. warning:: Each route's name must be unique across all bundles and firewalls and paths must be unique within the same firewall.

.. warning:: Order of routes matters as Symfony will use the first route that matches the URL.

Route definitions
^^^^^^^^^^^^^^^^^^

Route definitions define the route's method, path, controller, parameters, and others defined below.

.. list-table::
    :header-rows: 1

    * - Key
      - Is required?
      - Type
      - Description
    * - ``path``
      - yes
      - string
      - Defines the URL path for the route. Define placeholders for parameters using curly brackets. Values for parameters are passed into the controller method arguments that match by name. For example, ``/hello/{world}`` matches ``/hello/earth``, ``/hello/mars``, ``/hello/jupiter``, and so forth. ``earth``, ``mars``, and ``jupiter`` is assigned to the argument ``string $world`` if declared in the controller's method.
    * - ``controller``
      - yes
      - string|array
      - Defines the controller and function to call when the path is requested. There are three supported formats. The legacy string format, ``HelloWorldBundle:World:hello``, executes ``MauticPlugin\HelloWorldBundle\Controller\WorldController::helloAction()``. The recommended format starting in Mautic 4 is either ``[MauticPlugin\HelloWorldBundle\Controller\WorldController::class, 'hello']`` that executes ``MauticPlugin\HelloWorldBundle\Controller\WorldController::hello()`` or  ``MauticPlugin\HelloWorldBundle\Controller\WorldController::class`` that executes ``MauticPlugin\HelloWorldBundle\Controller\WorldController::__invoke()``.
    * - ``method``
      - no
      - string
      - Restricts the route to a specific method. For example GET, POST, PATCH, PUT, OPTIONS. All methods are supported by default.
    * - ``defaults``
      - no
      - array
      - Defines the default values for path placeholders as key/value paris. For example, if the ``path`` is defined as ``/hello/{world}`` where ``world`` defaults to ``earth``, define this as an array ``['world' => 'earth'],``. Visiting ``/hello`` is now the same as visiting ``/hello/earth``.
    * - ``requirements``
      - no
      - array
      - Defines regex patterns for placeholders as key/value pairs that the URL path must match in order for the route to be recognized. For example, if the ``path`` is defined as ``/hello/{world}`` and ``requirements`` as ``['world' => 'earth|mars'],`` visiting ``/hello/jupiter`` will not execute the defined controller.
    * - ``format``
      - no
      - string
      - The matched value is used to set the "request format" of the Request object. This is used for such things as setting the ``Content-Type`` of the response. For example, a json format translates into a ``Content-Type`` of ``application/json``.
    * - ``standard_entity``
      - no
      - boolean
      - If the firewall is ``api``, setting this to ``TRUE`` will automatically register GET, POST, PUT, PATCH, and DELETE API endpoints for single and batch handling of entities.

Special routing parameters
""""""""""""""""""""""""""

Mautic defaults the following route definitions if not declared otherwise by the plugin.

.. list-table::
    :header-rows: 1

    * - Parameter
      - Default value
      - Description
    * - ``{page}``
      - ``['requirements' => ['{page}' => '\d+']]``
      - Only digits are recognized for page parameters meant to be used in pagination.
    * - ``{objectId}``
      - ``['defaults' => ['{objectId' => 0]]``
      - Typically used in routes that views or edits a specific entity.
    * - ``{id}``
      - ``['requirements' => ['{id}' => '\d+']]``
      - A digit is required if using the ``api`` firewall.

Advanced routing
^^^^^^^^^^^^^^^^^

Configure custom routes through writing a listener to the ``\Mautic\CoreBundle\CoreEvents::BUILD_ROUTE`` event. Listeners to this event receives a ``Mautic\CoreBundle\Event\RouteEvent`` object. An event is dispatched for each firewall when routes are compiled.

.. php:class:: Mautic\CoreBundle\Event\RouteEvent

.. php:method:: getType(): string

      :returns: The :ref:`route firewall<Routing firewalls>` for the given route collection.

.. php:method:: getCollection(): Symfony\Component\Routing\RouteCollection

    :returns: Returns a RouteCollection object that can be used to manually define custom routes.

.. php:method:: addRoutes: void

    Load custom routes through a resource file such as yaml or XML.

    :param string $path: Path to the resource file. For example, ``@FMElfinderBundle/Resources/config/routing.yaml``.

Debugging routes
^^^^^^^^^^^^^^^^^^

Use the follow commands to help debug routes:

.. list-table::
    :header-rows: 1

    * - Command
      - Description
    * - ``php app/console router:debug``
      - Lists all registered routes.
    * - ``php app/console router:debug article_show``
      - Lists the definition for the route ``article_show``.
    * - ``php app/console router:match /blog/my-latest-post``
      - Lists the route that matches the URL path ``/blog/my-latest-post``.

Menu config items
--------------------------

Plugins define items for Mautic's varying menus through the ``menu`` config array keyed by the menu supported. Each menu can either be an array of menu items that assume default priority, see ``admin`` below for an example, or defined under an ``items`` array with an optional ``priority`` inherited by all defined items, see ``main`` below for an example.

.. code-block:: php

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


Available menus
^^^^^^^^^^^^^^^^^^

There are currently four menus built into Mautic.

.. list-table::
    :header-rows: 1

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

Menu definitions
^^^^^^^^^^^^^^^^^

Menu item priority
""""""""""""""""""""

The ``priority`` determines the position in the parent menu where items are displayed relative to other items defined by Core and Plugins. This can be in the root of the menu's array to set the priority for all items defined or in a specific item's definition. It can be negative to position the items lower than others or positive to position them higher. The default is ``9999`` if not defined.

.. notice:: You are not able to control the exact position of items in menus.

Menu item definitions
""""""""""""""""""""""

Define items in an ``items`` array along with ``priority`` or at the root of the menu's array.

Key each item with its respective :ref:`language string key<Translations>`.

.. list-table::
    :header-rows: 1

    * - Key
      - Is required?
      - Type
      - Description
    * - ``route``
      - conditional
      - string
      - Name of the :ref:`Routing config items<route>` for this item. Leave undefined if the item is a placeholder for a submenu.
    * - ``routeParameters``
      - no
      - array
      - Key/value pairs of :ref:`path parameters<Route definitions>`` for the given ``route``.
    * - ``parent``
      - no
      - string
      - Name of a parent menu to display this item under. For example, ``mautic.core.channels``, ``mautic.core.components``, or any parent defined by a Plugin.
    * - ``priority``
      - no
      - ``int``
      - Determines the position of this item relative to it's sibling items. See :ref:`Menu item priority`.
    * - ``access``
      - no
      - string
      - The :ref:`permission<Roles and permissions>` required in order to display this menu item. For example, ``category:categories:view`` or ``admin`` to restrict to only Administrators.
    * - ``checks``
      - no
      - array
      - Define checks that must evaluate to ``TRUE`` in order to display the item. See :ref:`Menu item checks` for more details.
    * - ``id``
      - no
      - string
      - ID for the menu item's link element, ``<a />``. The value for ``route`` is used by default.
    * - ``iconClass``
      - no
      - string
      - Font Awesome class to set the icon for the menu item.

Menu item checks
""""""""""""""""""

Supported checks are ``parameters``, ``request``, and ``integration``.

``parameters`` is an array of key/value pairs that matches the same key/value pair in Mautic's Configuration. For example:

.. code-block:: php

    [
        'parameters' => [
            'sysinfo_disabled' => false,
        ],
    ],

``request`` is an array of key/value pairs that matches the same key/value pair in Symfony's Request. For example:

.. code-block:: php

    [
        'request' => [
            'show-something' => 1,
        ],
    ],

``integration`` is an array keyed by the name of the Integration to be evaluated. Supported keys are ``enabled`` and ``features``. Define ``TRUE`` or ``FALSE`` for ``enabled`` to only show the menu item if the specified Integration's enabled state matches. Define an array of ``features`` that must be enabled for the Integration to show the menu item. For example:

.. code-block:: php

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

Of course, multiple checks can be combined. All must evaluate to true to display the item.

.. code-block:: php

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

Service config items
--------------------------

Services define the Plugin's classes and their dependencies with Mautic and Symfony. Services defined within specific keys are auto-tagged as noted below.

.. code-block:: php

    'services' => [
        'events'  => [
            'helloworld.leadbundle.subscriber' => [
                'class' => \MauticPlugin\HelloWorldBundle\EventListener\LeadSubscriber::class,
            ],
        ],
        'forms'   => [
            'helloworld.form' => [
                'class' => \MauticPlugin\HelloWorldBundle\Form\Type\HelloWorldType::class,
            ],
        ],
        'helpers' => [
            'helloworld.helper.world' => [
                'class' => MauticPlugin\HelloWorldBundle\Helper\WorldHelper::class,
                'alias' => 'helloworld',
            ],
        ],
        'other'   => [
            'helloworld.mars.validator' => [
                'class'     => MauticPlugin\HelloWorldBundle\Form\Validator\Constraints\MarsValidator::class,
                'arguments' => [
                    'mautic.helper.core_parameters',
                    'helloworld.helper.world',
                ],
                'tag'       => 'validator.constraint_validator',
            ],
        ],
    ],

Service types
^^^^^^^^^^^^^^^^^^

For convenience, Mautic will auto-tag services defined within specific keys.

.. list-table::
    :header-rows: 1

    * - Key
      - Tag
      - Description
    * - ``command`` or ``commands``
      - ``console.command``
      - Registers the service with :xref:`Symfony as a console command<Symfony 4 console command tag>`.
    * - ``controllers``
      - ``controller.service_arguments``
      - Controllers are typically autowired by Symfony. However, you can register :xref:`controllers as services<Symfony 4 controller service arguments tag` to manage your own dependency injection rather than relying on Symfony's service container.
    * - ``events``
      - ``kernel.event_subscriber``
      - Registers the service with :xref:`Symfony as an event subscriber<Symfony 4 event subscriber tag>`.
    * - ``forms``
      - ``form.type``
      - Registers the service with :xref:`Symfony as a custom form field type<Symfony 4 custom form field type tag>`.
    * - ``helpers``
      - ``templating.helper``
      - Registers the service with :xref:`Symfony as a PHP template helper<Symfony 4 PHP template helper tag>`. The service definition must include an ``alias``.
    * - ``models``
      - ``mautic.model``
      - Deprecated. Use service dependency injection instead.
    * - ``permissions``
      - ``mautic.permissions``
      - Registers the service with Mautic's :ref:`permission service<Roles and permissions>`.
    * - ``*`` or ``other``
      - n/a
      - You can use any other key you want to organize services in the config array. Note that this could risk incompatibility with a future version of Mautic if using something generic that Mautic starts to use as well.

Service definitions
^^^^^^^^^^^^^^^^^^^^^

Key each service with a unique name to all of Mautic, including other Plugins.

.. list-table::
    :header-rows: 1

    * - Key
      - Is required?
      - Type
      - Description
    * - ``class``
      - yes
      - string
      - Fully qualified name for the service's class.
    * - ``arguments``
      - no
      - array
      - Array of services, parameters, booleans, or strings injected as arguments into this service's construct. Parameters are recognized by wrapping the parameter key in ``%`` signs, for example, ``'%mautic.some_parameter%',``. Hard coded strings need to be wrapped in ``"`` signs, for example, ``'"some string"',``. Any other string is assumed to be the name of a defined service.
    * - ``alias``
      - conditional
      - string
      - Used by specific service types. For example, services defined under ``helpers`` use this as the key in the ``$view`` variable to access the defined service from PHP templates. Otherwise, it defines an alternate name for the service.
    * - ``tag``
      - no
      - string
      -
    * - ``tags``
      - no
      - array
      -
    * - ``tagArguments``
      - no
      - array
      -
    * - ``factory``
      - no
      - string
      -
    * - ``factory``
      - no
      - array
      -
    * - ``methodCalls``
      - no
      - array
      -
    * - ``decoratedService``
      - no
      - array
    * - ``abstract``
      - no
      - boolean
      -
    * - ``public``
      - no
      - boolean
      -
    * - ``lazy``
      - no
      - boolean
      -
    * - ``synthetic``
      - no
      - boolean
      -
    * - ``file``
      - no
      - string
      -
    * - ``configurator``
      - no
      - array
      -

**tag**|OPTIONAL|string|[Tags](http://symfony.com/doc/2.8/components/dependency_injection/tags.html) the service used by bundles to get a list of specific services (for example form types and event subscribers).
**tags**|OPTIONAL|array|Array of of tags
**tagArguments**|OPTIONAL|array|Array of attributes for the tag. See [Symfony docs](http://symfony.com/doc/2.8/components/dependency_injection/tags.html#adding-additional-attributes-on-tags) for more information.
**factory**|OPTIONAL|string|Preferred method for using a factory class. [Factory class](http://symfony.com/doc/2.8/components/dependency_injection/factories.html) for managing creating the service.
**methodCalls**|OPTIONAL|array|Array of methods to be called after a service is created passing in the array of arguments provided. Should be in the format of 'methodName' => array('service_name', '%parameter%')
**decoratedService**|OPTIONAL|array|[Decorated service](http://symfony.com/doc/2.8/components/dependency_injection/advanced.html#decorating-services)
**public**|OPTIONAL|bool|[Public/private service](http://symfony.com/doc/2.8/components/dependency_injection/advanced.html#marking-services-as-public-private)
**lazy**|OPTIONAL|bool|[Lazy load service](http://symfony.com/doc/2.8/components/dependency_injection/lazy_services.html)
**synthetic**|OPTIONAL|bool|[Synthetic service](http://symfony.com/doc/2.8/components/dependency_injection/synthetic_services.html)
**synthetic**|OPTIONAL|bool|[Synthetic service](http://symfony.com/doc/2.8/components/dependency_injection/synthetic_services.html)
**file**|OPTIONAL|string|[Include file prior to loading service](http://symfony.com/doc/2.8/components/dependency_injection/definitions.html#requiring-files)
**configurator**|OPTIONAL|array|[Use a configurator to load service](http://symfony.com/doc/current/components/dependency_injection/configurators.html#configurator-service-config)

Mautic service tags
""""""""""""""""""""
mautic.permissions

mautic.basic_integration
mautic.builder_integration
mautic.authentication_integration
mautic.config_integration
mautic.sync_integration
mautic.sync.notification_handler

mautic.sms_transport
mautic.sms_callback_handler
mautic.email_transport
mautic.email_stat_helper

Category config items
--------------------------

### Categories

```php
<?php // continued

    'categories' => array(
        'plugin:helloWorld' => 'mautic.helloworld.world.categories'
    ),
```
Defines category types available or the Category manager. See [Extending Categories](#extending-categories).

Parameters config items
--------------------------

### Parameters

```php
<?php // continued

    'parameters' => array(
        'helloworld_api_enabled' => false
    )
);
```

The parameters array define and set default values for [custom configuration parameters](#custom-config-params) specific to the plugin.

To obtain the values of these parameters, use the [`mautic.helper.core_parameters` service](#config-parameters).

<aside class="notice">
Any parameter to be written to the system's local config file should be defined here.
</aside>