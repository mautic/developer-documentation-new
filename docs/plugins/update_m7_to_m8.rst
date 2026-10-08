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
   + public function saveEntity(object $entity, $flush = true): void

   - public function deleteEntity($entity, $flush = true): void
   + public function deleteEntity(object $entity, $flush = true): void

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

.. vale off

AbstractPermissions
*******************

.. vale on

Every bundle and Plugin defines its own ``*Permissions`` class that extends ``Mautic\CoreBundle\Security\Permissions\AbstractPermissions``. If yours overrides any of these methods, copy the new signature exactly.

.. code:: diff

   - public function isGranted($userPermissions, $name, $level): bool
   + public function isGranted(array $userPermissions, $name, $level): bool

   - protected function addStandardFormFields($bundle, $level, &$builder, $data, $includePublish = true)
   + protected function addStandardFormFields($bundle, $level, &$builder, array $data, $includePublish = true)

   - protected function addManageFormFields($bundle, $level, &$builder, $data)
   + protected function addManageFormFields($bundle, $level, &$builder, array $data)

   - protected function addExtendedFormFields($bundle, $level, &$builder, $data, $includePublish = true)
   + protected function addExtendedFormFields($bundle, $level, &$builder, array $data, $includePublish = true)

.. vale off

For a permissions extension example, see :doc:`/plugins/permissions`.

.. vale on

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
   + public function authCallback(array $settings = [], $parameters = [])

   - public function mergeConfigToFeatureSettings($config = [])
   + public function mergeConfigToFeatureSettings(array $config = [])

   - public function getFormCompanyFields($settings = [])
   + public function getFormCompanyFields(array $settings = [])

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
   + protected function getModel(string $modelNameKey): MauticModelInterface

   - public function executeAction(Request $request, $objectAction, $objectId = 0, $objectSubId = 0, $objectModel = '')
   + public function executeAction(Request $request, $objectAction, $objectId = 0, $objectSubId = 0, $objectModel = ''): Response

   - public function ajaxAction(Request $request, $args = []): Response
   + public function ajaxAction(Request $request, array $args = []): Response

The ``AbstractFormController`` class adds parameter and return types to its lock-handling methods.

.. code:: diff

   - public function unlockAction(Request $request, $objectId, $objectModel)
   + public function unlockAction(Request $request, $objectId, string $objectModel): RedirectResponse

   - protected function isLocked($postActionVars, $entity, $model, $batch = false)
   + protected function isLocked($postActionVars, $entity, string $model, $batch = false)

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

.. vale off

CampaignBundle
**************

.. vale on

Mautic 8 adds type declarations to the Campaign Event entity and three Campaign event classes. It also dispatches the Campaign save and delete events by dedicated event classes.

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

Subscribers to Campaign membership changes receive ``CampaignSingleLeadChangeEvent`` or ``CampaignBatchLeadChangeEvent``. Both are ``final`` subclasses of the abstract ``Mautic\CampaignBundle\Event\CampaignLeadChangeEvent``, so the override risk doesn't apply. The base class constructor types ``$leads``, and ``getLead()`` gains a return type:

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

ChannelBundle
*************

.. vale on

Mautic 8 adds type declarations to three Channel event classes.

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

ConfigBundle
************

.. vale on

Mautic 8 adds type declarations to two configuration event classes.

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

.. vale off

CoreBundle
**********

.. vale on

Mautic 8 adds native type declarations to several ``Mautic\CoreBundle\Event\`` classes that Plugins subscribe to and dispatch. Some narrow a parameter or return type, so a subscriber or caller that passes a previously tolerated type raises a ``TypeError`` at runtime under ``strict_types``. Others match the types the methods already accepted. Grep your ``use`` statements for the ``Mautic\CoreBundle\Event\`` namespace to find the classes your Plugin references.

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
   +    public function getViewName(): string

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

.. vale off

DashboardBundle
***************

.. vale on

Mautic 8 adds type declarations to the Dashboard Widget entity and two Dashboard Widget event classes.

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

