.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

.. _event listeners:

Event listeners
###############

.. vale off

Mautic leverages Symfony's EventDispatcher to execute and communicate various actions through Mautic. Plugins can hook into these to extend Mautic's capabilities. For examples, see the Plugin Extensions pages, such as :doc:`/plugin_extensions/campaigns` and :doc:`/plugin_extensions/forms`.

.. vale on

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/EventListener/LeadSubscriber.php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Mautic\LeadBundle\Event\LeadPostDeleteEvent;
    use Mautic\LeadBundle\Event\LeadPostSaveEvent;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    final class LeadSubscriber implements EventSubscriberInterface
    {
        public static function getSubscribedEvents(): array
        {
            return [
                LeadPostSaveEvent::class   => ['onLeadPostSave', 0],
                LeadPostDeleteEvent::class => ['onLeadDelete', 0],
            ];
        }

        public function onLeadPostSave(LeadPostSaveEvent $event): void
        {
            $lead = $event->getLead();

            // do something
        }

        public function onLeadDelete(LeadPostDeleteEvent $event): void
        {
            $lead = $event->getLead();

            $deletedId = $lead->deletedId;

            // do something
        }
    }

Event subscribers
*****************

The easiest way to listen to various events is to use an event subscriber. Read more about :xref:`Symfony event subscribers` in Symfony's documentation.

.. vale off

Plugin event subscribers can extend ``Symfony\Component\EventDispatcher\EventSubscriberInterface``, which gives access to commonly used dependencies and also allows registering the subscriber service through autowiring.

.. vale on
    
Available events
****************

There are many events available throughout Mautic. To discover which events Mautic dispatches, run ``bin/console debug:event-dispatcher``. With no argument, it lists every event alongside its registered listeners. Pass an event name, or a partial name, to filter the output to matching events.

.. _mautic 8 class-name event dispatch:

Subscribing by event class
==========================

Mautic dispatches most events by the event object alone, following the Symfony convention that an event's class name is its event name. Key ``getSubscribedEvents()`` on ``EventClass::class``, as the earlier ``LeadSubscriber`` example does.

A subscriber keyed on a name that Mautic doesn't dispatch under receives nothing, and Mautic doesn't raise an error or write a log entry. Some ``*Events`` classes define a constant for an event that Mautic dispatches by class, for example ``StageEvents::STAGE_ON_BUILD`` for ``StageBuilderEvent``. Key subscribers for these events on the event class, not on the constant.

Mautic dispatches the following events under a string event name, so key their subscribers on the constant from the bundle's ``*Events`` class:

* The save and delete events that share one event class across several event names, such as ``FormEvents::FORM_POST_SAVE`` and ``StageEvents::STAGE_POST_SAVE``.
* The events that a bundle or Plugin names when it registers a Campaign action, condition, or decision, a Form submit action or Form Field validation, or a Point Trigger event. Mautic dispatches these events under the ``eventName`` or ``batchEventName`` value from the registration.

To list the listeners registered for an event, run ``bin/console debug:event-dispatcher`` with the event class. Your subscriber appears in the output only when its subscription key matches the name that Mautic dispatches the event under:

.. code-block:: console

    bin/console debug:event-dispatcher "Mautic\FormBundle\Event\SubmissionEvent"

.. note::

   Mautic 8 dispatches the ``MauticPlugin\MauticSocialBundle`` Monitor and Tweet save and delete events by event class, following the :ref:`Mautic 8 class-name event dispatch <Mautic 8 class-name event dispatch>` rule. Mautic 8 removed the matching constants from ``MauticPlugin\MauticSocialBundle\SocialEvents``, so a subscriber still keyed on one, such as ``SocialEvents::TWEET_POST_SAVE``, raises an undefined-constant error. Key ``getSubscribedEvents()`` on the replacement class in the ``MauticPlugin\MauticSocialBundle\Event`` namespace instead:

   * ``MONITOR_PRE_SAVE`` - ``MonitorPreSaveEvent``
   * ``MONITOR_POST_SAVE`` - ``MonitorPostSaveEvent``
   * ``MONITOR_PRE_DELETE`` - ``MonitorPreDeleteEvent``
   * ``MONITOR_POST_DELETE`` - ``MonitorPostDeleteEvent``
   * ``MONITOR_POST_PROCESS`` - ``SocialMonitorEvent``, which Mautic already dispatched by class
   * ``TWEET_PRE_SAVE`` - ``TweetPreSaveEvent``
   * ``TWEET_POST_SAVE`` - ``TweetPostSaveEvent``
   * ``TWEET_PRE_DELETE`` - ``TweetPreDeleteEvent``
   * ``TWEET_POST_DELETE`` - ``TweetPostDeleteEvent``

   Mautic 8 also removed the ``SocialEvent`` class. The Monitor events extend ``AbstractMonitorEvent``, which provides ``getMonitoring()``, and the Tweet events extend ``AbstractTweetEvent``, which provides ``getTweet()``.

