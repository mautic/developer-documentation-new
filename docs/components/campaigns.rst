Campaigns
#########

.. vale off

Registering Campaign Events
***************************

.. vale on

Mautic dispatches the Event ``\Mautic\CampaignBundle\CampaignEvents::CAMPAIGN_ON_BUILD`` for Plugins to register their Campaign Actions, Conditions and Decisions. Listeners receive a ``Mautic\CampaignBundle\Events\CampaignBuilderEvent`` object. Register the Event using the appropriate ``add`` method as described below.

.. php:namespace:: Mautic\CampaignBundle\Events
.. php:class:: CampaignBuilderEvent

  CampaignBuilderEvent class

  .. php:method:: public addAction(string $key, array $action)

      :param string $key: Unique key for the Action.
      :param array $action: :ref:`Campaign definition <components/campaigns:Campaign Action definition>`.

      :returntype: void

  .. php:method:: public addCondition(string $key, array $condition)

      :param string $key: Unique key for the Condition.
      :param array $condition: :ref:`Condition definition <components/campaigns:Campaign Condition definition>`.

      :returntype: void

  .. php:method:: public addDecision(string $key, array $decision)

      :param string $key: Unique key for the Decision.
      :param array $decision: :ref:`Decision definition <components/campaigns:Campaign Decision definition>`.

      :returntype: void

  .. php:method:: public getActions()

      :return: Array of registered Actions.
      :returntype: array

  .. php:method:: public getConditions()

      :return: Array of registered Conditions.
      :returntype: array

  .. php:method:: public getDecisions()

      :return: Array of registered Decisions.
      :returntype: array

.. vale off

Registering a Campaign Action
=============================

.. vale on

.. code-block:: php

    <?php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Mautic\CampaignBundle\CampaignEvents;
    use Mautic\CampaignBundle\Event\CampaignBuilderEvent;
    use MauticPlugin\HelloWorldBundle\HelloWorldEvents;
    use MauticPlugin\HelloWorldBundle\Form\Type\TravelType;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    class CampaignActionSubscriber implements EventSubscriberInterface
    {
        public const TYPE = 'helloworld.action';

        public static function getSubscribedEvents(): array
        {
            return [
                CampaignEvents::CAMPAIGN_ON_BUILD => ['onCampaignBuild', 0],
            ];
        }

        public function onCampaignBuild(CampaignBuilderEvent $event): void
        {
            $event->addAction(
                self::TYPE,
                [
                    'label'          => 'helloworld.campaign.event.action',
                    'description'    => 'helloworld.campaign.event.action.descr',
                    'batchEventName' => HelloWorldEvents::EXECUTE_CAMPAIGN_ACTION,
                    'formType'       => TravelType::class,
                ]
            );
        }
    }

.. vale off

Campaign Action definition
==========================

.. vale on

.. list-table::
    :header-rows: 1

    * - Key
      - Is required?
      - Type
      - Description
    * - ``label``
      - yes
      - string
      - Display name for the UI.
    * - ``batchEventName``
      - yes
      - string
      - The Campaign engine dispatches this Event through the ``event_dispatcher`` service when Contacts reach this point in the journey.
    * - ``description``
      - no
      - string
      - Displays as the tool-tip for this Event.
    * - ``formType``
      - no
      - string
      - :xref:`Symfony form type class<Symfony 4 custom form field type tag>` for the Event's configuration.
    * - ``formTypeOptions``
      - no
      - array
      - Array of options passed into the given Symfony form type.
    * - ``formTypeCleanMasks``
      - no
      - array
      - Array of field:filter pairs of input masks supported by ``Mautic\CoreBundle\Helper\InputHelper`` to sanitize the form's submitted data.
    * - ``formTypeTheme``
      - no
      - string
      - PHP template to customize the UI of the given form type.
    * - ``connectionRestrictions``
      - no
      - array
      - Array of restrictions defining the Events and anchors this Event is compatible with.
    * - ``connectionRestrictions.anchor``
      - no
      - array
      - Array of Event anchors this Event **isn't** allowed to connect to. Names of anchors are ``yes`` for the "action" or "TRUE" path and ``no`` for the "inaction" or "FALSE" path. Expected format is ``EventType.anchorName``. For example, ``decision.no``.
    * - ``connectionRestrictions.source``
      - no
      - array[]
      - Array with keys as Event types of ``action``, ``condition``, and/or ``decision`` with the keys of other Events allowed to connect into this Event's top anchor.
    * - ``connectionRestrictions.target``
      - no
      - array[]
      - Array with keys as Event types of ``action``, ``condition``, and/or ``decision`` with the keys of other Events allowed to flow from this Event. In other words, connect into the Event's bottom anchors.
    * - ``timelineTemplate``
      - no
      - string
      - PHP template to customize the UI for this Event in the Contact's timeline.

