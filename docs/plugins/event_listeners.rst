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

Since Mautic 8, some bundles dispatch an event by the event object alone rather than by a string constant, so you key ``getSubscribedEvents()`` on the event class. See :ref:`Mautic 8 class-name event dispatch <Mautic 8 class-name event dispatch>` for the general rule. The notes below cover the StageBundle and DashboardBundle events.

.. note::

   Since Mautic 8, Mautic dispatches ``Mautic\StageBundle\Event\StageBuilderEvent`` by the event object alone. Key ``getSubscribedEvents()`` on ``StageBuilderEvent::class``, not on ``StageEvents::STAGE_ON_BUILD`` or the string ``mautic.stage_on_build``. Those constants remain for backward compatibility but no longer dispatch this event. Mautic still dispatches the ``StageEvent`` CRUD group, ``STAGE_ON_ACTION``, and ``ON_CAMPAIGN_BATCH_ACTION`` by their string constants.

   .. code-block:: php

      return [
          StageBuilderEvent::class => ['onStageBuild', 0],
          // ...
      ];

.. note::

   Since Mautic 8, Mautic dispatches two DashboardBundle widget events by the event object alone. Key ``getSubscribedEvents()`` on the event class rather than on the former constant. The classes live in ``Mautic\DashboardBundle\Event``.

   .. list-table::
      :header-rows: 1
      :widths: 50 50

      * - Former event constant
        - Mautic 8 event class - subscription key
      * - ``DASHBOARD_ON_MODULE_LIST_GENERATE``
        - ``WidgetTypeListEvent``
      * - ``DASHBOARD_ON_MODULE_FORM_GENERATE``
        - ``WidgetFormEvent``

   The former constants remain for backward compatibility but no longer dispatch these events. Mautic still dispatches ``DASHBOARD_ON_MODULE_DETAIL_GENERATE`` and ``DASHBOARD_ON_MODULE_DETAIL_PRE_LOAD`` - both sharing ``WidgetDetailEvent`` - by their string constants.

   .. code-block:: php

      return [
          WidgetTypeListEvent::class => ['onWidgetListGenerate', 0],
          WidgetFormEvent::class     => ['onWidgetFormGenerate', 0],
          // ...
      ];

.. vale on

.. note::

   Since Mautic 8.0, Mautic dispatches the authentication content and Segment filtering events by class name - see :ref:`Mautic 8 class-name event dispatch <Mautic 8 class-name event dispatch>`. To inject HTML into the login UI, key ``getSubscribedEvents()`` on ``Mautic\UserBundle\Event\AuthenticationContentEvent::class``. To apply custom Segment filter logic, key it on ``Mautic\LeadBundle\Event\LeadListFilteringEvent::class``. The ``UserEvents::USER_AUTHENTICATION_CONTENT`` and ``LeadEvents::LIST_FILTERS_ON_FILTERING`` constants remain defined, but a subscriber still keyed on either one silently receives nothing.

.. vale off

Removed event constants
=======================

.. vale on

Mautic 8 removed the string constants for the following events, which Mautic dispatches by the event object alone. A subscriber that still references one of these constants fails with ``Error: Undefined constant`` when PHP loads it. Key ``getSubscribedEvents()`` on the event class instead.