.. vale off

AssetBundle events
==================

.. vale on

Mautic dispatches the following AssetBundle events by event class. The classes live in the ``Mautic\AssetBundle\Event`` namespace:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Event class
     - Description
   * - ``AssetLoadEvent``
     - Dispatched when Mautic records an Asset download.
   * - ``RemoteAssetBrowseEvent``
     - Dispatched when Mautic lists the files of a remote storage Integration.
   * - ``AssetPreSaveEvent``
     - Dispatched before Mautic saves an Asset.
   * - ``AssetPostSaveEvent``
     - Dispatched after Mautic saves an Asset.
   * - ``AssetPreDeleteEvent``
     - Dispatched before Mautic deletes an Asset.
   * - ``AssetPostDeleteEvent``
     - Dispatched after Mautic deletes an Asset.

The save and delete events extend ``AssetEvent``, so a listener method can type-hint ``AssetEvent``.

.. vale off

DashboardBundle events
======================

.. vale on

Mautic dispatches the following DashboardBundle events by event class. The classes live in the ``Mautic\DashboardBundle\Event`` namespace:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Event class
     - Description
   * - ``WidgetTypeListEvent``
     - Dispatched when Mautic builds the list of available Widget types.
   * - ``WidgetFormEvent``
     - Dispatched when Mautic builds the configuration fields for a Widget type.
   * - ``PreLoadWidgetDetailEvent``
     - Dispatched when Mautic renders a Widget preview without data.
   * - ``GenerateWidgetDetailEvent``
     - Dispatched when Mautic loads the content of a Widget with its data.

``PreLoadWidgetDetailEvent`` and ``GenerateWidgetDetailEvent`` extend the abstract ``WidgetDetailEvent``, so a listener method can type-hint ``WidgetDetailEvent``, as in this partial subscriber:

.. code-block:: php

    <?php

    use Mautic\DashboardBundle\Event\GenerateWidgetDetailEvent;
    use Mautic\DashboardBundle\Event\WidgetDetailEvent;
    use Mautic\DashboardBundle\Event\WidgetTypeListEvent;

    public static function getSubscribedEvents(): array
    {
        return [
            WidgetTypeListEvent::class       => ['onWidgetListGenerate', 0],
            GenerateWidgetDetailEvent::class => ['onWidgetDetailGenerate', 0],
        ];
    }

    public function onWidgetDetailGenerate(WidgetDetailEvent $event): void
    {
        // Set the Widget template and data.
    }

PHP can't instantiate an abstract class, so code that creates a Widget detail event, such as a Plugin test, creates ``PreLoadWidgetDetailEvent`` or ``GenerateWidgetDetailEvent``. ``WidgetDetailEventFactory`` creates them with ``createPreLoad()`` and ``createGenerate()``.

.. vale off

FormBundle events
=================

.. vale on

Mautic dispatches the following FormBundle events by event class. The classes live in the ``Mautic\FormBundle\Event`` namespace:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Event class
     - Description
   * - ``SubmissionEvent``
     - Dispatched when Mautic processes a Form submission.
   * - ``FormBuilderEvent``
     - Dispatched when Mautic collects the Form Field types, submit actions, and Form Field validations that bundles and Plugins add.
   * - ``ObjectCollectEvent``
     - Dispatched when Mautic collects the objects that Form Fields can map to.
   * - ``FieldCollectEvent``
     - Dispatched when Mautic collects the fields of an object that Form Fields can map to.

