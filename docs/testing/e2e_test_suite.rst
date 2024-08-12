
End to end test suite
#####################

This test suite ensures that new pull requests don't break any features in Mautic and helps maintain the overall quality of the app. It uses Codeception, a popular PHP testing framework, and Selenium for browser automation.

.. vale off

Setup
**********

.. vale on

This guide assumes that your Mautic project is already installed and running on DDEV. If not, follow these steps:

1. Clone the repository:

.. code-block:: bash

    git clone <repository-url>
    cd <repository-name>

2. Start DDEV:

Ensure you have installed DDEV on your system. Start the DDEV environment with:

.. code-block:: bash

    ddev start

For detailed steps, refer to the Mautic documentation.

3. Build the test dependencies:

.. code-block:: bash

    bin/codecept build

The ``codeception.yml`` and ``tests/acceptance.suite.yml`` configurations are already in place.

.. vale off

Configuring the test environment
*********************************

.. vale on

In acceptance tests, your tests interact with the app through a web server, using the same database as the app. To avoid modifying the actual app database during tests, you should configure a separate test database. This setup ensures that the test environment doesn't affect your production data and allows for isolated testing.

Whenever you need to run the tests, make sure to update ``.env.local`` to enable test mode.

1. Edit .env.local:

Set the environment to test mode.

.. code-block:: bash

    # .env.local
    APP_ENV=test
    APP_DEBUG=1

2. Configure Test Database Credentials:

Ensure that your ``.env.test.local`` file contains the correct credentials for the test database.

.. code-block:: bash

    # .env.test.local
    DB_HOST=db
    DB_USER=db
    DB_PASSWD=db
    DB_NAME=test

Mautic uses the ``db`` database for production and ``test`` database for running tests.

.. vale off

Acceptance Tests Structure
**************************

.. vale on

All tests are located in the tests/ directory, with codeception.yml in the root directory. The tests use WebDriver and Db modules, with configurations specified in acceptance.suite.yml. 
Tests are executed in real browsers using the W3C WebDriver protocol, with Selenium managing browser interactions.

Here’s an overview of tests directory structure:

.. image:: images/e2e_test_suite.png
    :width: 300
    :alt: Tests directory structure

.. list-table::
   :header-rows: 1

   * - Directory
     - Description
   * - ``_data/``
     - Contains fixture data used in tests, including SQL dump files and sample CSV files.
   * - ``_output/``
     - Contains output from tests in case of failures. This includes snapshots of the browser in JPEG format and generated HTML reports for troubleshooting.
   * - ``_support/``
     - 
       - ``AcceptanceTester.php``: Contains login logic that runs before each test.
       - ``Helper/``: Stores custom helper functions. For example, DbHelper.php automates the process of generating SQL dump files and populating the database. It prepares the database from scratch if no dump file exists and exports a SQL file for future use.
       - ``Page/``: Stores UI locators for each page. Avoid hard-coding complex CSS or XPath locators in tests; instead, use PageObject classes.
       - ``Step/``: Contains step objects that group common functionalities for tests.
   * - ``acceptance/``
     - Contains acceptance tests.

.. vale off

Writing and Running Tests
**************************

.. vale on

Writing tests
=============

Writing tests in Codeception involves creating files within the tests/Acceptance directory. Each file contains a class with methods that define the test scenarios.

1. Create a New Test File: Use the following command to generate a new file:

.. code-block:: bash

    bin/codecept generate:cest acceptance <TestName>

This command will create a file named TestSuiteNameCest.php inside the tests/Acceptance directory.

2. Define Test Scenarios: Open the generated file and define your test scenarios. Each method within the class represents a different scenario. Use Codeception's built-in assertions and helper functions to verify the expected outcomes. Here’s a simple example:

.. code-block:: PHP

    <?php

    class TestSuiteNameCest
    {
        public function _before(AcceptanceTester $I)
        {
            // Code to run before each test
        }

        public function _after(AcceptanceTester $I)
        {
            // Code to run after each test
        }

        // Define your test methods

        public function login(AcceptanceTester $I)
        {
            $I->amOnPage('/s/login');
            $I->fillField('#username', $name);
            $I->fillField('#password', $password);
            $I->click('button[type=submit]');
            $I->see('Dashboard');
        }
    }

3. Utilize PageObjects and StepObjects:

Organize your tests by using PageObject and StepObject classes. This keeps your tests clean and maintainable by separating locators and test steps into reusable components.

- Generate PageObject with:

.. code-block:: bash

    bin/codecept generate:pageobject acceptance ExamplePage

This will create an ExamplePage.php file in /tests/Support/Page/.

- Generate step objects with:

.. code-block:: bash

    bin/codecept generate:stepobject acceptance Example

This will create an Example.php file in/tests/Support/Step/Acceptance.

Running Tests
=============

You can start tests using the run command provided by Codeception. Here are different ways to run your tests:

**Run All Tests**

.. code-block:: bash

    bin/codecept run

**Run All Acceptance Tests**

.. code-block:: bash

    bin/codecept run acceptance

**Run a Specific Test File**

If you need to run a specific test file, such as ContactManagementCest, use:

.. code-block:: bash

    bin/codecept run acceptance ContactManagementCest

**Run a Specific Test Scenario**

To execute a specific scenario within a test file, you can specify the test method like this:

.. code-block:: bash

    bin/codecept run acceptance ContactManagementCest:createContactFromForm

View Test Results
=================

After running the tests, the results will be displayed in the terminal. Additionally, any failures will generate snapshots and HTML reports in the _output directory, which you can use for debugging.

Additional Options
==================

**Print Steps:**

To see a step-by-step breakdown of the test execution, use:

.. code-block:: bash

    bin/codecept run acceptance ContactManagementCest --steps

**Verbose Output**

For more detailed internal debug information, use:

.. code-block:: bash

    bin/codecept run acceptance ContactManagementCest -vvv

View Tests in the Browser
=========================

You can watch your tests being executed in an automated browser by visiting the following URL: https://mautic.ddev.site:7900/

noVNC Access:

``Password: secret``

Contributing
************

Contributions to the test suite are welcome. Please follow the guidelines for submitting pull requests.
