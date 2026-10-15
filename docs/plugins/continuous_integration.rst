Continuous Integration
######################

Mautic runs several tests on every commit to ensure that the code is working as expected using :xref:`GitHub Actions`.

- :xref:`phpstan` for static analysis.
- :xref:`phpunit` for unit, functional, and integration tests.
- :xref:`codecov` for code coverage reports and ensuring that the coverage isn't decreasing.
- :xref:`rector` for additional code quality checks, for example that an unsupported Symfony or PHP syntax isn't used.
- :xref:`easy_coding_standard` for checking that there is a unified code style across the codebase.
- :xref:`twig_lint` for checking that all Twig templates are valid.

Example ``.github/workflows/tests.yml``
***************************************

This file creates the GitHub Action jobs based on the definitions in it. It checks out Mautic, places your Plugin in the ``plugins`` directory, installs Mautic and the Plugin, and then runs the same tools that Mautic uses in its own :xref:`GitHub Actions` workflow against your Plugin directory.

.. code:: yaml

   name: Mautic Plugin tests

   on:
     push:
       branches:
         - main # Main branch
         - '[0-9]+.[0-9]+'
     pull_request:

   permissions:
     contents: read

   env:
     PLUGIN_DIR: plugins/HelloWorldBundle # Same as extra.install-directory-name in composer.json

   jobs:
     phpunit:
       runs-on: ubuntu-latest

       strategy:
         matrix:
           php-versions: ['8.4'] # The supported PHP versions. Mautic requires PHP 8.4 or later.
           db-types: ['mysql:8.4'] # Database Docker images, for example ['mysql:8.4', 'mariadb:10.11']
           mautic-versions: ['8.x'] # Branches or tags of mautic/mautic to test against

       name: Tests on PHP ${{ matrix.php-versions }}, ${{ matrix.db-types }}, Mautic ${{ matrix.mautic-versions }}

       services:
         database:
           image: ${{ matrix.db-types }}
           env:
             MYSQL_ALLOW_EMPTY_PASSWORD: yes
             MYSQL_DATABASE: mautictest
           ports:
             - 3306
           options: >-
             --shm-size=2gb
             --tmpfs=/var/lib/mysql
             --health-cmd "${{ startsWith(matrix.db-types, 'mysql:') && 'mysqladmin ping' || 'healthcheck.sh --connect --innodb_initialized' }}"
             --health-interval=10s
             --health-timeout=5s
             --health-retries=3

       steps:
         - name: Checkout Mautic
           uses: actions/checkout@v7
           with:
             repository: mautic/mautic
             ref: ${{ matrix.mautic-versions }}

         - name: Checkout this Plugin
           uses: actions/checkout@v7
           with:
             path: ${{ env.PLUGIN_DIR }}

         - name: Setup PHP, with Composer and extensions
           uses: shivammathur/setup-php@v2
           with:
             php-version: ${{ matrix.php-versions }}
             extensions: mbstring, xml, ctype, iconv, intl, pdo_sqlite, mysql, pdo_mysql
             coverage: pcov
             ini-values: pcov.enabled=0, pcov.directory=., pcov.exclude="~tests|themes|vendor~", zend.assertions=1

         - name: Add MySQL config file
           run: |
             mysqldump --version
             mysqldump --print-defaults
             cp .github/ci-files/.my.cnf ~/.my.cnf
             mysqldump --print-defaults

         - name: Set SYMFONY_ENV to test
           run: |
             echo "SYMFONY_ENV=test" >> "$GITHUB_ENV"
             echo "MAUTIC_ENV=test" >> "$GITHUB_ENV"

         - name: Get Composer cache directory
           id: composer-cache
           run: echo "dir=$(composer config cache-files-dir)" >> "$GITHUB_OUTPUT"

         - name: Cache Composer dependencies
           uses: actions/cache@v6
           with:
             path: ${{ steps.composer-cache.outputs.dir }}
             key: ${{ runner.os }}-composer-${{ hashFiles('**/composer.lock') }}
             restore-keys: ${{ runner.os }}-composer-

         - name: Install Composer dependencies
           run: composer install --no-interaction --no-progress

         - name: Install Mautic
           env:
             DB_PORT: ${{ job.services.database.ports['3306'] }}
           run: |
             cp ./.github/ci-files/local.php ./app/config/local.php
             php bin/console mautic:install --force http://localhost

         - name: Install Plugins
           env:
             DB_PORT: ${{ job.services.database.ports['3306'] }}
           run: php bin/console mautic:plugins:reload --env=dev

         - name: Easy Coding Standard
           run: vendor/bin/ecs check --no-progress-bar ${{ env.PLUGIN_DIR }}

         - name: PHPStan
           env:
             APP_ENV: test
             APP_DEBUG: 1
           run: composer phpstan -- --no-progress ${{ env.PLUGIN_DIR }}

         - name: Rector
           run: |
             bin/console cache:warmup
             vendor/bin/rector process --dry-run --no-progress-bar ${{ env.PLUGIN_DIR }}

         - name: Twig Lint
           run: bin/console lint:twig ${{ env.PLUGIN_DIR }}

         - name: Run PHPUnit tests
           env:
             DB_PORT: ${{ job.services.database.ports['3306'] }}
           run: php -d zend.assertions=1 -d pcov.enabled=1 vendor/bin/phpunit -d memory_limit=2G --configuration ${{ env.PLUGIN_DIR }}/phpunit.xml --coverage-clover=${{ env.PLUGIN_DIR }}/coverage.xml --coverage-text

         - name: Coverage report
           run: cat ${{ env.PLUGIN_DIR }}/coverage.xml

         - name: Upload coverage report
           if: ${{ matrix.php-versions == '8.4' && matrix.db-types == 'mysql:8.4' && matrix.mautic-versions == '8.x' }} # Upload just once, change for your matrix
           uses: codecov/codecov-action@v7
           with:
             token: ${{ secrets.CODECOV_TOKEN }}
             files: ./coverage.xml
             fail_ci_if_error: true
             working-directory: ${{ env.PLUGIN_DIR }}
             verbose: true

         - name: Upload logs as artifacts
           if: ${{ always() }}
           uses: actions/upload-artifact@v7
           with:
             name: mautic-logs-${{ strategy.job-index }} # Artifact names must be unique across matrix jobs
             path: var/logs/