.. vale off

Registering a Campaign Condition
********************************

.. vale on

.. code-block:: php

    <?php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Mautic\CampaignBundle\CampaignEvents;
    use Mautic\CampaignBundle\Event\CampaignBuilderEvent;
    use MauticPlugin\HelloWorldBundle\HelloWorldEvents;
    use MauticPlugin\HelloWorldBundle\Form\Type\TravelType;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    class CampaignConditionSubscriber implements EventSubscriberInterface
    {
        public const TYPE = 'helloworld.condition';

        public static function getSubscribedEvents(): array
        {
            return [
                CampaignEvents::CAMPAIGN_ON_BUILD => ['onCampaignBuild', 0],
            ];
        }

        public function onCampaignBuild(CampaignBuilderEvent $event): void
        {
            $event->addCondition(
                self::TYPE,
                [
                    'label'       => 'helloworld.campaign.event.condition',
                    'description' => 'helloworld.campaign.event.condition.descr',
                    'eventName'   => HelloWorldEvents::EVALUATE_CAMPAIGN_CONDITION,
                    'formType'    => TravelType::class,
                ]
            );
        }
    }

.. vale off

Campaign Condition definition
=============================

.. vale on

.. list-table::
    :header-rows: 1

    * - Key
      - Is required?
      - Type
      - Description
    * - ``label``
      - yes
      - string
      - Display name for the UI.
    * - ``eventName``
      - yes
      - string
      - The Campaign engine dispatches this Event through the ``event_dispatcher`` service when Contacts reach this point in the journey.
    * - ``description``
      - no
      - string
      - Displays as the tool-tip for this Event.
    * - ``formType``
      - no
      - string
      - :xref:`Symfony form type class<Symfony 4 custom form field type tag>` for the Event's configuration.
    * - ``formTypeOptions``
      - no
      - array
      - Array of options passed into the given Symfony form type.
    * - ``formTypeCleanMasks``
      - no
      - array
      - Array of field:filter pairs of input masks supported by ``Mautic\CoreBundle\Helper\InputHelper`` to sanitize the form's submitted data.
    * - ``formTypeTheme``
      - no
      - string
      - PHP template to customize the UI of the given form type.
    * - ``connectionRestrictions``
      - no
      - array
      - Array of restrictions defining the Events and anchors this Event is compatible with.
    * - ``connectionRestrictions.anchor``
      - no
      - array
      - Array of Event anchors this Event **isn't** allowed to connect to. Names of anchors are ``yes`` for the "action" or "TRUE" path and ``no`` for the "inaction" or "FALSE" path. Expected format is ``EventType.anchorName``. For example, ``decision.no``.
    * - ``connectionRestrictions.source``
      - no
      - array[]
      - Array with keys as Event types of ``action``, ``condition``, and/or ``decision`` with the keys of other Events allowed to connect into this Event's top anchor.
    * - ``connectionRestrictions.target``
      - no
      - array[]
      - Array with keys as Event types of ``action``, ``condition``, and/or ``decision`` with the keys of other Events allowed to flow from this Event. In other words, connect into the Event's bottom anchors.
    * - ``timelineTemplate``
      - no
      - string
      - PHP template to customize the UI for this Event in the Contact's timeline.

