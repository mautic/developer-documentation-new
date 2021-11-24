Deviations from standard Symfony Framework
==========================================================

Custom directory structure
---------------------------
Mautic uses some directory paths that are not typical in Symfony in order to make it distributable and pluggable.

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
      - Mautic plugins as Symfony bundles
    * - ``themes/``
      - Mautic themes
    * - ``themes/system``
      - :ref:`Contains custom overrides for Mautic Core templates<Overriding core view templates>`
    * - ``translations/``
      - Mautic translation files leveraged by Mautic's custom :ref:`Translator`
    * - ``var/``
      - Contains temporary files such as logs and Symfony's cache
    * - ``vendor/``
      - Contains Composer installed dependencies

Mautic mostly uses Symfony's 2.x/3.x bundle structure for Core bundles in ``app\bundles\`` and custom plugins in ``plugins\``. Read more about these :ref:`here<File and directory structure>`.

PHP everything
---------------
Mautic was originally written in PHP. Yaml and twig wasn't familiar at the time so mostly avoided. This is why Mautic used Symfony's PHP template engine by default and PHP based configurations.

.. note:: Symfony has since deprecated its PHP template engine and removed it in Symfony 5. Twig is being slowly introduced to replace PHP templates.

The goal for a PHP based config was to create a single place within the bundle to define routes, services, menus, parameters, etc rather than hunting for annotations buried throughout the application's code. Symfony's PHP configuration for registering services, parameters, routes, etc is verbose so a custom configuration framework was written that is parsed by various listeners and ``\Mautic\CoreBundle\DependencyInjection\MauticCoreExtension``.

Custom configuration
---------------------
Mautic has its own configuration system that is built on top of Symfony parameters and utilized in the application through the ``\Mautic\CoreBundle\Helper\CoreParametersHelper``. Configuration key/values are written to ``app/config/local.php`` by default.

.. warning:: Although you can define and use Symfony parameters, it is recommended to use Mautic's native means of managing configuration parameters.

In Mautic 3, the configuration was refactored to use Symfony's support environment variables. Note that not all bundles support environment variables for Symfony's configuration so this has to be taken into account before using third party bundles. Sometimes it can be worked around by using custom proxy or delegation services. For example, see ``\Mautic\EmailBundle\Swiftmailer\Spool\DelegatingSpool``.

Autowired services
-------------------
Mautic does not auto-wire native services other than Symfony commands and controllers.

Service scope
-------------
Services are registered as public by default to have backwards compatibility with Mautic 3 and Symfony 3. You can change the scope of your service by setting ``public`` to false when defining the service in the plugin's ``Config/config.php``.

Entity annotations
-------------------
By default, Mautic uses Doctrine's PHP driver instead of annotations which requires a ``public static function loadMetadata(ORM\ClassMetadata $metadata)`` method. However, plugins can use annotations if desired but should use only annotations or only PHP ``loadMetadata``. A plugin cannot use a mix of both.

Firewalls and user access management
-------------------------------------
The firewalls registered with Symfony are listed in ``app/config/security.php``. For the most part, we use Symfony's standard way of registering firewalls and authentication with a means for plugins to hook into the authentication process through listeners to the ``UserEvents::USER_PRE_AUTHENTICATION`` and ``UserEvents::USER_FORM_AUTHENTICATION`` events.

Mautic has its own permission system based on bitwise permissions and thus does not leverage Symfony voters.

Middlewares
------------
Mautic leverages middlewares before booting Symfony, see ``app/middlewares``. For example, ``index_dev.php`` is restricted by IP through ``\Mautic\Middleware\Dev\IpRestrictMiddleware``.

Custom Translator
------------------
Mautic has a custom translator that extends Symfony's ``Translator`` component that enables Mautic's distributable language package model. All plugins and bundles should contain US English language strings by default. Translations are managed via Transifex of which https://github.com/mautic/language-packer integrates to create language packs stored in https://github.com/mautic/language-packs.
