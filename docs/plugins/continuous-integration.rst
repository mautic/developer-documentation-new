Continuous Integration
######################

Mautic runs several tests on every commit to ensure that the code is working as expected using :xref:`GitHub Actions`.

- :xref:`phpstan` for static analysis.
- :xref:`phpunit` for unit, functional and integration tests.
- :xref:`codecov` for code coverage reports and ensuring that the coverage isn't decreasing.
- :xref:`rector` for additional code quality checks, for example that an unsupported Symfony or PHP syntax isn't used.
- :xref:`php_cs_fixer` for checking that the code style is unified across the codebase.
- :xref:`twig_lint` Checker for checking that all Twig templates are valid.

Example ``.github/workflows/tests.yml``
***************************************

This file creates the GitHub Action jobs based on the definitions in it. You can find a live example of this file and how this works in the :xref:`hello_world_plugin`.

.. code:: yaml

   name: Mautic Plugin tests

   on:
   push:
      branches:
         - main # Main branch
         - '[0-9]+\.[0-9]+'
   pull_request:

   env:
   PLUGIN_DIR: plugins/HelloWorldBundle # Same as extra.install-directory-name in composer.json

   jobs:
   phpunit:
      runs-on: ubuntu-latest
      
      strategy:
         matrix:
         php-versions: ['7.4', '8.0'] # The supported PHP versions
         db-types: ['mysql'] # can be: ['mysql', 'mariadb'] but not necessary for this plugin that does not add any DB schema
         mautic-versions: ['4.3', '4.4'] # The supported Mautic versions
   
      name: Tests on PHP ${{ matrix.php-versions }}, ${{ matrix.db-types }}, Mautic ${{ matrix.mautic-versions }}

      services:
         database:
         image: ${{ matrix.db-types == 'mysql' && 'mysql:5.7' || 'mariadb:10.3' }}
         env:
            MYSQL_ALLOW_EMPTY_PASSWORD: yes
            MYSQL_DATABASE: mautictest
         ports:
            - 3306
         options: >-
            --shm-size=2gb
            --name=${{ matrix.db-types }}
            --tmpfs=/var/lib/mysql
            --health-cmd="mysqladmin ping" 
            --health-interval=10s 
            --health-timeout=5s 
            --health-retries=3

      steps:
      - name: Checkout Mautic 4
         uses: actions/checkout@v3
         with:
         repository: mautic/mautic
         ref: ${{ matrix.mautic-versions }}

      - name: Checkout this plugin
         uses: actions/checkout@v3
         with:
         path: ${{ env.PLUGIN_DIR }}

      - name: Setup PHP, with composer and extensions
         uses: shivammathur/setup-php@v2
         with:
         php-version: ${{ matrix.php-versions }}
         ini-values: -dpcov.enabled=0, pcov.directory=."
         extensions: mbstring, xml, ctype, iconv, intl, pdo_sqlite, mysql, pdo_mysql
         coverage: pcov

      - name: add MySQL config file
         run: |
         mysqldump --version
         mysqldump --print-defaults
         cp .github/ci-files/.my.cnf ~/.my.cnf
         mysqldump --print-defaults

      - name: Set SYMFONY_ENV to test
         run: |
         echo "SYMFONY_ENV=test" >> $GITHUB_ENV
         echo "MAUTIC_ENV=test" >> $GITHUB_ENV

      - name: Get composer cache directory
         id: composer-cache
         run: echo "dir=$(composer config cache-files-dir)" >> $GITHUB_OUTPUT

      - name: Cache composer dependencies
         uses: actions/cache@v3
         with:
         path: ${{ steps.composer-cache.outputs.dir }}
         key: ${{ runner.os }}-composer-${{ hashFiles('**/composer.lock') }}
         restore-keys: ${{ runner.os }}-composer-

      - name: Install Composer dependencies
         run: composer install

      - name: Install Mautic
         env:
         DB_PORT: ${{ job.services.database.ports[3306] }}
         run: |
         cp ./.github/ci-files/local.php ./app/config/local.php
         php bin/console mautic:install --force http://localhost

      - name: Install Plugins
         env:
         DB_PORT: ${{ job.services.database.ports[3306] }}
         run: php bin/console mautic:plugins:install --env=dev
      
      - name: Run Code Style check
         run: bin/php-cs-fixer fix ${{ env.PLUGIN_DIR }} --config=.php-cs-fixer.php -v --dry-run --show-progress=dots --diff
      
      - name: PHPSTAN
         run: composer phpstan -- ${{ env.PLUGIN_DIR }}

      - name: Rector
         run: composer rector -- --dry-run --no-progress-bar ${{ env.PLUGIN_DIR }}

      - name: Twig Lint
         run: bin/console lint:twig ${{ env.PLUGIN_DIR }}
      
      - name: Run PHPUNIT tests
         env:
         DB_PORT: ${{ job.services.database.ports[3306] }}
         run: XDEBUG_MODE=coverage APP_DEBUG=0 php -dpcov.enabled=1 -dpcov.directory=. -dpcov.exclude="~tests|themes|vendor~" bin/phpunit -d memory_limit=1G --bootstrap vendor/autoload.php --configuration ${{ env.PLUGIN_DIR }}/phpunit.xml --coverage-clover=${{ env.PLUGIN_DIR }}/coverage.xml --coverage-text

      - name: Coverage report
         run: cat ${{ env.PLUGIN_DIR }}/coverage.xml

      - name: Upload coverage report
         if: ${{ matrix.php-versions == '8.0' && matrix.db-types == 'mysql' && matrix.mautic-versions == '4.4' }} # upload just once, change for your matrix
         uses: codecov/codecov-action@v3
         with:
         token: ${{ secrets.CODECOV_TOKEN }}
         fail_ci_if_error: true
         working-directory: ${{ env.PLUGIN_DIR }}
         verbose: true
      
      - name: Upload logs as artifacts
         uses: actions/upload-artifact@v3
         with:
         name: mautic-logs
         path: var/logs/

