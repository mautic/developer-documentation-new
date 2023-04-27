Setup
#############

Pre-requisites
==================
It is assumed that the system already has composer and git installed and configured.

Steps
==================
1. To setup the developer environment, simply fork and clone the source from GitHub. Then Run composer install on the source.

2. Open your browser and complete the installation through the Mautic installer.
You can also execute the install process from command line: * Add a local.php file in app/config * Edit the local.php file using the following template (adapt to your own settings):

.. code-block:: php

    <?php
        $parameters = array(
            'db_driver' => 'pdo_mysql',
            'db_host' => 'localhost',
            'db_table_prefix' => null,
            'db_port' => '3306',
            'db_name' => 'mautic',
            'db_user' => 'root',
            'db_password' => 'root_password',
            'db_backup_tables' => true,
            'db_backup_prefix' => 'bak_',
    );

* Execute the following command and add your own options:
.. code-block:: bash

    php bin/console mautic:install http://your.mautic.instance