Deviations from standard Symfony Framework
==========================================================

Custom directory structure
---------------------------
Mautic uses directory paths that aren't typical in Symfony to make it distributable.

.. list-table::
    :header-rows: 1

    * - Directory
      - Description
    * - ``app/bundles/``
      - Symfony bundles distributed with Core
    * - ``app/config/``
      - Symfony configuration files
    * - ``app/middlewares/``
      - See :ref:`Middlewares`
    * - ``app/migrations/``
      - Doctrine migrations that updates Core's database schema
    * - ``bin/console/``
      - Used to execute Symfony/Mautic commands
    * - ``media/``
      - Contains combined and minified production assets along with default images
    * - ``plugins/``
      - Mautic Plugins as Symfony bundles
    * - ``themes/``
      - Mautic Themes
    * - ``themes/system``
      - :ref:`Contains custom overrides for Mautic Core templates<Overriding core view templates>`
    * - ``translations/``
      - Mautic translation files leveraged by Mautic's custom :ref:`Translator`
    * - ``var/``
      - Contains temporary files such as logs and Symfony's cache
    * - ``vendor/``
      - Contains Composer installed dependencies

Mautic mostly uses Symfony's 2.x/3.x bundle structure for Core bundles in ``app\bundles\`` and custom Plugins in ``plugins\``. Read more about these :ref:`here<File and directory structure>`.

PHP everything
---------------
Mautic was originally written in PHP. YAML and Twig wasn't familiar at the time so mostly avoided. This is why Mautic used Symfony's PHP template engine by default and PHP based configurations.

.. note:: Symfony has since deprecated its PHP template engine and removed it in Symfony 5. Twig is being slowly introduced to replace PHP templates.

The goal for a PHP based config was to create a single place within the bundle to define routes, services, menus, parameters, etc rather than hunting for annotations buried throughout the app's code. Symfony's PHP configuration for registering services, parameters, routes, etc is also verbose. Therefore, Mautic provides a custom configuration framework through ``\Mautic\CoreBundle\DependencyInjection\MauticCoreExtension`` and various listeners.

Custom configuration
---------------------
Mautic built its own configuration system that services can access through Symfony parameters or ``\Mautic\CoreBundle\Helper\CoreParametersHelper``. Mautic writes configuration key/value pairs to ``app/config/local.php`` by default.

.. note:: Use Mautic's native means of managing configuration parameters, although you can define and use Symfony parameters if you want to.

Mautic 3 introduced support for Symfony's environment variables. Note that not all bundles support environment variables for Symfony's configuration so take this into account before using third party bundles. You can sometimes implement workarounds by using custom proxy or delegation services. For example, see ``\Mautic\EmailBundle\Swiftmailer\Spool\DelegatingSpool``.

Included commands
-----------------
Mautic includes it's own commands in addition to commands defined by Symfony and Symfony bundles such as the makers bundle.

Running ``./bin/console`` without any arguments outputs a list of available commands.

.. note:: Some commands are only available in the development or test environments.

Autowired services
-------------------
Mautic doesn't auto-wire native services other than Symfony commands and controllers.

Service scope
-------------
Services are public by default to have backwards compatibility with Mautic 3 and Symfony 3. You can change the scope of your service by setting ``public`` to false when defining the service in the Plugin's ``Config/config.php``.

Support for entity annotations
-------------------------------
By default, Mautic uses Doctrine's PHP driver instead of annotations which requires a ``public static function loadMetadata(ORM\ClassMetadata $metadata)`` method. However, Plugins can use annotations if desired but should use only annotations or only PHP ``loadMetadata``. A Plugin can't use a mix of both. See :ref:`Entities and schema` for more information.

Firewalls and User access management
-------------------------------------
``app/config/security.php`` lists Mautic's firewalls. For the most part, Mautic uses Symfony's standard way of registering firewalls and authentication with a means for Plugins to hook into the authentication process through listeners to the ``UserEvents::USER_PRE_AUTHENTICATION`` and ``UserEvents::USER_FORM_AUTHENTICATION`` events.

Mautic has its own permission system based on bitwise permissions and thus doesn't leverage Symfony voters.

Middlewares
------------
Mautic leverages middlewares before booting Symfony, see ``app/middlewares``. For example, ``\Mautic\Middleware\Dev\IpRestrictMiddleware`` restricts IPs access to ``index_dev.php``.

Custom Translator
------------------
Mautic has a custom translator that extends Symfony's ``Translator`` component and enables Mautic's distributable language package model. All Plugins and bundles should contain US English language strings by default. https://github.com/mautic/language-packer integrates with Transifex to create language packs stored in https://github.com/mautic/language-packs.
