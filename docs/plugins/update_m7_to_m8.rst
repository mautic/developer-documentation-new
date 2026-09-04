Update Plugins for Mautic 8
###########################

Mautic 8 adds native PHP parameter, return, and property type declarations to the base and abstract classes that Plugins and Integrations commonly extend. There's no runtime behavior change - the types that these classes already relied on are only made explicit. Your only upgrade risk is a signature mismatch in your subclasses. If an override or a re-declared property no longer matches the parent's now-explicit signature, PHP throws a fatal ``TypeError`` or compile error.

.. note::

   When you override a method or declare one of these properties again, copy the parent signature exactly - same parameter types, same return type, same property type.

Watch for four kinds of break:

* New parameter type: an override without the identical type is a fatal error.
* New return type: an override must declare the same return type, and an override that returns ``null`` or nothing now throws a ``TypeError``.
* New property type: a subclass that declares the property again without a type is a fatal error.
* Removed property: a subclass that read it must stop.

These changes land in Mautic 8 via the *Common class type changes* work in PR #17005.

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

Conclusion
**********

Mautic Plugin developers compiled this list for other Mautic Plugin developers. If you hit a common case that isn't covered here, please contribute it.