``FormEvents`` defines the ``FORM_ON_SUBMIT``, ``FORM_ON_BUILD``, ``ON_OBJECT_COLLECT``, and ``ON_FIELD_COLLECT`` constants, but Mautic doesn't dispatch these events under them. The ``FORM_ON_SUBMIT`` string value, ``mautic.form_on_submit``, is the Webhook event type for Form submissions, so Webhook configuration uses that string.

Mautic dispatches the Form and Form Field save and delete events under ``FormEvents`` constants, such as ``FormEvents::FORM_POST_SAVE``.

.. vale off

IntegrationsBundle events
=========================

.. vale on

Mautic dispatches every event in the ``Mautic\IntegrationsBundle\Event`` namespace by event class. Key ``getSubscribedEvents()`` on the event class, for example ``InternalObjectFindEvent::class`` or ``InternalObjectOwnerEvent::class``.

Mautic dispatches ``ConfigBeforeSaveEvent`` before it saves an Integration's configuration and ``ConfigAfterSaveEvent`` after it saves the configuration. Both extend the abstract ``ConfigSaveEvent``, which provides ``getIntegrationConfiguration()`` and ``getIntegration()``, so a listener method can type-hint ``ConfigSaveEvent``.

.. _leadbundle events dispatched by event class:

.. vale off

LeadBundle events
=================

.. vale on

Mautic dispatches the LeadBundle events for Contacts, Companies, Segments, Custom Fields, Tags, notes, devices, imports, and Contact exports by their event class. Key ``getSubscribedEvents()`` on ``EventClass::class``. The field column events live in the ``Mautic\LeadBundle\Field\Event`` namespace, and the other event classes in the following table live in the ``Mautic\LeadBundle\Event`` namespace:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Area
     - Event classes
   * - Contacts
     - ``LeadPreSaveEvent``, ``LeadPostSaveEvent``, ``LeadPreDeleteEvent``, ``LeadPostDeleteEvent``, ``LeadPreBatchSaveEvent``, ``LeadPostBatchSaveEvent``, ``LeadPreMergeEvent``, ``LeadPostMergeEvent``, ``LeadIdentifiedEvent``, ``LeadChangeEvent``, ``LeadUtmTagsEvent``, ``LeadChangeCompanyEvent``, ``CategoryChangeEvent``, ``ChannelSubscriptionChange``, ``DoNotContactAddEvent``, ``DoNotContactRemoveEvent``, ``PointsChangeEvent``, ``ContactIdentificationEvent``, ``LeadTimelineEvent``, ``LeadBuildSearchEvent``
   * - Companies
     - ``CompanyPreSaveEvent``, ``CompanyPostSaveEvent``, ``CompanyPreDeleteEvent``, ``CompanyPostDeleteEvent``, ``CompanySoftDeleteEvent``, ``CompanyPreMergeEvent``, ``CompanyPostMergeEvent``, ``CompanyBuildSearchEvent``
   * - Segments
     - ``ListPreSaveEvent``, ``ListPostSaveEvent``, ``ListPreUnpublishEvent``, ``ListPreDeleteEvent``, ``ListDeleteEvent``, ``ListPostDeleteEvent``, ``ListChangeEvent``, ``ListBatchChangeEvent``, ``ListPreProcessListEvent``
   * - Segment filters
     - ``LeadListFiltersChoicesEvent``, ``LeadListFilteringEvent``, ``LeadListFiltersOperatorsEvent``, ``LeadListFiltersDecoratorDelegateEvent``, ``LeadListMergeFiltersEvent``, ``LeadListQueryBuilderGeneratedEvent``, ``SegmentOperatorQueryBuilderEvent``, ``SegmentDictionaryGenerationEvent``, ``FormAdjustmentEvent``, ``TypeOperatorsEvent``, ``FieldOperatorsEvent``, ``ListFieldChoicesEvent``
   * - Custom Fields
     - ``FieldPreSaveEvent``, ``FieldPostSaveEvent``, ``FieldPreDeleteEvent``, ``FieldPostDeleteEvent``
   * - Field columns
     - ``AddColumnEvent``, ``AddColumnBackgroundEvent``, ``UpdateColumnEvent``, ``UpdateColumnBackgroundEvent``, ``DeleteColumnEvent``, ``DeleteColumnBackgroundEvent``
   * - Tags
     - ``TagPreSaveEvent``, ``TagPostSaveEvent``, ``TagPreDeleteEvent``, ``TagPostDeleteEvent``, ``TagPreMergeEvent``, ``TagPostMergeEvent``
   * - Notes
     - ``NotePreSaveEvent``, ``NotePostSaveEvent``, ``NotePreDeleteEvent``, ``NotePostDeleteEvent``
   * - Devices
     - ``DevicePreSaveEvent``, ``DevicePostSaveEvent``, ``DevicePreDeleteEvent``, ``DevicePostDeleteEvent``
   * - Imports
     - ``ImportInitEvent``, ``ImportMappingEvent``, ``ImportProcessEvent``, ``ImportValidateEvent``, ``ImportPreSaveEvent``, ``ImportPostSaveEvent``, ``ImportPreDeleteEvent``, ``ImportPostDeleteEvent``, ``ImportBatchProcessedEvent``
   * - Contact exports
     - ``ContactExportEvent``, ``ContactExportScheduledEvent``, ``ContactExportPrepareFileEvent``, ``ContactExportSendEmailEvent``, ``ContactExportEmailSentEvent``

