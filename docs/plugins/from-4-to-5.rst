Update plugins for Mautic 5
=======================================

Here is a list of steps that most of the Plugins may need to take to upgrade from Mautic 4 to Mautic 5. You should be able to get through each step, make a commit, move to the next one and once you are at finished you have upgraded your Plugin.

Continuous Integration
-------------------------

If you don't have CI configured, this is the time to do it. This is an optional step but it makes sense to do it at the beginning rather than later. Here's how to get it done: :doc:`/plugins/continuous-integration`.

In your PR add also support for PHP 8.1 and 8.2, and upgrade the Mautic version from 4.4 to 5.1. One more thing is that Mautic 5 have ``local.php`` in ``config/local.php`` instead of ``app/config/local.php`` so update that as well.

Autowiring
-------------

Mautic 5 comes with autowiring of PHP services which means the developer experience is much improved, and the code size is reduced.

There is a great doc already written on this topic: :doc:`/plugins/autowiring` - so refer to that for instructions.

To quickly verify that the wiring of services is complete and configured correctly you may find this command faster than refreshing the browser window:

``rm -rf var/cache && bin/console``

  .. note:: Ideally, you should be able to delete the whole ``services`` section from your ``config.php`` file, but do that as a cherry on top once you are sure everything is working as the later steps in this process may yet cause you difficulties.

``config.php`` - controllers
---------------------------

``config.php`` should be much lighter now when all services are gone after autowiring is configured. There is one more thing to verify. The controllers are now defined with a different syntax. Here is an example:

.. code:: diff

   - 'controller' => 'CronfigBundle:Cronfig:index',
   + 'controller' => 'MauticPlugin\CronfigBundle\Controller\CronfigController::indexAction'

Symfony 5 is much more explicit. That's a good thing even if it's longer. You don't have to guess what the syntax is. It's basically just standard FQCN (Fully Qualified Class Name) with the full method name behind the 2 colons. You don't even need to call the controller method `*Action` any more.

Rendering views
------------------

As Symfony 5 removed the PHP templating engine, Mautic had to switch to Twig. Your Plugin must also update the any views from PHP to Twig. Here is a helpful resource on how to migrate the ``*.html.php`` files to ``*.html.twig`` files:

:xref:`PHP to Twig migration`

In the controllers, you'll also have to update the view paths like this:

.. code:: diff

   - $this->renderView('MauticCoreBundle:Notification:flash_messages.html.php');
   + $this->renderView('@MauticCore/Notification/flash_messages.html.twig');

Running this command is faster than refreshing all the views in the browser. It validates the Twig syntax and can guide you through the process:

``bin/console lint:twig plugins/MyBundle``

.. note:: Update MyBundle with your bundle name.

.. vale off

The Integration class
------------------------

.. vale on


If you went ahead and deleted all services from ``config.php``, you may experience problems if you're using Mautic's Integration classes and interfaces. The inner workings of the IntegrationsBundle expects that your Integration has a service key in a specific format. Mautic 6 aims to improve this, but for now, add an alias to ``services.php``:

.. code:: php

   $services->alias('mautic.integration.[MY_INTEGRAION]', \MauticPlugin\[MY_INTEGRAION]Bundle\Integration\[MY_INTEGRAION]Integration::class);

.. note:: Replace `[MY_INTEGRAION]` with your Plugin name.

Compiler passes
------------------

If your Plugin uses a compiler pass, you may have to verify that it works correctly. In many cases you may have to change the service alias with FQCN like so:

.. code:: diff

   - ->setDecoratedService('mautic.form.type.email', 'mautic.form.type.email.inner');
   + ->setDecoratedService(EmailType::class, 'mautic.form.type.email.inner')

Getting container in tests
-----------------------------

This one is a quick find and replace:

.. code:: diff

   - $handlerStack = self::$container->get('mautic.http.client.mock_handler');
   + $handlerStack = static::getContainer()->get(MockHandler::class);

Notice you can also use FQCN instead of string service keys which is more convenient.

Automated refactoring
------------------------

Your Plugin should be working on Mautic 5 by now. Wouldn't it be great to shorten the code a little more? Mautic 5 uses PHP 8.0+ so can take advantage of the syntax. Rector can upgrade the code for you.

Run ``bin/rector process plugins/MyBundle`` and review the changes.

.. note:: Update MyBundle with your bundle name.

Automated code style
-----------------------

Another great way how to improve your Plugin code base quality is to run the CS Fixer: ``bin/php-cs-fixer fix plugins/MyBundle``.

.. note:: Update MyBundle with your bundle name.

Static analysis
-------------------

PHPSTAN is another amazing tool that detects bugs for you. It's better to run it on the whole codebase including core Mautic, so it's aware of all classes.

Run ``composer phpstan``

If your Plugin has more PHPSTAN errors than you can handle right now, consider using [PHPSTAN baseline](https://phpstan.org/user-guide/baseline). It allows you to store your tech debt to a single file and it forces you to write better code from now on. And you can reduce the baseline by small chunks every month to get to 0.

Conclusion
----------

This list of steps is compiled by Mautic Plugin developers for the Mautic Plugin developers. If you find that some common problem isn't addressed here, please add it.
