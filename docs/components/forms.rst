Forms
#####

You can extend Forms by listening to the ``\Mautic\FormBundle\FormEvents::FORM_ON_BUILD`` event. Read more about :doc:`listeners and subscribers</plugins/event_listeners>`.
At the bottom of this document, you can find code examples to make it easier to get started.

.. vale off

Form Fields
***********

.. vale on

To add a custom Form Field, use the ``$event->addFormField($identifier, $parameters)`` method. ``$identifier`` must be something unique. The ``$parameters`` array can contain the following elements:

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
      - View template used to render the ``formType``, for example ``HelloWorldBundle:SubscribedEvents\FormField:customfield.html.php``
    * - ``formTypeOptions``
      - Optional
      - array
      - Array of options to include into the ``formType``'s $options argument
    * - ``formTypeCleanMasks``
      - Optional
      - array
      - Array of input masks to clean a values from ``formType``
    * - ``formTypeTheme``
      - Optional
      - array
      - Array of input masks to clean a values from ``formType``
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

Form submit actions
*******************

To add an action, use the ``$event->addSubmitAction($identifier, $parameters)`` method. ``$identifier`` must be something unique. The ``$parameters`` array can contain the following elements:

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
    * - ``eventName``
      - Required
      - string
      - This is the custom event name that gets dispatched to handle this action. It receives a ``SubmissionEvent`` object
    * - ``description``
      - Optional
      - string
      - The language string to use for the option's tooltip
    * - ``formType``
      - Optional
      - string
      - The alias of a custom Form type used to set config options
    * - ``formTypeOptions``
      - Optional
      - array
      - Array of options to include into the ``formType``'s ``$options`` argument
    * - ``formTypeCleanMasks``
      - Optional
      - array
      - Array of input masks to clean a values from ``formType``
    * - ``formTypeTheme``
      - Optional
      - string
      - Theme to customize elements for ``formType``
    * - ``template``
      - Optional
      - string
      - View template used to render the ``formType``

The subscriber registered to listen to the ``eventName`` gets an instance of ``Mautic\FormBundle\Events\SubmissionEvent`` with the details about the submission. 
 
Sometimes, it's necessary to handle something after all the other submit actions have done their thing - like redirecting to another URL.
To do this, register a submit callback through the subscriber that processes the action.
You can either inject the ``Symfony\Component\HttpFoundation\Response`` at that time with ``$event->setPostSubmitCallbackResponse($identifier, $response);`` or register another custom event to be dispatched after all submit actions have been processed using ``$event->setPostSubmitCallback($key, ['eventName' => HelloWorld::ANOTHER_CUSTOM_EVENT]);``.

Form validations
****************

To add a custom validation, use the ``$event->addValidator($identifier, $parameters)`` method. ``$identifier`` must be something unique. The ``$parameters`` array can contain the following elements:

.. list-table::
    :header-rows: 1

    * - Key
      - Required
      - Type
      - Description
    * - ``eventName``
      - Required
      - string
      - The name of the custom event that gets dispatched to validate the Form or specific field
    * - ``fieldType``
      - Optional
      - string
      - The key to a custom Form type, for example something registered by ``addFormField()``, to limit this listener to. Otherwise every field gets sent to listener.
    * - ``formType``
      - Optional
      - string
      - Form type class to generate additional fields for the ``validator`` tab

The listener for the Form event receives a ``Mautic\FormBundle\Event\ValidationEvent`` object.
Obtain the field with ``$event->getField();``, do the logic to fail a validation, then execute ``$event->failedValidation('I said so.');``.

Example code
************