Several lifecycle events share a base class, so a listener method can type-hint the base class. For example, ``LeadPreSaveEvent`` and ``LeadPostSaveEvent`` both extend ``LeadEvent``. The following base classes are abstract, so code that creates one of these events, such as a Plugin test, creates the matching subclass from the preceding table:

* ``CompanyEvent``
* ``CompanyMergeEvent``
* ``ContactExportSchedulerEvent``
* ``ImportEvent``
* ``LeadDeviceEvent``
* ``LeadFieldEvent``
* ``LeadListEvent``
* ``LeadMergeEvent``
* ``LeadNoteEvent``
* ``SaveBatchLeadsEvent``
* ``TagEvent``
* ``TagMergeEvent``

Mautic creates a separate event object for the events before and after a save, delete, or merge. A value that a listener sets on the earlier event isn't available to listeners of the later one. To dispatch a Custom Field event from your own code, pass the ``LeadFieldEvent`` subclass to ``Mautic\LeadBundle\Field\Dispatcher\FieldSaveDispatcher::dispatchEvent()``.

The following ``LeadEvents`` constants hold Webhook event types. Mautic doesn't dispatch events under these names, so subscribe to the event class:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Webhook event type constant
     - Event class to subscribe to
   * - ``LEAD_POST_SAVE``
     - ``LeadPostSaveEvent``
   * - ``LEAD_POST_DELETE``
     - ``LeadPostDeleteEvent``
   * - ``LEAD_POINTS_CHANGE``
     - ``PointsChangeEvent``
   * - ``LEAD_COMPANY_CHANGE``
     - ``LeadChangeCompanyEvent``
   * - ``LEAD_LIST_CHANGE``
     - ``ListChangeEvent``
   * - ``CHANNEL_SUBSCRIPTION_CHANGED``
     - ``ChannelSubscriptionChange``
   * - ``COMPANY_POST_SAVE``
     - ``CompanyPostSaveEvent``
   * - ``COMPANY_POST_DELETE``
     - ``CompanyPostDeleteEvent``

.. vale off

UserBundle events
=================

.. vale on

