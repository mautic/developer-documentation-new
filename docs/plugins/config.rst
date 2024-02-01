Config file
###########

Mautic leverages a simple array based config file to register routes, menu items, services, Categories, and configuration parameters.

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

    // ...

Routing firewalls
=================

The following firewalls are available to routes.

.. list-table::
    :header-rows: 1

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
      - Defines the controller and function to call when the path matches. There are three supported formats. The legacy string format, ``HelloWorldBundle:World:hello``, executes ``MauticPlugin\HelloWorldBundle\Controller\WorldController::helloAction()``. The recommended format starting in Mautic 4 is either ``[MauticPlugin\HelloWorldBundle\Controller\WorldController::class, 'hello']`` that executes ``MauticPlugin\HelloWorldBundle\Controller\WorldController::hello()`` or  ``MauticPlugin\HelloWorldBundle\Controller\WorldController::class`` that executes ``MauticPlugin\HelloWorldBundle\Controller\WorldController::__invoke()``.
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

Configure custom routes through writing a listener to the ``\Mautic\CoreBundle\CoreEvents::BUILD_ROUTE`` event. Listeners to this event receives a ``Mautic\CoreBundle\Event\RouteEvent`` object. Mautic dispatches an event for each firewall when compiling routes.

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
    * - ``php app/console router:debug``
      - Lists all registered routes.
    * - ``php app/console router:debug article_show``
      - Lists the definition for the route ``article_show``.
    * - ``php app/console router:match /blog/my-latest-post``
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

    * - Key
      - Is required?
      - Type
      - Description
    * - ``route``
      - conditional
      - string
      - Name of the :ref:`Routing config items<plugins/config:Route definitions>` for this item. Leave undefined if the item is a placeholder for a sub-menu.
    * - ``routeParameters``
      - no
      - array
      - Key/value pairs of :ref:`path parameters<plugins/config:Route definitions>` for the given ``route``.
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

Service config items
********************

Services define the Plugin's classes and their dependencies with Mautic and Symfony. Services defined within specific keys are auto-tagged as noted below.

.. code-block:: php

    <?php

    // ...

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

    // ...

Service types
=============

For convenience, Mautic auto-tags services defined within specific keys.

.. list-table::
    :header-rows: 1

    * - Key
      - Tag
      - Description
    * - ``command`` or ``commands``
      - ``console.command``
      - Registers the service with :xref:`Symfony as a console command<Symfony console command tag>`.
    * - ``controllers``
      - ``controller.service_arguments``
      - Controllers are typically autowired by Symfony. However, you can register :xref:`controllers as services<Symfony controller service arguments tag` to manage your own dependency injection rather than relying on Symfony's service container.
    * - ``events``
      - ``kernel.event_subscriber``
      - Registers the service with :xref:`Symfony as an event subscriber<Symfony event subscriber tag>`.
    * - ``forms``
      - ``form.type``
      - Registers the service with :xref:`Symfony as a custom form field type<Symfony custom form field type tag>`.
    * - ``models``
      - ``mautic.model``
      - Deprecated. Use service dependency injection instead.
    * - ``permissions``
      - ``mautic.permissions``
      - Registers the service with Mautic's :ref:`permission service<security-roles-and-permissions>`.
    * - ``*`` or ``other``
      - n/a
      - You can use any other key you want to organize services in the config array. Note that this could risk incompatibility with a future version of Mautic if using something generic that Mautic starts to use as well.

