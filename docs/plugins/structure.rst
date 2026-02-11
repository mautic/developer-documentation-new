File and directory structure
############################

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

The directory structure of a Plugin varies based on the features implemented.

Plugins require the following structure at a minimum::

    HelloWorldBundle/
        Config/
            config.php
        HelloWorldBundle.php

``HelloWorldBundle/Config/config.php`` registers the Plugin with Mautic along with defining routes, menu items, services, and parameters.

The ``HelloWorldBundle.php`` file registers the bundle with Symfony's kernel. Extend the class with ``Mautic\IntegrationsBundle\Bundle\AbstractPluginBundle``.

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/HelloWorldBundle.php

    namespace MauticPlugin\HelloWorldBundle;

    use Mautic\IntegrationsBundle\Bundle\AbstractPluginBundle;

    class HelloWorldBundle extends AbstractPluginBundle
    {
        // Nothing more required
    }

An example Plugin directory and file structure may look something like this::

    HelloWorldBundle/
        Assets/
            images/
                earth.png
                mars.png
            css/
                helloworld.css
            js/
                helloworld.js
        Config/
            config.php
        Controller/
            WorldController.php
        Entity/
            World.php
        EventListener/
            CampaignSubscriber.php
        Form/
            Type/
                WorldType.php
        Migrations/
            Version_0_0_1.php
        Model/
            WorldModel.php
        Helper/
            TravelHelper.php
        Security/
            Permissions/
                WorldPermissions.php
        Translations/
            en_US/
                flashes.ini
                messages.ini
        Tests/
            Unit/
                EventListener/
                    CampaignSubscriberTest.php
                Helper/
                    TravelHelperTest.php
            Functional/
                Controller/
                    WorldControllerTest.php
        Views/
            World/
                form.html.php
                index.html.php
                list.html.php
        HelloWorldBundle.php