.. vale off

Registering a Campaign Decision
*******************************

.. vale on

.. code-block:: php

    <?php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Mautic\CampaignBundle\CampaignEvents;
    use Mautic\CampaignBundle\Event\CampaignBuilderEvent;
    use MauticPlugin\HelloWorldBundle\HelloWorldEvents;
    use MauticPlugin\HelloWorldBundle\Form\Type\TravelType;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    class CampaignDecisionSubscriber implements EventSubscriberInterface
    {
        public const TYPE = 'helloworld.decision';

        public static function getSubscribedEvents(): array
        {
            return [
                CampaignEvents::CAMPAIGN_ON_BUILD => ['onCampaignBuild', 0],
            ];
        }

        public function onCampaignBuild(CampaignBuilderEvent $event): void
        {
            $event->addCondition(
                self::TYPE,
                [
                    'label'       => 'helloworld.campaign.event.decision',
                    'description' => 'helloworld.campaign.event.decision.descr',
                    'eventName'   => HelloWorldEvents::EVALUATE_CAMPAIGN_DECISION,
                    'formType'    => TravelType::class,
                ]
            );
        }
    }

.. vale off

Campaign Decision definition
============================

.. vale on

.. list-table::
    :header-rows: 1

    * - Key
      - Is required?
      - Type
      - Description
    * - ``label``
      - yes
      - string
      - Display name for the UI.
    * - ``eventName``
      - yes
      - string
      - The Campaign engine dispatches this Event through the ``event_dispatcher`` service when Contacts reach this point in the journey.
    * - ``description``
      - no
      - string
      - Displays as the tool-tip for this Event.
    * - ``formType``
      - no
      - string
      - :xref:`Symfony form type class<Symfony 4 custom form field type tag>` for the Event's configuration.
    * - ``formTypeOptions``
      - no
      - array
      - Array of options passed into the given Symfony form type.
    * - ``formTypeCleanMasks``
      - no
      - array
      - Array of field:filter pairs of input masks supported by ``Mautic\CoreBundle\Helper\InputHelper`` to sanitize the form's submitted data.
    * - ``formTypeTheme``
      - no
      - string
      - PHP template to customize the UI of the given form type.
    * - ``connectionRestrictions``
      - no
      - array
      - Array of restrictions defining the Events and anchors this Event is compatible with.
    * - ``connectionRestrictions.anchor``
      - no
      - array
      - Array of Event anchors this Event **isn't** allowed to connect to. Names of anchors are ``yes`` for the "action" or "TRUE" path and ``no`` for the "inaction" or "FALSE" path. Expected format is ``EventType.anchorName``. For example, ``decision.no``.
    * - ``connectionRestrictions.source``
      - no
      - array[]
      - Array with keys as Event types of ``action``, ``condition``, and/or ``decision`` with the keys of other Events allowed to connect into this Event's top anchor.
    * - ``connectionRestrictions.target``
      - no
      - array[]
      - Array with keys as Event types of ``action``, ``condition``, and/or ``decision`` with the keys of other Events allowed to flow from this Event. In other words, connect into the Event's bottom anchors.
    * - ``timelineTemplate``
      - no
      - string
      - PHP template to customize the UI for this Event in the Contact's timeline.

.. vale off

Executing or evaluating Campaign Events
***************************************

.. vale on

Implement a listener to the event name defined in either ``batchEventName`` or ``eventName`` to execute or evaluate the Campaign Event.

.. vale off

Executing a Campaign Action
===========================

.. vale on

Listeners to the event's ``batchEventName`` receives a ``\Mautic\CampaignBundle\Event\PendingEvent`` object. This object contains the Contacts that are at this point in their journey. Listeners must process the batch of Contacts and mark their respective ``\Mautic\CampaignBundle\Entity\LeadEventLog`` as passed or failed. You must mark each `LeadEventLog` as passed or failed. The ``campaign_time_wait_on_event_false`` configuration option determines the rescheduling of failed events.

