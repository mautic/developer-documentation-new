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
    //plugins\HelloWorldBundle\EventListener\LeadSubscriber

    namespace MauticPlugin\HelloWorldBundle\EventListener;  

    use Mautic\LeadBundle\LeadEvent;  
    use Mautic\LeadBundle\LeadEvents;  
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;  

    final class LeadSubscriber extends EventSubscriberInterface  
    {  
        static public function getSubscribedEvents(): array  
        {  
            return [  
                LeadEvents::LEAD_POST_SAVE     => ['onLeadPostSave', 0],  
                LeadEvents::LEAD_POST_DELETE   => ['onLeadDelete', 0],  
            ];  
        }  
    
        public function onLeadPostSave(LeadEvent $event): void  
        {  
            $lead = $event->getLead();  
            
            // do something  
        }  
    
        public function onLeadDelete(LeadEvent $event): void  
        {  
            $lead = $event->getLead();  
            
            $deletedId = $lead->deletedId;  
            
            // do something  
        }  
    }  
    // ...

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

Mautic 8: class-name event dispatch
===================================

Since Mautic 8, CoreBundle dispatches selected events by the event object, following the Symfony 4.3+ convention, so you subscribe on ``EventClass::class`` instead of the ``CoreEvents`` string constant.

A subscriber still keyed on the old constant or the raw string silently receives nothing - no error, no log entry.

To find the name Mautic dispatches an event under, and to confirm a re-key, run ``bin/console debug:event-dispatcher``, optionally passing the event class:

.. code-block:: console

    bin/console debug:event-dispatcher "Mautic\CoreBundle\Event\MenuEvent"

:xref:`UPGRADE_GUIDE_8` maps each old CoreBundle event name and ``CoreEvents`` constant to its new event class.

.. note::

   In Mautic 8, Mautic dispatches the ``ContactFiltersEvaluateEvent`` by class name, so key ``getSubscribedEvents()`` on ``ContactFiltersEvaluateEvent::class``. See :ref:`Mautic 8 class-name event dispatch <Mautic 8 class-name event dispatch>` for the general rationale.

.. note::

   The ``Mautic\UserBundle`` User and Role save and delete lifecycle events follow the :ref:`Mautic 8 class-name event dispatch <Mautic 8 class-name event dispatch>` rule. Key ``getSubscribedEvents()`` on the event class - for example ``PostSaveUserEvent::class`` in the ``Mautic\UserBundle\Event`` namespace - not on a ``UserEvents`` constant. Mautic 8 removed the eight User and Role save and delete constants from ``Mautic\UserBundle\UserEvents``, so a subscriber still keyed on one, such as ``UserEvents::USER_POST_SAVE``, raises an undefined-constant error instead of silently receiving nothing. The base ``UserEvent`` and ``RoleEvent`` classes are now abstract, so dispatch or type-hint the concrete ``Pre*`` or ``Post*`` subclass. Mautic 8 leaves the authentication constants, such as ``USER_LOGIN`` and ``USER_LOGOUT``, in place, so they still dispatch by their string names. The ``UPGRADE-8.0.md`` guide lists each removed constant with its replacement event class.

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

.. note::

   Starting in Mautic 8, Mautic dispatches some events by their event class rather than the ``*Events`` string constant. See :ref:`Mautic 8 class-name event dispatch <Mautic 8 class-name event dispatch>`.

Form, Integration, and Focus events dispatched by class name in Mautic 8
========================================================================

Seven events across three bundles moved to class-name dispatch in Mautic 8. Those bundles are FormBundle, IntegrationsBundle, and MauticFocusBundle. You now subscribe using the event class shown in the table below.

