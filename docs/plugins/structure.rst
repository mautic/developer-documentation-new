File and directory structure
==========================================================

The directory structure of an plugin will vary based on the features implemented.

At a minimum, the following structure is required::

    HelloWorldBundle/
        Config/
            config.php
        HelloWorldBundle.php

``HelloWorldBundle/Config/config.php`` registers the plugin with Mautic along with defining routes, menu items, services, and parameters.

The ``HelloWorldBundle.php`` file registers the bundle with Symfony's kernel. It should extend ``Mautic\IntegrationsBundle\Bundle\AbstractPluginBundle``.

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/HelloWorldBundle.php

    namespace MauticPlugin\HelloWorldBundle;

    use Mautic\IntegrationsBundle\Bundle\AbstractPluginBundle;

    class HelloWorldBundle extends AbstractPluginBundle
    {
        // Nothing more required
    }

An example plugin directory and file structure may look something like this::

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