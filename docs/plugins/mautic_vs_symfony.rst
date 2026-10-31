Deviations from the standard Symfony Framework
##############################################

Custom directory structure
**************************

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
      - See :ref:`plugins/mautic_vs_symfony:Middlewares`
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
      - :ref:`Contains custom overrides for Mautic Core templates<themes/system:Overriding core view templates>`
    * - ``translations/``
      - Mautic translation files leveraged by Mautic's custom :ref:`components/translator:Translator`
    * - ``var/``
      - Contains temporary files such as logs and Symfony's cache
    * - ``vendor/``
      - Contains Composer installed dependencies

Mautic mostly uses Symfony's 2.x/3.x bundle structure for Core bundles in ``app\bundles\`` and custom Plugins in ``plugins\``. Read more about these :ref:`here<plugins/structure:File and directory structure>`.

PHP everything
**************

Mautic was originally written in PHP. YAML and Twig wasn't familiar at the time so mostly avoided. This is why Mautic used Symfony's PHP template engine by default and PHP based configurations.

.. note:: Symfony has since deprecated its PHP template engine and removed it in Symfony 5. Twig has replaced nearly all of Mautic's PHP templates. Only a handful of legacy ``.html.php`` templates remain.

The goal for a PHP based config was to create a single place within the bundle to define routes, services, menus, parameters, etc rather than hunting for annotations buried throughout the app's code. Symfony's PHP configuration for registering services, parameters, routes, etc is also verbose. Therefore, Mautic provides a custom configuration framework through ``\Mautic\CoreBundle\DependencyInjection\MauticCoreExtension`` and various listeners.

Custom configuration
********************

Mautic built its own configuration system that services can access through Symfony parameters or ``\Mautic\CoreBundle\Helper\CoreParametersHelper``. Mautic writes configuration key/value pairs to ``app/config/local.php`` by default.

.. note:: Use Mautic's native means of managing configuration parameters, although you can define and use Symfony parameters if you want to.

Mautic 3 introduced support for Symfony's environment variables. Note that not all bundles support environment variables for Symfony's configuration so take this into account before using third party bundles. You can sometimes implement workarounds by using a custom environment variable processor. For example, see ``\Mautic\EmailBundle\DependencyInjection\EnvProcessor\MailerDsnEnvVarProcessor``.

Included commands
-----------------
Mautic includes its own commands in addition to commands defined by Symfony and Symfony bundles such as the makers bundle.

Running ``./bin/console`` without any arguments outputs a list of available commands.

.. note:: Some commands are only available in the development or test environments.

Autowired services
******************

Every core bundle and Plugin's ``Config/services.php`` loads its own namespace with Symfony's ``->autowire()`` and ``->autoconfigure()``, so Mautic autowires nearly all services, not just commands and controllers. See :doc:`/plugins/autowiring` for details.

Service scope
*************

Services are public by default to have backwards compatibility with Mautic 3 and Symfony 3. You can change the scope of your service by calling ``->private()`` instead of ``->public()`` when defining the service in the Plugin's ``Config/services.php``.

Support for entity annotations
******************************
By default, Mautic uses Doctrine's PHP driver instead of annotations which requires a ``public static function loadMetadata(ORM\ClassMetadata $metadata)`` method. However, Plugins can use annotations if desired but should use only annotations or only PHP ``loadMetadata``. A Plugin can't use a mix of both. See :ref:`plugins/data:Entities and schema` for more information.

Firewalls and User access management
************************************
``app/config/security.php`` lists Mautic's firewalls. For the most part, Mautic uses Symfony's standard way of registering firewalls and authentication with a means for Plugins to hook into the authentication process by subscribing to the ``Mautic\UserBundle\Event\PreAuthenticationEvent`` and ``Mautic\UserBundle\Event\FormAuthenticationEvent`` events.

Mautic has its own permission system based on bitwise permissions and thus doesn't leverage Symfony voters.

Middlewares
***********

Mautic leverages middlewares before booting Symfony, see ``app/middlewares``. For example, ``\Mautic\Middleware\Dev\IpRestrictMiddleware`` restricts IP address access to ``index_dev.php``.

Custom Translator
*****************

Mautic has a custom Translator that extends Symfony's ``Translator`` component and enables Mautic's distributable language package model. All Plugins and bundles should contain US English language strings by default. https://github.com/mautic/language-packer integrates with Transifex to create language packs stored in https://github.com/mautic/language-packs.