.. list-table::
   :header-rows: 1
   :widths: 10 30 30 30

   * - Bundle
     - Old event name
     - Constant
     - New event class
   * - FormBundle
     - ``mautic.form_on_submit``
     - ``FormEvents::FORM_ON_SUBMIT``
     - ``Mautic\FormBundle\Event\SubmissionEvent``
   * - FormBundle
     - ``mautic.form_on_build``
     - ``FormEvents::FORM_ON_BUILD``
     - ``Mautic\FormBundle\Event\FormBuilderEvent``
   * - FormBundle
     - ``mautic.form.on_object_collect``
     - ``FormEvents::ON_OBJECT_COLLECT``
     - ``Mautic\FormBundle\Event\ObjectCollectEvent``
   * - FormBundle
     - ``mautic.form.on_field_collect``
     - ``FormEvents::ON_FIELD_COLLECT``
     - ``Mautic\FormBundle\Event\FieldCollectEvent``
   * - IntegrationsBundle
     - ``mautic.integration.INTEGRATION_FIND_INTERNAL_RECORDS``
     - ``IntegrationEvents::INTEGRATION_FIND_INTERNAL_RECORDS``
     - ``Mautic\IntegrationsBundle\Event\InternalObjectFindEvent``
   * - IntegrationsBundle
     - ``mautic.integration.INTEGRATION_FIND_OWNER_IDS``
     - ``IntegrationEvents::INTEGRATION_FIND_OWNER_IDS``
     - ``Mautic\IntegrationsBundle\Event\InternalObjectOwnerEvent``
   * - MauticFocusBundle
     - ``mautic.focus.on_view``
     - ``FocusEvents::FOCUS_ON_VIEW``
     - ``MauticPlugin\MauticFocusBundle\Event\FocusViewEvent``

The FormBundle event classes live in the ``Mautic\FormBundle\Event`` namespace and the IntegrationsBundle event classes in the ``Mautic\IntegrationsBundle\Event`` namespace, both under ``app/bundles/``. MauticFocusBundle is a Plugin under ``plugins/``, so its event class is in the ``MauticPlugin\MauticFocusBundle\Event`` namespace. Note the different top-level namespace.

Only these seven events changed. Mautic keeps an event as a string constant when several event names share one event object, or when the event crosses bundle boundaries, so those events still dispatch by the string name. For example, the IntegrationsBundle ``INTEGRATION_CONFIG_*`` before-and-after pair reuses one ``ConfigSaveEvent``, and FormBundle's create, read, update, and delete group constants do the same. For those, the guidance in the :ref:`Available events <Plugins/event_listeners:Available events>` intro to always use the event constants still holds.

.. warning::

   * The string value of ``FormEvents::FORM_ON_SUBMIT`` is ``mautic.form_on_submit``, which is also the persisted Webhook event-type identifier in ``WebhookSubscriber``. Only the event-dispatch subscription moved to ``SubmissionEvent::class``. This change doesn't affect Webhook configuration or the type identifier, so only your event-subscription code needs to change.
   * ``FocusEventTypes::FOCUS_ON_VIEW`` is a separate stat-type identifier, and the change doesn't affect it. Only ``FocusEvents::FOCUS_ON_VIEW`` converted to class-name dispatch. Don't confuse the two.

The following partial subscribers show the change for the FormBundle ``SubmissionEvent``. Each is a fragment, and only the ``getSubscribedEvents()`` key changes. Here's the pre-Mautic 8 subscriber:

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/EventListener/FormSubmitSubscriber.php

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Mautic\FormBundle\Event\SubmissionEvent;
    use Mautic\FormBundle\FormEvents;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    final class FormSubmitSubscriber implements EventSubscriberInterface
    {
        public static function getSubscribedEvents(): array
        {
            return [
                FormEvents::FORM_ON_SUBMIT => ['onFormSubmit', 0],
            ];
        }

        public function onFormSubmit(SubmissionEvent $event): void
        {
            // ...
        }
    }
    // ...

Here's the Mautic 8 subscriber:

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/EventListener/FormSubmitSubscriber.php

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Mautic\FormBundle\Event\SubmissionEvent;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    final class FormSubmitSubscriber implements EventSubscriberInterface
    {
        public static function getSubscribedEvents(): array
        {
            return [
                SubmissionEvent::class => ['onFormSubmit', 0],
            ];
        }

        public function onFormSubmit(SubmissionEvent $event): void
        {
            // ...
        }
    }
    // ...

.. tip::

   Run ``bin/console debug:event-dispatcher`` to list the listeners registered for an event, optionally passing the event class to scope the output to one event. Run it before and after re-keying to confirm the subscriber binds to the new event-class name.

   .. code-block:: console

      bin/console debug:event-dispatcher
      bin/console debug:event-dispatcher Mautic\FormBundle\Event\SubmissionEvent

.. note::

   Starting in Mautic 8, Mautic dispatches the LeadBundle events listed below by their event class rather than the ``LeadEvents::*`` string constant, so you subscribe to the event class shown in the table. For the general convention and how to re-key an affected subscriber or tagged listener, see :ref:`Mautic 8 class-name event dispatch <Mautic 8 class-name event dispatch>`.

