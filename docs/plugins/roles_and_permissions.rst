Roles and Permissions
###################

Mautic lets you define custom permissions for each Role. These permissions determine what Users can view or do within different parts of the system.

How Permissions Work
--------------------

Mautic assigns permissions using bit values. These bits double as they increase:

``1, 2, 4, 8, 16, 32, 64, 128...``

Bits should always follow this sequence. Avoid values like ``3`` or ``5`` because permission checks will fail.

Example permission set:

+--------------+-----+
| Permission   | Bit |
+--------------+-----+
| view         | 1   |
| edit         | 2   |
| create       | 4   |
| delete       | 8   |
| full         | 16  |
+--------------+-----+

A permission notation looks like this:

``plugin:helloWorld:worlds:view``

This checks the ``view`` permission for the ``worlds`` level of the plugin.

How Bit Storage Works
~~~~~~~~~~~~~~~~~~~~~

Mautic stores permissions by adding the bits of all permissions assigned to a Role.

Examples:

* ``view`` + ``edit`` = ``1 + 2 = 3``
* ``view`` + ``create`` = ``1 + 4 = 5``

When checking a permission, Mautic verifies whether the bit exists within the stored sum.

The ``full`` permission should always use the highest bit. It automatically grants all lower permissions.

Using Permissions
-----------------

Use the Security service to check permissions.

Example in Twig:

.. code-block:: twig

   {% if security.isGranted('user:roles:edit') %}
       {# User can edit roles #}
   {% endif %}

Permission notation:

* Core bundles: ``bundle:level:permission``
* Plugins: ``plugin:bundle:level:permission``

Example:

``user:roles:view``

Creating Custom Permissions
---------------------------

Plugins can define their own Permission classes.

Each Permission class must:

* Extend ``Mautic\CoreBundle\Security\Permissions\AbstractPermissions``
* Implement ``__construct()``
* Implement ``buildForm()``
* Implement ``getName()``

Constructor
~~~~~~~~~~~

Inside ``__construct()``:

1. Call ``parent::__construct($params)`` or assign ``$this->params = $params``.
2. Define ``$this->permissions`` as an array of permission levels and bits.

Example level definition:

* Level: ``worlds``
* Permissions: ``use_telescope``, ``send_probe``, ``visit``, ``full``

Access check example:

``plugin:helloWorld:worlds:send_probe``

Helper Methods for Permission Sets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mautic includes helper methods:

* ``addStandardPermissions()`` adds view, edit, create, delete, publish, full
* ``addExtendedPermissions()`` adds creator-based permissions
* ``addManagePermission()`` adds a single manage permission

buildForm()
~~~~~~~~~~~

``buildForm()`` adds permission fields to the Role form.

Available helpers:

* ``addStandardFormFields()``
* ``addExtendedFormFields()``
* ``addManageFormFields()``

getName()
~~~~~~~~~

This must return the bundle name in camelCase.

Example:

* Bundle: ``HelloWorldBundle``
* Method return value: ``helloWorld``
* File name: ``HelloWorldPermissions.php``

Permission Aliases
------------------

Use ``getSynonym()`` to map a permission name to another one.

Example:

``editown`` maps to ``edit`` if ``editown`` is not defined.

Analyzing Permissions Before Saving
-----------------------------------

Plugins can adjust permissions before saving.

Use:

``analyzePermissions()``

If a second pass is needed, return ``true``.  
The next call will include ``$isSecondRound = true``.

Advanced Permission Checks
--------------------------

To override bit-based checking, extend:

``isGranted($userPermissions, $name, $level)``

Advanced Support Logic
----------------------

You can customize support checks by overriding:

``isSupported()``

Use this for backward compatibility or custom permission rules.