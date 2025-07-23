API
###

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
                        'mautic.security',
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

----

.. vale off

API-aware entity locking
****************************

.. vale on

Mautic supports locking for API-editable entities, such as Emails, to prevent overwriting changes while a user is actively editing the entity in the UI.

This is useful when:

- You want the API to respect the locking behavior already in place in the UI.
- You want to return a `409 Conflict` when a record is locked.

.. vale off

Enable API lock for a model
============================

.. vale on

To make an entity model API-lock-aware:

1. Implement the interface:

.. code-block:: php

    use Mautic\ApiBundle\Model\ApiLockAwareInterface;

    class MyEntityModel implements ApiLockAwareInterface
    {
        // ...
    }

2. Use the trait to reuse locking logic:

.. code-block:: php

    use Mautic\ApiBundle\Model\ApiEntityLockTrait;

    class MyEntityModel implements ApiLockAwareInterface
    {
        use ApiEntityLockTrait;

        // Optional: Override `isApiLocked()` if you need custom behavior
    }

This ensures your model will be checked by the API when editing.

Behind the scenes, the API controller checks:

.. code-block:: php

    if ($this->model instanceof ApiLockAwareInterface && $this->model->isApiLocked($entity)) {
        ....
    }

.. vale off

Error message
=============

.. vale on

When an entity is locked, the API returns:

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
