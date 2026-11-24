Config parameters
#################

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

Call ``get(string $name, $default = null)`` to read a single parameter with a fallback value. ``CoreParametersHelper`` also provides ``has()`` to confirm whether a parameter exists and ``all()`` to return every parameter.
