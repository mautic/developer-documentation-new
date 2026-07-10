Config parameters
#################

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Use ``Mautic\CoreBundle\Helper\CoreParametersHelper`` to read Mautic's configuration parameters, including any your Plugin declares. Inject the helper into your service:

.. code-block:: php

    <?php

    use Mautic\CoreBundle\Helper\CoreParametersHelper;

    final class ExampleService
    {
        public function __construct(private CoreParametersHelper $coreParametersHelper)
        {
        }

        public function isApiEnabled(): bool
        {
            return (bool) $this->coreParametersHelper->get('helloworld_api_enabled', false);
        }
    }

Call ``get(string $name, $default = null)`` to read a single parameter with a fallback value. ``CoreParametersHelper`` also provides ``has()`` to confirm whether a parameter is set and ``all()`` to return every parameter.