.. code-block:: php

    <?php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Mautic\CampaignBundle\CampaignEvents;
    use Mautic\CampaignBundle\Event\CampaignBuilderEvent;
    use Mautic\CampaignBundle\Event\PendingEvent;
    use MauticPlugin\HelloWorldBundle\HelloWorldEvents;
    use MauticPlugin\HelloWorldBundle\Form\Type\TravelType;
    use MauticPlugin\HelloWorldBundle\Helper\TravelService;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;
    use Symfony\Component\Translation\TranslatorInterface;

    class CampaignActionSubscriber implements EventSubscriberInterface
    {
        public const TYPE = 'helloworld.action';

        private TranslatorInterface $translator;
        private TravelService $travelService;

        public function __construct(TranslatorInterface $translator, TravelService $travelService)
        {
            $this->translator    = $translator;
            $this->travelService = $travelService;
        }

        public static function getSubscribedEvents(): array
        {
            return [
                CampaignEvents::CAMPAIGN_ON_BUILD         => ['onCampaignBuild', 0],
                HelloWorldEvents::EXECUTE_CAMPAIGN_ACTION => ['onExecuteCampaignAction', 0],
            ];
        }

        public function onCampaignBuild(CampaignBuilderEvent $event): void
        {
            $event->addAction(
                self::TYPE,
                [
                    'label'          => 'helloworld.campaign.event.action',
                    'description'    => 'helloworld.campaign.event.action.descr',
                    'batchEventName' => HelloWorldEvents::EXECUTE_CAMPAIGN_ACTION,
                    'formType'       => TravelType::class,
                ]
            );
        }

        public function onExecuteCampaignAction(PendingEvent $pendingEvent): void
        {
            $worldToVisit = $pendingEvent->getConfig()->getProperty('worldToVisit');
            $pendingEvent->setChannel('world', $worldToVisit);

            $contacts = $pendingEvent->getContactsKeyedById();
            $emails   = [];
            foreach ($contacts as $contact) {
                if (!$contact->getEmail()) {
                    // Don't reschedule these events
                    $pendingEvent->passWithError(
                        $pendingEvent->findLogByContactId($contact->getId()),
                        $this->translator->trans('helloworld.validation.email_required', [], 'validators')
                    );

                    $emails[] = $contact->getEmail();
                }
            }

            $this->travelService->doSomethingWithThese($emails, $worldToVisit);

            $pendingEvent->passRemaining();
        }
    }

.. php:class:: Mautic\CampaignBundle\Events\PendingEvent

.. php:method:: public checkContext(string $eventType)

    Checks if the given Event type matches the Event executed or evaluated. This is useful if listeners for different Campaign Events are listening to the same name defined as ``batchEventName`` in the Event's definition.

    :return: ``TRUE`` if the context matches.
    :returntype: bool

.. php:method:: public fail(\Mautic\CampaignBundle\Entity\LeadEventLog $log, string $reason)

    Mark a specific LeadEventLog object as failed and retry again later.

    :param \\Mautic\\CampaignBundle\\Entity\\LeadEventLog $log: Event log to fail.
    :param string $reason: Reason the Event failed.

    :returntype: void

.. php:method:: public failAll(string $reason)

    Fail the entire batch of LeadEventLog objects and retry again later.

    :param string $reason: Reason the Events failed.

    :returntype: void

.. php:method:: public failLogs(\Doctrine\Common\Collections\ArrayCollection $logs, string $reason)

    Fail a collection of LeadEventLog objects and try again later.

    :param string $logs \\Doctrine\\Common\\Collections\\ArrayCollection: Collection to mark as failed.
    :param string $reason: Reason the Events failed.

    :returntype: void