Service definitions
===================

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
      - Array of services, parameters, booleans, or strings injected as arguments into this service's construct. Wrap parameter names in ``%`` signs, for example, ``'%mautic.some_parameter%',``. Hard coded strings need to be wrapped in ``"`` signs, for example, ``'"some string"',``. Any other string is assumed to be the name of a defined service.
    * - ``alias``
      - conditional
      - string
      - Used by specific types of services. For example, services defined under ``helpers`` use this as the key in the ``$view`` variable to access the defined service from PHP templates. Otherwise, it defines an alternate name for the service.
    * - ``serviceAlias``
      - no
      - string
      - Define an alias for this service in addition to the name defined as the service's key. Note that Mautic sets the service's class name as an alias by default.
    * - ``serviceAliases``
      - no
      - array
      - Define multiple aliases for this service in addition to the name defined as the service's key. Note that the service's class name is set as an alias by default.
    * - ``tag``
      - no
      - string
      - Define a :xref:`tag used by Symfony when compiling the container<Symfony service tags>`. See :ref:`plugins/config:Mautic service tags` for Mautic specific tags.
    * - ``tags``
      - no
      - array
      - An array of tags when there are more than one. See :ref:`plugins/config:Mautic service tags` for Mautic specific tags. This supersedes ``tag``.
    * - ``tagArguments``
      - no
      - array
      - Some tags have special arguments definable through an array of tagArguments. If using ``tag``, this should be a key/value pair of the arguments specific to the given tag. For example, ``['tag' => 'tag1', 'tagArguments' => ['tag1-key' => 'tag1-value'],],``. If using ``tags``, this should be an array of arrays keyed the same as the values of ``tags``. For example, ``['tags' => [ 'tag1', 'tag2'], 'tagArguments' => [['tag1-key' => 'tag1-value'],['tag2-key' => 'tag2-value'],],],``.
    * - ``factory``
      - no
      - array
      - Define a factory to create this service. For example, ``'factory' => ['@doctrine.orm.entity_manager', 'getRepository'],``. See :xref:`Symfony factories`.
    * - ``methodCalls``
      - no
      - array[]
      - Define methods to call after the service is instantiated. Use an array of arrays with keys as the method name and values the arguments to pass into the given method. For example,  ``['methodCalls' => ['setSecurity' => ['mautic.security'],],],``.
    * - ``decoratedService``
      - no
      - string
      - Name of another service to override and decorate. The original service becomes available as ``thisServiceName.inner``  to this or others services. See :xref:`Symfony service decoration`.
    * - ``public``
      - no
      - boolean
      - Defines the service as public and accessible through the service container. By default, all Mautic services are public. Set this to ``FALSE`` to make the service private instead.
    * - ``synthetic``
      - no
      - boolean
      - Configure the service as synthetic meaning it gets set during run time. See :xref:`Symfony synthetic services`.
    * - ``file``
      - no
      - string
      - Include the specified file prior to loading the service. Symfony uses PHP's ``require_once``. See :xref:`Symfony requiring a file before loading a service`.
    * - ``configurator``
      - no
      - array|string
      - Callable to use as a configurator to configure the service after its instantiation. See :xref:`Symfony service configurators`.
    * - ``abstract``
      - no
      - boolean
      - Configure this service as an abstract/parent service. Symfony ignores this until Mautic addresses https://forum.mautic.org/t/support-symfony-abstract-parent-services/21922.
    * - ``lazy``
      - no
      - boolean
      - Define the service with lazy loading. Symfony ignores this until Mautic addresses https://forum.mautic.org/t/supporty-symfony-lazy-services/21923.

Mautic service tags
-------------------

Mautic uses the follow tags to register services as described below.

**Channel tags**

.. list-table::
    :header-rows: 1

    * - Tag
      - Supported tag arguments
      - Description
    * - ``mautic.sms_transport``
      - ``['integrationAlias' => 'Name to display in the UI for this transport.']``
      - Register this service as a Text Message transport.
    * - ``mautic.sms_callback_handler``
      - none
      - Registers this service to handle webhooks from a Text Message transport.
    * - ``mautic.email_transport``
      - Key/value pairs to configure fields required to authenticate with the transport's service. See :ref:`components/emails:Email transports`.
      - Registers the service as an :ref:`Email transport<components/emails:Email transports>`.
    * - ``mautic.email_stat_helper``
      - none
      - Registers the service as a stat helper for Email charts. See :ref:`components/emails:Email stat helpers`.

**Core tags**

.. list-table::
    :header-rows: 1

    * - Tag
      - Supported tag arguments
      - Description
    * - ``mautic.permissions``
      - none
      - Registers the service as a permission object that must extend ``\Mautic\CoreBundle\Security\Permissions\AbstractPermissions``. See :ref:`security-roles-and-permissions`. Services under the ``['services']['permissions']`` array do not require this.

**Integration tags**

.. list-table::
    :header-rows: 1

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