.. note::

   * Replace ``plugins/HelloWorldBundle`` with the directory of your Plugin. The same value should be in ``extra.install-directory-name`` in ``composer.json``.
   * Name your default branch ``main``, or update the ``push.branches`` list to match your default branch.
   * Update the ``matrix`` to set the PHP versions, database images, and Mautic versions that your Plugin supports. Each ``mautic-versions`` value must be a branch or tag in the ``mautic/mautic`` repository, such as ``8.x``. Mautic's own workflow tests against ``mysql:8.4``, ``mysql:9.2``, ``mariadb:10.11``, and ``mariadb:11.4``.
   * The code style, static analysis, and Rector steps use the ``ecs.php``, ``phpstan.neon``, and ``rector.php`` configuration files from the Mautic checkout, so your Plugin follows the same rules as Mautic's core code.

Once you paste this file into the ``.github/workflows/tests.yml`` file and replace the ``PLUGIN_DIR`` environmental variable, you can commit it and push it to GitHub. GitHub creates the jobs automatically, and you can see them in the Actions tab of your repository.

Adding the PHPUnit.xml file
***************************

At this point, the GitHub Action won't complete due to the missing ``phpunit.xml`` file. Create it in the root of your Plugin directory and paste the following content:

.. note::

   Mautic uses ``phpunit/phpunit`` ``^13.0``. Configure code coverage with ``<source><include>`` and ``<exclude>``, and register the Mautic test extensions with ``<extensions>``, as Mautic's own ``app/phpunit.xml.dist`` does. The relative paths in this file assume that your Plugin is in ``plugins/{PluginDirectory}`` inside a Mautic checkout.

.. code:: xml

   <?xml version="1.0" encoding="UTF-8"?>

   <!-- https://docs.phpunit.de/en/13.0/configuration.html -->
   <phpunit
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:noNamespaceSchemaLocation="../../vendor/phpunit/phpunit/phpunit.xsd"
      colors="true"
      failOnWarning="true"
      bootstrap="../../app/tests/bootstrap.php">

      <testsuites>
         <testsuite name="unit">
               <directory>Tests/Unit</directory>
         </testsuite>
         <testsuite name="functional">
               <directory>Tests/Functional</directory>
         </testsuite>
         <testsuite name="all">
               <directory>Tests/Unit</directory>
               <directory>Tests/Functional</directory>
         </testsuite>
      </testsuites>

      <php>
         <env name="KERNEL_CLASS" value="AppTestKernel" />
         <server name="KERNEL_DIR" value="app" />
         <env name="SYMFONY_DEPRECATIONS_HELPER" value="weak" />
         <const name="IS_PHPUNIT" value="true" />
         <const name="MAUTIC_ENV" value="test" />
         <server name="APP_DEBUG" value="0" />
         <server name="APP_ENV" value="test" force="true" />
      </php>

      <source>
         <include>
               <directory>.</directory>
         </include>
         <exclude>
               <directory>Assets</directory>
               <directory>Config</directory>
               <directory>Tests</directory>
               <directory>Translations</directory>
               <directory>Views</directory>
               <directory>vendor</directory>
         </exclude>
      </source>

      <extensions>
         <bootstrap class="\Mautic\CoreBundle\Test\Extensions\SeparateProcess\SeparateProcess" />
         <bootstrap class="\Mautic\CoreBundle\Test\Extensions\DbPrefix\DbPrefix" />
      </extensions>

   </phpunit>

.. note::

   Update the ``testsuite`` directories if you don't have this structure.

Setting up Codecov
******************

At this point the checks should do their thing and point out all issues in your Plugin code. Once you fix them all you should find out that the Codecov report isn't uploading correctly. Here is how to make it work:

1. You must enable the :xref:`codecov_gh_app` for your repository to upload the coverage report.
2. The app provides you with an API key. Paste it into the secret variables as ``CODECOV_TOKEN`` in the GitHub repository settings.
3. Since the Plugin isn't in the root directory then you must tell it how to map the files from the report with the files in the repository. To do that, you need to create a ``codecov.yml`` file in the root of your Plugin directory and paste the following content:

.. code:: yaml

   codecov:
      disable_default_path_fixes: true
   fixes:
      - "/home/runner/work/plugin-helloworld/plugin-helloworld/plugins/HelloWorldBundle/::"

.. note::
   Update the path to match your Plugin repository. The safest way is to view the paths in the ``Coverage report`` step where Codecov prints the coverage XML before it's sent to Codecov.
