Update Plugins for Mautic 8
###########################

When you upgrade a Plugin to Mautic 8, review the event and entity classes your Plugin subscribes to, calls, or extends. Mautic 8 adds native PHP parameter, return, and property type declarations to the event and entity classes listed below. These types match what the methods already accepted, so there's no runtime behavior change - most were already recorded in the classes' ``@param`` and ``@return`` annotations, and Mautic 8 now enforces them in the signatures.

Plugins interact with these events by subscribing to them and calling their methods, and some Plugins extend them. This creates two kinds of break:

* A narrowed parameter or property type raises a ``TypeError`` at runtime when you pass an argument that no longer matches the method's declared type. For example, ``SubmissionEvent::setPostSubmitCallbackResponse()`` now requires a ``RedirectResponse``, so passing any other response type throws a ``TypeError``.
* An overridden method whose signature no longer matches the parent causes a fatal error when PHP loads your class.

If your Plugin doesn't subscribe to, call, or extend any of the classes listed below, you have nothing to change.

Mautic 8 also adds a native type to every class and interface constant. See :ref:`Typed class constants <Mautic 8 typed class constants>` if your Plugin overrides a constant from a Mautic class or interface.

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
