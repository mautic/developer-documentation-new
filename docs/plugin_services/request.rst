Request
#######

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Inject ``Symfony\Component\HttpFoundation\RequestStack`` and call ``getCurrentRequest()`` to access the current request:

.. code-block:: php

    <?php

    use Symfony\Component\HttpFoundation\RequestStack;

    final class ExampleService
    {
        public function __construct(private RequestStack $requestStack)
        {
        }

        public function readRequest(): void
        {
            $request = $this->requestStack->getCurrentRequest();

            // $_GET
            $get = $request->query->all();

            // $_POST
            $post = $request->request->all();

            // $_COOKIE
            $cookies = $request->cookies->all();

            // $_SERVER
            $server = $request->server->all();

            // Headers
            $headers = $request->headers->all();

            // Attributes - custom parameters
            $attributes = $request->attributes->all();

            // Check whether a parameter exists
            if ($request->request->has('hello')) {
                // Do something.
            }

            // Retrieve the value of a specific parameter, using 'mars' as the default
            $world = $request->query->get('world', 'mars');

            // Set a custom request value
            $request->attributes->set('hello', 'world');
        }
    }

Within a controller action, you can also type-hint ``Symfony\Component\HttpFoundation\Request`` as an argument and Symfony injects the current request automatically.
