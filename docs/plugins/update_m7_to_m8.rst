Update Plugins for Mautic 8
###########################

Mautic 8 adds native PHP parameter, return, and property type declarations to the base and abstract classes that Plugins and Integrations commonly extend. There's no runtime behavior change - the types that these classes already relied on are only made explicit. Your only upgrade risk is a signature mismatch in your subclasses. If an override or a re-declared property no longer matches the parent's now-explicit signature, PHP throws a fatal ``TypeError`` or compile error.

.. note::

   When you override a method or declare one of these properties again, copy the parent signature exactly - same parameter types, same return type, same property type.

Watch for four kinds of break:

* **New parameter type**: an override without the identical type is a fatal error.
* **New return type**: an override must declare the same return type, and an override that returns ``null`` or nothing now throws a ``TypeError``.
* **New property type**: a subclass that declares the property again without a type is a fatal error.
* **Removed property**: a subclass that read it must stop.

Mautic 8 also adds native PHP return type declarations to the public methods on its repository classes, and a :xref:`phpstan` rule now enforces this across Mautic's repositories. If your Plugin or Integration subclasses a Mautic repository and overrides one of these methods without declaring the same return type, PHP raises a fatal error when it loads your class.

.. vale off

CommonRepository
****************

.. vale on

Many of Mautic's repositories extend ``Mautic\CoreBundle\Entity\CommonRepository``, so its newly typed public methods have the widest impact. These signatures gain native return types:

.. code:: diff

   - public function checkUniqueAlias($alias, $entity = null)
   + public function checkUniqueAlias($alias, $entity = null): int
   - public function findOneBySlugs($alias, $catAlias = null, $lang = null)
   + public function findOneBySlugs($alias, $catAlias = null, $lang = null): ?object
   - public function getBaseColumns($entityClass, bool $returnColumnNames = false)
   + public function getBaseColumns($entityClass, bool $returnColumnNames = false): array
   - public function getEntities(array $args = [])
   + public function getEntities(array $args = []): iterable
   - public function getValue($id, $column)
   + public function getValue($id, $column): mixed
   - public function getTableName()
   + public function getTableName(): string

These signatures gain native parameter types:

.. code:: diff

   - public function saveEntity($entity, $flush = true): void
   + public function saveEntity(object $entity, bool $flush = true): void

   - public function deleteEntity($entity, $flush = true): void
   + public function deleteEntity(object $entity, bool $flush = true): void

   - protected function validateOrderByClause($clause)
   + protected function validateOrderByClause(array $clause): array

.. vale off

For a repository extension example, see :doc:`/plugin_extensions/contacts`.

.. vale on

A compliant override repeats the parent's return type:

.. code:: php

   public function getEntities(array $args = []): iterable
   {
       return parent::getEntities($args);
   }

Other repositories
******************

Concrete repositories across Mautic core also gain native return types on their public methods, so a Plugin that overrides a public method on any core repository must declare the matching return type.

Find affected overrides
***********************

Run :xref:`phpstan` against your Plugin on Mautic 8 before you ship. It flags every override whose return type no longer matches its parent, so you can fix them before a fatal error reaches production.

.. _mautic 8 abstractpermissions:

.. vale off

AbstractPermissions
*******************

.. vale on

Every bundle and Plugin defines its own ``*Permissions`` class that extends ``Mautic\CoreBundle\Security\Permissions\AbstractPermissions``. If yours overrides any of these methods, copy the new signature exactly.

.. code:: diff

   - public function isGranted($userPermissions, $name, $level): bool
   + public function isGranted(array $userPermissions, $name, $level): bool

   - protected function addStandardFormFields($bundle, $level, &$builder, $data, $includePublish = true)
   + protected function addStandardFormFields($bundle, $level, &$builder, array $data, bool $includePublish = true)

   - protected function addManageFormFields($bundle, $level, &$builder, $data)
   + protected function addManageFormFields($bundle, $level, &$builder, array $data)

   - protected function addExtendedFormFields($bundle, $level, &$builder, $data, $includePublish = true)
   + protected function addExtendedFormFields($bundle, $level, &$builder, array $data, bool $includePublish = true)

Mautic 8 removes ``definePermissions()``, so Mautic no longer calls it. Define your permissions in the constructor instead:

.. code:: diff

   - public function definePermissions(): void
   + public function __construct()
     {
         $this->addStandardPermissions('categories');
     }

Mautic 8 deprecates the ``array $params`` constructor argument, which now defaults to an empty array, and plans to remove it in Mautic 9. Mautic injects the configuration parameters after construction through the ``#[Required]`` method ``autowireAbstractPermissions(CoreParametersHelper $coreParametersHelper)``, so ``$this->params`` is empty inside the constructor. Drop the argument and the ``parent::__construct($params)`` call, and read ``$this->params`` only in the other methods:

.. code:: diff

   - public function __construct(array $params)
   + public function __construct()
     {
   -     parent::__construct($params);
   -
         $this->addStandardPermissions('categories');
     }

A permissions class that already defines its permissions in the constructor, without a ``$params`` argument, needs no change.

Mautic's autoconfiguration tags every ``AbstractPermissions`` subclass with ``mautic.permissions``, so register your permissions class in ``Config/services.php`` rather than under ``services > permissions`` in ``Config/config.php``, which Mautic 8 no longer reads.

.. vale off

For a permissions extension example, see :doc:`/plugins/permissions`.

.. vale on

.. _mautic 8 abstractintegration:

.. vale off

AbstractIntegration
*******************

.. vale on

Every third-party Integration extends ``Mautic\PluginBundle\Integration\AbstractIntegration``, so review any of these methods you override.

.. code:: diff

   - public function makeRequest($url, $parameters = [], $method = 'GET', $settings = [])
   + public function makeRequest($url, $parameters = [], $method = 'GET', array $settings = [])

   - public function prepareRequest($url, $parameters, $method, $settings, $authType)
   + public function prepareRequest(string $url, $parameters, string $method, array $settings, $authType)

   - public function authCallback($settings = [], $parameters = [])
   + public function authCallback(array $settings = [], array $parameters = []): false|string|array

   - public function mergeConfigToFeatureSettings($config = [])
   + public function mergeConfigToFeatureSettings(array $config = [])

   - public function getFormCompanyFields($settings = [])
   + public function getFormCompanyFields(array $settings = [])

``getCache()`` returns a ``Psr\SimpleCache\CacheInterface`` instead of the removed ``CacheStorageHelper``, and the second constructor argument is a ``Mautic\CacheBundle\Cache\CacheProviderInterface``. Mautic still keeps each Integration's cache keys separate, so calls such as ``$this->getCache()->get('leadFields')`` keep working. A cache miss returns ``null`` instead of ``false``, so change any ``false === $value`` comparison to ``null === $value``. If your Integration overrides ``getCache()`` or the constructor, match the new types:

.. code:: diff

   - public function getCache()
   + public function getCache(): \Psr\SimpleCache\CacheInterface

.. vale off

CrmAbstractIntegration
**********************

.. vale on

The ``MauticPlugin\MauticCrmBundle\Integration\CrmAbstractIntegration`` class now types the ``$config``, ``$fields``, and ``$fieldsToUpdate`` parameters as ``array`` across several methods. Here's a representative change on ``getFormFieldsByObject()``:

.. code:: diff

   - public function getFormFieldsByObject($object, $settings = [])
   + public function getFormFieldsByObject($object, array $settings = [])

The same ``array`` typing applies to ``cleanPriorityFields()``, ``getPriorityFieldsForMautic()``, ``getPriorityFieldsForIntegration()``, and ``getBlankFieldsToUpdate()``. When you override any of them, copy the parent signature exactly.

.. vale off

CommonController and AbstractFormController
*******************************************

.. vale on

Plugins extend ``Mautic\CoreBundle\Controller\CommonController`` and ``Mautic\CoreBundle\Controller\AbstractFormController`` to build create, read, update, and delete interfaces. This section lists only the methods Plugins commonly override.

.. code:: diff

   - protected function getModel($modelNameKey): MauticModelInterface
   + protected function getModel(string $modelNameKey): AbstractCommonModel

   - public function executeAction(Request $request, $objectAction, $objectId = 0, $objectSubId = 0, $objectModel = '')
   + public function executeAction(Request $request, $objectAction, $objectId = 0, $objectSubId = 0, $objectModel = ''): Response

   - public function ajaxAction(Request $request, $args = []): Response
   + public function ajaxAction(Request $request, array $args = []): Response

The ``AbstractFormController`` class adds parameter and return types to its lock-handling methods.

.. code:: diff

   - public function unlockAction(Request $request, $objectId, $objectModel)
   + public function unlockAction(Request $request, $objectId, string $objectModel): RedirectResponse

   - protected function isLocked($postActionVars, $entity, $model, $batch = false)
   + protected function isLocked($postActionVars, $entity, string $modelName, bool $batch = false)

The ``AbstractStandardFormController`` class follows the same pattern - for example ``getDefaultOrderDirection(): string`` and ``getDataForExport(): ?array`` gain return types.

.. vale off

For a controller extension example, see :doc:`/plugins/mvc`.

.. vale on

.. vale off

CommonApiController
*******************

.. vale on

The ``Mautic\ApiBundle\Controller\CommonApiController`` class gains explicit parameter and return types in two areas.

.. code:: diff

   - protected function prepareParametersForBinding(Request $request, $parameters, $entity, $action)
   + protected function prepareParametersForBinding(Request $request, array $parameters, object $entity, string $action): array|Response

.. note::

   The old ``@return`` annotation was ``mixed``. An override that falls through without a ``return`` now throws a ``TypeError``, so the override must ``return $parameters;``.

The batch actions now declare a ``Response`` return type:

.. code:: diff

   - public function newEntitiesAction(Request $request)
   + public function newEntitiesAction(Request $request): Response

The same return type now applies to ``editEntitiesAction()`` and ``deleteEntitiesAction()``. An override may no longer return an array.

For an API controller extension example, see :doc:`/plugin_extensions/api`.

.. vale off

FetchCommonApiController
************************

.. vale on

The ``Mautic\ApiBundle\Controller\FetchCommonApiController`` class adds property types, and removes one property.

A subclass that declares any of these properties again must use the same type:

.. code:: diff

   - protected $entityClass;
   + protected string $entityClass = '';

   - protected $entityNameOne;
   + protected string $entityNameOne;

   - protected $entityNameMulti;
   + protected string $entityNameMulti;

   - protected $permissionBase;
   + protected ?string $permissionBase = null;

   - protected $serializerGroups = [];
   + protected array $serializerGroups = [];

Mautic 8 removes the ``protected $parametersContainer;`` property. Mautic never assigned it, so any read already failed. A subclass that referenced it must stop doing so.

Event and entity classes
************************

When you upgrade a Plugin to Mautic 8, review the event and entity classes your Plugin subscribes to, calls, or extends. Mautic 8 adds native PHP parameter, return, and property type declarations to the event and entity classes listed below. These types match what the methods already accepted, so there's no runtime behavior change - most were already recorded in the classes' ``@param`` and ``@return`` annotations, and Mautic 8 now enforces them in the signatures.

Plugins interact with these events by subscribing to them and calling their methods, and some Plugins extend them. This creates two kinds of break:

* A narrowed parameter or property type raises a ``TypeError`` at runtime when you pass an argument that no longer matches the method's declared type. For example, ``SubmissionEvent::setPostSubmitCallbackResponse()`` now requires a ``RedirectResponse``, so passing any other response type throws a ``TypeError``.
* An overridden method whose signature no longer matches the parent causes a fatal error when PHP loads your class.

If your Plugin doesn't subscribe to, call, or extend any of the classes listed below, you have nothing to change.

Mautic 8 also removes the deprecated ``FormController`` base controller. See :ref:`Removed FormController <Mautic 8 removed FormController>` if your Plugin has a controller that extends it.

Mautic 8 also makes many core classes ``final``, so a Plugin can no longer extend them. See :ref:`Final classes <Mautic 8 final classes>` if your Plugin extends a Mautic class or mocks one in its tests.

Mautic 8 also changes the helper methods on the base controllers. See :ref:`Controller helper methods <Mautic 8 controller helper methods>` if your Plugin has a controller that extends a Mautic controller.

Mautic 8 also adds a native type to every class and interface constant. See :ref:`Typed class constants <Mautic 8 typed class constants>` if your Plugin overrides a constant from a Mautic class or interface.

Mautic 8 also dispatches most of these events by the event object alone instead of a bundle's ``*Events`` string constant. See :ref:`Events dispatched by class name <Mautic 8 events dispatched by class name>` if your Plugin subscribes to one of them.

.. vale off

.. seealso::

   For how a Plugin subscribes to Events, see :doc:`/plugins/event_listeners`. For the earlier upgrade, see :doc:`/plugins/update_m4_to_m5`.

.. vale on

.. note::

   When you call one of these methods, pass arguments of the declared types. When you extend one of these events and override a typed method, copy the parent signature exactly, using the same parameter types, return type, and property type.

Mautic 8 changes event or entity class signatures in these bundles:

* CampaignBundle
* ChannelBundle
* ConfigBundle
* CoreBundle
* DashboardBundle
* EmailBundle
* FormBundle
* IntegrationsBundle
* LeadBundle
* NotificationBundle
* PageBundle
* PointBundle
* SmsBundle
* StageBundle
* UserBundle
* WebhookBundle

.. _mautic 8 events dispatched by class name:

.. vale off

Events dispatched by class name
*******************************

.. vale on

Beyond the preceding signature changes, Mautic 8 also changes *how* it dispatches most bundle events. Following the Symfony 4.3+ convention, Mautic dispatches these events by the event object alone, so the event name is the event class. Key ``getSubscribedEvents()`` on ``EventClass::class`` instead of the bundle's ``*Events`` string constant or the raw event name, such as ``mautic.campaign_on_build``. If your Plugin dispatches one of these events itself, drop the event name argument:

.. code:: diff

   - CampaignEvents::CAMPAIGN_ON_BUILD => ['onCampaignBuild', 0],
   + CampaignBuilderEvent::class      => ['onCampaignBuild', 0],

   - $dispatcher->dispatch($event, CampaignEvents::CAMPAIGN_ON_BUILD);
   + $dispatcher->dispatch($event);

What happens to a subscriber that you don't update depends on what Mautic 8 did with the old constant:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Old constant
     - Result for a subscriber still keyed on it
   * - Mautic kept the constant
     - The subscriber silently receives nothing - no error, no log entry. Mautic keeps some of these constants because their string values are also Webhook event type identifiers.
   * - Mautic removed the constant
     - PHP fails with ``Error: Undefined constant`` when it loads the subscriber.
   * - Mautic deleted the whole ``*Events`` class
     - PHP fails with a ``Class "..." not found`` error, for example ``Class "Mautic\CoreBundle\CoreEvents" not found``.

Mautic 8 deletes these ``*Events`` classes entirely, so remove the matching ``use`` statements from your Plugin:

* ``Mautic\ApiBundle\ApiEvents``
* ``Mautic\ConfigBundle\ConfigEvents``
* ``Mautic\CoreBundle\CoreEvents``
* ``Mautic\DashboardBundle\DashboardEvents``
* ``Mautic\IntegrationsBundle\IntegrationEvents``
* ``Mautic\StatsBundle\StatEvents``
* ``Mautic\UserBundle\UserEvents``

``UPGRADE-8.0.md`` still says Mautic keeps the ``CoreEvents``, ``IntegrationEvents``, and ``DashboardEvents`` constants for backwards compatibility, but Mautic 8 deletes those classes, so replace every reference to them with the matching event class.

Each bundle section in this guide maps the bundle's old constants to the event classes to key on:

.. vale off

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Bundle
     - Constants class
     - What Mautic 8 does with the constants
   * - :ref:`ApiBundle <mautic 8 apibundle>`
     - ``ApiEvents``
     - Deletes the class
   * - :ref:`AssetBundle <mautic 8 assetbundle>`
     - ``AssetEvents``
     - Removes the Asset load, browse, save, and delete constants
   * - :ref:`CampaignBundle <mautic 8 campaignbundle>`
     - ``CampaignEvents``
     - Removes most constants
   * - CategoryBundle
     - ``CategoryEvents``
     - Keeps ``CATEGORY_ON_BUNDLE_LIST_BUILD`` but dispatches ``CategoryTypesEvent`` by class
   * - :ref:`ChannelBundle <mautic 8 channelbundle>`
     - ``ChannelEvents``
     - Keeps the constants
   * - :ref:`ConfigBundle <mautic 8 configbundle>`
     - ``ConfigEvents``
     - Deletes the class
   * - :ref:`CoreBundle <mautic 8 corebundle>`
     - ``CoreEvents``
     - Deletes the class
   * - :ref:`DashboardBundle <mautic 8 dashboardbundle>`
     - ``DashboardEvents``
     - Deletes the class
   * - :ref:`DynamicContentBundle <mautic 8 dynamiccontentbundle>`
     - ``DynamicContentEvents``
     - Removes the filter, token, and Category constants
   * - :ref:`EmailBundle <mautic 8 emailbundle>`
     - ``EmailEvents``
     - Removes most constants and keeps ``EMAIL_ON_SEND`` and ``EMAIL_ON_OPEN``
   * - :ref:`FormBundle <mautic 8 formbundle>`
     - ``FormEvents``
     - Keeps the constants
   * - :ref:`IntegrationsBundle <mautic 8 integrationsbundle>`
     - ``IntegrationEvents``
     - Deletes the class
   * - :ref:`LeadBundle <mautic 8 leadbundle>`
     - ``LeadEvents``
     - Removes some constants and keeps others
   * - :ref:`MauticFocusBundle <mautic 8 focusbundle>`
     - ``FocusEvents``
     - Keeps ``FOCUS_ON_VIEW``
   * - :ref:`MauticSocialBundle <mautic 8 socialbundle>`
     - ``SocialEvents``
     - Removes the Monitor and Tweet constants
   * - :ref:`NotificationBundle <mautic 8 notificationbundle>`
     - ``NotificationEvents``
     - Keeps ``NOTIFICATION_ON_SEND``
   * - :ref:`PageBundle <mautic 8 pagebundle>`
     - ``PageEvents``
     - Removes ``PAGE_ON_BUILD`` and ``PAGE_ON_DISPLAY`` and keeps the others
   * - :ref:`PluginBundle <mautic 8 pluginbundle>`
     - ``PluginEvents``
     - Removes most constants
   * - :ref:`PointBundle <mautic 8 pointbundle>`
     - ``PointEvents``, ``PointGroupEvents``
     - Keeps the constants
   * - :ref:`ReportBundle <mautic 8 reportbundle>`
     - ``ReportEvents``
     - Keeps the constants
   * - :ref:`SmsBundle <mautic 8 smsbundle>`
     - ``SmsEvents``
     - Removes most constants and keeps ``SMS_ON_SEND``
   * - :ref:`StageBundle <mautic 8 stagebundle>`
     - ``StageEvents``
     - Keeps ``STAGE_ON_BUILD``
   * - :ref:`StatsBundle <mautic 8 statsbundle>`
     - ``StatEvents``
     - Deletes the class
   * - :ref:`UserBundle <mautic 8 userbundle>`
     - ``UserEvents``
     - Deletes the class
   * - :ref:`WebhookBundle <mautic 8 webhookbundle>`
     - ``WebhookEvents``
     - Removes the lifecycle constants and keeps the others

.. vale on

Some constants that several events share keep their string names, such as the ``FormEvents::FORM_*`` and ``PageEvents::PAGE_*`` save and delete groups. Mautic still dispatches those events under the constant, so subscribers keyed on them don't change. Each bundle section names the constants that don't change.

.. _mautic 8 check event subscriptions:

.. vale off

Check event subscriptions
=========================

.. vale on

To confirm the name Mautic dispatches an event under, and that your re-keyed subscriber binds to it, run ``bin/console debug:event-dispatcher`` with the event class:

.. code-block:: console

   bin/console debug:event-dispatcher "Mautic\SmsBundle\Event\DncEvent"

