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

.. vale off

CommonRepository
****************

.. vale on

This has the widest impact - this change hits every repository that overrides these methods. The class is ``Mautic\CoreBundle\Entity\CommonRepository``.

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

Mautic 8 also changes the helper methods on the base controllers. See :ref:`Controller helper methods <Mautic 8 controller helper methods>` if your Plugin has a controller that extends a Mautic controller.

.. note::

   When you call one of these methods, pass arguments of the declared types. When you extend one of these events and override a typed method, copy the parent signature exactly, using the same parameter types, return type, and property type.

Mautic 8 changes event or entity class signatures in these bundles:

* CampaignBundle
* ChannelBundle
* ConfigBundle
* DashboardBundle
* EmailBundle
* FormBundle
* IntegrationsBundle
* PageBundle
* PointBundle
* UserBundle
* WebhookBundle

.. vale off

CampaignBundle
**************

.. vale on

Mautic 8 adds type declarations to the Campaign Event entity and three Campaign event classes.

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

Subscribers to Campaign membership changes receive ``Mautic\CampaignBundle\Event\CampaignLeadChangeEvent``, a ``final`` class, so the override risk doesn't apply. Its constructor types ``$leads``, and ``getLead()`` gains a return type:

.. code:: diff

   - public function __construct(..., $leads, ...)
   + public function __construct(..., array|\Mautic\LeadBundle\Entity\Lead $leads, ...)

.. code:: diff

   - public function getLead()
   + public function getLead(): ?\Mautic\LeadBundle\Entity\Lead

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
   + public function getParametersFromConfig(string $bundle)

.. vale off

ConfigEvent
===========

.. vale on

Subscribers that read and validate saved configuration values use ``Mautic\ConfigBundle\Event\ConfigEvent``. ``getConfig()`` and ``setConfig()`` type ``$key`` as ``?string``:

.. code:: diff

   - public function getConfig($key = null)
   + public function getConfig(?string $key = null)

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

DashboardBundle
***************

.. vale on

Mautic 8 adds type declarations to two Dashboard Widget event classes.

.. vale off

WidgetDetailEvent
=================

.. vale on

Widget subscribers set the Widget template on ``Mautic\DashboardBundle\Event\WidgetDetailEvent``. ``setTemplate()`` types ``$template`` as ``string``:

.. code:: diff

   - public function setTemplate($template): void
   + public function setTemplate(string $template): void

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

.. vale off

TriggerBuilderEvent
===================

.. vale on

Plugins register a custom Point trigger on ``Mautic\PointBundle\Event\TriggerBuilderEvent``. ``addEvent()`` types ``$key`` as ``string``:

.. code:: diff

   - public function addEvent($key, array $event): void
   + public function addEvent(string $key, array $event): void

.. vale off

For a Point extension example, see :doc:`/plugin_extensions/points`.

UserBundle
**********

.. vale on

Mautic 8 adds type declarations to one User authentication event class.

.. vale off

AuthenticationEvent
===================

.. vale on

Authentication Integrations set the User on ``Mautic\UserBundle\Event\AuthenticationEvent``. ``setUser()`` types ``$saveUser`` and ``$createIfNotExists`` as ``bool``, and ``setIsAuthenticated()`` types ``$createIfNotExists`` as ``bool``:

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