LeadBundle events dispatched by class name in Mautic 8
======================================================

.. list-table::
   :header-rows: 1
   :widths: 34 33 33

   * - Old event name
     - ``LeadEvents`` constant
     - New event class
   * - ``mautic.lead_utmtags_add``
     - ``LEAD_UTMTAGS_ADD``
     - ``LeadUtmTagsEvent``
   * - ``mautic.lead_category_change``
     - ``LEAD_CATEGORY_CHANGE``
     - ``CategoryChangeEvent``
   * - ``mautic.lead_channel_subscription_changed``
     - ``CHANNEL_SUBSCRIPTION_CHANGED``
     - ``ChannelSubscriptionChange``
   * - ``mautic.lead_build_search_commands``
     - ``LEAD_BUILD_SEARCH_COMMANDS``
     - ``LeadBuildSearchEvent``
   * - ``mautic.company_build_search_commands``
     - ``COMPANY_BUILD_SEARCH_COMMANDS``
     - ``CompanyBuildSearchEvent``
   * - ``mautic.adjust_filter_form_type_for_field``
     - ``ADJUST_FILTER_FORM_TYPE_FOR_FIELD``
     - ``FormAdjustmentEvent``
   * - ``mautic.collect_operators_for_field_type``
     - ``COLLECT_OPERATORS_FOR_FIELD_TYPE``
     - ``TypeOperatorsEvent``
   * - ``mautic.collect_operators_for_field``
     - ``COLLECT_OPERATORS_FOR_FIELD``
     - ``FieldOperatorsEvent``
   * - ``mautic.collect_filter_choices_for_list_field_type``
     - ``COLLECT_FILTER_CHOICES_FOR_LIST_FIELD_TYPE``
     - ``ListFieldChoicesEvent``
   * - ``mautic.list_filters_delegate_decorator``
     - ``SEGMENT_ON_DECORATOR_DELEGATE``
     - ``LeadListFiltersDecoratorDelegateEvent``
   * - ``mautic.list_filters_merge``
     - ``LIST_FILTERS_MERGE``
     - ``LeadListMergeFiltersEvent``
   * - ``mautic.list_filters_operators_on_generate``
     - ``LIST_FILTERS_OPERATORS_ON_GENERATE``
     - ``LeadListFiltersOperatorsEvent``
   * - ``mautic.list_filters_operator_querybuilder_on_generate``
     - ``LIST_FILTERS_OPERATOR_QUERYBUILDER_ON_GENERATE``
     - ``SegmentOperatorQueryBuilderEvent``
   * - ``mautic.list_filters_querybuilder_generated``
     - ``LIST_FILTERS_QUERYBUILDER_GENERATED``
     - ``LeadListQueryBuilderGeneratedEvent``
   * - ``mautic.lead_import_on_initialize``
     - ``IMPORT_ON_INITIALIZE``
     - ``ImportInitEvent``
   * - ``mautic.lead_import_on_field_mapping``
     - ``IMPORT_ON_FIELD_MAPPING``
     - ``ImportMappingEvent``
   * - ``mautic.lead_import_on_process``
     - ``IMPORT_ON_PROCESS``
     - ``ImportProcessEvent``
   * - ``mautic.lead_import_on_validate``
     - ``IMPORT_ON_VALIDATE``
     - ``ImportValidateEvent``
   * - ``mautic.lead_field_pre_add_column``
     - ``LEAD_FIELD_PRE_ADD_COLUMN``
     - ``AddColumnEvent``
   * - ``mautic.lead_field_pre_add_column_background_job``
     - ``LEAD_FIELD_PRE_ADD_COLUMN_BACKGROUND_JOB``
     - ``AddColumnBackgroundEvent``
   * - ``mautic.lead_field_pre_update_column``
     - ``LEAD_FIELD_PRE_UPDATE_COLUMN``
     - ``UpdateColumnEvent``
   * - ``mautic.lead_field_pre_update_column_background_job``
     - ``LEAD_FIELD_PRE_UPDATE_COLUMN_BACKGROUND_JOB``
     - ``UpdateColumnBackgroundEvent``
   * - ``mautic.lead_field_pre_delete_column``
     - ``LEAD_FIELD_PRE_DELETE_COLUMN``
     - ``DeleteColumnEvent``
   * - ``mautic.lead_field_pre_delete_column_background_job``
     - ``LEAD_FIELD_PRE_DELETE_COLUMN_BACKGROUND_JOB``
     - ``DeleteColumnBackgroundEvent``

