Update Plugins for Mautic 8
###########################

Mautic 8 adds native type declarations to several ``CoreBundle`` Event classes that Plugins subscribe to and dispatch. For how a Plugin subscribes to Events, see :doc:`/plugins/event_listeners`. Where a type narrowed, a subscriber or caller that passes a previously tolerated type now throws a ``TypeError`` at runtime under ``strict_types``. This guide covers only these ``CoreBundle`` Event type-declaration changes, not the full Mautic 8 upgrade process. It names each changed signature so you can align your Plugin when upgrading from Mautic 7 to Mautic 8. For the earlier upgrade, see :doc:`/plugins/update_m4_to_m5`.

.. note::

   Mautic updates its own in-tree callers as part of this change. Only out-of-tree Plugins that pass a previously tolerated type to these Events are affected.

These Event classes all live under the ``Mautic\CoreBundle\Event\`` namespace, so you can grep your ``use`` statements to find the ones your Plugin references.

Breaking type changes
*********************

These signatures narrowed a parameter or return type. Where your Plugin passes a previously tolerated type, align the call to the accepted type shown.

``TokenReplacementEvent``
=========================

``TokenReplacementEvent`` declares ``strict_types`` and has subscribers in the ``EmailBundle``, ``LeadBundle``, ``SmsBundle``, ``NotificationBundle``, and ``DynamicContentBundle``, and in the ``MauticFocusBundle`` Plugin.

``setContent()`` narrowed to ``string`` only. It previously accepted ``CommonEntity|string|null``, per the old ``PHPDoc`` annotation ``@param CommonEntity|string|null $content``. If your Plugin subscribes to this Event and calls ``setContent()``, pass a ``string``. This diff shows the signature change:

.. code:: diff

   -    public function setContent($content): void
   +    public function setContent(string $content): void

If your Plugin dispatches this Event, the constructor and ``getLead()`` are also typed. Note the asymmetry: the constructor accepts ``Lead|array|string|null`` for ``$content``, while ``setContent()`` accepts only ``string``. These diffs show the signature changes:

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

``CustomContentEvent``
======================

``CustomContentEvent`` is a ``final`` class and declares ``strict_types``.

``checkContext()`` now types both parameters as ``string``. Its ``$context`` parameter previously carried the ``PHPDoc`` type ``string|null``. The parameter order is ``$viewName`` then ``$context``. If your Plugin subscribes to this Event and calls ``checkContext()``, pass a ``string`` for both ``$viewName`` and ``$context``. This diff shows the signature change:

.. code:: diff

   -    public function checkContext($viewName, $context): bool
   +    public function checkContext(string $viewName, string $context): bool

If your Plugin dispatches this Event, the constructor promotes both parameters to ``readonly`` typed properties, ``readonly ?string $viewName`` and ``readonly ?string $context``. The getters are now typed ``getViewName(): string`` and ``getContext(): ?string``. This diff shows the constructor change:

.. code:: diff

   -    public function __construct(
   -        private $viewName,
   -        private $context = null,
   +    public function __construct(
   +        private readonly ?string $viewName,
   +        private readonly ?string $context = null,

These diffs show the getter changes:

.. code:: diff

   -    public function getViewName()
   +    public function getViewName(): string

   -    public function getContext()
   +    public function getContext(): ?string

``CustomButtonEvent``
=====================

``addButton()`` narrows ``$location`` to ``?string`` and widens ``$route`` to ``array|string|null``. If your Plugin subscribes to this Event and calls ``addButton()``, pass a ``string`` or ``null`` for ``$location``. Its sibling ``addButtons()`` keeps its original signature and needs no action. This diff shows the ``addButton()`` signature change:

.. code:: diff

   -    public function addButton(array $button, $location = null, $route = null): static
   +    public function addButton(array $button, ?string $location = null, array|string|null $route = null): static

Behavior changes to review
**************************

These changes preserve behavior in most cases. Review your Plugin against each one.

``BuilderEvent``
================

``getRequested()`` now requires a ``string $type`` argument, and ``$requested`` is typed ``string|array``. The internal comparison changed from loose ``==`` to strict ``===``, which is equivalent under the new types. Because ``getRequested()`` is ``protected``, this affects only a Plugin that subclasses ``BuilderEvent``. A subclass that overrides the method must add the required ``string $type`` parameter to its override. A subclass that assigns to the newly typed ``protected`` ``$requested`` property directly must assign a ``string`` or ``array``. These diffs show the changes:

.. code:: diff

   -    protected function getRequested($type): bool
   +    protected function getRequested(string $type): bool

.. code:: diff

   -        protected $requested = 'all',
   +        protected string|array $requested = 'all',

``MaintenanceEvent``
====================

The constructor now promotes ``$daysOld`` to a typed ``int`` property, which removes the explicit ``(int)`` cast. This preserves behavior for ``int`` or numeric-string input, because ``MaintenanceEvent`` doesn't declare ``strict_types``. A subscriber calls the public ``setStat()`` method to record maintenance stats. It now types ``$parameters`` as ``array``, which keeps its ``= []`` default, so only a caller passing a non-array value breaks. If your Plugin subscribes to this Event and calls ``setStat()``, pass an array for ``$parameters`` (or omit it). These diffs show the changes:

.. code:: diff

   -    public function __construct(
   -        $daysOld,
   +    public function __construct(
   +        protected int $daysOld,

.. code:: diff

   -    public function setStat($key, $recordCount, $sql = null, $parameters = []): void
   +    public function setStat($key, $recordCount, $sql = null, array $parameters = []): void

Classes typed to match existing ``PHPDoc``
*******************************************

These Event classes gained native types that match their previously documented ``PHPDoc``, so no Plugin action is needed:

* ``CustomAssetsEvent``
* ``BuildJsEvent`` - a ``final`` class
* ``CommandListEvent``
* ``GlobalSearchEvent``
* ``IconEvent``

Confirm your Plugin
*******************

Catch these type mismatches before you upgrade, rather than at runtime. Run static analysis with ``composer phpstan``, and exercise the affected code paths against Mautic 8 to surface any remaining mismatches.
