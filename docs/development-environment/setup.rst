How to install Mautic manually
##############################

Pre-requisites to setup
=======================

Mautic assumed that the system already has ``composer`` and ``git`` installed and configured.

.. note:: 
    If you get stuck, join the lively Mautic Community on :xref:`Mautic Slack` or the :xref:`Developer Forum` for support and answers. **Please first post in the forum**, then share the link in Slack, so others can learn from your question.

Steps
=====
1. To setup the developer environment, fork and clone the source from GitHub as outlined in :doc:`/development-environment/how_to_install_with_ddev`. 
2. Run ``composer install`` on the source.
3. Open your browser and complete the installation through the Mautic installer.

You can also run the install process from command line:

* Add a ``local.php`` file in ``app/config``
* Edit the ``local.php`` file using the following template (Mautic adapts to new local settings):

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

* Run the following command and add your own options:

.. code-block:: bash

    php bin/console mautic:install https://mautic.example.com