Your subscriber's class and method appear in the listing for the event class. If they're absent, Mautic hasn't registered the subscriber for that event. Run the command before and after you re-key a subscriber to compare the two listings. Without an argument, the command lists every event with its listeners, and a partial name filters the output.

.. _mautic 8 removed event constants:

.. vale off

Removed event constants
=======================

.. vale on

When Mautic 8 removes a constant, PHP fails with ``Error: Undefined constant`` as soon as it loads a subscriber that still references it. The bundle sections in this guide list each removed constant with the event class to key on, so replace every reference and remove the ``use`` statement for any ``*Events`` class that your Plugin no longer needs. For example, :ref:`DynamicContentBundle <mautic 8 dynamiccontentbundle>` covers the removed ``DynamicContentEvents::TOKEN_REPLACEMENT`` constant, and :ref:`PluginBundle <mautic 8 pluginbundle>` shows a complete re-keyed subscriber.

Mautic 8 also removes a few constants that Mautic never dispatched an event under, such as ``AssetEvents::ASSET_ON_UPLOAD`` and ``PluginEvents::ON_FORM_SUBMIT_ACTION_TRIGGERED``. These constants have no replacement event, so remove any subscription to them. Each bundle section names them.

.. _mautic 8 apibundle:

.. vale off

ApiBundle
*********

.. vale on

Mautic 8 deletes the ``Mautic\ApiBundle\ApiEvents`` class and dispatches the ApiBundle events by their event class. A subscriber that still references an ``ApiEvents`` constant fails with a ``Class "Mautic\ApiBundle\ApiEvents" not found`` error. Key ``getSubscribedEvents()`` on the event class in the ``Mautic\ApiBundle\Event`` namespace instead:

.. vale off

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Removed ``ApiEvents`` constant
     - Event class
   * - ``API_ON_ENTITY_PRE_SAVE``
     - ``PreSaveApiEntityEvent``
   * - ``API_ON_ENTITY_POST_SAVE``
     - ``PostSaveApiEntityEvent``
   * - ``CLIENT_POST_SAVE``
     - ``ClientPostSaveEvent``
   * - ``CLIENT_POST_DELETE``
     - ``ClientPostDeleteEvent``
   * - ``API_PRE_SERIALIZATION_CONTEXT``
     - ``PreSerializationContextEvent``
   * - ``API_POST_SERIALIZATION_CONTEXT``
     - ``PostSerializationContextEvent``
   * - ``API_PLATFORM_PERMISSION_CONTEXT``
     - ``ApiPlatformPermissionContextEvent``

.. vale on

Mautic didn't dispatch any event under ``ApiEvents::CLIENT_PRE_SAVE`` or ``ApiEvents::BUILD_ROUTE``, so remove any subscription to them.

Each pair of save, delete, or serialization events used to share one event object. ``ApiEntityEvent``, ``ClientEvent``, and ``ApiSerializationContextEvent`` are now abstract base classes for the classes in the preceding table. A listener method can keep its type hint on the base class, but code that creates one of these events with ``new``, such as a Plugin test, must create the matching subclass.

.. _mautic 8 assetbundle:

.. vale off

AssetBundle
***********

.. vale on

Mautic 8 removes the ``Mautic\AssetBundle\AssetEvents`` constants for the Asset load, remote browse, save, and delete events, and dispatches these events by their event class. A subscriber that still references one of the constants fails with ``Error: Undefined constant``, and a subscriber keyed on a raw event name, such as ``mautic.asset_on_load``, silently receives nothing. Key ``getSubscribedEvents()`` on the event class in the ``Mautic\AssetBundle\Event`` namespace instead:

.. vale off

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Removed ``AssetEvents`` constant
     - Event class
   * - ``ASSET_ON_LOAD``
     - ``AssetLoadEvent``
   * - ``ASSET_ON_REMOTE_BROWSE``
     - ``RemoteAssetBrowseEvent``
   * - ``ASSET_PRE_SAVE``
     - ``AssetPreSaveEvent``
   * - ``ASSET_POST_SAVE``
     - ``AssetPostSaveEvent``
   * - ``ASSET_PRE_DELETE``
     - ``AssetPreDeleteEvent``
   * - ``ASSET_POST_DELETE``
     - ``AssetPostDeleteEvent``

.. vale on

The four save and delete classes extend ``AssetEvent``, so a listener method can keep its ``AssetEvent`` type hint. Mautic also removes the ``ASSET_ON_UPLOAD`` constant, which it never dispatched or listened to. The ``ON_CAMPAIGN_TRIGGER_DECISION`` and ``ON_DETERMINE_DOWNLOAD_RATE_WINNER`` constants don't change.

.. _mautic 8 campaignbundle:

.. vale off

CampaignBundle
**************

.. vale on

Mautic 8 adds type declarations to the Campaign Event entity and three Campaign event classes. It also removes most ``CampaignEvents`` constants and dispatches the Campaign membership, save, and delete events by dedicated event classes.

.. vale off

CampaignEvents constants
========================

.. vale on

Mautic 8 removes these ``Mautic\CampaignBundle\CampaignEvents`` constants and dispatches the events by their event class. A subscriber that still references one of them fails with ``Error: Undefined constant``. Key ``getSubscribedEvents()`` on the event class in the ``Mautic\CampaignBundle\Event`` namespace instead:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Removed ``CampaignEvents`` constant
     - Event class
   * - ``CAMPAIGN_ON_BUILD``
     - ``CampaignBuilderEvent``
   * - ``CAMPAIGN_ON_TRIGGER``
     - ``CampaignTriggerEvent``
   * - ``ON_CAMPAIGN_DELETE``
     - ``DeleteCampaign``
   * - ``ON_AFTER_EVENTS_DELETE``
     - ``AfterEventsDeleteEvent``
   * - ``ON_EVENT_DELETE``
     - ``DeleteEvent``
   * - ``ON_EVENT_EXECUTED``
     - ``ExecutedEvent``
   * - ``ON_EVENT_EXECUTED_BATCH``
     - ``ExecutedBatchEvent``
   * - ``ON_EVENT_SCHEDULED``
     - ``ScheduledEvent``
   * - ``ON_EVENT_SCHEDULED_BATCH``
     - ``ScheduledBatchEvent``
   * - ``ON_EVENT_FAILED``
     - ``FailedEvent``
   * - ``ON_EVENT_DECISION_EVALUATION_RESULTS``
     - ``DecisionResultsEvent``
   * - ``ON_CAMPAIGN_FAILURE_NOTIFY``
     - ``NotifyOfFailureEvent``
   * - ``ON_CAMPAIGN_UNPUBLISH_NOTIFY``
     - ``NotifyOfUnpublishEvent``

The removed membership change, save, and delete constants are in :ref:`CampaignLeadChangeEvent <Plugins/update_m7_to_m8:CampaignLeadChangeEvent>` and :ref:`CampaignEvent <Plugins/update_m7_to_m8:CampaignEvent>`. Mautic still dispatches the ``ON_EVENT_CONDITION_EVALUATION`` and ``ON_EVENT_DECISION_EVALUATION`` events under their string constants, so subscribers keyed on them don't change.

.. vale off

Campaign Event entity
=====================

.. vale on

Campaign subscribers and Plugins that build or inspect Campaign events work with ``Mautic\CampaignBundle\Entity\Event``. Three setters on this entity narrow to reject a type Mautic 7 accepted, so a call that still passes the old type raises a ``TypeError`` at runtime.

``setTriggerHour()`` no longer accepts a ``\DateTime``:

.. code:: diff

   - public function setTriggerHour($triggerHour): static
   + public function setTriggerHour(array|string|null $triggerHour): static

``setTriggerRestrictedStartHour()`` no longer accepts an ``array``:

.. code:: diff

   - public function setTriggerRestrictedStartHour($triggerRestrictedStartHour): static
   + public function setTriggerRestrictedStartHour(string|\DateTimeInterface|null $triggerRestrictedStartHour): static

``setTriggerRestrictedStopHour()`` no longer accepts an ``array``:

.. code:: diff

   - public function setTriggerRestrictedStopHour($triggerRestrictedStopHour): static
   + public function setTriggerRestrictedStopHour(string|\DateTime|null $triggerRestrictedStopHour): static

The same entity adds routine scalar types to its remaining methods that match the values they already took - for example ``setOrder()`` takes ``int``, ``setType()`` and ``setName()`` take ``string``, ``setDescription()`` and ``getDescription()`` use ``?string``, ``setEventType()`` takes ``string``, and the ``triggerMode``, ``decisionPath``, and ``tempId`` methods use ``?string``.

.. vale off

CampaignBuilderEvent
====================

.. vale on

Plugins register Campaign actions, conditions, and decisions on ``Mautic\CampaignBundle\Event\CampaignBuilderEvent``. Its ``addDecision()`` method types ``$key`` as ``string``:

.. code:: diff

   - public function addDecision($key, array $decision): void
   + public function addDecision(string $key, array $decision): void

``addCondition()`` and ``addAction()`` narrow ``$key`` to ``string`` in the same way.

.. vale off

CampaignLeadChangeEvent
=======================

.. vale on

Mautic 8 removes the ``CampaignEvents::CAMPAIGN_ON_LEADCHANGE`` and ``LEAD_CAMPAIGN_BATCH_CHANGE`` constants, which shared one ``CampaignLeadChangeEvent`` object, and dispatches a dedicated event class for each:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Removed ``CampaignEvents`` constant
     - Event class
   * - ``CAMPAIGN_ON_LEADCHANGE``
     - ``Mautic\CampaignBundle\Event\CampaignSingleLeadChangeEvent``
   * - ``LEAD_CAMPAIGN_BATCH_CHANGE``
     - ``Mautic\CampaignBundle\Event\CampaignBatchLeadChangeEvent``

Both are ``final`` subclasses of the now abstract ``Mautic\CampaignBundle\Event\CampaignLeadChangeEvent``, so a listener method can keep its ``CampaignLeadChangeEvent`` type hint and the override risk doesn't apply. Code that creates a ``CampaignLeadChangeEvent`` with ``new``, such as a Plugin test, must create one of the subclasses instead. The base class constructor types ``$leads``, and ``getLead()`` gains a return type:

.. code:: diff

   - public function __construct(..., $leads, ...)
   + public function __construct(..., array|\Mautic\LeadBundle\Entity\Lead $leads, ...)

.. code:: diff

   - public function getLead()
   + public function getLead(): ?\Mautic\LeadBundle\Entity\Lead

.. vale off

CampaignEvent
=============

.. vale on

Before Mautic 8, one ``Mautic\CampaignBundle\Event\CampaignEvent`` object served the ``CampaignEvents::CAMPAIGN_PRE_SAVE``, ``CAMPAIGN_POST_SAVE``, ``CAMPAIGN_PRE_DELETE``, and ``CAMPAIGN_POST_DELETE`` names. Mautic removed all four constants and now dispatches a dedicated event class for each, by class name:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Removed ``CampaignEvents`` constant
     - Event class
   * - ``CAMPAIGN_PRE_SAVE``
     - ``Mautic\CampaignBundle\Event\CampaignPreSaveEvent``
   * - ``CAMPAIGN_POST_SAVE``
     - ``Mautic\CampaignBundle\Event\CampaignPostSaveEvent``
   * - ``CAMPAIGN_PRE_DELETE``
     - ``Mautic\CampaignBundle\Event\CampaignPreDeleteEvent``
   * - ``CAMPAIGN_POST_DELETE``
     - ``Mautic\CampaignBundle\Event\CampaignPostDeleteEvent``

A subscriber that still references one of the constants throws a PHP ``Error`` with the message 'Undefined constant'. Each new class is ``final`` and extends ``CampaignEvent``, so a listener method can keep its ``CampaignEvent`` type hint. Re-key your subscriber on the event classes:

.. code:: diff

   - CampaignEvents::CAMPAIGN_POST_SAVE   => ['onCampaignPostSave', 0],
   - CampaignEvents::CAMPAIGN_POST_DELETE => ['onCampaignDelete', 0],
   + CampaignPostSaveEvent::class         => ['onCampaignPostSave', 0],
   + CampaignPostDeleteEvent::class       => ['onCampaignDelete', 0],

Mautic still dispatches ``CampaignEvent`` itself after it imports a Campaign, so the class stays concrete. A Plugin test that passes ``new CampaignEvent($campaign)`` to a save or delete listener must create the matching subclass instead. For a subscriber example, see :ref:`Campaign save and delete events <plugin_extensions/campaigns:Campaign save and delete events>`.

.. vale off

PendingEvent
============

.. vale on

Campaign action subscribers use ``Mautic\CampaignBundle\Event\PendingEvent``, a ``final`` class, so the override risk doesn't apply. Its ``fail()`` and ``setChannel()`` methods type their string arguments:

.. code:: diff

   - public function fail(LeadEventLog $log, $reason, ?\DateInterval $rescheduleInterval = null): void
   + public function fail(LeadEventLog $log, string $reason, ?\DateInterval $rescheduleInterval = null): void

.. code:: diff

   - public function setChannel($channel, $channelId = null): void
   + public function setChannel(string $channel, $channelId = null): void

``failAll()``, ``failRemaining()``, ``failRemainingPending()``, and ``failLogs()`` all narrow ``$reason`` to ``string`` in the same way.

.. vale off

For a Campaign extension example, see :doc:`/plugin_extensions/campaigns`.

.. _mautic 8 channelbundle:

ChannelBundle
*************

.. vale on

Mautic 8 adds type declarations to three Channel event classes and dispatches the Channel events by their event class.

.. vale off

ChannelEvents constants
=======================

.. vale on

Mautic 8 dispatches these ChannelBundle events by their event class. The ``Mautic\ChannelBundle\ChannelEvents`` constants still exist, but Mautic doesn't dispatch the events under them, so a subscriber keyed on one silently receives nothing. Key ``getSubscribedEvents()`` on the event class in the ``Mautic\ChannelBundle\Event`` namespace instead:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - ``ChannelEvents`` constant
     - Event class
   * - ``ADD_CHANNEL``
     - ``ChannelEvent``
   * - ``CHANNEL_BROADCAST``
     - ``ChannelBroadcastEvent``
   * - ``MESSAGE_QUEUED``
     - ``MessageQueueEvent``
   * - ``PROCESS_MESSAGE_QUEUE``
     - ``MessageQueueProcessEvent``
   * - ``PROCESS_MESSAGE_QUEUE_BATCH``
     - ``MessageQueueBatchProcessEvent``

The ``MESSAGE_PRE_SAVE``, ``MESSAGE_POST_SAVE``, ``MESSAGE_PRE_DELETE``, and ``MESSAGE_POST_DELETE`` constants share ``MessageEvent``, so they don't change, and neither does ``ON_CAMPAIGN_BATCH_ACTION``.

.. vale off

ChannelBroadcastEvent
=====================

.. vale on

Channel broadcast subscribers record send results on ``Mautic\ChannelBundle\Event\ChannelBroadcastEvent``. ``setResults()`` types only ``$channelLabel`` and ``$failedCount``, and leaves ``$successCount`` without a type:

.. code:: diff

   - public function setResults($channelLabel, $successCount, $failedCount = 0, array $failedRecipientsByList = []): void
   + public function setResults(string $channelLabel, $successCount, int $failedCount = 0, array $failedRecipientsByList = []): void

``checkContext()`` types ``$channel`` as ``string``:

.. code:: diff

   - public function checkContext($channel): bool
   + public function checkContext(string $channel): bool

.. vale off

ChannelEvent
============

.. vale on

Plugins register a Channel on ``Mautic\ChannelBundle\Event\ChannelEvent``, a ``final`` class, so the override risk doesn't apply. ``addChannel()`` types ``$channel`` as ``string``:

.. code:: diff

   - public function addChannel($channel, array $config = []): static
   + public function addChannel(string $channel, array $config = []): static

.. vale off

MessageQueueBatchProcessEvent
=============================

.. vale on

Subscribers that process a queued message batch use ``Mautic\ChannelBundle\Event\MessageQueueBatchProcessEvent``. ``checkContext()`` types ``$channel`` as ``string``:

.. code:: diff

   - public function checkContext($channel): bool
   + public function checkContext(string $channel): bool

.. vale off

For a Channel extension example, see :doc:`/plugin_extensions/channels`.

.. _mautic 8 configbundle:

ConfigBundle
************

.. vale on

Mautic 8 adds type declarations to two configuration event classes and deletes the ``ConfigEvents`` class.

.. vale off

ConfigEvents constants
======================

.. vale on

Mautic 8 deletes the ``Mautic\ConfigBundle\ConfigEvents`` class. A subscriber that still references one of its constants fails with a ``Class "Mautic\ConfigBundle\ConfigEvents" not found`` error, so remove the ``use Mautic\ConfigBundle\ConfigEvents;`` statement and key ``getSubscribedEvents()`` on the event class in the ``Mautic\ConfigBundle\Event`` namespace:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Removed ``ConfigEvents`` constant
     - Event class
   * - ``CONFIG_ON_GENERATE``
     - ``ConfigBuilderEvent``
   * - ``CONFIG_PRE_SAVE``
     - ``ConfigPreSaveEvent``
   * - ``CONFIG_POST_SAVE``
     - ``ConfigPostSaveEvent``

The two save events used to share one ``ConfigEvent`` object. ``ConfigPreSaveEvent`` and ``ConfigPostSaveEvent`` both extend ``ConfigEvent``, so a listener method can keep its ``ConfigEvent`` type hint.

.. vale off

ConfigBuilderEvent
==================

.. vale on

Plugins contribute their configuration through ``Mautic\ConfigBundle\Event\ConfigBuilderEvent``. ``getParametersFromConfig()`` types ``$bundle`` as ``string``:

.. code:: diff

   - public function getParametersFromConfig($bundle)
   + public function getParametersFromConfig(string $bundle): array

.. vale off

ConfigEvent
===========

.. vale on

Subscribers that read and validate saved configuration values use ``Mautic\ConfigBundle\Event\ConfigEvent``. ``getConfig()`` and ``setConfig()`` type ``$key`` as ``?string``:

.. code:: diff

   - public function getConfig($key = null)
   + public function getConfig(?string $key = null): array

.. code:: diff

   - public function setConfig(array $config, $key = null): void
   + public function setConfig(array $config, ?string $key = null): void

``unsetIfEmpty()`` types ``$fields`` as ``string|array``, and ``setError()`` types its arguments:

.. code:: diff

   - public function unsetIfEmpty($fields): void
   + public function unsetIfEmpty(string|array $fields): void

.. code:: diff

   - public function setError($message, $messageVars = [], $key = null, $field = null): static
   + public function setError(string $message, array $messageVars = [], ?string $key = null, ?string $field = null): static

.. _mautic 8 corebundle:

.. vale off

CoreBundle
**********

.. vale on

Mautic 8 deletes the ``CoreEvents`` class and adds native type declarations to several ``Mautic\CoreBundle\Event\`` classes that Plugins subscribe to and dispatch. Some narrow a parameter or return type, so a subscriber or caller that passes a previously tolerated type raises a ``TypeError`` at runtime under ``strict_types``. Others match the types the methods already accepted. Grep your ``use`` statements for the ``Mautic\CoreBundle\Event\`` namespace to find the classes your Plugin references.

.. vale off

CoreEvents constants
====================

.. vale on

Mautic 8 deletes the ``Mautic\CoreBundle\CoreEvents`` class, so a subscriber that still references one of its constants fails with a ``Class "Mautic\CoreBundle\CoreEvents" not found`` error. Remove the ``use Mautic\CoreBundle\CoreEvents;`` statement and key ``getSubscribedEvents()`` on the event class in the ``Mautic\CoreBundle\Event`` namespace:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Removed ``CoreEvents`` constant
     - Event class
   * - ``BUILD_MENU``
     - ``MenuEvent``
   * - ``BUILD_ROUTE``
     - ``RouteEvent``
   * - ``GLOBAL_SEARCH``
     - ``GlobalSearchEvent``
   * - ``LIST_STATS``
     - ``StatsEvent``
   * - ``BUILD_COMMAND_LIST``
     - ``CommandListEvent``
   * - ``FETCH_ICONS``
     - ``IconEvent``
   * - ``BUILD_MAUTIC_JS``
     - ``BuildJsEvent``
   * - ``MAINTENANCE_CLEANUP_DATA``
     - ``MaintenanceEvent``
   * - ``VIEW_INJECT_CUSTOM_BUTTONS``
     - ``CustomButtonEvent``
   * - ``VIEW_INJECT_CUSTOM_CONTENT``
     - ``CustomContentEvent``
   * - ``VIEW_INJECT_CUSTOM_TEMPLATE``
     - ``CustomTemplateEvent``
   * - ``VIEW_INJECT_CUSTOM_ASSETS``
     - ``CustomAssetsEvent``
   * - ``ON_GENERATED_COLUMNS_BUILD``
     - ``GeneratedColumnsEvent``

