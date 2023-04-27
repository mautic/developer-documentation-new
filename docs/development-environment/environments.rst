Environments
#############

Mautic is following the Symfony 4.4 environment conventions.
https://symfony.com/doc/4.4/configuration/environments.html

By default the structure come with 3 environments
``.env``
``.env.test``
``.env.test.local``

Mautic load default values filled in app/config/parameters.php file when the system is installed.
These values can be override by .env structure.

Development environment:
==================
``.env`` come with two values:
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
