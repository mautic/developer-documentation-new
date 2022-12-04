Configuration
#############

For basic information about configuring your Plugin, see :ref:`Config file`. This document goes into more detail by explaining how to add User-configurable options to Mautic.

Configuration parameters
************************

You can find Mautic's configuration in ``app/config/local.php``. Plugins can leverage custom config parameters to use within its code.

You can define every configuration option you need. Make sure it has a default set in the :ref:`Plugin's config file<Config file>`.
This prevents Symfony from throwing errors if the parameter gets used during cache compilation or if accessed directly from the container without checking if it exists first.
Defining the parameters in the Plugin's config file ensures that it always exists.

To add config options to the Configuration section, you will need to add an :ref:`Event Listener<Event listeners>`, a config  :ref:`form type<Forms>`, and a specific view (TODO).

.. note:: To translate the Plugin's tab in the configuration Form, be sure to include ``mautic.config.tab.helloworld_config`` in the Plugin's messages.ini file. Replace helloworld_config with whatever you use as the ``formAlias`` when registering the Form in the event subscriber. You can find more on this below.

.. vale off

Config Event Subscriber
=======================

.. vale on

The event subscriber should listen to the ``ConfigEvents::CONFIG_ON_GENERATE`` and ``ConfigEvents::CONFIG_PRE_SAVE`` events.  

The ``ConfigEvents::CONFIG_ON_GENERATE`` is dispatched when the configuration form is built giving the plugin an opportunity to inject it's own tab and config options.

To do this, the Plugin must register it's configuration details through the method assigned to the ``ConfigEvents::CONFIG_ON_GENERATE`` event.
The ``\Mautic\ConfigBundle\Event\ConfigBuilderEvent`` object gets passed into the method and expects the method to call ``addForm()``. ``addForm()`` expects an array with the following elements:

.. list-table::
   :header-rows: 1

   * - Key
     - Description
   * - ``formAlias``
     - Alias of the Form type class that sets the expected Form elements
   * - ``formTheme``
     - View to format the configuration Form elements, i.e, ``HelloWorldBundle:FormTheme\Config``
   * - ``parameters``
     - Array of custom config elements. ``$event->getParametersFromConfig('HelloWorldBundle')))`` can be used to glean them from the plugin's config file.


The ``ConfigEvents::CONFIG_PRE_SAVE`` is called before the values from the form are rendered and saved to the ``local.php`` file.
This gives the Plugin an opportunity to clean up or manipulate the data before it's written.

Remember that you must register the subscriber through the Plugin's config in the ``services[events]`` :ref:`section<Service config items>`.

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/EventListener/ConfigSubscriber.php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Mautic\ConfigBundle\Event\ConfigEvent;
    use Mautic\ConfigBundle\ConfigEvents;
    use Mautic\ConfigBundle\Event\ConfigBuilderEvent;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    class ConfigSubscriber implements EventSubscriberInterface
    {
        static public function getSubscribedEvents()
        {
            return [
                ConfigEvents::CONFIG_ON_GENERATE => ['onConfigGenerate', 0],
                ConfigEvents::CONFIG_PRE_SAVE    => ['onConfigSave', 0]
            ];
        }

        public function onConfigGenerate(ConfigBuilderEvent $event)
        {
            $event->addForm(
                [
                    'formAlias'  => 'helloworld_config',
                    'formTheme'  => 'HelloWorldBundle:FormTheme\Config',
                    'parameters' => $event->getParametersFromConfig('HelloWorldBundle')
                ]
            );
        }

        public function onConfigSave(ConfigEvent $event)
        {
            $values = $event->getConfig();

            // Manipulate the values
            if (!empty($values['helloworld_config']['custom_config_option'])) {
                $values['helloworld_config']['custom_config_option'] = htmlspecialchars($values['helloworld_config']['custom_config_option']);
            }

            // Set updated values 
            $event->setConfig($values);
        }
    }

.. vale off

Config Form
===========

.. vale on

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/Form/Type/ConfigType.php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\Form\Type;

    use Symfony\Component\Form\AbstractType;
    use Symfony\Component\Form\FormBuilderInterface;

    class ConfigType extends AbstractType
    {
        public function buildForm(FormBuilderInterface $builder, array $options)
        {
            $builder->add(
                'custom_config_option',
                'text',
                [
                    'label' => 'plugin.helloworld.config.custom_config_option',
                    'data'  => $options['data']['custom_config_option'],
                    'attr'  => [
                        'tooltip' => 'plugin.helloworld.config.custom_config_option_tooltip'
                    ]
                ]
            );
        }

        public function getName()
        {
            return 'helloworld_config';
        }
    }

The Form type gets used to generate the Form Fields in the main configuration Form. Refer to :ref:`Forms` for more information on using Form types.

Remember that you must register the Form type through the Plugin's config in the ``services[forms]`` :ref:`section<Service config items>`.

.. vale off

Config Template
===============

.. vale oon

.. code-block:: php

   <?php
   // plugins/HelloWorldBundle/Views/FormTheme/Config/_config_helloworld_config_widget.html.php
   ?>

   <div class="panel panel-primary">
       <div class="panel-heading">
           <h3 class="panel-title"><?php echo $view['translator']->trans('mautic.config.tab.helloworld_config'); ?></h3>
       </div>
       <div class="panel-body">
           <?php foreach ($form->children as $f): ?>
               <div class="row">
                   <div class="col-md-6">
                       <?php echo $view['form']->row($f); ?>
                   </div>
               </div>
           <?php endforeach; ?>
       </div>
   </div>

Registering a ``formTheme`` as ``HelloWorldBundle:FormTheme\Config`` in the event listener told the ConfigBundle to look in the HelloWorldBundle's Views/FormTheme/Config folder for templates.
Specifically, it will look for a template named ``_config_{formAlias}_widget.html.php`` where ``{formAlias}`` is the same as ``formAlias`` set in the plugin's ``ConfigEvents::CONFIG_ON_GENERATE`` event listener.

The template should be in a panel format to match the rest of the config UI.
