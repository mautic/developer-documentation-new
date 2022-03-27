Categories
==========================================================

Categories are a way to organize Mautic elements.
Mautic has a ``CategoryBundle`` that you can leverage to incorporate Categories into your Plugin.

Adding Categories
-----------------

You can add Categories through your Plugin's ``config.php`` file by adding the following as a key to the returned config array:

.. code-block:: php

    <?php

    'categories' => [
        'plugin:helloWorld' => 'mautic.helloworld.world.categories'
    ]

Please prefix Category keys with ``plugin:`` it determines permissions to manage Categories.
The ``helloWorld`` should match the permission class name.

Configuring Categories for Routes
---------------------------------

There is no need to add custom routes for Categories.
However, when generating a URL to the Plugin's Category list, use the following code:

.. code-block:: php
    
    <?php

    $categoryUrl = $router->generateUrl('mautic_category_index', ['bundle' => 'plugin:helloWorld']);

Including Category in Forms
---------------------------

To add a Category select list to a Form, use ``category`` as the Form type and pass ``bundle`` as an option:

.. code-block:: php

    <?php
    
    $builder->add('category', 'category', [
        'bundle' => 'plugin:helloWorld'
    ]);

Restricting Category Management
-------------------------------

To restrict access to Categories, use the following in the Plugin's Permission class (TODO).

In ``__construct()``, add ``$this->addStandardPermissions('categories');``, then in ``buildForm()``, add ``$this->addStandardFormFields('helloWorld', 'categories', $builder, $data);``.

See a code example in Roles and Permissions (TODO).

The two standard helper methods add the permissions of ``view``, ``edit``, ``create``, ``delete``, ``publish``, and ``full`` for Categories.