.. code-block:: PHP

    <?php
    // plugins/HelloWorldBundle/EventListener/FormSubscriber.php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use MauticPlugin\HelloWorldBundle\HelloWorldEvents;
    use Mautic\FormBundle\Event\FormBuilderEvent;
    use Mautic\FormBundle\Event\SubmissionEvent;
    use Mautic\FormBundle\Event\ValidationEvent;
    use Mautic\FormBundle\FormEvents;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;
    use Symfony\Component\HttpFoundation\RedirectResponse;
    use Symfony\Component\HttpFoundation\Response;

    class FormSubscriber implements EventSubscriberInterface
    {
        /**
        * {@inheritdoc}
        */
        static public function getSubscribedEvents()
        {
            return [
                FormEvents::FORM_ON_BUILD                         => ['onFormBuilder', 0],
                // Generic validation function that runs on ALL field types
                FormEvents::ON_FORM_VALIDATE                      => ['onFormValidate', 0],
                HelloWorldEvents::ON_FORM_SUBMISSION              => ['onFormSubmission', 0],
                // Only validates our custom field type (helloworld.customfield)
                HelloWorldEvents::ON_FORM_CUSTOM_FIELD_VALIDATION => ['onFormValidateCustomFIeld', 0]
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
                    'eventName'    => HelloWorldEvents::ON_FORM_SUBMISSION
                ]
            );

            /**
            * Register a custom validation service. This is only needed if:
            * - you only want to validate your custom field type (the generic FormEvents::ON_FORM_VALIDATE runs on all field types which is less efficient)
            * - you have more complex validation logic that you want to have in its own event listener
            * 
            * In all other cases, you can simply listen to FormEvents::ON_FORM_VALIDATE as shown in onFormValidate() below.
            */
            $event->addValidator(
                'helloworld.customfield',
                [
                    'eventName' => HelloWorldEvents::ON_FORM_CUSTOM_FIELD_VALIDATION,
                    // Optional - otherwise all fields will be sent through this listener for validation
                    'fieldType' => 'helloworld.customfield',
                    // Optional - otherwise just default required option should be generated to validation tab
                    'formType' => \MauticPlugin\HelloWorldBundle\Form\Type\HelloWorldType::class
                ]
            );
        }
        
        /**
        * Generic validation function that runs on ALL field types.
        * For efficiency reasons, it's recommended to set up a custom validator (see $event->addValidator() above) if you
        * only need to validate a custom field type.
        */
        public function onFormValidate(ValidationEvent $event): void
        {
            $field = $event->getField();
            $validation = $field->getValidation();

            if ($field->getType() === 'helloworld.customfield' && !empty($validation['c_enable'])) {
                if (empty($validation['helloworld_customfield_enable_validationmsg'])) {
                    $event->failedValidation($validation['helloworld_customfield_enable_validationmsg']);
                } else {
                    $event->failedValidation('plugin.helloworld.formfield.customfield.invalid');
                }
            }
        }

        /**
        * Validation function that we registered specifically for our custom field type (helloworld.customfield).
        * We don't need to check the field in this case, because it'll only trigger when validating our custom field
        * (see $event->addValidator() above).
        */
        public function onFormValidateCustomField(ValidationEvent $event): void
        {
            $field = $event->getField();
            $validation = $field->getValidation();

            if (!empty($validation['c_enable'])) {
                if (empty($validation['helloworld_customfield_enable_validationmsg'])) {
                    $event->failedValidation($$validation['helloworld_customfield_enable_validationmsg']);
                } else {
                    $event->failedValidation('plugin.helloworld.formfield.customfield.invalid');
                }
            }
        }

        public function onFormSubmission(SubmissionEvent $event): void
        {
            // Get the submitted data
            $data = $event->getPost();

            // Redirect to an external URL after the form has been submitted
            $event->setPostSubmitCallbackResponse('helloworld.submit.response', new RedirectResponse('https://mydomain.com'));

            // Dispatch a custom event to be dispatched after all submit actions have been processed
            $event->setPostSubmitCallback('helloworld.submit.callback', [
                'eventName' => HelloWorldEvents::ON_FORM_SUBMISSION_CALLBACK
            ]);
        }
    }

.. code-block:: PHP

    <?php

    namespace MauticPlugin\HelloWorldBundle;

    final class HelloWorldEvents
    {
        /**
        * The plugin.hello.world.on_form_submission event is fired when a form is submitted.
        *
        * The event listener receives a Mautic\FormBundle\Events\SubmissionEvent
        *
        * @var string
        */
        public const ON_FORM_SUBMISSION = 'plugin.hello.world.on_form_submission';

        /**
        * The plugin.hello.world.on_form_submission_callback event is fired after all submit actions have been processed
        *
        * The event listener receives a Mautic\FormBundle\Events\SubmissionEvent
        *
        * @var string
        */
        public const ON_FORM_SUBMISSION_CALLBACK = 'plugin.hello.world.on_form_submission_callback';

        /**
        * The plugin.hello.world.on_form_validation event is fired when our custom field type (helloworld.customfield)
        * is being validated in a form submission.
        *
        * The event listener receives a Mautic\FormBundle\Event\ValidationEvent
        *
        * @var string
        */
        public const ON_FORM_CUSTOM_FIELD_VALIDATION = 'plugin.hello.world.on_form_custom_field_validation';
    }