.. php:method:: public failRemaining(string $reason)

    Fail all remaining LeadEventLog objects that are not marked as passed.

    :param string $reason: Reason the Events failed.

    :returntype: void

.. php:method:: public findLogByContactId(int $id)

    Returns a LeadEventLog object for the given contact ID.

    :param int $id:

    :return: Event log for the given contact.
    :returntype: \\Mautic\\CampaignBundle\\Entity\\LeadEventLog

.. php:method:: public getConfig()

    Use the returned ``AbstractEventAccessor`` object to access properties configured for this Event.

    :return: Object to fetch the configuration options for the Campaign Event.
    :returntype: \\Mautic\\CampaignBundle\\EventCollector\\Accessor\\Event\\AbstractEventAccessor

.. php:method:: public getContactIds()

    :return: Array of Contact IDs for the current batch of LeadEventLog objects to process.
    :returntype: array

.. php:method:: public getContacts()

    Returns the Lead objects for all Contacts in the current batch of LeadEventLog objecdts to process.

    :return: Collection of Lead objects.
    :returntype: \\Doctrine\\Common\\Collections\\ArrayCollection

.. php:method:: public getContactsKeyedById()

    Same as ``getContacts`` except keyed by Contact ID.

    :return: Collection of Lead objects.
    :returntype: \\Doctrine\\Common\\Collections\\ArrayCollection

.. php:method:: public getEvent()

    Returns the current Event entity.

    :return: Event entity.
    :returntype: \\Mautic\\CampaignBundle\\Entity\\Event

.. php:method:: public pass(\Mautic\CampaignBundle\Entity\LeadEventLog $log)

    Mark a specific LeadEventLog as successful.

    :param \\Mautic\\CampaignBundle\\Entity\\LeadEventLog $log: Event log to pass.

    :returntype: void

.. php:method:: public passAll()

    Mark all LeadEventLog objects as successful for the current batch.

    :returntype: void

.. php:method:: public passAllWithError(string $reason)

    Mark all LeadEventLog objects with an error and they will **not** be retried later.

    :returntype: void

.. php:method:: public passLogs(\Doctrine\Common\Collections\ArrayCollection $logs)

    Mark a collection of LeadEventLog objects as successful.

    :param string $logs \\Doctrine\\Common\\Collections\\ArrayCollection: Collection to mark as successful.

    :returntype: void

.. php:method:: public passRemaining()

    Mark remaining LeadEventLog objects that are not marked as failed.

    :returntype: void

.. php:method:: public passRemainingWithError(string $reason)

    Mark remaining LeadEventLog objects that are not already marked as failed.

    :param string $reason: The error message.

    :returntype: void

.. php:method:: public passWithError(\Mautic\CampaignBundle\Entity\LeadEventLog $log, string $reason)

    Mark a specific LeadEventLog with an error and do not try again.

    :param \\Mautic\\CampaignBundle\\Entity\\LeadEventLog $log: Event log to pass.
    :param string $reason: The error message.

    :returntype: void

