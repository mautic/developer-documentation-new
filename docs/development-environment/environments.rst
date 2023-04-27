Environments
#############

Mautic is following the Symfony 4.4 environment conventions.
https://symfony.com/doc/4.4/configuration/environments.html

In all environments, the following files are loaded if they exist,
the latter taking precedence over the former:

* .env                contains default values for the environment variables needed by the app
* .env.local          uncommitted file with local overrides
* .env.$APP_ENV       committed environment-specific defaults
* .env.$APP_ENV.local uncommitted environment-specific overrides

Real environment variables win over .env files.

.. warning:: DO NOT DEFINE PRODUCTION SECRETS IN THIS FILE NOR IN ANY OTHER COMMITTED FILES.

.. warning:: All secrets should be set via environment variables or through other secret management.


Run "composer dump-env prod" to compile .env files for production use (requires symfony/flex >=1.2).
https://symfony.com/doc/current/best_practices.html#use-environment-variables-for-infrastructure-configuration

By default the structure come with 3 environments
``.env``
``.env.test``
``.env.test.local``

Mautic load default values filled in app/config/parameters.php file when the system is installed.
These values can be override by .env structure.

Development environment:
==================
``.env`` come with two values:

.. code-block:: env

    APP_ENV=prod
    APP_DEBUG=0

We recommend to create the ``.env.local``, this file will override the values in ``.env`` file.
Example:

.. code-block:: env

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
==================

In test environment we come with two files.

First one is default file ``.env.test`` that come with parameters to github deploy.

.. code-block:: env

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

Second one, ``.env.test.local`` come with values to ddev test environment overriding ``.env.test`` vales .
We recommend that any changes be made to this file with its values.

.. code-block:: env

    DB_HOST=db
    DB_USER=db
    DB_PASSWD=db
    DB_NAME=test
    ...
    MAUTIC_DB_PREFIX=...
