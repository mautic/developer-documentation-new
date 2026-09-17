Update Plugins for Mautic 8
###########################

Mautic 8 adds native PHP parameter, return, and property type declarations to nine ``CoreBundle`` event classes. These types match what the methods already accepted, so there's no runtime behavior change - most were already recorded in the classes' ``@param`` and ``@return`` annotations, and Mautic 8 now enforces them in the signatures.

Plugins interact with these events by subscribing to them and calling their methods, and some Plugins extend them. Your upgrade risk is twofold: a call that passes an argument outside a method's now-narrowed type raises a ``TypeError`` at runtime, and an override that no longer matches the parent's explicit signature is a fatal error when PHP loads your class.

.. note::

   When you call one of these methods, pass the documented types. When you extend one of these events and override a method, copy the parent signature exactly, using the same parameter types, return type, and property type.

Watch for two kinds of break:

* **Narrowed parameter or property type**: passing an argument that no longer matches a method's or constructor's declared type raises a ``TypeError`` at runtime. This includes a promoted property such as ``MaintenanceEvent``'s ``$daysOld``, which now requires an ``int``.
* **Overridden method**: if your Plugin extends one of these events and overrides a typed method, the override must copy the new signature exactly or PHP raises a fatal error.

.. vale off

BuildJsEvent
************

.. vale on

Subscribers to ``CoreEvents::BUILD_MAUTIC_JS`` call ``appendJs()`` on ``Mautic\CoreBundle\Event\BuildJsEvent`` to add JavaScript. Both string parameters are now typed:

.. code:: diff

   - public function appendJs($js, $section = '')
   + public function appendJs(string $js, string $section = '')

The ``appendJsForScope()`` method narrows its ``$js`` and section parameters to ``string`` in the same way.

.. vale off

BuilderEvent
************

.. vale on

The ``Mautic\CoreBundle\Event\BuilderEvent`` constructor now accepts a ``string`` or an ``array`` for its ``$requested`` argument:

.. code:: diff

   - public function __construct(..., $requested = 'all')
   + public function __construct(..., string|array $requested = 'all')

.. vale off

CommandListEvent
****************

.. vale on

``addCommands()`` in ``Mautic\CoreBundle\Event\CommandListEvent`` now types its ``$header`` parameter as ``string``:

.. code:: diff

   - public function addCommands($header, array $commands)
   + public function addCommands(string $header, array $commands)

.. vale off

CustomAssetsEvent
*****************

.. vale on

Subscribers add custom scripts and declarations to the GrapesJS Theme through ``Mautic\CoreBundle\Event\CustomAssetsEvent``. Its ``addCustomDeclaration()``, ``addScript()``, and ``addScriptDeclaration()`` methods now type the ``$location`` parameter as ``string``. For example, on ``addScript()``:

.. code:: diff

   - public function addScript(..., $location)
   + public function addScript(..., string $location)

.. vale off

CustomButtonEvent
*****************

.. vale on

``Mautic\CoreBundle\Event\CustomButtonEvent`` is a ``final`` class, so you can't extend it - the change affects only your calls to ``addButton()``. The ``$location`` and ``$route`` parameters gain types:

.. code:: diff

   - public function addButton(array $button, $location = null, $route = null)
   + public function addButton(array $button, ?string $location = null, array|string|null $route = null)

.. vale off

GlobalSearchEvent
*****************

.. vale on

``addResults()`` in ``Mautic\CoreBundle\Event\GlobalSearchEvent`` now types its ``$header`` parameter as ``string``:

.. code:: diff

   - public function addResults($header, array $results)
   + public function addResults(string $header, array $results)

.. vale off

IconEvent
*********

.. vale on

``addIcon()`` in ``Mautic\CoreBundle\Event\IconEvent`` now types its ``$type`` parameter as ``string``. The ``$icon`` parameter keeps no type declaration:

.. code:: diff

   - public function addIcon($type, $icon)
   + public function addIcon(string $type, $icon)

.. vale off

MaintenanceEvent
****************

.. vale on

Data-cleanup subscribers receive ``Mautic\CoreBundle\Event\MaintenanceEvent``. Its constructor now promotes ``$daysOld`` to a ``protected int $daysOld`` property, so callers must pass an ``int``. A numeric string only works when the calling file runs without ``strict_types``:

.. code:: diff

   - public function __construct($daysOld, ...)
   + public function __construct(protected int $daysOld, ...)

``setStat()`` now types its ``$parameters`` argument as ``array``:

.. code:: diff

   - public function setStat($key, $recordCount, $sql = null, $parameters = [])
   + public function setStat($key, $recordCount, $sql = null, array $parameters = [])

For a maintenance subscriber example, see :doc:`/plugin_extensions/maintenance`.

.. vale off

TokenReplacementEvent
*********************

.. vale on

Of all the classes on this list, ``Mautic\CoreBundle\Event\TokenReplacementEvent`` has the biggest impact on Plugin authors. The ``@param`` annotation on ``setContent()`` was ``CommonEntity|string|null``. The method now accepts ``string`` only:

.. code:: diff

   - public function setContent($content)
   + public function setContent(string $content)

A subscriber that calls ``setContent(null)`` or passes an entity now triggers a ``TypeError``.

The constructor types ``$content`` as ``Lead|array|string|null`` and ``$lead`` as ``Lead|array|null``:

.. code:: diff

   - public function __construct($content, $lead, ...)
   + public function __construct(Lead|array|string|null $content, Lead|array|null $lead, ...)

The ``getLead()`` method gains a matching return type:

.. code:: diff

   - public function getLead()
   + public function getLead(): Lead|array|null