Six field-column classes live in the ``Mautic\LeadBundle\Field\Event`` namespace:

* ``AddColumnEvent``
* ``AddColumnBackgroundEvent``
* ``UpdateColumnEvent``
* ``UpdateColumnBackgroundEvent``
* ``DeleteColumnEvent``
* ``DeleteColumnBackgroundEvent``

The other 18 live in the ``Mautic\LeadBundle\Event`` namespace.

``CHANNEL_SUBSCRIPTION_CHANGED`` is the one exception to watch. Its event dispatch and subscription move to the ``ChannelSubscriptionChange`` event class, but its string value ``mautic.lead_channel_subscription_changed`` stays the Webhook type identifier. Webhook configuration and receivers keep working, so you only need to change your event-subscription code.

These illustrative fragments show the change inside an existing subscriber's ``getSubscribedEvents()`` method, using the ``LEAD_BUILD_SEARCH_COMMANDS`` event. Before Mautic 8, the subscriber keys on the constant:

.. code-block:: php

    <?php

    use Mautic\LeadBundle\LeadEvents;

    public static function getSubscribedEvents(): array
    {
        return [
            LeadEvents::LEAD_BUILD_SEARCH_COMMANDS => ['onBuildSearchCommands', 0],
        ];
    }

In Mautic 8, the subscriber keys on the event class:

.. code-block:: php

    <?php

    use Mautic\LeadBundle\Event\LeadBuildSearchEvent;

    public static function getSubscribedEvents(): array
    {
        return [
            LeadBuildSearchEvent::class => ['onBuildSearchCommands', 0],
        ];
    }

.. tip::

   To list the listeners registered for an event, run the Symfony console command ``bin/console debug:event-dispatcher``, optionally passing the event class to list only that event's listeners. Run it before and after re-keying a subscriber to confirm the subscriber now appears under the new event-class name.

.. note::

   The ``Mautic\AssetBundle\AssetEvents`` family follows the :ref:`Mautic 8 class-name event dispatch <Mautic 8 class-name event dispatch>` rule. Key ``getSubscribedEvents()`` on the event class - for example ``AssetLoadEvent::class`` in the ``Mautic\AssetBundle\Event`` namespace - not on the ``AssetEvents::*`` constant or the raw string name such as ``mautic.asset_on_load``. Mautic also removed the dead ``ASSET_ON_UPLOAD`` constant, which it never dispatched or listened to.

The following table is the complete migration reference for AssetBundle event subscribers. It maps each old event name and ``AssetEvents`` constant to its new event class. All new event classes live in the ``Mautic\AssetBundle\Event`` namespace, and ``app/bundles/AssetBundle/AssetEvents.php`` defines the constants.

.. list-table::
   :header-rows: 1
   :widths: 40 35 25

   * - Old event name
     - AssetEvents constant
     - New event class
   * - ``mautic.asset_on_load``
     - ``AssetEvents::ASSET_ON_LOAD``
     - ``AssetLoadEvent``
   * - ``mautic.asset_on_remote_browse``
     - ``AssetEvents::ASSET_ON_REMOTE_BROWSE``
     - ``RemoteAssetBrowseEvent``
   * - ``mautic.asset_pre_save``
     - ``AssetEvents::ASSET_PRE_SAVE``
     - ``AssetPreSaveEvent``
   * - ``mautic.asset_post_save``
     - ``AssetEvents::ASSET_POST_SAVE``
     - ``AssetPostSaveEvent``
   * - ``mautic.asset_pre_delete``
     - ``AssetEvents::ASSET_PRE_DELETE``
     - ``AssetPreDeleteEvent``
   * - ``mautic.asset_post_delete``
     - ``AssetEvents::ASSET_POST_DELETE``
     - ``AssetPostDeleteEvent``

