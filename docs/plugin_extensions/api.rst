API
###

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

To add custom API endpoints, define the routes under the API firewall in the :doc:`Plugin's config file</plugins/config>`.
This places the route behind ``/api`` which is only accessible to authorized Users.

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/Config/config.php

    declare(strict_types=1);

    return [
        // ...

        'services' => [

            // ...

            'controllers' => [
                'plugin.hello_world.controller.api' => [
                    'class' => \MauticPlugin\HelloWorldBundle\Controller\ApiController::class,
                    'arguments' => [
                        \Mautic\CoreBundle\Security\Permissions\CorePermissions::class,
                        'plugin.hello_world.model.worlds'
                    ],
                    'methodCalls' => [
                        'setContainer' => [
                            '@service_container',
                        ],
                    ],
                ],
            ],
        ],

        'routes'   => [

            // ...

            'api' => [
                'plugin_helloworld_api' => [
                    'path'       => '/hello/worlds',
                    'controller' => 'HelloWorldBundle:Api:worlds',
                    'method'     => 'GET'
                ]
            ]
        ],

        // ...
    ];

The API controller should extend ``Mautic\ApiBundle\Controller\CommonApiController`` to leverage the helper methods provided.

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/Controller/ApiController.php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\Controller;

    use Mautic\ApiBundle\Controller\CommonApiController;
    use Mautic\CoreBundle\Security\Permissions\CorePermissions;
    use MauticPlugin\HelloWorldBundle\Model\WorldsModel;
    use Symfony\Component\HttpFoundation\Request;
    use Symfony\Component\HttpFoundation\Response;

    class ApiController extends CommonApiController
    {
        private CorePermissions $corePermissions;
        private WorldsModel     $worldsModel;

        public function __construct(CorePermissions $corePermissions, WorldsModel $worldsModel)
        {
            $this->corePermissions = $corePermissions;
            $this->worldsModel     = $worldsModel;
        }
        
        /**
        * Get a list of worlds
        */
        public function getWorldsAction(Request $request): Response
        {
            if (!$this->corePermissions->isGranted('plugin:helloWorld:worlds:view')) {
                return $this->accessDenied();
            }

            $filter  = $request->query->get('filter', null);
            $limit   = $request->query->get('limit', null);
            $start   = $request->query->get('start', null);

            $worlds  = $this->model->getWorlds($filter, $limit, $start);
            $worlds  = $this->view($worlds, 200);

            return $this->handleView($worlds);
        }
    }

.. vale off

API-aware entity locking
************************

.. vale on

Mautic supports locking for API-editable entities, such as Emails, to prevent overwriting changes while a User is actively editing the entity in the UI.

This is useful to:

* Ensure the API respects the locking behavior already in place in the UI.
* Return a ``409 Conflict`` when the system locks a record.

.. vale off

Enable API lock for a model
===========================

.. vale on

To make an entity model API-lock-aware:

#. Implement the interface:

   .. code-block:: php

      use Mautic\ApiBundle\Model\ApiLockAwareInterface;

      class MyEntityModel implements ApiLockAwareInterface
      {
         // ...
      }

#. Use the trait to reuse locking logic:

   .. code-block:: php

      use Mautic\ApiBundle\Model\ApiEntityLockTrait;

      class MyEntityModel implements ApiLockAwareInterface
      {
          use ApiEntityLockTrait;

          // Optional: Override `isApiLocked()` if you need custom behavior
      }

This ensures the API checks your model during editing.

Behind the scenes, the API controller validates:

.. code-block:: php

    if ($this->model instanceof ApiLockAwareInterface && $this->model->isApiLocked($entity)) {
        ....
    }

.. vale off

Error message
=============

.. vale on

If the API detects a locked entity, it returns:

.. code-block:: json

    {
      "errors": [
        {
          "message": "{Entity} is currently checked out by {User} (on {Date} at {Time}).",
          "code": 409,
          "details": {
            "checkedOutBy": "{User}",
            "checkedOut": "{Date} {Time}"
          }
        }
      ]
    }

This format helps client apps identify locked records and avoid overwriting.

.. vale off

API permission-context event
****************************

.. vale on

Mautic dispatches this event immediately before API Platform v2 evaluates authorization, letting a subscriber rewrite the permission, the request object, or both.

