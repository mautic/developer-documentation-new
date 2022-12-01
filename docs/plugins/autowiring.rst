Autowiring
##########

Mautic 5 adds support for Symfony's :xref:`symfony-autowiring` and :xref:`symfony-autoconfigure` for services.

Earlier versions required defining services in the ``*Bundle/Config/config.php`` file. This still works in Mautic 5, but won't work in Mautic 6 as it's due for removal. 

Follow these steps to migrate from hard-coded services to autowired services.

Advantages
**********

-  New services no longer need to have any definition in the ``app/bundles/*Bundle/Config/config.php``. The same is true for Plugins. Symfony will guess what services are needed in the services by types of arguments in the constructor.
-  If services aren't used in other services as dependencies, they're deleted, like **subscribers**, **commands** and **form types**.
-  You can reduce existing service definitions to setting just the string alias, to maintain backward compatibility and keep controllers working.
-  ``app/config/services.php`` automatically configures all bundles including Plugins so if the bundle doesn't do anything unusual, it should work out of the box.
-  The legacy services definitions are in the ``*Bundle/Config/config.php`` file , but in Mautic 6 this is due for removal.

The same applies for Plugins as well as for the core bundles.

Introducing ``services.php``
****************************

``*Bundle/Config/services.php`` is the right place to store special cases of PHP services. Mautic is getting closer to Symfony's default app by doing this. The ideal state at the end of life of Mautic 5 is that all services are either autowired or defined in the ``services.php`` file.

If your Plugin doesn't have this file, it uses the :xref:`default_services_config`.  It excludes classic directories that a Mautic bundle should exclude, and autowires entity repositories as services for you.

However, every bundle should have its own ``services.php`` as each bundle is responsible for defining its services. A basic ``services.php`` file looks like this:

.. code:: php

   <?php

   declare(strict_types=1);

   use Mautic\CoreBundle\DependencyInjection\MauticCoreExtension;
   use Symfony\Component\DependencyInjection\Loader\Configurator\ContainerConfigurator;

   return function (ContainerConfigurator $configurator) {
       $services = $configurator->services()
           ->defaults()
           ->autowire()
           ->autoconfigure()
           ->public();

       $excludes = [
           'SomeDirectoryYouWantToExclude',
       ];

       $services->load('MauticPlugin\\[YourPluginName]Bundle\\', '../')
           ->exclude('../{'.implode(',', array_merge(MauticCoreExtension::DEFAULT_EXCLUDES, $excludes)).'}');
   };

.. note::
   Replace ``[YourPluginName]`` with your Plugin name

This allows you to state that bundle services are autowired and autoconfigured. All services shouldn't be public by default, but Controllers and other old services load dependencies
directly from the container instead of using dependency injection via constructor. More on that below.

You can define directories or files you wish to exclude in the ``$excludes`` array. They're later merged with all directories excluded by default and stored in the ``MauticCoreExtension::DEFAULT_EXCLUDES`` constant.

If you wish to load entity repositories as services you can do so with this line:

.. code:: php

   $services->load('MauticPlugin\\[YourPluginName]Bundle\\Entity\\', '../Entity/*Repository.php');

Most Mautic bundles keep entities - DTO objects - and repositories - services - in one directory, hence taking this approach. Excluding the Entity directory by default, now you must select only the files ending with ``Repository.php`` and load those as services.

In order to use the ``services.php`` file you have to create an Extension file for your bundle. Here is an example:

.. code:: php

   // *Bundle/DependencyInjection/[YourPluginName]Extension.php
   <?php

   declare(strict_types=1);

   namespace MauticPlugin\[YourPluginName]Bundle\DependencyInjection;

   use Symfony\Component\Config\FileLocator;
   use Symfony\Component\DependencyInjection\ContainerBuilder;
   use Symfony\Component\DependencyInjection\Extension\Extension;
   use Symfony\Component\DependencyInjection\Loader\PhpFileLoader;

   class Mautic[YourPluginName]Extension extends Extension
   {
       /**
        * @param mixed[] $configs
        */
       public function load(array $configs, ContainerBuilder $container): void
       {
           $loader = new PhpFileLoader($container, new FileLocator(__DIR__.'/../Config'));
           $loader->load('services.php');
       }
   }