.. note::

   The WebhookBundle applies the :ref:`Mautic 8 class-name event dispatch <Mautic 8 class-name event dispatch>` change. Mautic 8 converted only ``WebhookBuilderEvent``, ``WebhookQueueEvent``, and ``WebhookRequestEvent``, so key ``getSubscribedEvents()`` on the event class, for example ``WebhookBuilderEvent::class``, not on the matching ``Mautic\WebhookBundle\WebhookEvents`` constant.

   ``WebhookEvent`` - dispatched for ``WEBHOOK_PRE_SAVE``, ``WEBHOOK_POST_SAVE``, ``WEBHOOK_PRE_DELETE``, ``WEBHOOK_POST_DELETE``, and ``WEBHOOK_KILL`` - still dispatches by its ``WebhookEvents`` constants, so keep keying on the constant for those.

.. note::

   In Mautic 8, ``Mautic\IntegrationsBundle\Event`` events whose class maps to a single event name dispatch by the event object alone. Key ``getSubscribedEvents()`` on the event class - for example ``InternalObjectEvent::class`` - for those. Families whose class serves several names, such as ``ConfigSaveEvent`` and ``InternalObjectFindEvent``, still dispatch by their ``IntegrationEvents`` constants, so keep keying on the constant for those. For why this changed and what breaks if you don't re-key, see :ref:`Mautic 8 class-name event dispatch <Mautic 8 class-name event dispatch>`.

.. vale off

Since Mautic 8, some bundles dispatch an event by the event object alone rather than by a string constant, so you key ``getSubscribedEvents()`` on the event class. See :ref:`Mautic 8 class-name event dispatch <Mautic 8 class-name event dispatch>` for the general rule. The following content covers the StageBundle and DashboardBundle events.

.. note::

   Since Mautic 8, Mautic dispatches ``Mautic\StageBundle\Event\StageBuilderEvent`` by the event object alone. Key ``getSubscribedEvents()`` on ``StageBuilderEvent::class``, not on ``StageEvents::STAGE_ON_BUILD`` or the string ``mautic.stage_on_build``. Those constants remain for backward compatibility but no longer dispatch this event. Mautic still dispatches the ``StageEvent`` CRUD group, ``STAGE_ON_ACTION``, and ``ON_CAMPAIGN_BATCH_ACTION`` by their string constants.

   .. code-block:: php

      return [
          StageBuilderEvent::class => ['onStageBuild', 0],
          // ...
      ];

.. vale on

.. note::

   The DashboardBundle applies the :ref:`Mautic 8 class-name event dispatch <Mautic 8 class-name event dispatch>` change to all four Widget events and removes the ``Mautic\DashboardBundle\DashboardEvents`` class. A subscriber that still references a ``DashboardEvents`` constant raises a ``Class "Mautic\DashboardBundle\DashboardEvents" not found`` error, and a subscriber keyed on a raw string name such as ``mautic.dashboard_on_widget_detail_generate`` silently receives nothing.

The following table maps each old event name and ``DashboardEvents`` constant to the event class to key ``getSubscribedEvents()`` on. All event classes live in the ``Mautic\DashboardBundle\Event`` namespace:

.. list-table::
   :header-rows: 1
   :widths: 40 35 25

   * - Old event name
     - Removed ``DashboardEvents`` constant
     - New event class
   * - ``mautic.dashboard_on_widget_list_generate``
     - ``DASHBOARD_ON_MODULE_LIST_GENERATE``
     - ``WidgetTypeListEvent``
   * - ``mautic.dashboard_on_widget_form_generate``
     - ``DASHBOARD_ON_MODULE_FORM_GENERATE``
     - ``WidgetFormEvent``
   * - ``mautic.dashboard_on_widget_detail_pre_load``
     - ``DASHBOARD_ON_MODULE_DETAIL_PRE_LOAD``
     - ``PreLoadWidgetDetailEvent``
   * - ``mautic.dashboard_on_widget_detail_generate``
     - ``DASHBOARD_ON_MODULE_DETAIL_GENERATE``
     - ``GenerateWidgetDetailEvent``

Mautic previously dispatched ``WidgetDetailEvent`` under both detail event names. ``WidgetDetailEvent`` is now an abstract base class with two ``final`` subclasses, so each detail event has its own class:

* ``PreLoadWidgetDetailEvent`` renders a Widget preview without data.
* ``GenerateWidgetDetailEvent`` loads the Widget content with its data.

Your listener methods can keep the ``WidgetDetailEvent`` type hint, because both subclasses extend it. Only the subscription keys change:

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