``WidgetDetailEvent`` is an abstract base class for the ``final`` ``PreLoadWidgetDetailEvent`` and ``GenerateWidgetDetailEvent`` classes that Mautic dispatches. For the event classes to subscribe to, see :ref:`Mautic 8 class-name event dispatch <Mautic 8 class-name event dispatch>`.

.. vale off

WidgetTypeListEvent
===================

.. vale on

Plugins register a Widget type on ``Mautic\DashboardBundle\Event\WidgetTypeListEvent``, a ``final`` class, so the override risk doesn't apply. ``addType()`` types only ``$bundle``, and leaves ``$widgetType`` without a type:

.. code:: diff

   - public function addType($widgetType, $bundle = 'others'): void
   + public function addType($widgetType, string $bundle = 'others'): void

.. vale off

EmailBundle
***********

.. vale on

Mautic 8 adds type declarations to four Email event classes.

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

``setCriteriaRequest()`` types the same two parameters, and leaves ``$criteria`` without a type:

.. code:: diff

   - public function setCriteriaRequest($bundleKey, $folderKeys, $criteria, bool $markAsSeen = true): void
   + public function setCriteriaRequest(string $bundleKey, string|array $folderKeys, $criteria, bool $markAsSeen = true): void

.. vale off

For an Email extension example, see :doc:`/plugin_extensions/emails`.

FormBundle
**********

.. vale on

Mautic 8 adds type declarations to two Form event classes.

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

IntegrationsBundle
******************

.. vale on

Mautic 8 adds type declarations to one Integrations token event class.

.. vale off

MappedIntegrationObjectTokenEvent
=================================

.. vale on

Integration subscribers register mapped-object tokens on ``Mautic\IntegrationsBundle\Event\MappedIntegrationObjectTokenEvent``. On ``addToken()``, only the last three parameters gain ``string`` types, and ``$integrationName``, ``$objectName``, and ``$objectLink`` keep none:

.. code:: diff

   - public function addToken($integrationName, $objectName, $objectLink, $title = '', $linkText = 'Link Text', $default = 'Default Value'): void
   + public function addToken($integrationName, $objectName, $objectLink, string $title = '', string $linkText = 'Link Text', string $default = 'Default Value'): void

.. vale off

LeadBundle
**********

.. vale on

Mautic 8 adds type declarations to three Contact and Segment event classes and to the ``ContactTracker`` service.

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

For a Contact extension example that uses ``ContactTracker``, see :doc:`/plugin_extensions/contacts`.

NotificationBundle
******************

.. vale on

Mautic 8 adds parameter types to three Notification entity classes. Plugins that create or update these entities must pass arguments of the declared types:

* ``Mautic\NotificationBundle\Entity\Notification`` - ``setName()``, ``setButton()``, and ``setMessage()`` take ``?string``, ``setNotificationType()`` takes ``string``, ``setUtmTags()`` takes ``array``, and ``setMobile()`` takes ``bool``.
* ``Mautic\NotificationBundle\Entity\PushID`` - ``setEnabled()`` and ``setMobile()`` take ``bool``.
* ``Mautic\NotificationBundle\Entity\Stat`` - ``setDateSent()`` narrows from ``mixed`` to ``\DateTimeInterface``, so passing a date string now raises a ``TypeError`` at runtime.

.. code:: diff

   - public function setDateSent($dateSent): void
   + public function setDateSent(\DateTimeInterface $dateSent): void

.. vale off

PageBundle
**********

.. vale on

Mautic 8 adds type declarations to one tracked-link redirect event class.

.. vale off

RedirectGenerationEvent
=======================

.. vale on

Subscribers that build a tracked-link redirect use ``Mautic\PageBundle\Event\RedirectGenerationEvent``. ``setInClickthrough()`` narrows ``$value`` from ``mixed`` to ``string``, so passing a non-string value now raises a ``TypeError`` at runtime:

.. code:: diff

   - public function setInClickthrough($key, $value): void
   + public function setInClickthrough(string $key, string $value): void

.. vale off

PointBundle
***********

.. vale on

Mautic 8 adds type declarations to the Point TriggerEvent entity and two Point event classes.

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

For an SMS transport example, see :doc:`/plugin_extensions/sms`.

StageBundle
***********

.. vale on

Mautic 8 adds parameter types to the Stage and Contact Stage log entities.

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

.. vale off

UserBundle
**********

.. vale on

Mautic 8 adds type declarations to one User authentication event class.

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

.. vale off

WebhookBundle
*************

.. vale on

Mautic 8 adds type declarations to the Webhook Event entity and one Webhook event class.

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

Listeners to ``PluginEvents::PLUGIN_ON_INTEGRATION_RESPONSE`` now receive a new ``Mautic\PluginBundle\Event\PluginIntegrationResponseEvent`` instead of ``PluginIntegrationRequestEvent``. ``AbstractIntegration::makeRequest()`` creates the new event with the Integration and the response, so ``getResponse()`` always returns a ``Psr\Http\Message\ResponseInterface``. ``PluginIntegrationRequestEvent`` no longer has ``getResponse()`` or ``setResponse()``.

A listener that still type-hints ``PluginIntegrationRequestEvent`` raises a ``TypeError`` when Mautic dispatches the event. Change the type hint:

.. code:: diff

   - public function onResponse(PluginIntegrationRequestEvent $event): void
   + public function onResponse(PluginIntegrationResponseEvent $event): void
     {
         $response = $event->getResponse();

The new event extends ``AbstractPluginIntegrationEvent``, so ``getIntegration()`` and ``getIntegrationName()`` still work. Listeners to ``PluginEvents::PLUGIN_ON_INTEGRATION_REQUEST`` still receive ``PluginIntegrationRequestEvent``, but can no longer read the response from it.

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

.. _mautic 8 final classes:

``final`` classes
*****************

Mautic 8 declares more than 300 core classes ``final``, because no Mautic class extends them and Mautic doesn't intend them as base classes. Nothing changes for code that gets these classes through dependency injection, calls their public methods, or subscribes to their events. Two kinds of Plugin code break:

* A Plugin class that extends one of these classes causes a fatal error when PHP loads it, for example ``Class MauticPlugin\HelloWorldBundle\Model\MyPageModel cannot extend final class Mautic\PageBundle\Model\PageModel``.
* A Plugin test that mocks one of these classes with :xref:`phpunit` fails, because the test framework can't create a test double of a ``final`` class.

Some of the event classes described earlier in this guide are now ``final``, including ``ConfigBuilderEvent``, ``ConfigEvent``, ``EmailValidationEvent``, ``SubmissionEvent``, ``PointBuilderEvent``, and ``WebhookBuilderEvent``. For these classes, the guidance about overriding typed methods no longer applies, because you can't extend them.

.. vale off

Affected classes
================

.. vale on

These event classes are now ``final``:

.. vale off

* ``Mautic\ConfigBundle\Event\ConfigBuilderEvent``
* ``Mautic\ConfigBundle\Event\ConfigEvent``
* ``Mautic\CoreBundle\Event\MaintenanceEvent``
* ``Mautic\CoreBundle\Event\StatsEvent``
* ``Mautic\EmailBundle\Event\EmailValidationEvent``
* ``Mautic\FormBundle\Event\SubmissionEvent``
* ``Mautic\IntegrationsBundle\Event\MauticSyncFieldsLoadEvent``
* ``Mautic\LeadBundle\Event\CompanyEvent``
* ``Mautic\LeadBundle\Event\ImportValidateEvent``
* ``Mautic\LeadBundle\Event\LeadListEvent``
* ``Mautic\LeadBundle\Event\ListChangeEvent``
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
* ``Mautic\WebhookBundle\Event\WebhookEvent``
* ``Mautic\WebhookBundle\Event\WebhookNotificationEvent``

.. vale on

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