The naming is very important for Mautic to be able to use this file. It must be in the ``DependencyInjection`` directory and you must name it the same as the main bundle class in the bundle's root directory. So if you have named that file for example ``MauticConfigBundle.php`` then you must name this new file ``DependencyInjection/MauticConfigExtension.php``.  

Replace ``Bundle.php`` with ``Extension.php`` and you get the name of this new file.

Why exclude directories from autowiring?
****************************************

If you don't exclude directories from autowiring, Symfony tries to autowire all PHP classes, which fails in some cases. For example DTO or value object classes shouldn't be autowired. They're created during the app's execution, and aren't meant to be services. Such classes are for example entities or events. Here is the full list of directories :xref:`excluded_directories`.

How to migrate?
***************

You'll enjoy the work as long as you like to remove unnecessary code.

.. vale off

Remove Commands, Subscribers and Forms
======================================
.. vale on

A fun fact is that **commands** were autowired since Mautic 3. So you can remove them from ``config.php``, remove the cache and they work as before.

With Mautic 5 you can remove service definitions for **subscribers** and **forms** as well as they're not used as dependencies for other services.

Consider backward compatibility for services
============================================

For core bundles it's important to care about backward compatibility and maintain the service aliases. If you're a Plugin developer you can jump directly into using Fully Qualified Class Names (FQCN) instead. If you do this, release the new Plugin version as a major release to warn users of your Plugin. You never know how people use your Plugin in production.

In core bundles, keep the service aliases. So with a service definition like this:

.. code:: php

   // config.php
   'mautic.campaign.model.campaign' => [
       'class'     => \Mautic\CampaignBundle\Model\CampaignModel::class,
       'arguments' => [
           'mautic.lead.model.list',
           'mautic.form.model.form',
           'mautic.campaign.event_collector',
           'mautic.campaign.membership.builder',
           'mautic.tracker.contact',
       ],
   ],

You can remove all the preceding code, and create the alias like this:

.. code:: php

   // services.php
   $services->alias('mautic.campaign.model.campaign', \Mautic\CampaignBundle\Model\CampaignModel::class);

You can skip the step of creating aliases, delete all services definitions from ``config.php`` and replace all string service definitions wherever they're loaded directly from the container like this:

.. code:: diff

   - $container->get('mautic.campaign.model.campaign');
   + $container->get(\Mautic\CampaignBundle\Model\CampaignModel::class);

Use interfaces over implementation
==================================

Symfony complains if you use for example ``Http\Adapter\Guzzle7\Client`` as a dependency in your service instead of its interface ``Psr\Http\Client\ClientInterface``. Don't worry, it tells you exactly that in the error message.

Special cases
=============

Some services don't need only other services as dependencies but sometimes parameters. Consider for example a service like this:

.. code:: php

   // config.php
   'mautic.config.form.escape_transformer' => [
       'class'     => \Mautic\ConfigBundle\Form\Type\EscapeTransformer::class,
       'arguments' => [
           '%mautic.config_allowed_parameters%',
       ],
   ],

If you delete this definition and let the autowiring to take care of it then you get this nice error message:

::

   Cannot autowire service "Mautic\ConfigBundle\Form\Type\EscapeTransformer": argument "$allowedParameters" of method "__construct()" is type-hinted "array", you should configure its value explicitly.

It doesn't know what array argument to send there. So you have to define it:

.. code:: php

   // services.php
   $services->get(\Mautic\ConfigBundle\Form\Type\EscapeTransformer::class)->arg('$allowedParameters', '%mautic.config_allowed_parameters%');

The big advantage is that Mautic is getting closer to a standard Symfony app with autowiring, so all these special cases are nicely documented by
the :xref:`manually_wiring_arguments`.

.. vale off

Dependency Injection in Controllers
===================================

.. vale on

Controllers are still using the container to get dependencies. Refactoring of the other services to use proper dependency injection is complete already, so this is the next project. The goal is to use :xref:`action_based_di` and for the new controllers consider :xref:`invokable_controllers`.

The problem with Mautic controllers are that there are many layers of abstraction. These abstractions must move to their own services to make the controllers as light as possible.
