Environments
############

:xref:`Symfony 4 environment conventions`

In all environments, Mautic loads the following files if they exist,
the latter taking precedence over the former:

* ``.env``                contains default values for the environment variables needed by the app
* ``.env.local``          uncommitted file with local overrides
* ``.env.$APP_ENV``       committed environment-specific defaults
* ``.env.$APP_ENV.local`` uncommitted environment-specific overrides

Real environment variables win over ``.env`` files.

.. warning:: Don't define secrets in this file, or any other committed files. Set secrets via environment variables, or through other secret management tools.

Run ``composer dump-env prod`` to compile .env files for production use (``requires symfony/flex >=1.2``).
Read more about best practices at :xref:`Symfony 4 best practices environment variables`

By default the structure come with 3 environments
``.env``
``.env.test``
``.env.test.local``

Mautic loads default values filled in the ``app/config/parameters.php`` file at installation.
These values can be overridden by the ``.env`` structure.

Development environment:
========================
``.env`` come with two values:

.. code-block:: bash

    APP_ENV=prod
    APP_DEBUG=0

It's recommended to create the ``.env.local`` file. This file overrides the values in ``.env`` file.
Example:

.. code-block:: bash

    APP_ENV=dev
    APP_DEBUG=1
    DB_HOST=...
    DB_PORT=3306
    DB_NAME=...
    DB_USER=...
    DB_PASSWD=...
    MAUTIC_DB_PREFIX=...
    MAUTIC_TABLE_PREFIX=...

Test environment:
=================

In the test environment there are two files.

The first one is the default file ``.env.test`` that includes credentials used to create a test instance of Mautic.

.. code-block:: bash

    DB_HOST=127.0.0.1
    DB_PORT=3306
    DB_NAME=mautictest
    DB_USER=root
    DB_PASSWD=
    MAUTIC_DB_PREFIX=test_
    MAUTIC_TABLE_PREFIX=test_
    MAUTIC_ENV=test
    MAUTIC_ADMIN_USERNAME=admin
    MAUTIC_ADMIN_PASSWORD=mautic

The second one, ``.env.test.local`` includes values for the DDEV local development environment, overriding the ``.env.test`` values.
It's recommended making any changes to this file with its values.

.. code-block:: bash

    DB_HOST=db
    DB_USER=db
    DB_PASSWD=db
    DB_NAME=test
    ...
    MAUTIC_DB_PREFIX=...
