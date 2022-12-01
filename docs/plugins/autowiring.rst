Autowiring
==========

Mautic 5 adds support for Symfony's
`autowiring <https://symfony.com/doc/5.4/service_container/autowiring.html>`__
and
`autoconfigure <https://symfony.com/doc/5.4/service_container.html#the-autoconfigure-option>`__
for services.

Earlier versions required to define services in the
``*Bundle/Config/config.php`` file. This functionality is still working
in Mautic 5 but will be removed in Mautic 6. Let's go through the steps
to migrate from hard-coded services to autowired services.

Advantages
----------

-  New services no longer need to have any definition in the
   app/bundles/*Bundle/Config/config.php. Same for plugins. Symfony will
   guess what services are needed in the services by types of arguments
   in the constructor.
-  Services that aren't used in other services as dependencies like
   **subscribers**, **commands** and **form types** were deleted
   completely.
-  Existing service definitions can be reduced to setting just the
   string alias to keep backward compatibility and controllers working.
-  ``app/config/services.php`` is automatically configuring all bundles
   including plugins so if the bundle doesn't do anything uncommon then
   it should work out of the box.
-  The legacy services definitions in ``*Bundle/Config/config.php`` file
   are still working but will be removed in Mautic 6.

The same applies for plugins as well as for the core bundles.

.. _introducing-servicesphp:

Introducing ``services.php``
----------------------------

``*Bundle/Config/services.php`` is the right place where to store
special cases of PHP services. We are getting closer to Symfony's
default app by doing this. The ideal state at the end of life of Mautic
5 is that all services are either autowired or defined in the
``services.php`` file.

If your plugin does not have this file, it will use the `default
configuration <https://github.com/mautic/mautic/blob/5.x/app/config/services.php>`__.
It will exclude classic directories that a Mautic bundle should exclude
and autowire entity repositories as services for you.

However, every bundle should have its own ``services.php`` as each
bundle is responsible for defining it's services. A basic services.php
file looks like this:

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

*Replace ``[YourPluginName]`` with your plugin name*

It allows you to state that bundle services are autowired and
autoconfigured. All services should not be public by default but we do
so because of Controllers and other old services that load dependencies
directly from the container instead of using dependency injection via
constructor. More on that bellow.

Then you can define directories or files you wish to exclude in the
``$excludes`` array. They are later merged with all directories excluded
by default and stored in the ``MauticCoreExtension::DEFAULT_EXCLUDES``
constant.

If you wish to load entity repositories as services you can do so with
this line:

.. code:: php

   $services->load('MauticPlugin\\[YourPluginName]Bundle\\Entity\\', '../Entity/*Repository.php');

It must be done like this because Most Mautic bundles keep entities (DTO
objects) and repositories (services) in one directory. So the Entity
directory is excluded by default and we have to select only the files
ending with ``Repository.php`` and load those as services.

In order to make the ``services.php`` file alive you have to create an
Extension file for your bundle. Here is an example:

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

The naming is very important for this file to be used. It must be in the
``DependencyInjection`` directory and it must be called the same as the
main bundle class in the bundle's root directory. So if that file is
called for example ``MauticConfigBundle.php`` then this new file must be
called ``DependencyInjection/MauticConfigExtension.php``. Just replace
``Bundle.php`` with ``Extension.php`` and you get the name of this new
file.

Why excluding directories from autowiring?
------------------------------------------

Because otherwise Symfony tries to autowire all PHP classes. And it will
fail in some cases. For example DTO or value object classes should not
be autowired. They are meant to be created during the app's execution.
They are not meant to be services. Such classes are for example entities
or events. Here is the full list of directories excluded by default:

`https://github.com/mautic/mautic/blob/5.x/app/bundles/CoreBundle/DependencyInjection/MauticCoreExtension.php#L12 <https://github.com/mautic/mautic/blob/5.x/app/bundles/CoreBundle/DependencyInjection/MauticCoreExtension.php#L12>`__

How do I migrate?
-----------------

You'll enjoy the work as long as you like to remove unnecessary code!

Remove Commands, Subscribers, Forms right away
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fun fact is that **commands** were autowired since Mautic 3. So you can
remove them from ``config.php``, remove cache and they will work as
before.

With Mautic 5 you can remove service definitions for **subscribers** and
**forms** as well becuase they are not used as dependencies for other
services.

Consider backward compatibility for services
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For core bundles we have to care about backward compatibility and keep
the service aliases. If you are a plugin developer you can jump directly
into using Fully Qualified Class Names (FQCN) instead. But release this
new plugin version as a major release just to warn users. You never know
your plugin is being used.

In core bundles we'll keep the service aliases. So if we have a service
definition like this:

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

We can remove all that code above and create the alias like this:

.. code:: php

   // services.php
   $services->alias('mautic.campaign.model.campaign', \Mautic\CampaignBundle\Model\CampaignModel::class);

You can skip the step of creating aliases, delete all services
definitions from ``config.php`` and replace all string service
definitions wherever they are loaded directly from the container like
this:

.. code:: diff

   - $container->get('mautic.campaign.model.campaign');
   + $container->get(\Mautic\CampaignBundle\Model\CampaignModel::class);

Use interfaces over implementation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Symfony will complain if you use for example
``Http\Adapter\Guzzle7\Client`` as a dependency in your service instead
of its interface ``Psr\Http\Client\ClientInterface``. Don't worry, it
will tell you exacely that in the error message.

Special cases
~~~~~~~~~~~~~

Some services do not need only other services as dependencies but
sometimes parameters. Consider for example a service like this:

.. code:: php

   // config.php
   'mautic.config.form.escape_transformer' => [
       'class'     => \Mautic\ConfigBundle\Form\Type\EscapeTransformer::class,
       'arguments' => [
           '%mautic.config_allowed_parameters%',
       ],
   ],

If you delete this definition and let the autowiring to take care of it
then you get this nice error message:

::

   Cannot autowire service "Mautic\ConfigBundle\Form\Type\EscapeTransformer": argument "$allowedParameters" of method "__construct()" is type-hinted "array", you should configure its value explicitly.

It doesn't know what array argument to send there. So we have to define
it:

.. code:: php

   // services.php
   $services->get(\Mautic\ConfigBundle\Form\Type\EscapeTransformer::class)->arg('$allowedParameters', '%mautic.config_allowed_parameters%');

The big advantage is that we are getting closer to a standard Symfony
app with autowiring so all these special cases are nicely documented by
the `Symfony
docs <https://symfony.com/doc/5.4/service_container.html#manually-wiring-arguments>`__.

Dependency Injection in Controllers
-----------------------------------

Controllers are still using container to get dependencies. We've
refactor most of other services to use proper DI. So this will be the
next project. The goal is to use `action-based
DI <https://symfony.com/doc/5.4/controller.html#controller-accessing-services>`__
and for the new controllers consider `invokable
controllers <https://symfony.com/doc/5.4/controller/service.html#invokable-controllers>`__.

The problem with Mautic controllers are many layers of abstraction.
These abstractions will have to be moved to their own services to make
the controllers as light as they should be.