.. vale off

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Removed constant
     - Subscription key
   * - ``ConfigEvents::CONFIG_PRE_SAVE``
     - ``Mautic\ConfigBundle\Event\ConfigPreSaveEvent``
   * - ``ConfigEvents::CONFIG_POST_SAVE``
     - ``Mautic\ConfigBundle\Event\ConfigPostSaveEvent``
   * - ``CampaignEvents::ON_CAMPAIGN_DELETE``
     - ``Mautic\CampaignBundle\Event\DeleteCampaign``
   * - ``CampaignEvents::CAMPAIGN_ON_BUILD``
     - ``Mautic\CampaignBundle\Event\CampaignBuilderEvent``
   * - ``CampaignEvents::CAMPAIGN_ON_TRIGGER``
     - ``Mautic\CampaignBundle\Event\CampaignTriggerEvent``
   * - ``CampaignEvents::ON_EVENT_EXECUTED``
     - ``Mautic\CampaignBundle\Event\ExecutedEvent``
   * - ``CampaignEvents::ON_EVENT_DELETE``
     - ``Mautic\CampaignBundle\Event\DeleteEvent``
   * - ``CampaignEvents::ON_EVENT_EXECUTED_BATCH``
     - ``Mautic\CampaignBundle\Event\ExecutedBatchEvent``
   * - ``CampaignEvents::ON_EVENT_SCHEDULED``
     - ``Mautic\CampaignBundle\Event\ScheduledEvent``
   * - ``CampaignEvents::ON_EVENT_SCHEDULED_BATCH``
     - ``Mautic\CampaignBundle\Event\ScheduledBatchEvent``
   * - ``CampaignEvents::ON_EVENT_FAILED``
     - ``Mautic\CampaignBundle\Event\FailedEvent``
   * - ``CampaignEvents::ON_EVENT_DECISION_EVALUATION_RESULTS``
     - ``Mautic\CampaignBundle\Event\DecisionResultsEvent``
   * - ``CampaignEvents::ON_CAMPAIGN_FAILURE_NOTIFY``
     - ``Mautic\CampaignBundle\Event\NotifyOfFailureEvent``
   * - ``CampaignEvents::ON_CAMPAIGN_UNPUBLISH_NOTIFY``
     - ``Mautic\CampaignBundle\Event\NotifyOfUnpublishEvent``
   * - ``PluginEvents::PLUGIN_ON_INTEGRATION_CONFIG_SAVE``
     - ``Mautic\PluginBundle\Event\PluginIntegrationEvent``
   * - ``PluginEvents::PLUGIN_ON_INTEGRATION_REQUEST``
     - ``Mautic\PluginBundle\Event\PluginIntegrationRequestEvent``
   * - ``PluginEvents::PLUGIN_ON_INTEGRATION_RESPONSE``
     - ``Mautic\PluginBundle\Event\PluginIntegrationResponseEvent``
   * - ``PluginEvents::PLUGIN_ON_INTEGRATION_AUTH_REDIRECT``
     - ``Mautic\PluginBundle\Event\PluginIntegrationAuthRedirectEvent``
   * - ``PluginEvents::PLUGIN_ON_INTEGRATION_GET_AUTH_CALLBACK_URL``
     - ``Mautic\PluginBundle\Event\PluginIntegrationAuthCallbackUrlEvent``
   * - ``PluginEvents::PLUGIN_ON_INTEGRATION_FORM_DISPLAY``
     - ``Mautic\PluginBundle\Event\PluginIntegrationFormDisplayEvent``
   * - ``PluginEvents::PLUGIN_ON_INTEGRATION_FORM_BUILD``
     - ``Mautic\PluginBundle\Event\PluginIntegrationFormBuildEvent``
   * - ``PluginEvents::ON_PLUGIN_UPDATE``
     - ``Mautic\PluginBundle\Event\PluginUpdateEvent``
   * - ``PluginEvents::ON_PLUGIN_INSTALL``
     - ``Mautic\PluginBundle\Event\PluginInstallEvent``
   * - ``PluginEvents::PLUGIN_IS_PUBLISHED_STATE_CHANGING``
     - ``Mautic\PluginBundle\Event\PluginIsPublishedEvent``
   * - ``DynamicContentEvents::ON_CONTACTS_FILTER_EVALUATE``
     - ``Mautic\DynamicContentBundle\Event\ContactFiltersEvaluateEvent``
   * - ``DynamicContentEvents::TOKEN_REPLACEMENT``
     - ``Mautic\CoreBundle\Event\TokenReplacementEvent``
   * - ``DoNotContactAddEvent::ADD_DONOT_CONTACT``
     - ``Mautic\LeadBundle\Event\DoNotContactAddEvent``
   * - ``DoNotContactRemoveEvent::REMOVE_DONOT_CONTACT``
     - ``Mautic\LeadBundle\Event\DoNotContactRemoveEvent``

.. vale on

The ``Mautic\ConfigBundle\ConfigEvents`` class no longer exists, so also remove any ``use Mautic\ConfigBundle\ConfigEvents;`` statement. Mautic 8 also removed these constants, which have no replacement event:

* ``DynamicContentEvents::CATEGORY_PRE_SAVE``, ``CATEGORY_POST_SAVE``, ``CATEGORY_PRE_DELETE``, and ``CATEGORY_POST_DELETE`` duplicated the ``Mautic\CategoryBundle\CategoryEvents`` constants with the same string values. Use the ``CategoryEvents`` constants instead.
* ``PluginEvents::ON_FORM_SUBMIT_ACTION_TRIGGERED`` had no dispatcher or listener.

These illustrative fragments show the change for the Plugin Integration request event. Before Mautic 8, the subscriber keys on the constant:

.. code-block:: php

    <?php

    use Mautic\PluginBundle\PluginEvents;

    public static function getSubscribedEvents(): array
    {
        return [
            PluginEvents::PLUGIN_ON_INTEGRATION_REQUEST => ['onRequest', 0],
        ];
    }

In Mautic 8, the subscriber keys on the event class:

.. code-block:: php

    <?php

    use Mautic\PluginBundle\Event\PluginIntegrationRequestEvent;

    public static function getSubscribedEvents(): array
    {
        return [
            PluginIntegrationRequestEvent::class => ['onRequest', 0],
        ];
    }

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

.. _leadbundle events dispatched by event class:

.. vale off

LeadBundle events dispatched by event class
*******************************************

.. vale on

Since Mautic 8, Mautic dispatches the LeadBundle events for Contacts, Companies, Segments, Custom Fields, Tags, notes, devices, imports, and Contact exports by their event class instead of a ``LeadEvents`` string constant. Key ``getSubscribedEvents()`` on ``EventClass::class``. All the event classes below live in the ``Mautic\LeadBundle\Event`` namespace.

Where several ``LeadEvents`` constants used to share one event class, each event now has its own subclass of that shared class. For example, ``LeadPreSaveEvent`` and ``LeadPostSaveEvent`` both extend ``LeadEvent``. Listener methods that type-hint the former shared class keep working.

Mautic 8 keeps these ``LeadEvents`` constants because their string values remain the Webhook event type identifiers. Mautic no longer dispatches events under these names, so a subscriber still keyed on one of these constants silently stops receiving the event - no error, no log entry. Re-key it on the event class:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Kept ``LeadEvents`` constant
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
   * - ``COMPANY_POST_SAVE``
     - ``CompanyPostSaveEvent``
   * - ``COMPANY_POST_DELETE``
     - ``CompanyPostDeleteEvent``