It fires from both API Platform authorization paths:

* The deny-access listener - ``MauticDenyAccessListener::checkSecurity()``
* The permission voter - ``ApiPermissionVoter::voteOnAttribute()``

After dispatch, Mautic re-reads ``getPermission()`` and ``getRequestObject()``, then runs the ownership or ``isGranted()`` authorization against them.

A Plugin uses this event to resolve dynamic permissions that contain placeholders. For example, the Custom Objects Plugin resolves ``custom_objects:[customObject]:viewown`` or the object-path-derived ownership context ``custom_objects:custom_fields:viewown(getCustomField)`` into a concrete permission and subject at runtime.

The event is additive and non-breaking, so existing permission checks keep working unchanged.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Event constant
     - Description
   * - ``ApiEvents::API_PLATFORM_PERMISSION_CONTEXT``
     - Mautic dispatches this before API Platform evaluates authorization. The event string is ``mautic.api_platform_permission_context``.

The event receives a ``Mautic\ApiBundle\Event\ApiPlatformPermissionContextEvent`` instance with the following methods:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Method
     - Description
   * - ``getSecurityExpression()``
     - Returns the raw security expression the API Platform operation declares. On the permission-voter path, this matches the value passed as the permission attribute.
   * - ``getPermission()``
     - Returns the permission string extracted from the security expression. Mautic re-reads this after the event to authorize.
   * - ``setPermission()``
     - Sets the permission string Mautic authorizes against.
   * - ``getRequestObject()``
     - Returns the request object Mautic authorizes against.
   * - ``setRequestObject()``
     - Sets the request object Mautic runs the ownership or ``isGranted()`` authorization against.
   * - ``getRequest()``
     - Returns the current Symfony ``Request``, or ``null``. It's ``null`` when the permission voter dispatches the event.
   * - ``getAttributes()``
     - Returns the operation attributes array. It's empty when the permission voter dispatches the event.

.. note::

   Mautic populates ``getRequest()`` and ``getAttributes()`` only on the deny-access listener path. On the permission-voter path, the request is ``null`` and the attributes are empty. Because a subscriber can't always tell which path dispatched the event, guard for a ``null`` request and empty attributes before you rely on them.

Example subscriber
==================

.. code-block:: php

    <?php
    // plugins/CustomObjectsBundle/EventListener/ApiPermissionContextSubscriber.php

    declare(strict_types=1);

    namespace MauticPlugin\CustomObjectsBundle\EventListener;

    use Mautic\ApiBundle\ApiEvents;
    use Mautic\ApiBundle\Event\ApiPlatformPermissionContextEvent;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    final class ApiPermissionContextSubscriber implements EventSubscriberInterface
    {
        public static function getSubscribedEvents(): array
        {
            return [
                ApiEvents::API_PLATFORM_PERMISSION_CONTEXT => ['onPermissionContext', 0],
            ];
        }

        public function onPermissionContext(ApiPlatformPermissionContextEvent $event): void
        {
            $permission = $event->getPermission();

            // Only act on Custom Objects permissions that still contain a placeholder.
            if (!str_contains($permission, 'custom_objects:[customObject]:')) {
                return;
            }

            // Resolve the `[customObject]` placeholder to the concrete Custom Object
            // alias for the current request. Real resolution reads the object from
            // the request object or route parameters.
            $requestObject = $event->getRequestObject();
            $customObjectAlias = $this->resolveCustomObjectAlias($requestObject);

            $resolvedPermission = str_replace(
                'custom_objects:[customObject]:',
                sprintf('custom_objects:%s:', $customObjectAlias),
                $permission
            );

            $event->setPermission($resolvedPermission);

            // Narrow the ownership check to the resolved Custom Object entity.
            $resolvedSubject = $this->resolveCustomObject($requestObject);
            $event->setRequestObject($resolvedSubject);
        }

        private function resolveCustomObjectAlias(mixed $requestObject): string
        {
            // Illustrative: derive the Custom Object alias from the subject.
            return 'my_custom_object';
        }

        private function resolveCustomObject(mixed $requestObject): object
        {
            // Illustrative: load the concrete Custom Object entity for the subject.
            return new \stdClass();
        }
    }
