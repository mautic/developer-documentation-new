Forms
==========================================================

You can extend Forms by listening to the ``\Mautic\FormBundle\FormEvents::FORM_ON_BUILD`` event.  Read more about :doc:`listeners and subscribers</plugins/event_listeners>`. 

Form fields
-----------
To add a custom form field, use the ``$event->addFormField($identifier, $parameters)`` method. ``$identifier`` must be something unique. The ``$parameters`` array can contain the following elements:

.. list-table::
    :header-rows: 1

    * - Key
      - Required
      - Type
      - Description
    * - ``label``
      - Required
      - string
      - The language string for the option in the dropdown
    * - ``formType``
      - Required
      - string
      - The alias of a custom Form type used to set config options
    * - ``template``
      - Required
      - string
      - View template used to render the formType, for example ``HelloWorldBundle:SubscribedEvents\FormField:customfield.html.php``
    * - ``formTypeOptions``
      - Optional
      - array
      - Array of options to include into the formType's $options argument
    * - ``formTypeCleanMasks``
      - Optional
      - array
      - Array of input masks to clean a values from formType
    * - ``formTypeTheme``
      - Optional
      - array
      - Array of input masks to clean a values from formType
    * - ``valueFilter``
      - Optional
      - mixed
      - Filter to use to clean the submitted value as supported by InputHelper or a callback function that accepts the arguments ``\Mautic\FormBundle\Entity\Field $field`` and ``$value``.
    * - ``valueConstraints``
      - Optional
      - mixed
      - Callback function to use to validate the value; the function should accept the arguments ``\Mautic\FormBundle\Entity\Field $field`` and ``$filteredValue``.
    * - ``builderOptions``
      - Optional
      - array
      - Array of boolean options for the Form builder:
        
        .. code-block:: PHP

            <?php

            $builderOptions = [
                'addHelpMessage' => true,
                'addShowLabel' => true,
                'addDefaultValue' => true,
                'addLabelAttributes' => true,
                'addInputAttributes' => true,
                'addIsRequired' => true
            ];

Form Submit Actions
-------------------

To add an action, use the `$event->addSubmitAction($identifier, $parameters)` method. `$identifier` must be something unique. The `$parameters` array can contain the following elements:
 
Key|Required|Type|Description
---|--------|----|-----------
**label**|REQUIRED|string|The language string for the option in the dropdown
**description**|OPTIONAL|string|The language string to use for the option's tooltip
**eventName**|REQUIRED|string|This is the custom event name that will be dispatched to handle this action (`callback` has been deprecated)
**formType**|OPTIONAL|string|The alias of a custom form type used to set config options
**formTypeOptions**|OPTIONAL|array|Array of options to include into the formType's $options argument
**formTypeCleanMasks**|OPTIONAL|array|Array of input masks to clean a values from formType
**formTypeTheme**|OPTIONAL|string|Theme to customize elements for formType
**template**|OPTIONAL|string|View template used to render the formType 
**validator**|DEPRECATED|mixed|Static callback function called to validate the form submission. Deprecated - Register a validator using the `$event->addValidator()`. 
**callback**|DEPRECATED|mixed|Static callback function called after a submission (submit action logic goes here). Deprecated - use eventName instead.

The subscriber registered to listen to the `eventName` will be passed an instance of `Mautic\FormBundle\Events\SubmissionEvent` with the details about the post. 
 
Sometimes, it is necessary to handle something after all the other submit actions have done their thing - like redirect to another page. This is done by registering a post submit callback through the subscriber that processes the action. You can either inject the `Symfony\Component\HttpFoundation\Response` at that time with `$event->setPostSubmitCallbackResponse($response);` or register another custom event to be dispatched after all submit actions have been processed using `$event->setPostSubmitCallback($key, ['eventName' => HelloWorld::ANOTHER_CUSTOM_EVENT]);`.

Form Validations
----------------

To add a custom validation, use the `$event->addValidator($identifier, $parameters)` method. `$identifier` must be something unique. The `$parameters` array can contain the following elements:

Key|Required|Type|Description
---|--------|----|-----------
**eventName**|REQUIRED|string|The name of the custom event that will be dispatched to validate the form or specific field
**fieldType**|optional|string|The key to a custom form type (for example something registered by `addFormField()`) to limit this listener to. Otherwise every field will be sent to listener.
**formType**|optional|string|Form type class to generate additional fields to validator tab
  
The listener for the form event will receive a `Mautic\FormBundle\Event\ValidationEvent` object. Obtain the field with `$event->getField();` do the logic then to fail a validation, execute `$event->failedValidation('I said so.');`.

Example code
------------

.. code-block:: PHP

    <?php
    // plugins/HelloWorldBundle/EventListener/FormSubscriber.php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use MauticPlugin\HelloWorldBundle\HelloWorldEvents;
    use Mautic\FormBundle\Event\FormBuilderEvent;
    use Mautic\FormBundle\Event\ValidationEvent;
    use Mautic\FormBundle\FormEvents;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    class FormSubscriber implements EventSubscriberInterface
    {
        /**
        * {@inheritdoc}
        */
        static public function getSubscribedEvents()
        {
            return [
                FormEvents::FORM_ON_BUILD     => ['onFormBuilder', 0],
                FormEvents::ON_FORM_VALIDATE  => ['onFormValidate', 0],

            ];
        }

        /**
        * Add a simple email form
        */
        public function onFormBuilder(FormBuilderEvent $event): void
        {
            // Register a custom form field
            $event->addFormField(
                'helloworld.customfield',
                [
                    // Field label
                    'label'    => 'plugin.helloworld.formfield.customfield',
                    
                    // Form service for the field's configuration
                    'formType' => 'helloworld_worlds',
                    
                    // Template to use to render the formType
                    'template' => 'HelloWorldBundle:SubscribedEvents\FormField:customfield.html.php'
                ]
            );

            // Register a form submit actions
            $event->addSubmitAction(
                'helloworld.sendemail',
                [
                    // Label to group by in the dropdown
                    'group'       => 'plugin.helloworld.header',
                    
                    // Label to list by in the dropdown
                    'label'       => 'plugin.helloworld.formaction.send_email',
                    'description' => 'plugin.helloworld.formaction.send_email_descr',
                    
                    // Form service for custom config options
                    'formType'    => 'helloworld_worlds',
                    'formTheme'   => 'HelloWorldBundle:FormTheme\SubmitAction',
                    
                    // Callback method to be executed after the submission 
                    'eventName'    => HelloWorldEvents::FORM_SUBMIT_ACTION
                ]
            );

            // Register a custom validation service
            $event->addValidator(
                'helloworld.customfield',
                [
                    'eventName' => HelloWorldEvents::FORM_VALIDATION,
                    'fieldType' => 'helloworld.customfield', // Optional - otherwise all fields will be sent through this listener for validation
                    'formType' => \MauticPlugin\HelloWorldBundle\Form\Type\HelloWorldType::class // Optional - otherwise just default required option should be generated to validation tab 
                    
                ]
            );
        }
        
        public function onFormValidate(ValidationEvent $event): void
        {
            $field = $event->getField();
            if ($field->getType() === 'helloworld.customfield' && !empty($field->getValidation()['c_enable'])) {
                if (empty($field->getValidation()['helloworld_customfield_enable_validationmsg'])) {
                    $event->failedValidation($field->getValidation()['helloworld_customfield_enable_validationmsg']);
                } else {
                    $event->failedValidation('plugin.helloworld.formfield.customfield.invalid');
                }
            }
        }
    }