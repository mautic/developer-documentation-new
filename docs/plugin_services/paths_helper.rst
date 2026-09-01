Paths helper
############

.. vale off

The Paths helper resolves filesystem paths for Mautic's system locations - images, themes, cache, logs, and temporary files - so your Plugin can read from and write to the right directory without hardcoding the directory structure.

.. vale on

Using the helper
****************

Inject ``Mautic\CoreBundle\Helper\PathsHelper`` into your service, or retrieve the ``mautic.helper.paths`` service from the container in legacy code.

.. code-block:: php

   <?php

   use Mautic\CoreBundle\Helper\PathsHelper;

   final class ExampleService
   {
       public function __construct(private PathsHelper $pathsHelper)
       {
       }

       public function locateImages(): void
       {
           // Relative path, for example "media/images"
           $relativeImagesDir = $this->pathsHelper->getSystemPath('images');

           // Absolute path, for example "/home/user/public_html/media/images"
           $absoluteImagesDir = $this->pathsHelper->getSystemPath('images', true);
       }
   }

* Service name: ``mautic.helper.paths``
* Class: ``Mautic\CoreBundle\Helper\PathsHelper``

Retrieving system paths
***********************

Call ``getSystemPath(string $name, bool $fullPath = false)`` to resolve a system location. By default, it returns a path relative to the Mautic root. Pass ``true`` as the second argument to get the absolute path instead. The ``cache``, ``logs``, and ``temporary`` locations are always absolute, regardless of the ``$fullPath`` argument.

Commonly used names include:

* ``images``: the media images directory.
* ``themes``: the Themes directory.
* ``assets``: the uploaded Assets directory.
* ``cache``: the kernel cache directory - always absolute.
* ``logs``: the kernel logs directory - always absolute.
* ``temporary`` or ``tmp``: a directory for temporary files - always absolute.

Passing a name that Mautic doesn't recognize throws an ``\InvalidArgumentException``.

.. tip::

   Use the ``temporary`` or ``tmp`` name when your Plugin needs to store temporary files. Reserve the ``cache`` location for cached data so your temporary files don't collide with Mautic's cache.