.. php:method:: public setChannel(string $channel[, $channelId = null)

    Set the Channel to attribute to the Event.

    :param string $channel: Name of the Channel this Event relates to. For example, ``email``, ``page``, ``form``, and so forth.
    :param mixed $channelId: ID of the Channel entity.

    :returntype: void

.. vale off

Evaluating a Campaign Condition
*******************************

.. vale on

Listeners to the event's ``eventName`` receives a ``\Mautic\CampaignBundle\Event\ConditionEvent`` object. This object contains the single LeadEventLog object for the Contact to evaluate this condition. The listener must call ``ConditionEvent::pass()`` or ``ConditionEvent::fail()`` after evaluating the condition.

.. code-block:: php

    <?php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Mautic\CampaignBundle\CampaignEvents;
    use Mautic\CampaignBundle\Event\CampaignBuilderEvent;
    use Mautic\CampaignBundle\Event\ConditionEvent;
    use MauticPlugin\HelloWorldBundle\HelloWorldEvents;
    use MauticPlugin\HelloWorldBundle\Form\Type\TravelType;
    use MauticPlugin\HelloWorldBundle\Helper\TravelService;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    class CampaignConditionSubscriber implements EventSubscriberInterface
    {
        public const TYPE = 'helloworld.condition';

        private TravelService $travelService;

        public function __construct(TravelService $travelService): void
        {
            $this->travelService = $travelService;
        }

        public static function getSubscribedEvents(): array
        {
            return [
                CampaignEvents::CAMPAIGN_ON_BUILD             => ['onCampaignBuild', 0],
                HelloWorldEvents::EVALUATE_CAMPAIGN_CONDITION => ['onEvaluateCampaignCondition', 0],
            ];
        }

        public function onCampaignBuild(CampaignBuilderEvent $event): void
        {
            $event->addCondition(
                self::TYPE,
                [
                    'label'       => 'helloworld.campaign.event.condition',
                    'description' => 'helloworld.campaign.event.condition.descr',
                    'eventName'   => HelloWorldEvents::EVALUATE_CAMPAIGN_CONDITION,
                    'formType'    => TravelType::class,
                ]
            );
        }

        public function onEvaluateCampaignCondition(ConditionEvent $event): void
        {
            $leadEventLog = $event->getLog();
            $contact      = $leadEventLog->getLead();
            $world        = $event->getEventConfig()->getProperty('world');

            if ($this->travelService->hasTraveledTo($contact, $world)) {
                $event->pass();
            } else {
                $event->fail();
            }
        }
    }

.. php:class:: Mautic\CampaignBundle\Events\ConditionEvent

.. php:method:: public checkContext(string $eventType)

    Checks if the given Event type matches the Event executed or evaluated. This is useful if listeners for different Campaign Events are listening to the same name defined as ``eventName`` in the Event's definition.

    :return: ``TRUE`` if the context matches.
    :returntype: bool

.. php:method:: public fail()

    Evaluate this Condition as ``FALSE``.

    :returntype: void

.. php:method:: public getEventConfig()

    Use the returned ``AbstractEventAccessor`` object to access properties configured for this Event.

    :return: Object to fetch the configuration options for the Campaign Event.
    :returntype: \\Mautic\\CampaignBundle\\EventCollector\\Accessor\\Event\\AbstractEventAccessor

.. php:method:: public getLog()

    :return: The ``LeadEventLog`` object for the Condition.
    :returntype: \\Mautic\\CampaignBundle\\Entity\\LeadEventLog

.. php:method:: public pass()

    Evaluate this Condition as ``TRUE``.

    :returntype: void

.. php:method:: public setChannel(string $channel[, $channelId = null)

    Set the Channel to attribute to the Event.

    :param string $channel: Name of the Channel this Event relates to. For example, ``email``, ``page``, ``form``, and so forth.
    :param mixed $channelId: ID of the Channel entity.

    :returntype: void

.. vale off

Evaluating a Campaign Decision
******************************

.. vale on

Decisions are when a Contact takes some kind of direct action - where they made a decision to act. The code that handles the logic of the decision also needs to tell the Campaign Engine to evaluate Campaign Decisions of the given type by calling ``Mautic\CampaignBundle\Executioner\RealTimeExecutioner::execute()``, registered as the the ``mautic.campaign.executioner.realtime`` service.

The Campaign Engine then dispatches the Decision Event's ``eventName`` where listeners receive a ``\Mautic\CampaignBundle\Event\DecisionEvent`` object. This object contains the single LeadEventLog object for the Contact to evaluate this decision. The listener must call ``DecisionEvent::setAsApplicable()`` to instruct the Campaign Engine to execute or schedule Events attached to the "action" (left) path of the decision.

.. code-block:: php

    <?php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Mautic\CampaignBundle\CampaignEvents;
    use Mautic\CampaignBundle\Event\CampaignBuilderEvent;
    use Mautic\CampaignBundle\Event\DecisionEvent;
    use Mautic\CampaignBundle\Executioner\RealTimeExecutioner;
    use MauticPlugin\HelloWorldBundle\HelloWorldEvents;
    use MauticPlugin\HelloWorldBundle\Event\TravelDocumentEvent;
    use MauticPlugin\HelloWorldBundle\Form\Type\TravelType;
    use MauticPlugin\HelloWorldBundle\Helper\TravelService;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    class CampaignDecisionSubscriber implements EventSubscriberInterface
    {
        public const TYPE = 'helloworld.decision';

        private TravelService $travelService;
        private RealTimeExecutioner $realTimeExecutioner;

        public function __construct(TravelService $travelService, RealTimeExecutioner $realTimeExecutioner)
        {
            $this->travelService       = $travelService;
            $this->realTimeExecutioner = $realTimeExecutioner;
        }

        public static function getSubscribedEvents()
        {
            return [
                CampaignEvents::CAMPAIGN_ON_BUILD                  => ['onCampaignBuild', 0],
                HelloWorldEvents::EVALUATE_CAMPAIGN_DECISION       => ['onEvaluateCampaignDecision', 0],
                HelloWorldEvents::CONTACT_TRAVEL_DOCUMENTS_CREATED => ['onContactTravelDocumentsCreated', 0],
            ];
        }

        public function onCampaignBuild(CampaignBuilderEvent $event)
        {
            $event->addDecision(
                self::TYPE,
                [
                    'label'       => 'helloworld.campaign.event.Decision',
                    'description' => 'helloworld.campaign.event.Decision.descr',
                    'eventName'   => HelloWorldEvents::EVALUATE_CAMPAIGN_DECISION,
                    'formType'    => TravelType::class,
                ]
            );
        }

        public function onContactTravelDocumentsCreated(TravelDocumentEvent $event)
        {
            $this->realTimeExecutioner->execute(self::TYPE, $event, 'world', $event->getWorldId());
        }

        public function onEvaluateCampaignDecision(DecisionEvent $event)
        {
            $applicableWorld     = $event->getEventConfig()->getProperty('world');
            $travelDocumentEvent = $event->getPassthrough();

            if ($applicableWorld !== $travelDocumentEvent->getWorldId()) {
                return;
            }

            $event->setAsApplicable();
            $event->setChannel('world', $travelDocumentEvent->getWorldId());
        }
    }

.. php:class:: Mautic\CampaignBundle\Events\DecisionEvent

.. php:method:: public checkContext(string $eventType)

    Checks if the given Event type matches the Event executed or evaluated. This is useful if listeners for different Campaign Events are listening to the same name defined as ``eventName`` in the Event's definition.

    :return: ``TRUE`` if the context matches.
    :returntype: bool

.. php:method:: public getEventConfig()

    Use the returned ``AbstractEventAccessor`` object to access properties configured for this Event.

    :return: Object to fetch the configuration options for the Campaign Event.
    :returntype: \\Mautic\\CampaignBundle\\EventCollector\\Accessor\\Event\\AbstractEventAccessor

.. php:method:: public getLog()

    :return: The ``LeadEventLog`` object for the Condition.
    :returntype: \\Mautic\\CampaignBundle\\Entity\\LeadEventLog

.. php:method:: public getPassthrough()

    Access context data set by ``RealTimeExecutioner::execute()``.

    :return: Returns whatever was set as the second argument to ``RealTimeExecutioner::execute()``.
    :returntype: mixed

.. php:method:: public setAsApplicable()

    Call this if the Decision is applicable to the action taken by the Contact which instructs the Campaign Engine to execute or schedule Events connected into this Decision's "action" (left) path.

    :returntype: void

.. php:method:: public setChannel(string $channel[, $channelId = null)

    Set the Channel to attribute to the Event.

    :param string $channel: Name of the Channel this Event relates to. For example, ``email``, ``page``, ``form``, and so forth.
    :param mixed $channelId: ID of the Channel entity.

    :returntype: void
