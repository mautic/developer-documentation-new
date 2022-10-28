Points
######

.. vale off

Point Actions
*************

.. vale on

In Mautic, custom Point Actions give a Contact `x` Points for doing a certain action.

Mautic dispatches the Event ``\Mautic\PointBundle\PointEvents::POINT_ON_BUILD`` for Plugins to register their custom Point Action. Listeners receive a ``Mautic\PointBundle\Event\PointBuilderEvent`` object. Register the Event using the ``addAction`` method as described below.

.. php:class:: Mautic\PointBundle\Event\PointBuilderEvent

.. php:method:: public function addAction(string $key, array $action)

    :param string $key: Unique key for the Action.
    :param array $action: :ref:`Action definition<Custom Point Action definition>`.

.. php:method:: public getActions()

    :return: Array of registered Actions.
    :returntype: array

.. vale off

Registering a Custom Point Action
==================================

.. vale on

.. code-block:: php

    <?php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Mautic\PointBundle\Event\PointBuilderEvent;
    use Mautic\PointBundle\PointEvents;
    use MauticPlugin\HelloWorldBundle\Form\Type\PointActionsType;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    class PointSubscriber implements EventSubscriberInterface
    {
        public static function getSubscribedEvents(): array
        {
            return [
                PointEvents::POINT_ON_BUILD => ['onPointBuild', 0],
            ];
        }

        public function onPointBuild(PointBuilderEvent $event)
        {
            $action = [
                'group'    => 'helloworld.points.actions',
                'label'    => 'helloworld.points.actions.action',
                'callback' => [self::class, 'addPointTriggerCallback'],
                'formType' => PointActionsType::class,
            ];

            $event->addAction('helloworld.action', $action);
        }

        public static function addPointTriggerCallback(array $action, array $eventDetails): bool
        {
            // .. Add logic to weigh the action.
        }
    }


In order for the custom Point Action to work, add something like the following in the code logic when the Contact executes the custom action::

    $this->getModel('point')->triggerAction('helloworld.action', $event->getHit());

.. vale off

Custom Point Action definition
==============================

.. vale on

.. list-table::
    :header-rows: 1

    * - Key
      - Required
      - Type
      - Description
    * - ``label``
      - REQUIRED
      - string
      - The language string for the option in the dropdown
    * - ``formType``
      - OPTIONAL
      - string
      - The alias of a custom Form type used to set config options.
    * - ``formTypeOptions``
      - OPTIONAL
      - array[]
      - Array of options to include into the ``formType``’s $options argument
    * - ``formTypeCleanMasks``
      - OPTIONAL
      - array[]
      - Array of input masks to clean a values from ``formType``
    * - ``formTypeTheme``
      - OPTIONAL
      - string
      - Theme to customize elements for ``formType``
    * - ``template``
      - OPTIONAL
      - string
      - View template used to render the ``formType``
    * - ``callback``
      - OPTIONAL
      - mixed
      - Static callback function used to validate the action. Return true to add the Points to the Contact.

.. vale off

Point Triggers
**************

.. vale on

A custom Point Trigger used to execute a specific action once a Contact reaches X number of Points.

Mautic dispatches the Event ``\Mautic\PointBundle\PointEvents::TRIGGER_ON_BUILD`` for Plugins to register their custom Point Triggers. Listeners receive a ``Mautic\PointBundle\Event\TriggerBuilderEvent`` object. Register the Event using the ``addEvent`` method as described below.

.. php:class:: Mautic\PointBundle\Event\TriggerBuilderEvent

.. php:method:: public function addEvent(string $key, array $action)

    :param string $key: Unique key for the Action.
    :param array $action: :ref:`Action definition<Custom Point Trigger definition>`.

.. php:method:: public getEvents()

    :return: Array of registered Events.
    :returntype: array

.. vale off

Registering a Custom Point Trigger
===================================

.. vale on

.. code-block:: php

    <?php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Mautic\CoreBundle\Factory\MauticFactory;
    use Mautic\HelloWorldBundle\Form\Type\TriggerChoiceType;
    use Mautic\PointBundle\Event\TriggerBuilderEvent;
    use Mautic\PointBundle\PointEvents;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    class PointSubscriber implements EventSubscriberInterface
    {
        public static function getSubscribedEvents(): array
        {
            return [
                PointEvents::TRIGGER_ON_BUILD => ['onTriggerBuild', 0],
            ];
        }

        public function onTriggerBuild(TriggerBuilderEvent $event)
        {
            $changeLists = [
                'group'    => 'mautic.campaign.point.trigger',
                'label'    => 'mautic.campaign.point.trigger.changecampaigns',
                'callback' => [self::class, 'updatePointsOnBuild'],
                'formType' => TriggerChoiceType::class,
            ];

            $event->addEvent('campaign.changecampaign', $changeLists);
        }

        public static function updatePointsOnBuild($config, $lead, MauticFactory $factory): bool
        {
            // Add custom code to do some action.
        }
    }

.. vale off

Custom Point Trigger definition
===============================

.. vale on

.. list-table::
    :header-rows: 1

    * - Key
      - Required
      - Type
      - Description
    * - ``label``
      - REQUIRED
      - string
      - The language string for the option in the dropdown
    * - ``formType``
      - OPTIONAL
      - string
      - The alias of a custom Form type used to set config options.
    * - ``formTypeOptions``
      - OPTIONAL
      - array[]
      - Array of options to include into the ``formType``'s $options argument
    * - ``formTypeCleanMasks``
      - OPTIONAL
      - array[]
      - Array of input masks to clean a values from ``formType``
    * - ``formTypeTheme``
      - OPTIONAL
      - string
      - Theme to customize elements for ``formType``
    * - ``template``
      - OPTIONAL
      - string
      - View template used to render the ``formType``
    * - ``callback``
      - OPTIONAL
      - mixed
      - Static callback function used to execute the custom action.