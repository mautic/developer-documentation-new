Session
#######

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

In Mautic 7, the session is part of the request. Obtain it from the current ``Request`` rather than from a ``session`` service. Inject ``Symfony\Component\HttpFoundation\RequestStack`` and call ``getSession()`` on the current request:

.. code-block:: php

    <?php

    use Symfony\Component\HttpFoundation\RequestStack;

    final class ExampleService
    {
        public function __construct(private RequestStack $requestStack)
        {
        }

        public function handleSession(): void
        {
            $session = $this->requestStack->getSession();

            // Get all session parameters
            $all = $session->all();

            // Get a specific parameter, using 'mars' as the default
            $world = $session->get('helloworld.world', 'mars');

            // Check whether a parameter exists
            if ($session->has('helloworld.world')) {
                // Do something.
            }

            // Set a session parameter
            $session->set('helloworld.world', 'mars');

            // Remove a session parameter
            $session->remove('helloworld.world');

            // Clear the whole session
            $session->clear();
        }
    }

Within a controller action, you can also type-hint ``Symfony\Component\HttpFoundation\Request`` as an argument and call ``$request->getSession()`` directly.
