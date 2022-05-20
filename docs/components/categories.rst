Categories
==========================================================

Categories are a way to organize Mautic elements.
Mautic has a ``CategoryBundle`` that you can leverage to incorporate Categories into your Plugin.

.. vale off

Adding Categories
-----------------

.. vale on

You can add Categories through your Plugin's ``config.php`` file by adding the following as a key to the returned config array:

.. code-block:: php

    <?php

    'categories' => [
        'plugin:helloWorld' => 'mautic.helloworld.world.categories'
    ]

Please prefix Category keys with ``plugin:`` as it determines permissions to manage Categories.
The ``helloWorld`` should match the permission class name.

.. vale off

Configuring Categories for Routes
---------------------------------

.. vale on

There is no need to add custom routes for Categories.
However, when generating a URL to the Plugin's Category list, use the following code:

.. code-block:: php
    
    <?php

    $categoryUrl = $router->generateUrl('mautic_category_index', ['bundle' => 'plugin:helloWorld']);

.. vale off

Including Category in Forms
---------------------------

.. vale on

To add a Category select list to a Form, use ``category`` as the Form type and pass ``bundle`` as an option:

.. code-block:: php

    <?php
    
    $builder->add('category', 'category', [
        'bundle' => 'plugin:helloWorld'
    ]);

.. vale off

Restricting Category Management
-------------------------------

.. vale on

To restrict access to Categories, use the following in the Plugin's :ref:`Permission class<security-roles-and-permissions>`.

In ``__construct()``, add ``$this->addStandardPermissions('categories');``, then in ``buildForm()``, add ``$this->addStandardFormFields('helloWorld', 'categories', $builder, $data);``.

See a code example in :ref:`Roles and Permissions<security-roles-and-permissions>`.

The two standard helper methods add the permissions of ``view``, ``edit``, ``create``, ``delete``, ``publish``, and ``full`` for Categories.