.. note::
   Replace ``plugins/HelloWorldBundle`` with the directory of your Plugin. The same value should be in ``extra.install-directory-name`` in ``composer.json``.
   Make sure that you name your default branch `main` and if not, update it in the file.
   Also update the ``matrix`` to set the supported PHP and Mautic versions. Also, if you want to run the tests on MySql, MariaDB, or both.

Once you paste this file into the ``.github/workflows/tests.yml`` file and replace the ``PLUGIN_DIR`` environmental variable, you can commit it and push it to GitHub. GitHub will create the jobs automatically, and you can see them in the Actions tab of your repository.

At this point, the GitHub Action won't complete due to the missing ``phpunit.xml`` file. Create it in the root of your Plugin directory and paste the following content:

.. code:: xml

   <?xml version="1.0" encoding="UTF-8"?>

   <!-- http://www.phpunit.de/manual/current/en/appendixes.configuration.html -->
   <phpunit
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:noNamespaceSchemaLocation="https://schema.phpunit.de/8.5/phpunit.xsd"
      colors                      = "true"
      failOnWarning               = "true"
      bootstrap                   = "autoload.php" >

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
      </php>

      <filter>
         <whitelist>
               <directory>*</directory>
               <exclude>
                  <directory>Assets</directory>
                  <directory>Config</directory>
                  <directory>Tests</directory>
                  <directory>Translations</directory>
                  <directory>Views</directory>
               </exclude>
         </whitelist>
      </filter>

      <listeners>
         <listener class="\Symfony\Bridge\PhpUnit\SymfonyTestsListener" />
         <listener class="\Mautic\CoreBundle\Test\Listeners\CleanupListener" />
      </listeners>

   </phpunit>

.. note::
   Update the ``testsuite`` directories if you don't have this structure.

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