Mautic dispatches the following UserBundle events by event class. The classes live in the ``Mautic\UserBundle\Event`` namespace:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Event class
     - Description
   * - ``LoginEvent``
     - Dispatched when a User logs in.
   * - ``LogoutEvent``
     - Dispatched when a User logs out.
   * - ``PreAuthenticationEvent``
     - Dispatched when Mautic asks a Plugin to authenticate a login request with an external service.
   * - ``FormAuthenticationEvent``
     - Dispatched when Mautic asks a Plugin to authenticate the username and password that a User enters to log in.
   * - ``AuthenticationContentEvent``
     - Dispatched when Mautic renders the login screen, so a listener can add HTML to it.
   * - ``PasswordStrengthValidateEvent``
     - Dispatched when Mautic validates the strength of a password.
   * - ``PreSaveUserEvent``, ``PostSaveUserEvent``
     - Dispatched before and after Mautic saves a User.
   * - ``PreDeleteUserEvent``, ``PostDeleteUserEvent``
     - Dispatched before and after Mautic deletes a User.
   * - ``PreSaveRoleEvent``, ``PostSaveRoleEvent``
     - Dispatched before and after Mautic saves a Role.
   * - ``PreDeleteRoleEvent``, ``PostDeleteRoleEvent``
     - Dispatched before and after Mautic deletes a Role.

``UserEvent``, ``RoleEvent``, and ``AuthenticationEvent`` are abstract base classes. A listener method can type-hint the base class, but code that creates one of these events, such as a Plugin test, creates the concrete subclass.

.. vale off

WebhookBundle events
====================

.. vale on

Mautic dispatches the following WebhookBundle events by event class. The classes live in the ``Mautic\WebhookBundle\Event`` namespace:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Event class
     - Description
   * - ``WebhookBuilderEvent``
     - Dispatched when Mautic collects the Webhook event types that bundles and Plugins add.
   * - ``WebhookQueueEvent``
     - Dispatched when Mautic creates a Webhook queue entry, before it saves the entry.
   * - ``WebhookRequestEvent``
     - Dispatched before Mautic sends the request for a Campaign's Webhook action.
   * - ``WebhookNotificationEvent``
     - Dispatched before Mautic sends a notification Email about a Webhook. A listener can stop the notification.
   * - ``WebhookPreSaveEvent``, ``WebhookPostSaveEvent``
     - Dispatched before and after Mautic saves a Webhook.
   * - ``WebhookPreDeleteEvent``, ``WebhookPostDeleteEvent``
     - Dispatched before and after Mautic deletes a Webhook.
   * - ``WebhookKillEvent``
     - Dispatched after Mautic stops a Webhook by deactivating it.

``WebhookKillEvent`` and the save and delete events extend the abstract ``WebhookEvent``, so a listener method can type-hint ``WebhookEvent``.

.. vale off

DynamicContentBundle, MauticFocusBundle, StageBundle, and StatsBundle events
============================================================================

.. vale on

Mautic dispatches the following events by event class:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Event class
     - Description
   * - ``Mautic\DynamicContentBundle\Event\ContactFiltersEvaluateEvent``
     - Dispatched when Mautic evaluates the filters of a Dynamic Content item for a Contact.
   * - ``MauticPlugin\MauticFocusBundle\Event\FocusViewEvent``
     - Dispatched when Mautic records a view of a Focus Item.
   * - ``Mautic\StageBundle\Event\StageBuilderEvent``
     - Dispatched when Mautic collects the Stage actions that bundles and Plugins add.
   * - ``Mautic\StatsBundle\Event\AggregateStatRequestEvent``
     - Dispatched when Mautic fetches aggregate statistics for a date range.

MauticFocusBundle is a Plugin under ``plugins/``, so its event classes use the ``MauticPlugin`` top-level namespace. Mautic dispatches the Stage save and delete events under ``StageEvents`` constants, such as ``StageEvents::STAGE_POST_SAVE``, and the Focus Item save, delete, and token replacement events under ``FocusEvents`` constants.

Custom events
*************

A Plugin can create and dispatch its own events. Since Symfony 4.3, the event class name is the event name, so a custom event doesn't need a separate class of event name constants.

Custom events require the following:

