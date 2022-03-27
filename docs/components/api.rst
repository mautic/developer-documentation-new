API
==========================================================

To add custom API endpoints, simply define the routes under the API firewall in the :doc:`Plugin's config file</plugins/config>`.
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