PHP can't instantiate an abstract class, so code that creates a ``WidgetDetailEvent`` directly, such as a Plugin test, must create ``GenerateWidgetDetailEvent`` or ``PreLoadWidgetDetailEvent`` instead. ``WidgetDetailEventFactory`` replaces its ``create()`` method with ``createPreLoad()`` and ``createGenerate()``.

.. note::

   Since Mautic 8.0, Mautic dispatches the authentication content and Segment filtering events by class name - see :ref:`Mautic 8 class-name event dispatch <Mautic 8 class-name event dispatch>`. To inject HTML into the login UI, key ``getSubscribedEvents()`` on ``Mautic\UserBundle\Event\AuthenticationContentEvent::class``. To apply custom Segment filter logic, key it on ``Mautic\LeadBundle\Event\LeadListFilteringEvent::class``. The ``UserEvents::USER_AUTHENTICATION_CONTENT`` and ``LeadEvents::LIST_FILTERS_ON_FILTERING`` constants remain defined, but a subscriber still keyed on either one silently receives nothing.

Custom events
*************

A Plugin can create and dispatch its own events. 

Custom events require the following:

#. The class defines the available events for the Plugin using a ``final class`` with constants.

   .. code-block:: php

       <?php
       // plugins\HelloWorldBundle\HelloWorldEvents.php
    
       namespace MauticPlugin\HelloWorldBundle;
    
       final class HelloWorldEvents
       {
           /**
            * The giant meteor that dooms a world triggers the helloworld.armageddon event
            *
            * The event listener receives a MauticPlugin\HelloWorldBundle\Event\ArmageddonEvent instance.
            *
            * @var string
            */
           const ARMAGEDDON = 'helloworld.armageddon';
       }
       // ...


#. The listeners receive the ``Event`` class. This class should extend ``Symfony\Contracts\EventDispatcher\Event``. The event object contains all data required for listeners to process the event.

   .. code-block:: php

       <?php  
    // plugins\HelloWorldBundle\Event\ArmageddonEvent.php  
    
       namespace MauticPlugin\HelloWorldBundle\Event;  
    
       use Symfony\Contracts\EventDispatcher\Event;  
       use MauticPlugin\HelloWorldBundle\Entity\World;  
    
       final class ArmageddonEvent extends Event  
       {  
           private bool $falseAlarm = false;  
         
           public function __construct(private World $world)
           {  
               $this->world = $world;
           }  
        
           public function shouldPanic(): bool  
           {  
               return ('earth' == $this->world->getName());  
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
       // ...


#. The code that dispatches the event where appropriate using the ``event_dispatcher`` service.

   .. code-block:: php

       <?php
    
       $dispatcher = $this->get('event_dispatcher');
       if ($dispatcher->hasListeners   (HelloWorldEvents::ARMAGEDDON)) {
           $event = $dispatcher->dispatch(HelloWorldEvents::ARMAGEDDON, new ArmageddonEvent($world));

           if ($event->shouldPanic()) {
               throw new \Exception("Run for the hills!");
           }
       }

Tag merge events
****************

Mautic dispatches events when two Tags merge. Use these events to sync Tag changes to external systems, log merge operations, or trigger custom business logic.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Event constant
     - Description
   * - ``LeadEvents::TAG_PRE_MERGE``
     - Dispatched before two Tags merge. The event string is ``mautic.lead_tag_pre_merge``.
   * - ``LeadEvents::TAG_POST_MERGE``
     - Dispatched after two Tags merge. The event string is ``mautic.lead_tag_post_merge``.

Both events receive a ``Mautic\LeadBundle\Event\TagMergeEvent`` instance with the following methods:

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

    use Mautic\LeadBundle\Event\TagMergeEvent;
    use Mautic\LeadBundle\LeadEvents;
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
                LeadEvents::TAG_PRE_MERGE  => ['onTagPreMerge', 0],
                LeadEvents::TAG_POST_MERGE => ['onTagPostMerge', 0],
            ];
        }

        public function onTagPreMerge(TagMergeEvent $event): void
        {
            $primaryTag   = $event->getPrimaryTag();
            $secondaryTag = $event->getSecondaryTag();

            $this->logger->info(sprintf(
                'About to merge tag "%s" into "%s"',
                $secondaryTag->getTag(),
                $primaryTag->getTag()
            ));
        }

        public function onTagPostMerge(TagMergeEvent $event): void
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