#. An event class that extends ``Symfony\Contracts\EventDispatcher\Event``. The event object contains all data required for listeners to process the event.

   .. code-block:: php

       <?php
       // plugins\HelloWorldBundle\Event\ArmageddonEvent.php

       namespace MauticPlugin\HelloWorldBundle\Event;

       use MauticPlugin\HelloWorldBundle\Entity\World;
       use Symfony\Contracts\EventDispatcher\Event;

       final class ArmageddonEvent extends Event
       {
           private bool $falseAlarm = false;

           public function __construct(private World $world)
           {
           }

           public function shouldPanic(): bool
           {
               return 'earth' === $this->world->getName();
           }

           public function setIsFalseAlarm(): void
           {
               $this->falseAlarm = true;
           }

           public function getIsFalseAlarm(): bool
           {
               return $this->falseAlarm;
           }
       }

#. The code that dispatches the event object through the ``event_dispatcher`` service. Pass the event object as the only argument.

   .. code-block:: php

       <?php

       // $dispatcher is an injected Symfony\Component\EventDispatcher\EventDispatcherInterface
       if ($dispatcher->hasListeners(ArmageddonEvent::class)) {
           $event = $dispatcher->dispatch(new ArmageddonEvent($world));

           if ($event->shouldPanic()) {
               throw new \Exception('Run for the hills!');
           }
       }

   Don't pass an event name as a second argument, as in ``$dispatcher->dispatch($event, HelloWorldEvents::ARMAGEDDON)``. Mautic's static analysis rules flag that call as a ``mautic.singleArgumentDispatch`` error when you run ``composer phpstan`` on your Plugin.

#. Subscribers that listen on the event class.

   .. code-block:: php

       <?php
       // plugins\HelloWorldBundle\EventListener\ArmageddonSubscriber.php

       namespace MauticPlugin\HelloWorldBundle\EventListener;

       use MauticPlugin\HelloWorldBundle\Event\ArmageddonEvent;
       use Symfony\Component\EventDispatcher\EventSubscriberInterface;

       final class ArmageddonSubscriber implements EventSubscriberInterface
       {
           public static function getSubscribedEvents(): array
           {
               return [
                   ArmageddonEvent::class => ['onArmageddon', 0],
               ];
           }

           public function onArmageddon(ArmageddonEvent $event): void
           {
               // do something
           }
       }

Tag merge events
****************

Mautic dispatches events when two Tags merge. Use these events to sync Tag changes to external systems, log merge operations, or trigger custom business logic.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Event class
     - Description
   * - ``Mautic\LeadBundle\Event\TagPreMergeEvent``
     - Dispatched before two Tags merge.
   * - ``Mautic\LeadBundle\Event\TagPostMergeEvent``
     - Dispatched after two Tags merge.

Both event classes extend ``Mautic\LeadBundle\Event\TagMergeEvent`` and provide the following methods:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Method
     - Description
   * - ``getPrimaryTag()``
     - Returns the Tag entity that remains after the merge.
   * - ``getSecondaryTag()``
     - Returns the Tag entity that merges into the primary Tag and then gets deleted.

Example subscriber
==================

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/EventListener/TagMergeSubscriber.php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Mautic\LeadBundle\Event\TagPostMergeEvent;
    use Mautic\LeadBundle\Event\TagPreMergeEvent;
    use Psr\Log\LoggerInterface;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    final class TagMergeSubscriber implements EventSubscriberInterface
    {
        public function __construct(private LoggerInterface $logger)
        {
        }

        public static function getSubscribedEvents(): array
        {
            return [
                TagPreMergeEvent::class  => ['onTagPreMerge', 0],
                TagPostMergeEvent::class => ['onTagPostMerge', 0],
            ];
        }

        public function onTagPreMerge(TagPreMergeEvent $event): void
        {
            $primaryTag   = $event->getPrimaryTag();
            $secondaryTag = $event->getSecondaryTag();

            $this->logger->info(sprintf(
                'About to merge tag "%s" into "%s"',
                $secondaryTag->getTag(),
                $primaryTag->getTag()
            ));
        }

        public function onTagPostMerge(TagPostMergeEvent $event): void
        {
            $primaryTag   = $event->getPrimaryTag();
            $secondaryTag = $event->getSecondaryTag();

            $this->logger->info(sprintf(
                'Tag "%s" merged into "%s"',
                $secondaryTag->getTag(),
                $primaryTag->getTag()
            ));

            // Sync to external CRM, analytics platform, etc.
        }
    }