.. vale off

TokenReplacementEvent
=====================

.. vale on

``Mautic\CoreBundle\Event\TokenReplacementEvent`` declares ``strict_types`` and has subscribers in the ``EmailBundle``, ``LeadBundle``, ``SmsBundle``, ``NotificationBundle``, and ``DynamicContentBundle``, and in the ``MauticFocusBundle`` Plugin. ``setContent()`` narrowed to ``string`` only, from the ``CommonEntity|string|null`` its old ``@param CommonEntity|string|null $content`` annotation allowed, so a call that still passes a non-string now raises a ``TypeError`` at runtime.

.. code:: diff

   -    public function setContent($content): void
   +    public function setContent(string $content): void

If your Plugin dispatches this Event, Mautic 8 also types the constructor and ``getLead()``. The constructor accepts ``Lead|array|string|null`` for ``$content``, while ``setContent()`` accepts only ``string``.

.. code:: diff

   -    public function __construct(
   -        $content,
   -        protected $lead = null,
   +    public function __construct(
   +        \Mautic\LeadBundle\Entity\Lead|array|string|null $content,
   +        protected \Mautic\LeadBundle\Entity\Lead|array|null $lead = null,

.. code:: diff

   -    public function getLead()
   +    public function getLead(): \Mautic\LeadBundle\Entity\Lead|array|null

``TokenReplacementEvent`` is ``final`` in Mautic 8, and the methods in the preceding examples live on the new abstract ``Mautic\CoreBundle\Event\AbstractTokenReplacementEvent``. If your Plugin has an event class that extends ``TokenReplacementEvent``, extend ``AbstractTokenReplacementEvent`` instead, which provides the same methods. For the removed Dynamic Content token constant, see :ref:`DynamicContentBundle <mautic 8 dynamiccontentbundle>`.

.. vale off

CustomContentEvent
==================

.. vale on

``Mautic\CoreBundle\Event\CustomContentEvent`` is a ``final`` class, so the override risk doesn't apply. It also declares ``strict_types``. ``checkContext()`` now types both parameters as ``string``, narrowing the ``$context`` parameter that previously carried the ``PHPDoc`` type ``string|null``. The parameter order is ``$viewName`` then ``$context``.

.. code:: diff

   -    public function checkContext($viewName, $context): bool
   +    public function checkContext(string $viewName, string $context): bool

If your Plugin dispatches this Event, the constructor promotes both parameters to ``readonly`` typed properties, and ``getViewName()`` and ``getContext()`` gain return types.

.. code:: diff

   -    public function __construct(
   -        private $viewName,
   -        private $context = null,
   +    public function __construct(
   +        private readonly ?string $viewName,
   +        private readonly ?string $context = null,

.. code:: diff

   -    public function getViewName()
   +    public function getViewName(): ?string

   -    public function getContext()
   +    public function getContext(): ?string

.. vale off

CustomButtonEvent
=================

.. vale on

Plugins that add custom buttons use ``Mautic\CoreBundle\Event\CustomButtonEvent``. ``addButton()`` narrows ``$location`` to ``?string`` and widens ``$route`` to ``array|string|null``, so pass a ``string`` or ``null`` for ``$location``. Its sibling ``addButtons()`` keeps its original signature and needs no action.

.. code:: diff

   -    public function addButton(array $button, $location = null, $route = null): static
   +    public function addButton(array $button, ?string $location = null, array|string|null $route = null): static

.. _mautic 8 builderevent:

.. vale off

BuilderEvent
============

.. vale on

``getRequested()`` now requires a ``string $type`` argument, and the ``protected`` ``$requested`` property carries the type ``string|array``. The internal comparison changed from loose ``==`` to strict ``===``, which is equivalent under the new types. Because ``getRequested()`` is ``protected``, this affects only a Plugin that subclasses ``Mautic\CoreBundle\Event\BuilderEvent``. An override must add the required ``string $type`` parameter, and an assignment to the newly typed ``$requested`` property must pass a ``string`` or ``array``.

.. code:: diff

   -    protected function getRequested($type): bool
   +    protected function getRequested(string $type): bool

.. code:: diff

   -        protected $requested = 'all',
   +        protected string|array $requested = 'all',

Mautic 8 also removes the ``addTokensFromHelper()`` and ``getTokensFromHelper()`` methods, which Mautic deprecated in Mautic 7.2. A Plugin that still calls one of them on an Email or Landing Page builder event, such as ``EmailOnBuildEvent`` or ``PageBuilderEvent``, fails with an undefined method error. Build the tokens with ``Mautic\CoreBundle\Helper\BuilderTokenHelper::getFormattedTokens()`` and pass them to ``$event->addTokens()`` instead:

.. code-block:: php

    // Before:
    public function onEmailBuild(EmailOnBuildEvent $event): void
    {
        $event->addTokensFromHelper($tokenHelper, $tokenRegex, 'label', 'alias');
    }

    // After:
    public function onEmailBuild(EmailOnBuildEvent $event): void
    {
        $tokenHelper = $this->builderTokenHelperFactory->getBuilderTokenHelper('page');
        $tokenFilter = $event->getTokenFilter();
        $tokens      = $tokenHelper->getFormattedTokens(
            $tokenRegex,
            TokenFormatOptions::simplePrefix('mautic.page.page'),
            'label' === $tokenFilter['target'] ? $tokenFilter['filter'] : '',
            'label', // Label column
            'alias'  // Value column
        );

        if ($tokens) {
            $event->addTokens($tokens);
        }
    }

For more about ``getFormattedTokens()``, see :doc:`/plugin_extensions/emails`.

.. vale off

MaintenanceEvent
================

.. vale on

The constructor of ``Mautic\CoreBundle\Event\MaintenanceEvent`` promotes ``$daysOld`` to a typed ``int`` property, which removes the explicit ``(int)`` cast. This preserves behavior for ``int`` or numeric-string input, because the class doesn't declare ``strict_types``. ``setStat()`` now types ``$parameters`` as ``array`` and keeps its ``= []`` default, so only a caller passing a non-array value breaks. Pass an array, or omit the argument.

.. code:: diff

   -    public function __construct(
   -        $daysOld,
   +    public function __construct(
   +        protected int $daysOld,

.. code:: diff

   -    public function setStat($key, $recordCount, $sql = null, $parameters = []): void
   +    public function setStat($key, $recordCount, $sql = null, array $parameters = []): void

.. vale off

IconEvent
=========

.. vale on

``Mautic\CoreBundle\Event\IconEvent`` no longer carries the ``CorePermissions`` service. Its constructor takes no arguments, and the class no longer provides ``getSecurity()``. If your icon subscriber called ``$event->getSecurity()``, inject ``Mautic\CoreBundle\Security\Permissions\CorePermissions`` into the subscriber's constructor and use that instead. If your Plugin creates an ``IconEvent`` itself, drop the constructor argument:

.. code:: diff

   -    $iconEvent = new IconEvent($this->security);
   +    $iconEvent = new IconEvent();

.. vale off

PreExecuteEvent
===============

.. vale on

Mautic dispatches ``Mautic\CoreBundle\Doctrine\Common\DataFixtures\Event\PreExecuteEvent`` when it creates the purger for loading data fixtures. The event no longer carries the entity manager. Its constructor takes only the purge mode, and the class no longer provides ``getEntityManager()``. If a fixture listener called ``$event->getEntityManager()``, inject ``Doctrine\ORM\EntityManagerInterface`` into the fixture class and use that instead:

.. code:: diff

   -    $event->getEntityManager()->getConnection()->executeStatement($sql);
   +    $this->entityManager->getConnection()->executeStatement($sql);

.. vale off

Services in event constructors
==============================

.. vale on

A new :xref:`phpstan` rule, ``mautic.noServiceInEventConstructor``, flags event classes that accept a service in their constructor only to hand it to listeners. It checks for services such as ``CorePermissions``, ``EntityManagerInterface``, and ``TranslatorInterface``. Mautic's ``phpstan.neon`` enables the rule, so ``composer phpstan`` also flags matching event classes in your Plugin. Inject the service into the listener that needs it, and keep the event limited to the values it carries.

Several other ``CoreBundle`` event classes gained native types that match their existing ``PHPDoc``, so your Plugin needs no action for ``CustomAssetsEvent``, ``BuildJsEvent``, ``CommandListEvent``, and ``GlobalSearchEvent``.

.. _mautic 8 dashboardbundle:

.. vale off

DashboardBundle
***************

.. vale on

Mautic 8 adds type declarations to the Dashboard Widget entity and two Dashboard Widget event classes, and deletes the ``DashboardEvents`` class.

.. vale off

DashboardEvents constants
=========================

.. vale on

Mautic 8 deletes the ``Mautic\DashboardBundle\DashboardEvents`` class. A subscriber that still references one of its constants fails with a ``Class "Mautic\DashboardBundle\DashboardEvents" not found`` error, and a subscriber keyed on a raw event name, such as ``mautic.dashboard_on_widget_detail_generate``, silently receives nothing. Key ``getSubscribedEvents()`` on the event class in the ``Mautic\DashboardBundle\Event`` namespace instead:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Removed ``DashboardEvents`` constant
     - Event class
   * - ``DASHBOARD_ON_MODULE_LIST_GENERATE``
     - ``WidgetTypeListEvent``
   * - ``DASHBOARD_ON_MODULE_FORM_GENERATE``
     - ``WidgetFormEvent``
   * - ``DASHBOARD_ON_MODULE_DETAIL_PRE_LOAD``
     - ``PreLoadWidgetDetailEvent``
   * - ``DASHBOARD_ON_MODULE_DETAIL_GENERATE``
     - ``GenerateWidgetDetailEvent``

The two detail events used to share one ``WidgetDetailEvent`` object. For the changes to that class, see :ref:`WidgetDetailEvent <Plugins/update_m7_to_m8:WidgetDetailEvent>`.

.. vale off

Widget entity
=============

.. vale on

Widget subscribers read the settings and data of a Widget from ``Mautic\DashboardBundle\Entity\Widget``. ``getParams()`` and ``getTemplateData()`` now declare the ``array`` return type they already returned, so calls to them need no change. If your Plugin extends ``Widget`` and overrides either method, add the ``array`` return type to the override. Otherwise PHP raises a fatal error when it loads your class:

.. code:: diff

   - public function getParams()
   + public function getParams(): array

.. code:: diff

   - public function getTemplateData()
   + public function getTemplateData(): array

.. vale off

WidgetDetailEvent
=================

.. vale on

Widget subscribers set the Widget template on ``Mautic\DashboardBundle\Event\WidgetDetailEvent``. ``setTemplate()`` types ``$template`` as ``string``:

.. code:: diff

   - public function setTemplate($template): void
   + public function setTemplate(string $template): void

Mautic 8 also removes the legacy filesystem Widget cache. It drops ``setCacheDir()`` and ``setCacheTimeout()`` entirely, makes the constructor's ``$cacheProvider`` argument required, and drops the second ``$skipCache`` parameter from ``setTemplateData()``:

.. code:: diff

   - public function setTemplateData(array $templateData, $skipCache = false): void
   + public function setTemplateData(array $templateData): void

Widget data now caches only through ``Mautic\CacheBundle\Cache\CacheProviderTagAwareInterface``, using the lifetime from ``Widget::getCacheTimeout()``. If your Plugin calls ``setCacheDir()``, ``setCacheTimeout()``, or passes a second argument to ``setTemplateData()``, remove the call or the argument.

``WidgetDetailEvent`` is now an abstract base class for the ``final`` ``PreLoadWidgetDetailEvent`` and ``GenerateWidgetDetailEvent`` classes that Mautic dispatches, so key your subscriber on one of those classes, as the :ref:`DashboardEvents constants <Plugins/update_m7_to_m8:DashboardEvents constants>` table shows. A listener method can keep its ``WidgetDetailEvent`` type hint:

.. code:: diff

   - DashboardEvents::DASHBOARD_ON_MODULE_DETAIL_GENERATE => ['onWidgetDetailGenerate', 0],
   + GenerateWidgetDetailEvent::class                    => ['onWidgetDetailGenerate', 0],

PHP can't instantiate an abstract class, so code that creates a ``WidgetDetailEvent`` directly, such as a Plugin test, must create ``GenerateWidgetDetailEvent`` or ``PreLoadWidgetDetailEvent`` instead. ``Mautic\DashboardBundle\Factory\WidgetDetailEventFactory`` replaces its ``create()`` method with ``createPreLoad()`` and ``createGenerate()``, and its constructor no longer takes the ``UserHelper``, ``CoreParametersHelper``, and ``PathsHelper`` arguments.

.. vale off

WidgetTypeListEvent
===================

.. vale on

Plugins register a Widget type on ``Mautic\DashboardBundle\Event\WidgetTypeListEvent``, a ``final`` class, so the override risk doesn't apply. ``addType()`` types only ``$bundle``, and leaves ``$widgetType`` without a type:

.. code:: diff

   - public function addType($widgetType, $bundle = 'others'): void
   + public function addType($widgetType, string $bundle = 'others'): void

.. _mautic 8 dynamiccontentbundle:

.. vale off

DynamicContentBundle
********************

.. vale on

Mautic 8 removes these ``Mautic\DynamicContentBundle\DynamicContentEvents`` constants. A subscriber that still references one of them fails with ``Error: Undefined constant``:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Removed ``DynamicContentEvents`` constant
     - Replacement
   * - ``ON_CONTACTS_FILTER_EVALUATE``
     - Key on ``Mautic\DynamicContentBundle\Event\ContactFiltersEvaluateEvent::class``.
   * - ``TOKEN_REPLACEMENT``
     - Key on ``Mautic\CoreBundle\Event\TokenReplacementEvent::class``.
   * - ``CATEGORY_PRE_SAVE``, ``CATEGORY_POST_SAVE``, ``CATEGORY_PRE_DELETE``, and ``CATEGORY_POST_DELETE``
     - Use the ``Mautic\CategoryBundle\CategoryEvents`` constants with the same names, which have the same string values.

``DynamicContentEvents::TOKEN_REPLACEMENT`` held the ``mautic.dwc_token_replacement`` event name, which Mautic dispatched right before it returned the content of a Dynamic Content item. The EmailBundle also dispatches ``TokenReplacementEvent`` by its class to replace the Dynamic Content tokens in an Email, so a subscriber keyed on ``TokenReplacementEvent::class`` receives both events. To handle only Dynamic Content items, return early unless the array from ``getClickthrough()`` contains a ``dynamic_content_id`` key:

.. code-block:: php

   public function onTokenReplacement(TokenReplacementEvent $event): void
   {
       if (!array_key_exists('dynamic_content_id', $event->getClickthrough())) {
           return;
       }

       // Replace your tokens in the Dynamic Content item.
   }

``TokenReplacementEvent`` is ``final``, so a Plugin's event class can't extend it. See :ref:`TokenReplacementEvent <Plugins/update_m7_to_m8:TokenReplacementEvent>`.

.. _mautic 8 emailbundle:

.. vale off

EmailBundle
***********

.. vale on

Mautic 8 adds type declarations to four Email event classes and removes most ``EmailEvents`` constants.

.. vale off

EmailEvents constants
=====================

.. vale on

Mautic 8 removes these ``Mautic\EmailBundle\EmailEvents`` constants and dispatches the events by their event class. A subscriber that still references one of them fails with ``Error: Undefined constant``. Key ``getSubscribedEvents()`` on the event class, which is in the ``Mautic\EmailBundle\Event`` namespace unless the table shows a full class name:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Removed ``EmailEvents`` constant
     - Event class
   * - ``EMAIL_ON_BUILD``
     - ``EmailOnBuildEvent``
   * - ``EMAIL_ON_DISPLAY``
     - ``EmailDisplayEvent``
   * - ``EMAIL_PRE_SEND``
     - ``EmailPreSendEvent``
   * - ``EMAIL_ON_TOGGLE_PUBLISH``
     - ``EmailOnTogglePublishEvent``
   * - ``EMAIL_PRE_SAVE``
     - ``EmailPreSaveEvent``
   * - ``EMAIL_POST_SAVE``
     - ``EmailPostSaveEvent``
   * - ``EMAIL_PRE_DELETE``
     - ``EmailPreDeleteEvent``
   * - ``EMAIL_POST_DELETE``
     - ``EmailPostDeleteEvent``
   * - ``ON_EMAIL_STAT_PRE_SAVE``
     - ``EmailStatEvent``
   * - ``ON_EMAIL_STAT_POST_SAVE``
     - ``EmailStatPostSaveEvent``
   * - ``ON_EMAIL_EDIT_SUBMIT``
     - ``EmailEditSubmitEvent``
   * - ``EMAIL_ON_REPLY``
     - ``EmailReplyEvent``
   * - ``ON_EMAIL_VALIDATION``
     - ``EmailValidationEvent``
   * - ``ON_TRANSPORT_WEBHOOK``
     - ``TransportWebhookEvent``
   * - ``MONITORED_EMAIL_CONFIG``
     - ``MonitoredEmailEvent``
   * - ``TOKEN_REPLACEMENT``
     - ``Mautic\CoreBundle\Event\TokenReplacementEvent``
   * - ``ON_EMAIL_ADDRESS_TOKEN_REPLACEMENT``
     - ``OnEmailAddressTokenReplacementEvent``

For the ``EMAIL_PRE_FETCH`` and ``EMAIL_PARSE`` constants, see :ref:`ParseEmailEvent <Plugins/update_m7_to_m8:ParseEmailEvent>`.

Mautic 8 also deletes the ``EmailBuilderEvent`` class that it dispatched for ``EMAIL_ON_BUILD``. Type-hint your build listener with ``EmailOnBuildEvent`` instead. Because Mautic dispatches the send and display events separately, a listener keyed only on ``EmailSendEvent::class`` doesn't receive ``EmailDisplayEvent``, so a handler that served both ``EMAIL_ON_SEND`` and ``EMAIL_ON_DISPLAY`` must register under both keys:

.. code:: diff

   - EmailEvents::EMAIL_ON_BUILD   => ['onEmailBuild', 0],
   - EmailEvents::EMAIL_ON_SEND    => ['onEmailGenerate', 0],
   - EmailEvents::EMAIL_ON_DISPLAY => ['onEmailGenerate', 0],
   + EmailOnBuildEvent::class      => ['onEmailBuild', 0],
   + EmailSendEvent::class         => ['onEmailGenerate', 0],
   + EmailDisplayEvent::class      => ['onEmailGenerate', 0],

Mautic keeps the ``EMAIL_ON_SEND`` and ``EMAIL_ON_OPEN`` constants, because their string values are also Webhook event type identifiers, but it doesn't dispatch events under them. A subscriber keyed on one of them silently receives nothing, so key it on ``EmailSendEvent::class`` or ``EmailOpenEvent::class`` instead. The Campaign registration constants, such as ``ON_CAMPAIGN_BATCH_ACTION``, and ``ON_SENT_EMAIL_TO_USER`` don't change.

.. vale off

EmailSendEvent
==============

.. vale on

Plugins add Email tokens through ``Mautic\EmailBundle\Event\EmailSendEvent``. ``addToken()`` and ``addTextHeader()`` type both parameters as ``string``:

.. code:: diff

   - public function addToken($key, $value): void
   + public function addToken(string $key, string $value): void

.. code:: diff

   - public function addTextHeader($name, $value): void
   + public function addTextHeader(string $name, string $value): void

.. vale off

EmailValidationEvent
====================

.. vale on

Email validation subscribers mark an address invalid on ``Mautic\EmailBundle\Event\EmailValidationEvent``. ``setInvalid()`` types ``$reason`` as ``string``:

.. code:: diff

   - public function setInvalid($reason): void
   + public function setInvalid(string $reason): void

.. vale off

MonitoredEmailEvent
===================

.. vale on

Subscribers that watch a monitored mailbox register folders on ``Mautic\EmailBundle\Event\MonitoredEmailEvent``. ``addFolder()`` types all of its parameters as ``string``:

.. code:: diff

   - public function addFolder($bundleKey, $folderKey, $label, $default = ''): void
   + public function addFolder(string $bundleKey, string $folderKey, string $label, string $default = ''): void

On ``getData()``, only ``$default`` gains a type:

.. code:: diff

   - public function getData($bundleKey, $folderKey, $default = '')
   + public function getData($bundleKey, $folderKey, string $default = '')

.. vale off

ParseEmailEvent
===============

.. vale on

Subscribers that parse fetched mail use ``Mautic\EmailBundle\Event\ParseEmailEvent``. ``isApplicable()`` types ``$bundleKey`` as ``string`` and ``$folderKeys`` as ``string|array``:

.. code:: diff

   - public function isApplicable($bundleKey, $folderKeys): bool
   + public function isApplicable(string $bundleKey, string|array $folderKeys): bool

Mautic 8 also splits the pre-fetch phase out of ``ParseEmailEvent``. Before Mautic 8, one ``ParseEmailEvent`` object served both the ``EmailEvents::EMAIL_PRE_FETCH`` and ``EmailEvents::EMAIL_PARSE`` names. Mautic removed both constants and now dispatches two event classes by class name:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Removed ``EmailEvents`` constant
     - Event class
   * - ``EMAIL_PRE_FETCH``
     - ``Mautic\EmailBundle\Event\PreFetchEmailEvent``
   * - ``EMAIL_PARSE``
     - ``Mautic\EmailBundle\Event\ParseEmailEvent``

``setCriteriaRequest()``, ``getCriteriaRequests()``, and ``getMarkAsSeenInstructions()`` moved from ``ParseEmailEvent`` to ``PreFetchEmailEvent``. ``ParseEmailEvent`` keeps only the fetched messages and ``isApplicable()``. Re-key your subscriber on the event classes and type-hint the pre-fetch listener with ``PreFetchEmailEvent``:

.. code:: diff

   - EmailEvents::EMAIL_PRE_FETCH => ['onPreFetch', 0],
   - EmailEvents::EMAIL_PARSE     => ['onParse', 0],
   + PreFetchEmailEvent::class    => ['onPreFetch', 0],
   + ParseEmailEvent::class       => ['onParse', 0],

   - public function onPreFetch(ParseEmailEvent $event): void
   + public function onPreFetch(PreFetchEmailEvent $event): void

On ``PreFetchEmailEvent``, ``setCriteriaRequest()`` types ``$bundleKey`` as ``string`` and ``$folderKeys`` as ``string|array``, and leaves ``$criteria`` without a type:

.. code:: diff

   - public function setCriteriaRequest($bundleKey, $folderKeys, $criteria, bool $markAsSeen = true): void
   + public function setCriteriaRequest(string $bundleKey, string|array $folderKeys, $criteria, bool $markAsSeen = true): void

.. vale off

For an Email extension example, see :doc:`/plugin_extensions/emails`.

.. _mautic 8 formbundle:

FormBundle
**********

.. vale on

Mautic 8 adds type declarations to two Form event classes and dispatches four Form events by their event class.

.. vale off

FormEvents constants
====================

.. vale on

Mautic 8 dispatches these FormBundle events by their event class. The ``Mautic\FormBundle\FormEvents`` constants still exist, but Mautic doesn't dispatch the events under them, so a subscriber keyed on one silently receives nothing. Key ``getSubscribedEvents()`` on the event class in the ``Mautic\FormBundle\Event`` namespace instead:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - ``FormEvents`` constant
     - Event class
   * - ``FORM_ON_SUBMIT``
     - ``SubmissionEvent``
   * - ``FORM_ON_BUILD``
     - ``FormBuilderEvent``
   * - ``ON_OBJECT_COLLECT``
     - ``ObjectCollectEvent``
   * - ``ON_FIELD_COLLECT``
     - ``FieldCollectEvent``

The string value of ``FORM_ON_SUBMIT``, ``mautic.form_on_submit``, stays the Webhook event type identifier, so Webhook configuration doesn't change. The other ``FormEvents`` constants, such as the ``FORM_*`` and ``FIELD_*`` save and delete groups, ``ON_EXECUTE_SUBMIT_ACTION``, and ``ON_FORM_VALIDATE``, don't change.

.. vale off

FormBuilderEvent
================

.. vale on

Plugins register a custom Form Field or validation rule on ``Mautic\FormBundle\Event\FormBuilderEvent``. ``addFormField()`` and ``addValidator()`` type ``$key`` as ``string``:

.. code:: diff

   - public function addFormField($key, array $field): void
   + public function addFormField(string $key, array $field): void

.. code:: diff

   - public function addValidator($key, array $validator): void
   + public function addValidator(string $key, array $validator): void

.. vale off

SubmissionEvent
===============

.. vale on

Of all the classes on this list, ``Mautic\FormBundle\Event\SubmissionEvent`` has the biggest impact on Plugin authors. ``setPostSubmitCallbackResponse()`` narrows its second argument from ``mixed`` to a ``\Symfony\Component\HttpFoundation\RedirectResponse``, so passing any other response type now raises a ``TypeError`` at runtime:

.. code:: diff

   - public function setPostSubmitCallbackResponse($key, $callbackResponse): static
   + public function setPostSubmitCallbackResponse(string $key, \Symfony\Component\HttpFoundation\RedirectResponse $callbackResponse): static

``getPostSubmitCallback()`` types ``$key`` as ``?string``, and the post-submit response getter and setter gain matching types:

.. code:: diff

   - public function getPostSubmitCallback($key = null)
   + public function getPostSubmitCallback(?string $key = null)

.. code:: diff

   - public function getPostSubmitResponse()
   + public function getPostSubmitResponse(): \Symfony\Component\HttpFoundation\Response|array|null

.. code:: diff

   - public function setPostSubmitResponse($response): void
   + public function setPostSubmitResponse(array|\Symfony\Component\HttpFoundation\Response $response): void

.. vale off

For a Form extension example, see :doc:`/plugin_extensions/forms`.

.. _mautic 8 integrationsbundle:

IntegrationsBundle
******************

.. vale on

Mautic 8 adds type declarations to one Integrations token event class and deletes the ``IntegrationEvents`` class.

.. vale off

IntegrationEvents constants
===========================

.. vale on

Mautic 8 deletes the ``Mautic\IntegrationsBundle\IntegrationEvents`` class and dispatches every IntegrationsBundle event by its event class. A subscriber that still references an ``IntegrationEvents`` constant fails with a ``Class "Mautic\IntegrationsBundle\IntegrationEvents" not found`` error, and a subscriber keyed on a raw event name, such as ``mautic.integration.INTEGRATION_FIND_INTERNAL_RECORDS``, silently receives nothing. Key ``getSubscribedEvents()`` on the event class in the ``Mautic\IntegrationsBundle\Event`` namespace instead:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Removed ``IntegrationEvents`` constant
     - Event class
   * - ``INTEGRATION_POST_EXECUTE``
     - ``SyncEvent``
   * - ``INTEGRATION_CONFIG_FORM_LOAD``
     - ``FormLoadEvent``
   * - ``INTEGRATION_CONFIG_ON_GENERATE_AUTH_URL``
     - ``ConfigAuthUrlEvent``
   * - ``INTEGRATION_CONFIG_BEFORE_SAVE``
     - ``ConfigBeforeSaveEvent``
   * - ``INTEGRATION_CONFIG_AFTER_SAVE``
     - ``ConfigAfterSaveEvent``
   * - ``INTEGRATION_API_KEYS_BEFORE_SAVE``
     - ``KeysSaveEvent``
   * - ``INTEGRATION_KEYS_BEFORE_ENCRYPTION``
     - ``KeysEncryptionEvent``
   * - ``INTEGRATION_KEYS_AFTER_DECRYPTION``
     - ``KeysDecryptionEvent``
   * - ``INTEGRATION_MAUTIC_SYNC_FIELDS_LOAD``
     - ``MauticSyncFieldsLoadEvent``
   * - ``INTEGRATION_COLLECT_INTERNAL_OBJECTS``
     - ``InternalObjectEvent``
   * - ``INTEGRATION_CREATE_INTERNAL_OBJECTS``
     - ``InternalObjectCreateEvent``
   * - ``INTEGRATION_UPDATE_INTERNAL_OBJECTS``
     - ``InternalObjectUpdateEvent``
   * - ``INTEGRATION_FIND_INTERNAL_RECORD``
     - ``InternalObjectFindByIdEvent``
   * - ``INTEGRATION_FIND_INTERNAL_RECORDS``
     - ``InternalObjectFindEvent``
   * - ``INTEGRATION_FIND_OWNER_IDS``
     - ``InternalObjectOwnerEvent``
   * - ``INTEGRATION_BUILD_INTERNAL_OBJECT_ROUTE``
     - ``InternalObjectRouteEvent``
   * - ``INTEGRATION_OBJECT_TOKEN_EVENT``
     - ``MappedIntegrationObjectTokenEvent``
   * - ``INTEGRATION_BEFORE_CONTACT_FIELD_CHANGES``
     - ``InternalContactFieldChangesEvent``
   * - ``INTEGRATION_BEFORE_COMPANY_FIELD_CHANGES``
     - ``InternalCompanyFieldChangesEvent``
   * - ``INTEGRATION_BEFORE_FULL_CONTACT_REPORT_BUILD``
     - ``InternalContactFullReportBuildEvent``
   * - ``INTEGRATION_BEFORE_FULL_COMPANY_REPORT_BUILD``
     - ``InternalCompanyFullReportBuildEvent``
   * - ``INTEGRATION_BATCH_SYNC_COMPLETED_INTEGRATION_TO_MAUTIC``
     - ``IntegrationToMauticSyncCompletedEvent``
   * - ``INTEGRATION_BATCH_SYNC_COMPLETED_MAUTIC_TO_INTEGRATION``
     - ``MauticToIntegrationSyncCompletedEvent``

Several of these events used to share one event object under two constants. ``ConfigSaveEvent``, ``InternalContactEvent``, ``InternalCompanyEvent``, and ``CompletedSyncIterationEvent`` are now abstract base classes for the matching classes in the preceding table. A listener method can keep its type hint on the base class, and both configuration save subclasses keep the ``getIntegrationConfiguration()`` and ``getIntegration()`` methods. Code that creates one of these base classes with ``new``, such as a Plugin test, must create the matching subclass instead.

.. vale off

MappedIntegrationObjectTokenEvent
=================================

.. vale on

Integration subscribers register mapped-object tokens on ``Mautic\IntegrationsBundle\Event\MappedIntegrationObjectTokenEvent``. On ``addToken()``, only the last three parameters gain ``string`` types, and ``$integrationName``, ``$objectName``, and ``$objectLink`` keep none:

.. code:: diff

   - public function addToken($integrationName, $objectName, $objectLink, $title = '', $linkText = 'Link Text', $default = 'Default Value'): void
   + public function addToken($integrationName, $objectName, $objectLink, string $title = '', string $linkText = 'Link Text', string $default = 'Default Value'): void

.. _mautic 8 leadbundle:

.. vale off

LeadBundle
**********

.. vale on

Mautic 8 dispatches the LeadBundle events by their event class and adds type declarations to three Contact and Segment event classes and to the ``ContactTracker`` service.

.. vale off

LeadEvents constants
====================

.. vale on

Mautic 8 dispatches the LeadBundle events for Contacts, Companies, Segments, Custom Fields, Tags, notes, devices, imports, and Contact exports by their event class. The event classes live in the ``Mautic\LeadBundle\Event`` namespace, except the six ``*ColumnEvent`` and ``*ColumnBackgroundEvent`` classes, which live in ``Mautic\LeadBundle\Field\Event``.

Mautic 8 removes these ``Mautic\LeadBundle\LeadEvents`` constants, so a subscriber that still references one of them fails with ``Error: Undefined constant``. Key ``getSubscribedEvents()`` on the event class instead:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Removed ``LeadEvents`` constant
     - Event class
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
   * - ``LIST_FILTERS_ON_FILTERING``
     - ``LeadListFilteringEvent``
   * - ``LIST_PRE_PROCESS_LIST``
     - ``ListPreProcessListEvent``
   * - ``SEGMENT_DICTIONARY_ON_GENERATE``
     - ``SegmentDictionaryGenerationEvent``
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

Mautic 8 also removes the ``DoNotContactAddEvent::ADD_DONOT_CONTACT`` and ``DoNotContactRemoveEvent::REMOVE_DONOT_CONTACT`` constants, so key the subscriber on ``DoNotContactAddEvent::class`` or ``DoNotContactRemoveEvent::class``.

Mautic keeps these ``LeadEvents`` constants, but it doesn't dispatch events under them, so a subscriber keyed on one silently receives nothing. Key it on the event class instead:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Kept ``LeadEvents`` constant
     - Event class
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
   * - ``CHANNEL_SUBSCRIPTION_CHANGED``
     - ``ChannelSubscriptionChange``
   * - ``TIMELINE_ON_GENERATE``
     - ``LeadTimelineEvent``
   * - ``LEAD_UTMTAGS_ADD``
     - ``LeadUtmTagsEvent``
   * - ``LEAD_CATEGORY_CHANGE``
     - ``CategoryChangeEvent``
   * - ``LEAD_BUILD_SEARCH_COMMANDS``
     - ``LeadBuildSearchEvent``
   * - ``COMPANY_BUILD_SEARCH_COMMANDS``
     - ``CompanyBuildSearchEvent``
   * - ``ADJUST_FILTER_FORM_TYPE_FOR_FIELD``
     - ``FormAdjustmentEvent``
   * - ``COLLECT_OPERATORS_FOR_FIELD_TYPE``
     - ``TypeOperatorsEvent``
   * - ``COLLECT_OPERATORS_FOR_FIELD``
     - ``FieldOperatorsEvent``
   * - ``COLLECT_FILTER_CHOICES_FOR_LIST_FIELD_TYPE``
     - ``ListFieldChoicesEvent``
   * - ``SEGMENT_ON_DECORATOR_DELEGATE``
     - ``LeadListFiltersDecoratorDelegateEvent``
   * - ``LIST_FILTERS_MERGE``
     - ``LeadListMergeFiltersEvent``
   * - ``LIST_FILTERS_OPERATORS_ON_GENERATE``
     - ``LeadListFiltersOperatorsEvent``
   * - ``LIST_FILTERS_OPERATOR_QUERYBUILDER_ON_GENERATE``
     - ``SegmentOperatorQueryBuilderEvent``
   * - ``LIST_FILTERS_QUERYBUILDER_GENERATED``
     - ``LeadListQueryBuilderGeneratedEvent``
   * - ``IMPORT_ON_INITIALIZE``
     - ``ImportInitEvent``
   * - ``IMPORT_ON_FIELD_MAPPING``
     - ``ImportMappingEvent``
   * - ``IMPORT_ON_PROCESS``
     - ``ImportProcessEvent``
   * - ``IMPORT_ON_VALIDATE``
     - ``ImportValidateEvent``
   * - ``LEAD_FIELD_PRE_ADD_COLUMN``
     - ``AddColumnEvent``
   * - ``LEAD_FIELD_PRE_ADD_COLUMN_BACKGROUND_JOB``
     - ``AddColumnBackgroundEvent``
   * - ``LEAD_FIELD_PRE_UPDATE_COLUMN``
     - ``UpdateColumnEvent``
   * - ``LEAD_FIELD_PRE_UPDATE_COLUMN_BACKGROUND_JOB``
     - ``UpdateColumnBackgroundEvent``
   * - ``LEAD_FIELD_PRE_DELETE_COLUMN``
     - ``DeleteColumnEvent``
   * - ``LEAD_FIELD_PRE_DELETE_COLUMN_BACKGROUND_JOB``
     - ``DeleteColumnBackgroundEvent``

Mautic keeps the first eight constants in this table because it also uses them as Webhook event type identifiers, so Webhook configuration doesn't change.

.. vale off

Shared LeadBundle event classes
===============================

.. vale on

Before Mautic 8, several ``LeadEvents`` constants shared one event class. Each event now has its own subclass of that shared class, which changes code that creates or reads these events:

* ``CompanyEvent``, ``CompanyMergeEvent``, ``ContactExportSchedulerEvent``, ``ImportEvent``, ``LeadDeviceEvent``, ``LeadFieldEvent``, ``LeadListEvent``, ``LeadMergeEvent``, ``LeadNoteEvent``, ``SaveBatchLeadsEvent``, ``TagEvent``, and ``TagMergeEvent`` are now ``abstract``. A listener method can keep its type hint on the shared class, but code that creates one of these events with ``new``, such as a Plugin test, must create the matching subclass from the preceding tables.
* ``LeadEvent`` is no longer ``final``, because the Contact lifecycle classes such as ``LeadPreSaveEvent`` and ``LeadPostSaveEvent`` extend it.
* The event that Mautic dispatches before a save, delete, or merge and the event that it dispatches afterward are now separate objects. A value that a listener sets on the earlier event isn't available to listeners of the later one.
* ``Mautic\LeadBundle\Field\Dispatcher\FieldSaveDispatcher::dispatchEvent()`` now takes the ``LeadFieldEvent`` subclass to dispatch, instead of an event name, the field entity, and an ``isNew`` flag.

.. vale off

ContactIdentificationEvent
==========================

.. vale on

Subscribers that identify a Contact from a tracked link click use ``Mautic\LeadBundle\Event\ContactIdentificationEvent``, a ``final`` class, so the override risk doesn't apply. ``setIdentifiedContact()`` types ``$channel`` as ``string``, and ``getIdentifier()`` gains a ``?string`` return type:

.. code:: diff

   - public function setIdentifiedContact(Lead $contact, $channel): void
   + public function setIdentifiedContact(Lead $contact, string $channel): void

.. code:: diff

   - public function getIdentifier()
   + public function getIdentifier(): ?string

.. vale off

LeadListFiltersOperatorsEvent
=============================

.. vale on

Plugins register custom Segment filter operators on ``Mautic\LeadBundle\Event\LeadListFiltersOperatorsEvent``, a ``final`` class. ``addOperator()`` types ``$operatorKey`` as ``string`` and ``$operatorConfig`` as ``array``:

.. code:: diff

   - public function addOperator($operatorKey, $operatorConfig): void
   + public function addOperator(string $operatorKey, array $operatorConfig): void

.. vale off

ListPreProcessListEvent
=======================

.. vale on

Subscribers that pre-process a Segment use ``Mautic\LeadBundle\Event\ListPreProcessListEvent``, a ``final`` class. ``setResult()`` now requires a ``bool``, and ``getResult()`` returns ``?bool``, which is ``null`` until a subscriber sets a result:

.. code:: diff

   - public function setResult($result): static
   + public function setResult(bool $result): static

.. code:: diff

   - public function getResult()
   + public function getResult(): ?bool

.. vale off

ContactTracker
==============

.. vale on

Plugins that read or set the tracked Contact use the ``Mautic\LeadBundle\Tracker\ContactTracker`` service. ``setUseSystemContact()`` no longer accepts ``null``, so passing ``null`` now raises a ``TypeError`` at runtime:

.. code:: diff

   - public function setUseSystemContact(?bool $useSystemContact): void
   + public function setUseSystemContact(bool $useSystemContact): void

.. vale off

IdentifyCompanyHelper
=====================

.. vale on

``Mautic\LeadBundle\Helper\IdentifyCompanyHelper`` is now an Autowired, ``final readonly`` instance service instead of a static utility, and its constructor injects ``CompanyModel`` and ``CompanyLeadRepository``. ``identifyLeadsCompany()`` and ``findCompany()`` are now instance methods, and both drop their ``CompanyModel`` parameter:

.. code:: diff

   - public static function identifyLeadsCompany(array $data, $lead, CompanyModel $companyModel): array
   + public function identifyLeadsCompany(array $data, $lead): array

   - public static function findCompany(array $data, CompanyModel $companyModel): array
   + public function findCompany(array $data): array

Inject the helper and call it on the instance instead of calling it statically:

.. code:: diff

    use Mautic\LeadBundle\Helper\IdentifyCompanyHelper;

   +public function __construct(
   +    private IdentifyCompanyHelper $identifyCompanyHelper,
   +) {
   +}

   -[$company, $companyEntities] = IdentifyCompanyHelper::identifyLeadsCompany($data, $lead, $companyModel);
   +[$company, $companyEntities] = $this->identifyCompanyHelper->identifyLeadsCompany($data, $lead);

.. vale off

For a Contact extension example that uses ``ContactTracker``, see :doc:`/plugin_extensions/contacts`.

.. _mautic 8 focusbundle:

MauticFocusBundle
*****************

.. vale on

Mautic 8 dispatches ``MauticPlugin\MauticFocusBundle\Event\FocusViewEvent`` by its class. The ``MauticPlugin\MauticFocusBundle\FocusEvents::FOCUS_ON_VIEW`` constant still exists, but Mautic doesn't dispatch the event under it, so key ``getSubscribedEvents()`` on ``FocusViewEvent::class``. ``FocusEventTypes::FOCUS_ON_VIEW`` is a separate stat type identifier that doesn't change, so don't confuse the two.

.. _mautic 8 socialbundle:

.. vale off

MauticSocialBundle
******************

.. vale on

Mautic 8 removes the Monitor and Tweet save and delete constants from ``MauticPlugin\MauticSocialBundle\SocialEvents`` and dispatches these events by their event class. A subscriber that still references one of the constants, such as ``SocialEvents::TWEET_POST_SAVE``, fails with ``Error: Undefined constant``. Key ``getSubscribedEvents()`` on the event class in the ``MauticPlugin\MauticSocialBundle\Event`` namespace instead:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Removed ``SocialEvents`` constant
     - Event class
   * - ``MONITOR_PRE_SAVE``
     - ``MonitorPreSaveEvent``
   * - ``MONITOR_POST_SAVE``
     - ``MonitorPostSaveEvent``
   * - ``MONITOR_PRE_DELETE``
     - ``MonitorPreDeleteEvent``
   * - ``MONITOR_POST_DELETE``
     - ``MonitorPostDeleteEvent``
   * - ``MONITOR_POST_PROCESS``
     - ``SocialMonitorEvent``, which Mautic already dispatched by its class
   * - ``TWEET_PRE_SAVE``
     - ``TweetPreSaveEvent``
   * - ``TWEET_POST_SAVE``
     - ``TweetPostSaveEvent``
   * - ``TWEET_PRE_DELETE``
     - ``TweetPreDeleteEvent``
   * - ``TWEET_POST_DELETE``
     - ``TweetPostDeleteEvent``

Mautic 8 also removes the ``SocialEvent`` class. The Monitor events extend ``AbstractMonitorEvent``, which provides ``getMonitoring()``, and the Tweet events extend ``AbstractTweetEvent``, which provides ``getTweet()``.

.. _mautic 8 notificationbundle:

.. vale off

NotificationBundle
******************

.. vale on

Mautic 8 dispatches ``Mautic\NotificationBundle\Event\NotificationSendEvent`` by its class. The ``NotificationEvents::NOTIFICATION_ON_SEND`` constant still exists, but Mautic doesn't dispatch the event under it, so key ``getSubscribedEvents()`` on ``NotificationSendEvent::class``.

Mautic 8 also adds parameter types to three Notification entity classes. Plugins that create or update these entities must pass arguments of the declared types:

* ``Mautic\NotificationBundle\Entity\Notification`` - ``setName()``, ``setButton()``, and ``setMessage()`` take ``?string``, ``setNotificationType()`` takes ``string``, ``setUtmTags()`` takes ``array``, and ``setMobile()`` takes ``bool``.
* ``Mautic\NotificationBundle\Entity\PushID`` - ``setEnabled()`` and ``setMobile()`` take ``bool``.
* ``Mautic\NotificationBundle\Entity\Stat`` - ``setDateSent()`` narrows from ``mixed`` to ``\DateTimeInterface``, so passing a date string now raises a ``TypeError`` at runtime.

.. code:: diff

   - public function setDateSent($dateSent): void
   + public function setDateSent(\DateTimeInterface $dateSent): void

.. _mautic 8 pagebundle:

.. vale off

PageBundle
**********

.. vale on

Mautic 8 adds type declarations to one tracked-link redirect event class and dispatches several Landing Page and tracking events by their event class.

.. vale off

PageEvents constants
====================

.. vale on

Mautic 8 removes the ``Mautic\PageBundle\PageEvents::PAGE_ON_BUILD`` and ``PAGE_ON_DISPLAY`` constants, so a subscriber that still references one of them fails with ``Error: Undefined constant``. Mautic keeps the other constants in the following table, but it doesn't dispatch events under them, so a subscriber keyed on one silently receives nothing. Key ``getSubscribedEvents()`` on the event class in the ``Mautic\PageBundle\Event`` namespace instead:

.. list-table::
   :header-rows: 1
   :widths: 40 20 40

   * - ``PageEvents`` constant
     - Status
     - Event class
   * - ``PAGE_ON_BUILD``
     - Removed
     - ``PageBuilderEvent``
   * - ``PAGE_ON_DISPLAY``
     - Removed
     - ``PageDisplayEvent``
   * - ``PAGE_ON_HIT``
     - Kept
     - ``PageHitEvent``
   * - ``VIDEO_ON_HIT``
     - Kept
     - ``VideoHitEvent``
   * - ``ON_CONTACT_TRACKED``
     - Kept
     - ``TrackingEvent``
   * - ``ON_REDIRECT_GENERATE``
     - Kept
     - ``RedirectGenerationEvent``
   * - ``REDIRECT_DO_NOT_TRACK``
     - Kept
     - ``UntrackableUrlsEvent``

``PAGE_ON_HIT`` stays the Webhook event type identifier for Landing Page hits, so Webhook configuration doesn't change. ``PAGE_ON_TOGGLE_PUBLISH`` and the ``PAGE_PRE_SAVE``, ``PAGE_POST_SAVE``, ``PAGE_PRE_DELETE``, and ``PAGE_POST_DELETE`` constants share the ``PageEvent`` class, so Mautic still dispatches them under their string constants and subscribers keyed on them don't change.

.. vale off

RedirectGenerationEvent
=======================

.. vale on

Subscribers that build a tracked-link redirect use ``Mautic\PageBundle\Event\RedirectGenerationEvent``. ``setInClickthrough()`` narrows ``$value`` from ``mixed`` to ``string``, so passing a non-string value now raises a ``TypeError`` at runtime:

.. code:: diff

   - public function setInClickthrough($key, $value): void
   + public function setInClickthrough(string $key, string $value): void

.. _mautic 8 pluginbundle:

.. vale off

PluginBundle
************

.. vale on

Mautic 8 removes these ``Mautic\PluginBundle\PluginEvents`` constants and dispatches the events by their event class. A subscriber that still references one of them fails with ``Error: Undefined constant``. Key ``getSubscribedEvents()`` on the event class in the ``Mautic\PluginBundle\Event`` namespace instead:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Removed ``PluginEvents`` constant
     - Event class
   * - ``ON_PLUGIN_INSTALL``
     - ``PluginInstallEvent``
   * - ``ON_PLUGIN_UPDATE``
     - ``PluginUpdateEvent``
   * - ``PLUGIN_IS_PUBLISHED_STATE_CHANGING``
     - ``PluginIsPublishedEvent``
   * - ``PLUGIN_ON_INTEGRATION_CONFIG_SAVE``
     - ``PluginIntegrationEvent``
   * - ``PLUGIN_ON_INTEGRATION_REQUEST``
     - ``PluginIntegrationRequestEvent``
   * - ``PLUGIN_ON_INTEGRATION_RESPONSE``
     - ``PluginIntegrationResponseEvent``
   * - ``PLUGIN_ON_INTEGRATION_AUTH_REDIRECT``
     - ``PluginIntegrationAuthRedirectEvent``
   * - ``PLUGIN_ON_INTEGRATION_GET_AUTH_CALLBACK_URL``
     - ``PluginIntegrationAuthCallbackUrlEvent``
   * - ``PLUGIN_ON_INTEGRATION_FORM_DISPLAY``
     - ``PluginIntegrationFormDisplayEvent``
   * - ``PLUGIN_ON_INTEGRATION_FORM_BUILD``
     - ``PluginIntegrationFormBuildEvent``

For example, re-key a Plugin's install and update subscriber like this:

.. code:: diff

   - use Mautic\PluginBundle\PluginEvents;
   + use Mautic\PluginBundle\Event\PluginInstallEvent;
   + use Mautic\PluginBundle\Event\PluginUpdateEvent;

     public static function getSubscribedEvents(): array
     {
         return [
   -         PluginEvents::ON_PLUGIN_INSTALL => ['onPluginInstall', 0],
   -         PluginEvents::ON_PLUGIN_UPDATE  => ['onPluginUpdate', 0],
   +         PluginInstallEvent::class      => ['onPluginInstall', 0],
   +         PluginUpdateEvent::class       => ['onPluginUpdate', 0],
         ];
     }

Mautic 8 also removes ``ON_FORM_SUBMIT_ACTION_TRIGGERED``, which had no dispatcher or listener. The ``PLUGIN_ON_INTEGRATION_KEYS_ENCRYPT``, ``PLUGIN_ON_INTEGRATION_KEYS_DECRYPT``, and ``PLUGIN_ON_INTEGRATION_KEYS_MERGE`` constants share one event class, so they don't change. For the change to the Integration response event, see :ref:`Integration response event <Plugins/update_m7_to_m8:Integration response event>`.

.. _mautic 8 pointbundle:

.. vale off

PointBundle
***********

.. vale on

Mautic 8 adds type declarations to the Point TriggerEvent entity and two Point event classes. It also dispatches ``Mautic\PointBundle\Event\PointActionEvent`` and ``GroupScoreChangeEvent`` by their class. The ``PointEvents::POINT_ON_ACTION`` and ``PointGroupEvents::SCORE_CHANGE`` constants still exist, but Mautic doesn't dispatch the events under them, so key ``getSubscribedEvents()`` on ``PointActionEvent::class`` and ``GroupScoreChangeEvent::class``.

.. vale off

Point TriggerEvent entity
=========================

.. vale on

Point trigger subscribers work with ``Mautic\PointBundle\Entity\TriggerEvent``. ``setProperties()`` types ``$properties`` as ``array``, and ``setType()`` and ``setName()`` take ``string``:

.. code:: diff

   - public function setProperties($properties): static
   + public function setProperties(array $properties): static

.. code:: diff

   - public function setType($type): static
   + public function setType(string $type): static

.. code:: diff

   - public function setName($name): static
   + public function setName(string $name): static

.. vale off

PointBuilderEvent
=================

.. vale on

Plugins register a custom Point action on ``Mautic\PointBundle\Event\PointBuilderEvent``. ``addAction()`` types ``$key`` as ``string``:

.. code:: diff

   - public function addAction($key, array $action): void
   + public function addAction(string $key, array $action): void

Mautic 8 also dispatches ``PointBuilderEvent`` by its class name. Re-key your subscriber from ``PointEvents::POINT_ON_BUILD`` to ``PointBuilderEvent::class``, because a subscriber keyed on the constant or the ``mautic.point_on_build`` string silently receives nothing.

.. vale off

TriggerBuilderEvent
===================

.. vale on

Plugins register a custom Point trigger on ``Mautic\PointBundle\Event\TriggerBuilderEvent``. ``addEvent()`` types ``$key`` as ``string``:

.. code:: diff

   - public function addEvent($key, array $event): void
   + public function addEvent(string $key, array $event): void

Mautic 8 also dispatches ``TriggerBuilderEvent`` by its class name. Re-key your subscriber from ``PointEvents::TRIGGER_ON_BUILD`` to ``TriggerBuilderEvent::class``, because a subscriber keyed on the constant or the ``mautic.trigger_on_build`` string silently receives nothing.

.. vale off

For a Point extension example, see :doc:`/plugin_extensions/points`.

.. _mautic 8 reportbundle:

ReportBundle
************

.. vale on

Mautic 8 dispatches these ReportBundle events by their event class. The ``Mautic\ReportBundle\ReportEvents`` constants still exist, but Mautic doesn't dispatch the events under them, so a subscriber keyed on one silently receives nothing. Key ``getSubscribedEvents()`` on the event class in the ``Mautic\ReportBundle\Event`` namespace instead:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - ``ReportEvents`` constant
     - Event class
   * - ``REPORT_ON_BUILD``
     - ``ReportBuilderEvent``
   * - ``REPORT_ON_GENERATE``
     - ``ReportGeneratorEvent``
   * - ``REPORT_ON_GRAPH_GENERATE``
     - ``ReportGraphEvent``
   * - ``REPORT_QUERY_PRE_EXECUTE``
     - ``ReportQueryEvent``
   * - ``REPORT_ON_DISPLAY``
     - ``ReportDataEvent``
   * - ``REPORT_SCHEDULE_SEND``
     - ``ReportScheduleSendEvent``
   * - ``REPORT_ON_COLUMN_COLLECT``
     - ``ColumnCollectEvent``
   * - ``REPORT_PERMANENT_FILE_CREATED``
     - ``PermanentReportFileCreatedEvent``

The ``REPORT_PRE_SAVE``, ``REPORT_POST_SAVE``, ``REPORT_PRE_DELETE``, and ``REPORT_POST_DELETE`` constants share one ``ReportEvent`` object, so they don't change.

.. vale off

For a Report extension example, see :doc:`/plugin_extensions/reports`.

.. _mautic 8 smsbundle:

SmsBundle
*********

.. vale on

Mautic 8 adds parameter types to the SMS and SMS Stat entities. Plugins that create or update these entities must pass arguments of the declared types:

* ``Mautic\SmsBundle\Entity\Sms`` - ``setName()`` takes ``?string``, and ``setSmsType()`` takes ``string``.
* ``Mautic\SmsBundle\Entity\Stat`` - ``setTrackingHash()`` takes ``string``, ``setIsFailed()`` takes ``bool``, and ``setDateSent()`` now requires a ``\DateTimeInterface``, so passing a date string now raises a ``TypeError`` at runtime.

.. code:: diff

   - public function setDateSent($dateSent): static
   + public function setDateSent(\DateTimeInterface $dateSent): static

.. vale off

SmsEvents constants
===================

.. vale on

Mautic 8 removes these ``Mautic\SmsBundle\SmsEvents`` constants and dispatches the events by their event class. A subscriber that still references one of them fails with ``Error: Undefined constant``. Key ``getSubscribedEvents()`` on the event class in the ``Mautic\SmsBundle\Event`` namespace instead:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Removed ``SmsEvents`` constant
     - Event class
   * - ``SMS_PRE_SAVE``
     - ``SmsPreSaveEvent``
   * - ``SMS_POST_SAVE``
     - ``SmsPostSaveEvent``
   * - ``SMS_PRE_DELETE``
     - ``SmsPreDeleteEvent``
   * - ``SMS_POST_DELETE``
     - ``SmsPostDeleteEvent``
   * - ``ON_REPLY``
     - ``ReplyEvent``
   * - ``DNC_FILTER_CONTACTS_ON_SEND``
     - ``DncEvent``
   * - ``QUEUE_FILTER_CONTACTS_ON_SEND``
     - ``QueueEvent``
   * - ``FILTER_CONTACTS_ON_SEND``
     - ``FilterEvent``
   * - ``ON_SMS_TOKENS_BUILD``
     - ``TokensBuildEvent``

The four save and delete events used to share one ``SmsEvent`` object. ``SmsEvent`` is now abstract, so a listener method can keep its ``SmsEvent`` type hint, but code that creates an ``SmsEvent`` with ``new``, such as a Plugin test, must create the matching subclass.

Mautic 8 also removes the deprecated ``ON_CAMPAIGN_TRIGGER_ACTION`` constant. Mautic runs the SMS Campaign action through ``ON_CAMPAIGN_TRIGGER_BATCH_ACTION``, so listen to that event instead. Mautic keeps the ``SMS_ON_SEND`` constant as the Webhook event type identifier for sent SMS messages, but it doesn't dispatch the send event under it, so key the subscriber on ``SmsSendEvent::class``. ``TOKEN_REPLACEMENT``, ``ON_CAMPAIGN_TRIGGER_BATCH_ACTION``, and ``ON_CAMPAIGN_REPLY`` don't change.

To confirm that Mautic registers a re-keyed filter subscriber, see :ref:`Check event subscriptions <mautic 8 check event subscriptions>`.

.. vale off

For an SMS transport example, see :doc:`/plugin_extensions/sms`.

.. _mautic 8 stagebundle:

StageBundle
***********

.. vale on

Mautic 8 dispatches ``Mautic\StageBundle\Event\StageBuilderEvent`` by its class. The ``StageEvents::STAGE_ON_BUILD`` constant still exists, but Mautic doesn't dispatch the event under it, so key ``getSubscribedEvents()`` on ``StageBuilderEvent::class``. Mautic still dispatches the ``STAGE_*`` save and delete group, ``STAGE_ON_ACTION``, and ``ON_CAMPAIGN_BATCH_ACTION`` under their string constants, so subscribers keyed on them don't change.

Mautic 8 also adds parameter types to the Stage and Contact Stage log entities.

``Mautic\StageBundle\Entity\Stage`` types ``setDescription()`` as ``?string`` and ``setCategory()`` as a Category entity or ``null``:

.. code:: diff

   - public function setCategory($category): void
   + public function setCategory(?\Mautic\CategoryBundle\Entity\Category $category): void

``Mautic\StageBundle\Entity\LeadStageLog`` adds entity and date types to its setters, so passing an ID or a date string instead of the object now raises a ``TypeError`` at runtime:

.. code:: diff

   - public function setLead($lead): void
   + public function setLead(\Mautic\LeadBundle\Entity\Lead $lead): void

.. code:: diff

   - public function setStage($stage): void
   + public function setStage(\Mautic\StageBundle\Entity\Stage $stage): void

.. code:: diff

   - public function setDateFired($dateFired): void
   + public function setDateFired(\DateTimeInterface $dateFired): void

.. code:: diff

   - public function setIpAddress($ipAddress): void
   + public function setIpAddress(\Mautic\CoreBundle\Entity\IpAddress $ipAddress): void

.. _mautic 8 statsbundle:

.. vale off

StatsBundle
***********

.. vale on

Mautic 8 deletes the ``Mautic\StatsBundle\StatEvents`` class and dispatches ``Mautic\StatsBundle\Event\AggregateStatRequestEvent`` by its class. A subscriber that still references ``StatEvents::AGGREGATE_STAT_REQUEST`` fails with a ``Class "Mautic\StatsBundle\StatEvents" not found`` error, and a subscriber keyed on the raw ``mautic.aggregate_stat_request`` event name silently receives nothing. Key ``getSubscribedEvents()`` on ``AggregateStatRequestEvent::class`` instead.

.. _mautic 8 userbundle:

.. vale off

UserBundle
**********

.. vale on

Mautic 8 adds type declarations to one User authentication event class and deletes the ``UserEvents`` class.

.. vale off

UserEvents constants
====================

.. vale on

Mautic 8 deletes the ``Mautic\UserBundle\UserEvents`` class. A subscriber that still references one of its constants, such as ``UserEvents::USER_LOGIN``, fails with a ``Class "Mautic\UserBundle\UserEvents" not found`` error. Key ``getSubscribedEvents()`` on the event class in the ``Mautic\UserBundle\Event`` namespace instead:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Removed ``UserEvents`` constant
     - Event class
   * - ``USER_LOGIN``
     - ``LoginEvent``
   * - ``USER_LOGOUT``
     - ``LogoutEvent``
   * - ``USER_PRE_AUTHENTICATION``
     - ``PreAuthenticationEvent``
   * - ``USER_FORM_AUTHENTICATION``
     - ``FormAuthenticationEvent``
   * - ``USER_AUTHENTICATION_CONTENT``
     - ``AuthenticationContentEvent``
   * - ``USER_PASSWORD_STRENGTH_VALIDATION``
     - ``PasswordStrengthValidateEvent``
   * - ``USER_PRE_SAVE``
     - ``PreSaveUserEvent``
   * - ``USER_POST_SAVE``
     - ``PostSaveUserEvent``
   * - ``USER_PRE_DELETE``
     - ``PreDeleteUserEvent``
   * - ``USER_POST_DELETE``
     - ``PostDeleteUserEvent``
   * - ``ROLE_PRE_SAVE``
     - ``PreSaveRoleEvent``
   * - ``ROLE_POST_SAVE``
     - ``PostSaveRoleEvent``
   * - ``ROLE_PRE_DELETE``
     - ``PreDeleteRoleEvent``
   * - ``ROLE_POST_DELETE``
     - ``PostDeleteRoleEvent``

The User and Role save and delete events used to share one ``UserEvent`` or ``RoleEvent`` object, and Mautic dispatched one ``AuthenticationEvent`` under both authentication names. ``UserEvent``, ``RoleEvent``, and ``AuthenticationEvent`` are now abstract base classes for the classes in the preceding table. A listener method can keep its type hint on the base class, but code that creates one of these events with ``new``, such as a Plugin test, must create the matching subclass. Mautic also removes the ``USER_FORM_POST_LOCAL_PASSWORD_AUTHENTICATION`` constant without a replacement, because it never dispatched an event under it.

.. vale off

AuthenticationEvent
===================

.. vale on

Authentication Integrations set the User on the ``PreAuthenticationEvent`` or ``FormAuthenticationEvent`` that Mautic dispatches. Both are ``final`` subclasses of the abstract ``Mautic\UserBundle\Event\AuthenticationEvent``, which defines these methods. ``setUser()`` types ``$saveUser`` and ``$createIfNotExists`` as ``bool``, and ``setIsAuthenticated()`` types ``$createIfNotExists`` as ``bool``:

.. code:: diff

   - public function setUser(User $user, $saveUser = true, $createIfNotExists = true): void
   + public function setUser(User $user, bool $saveUser = true, bool $createIfNotExists = true): void

.. code:: diff

   - public function setIsAuthenticated(?string $service, ?User $user = null, $createIfNotExists = true): void
   + public function setIsAuthenticated(?string $service, ?User $user = null, bool $createIfNotExists = true): void

.. _mautic 8 webhookbundle:

.. vale off

WebhookBundle
*************

.. vale on

Mautic 8 adds type declarations to the Webhook Event entity and one Webhook event class, and dispatches the Webhook events by their event class.

.. vale off

WebhookEvents constants
=======================

.. vale on

Mautic 8 removes the Webhook lifecycle constants from ``Mautic\WebhookBundle\WebhookEvents``, so a subscriber that still references one of them fails with ``Error: Undefined constant``. Mautic keeps the other constants in the following table, but it doesn't dispatch events under them, so a subscriber keyed on one silently receives nothing. Key ``getSubscribedEvents()`` on the event class in the ``Mautic\WebhookBundle\Event`` namespace instead:

.. list-table::
   :header-rows: 1
   :widths: 40 20 40

   * - ``WebhookEvents`` constant
     - Status
     - Event class
   * - ``WEBHOOK_PRE_SAVE``
     - Removed
     - ``WebhookPreSaveEvent``
   * - ``WEBHOOK_POST_SAVE``
     - Removed
     - ``WebhookPostSaveEvent``
   * - ``WEBHOOK_PRE_DELETE``
     - Removed
     - ``WebhookPreDeleteEvent``
   * - ``WEBHOOK_POST_DELETE``
     - Removed
     - ``WebhookPostDeleteEvent``
   * - ``WEBHOOK_KILL``
     - Removed
     - ``WebhookKillEvent``
   * - ``WEBHOOK_ON_BUILD``
     - Kept
     - ``WebhookBuilderEvent``
   * - ``WEBHOOK_QUEUE_ON_ADD``
     - Kept
     - ``WebhookQueueEvent``
   * - ``WEBHOOK_ON_REQUEST``
     - Kept
     - ``WebhookRequestEvent``

The five lifecycle events used to share one ``WebhookEvent`` object. ``WebhookEvent`` is now an abstract base class for the five lifecycle classes, so a listener method can keep its ``WebhookEvent`` type hint, but code that creates a ``WebhookEvent`` with ``new``, such as a Plugin test, must create the matching subclass.

.. vale off

Webhook Event entity
====================

.. vale on

Webhook payload subscribers work with ``Mautic\WebhookBundle\Entity\Event``. ``setEventType()`` types ``$eventType`` as ``string``:

.. code:: diff

   - public function setEventType($eventType): static
   + public function setEventType(string $eventType): static

.. vale off

WebhookBuilderEvent
===================

.. vale on

Plugins register a Webhook event on ``Mautic\WebhookBundle\Event\WebhookBuilderEvent``. ``addEvent()`` types ``$key`` as ``string``:

.. code:: diff

   - public function addEvent($key, array $event): void
   + public function addEvent(string $key, array $event): void

.. _mautic 8 removed FormController:

.. vale off

Removed FormController
**********************

.. vale on

Mautic 8 removes ``Mautic\CoreBundle\Controller\FormController``. A Plugin controller that still extends it causes a fatal error when PHP loads the class. Change the parent class to one of these controllers:

* ``Mautic\CoreBundle\Controller\AbstractFormController`` if your controller handles Symfony ``FormInterface`` objects with helpers such as ``isFormCancelled()`` and ``isFormValid()``, but doesn't use the standard entity actions.
* ``Mautic\CoreBundle\Controller\AbstractStandardFormController`` if your controller calls the standard entity helpers, such as ``indexStandard()``, ``newStandard()``, ``editStandard()``, or ``deleteStandard()``.

.. code:: diff

   - use Mautic\CoreBundle\Controller\FormController;
   + use Mautic\CoreBundle\Controller\AbstractFormController;

   - class DefaultController extends FormController
   + class DefaultController extends AbstractFormController

``FormController`` also provided ``setStandardParameters()``, which a controller called from its constructor to set the values that the standard helpers read. That method no longer exists. If your controller called it, extend ``AbstractStandardFormController`` and return each value from the matching method instead.

.. list-table:: ``setStandardParameters()`` arguments and their replacement methods
   :widths: 40 60
   :header-rows: 1

   * - Argument
     - Method to override
   * - ``$modelName``
     - ``getModelName()`` - required, because ``AbstractStandardFormController`` declares it ``abstract``
   * - ``$permissionBase``
     - ``getPermissionBase()``
   * - ``$routeBase``
     - ``getRouteBase()``
   * - ``$sessionBase``
     - ``getSessionBase()`` - ``setStandardParameters()`` prefixed this value with ``mautic.``, so include that prefix in the returned value to keep existing session keys
   * - ``$translationBase``
     - ``getTranslationBase()``
   * - ``$templateBase``
     - ``getTemplateBase()``
   * - ``$mauticContent``
     - ``getJsLoadMethodPrefix()``

``AbstractStandardFormController`` derives defaults for most of these methods from ``getModelName()``, while ``FormController`` returned exactly the values you passed. Override every method whose default differs from the value your controller passed before. For example:

.. code:: diff

   - public function __construct(...)
   - {
   -     $this->setStandardParameters(
   -         'helloworld.world',  // model name
   -         'helloworld:worlds', // permission base
   -         'mautic_helloworld', // route base
   -         'mautic_helloworld', // session base
   -         'plugin.helloworld', // translation base
   -         '@HelloWorld/World', // template base
   -         'plugin_helloworld', // activeLink
   -         'helloWorld'         // mauticContent
   -     );
   -
   -     parent::__construct(...);
   - }
   + protected function getModelName(): string
   + {
   +     return 'helloworld.world';
   + }
   +
   + protected function getPermissionBase(): string
   + {
   +     return 'helloworld:worlds';
   + }
   +
   + protected function getRouteBase(): string
   + {
   +     return 'mautic_helloworld';
   + }
   +
   + protected function getSessionBase($objectId = null): string
   + {
   +     return 'mautic.mautic_helloworld';
   + }
   +
   + protected function getTranslationBase(): string
   + {
   +     return 'plugin.helloworld';
   + }
   +
   + protected function getTemplateBase(): string
   + {
   +     return '@HelloWorld/World';
   + }
   +
   + protected function getJsLoadMethodPrefix(): string
   + {
   +     return 'helloWorld';
   + }

Mautic's generic entity unlock route, ``mautic_core_form_action``, moves to the new ``Mautic\CoreBundle\Controller\LockController``. The route path and its ``unlockAction()`` behavior don't change, so Plugins that link to this route need no update.

.. _mautic 8 controller helper methods:

.. vale off

Controller helper methods
*************************

.. vale on

In Mautic 8, a controller exposes only its route actions as public methods. Helper methods on the base controllers are now ``protected``, and several gain native return types. Your Plugin controllers can still call these helpers through ``$this``, so a controller that only calls them needs no changes. Two kinds of Plugin code break:

* Code outside the controller that calls one of these helpers, such as a service or a test, raises an ``Error`` for calling a protected method.
* A Plugin controller that overrides one of the helpers that gained a return type, but omits the return type or declares an incompatible one, causes a fatal error when PHP loads the class.

.. vale off

CommonController
================

.. vale on

These methods on ``Mautic\CoreBundle\Controller\CommonController`` change from ``public`` to ``protected``, with no signature change otherwise:

* ``addFlashMessage()``
* ``delegateRedirect()``
* ``delegateView()``
* ``eventAwareRenderView()``
* ``exportResultsAs()``
* ``forwardWithPost()``
* ``getAccessDeniedFlash()``
* ``modalAccessDenied()``
* ``notFound()``
* ``postActionRedirect()``
* ``renderException()``
* ``throwAccessDenied()``

``Mautic\CoreBundle\Controller\AjaxLookupControllerTrait`` now declares ``renderException()`` as ``abstract protected`` to match.

.. vale off

FetchCommonApiController
========================

.. vale on

``Mautic\ApiBundle\Controller\FetchCommonApiController`` is the parent of ``CommonApiController``, which Plugin API controllers extend. Three of its methods change from ``public`` to ``protected``:

.. code:: diff

   - public function getNewEntity(array $params)
   + protected function getNewEntity(array $params)

.. code:: diff

   - public function getCurrentRequest(): Request
   + protected function getCurrentRequest(): Request

.. code:: diff

   - public function postActionRedirect(array $args = [])
   + protected function postActionRedirect(array $args = []): Response

These ``protected`` methods gain native return types:

.. code:: diff

   - protected function accessDenied(string $msg = 'mautic.core.error.accessdenied')
   + protected function accessDenied(string $msg = 'mautic.core.error.accessdenied'): Response

.. code:: diff

   - protected function badRequest(string $msg = 'mautic.core.error.badrequest')
   + protected function badRequest(string $msg = 'mautic.core.error.badrequest'): Response

.. code:: diff

   - protected function checkEntityAccess($entity, $action = 'view')
   + protected function checkEntityAccess($entity, $action = 'view'): bool|Response

.. code:: diff

   - protected function notFound(string $msg = 'mautic.core.error.notfound')
   + protected function notFound(string $msg = 'mautic.core.error.notfound'): Response

.. code:: diff

   - protected function returnError(string $msg, int $code = Response::HTTP_INTERNAL_SERVER_ERROR, array $details = [])
   + protected function returnError(string $msg, int $code = Response::HTTP_INTERNAL_SERVER_ERROR, array $details = []): Response|array

.. code:: diff

   - protected function validateBatchPayload(array $parameters)
   + protected function validateBatchPayload(array $parameters): \Symfony\Component\HttpFoundation\Response|array|true

``validateBatchPayload()`` declares ``true`` where its annotation previously documented ``bool``, so an override can't return ``false``.

.. vale off

FormController
==============

.. vale on

``clearSessionComponents()`` on ``Mautic\FormBundle\Controller\FormController`` changes from ``public`` to ``protected``.

.. vale off

Bundle controllers
==================

.. vale on

Helper methods that only their own class used are now ``private``. Examples include ``getMapOptions()`` on the Campaign and Email map stats controllers and ``getUnsubscribeMessage()`` on ``Mautic\EmailBundle\Controller\PublicController``. A Plugin controller that extends one of these bundle controllers can no longer call or override these methods.

.. vale off

Update your Plugin
==================

.. vale on

To update your Plugin:

#. Move any logic that calls a controller helper from outside the controller into the controller itself, or into a service that both the controller and the calling code use.
#. In each Plugin controller that overrides one of these helpers, copy the parent's return type into the override. An override can keep ``public`` visibility, because PHP lets a child class widen visibility.

.. vale off

Return types in Campaign, Email, Point, Notification, Dynamic Content, and SMS bundles
**************************************************************************************

.. vale on

Mautic 8 replaces ``@return array`` annotations with native return types on methods in the CampaignBundle, EmailBundle, PointBundle, NotificationBundle, DynamicContentBundle, and SmsBundle. The methods already returned these types, so code that only calls them needs no change.

The break affects Plugins that implement one of these interfaces or extend one of these classes. If your class overrides a listed method without a compatible return type, PHP raises a fatal error when it loads your class, because the override's declaration isn't compatible with the parent method.

.. note::

   PHP lets a child method declare a return type that its parent leaves out. Add the return type to your overrides now, and the same code runs on both Mautic 7 and Mautic 8.

.. vale off

Interfaces and abstract base classes
====================================

.. vale on

Every class that implements or extends one of these must declare the ``array`` return type on the listed methods:

.. code:: diff

   // Mautic\EmailBundle\Entity\EmailReplyRepositoryInterface
   - public function getByLeadIdForTimeline($leadId, $options);
   + public function getByLeadIdForTimeline($leadId, $options): array;

   // Mautic\CampaignBundle\Event\AbstractLogCollectionEvent
   - public function getContactIds()
   + public function getContactIds(): array

   // Mautic\CampaignBundle\EventCollector\Accessor\Event\AbstractEventAccessor
   - public function getFormTypeOptions()
   + public function getFormTypeOptions(): array
   - public function getConnectionRestrictions()
   + public function getConnectionRestrictions(): array
   - public function getExtraProperties()
   + public function getExtraProperties(): array

   // Mautic\EmailBundle\Stats\Helper\AbstractHelper
   - public function fetchStats(\DateTime $fromDateTime, \DateTime $toDateTime, EmailStatOptions $options)
   + public function fetchStats(\DateTime $fromDateTime, \DateTime $toDateTime, EmailStatOptions $options): array

.. vale off

Event classes
=============

.. vale on

If your Plugin extends ``Mautic\EmailBundle\Event\EmailSendEvent`` or the deprecated ``Mautic\CampaignBundle\Event\CampaignExecutionEvent``, add the return type to any of these overrides:

.. code:: diff

   // Mautic\EmailBundle\Event\EmailSendEvent
   - public function getSource()
   + public function getSource(): array

   // Mautic\CampaignBundle\Event\CampaignExecutionEvent
   - public function getLeadFields()
   + public function getLeadFields(): array
   - public function getEvent()
   + public function getEvent(): array
   - protected function getEventArray(CampaignEvent $event)
   + protected function getEventArray(CampaignEvent $event): array
   - public function getConfig()
   + public function getConfig(): array

``CampaignBuilderEvent::getActions()``, ``getConditions()``, and ``getDecisions()``, and ``ScheduledEvent::getEvent()`` and ``getConfig()`` also gain ``: array``. Both classes are ``final``, so the override risk doesn't apply.

.. vale off

Entities
========

.. vale on

If your Plugin extends one of these entities, add the return type to any override of the listed methods. The return type is ``array`` unless noted:

* ``Mautic\CampaignBundle\Entity\Event::getProperties()``
* ``Mautic\CampaignBundle\Entity\LeadEventLog::getMetadata()``
* ``Mautic\EmailBundle\Entity\Email::getContent()``, which returns ``array|string``, plus ``getUtmTags()`` and ``getHeaders()``
* ``Mautic\EmailBundle\Entity\Stat::getOpenDetails()``
* ``Mautic\NotificationBundle\Entity\Notification::getUtmTags()`` and ``getMobileSettings()``
* ``Mautic\NotificationBundle\Entity\Stat::getTokens()`` and ``getClickDetails()``
* ``Mautic\DynamicContentBundle\Entity\Stat::getSentDetails()`` and ``getTokens()``
* ``Mautic\SmsBundle\Entity\Stat::getTokens()`` and ``getDetails()``
* ``Mautic\PointBundle\Entity\Point::getProperties()`` and ``Mautic\PointBundle\Entity\TriggerEvent::getProperties()``
* ``Mautic\PointBundle\Entity\PointInsight::getPointGroups()``

Run :xref:`phpstan` against your Plugin on Mautic 8 to find any override whose return type no longer matches its parent.

.. vale off

Nullable getter methods and Integration changes
***********************************************

.. vale on

Some Mautic 7 getter methods, whose names start with ``get``, declared a return type that excludes ``null`` while returning a property that can hold ``null``. Calling one of them before Mautic set the property raised a ``TypeError``. Mautic 8 corrects these methods, and the correction also changes three Integration classes and methods that Plugins call directly.

.. vale off

Integration response event
==========================

.. vale on

Mautic now dispatches the Integration response as a new ``Mautic\PluginBundle\Event\PluginIntegrationResponseEvent`` instead of ``PluginIntegrationRequestEvent``. ``AbstractIntegration::makeRequest()`` creates the new event with the Integration and the response, so ``getResponse()`` always returns a ``Psr\Http\Message\ResponseInterface``. ``PluginIntegrationRequestEvent`` no longer has ``getResponse()`` or ``setResponse()``.

Mautic 8 also removes the ``PluginEvents::PLUGIN_ON_INTEGRATION_REQUEST`` and ``PLUGIN_ON_INTEGRATION_RESPONSE`` constants and dispatches both events by the event object alone. Key ``getSubscribedEvents()`` on ``PluginIntegrationRequestEvent::class`` and ``PluginIntegrationResponseEvent::class``. For the other removed ``PluginEvents`` constants, see :ref:`PluginBundle <mautic 8 pluginbundle>`.

A listener that still type-hints ``PluginIntegrationRequestEvent`` raises a ``TypeError`` when Mautic dispatches the event. Change the type hint:

.. code:: diff

   - public function onResponse(PluginIntegrationRequestEvent $event): void
   + public function onResponse(PluginIntegrationResponseEvent $event): void
     {
         $response = $event->getResponse();

The new event extends ``AbstractPluginIntegrationEvent``, so ``getIntegration()`` and ``getIntegrationName()`` still work. Listeners on the request event still receive ``PluginIntegrationRequestEvent``, but can no longer read the response from it.

.. vale off

MappingManualDAO
================

.. vale on

The mapping manual, described in :doc:`/plugin_integrations/integrations_sync`, now takes its object mappings in the constructor. ``Mautic\IntegrationsBundle\Sync\DAO\Mapping\MappingManualDAO`` requires an array of ``ObjectMappingDAO`` objects as its second argument, and ``addObjectMapping()`` is now ``private``:

.. code:: diff

   - public function __construct(private readonly string $integration)
   + public function __construct(private readonly string $integration, array $objectsMapping)

   - public function addObjectMapping(ObjectMappingDAO $objectMappingDAO): void
   + private function addObjectMapping(ObjectMappingDAO $objectMappingDAO): void

Build each ``ObjectMappingDAO`` first, then pass them all to the constructor. You can still add field mappings to each ``ObjectMappingDAO`` after you create the manual:

.. code:: diff

   - $mappingManual = new MappingManualDAO(self::NAME);
     $leadObjectMapping = new ObjectMappingDAO(Contact::NAME, 'lead');
   - $mappingManual->addObjectMapping($leadObjectMapping);
   + $mappingManual = new MappingManualDAO(self::NAME, [$leadObjectMapping]);

.. vale off

getIntegrationConfiguration()
=============================

.. vale on

``getIntegrationConfiguration()`` from ``Mautic\IntegrationsBundle\Integration\ConfigurationTrait`` keeps its ``Integration`` return type. When Mautic hasn't set the configuration, the method now throws a ``\LogicException`` instead of a ``TypeError``. If your Integration code can run before Mautic sets the configuration, call ``hasIntegrationConfiguration()`` first:

.. code-block:: php

   if ($integration->hasIntegrationConfiguration()) {
       $apiKeys = $integration->getIntegrationConfiguration()->getApiKeys();
   }

.. vale off

Getter methods that can return null
===================================

.. vale on

These getter methods now declare a return type that accepts ``null``. When the value is ``null``, Mautic 7 raised a ``TypeError`` and Mautic 8 returns ``null``. If your Plugin passes a result to a parameter that doesn't accept ``null``, handle the ``null`` case first:

.. code:: diff

   - public function getViewName(): string
   + public function getViewName(): ?string                          // CustomContentEvent

   - public function getContent(): string|array
   + public function getContent(): string|array|null                 // TokenReplacementEvent

   - public function getPostSubmitPayload(): array
   + public function getPostSubmitPayload(): ?array                  // SubmissionEvent

   - public function getChangeDateTime(): \DateTimeInterface
   + public function getChangeDateTime(): ?\DateTimeInterface        // ObjectChangeDAO

   - public function getObjectMapping(): ObjectMapping
   + public function getObjectMapping(): ?ObjectMapping              // ObjectChangeDAO

``CustomContentEvent`` and ``TokenReplacementEvent`` are in ``Mautic\CoreBundle\Event``, ``SubmissionEvent`` is in ``Mautic\FormBundle\Event``, and ``ObjectChangeDAO`` is in ``Mautic\IntegrationsBundle\Sync\DAO\Sync\Order``. ``ObjectChangeDAO::getObjectMapping()`` returns ``null`` until the sync engine persists the object mapping.

The same change applies to these entity and DTO getter methods:

* ``Mautic\ApiBundle\Entity\oAuth2\Client::getRole()`` returns ``?Role``.
* ``Mautic\EmailBundle\Entity\EmailDraft::getHtml()`` and ``getTemplate()`` return ``?string``, and ``getPublishStatus()`` returns ``?bool``.
* ``Mautic\PageBundle\Entity\Page::getCloneObjectId()`` returns ``?int``, and ``getPublicPreview()`` returns ``?bool``.
* ``Mautic\CampaignBundle\DTO\PublishState::getPublished()`` returns ``?bool``.

An override that keeps the old non-nullable return type is still compatible, because PHP allows a child method to narrow its return type.

.. _mautic 8 core return types:

.. vale off

Return types on Core base classes and interfaces
************************************************

.. vale on

Mautic 8 replaces ``@return array`` annotations with native return types on Core base classes and interfaces that Plugins implement or extend. The methods already returned these types, so code that only calls them needs no change.

The break affects Plugins that implement one of these interfaces or extend one of these base classes. If your class overrides a listed method without the same return type, PHP raises a fatal error when it loads your class.

.. note::

   PHP lets a child method declare a return type that its parent leaves out. Add the return type to your overrides now, and the same code runs on both Mautic 7 and Mautic 8.

.. vale off

Interfaces
==========

.. vale on

Every class that implements one of these interfaces must declare the ``array`` return type:

.. code:: diff

   // Mautic\CoreBundle\Configurator\Step\StepInterface
   - public function checkRequirements();
   + public function checkRequirements(): array;
   - public function checkOptionalSettings();
   + public function checkOptionalSettings(): array;
   - public function update(self $data);
   + public function update(self $data): array;

   // Mautic\CoreBundle\Helper\ThemeHelperInterface
   - public function getDefaultThemes();
   + public function getDefaultThemes(): array;
   - public function getOptionalSettings();
   + public function getOptionalSettings(): array;
   - public function getInstalledThemes($specificFeature = 'all', bool $extended = false, bool $ignoreCache = false, bool $includeDirs = true);
   + public function getInstalledThemes($specificFeature = 'all', bool $extended = false, bool $ignoreCache = false, bool $includeDirs = true): array;

   // Mautic\CoreBundle\IpLookup\IpLookupFormInterface
   - public function getConfigFormThemes();
   + public function getConfigFormThemes(): array;

   // Mautic\CoreBundle\Model\SearchCommandListInterface
   - public function getCommandList();
   + public function getCommandList(): array;

   // Mautic\StatsBundle\Aggregate\Collection\Stats\StatInterface
   - public function getStats();
   + public function getStats(): array;

.. vale off

AbstractPermissions
===================

.. vale on

Every Plugin permissions class extends ``Mautic\CoreBundle\Security\Permissions\AbstractPermissions``. If yours defines permission aliases in ``getSynonym()``, or overrides one of the other listed methods, add the return type:

.. code:: diff

   - public function getPermissions()
   + public function getPermissions(): array
   - protected function getSynonym($name, $level)
   + protected function getSynonym($name, $level): array
   - public function getPermissionRatio(array $data)
   + public function getPermissionRatio(array $data): array

.. vale off

For a ``getSynonym()`` example, see :doc:`/plugins/permissions`.

.. vale on

.. vale off

Models and entities
===================

.. vale on

Plugin models that extend ``Mautic\CoreBundle\Model\AbstractCommonModel`` must match these return types. ``getEntities()`` declares ``iterable`` rather than ``array``, because it can return a Doctrine ``Paginator``:

.. code:: diff

   - public function getEntities(array $args = [])
   + public function getEntities(array $args = []): iterable
   - public function getSupportedSearchCommands()
   + public function getSupportedSearchCommands(): array
   - public function getCommandList()
   + public function getCommandList(): array

Plugin entities that extend ``Mautic\CoreBundle\Entity\CommonEntity`` and override ``getChanges()`` must declare ``: array``:

.. code:: diff

   - public function getChanges(bool $includePast = false)
   + public function getChanges(bool $includePast = false): array

.. _mautic 8 formmodel parameter types:

.. vale off

FormModel parameter types
=========================

.. vale on

Mautic 8 also adds native parameter types to these public methods on ``Mautic\CoreBundle\Model\FormModel``, and adds ``: bool`` to ``isNewEntity()``:

.. code:: diff

   - public function saveEntity($entity, $unlock = true): void
   + public function saveEntity(object $entity, bool $unlock = true): void
   - public function saveAndDetachEntity($entity, $unlock = true): void
   + public function saveAndDetachEntity(object $entity, bool $unlock = true): void
   - public function lockEntity($entity): void
   + public function lockEntity(object $entity): void
   - public function isLocked($entity): bool
   + public function isLocked(object $entity): bool
   - public function isNewEntity($entity)
   + public function isNewEntity(object $entity): bool
   - public function togglePublishStatus($entity): bool
   + public function togglePublishStatus(object $entity): bool
   - public function deleteEntity($entity): void
   + public function deleteEntity(object $entity): void
   - public function deleteEntities($ids): array
   + public function deleteEntities(array $ids): array

``AbstractCommonModel::encodeArrayForUrl()``, which ``FormModel`` and Plugin models inherit, also types its parameter, as ``encodeArrayForUrl(array $array)``.

Code that only calls these methods needs no change, because they already worked with entity objects and arrays. An override that declares a narrower or different parameter type, such as a concrete entity class instead of ``object``, causes a fatal error when PHP loads your class. An override that declares no parameter type stays compatible. To fix an incompatible override, use ``object $entity`` or ``array $ids``, or remove the parameter type.

Mautic's own ``saveEntity()`` overrides, such as the ones on ``EmailModel`` and ``LeadModel``, also declare ``object $entity``, so the same rule applies if your model extends one of them. ``AssetModel``, ``PageModel``, and ``UserModel`` are ``final``, so a Plugin can't extend them. See :ref:`Final classes <Mautic 8 final classes>`.

.. vale off

Controllers
===========

.. vale on

Plugin controllers that extend these Mautic controller classes must declare ``: array`` on these overrides:

.. code:: diff

   // Mautic\CoreBundle\Controller\AbstractFormController
   - protected function refererPostActionVars(array $vars)
   + protected function refererPostActionVars(array $vars): array

   // Mautic\CoreBundle\Controller\AbstractStandardFormController
   - protected function afterEntityClone($newEntity, $entity)
   + protected function afterEntityClone($newEntity, $entity): array
   - protected function getEntityFormOptions()
   + protected function getEntityFormOptions(): array
   - protected function getIndexItems($start, $limit, $filter, $orderBy, $orderByDir, array $args = [])
   + protected function getIndexItems($start, $limit, $filter, $orderBy, $orderByDir, array $args = []): array
   - protected function getUpdateSelectParams($updateSelect, $entity, $nameMethod = 'getName', $groupMethod = 'getLanguage')
   + protected function getUpdateSelectParams($updateSelect, $entity, $nameMethod = 'getName', $groupMethod = 'getLanguage'): array
   - protected function getViewDateRange(Request $request, $objectId, $returnUrl, $timezone = 'local', &$dateRangeForm = null)
   + protected function getViewDateRange(Request $request, $objectId, $returnUrl, $timezone = 'local', &$dateRangeForm = null): array

   // Mautic\ApiBundle\Controller\FetchCommonApiController
   - protected function getWhereFromRequest(Request $request)
   + protected function getWhereFromRequest(Request $request): array

.. vale off

Other base classes
==================

.. vale on

These base classes also gain ``: array`` return types on the listed methods:

* ``Mautic\CoreBundle\Doctrine\AbstractMauticMigration::generateKeys()``
* ``Mautic\CoreBundle\IpLookup\AbstractLookup::getDetails()``, ``AbstractLocalDataLookup::getConfigFormThemes()``, and ``getHeaders()`` on ``AbstractMaxmindLookup`` and ``AbstractRemoteDataLookup``, plus ``AbstractRemoteDataLookup::getParameters()``
* ``Mautic\CoreBundle\Event\BuilderEvent::getTokens()`` and ``filterTokens()``
* ``Mautic\CoreBundle\Event\TokenReplacementEvent::getTokens()``
* ``MauticPlugin\MauticCrmBundle\Integration\CrmAbstractIntegration::getSyncTimeframeDates()``

``Mautic\PluginBundle\Integration\AbstractIntegration::mergeApiKeys()`` gains a ``: ?array`` return type, because it returns ``null`` unless you pass ``true`` as its ``$return`` argument. An override can declare ``: ?array``, or ``: array`` if it always returns an array.

Run :xref:`phpstan` against your Plugin on Mautic 8 to find any override whose return type no longer matches its parent.

.. vale off

Return types on Plugin Integration base classes
***********************************************

.. vale on

Mautic 8 replaces ``@return array`` annotations with native ``array`` return types on the base classes for Integrations built with the Plugin framework: ``Mautic\PluginBundle\Integration\AbstractIntegration``, ``MauticPlugin\MauticCrmBundle\Integration\CrmAbstractIntegration``, and ``MauticPlugin\MauticSocialBundle\Integration\SocialIntegration``. The methods already returned arrays, so code that only calls them needs no change.

The break affects Plugins whose Integration class extends one of these base classes and overrides a listed method. If the override doesn't declare the ``array`` return type, PHP raises a fatal error when it loads your class:

.. code-block:: text

   Declaration of MauticPlugin\HelloWorldBundle\Integration\HelloWorldIntegration::getRequiredKeyFields() must be compatible with Mautic\PluginBundle\Integration\AbstractIntegration::getRequiredKeyFields(): array

Add ``: array`` to each override, and make sure every code path in it returns an array. An override that still returns ``null`` or another type raises a ``TypeError`` when Mautic calls it.

.. note::

   PHP lets a child method declare a return type that its parent leaves out. Add the return type to your overrides now, and the same code runs on both Mautic 7 and Mautic 8.

.. vale off

This change doesn't affect Integrations that extend ``Mautic\IntegrationsBundle\Integration\BasicIntegration``, the base class that :doc:`/plugin_integrations/integrations` describes, because ``BasicIntegration`` doesn't inherit from these classes.

AbstractIntegration
===================

.. vale on

Integrations built with the Plugin framework commonly override the methods that describe the Integration's API keys and configuration Form, such as ``getRequiredKeyFields()``, ``getSecretKeys()``, ``getFormNotes()``, and ``getFormLeadFields()``. These methods on ``Mautic\PluginBundle\Integration\AbstractIntegration`` now declare ``: array``:

.. code:: diff

   - public function encryptApiKeys(array $keys)
   + public function encryptApiKeys(array $keys): array
   - public function decryptApiKeys(array $keys, bool $mainDecryptOnly = false)
   + public function decryptApiKeys(array $keys, bool $mainDecryptOnly = false): array
   - public function getSecretKeys()
   + public function getSecretKeys(): array
   - public function getRefreshTokenKeys()
   + public function getRefreshTokenKeys(): array
   - public function getRequiredKeyFields()
   + public function getRequiredKeyFields(): array
   - public function prepareRequest(string $url, $parameters, string $method, array $settings, $authType)
   + public function prepareRequest(string $url, $parameters, string $method, array $settings, $authType): array
   - public function cleanUpFields(Integration $entity, array $mauticLeadFields, array $mauticCompanyFields)
   + public function cleanUpFields(Integration $entity, array $mauticLeadFields, array $mauticCompanyFields): array
   - public function getRequiredFields(array $fields, $fieldType = '')
   + public function getRequiredFields(array $fields, $fieldType = ''): array
   - public function populateLeadData($lead, $config = [])
   + public function populateLeadData($lead, $config = []): array
   - public function populateCompanyData($entity, $config = [])
   + public function populateCompanyData($entity, $config = []): array
   - public function populateMauticLeadData($data, $config = [], $object = null)
   + public function populateMauticLeadData($data, $config = [], $object = null): array
   - protected function matchUpData($data)
   + protected function matchUpData($data): array
   - public function getFormNotes($section)
   + public function getFormNotes($section): array
   - public function getFormDisplaySettings()
   + public function getFormDisplaySettings(): array
   - public function getFormLeadFields(array $settings = [])
   + public function getFormLeadFields(array $settings = []): array
   - public function getFormCompanyFields(array $settings = [])
   + public function getFormCompanyFields(array $settings = []): array
   - protected function dispatchIntegrationKeyEvent(?string $eventName, array $keys = [])
   + protected function dispatchIntegrationKeyEvent(?string $eventName, array $keys = []): array
   - public function formatMatchedFields(array $fields)
   + public function formatMatchedFields(array $fields): array

.. vale off

CrmAbstractIntegration
======================

.. vale on

CRM Integrations that extend ``MauticPlugin\MauticCrmBundle\Integration\CrmAbstractIntegration`` inherit the ``AbstractIntegration`` changes in the preceding section. These field-mapping and sync methods on ``CrmAbstractIntegration`` also declare ``: array``:

.. code:: diff

   - protected function getFormFieldsByObject($object, array $settings = [])
   + protected function getFormFieldsByObject($object, array $settings = []): array
   - protected function getPriorityFieldsForMautic(array $config, $entityObject = null, $priorityObject = 'mautic')
   + protected function getPriorityFieldsForMautic(array $config, $entityObject = null, $priorityObject = 'mautic'): array
   - protected function getPriorityFieldsForIntegration(array $config, $entityObject = null, $priorityObject = 'mautic')
   + protected function getPriorityFieldsForIntegration(array $config, $entityObject = null, $priorityObject = 'mautic'): array
   - protected function getFieldsByPriority(array $config, $priorityObject, $direction)
   + protected function getFieldsByPriority(array $config, $priorityObject, $direction): array
   - protected function cleanPriorityFields(array $fieldsToUpdate, $objects = null)
   + protected function cleanPriorityFields(array $fieldsToUpdate, $objects = null): array
   - protected function prepareFieldsForPush($fields)
   + protected function prepareFieldsForPush($fields): array

.. vale off

SocialIntegration
=================

.. vale on

``MauticPlugin\MauticSocialBundle\Integration\SocialIntegration`` overrides four ``AbstractIntegration`` methods, and its overrides now declare the same ``: array`` return type: ``getFormLeadFields()``, ``getFormCompanyFields()``, ``getRequiredKeyFields()``, and ``getFormNotes()``. If your Integration extends ``SocialIntegration`` and overrides one of these methods, add ``: array`` to the override.

Run :xref:`phpstan` against your Plugin on Mautic 8 to find any override whose return type no longer matches the return type of the parent method.

.. _mautic 8 services and helpers:

.. vale off

Services and helpers
********************

.. vale on

Mautic 8 also changes a handful of services and helpers that a Plugin might call directly.

.. _mautic 8 config php services array:

.. vale off

Config/config.php services array
================================

.. vale on

Mautic 8 no longer reads the ``services`` array from a bundle's ``Config/config.php`` at all. ``Mautic\CoreBundle\DependencyInjection\Builder\Metadata\ConfigMetadata`` dropped the code that parsed it, so Mautic silently ignores anything your Plugin still declares under ``services`` - including the ``events``, ``forms``, ``helpers``, ``menus``, ``models``, ``permissions``, ``integrations``, and ``controllers`` sub-keys. Register each of these as a Symfony service in your Plugin's ``Config/services.php`` instead. See :ref:`Plugins/config:config file` for the current service-registration reference.

The deprecated ``models`` sub-key is also gone, together with the compiler pass that read it. Instead, implement ``Mautic\CoreBundle\Model\MauticModelInterface`` and register the class in ``Config/services.php``. Mautic's autoconfiguration tags every service that implements this interface, so ``ModelFactory`` finds the model with no further configuration:

.. code:: diff

   -'services' => [
   -    'models' => [
   -        'yourbundle.yourmodel' => [
   -            'class' => \MauticPlugin\YourBundle\Model\YourModel::class,
   -        ],
   -    ],
   -],
   +$services->set(\MauticPlugin\YourBundle\Model\YourModel::class);

For permissions classes, see :ref:`AbstractPermissions <mautic 8 abstractpermissions>`.

.. _mautic 8 custom model lookup:

.. vale off

Custom model lookup
===================

.. vale on

``Mautic\CoreBundle\Factory\ModelFactory`` now collects every service that implements ``MauticModelInterface`` and resolves ``getModel()`` lookup keys through each model's static ``getName()`` method, instead of the removed ``Mautic\CoreBundle\DependencyInjection\Compiler\ModelPass``. Add ``getName()`` to a custom model if it doesn't already have one:

.. code-block:: php

   public static function getName(): string
   {
       return 'yourbundle.yourmodel';
   }

A model without ``getName()`` is still registered in the locator, but only under its fully qualified class name, so ``$modelFactory->getModel('yourbundle.yourmodel')`` fails until you add the method. ``ModelFactory::getModel()`` no longer accepts a fully qualified class name as the lookup key. Mautic 8 also removes the ``mautic.<bundle>.model.<name>`` service aliases, as :ref:`Service IDs <mautic 8 removed service ids>` describes.

.. _mautic 8 removed service ids:

.. vale off

Service IDs
===========

.. vale on

Mautic 8 registers many core services only under their class name and removes the string service IDs that pointed at them. Autowired and type-hinted services don't change. If your Plugin fetches one of these services from the container by its old ID, or passes the ID to ``service()`` in ``Config/services.php``, use the class name instead:

.. vale off

.. list-table::
   :header-rows: 1
   :widths: 45 55

   * - Removed service ID
     - Service ID to use
   * - ``mautic.security``
     - ``Mautic\CoreBundle\Security\Permissions\CorePermissions``
   * - ``mautic.helper.core_parameters`` and ``mautic.config``
     - ``Mautic\CoreBundle\Helper\CoreParametersHelper``
   * - ``mautic.helper.integration``
     - ``Mautic\PluginBundle\Helper\IntegrationHelper``
   * - ``mautic.integrations.helper``
     - ``Mautic\IntegrationsBundle\Helper\IntegrationsHelper``
   * - ``mautic.menu.builder``
     - ``Mautic\CoreBundle\Menu\MenuBuilder``
   * - ``mautic.cache.provider``
     - ``Mautic\CacheBundle\Cache\CacheProvider``, or inject ``Mautic\CacheBundle\Cache\CacheProviderInterface``
   * - ``mautic.cache.provider_tag_aware``
     - ``Mautic\CacheBundle\Cache\CacheProviderTagAware``
   * - ``mautic.cache.adapter.filesystem``
     - ``Mautic\CacheBundle\Cache\Adapter\FilesystemTagAwareAdapter``
   * - ``mautic.cache.adapter.memcached``
     - ``Mautic\CacheBundle\Cache\Adapter\MemcachedTagAwareAdapter``
   * - ``mautic.cache.adapter.redis``
     - ``Mautic\CacheBundle\Cache\Adapter\RedisAdapter``
   * - ``mautic.cache.adapter.redis_tag_aware``
     - ``Mautic\CacheBundle\Cache\Adapter\RedisTagAwareAdapter``
   * - ``mautic.<bundle>.model.<name>``, for example ``mautic.lead.model.lead``
     - The model class, or ``ModelFactory::getModel()`` with the model's ``getName()`` key

.. vale on

For example, replace a container lookup by a removed ID:

.. code:: diff

   -$security  = $container->get('mautic.security');
   +$security  = $container->get(\Mautic\CoreBundle\Security\Permissions\CorePermissions::class);

   -$leadModel = $container->get('mautic.lead.model.lead');
   +$leadModel = $modelFactory->getModel('lead.lead');

The ``cache_adapter`` and ``cache_adapter_tag_aware`` configuration parameters also take the adapter's class name as the service ID, so update a ``config/local.php`` that names an adapter by its old ID. :xref:`UPGRADE_GUIDE_8` lists further removed service IDs that Plugins rarely use.

.. _mautic 8 menu registration:

.. vale off

Menu registration
=================

.. vale on

Mautic 8 removes ``Mautic\CoreBundle\DependencyInjection\Compiler\ServicePass``, which used to read a bundle's ``services > menus`` array from ``Config/config.php`` and wire the menu item and its renderer automatically. If your Plugin registers its own menu, declare both services explicitly in ``Config/services.php`` instead. Mautic 8 also removes the ``mautic.menu.builder`` service alias, so reference the menu builder by its class through ``service(MenuBuilder::class)``, as this example does. See :ref:`Plugins/config:Registering a custom menu` for the full worked example, including Plugins that register several menus:

.. code:: diff

   -'services' => [
   -    'menus' => [
   -        'mautic.menu.mybundle' => [
   -            'alias'   => 'mybundle',
   -            'options' => ['template' => '@MyBundle/Menu/mybundle.html.twig'],
   -        ],
   -    ],
   -],
   +$services->set('mautic.menu.mybundle', Knp\Menu\MenuItem::class)
   +    ->factory([service(Mautic\CoreBundle\Menu\MenuBuilder::class), 'mybundleMenu'])
   +    ->tag('knp_menu.menu', ['alias' => 'mybundle']);
   +
   +$services->set('mautic.menu_renderer.mybundle', Mautic\CoreBundle\Menu\MenuRenderer::class)
   +    ->args([service('knp_menu.matcher'), service('twig'), ['template' => '@MyBundle/Menu/mybundle.html.twig']])
   +    ->tag('knp_menu.renderer', ['alias' => 'mybundle']);

.. _mautic 8 cachestoragehelper:

.. vale off

CacheStorageHelper
==================

.. vale on

Mautic 8 removes the deprecated ``Mautic\CoreBundle\Helper\CacheStorageHelper`` class and its ``mautic.helper.cache_storage`` service. Inject ``Mautic\CacheBundle\Cache\CacheProviderInterface`` instead, and call ``getSimpleCache()`` for the simple cache API the helper mimicked. The ``get()``, ``set()``, ``has()``, and ``delete()`` methods keep their signatures:

.. vale off

.. code:: diff

   -use Mautic\CoreBundle\Helper\CacheStorageHelper;
   +use Mautic\CacheBundle\Cache\CacheProviderInterface;

   -public function __construct(private CacheStorageHelper $cache)
   +public function __construct(private CacheProviderInterface $cache)
    {
    }

    public function getPendingCount(int $id): ?int
    {
   -    return $this->cache->get("email|{$id}|pending");
   +    return $this->cache->getSimpleCache()->get("email|{$id}|pending");
    }

.. vale on

Two behaviors change with the new provider:

* A cache miss returns ``null`` instead of ``false``, so change a comparison from ``false === $value`` to ``null === $value``.
* Cached data lives in the adapter that the ``cache_adapter`` parameter sets, filesystem by default, instead of the ``cache_items`` database table, so clearing the cache drops it. Mautic 8 also removes the ``Mautic\CoreBundle\Entity\Cache`` entity that mapped the ``cache_items`` table.

For how to configure the adapter, see :doc:`/plugins/cache`. For the Integration cache, see :ref:`AbstractIntegration <mautic 8 abstractintegration>`.

.. vale off

Segment and Contact filter operators
====================================

.. vale on

Mautic 8 removes the public ``getFilterExpressionFunctions()`` method from ``Mautic\LeadBundle\Entity\OperatorListTrait``, and ``Mautic\LeadBundle\Entity\LeadRepository`` and ``Mautic\LeadBundle\Entity\LeadListRepository`` no longer use that trait. If your Plugin called ``getFilterExpressionFunctions()`` on either repository, call ``Mautic\LeadBundle\Provider\TypeOperatorProvider::getOperatorsForFieldType()`` instead:

.. code:: diff

   -$operators = $leadRepository->getFilterExpressionFunctions();
   +$operators = $typeOperatorProvider->getOperatorsForFieldType($fieldType);

.. vale off

FieldModel::getFieldList()
==========================

.. vale on

Mautic 8 removes the deprecated ``Mautic\LeadBundle\Model\FieldModel::getFieldList()`` method, which only forwarded the call to ``Mautic\LeadBundle\Field\FieldList::getFieldList()``. Call ``FieldList::getFieldList()`` directly:

.. code:: diff

   -$fields = $fieldModel->getFieldList();
   +$fields = $fieldList->getFieldList();

.. _mautic 8 defaultconfigformtrait:

.. vale off

DefaultConfigFormTrait
======================

.. vale on

Mautic 8 removes ``Mautic\IntegrationsBundle\Integration\DefaultConfigFormTrait``. Each of its methods returned ``null`` to keep Mautic's default configuration Form. Remove the ``use DefaultConfigFormTrait;`` statement from your Integration class and implement the methods directly. ``ConfigFormInterface`` declares ``getConfigFormName()`` and ``getConfigFormContentTemplate()``, and ``ConfigFormSyncInterface`` declares ``getSyncConfigFormName()``, so add the ones that your Integration's interfaces require:

.. code-block:: php

   public function getConfigFormName(): ?string
   {
       return null;
   }

   public function getConfigFormContentTemplate(): ?string
   {
       return null;
   }

   public function getSyncConfigFormName(): ?string
   {
       return null;
   }

Return ``null`` from a method to keep Mautic's default, or return your own Form type or template.

.. _mautic 8 doctrine orm 3 and dbal 4:

.. vale off

Doctrine ORM 3 and DBAL 4
=========================

.. vale on

Mautic 8 upgrades to Doctrine ``ORM`` 3, DBAL 4, and doctrine-bundle 3. Doctrine ``ORM`` 3 doesn't support DocBlock annotations such as ``@ORM\Column``, so convert any annotations on your Plugin's entities to ``#[ORM\...]`` attributes, or map the entities with the PHP static function mapping. :ref:`Plugins/database:Entities and schema` covers both mapping styles. This section lists the API surface a Plugin might call directly:

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Was
     - Now
   * - ``Doctrine\ORM\Mapping\ClassMetadataInfo``
     - ``Doctrine\ORM\Mapping\ClassMetadata``
   * - ``Doctrine\ORM\ORMException``
     - ``Doctrine\ORM\Exception\ORMException``, now an interface
   * - ``Doctrine\DBAL\Exception`` thrown directly
     - an interface - throw ``Mautic\CoreBundle\Exception\DbalException``
   * - ``EntityRepository::$_em``
     - ``getEntityManager()``
   * - DBAL's ``ExpressionBuilder::andX()`` / ``orX()``
     - ``and()`` / ``or()``, or ``CompositeExpression::and()`` / ``or()``
   * - ``Connection::ARRAY_PARAM_OFFSET``, ``Connection::PARAM_*_ARRAY``
     - ``Doctrine\DBAL\ArrayParameterType``
   * - ``AbstractPlatform::quoteIdentifier()``
     - ``quoteSingleIdentifier()``

``Doctrine\DBAL\Connection::createQueryBuilder()`` now returns ``Mautic\CoreBundle\Doctrine\Query\QueryBuilder`` on every Mautic connection, which keeps the ``getQueryPart()``, ``getQueryParts()``, and ``resetQueryPart()`` methods DBAL 4 dropped from its own builder. If your Plugin builds its own DBAL builder with ``new QueryBuilder($connection)``, take the builder from the connection instead, so you keep those methods.

.. _mautic 8 classmetadatabuilder:

.. vale off

ClassMetadataBuilder
====================

.. vale on

Mautic 8 removes the ``addContact()`` and ``addLead()`` helpers from ``Mautic\CoreBundle\Doctrine\Mapping\ClassMetadataBuilder``. Each mapped a many-to-one association to ``Mautic\LeadBundle\Entity\Lead``, on the ``contact_id`` or ``lead_id`` column. If an entity's ``loadMetadata()`` calls one of them, build the association yourself. For example, this replaces ``$builder->addContact()`` with its default arguments:

.. code:: diff

   -$builder->addContact();
   +$builder->createManyToOne('contact', Lead::class)
   +    ->addJoinColumn('contact_id', 'id', false, false, 'CASCADE')
   +    ->build();

An entity that you map with attributes declares the same association with ``#[ORM\ManyToOne(targetEntity: Lead::class)]`` and ``#[ORM\JoinColumn(name: 'contact_id', nullable: false, onDelete: 'CASCADE')]``.

``createManyToMany()`` and ``createOneToMany()`` still work, but they now return Doctrine's own ``Doctrine\ORM\Mapping\Builder\ManyToManyAssociationBuilder`` and ``OneToManyAssociationBuilder``. Mautic 8 removes its ``Mautic\CoreBundle\Doctrine\Mapping\ManyToManyAssociationBuilder`` and ``OneToManyAssociationBuilder`` classes, so update any type hint that names them.

Mautic 8 also removes ``AssociationBuilder::isOwnershipParent()``. Mark the entity class with the ``#[Mautic\CoreBundle\Entity\Attribute\OwnershipParent]`` attribute instead, naming the association that carries the owner:

.. code:: diff

   +#[OwnershipParent('form')]
    class Field
    {
        public static function loadMetadata(ORM\ClassMetadata $metadata): void
        {
            $builder->createManyToOne('form', 'Form')
   -            ->isOwnershipParent()
                ->build();

.. vale off

.. _mautic 8 final classes:

``final`` classes
*****************

Mautic 8 declares more than 300 core classes ``final``, because no Mautic class extends them and Mautic doesn't intend them as base classes. Nothing changes for code that gets these classes through dependency injection, calls their public methods, or subscribes to their events. Two kinds of Plugin code break:

* A Plugin class that extends one of these classes causes a fatal error when PHP loads it, for example ``Class MauticPlugin\HelloWorldBundle\Model\MyPageModel cannot extend final class Mautic\PageBundle\Model\PageModel``.
* A Plugin test that mocks one of these classes with :xref:`phpunit` fails, because the test framework can't create a test double of a ``final`` class.

Some of the event classes described earlier in this guide are now ``final``, including ``ConfigBuilderEvent``, ``EmailValidationEvent``, ``SubmissionEvent``, ``PointBuilderEvent``, and ``WebhookBuilderEvent``. For these classes, the guidance about overriding typed methods no longer applies, because you can't extend them.

.. vale off

Affected classes
================

.. vale on

These event classes are now ``final``:

.. vale off

* ``Mautic\ConfigBundle\Event\ConfigBuilderEvent``
* ``Mautic\CoreBundle\Event\MaintenanceEvent``
* ``Mautic\CoreBundle\Event\StatsEvent``
* ``Mautic\EmailBundle\Event\EmailValidationEvent``
* ``Mautic\FormBundle\Event\SubmissionEvent``
* ``Mautic\IntegrationsBundle\Event\MauticSyncFieldsLoadEvent``
* ``Mautic\LeadBundle\Event\ImportValidateEvent``
* ``Mautic\PageBundle\Event\PageDisplayEvent``
* ``Mautic\PageBundle\Event\PageHitEvent``
* ``Mautic\PluginBundle\Event\PluginIntegrationRequestEvent``
* ``Mautic\PluginBundle\Event\PluginIsPublishedEvent``
* ``Mautic\PointBundle\Event\PointBuilderEvent``
* ``Mautic\PointBundle\Event\TriggerExecutedEvent``
* ``Mautic\ReportBundle\Event\ReportDataEvent``
* ``Mautic\ReportBundle\Event\ReportGeneratorEvent``
* ``Mautic\ReportBundle\Event\ReportGraphEvent``
* ``Mautic\SmsBundle\Event\SmsSendEvent``
* ``Mautic\UserBundle\Event\LoginEvent``
* ``Mautic\WebhookBundle\Event\WebhookBuilderEvent``
* ``Mautic\WebhookBundle\Event\WebhookNotificationEvent``

.. vale on

Four event classes aren't on this list because they stay extendable. ``Mautic\LeadBundle\Event\CompanyEvent``, ``Mautic\LeadBundle\Event\LeadListEvent``, and ``Mautic\WebhookBundle\Event\WebhookEvent`` are ``abstract``, since each lifecycle event now gets its own dedicated subclass instead of sharing one object. ``Mautic\LeadBundle\Event\ListChangeEvent`` is a plain, non-``final`` class. A Plugin can still extend any of these four.

The other ``final`` classes include:

.. vale off

* Models such as ``AssetModel``, ``CampaignModel``, ``EventModel``, the Form ``FieldModel``, ``PageModel``, ``PointModel``, ``ReportModel``, ``SmsModel``, ``UserModel``, and ``WebhookModel``
* Repositories such as ``LeadRepository``, ``LeadListRepository``, ``CompanyRepository``, ``FormRepository``, ``PageRepository``, and ``UserRepository``
* Helpers such as ``MailHelper``, ``IpLookupHelper``, ``CookieHelper``, ``DateTimeHelper``, ``IntegrationHelper``, and the Asset, Form, Page, and Focus ``TokenHelper`` classes
* The ``ConnectwiseIntegration``, ``HubspotIntegration``, ``SalesforceIntegration``, and ``VtigerIntegration`` classes in ``MauticPlugin\MauticCrmBundle\Integration``

.. vale on

To find out whether a class you use is ``final``, open it in your Mautic 8 codebase and look for the ``final`` keyword in its declaration.

.. vale off

Removed methods
===============

.. vale on

Mautic 8 removes two unused public methods:

* ``Mautic\LeadBundle\Entity\LeadListRepository::autowireLeadListRepository()``, which injected an event dispatcher that the repository never used.
* ``Mautic\PluginBundle\Model\IntegrationEntityModel::logDataSync()``, which had an empty body.

Remove any calls to these methods from your Plugin.

.. vale off

Update your Plugin
==================

.. vale on

If your Plugin extends one of these classes, inject the Mautic class into your own service and call its public methods instead of inheriting from it. To change what an event carries, subscribe to the event and call its setters rather than dispatching a subclass.

If your Plugin's tests mock one of these classes, enable ``DG\BypassFinals`` before the tests load the classes. Mautic lists ``dg/bypass-finals`` as a development dependency and enables it in ``app/tests/bootstrap.php``. The example Plugin workflow in :doc:`continuous_integration` bootstraps with ``vendor/autoload.php`` only, so add a bootstrap file to your Plugin that enables ``DG\BypassFinals``:

.. code-block:: php

   <?php

   declare(strict_types=1);

   use DG\BypassFinals;

   require __DIR__.'/../../../vendor/autoload.php';

   BypassFinals::enable(bypassReadOnly: false);
   BypassFinals::denyPaths(['*/vendor/*']);

Point the ``--bootstrap`` option of ``bin/phpunit`` at this file instead of ``vendor/autoload.php``. Adjust the ``require`` path to match where the file sits in your Plugin.

.. _mautic 8 typed class constants:

Typed class constants
*********************

Mautic 8 declares a native type on every class and interface constant, using PHP 8.3 typed class constants. For example, ``ConfigFormFeaturesInterface::FEATURE_SYNC`` changes from ``public const FEATURE_SYNC = 'sync';`` to ``public const string FEATURE_SYNC = 'sync';``. The values don't change, so code that only reads these constants keeps working.

A Plugin class that overrides a constant from a Mautic parent class or interface must declare a compatible type on its own constant. If the overriding constant has no type, or a type that isn't compatible, PHP stops with a fatal error like this when it loads the class:

.. code-block:: text

   Type of MauticPlugin\HelloWorldBundle\Command\SyncWorldsCommand::MODE_PID must be compatible with Mautic\CoreBundle\Command\ModeratedCommand::MODE_PID of type string

To fix it, add the parent's type to the constant in your Plugin. A narrower type also works, such as ``string`` where the parent declares ``?string``:

.. code:: diff

   - public const MODE_PID = 'pid';
   + public const string MODE_PID = 'pid';

Constants that a Plugin is most likely to override come from these base classes and interfaces:

.. vale off

* ``Mautic\CoreBundle\Command\ModeratedCommand``: ``MODE_PID``, ``MODE_FLOCK``, and ``MODE_REDIS`` are ``string``
* ``Mautic\CoreBundle\Doctrine\AbstractMauticMigration``: ``TABLE_NAME`` is ``?string``, and ``COLUMN_TYPE_SIGNED`` and ``COLUMN_TYPE_UNSIGNED`` are ``string``
* ``Mautic\CoreBundle\Entity\OptimisticLockInterface``: ``INITIAL_VERSION`` is ``int``
* ``Mautic\CoreBundle\Entity\UpsertInterface``: ``ROWS_AFFECTED_ON_INSERT`` and ``ROWS_AFFECTED_ON_UPDATE`` are ``int``
* ``Mautic\CoreBundle\Helper\AbstractFormFieldHelper``: the ``FORMAT_*`` constants are ``string``
* ``Mautic\CoreBundle\IpLookup\AbstractLocalDataLookup``: ``TAR_CACHE_FOLDER`` and ``TAR_TEMP_FILE`` are ``string``
* ``Mautic\IntegrationsBundle\Integration\Interfaces\ConfigFormFeaturesInterface``: ``FEATURE_SYNC`` and ``FEATURE_PUSH_ACTIVITY`` are ``string``
* ``Mautic\IntegrationsBundle\Sync\SyncJudge\SyncJudgeInterface``: the evidence mode and winner constants are ``string``
* ``Mautic\PluginBundle\Integration\AbstractIntegration``: the ``FIELD_TYPE_*`` constants are ``string``

.. vale on

Because ``AbstractMauticMigration::TABLE_NAME`` is ``?string``, a migration that sets a table name declares it as ``protected const string TABLE_NAME = 'table_name';``.

.. _mautic 8 symfony 8:

Symfony 8
*********

Mautic 8 requires PHP 8.4 and runs on Symfony 8.1, so your Plugin's code and templates must also follow the Symfony 8 changes. For the full list, see the :xref:`Symfony 8.0 upgrade guide`.

Symfony 8 removes ``Symfony\Component\HttpFoundation\Request::get()``, which searched the route attributes, the query string, and the request body in turn. Read the value from the parameter bag that holds it instead:

.. code:: diff

   - $code = $request->get('code');
   + $code = $request->query->get('code');

Use ``$request->query`` for query string parameters, ``$request->request`` for parameters in a ``POST`` body, and ``$request->attributes`` for route parameters. In Twig templates, replace ``app.request.get('name')`` with the matching bag, such as ``app.request.query.get('name')``.

Symfony 8 also removes ``eraseCredentials()`` from ``Symfony\Component\Security\Core\User\UserInterface``, and Mautic 8 removes ``Mautic\UserBundle\Entity\User::eraseCredentials()``. Remove any call to it. A class of your own that implements ``UserInterface`` no longer needs the method.
