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
