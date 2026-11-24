Router
######

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Use the router to generate URLs from route names. In services, inject ``Symfony\Component\Routing\RouterInterface`` and call ``generate()``:

.. code-block:: php

    <?php

    use Symfony\Component\Routing\RouterInterface;
    use Symfony\Component\Routing\Generator\UrlGeneratorInterface;

    final class ExampleService
    {
        public function __construct(private RouterInterface $router)
        {
        }

        public function buildUrls(): void
        {
            // Relative URL
            $url = $this->router->generate('plugin_helloworld_admin');

            // URL with placeholders
            $url = $this->router->generate('plugin_helloworld_world', ['world' => 'mars']);

            // Absolute URL
            $absoluteUrl = $this->router->generate(
                'plugin_helloworld_admin',
                [],
                UrlGeneratorInterface::ABSOLUTE_URL
            );
        }
    }

Generating URLs in templates
****************************

Mautic 7 uses Twig templates. Use the ``path()`` and ``url()`` Twig functions instead of the router service:

.. code-block:: twig

    {# Relative path #}
    <a href="{{ path('plugin_helloworld_admin') }}">Admin</a>

    {# Absolute URL #}
    <a href="{{ url('plugin_helloworld_admin') }}">Admin</a>

The legacy PHP-template helper ``$view['router']`` no longer exists in Mautic 7.