Mautic 8 removes these ``LeadEvents`` constants. Code that still references one of them throws a PHP fatal error - ``Error: Undefined constant``. Subscribe to the event class instead:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Removed ``LeadEvents`` constant
     - Event class to subscribe to
   * - ``LEAD_PRE_SAVE``
     - ``LeadPreSaveEvent``
   * - ``LEAD_PRE_DELETE``
     - ``LeadPreDeleteEvent``
   * - ``LEAD_PRE_MERGE``
     - ``LeadPreMergeEvent``
   * - ``LEAD_POST_MERGE``
     - ``LeadPostMergeEvent``
   * - ``LEAD_IDENTIFIED``
     - ``LeadIdentifiedEvent``
   * - ``LEAD_LIST_BATCH_CHANGE``
     - ``ListBatchChangeEvent``
   * - ``LEAD_PRE_BATCH_SAVE``
     - ``LeadPreBatchSaveEvent``
   * - ``LEAD_POST_BATCH_SAVE``
     - ``LeadPostBatchSaveEvent``
   * - ``CURRENT_LEAD_CHANGED``
     - ``LeadChangeEvent``
   * - ``LIST_PRE_SAVE``
     - ``ListPreSaveEvent``
   * - ``LIST_POST_SAVE``
     - ``ListPostSaveEvent``
   * - ``LIST_PRE_UNPUBLISH``
     - ``ListPreUnpublishEvent``
   * - ``LIST_PRE_DELETE``
     - ``ListPreDeleteEvent``
   * - ``ON_LIST_DELETE``
     - ``ListDeleteEvent``
   * - ``LIST_POST_DELETE``
     - ``ListPostDeleteEvent``
   * - ``FIELD_PRE_SAVE``
     - ``FieldPreSaveEvent``
   * - ``FIELD_POST_SAVE``
     - ``FieldPostSaveEvent``
   * - ``FIELD_PRE_DELETE``
     - ``FieldPreDeleteEvent``
   * - ``FIELD_POST_DELETE``
     - ``FieldPostDeleteEvent``
   * - ``NOTE_PRE_SAVE``
     - ``NotePreSaveEvent``
   * - ``NOTE_POST_SAVE``
     - ``NotePostSaveEvent``
   * - ``NOTE_PRE_DELETE``
     - ``NotePreDeleteEvent``
   * - ``NOTE_POST_DELETE``
     - ``NotePostDeleteEvent``
   * - ``IMPORT_PRE_SAVE``
     - ``ImportPreSaveEvent``
   * - ``IMPORT_POST_SAVE``
     - ``ImportPostSaveEvent``
   * - ``IMPORT_PRE_DELETE``
     - ``ImportPreDeleteEvent``
   * - ``IMPORT_POST_DELETE``
     - ``ImportPostDeleteEvent``
   * - ``IMPORT_BATCH_PROCESSED``
     - ``ImportBatchProcessedEvent``
   * - ``DEVICE_PRE_SAVE``
     - ``DevicePreSaveEvent``
   * - ``DEVICE_POST_SAVE``
     - ``DevicePostSaveEvent``
   * - ``DEVICE_PRE_DELETE``
     - ``DevicePreDeleteEvent``
   * - ``DEVICE_POST_DELETE``
     - ``DevicePostDeleteEvent``
   * - ``TAG_PRE_SAVE``
     - ``TagPreSaveEvent``
   * - ``TAG_POST_SAVE``
     - ``TagPostSaveEvent``
   * - ``TAG_PRE_DELETE``
     - ``TagPreDeleteEvent``
   * - ``TAG_POST_DELETE``
     - ``TagPostDeleteEvent``
   * - ``TAG_PRE_MERGE``
     - ``TagPreMergeEvent``
   * - ``TAG_POST_MERGE``
     - ``TagPostMergeEvent``
   * - ``COMPANY_PRE_SAVE``
     - ``CompanyPreSaveEvent``
   * - ``COMPANY_PRE_DELETE``
     - ``CompanyPreDeleteEvent``
   * - ``COMPANY_SOFT_DELETE``
     - ``CompanySoftDeleteEvent``
   * - ``COMPANY_PRE_MERGE``
     - ``CompanyPreMergeEvent``
   * - ``COMPANY_POST_MERGE``
     - ``CompanyPostMergeEvent``
   * - ``LIST_FILTERS_CHOICES_ON_GENERATE``
     - ``LeadListFiltersChoicesEvent``
   * - ``SEGMENT_DICTIONARY_ON_GENERATE``
     - ``SegmentDictionaryGenerationEvent``
   * - ``LIST_FILTERS_ON_FILTERING``
     - ``LeadListFilteringEvent``
   * - ``LIST_PRE_PROCESS_LIST``
     - ``ListPreProcessListEvent``
   * - ``ON_CLICKTHROUGH_IDENTIFICATION``
     - ``ContactIdentificationEvent``
   * - ``POST_CONTACT_EXPORT``
     - ``ContactExportEvent``
   * - ``POST_CONTACT_EXPORT_SCHEDULED``
     - ``ContactExportScheduledEvent``
   * - ``CONTACT_EXPORT_PREPARE_FILE``
     - ``ContactExportPrepareFileEvent``
   * - ``CONTACT_EXPORT_SEND_EMAIL``
     - ``ContactExportSendEmailEvent``
   * - ``POST_CONTACT_EXPORT_SEND_EMAIL``
     - ``ContactExportEmailSentEvent``

Mautic 8 also changes how these events behave for code that creates or reads them:

* Mautic 8 makes these 12 former shared classes ``abstract``:

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

  If your Plugin creates one of these events with ``new``, create the matching subclass from the preceding tables instead. ``LeadEvent`` and ``ListChangeEvent`` are no longer ``final``, and Mautic still dispatches them directly.

* The event Mautic dispatches before a save, delete, or merge and the event it dispatches afterward are now separate objects. A value that a listener sets on the earlier event isn't available to listeners of the later one.
* ``Mautic\LeadBundle\Field\Dispatcher\FieldSaveDispatcher::dispatchEvent()`` now takes the ``LeadFieldEvent`` subclass to dispatch, instead of an event name, the field entity, and an ``isNew`` flag.

For the full list of Mautic 8 changes, see :xref:`UPGRADE_GUIDE_8`.

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
