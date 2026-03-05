Roles and permissions
#####################

Mautic defines custom Role permissions through Permission objects.

How permissions work
********************

Mautic calculates permissions based on bits assigned to a Plugin level and permission. Bits are integers that increase by doubling the value - 1, 2, 4, 8, 16, 32, 64, 128, 512, 1024, and so forth. Avoid assigning numbers in between, such as 3 or 5, because the permission won't calculate correctly.

For example, if ``HelloWorldBundle`` manages access to a ``worlds`` entity, the permission set for ``plugin:helloWorld:worlds`` resembles this setup:

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Permission
     - Bit
   * - view
     - 1
   * - edit
     - 2
   * - create
     - 4
   * - delete
     - 8
   * - full
     - 16

.. note::

   The notation ``plugin:helloWorld:worlds:view`` typically requests permission in Mautic. This notation tells Mautic to verify the ``view`` permission for the Plugin ``HelloWorldBundle`` at the ``worlds`` level. Levels allow Plugins to set permissions for multiple areas.

Mautic sums the bits for the permissions granted to a Role and stores the result in the database. For example, if a Role has ``view`` and ``edit`` access, the stored bit is 3. If given ``view`` and ``create`` access, the stored bit is 5.

When permission verification is necessary - for instance ``plugin:helloWorld:worlds:create`` - Mautic verifies if the Role's generated bit for ``plugin:helloWorld:worlds`` includes bit 4. If so, Mautic grants permission.

.. note::

   The ``full`` permission grants access to all prior permissions and should always be the highest bit.

Using permissions
*****************

.. code-block:: php

   <?php

   $security = $this->get('mautic.security');

   // Check if user is granted a single permission
   if ($security->isGranted('plugin:helloWorld:worlds:view')) {
       // do something
   }

   // Check if user is granted multiple permissions (must be granted to all to be true)
   if ($security->isGranted(
       array(
           'plugin:helloWorld:worlds:view',
           'plugin:helloWorld:worlds:create',
       )
   )) {
       // do something
   }

   // Check if user is granted to at least one permission
   if ($security->isGranted(
       array(
           'plugin:helloWorld:worlds:view',
           'plugin:helloWorld:worlds:edit',
       ),
       'MATCH_ONE'
   )) {
       // do something
   }

   // Get an array of user permissions
   $permissions = $security->isGranted(
       array(
           'plugin:helloWorld:worlds:view',
           'plugin:helloWorld:worlds:edit',
       ),
       'RETURN_ARRAY'
   );

   if ($permissions['plugin:helloWorld:worlds:view']) {
       // do something
   }

   // Check if user has access to view leads
   if ($security->isGranted('lead:leads:viewother')) {
       // do something
   }

To determine if a User has a specific permission, use the Mautic security service, which you can obtain from the ``mautic.security`` service.

Mautic uses specific notation to identify permissions:

* **Core bundles**: use the format ``bundleName:permissionLevel:permission``.
* **Plugins**: append the ``plugin:`` prefix. For example, ``plugin:bundleName:permissionLevel:permission``. Plugins require this prefix because it directs Mautic to search for the permission class within the ``plugins/`` directory and the ``MauticPlugin`` namespace.

Core bundles or Plugins set the permission level and permissions. For example, the core UserBundle has ``users`` and ``roles`` levels with ``view``, ``edit``, ``create``, ``delete``, and ``full`` permissions for each. To verify if a User has permission to edit Roles, use:

.. code-block:: php

   $security->isGranted('user:roles:edit');

Creating custom permissions
***************************

A Plugin creates its own set of permissions by defining a Permission class. Each permission class must extend ``Mautic\CoreBundle\Security\Permissions\AbstractPermissions``.

.. code-block:: php

   <?php
   // plugins/HelloWorldBundle/Security/Permissions/HelloWorldPermissions.php

   namespace MauticPlugin\HelloWorldBundle\Security\Permissions;

   use Symfony\Component\Form\FormBuilderInterface;
   use Mautic\CoreBundle\Security\Permissions\AbstractPermissions;

   class HelloWorldPermissions extends AbstractPermissions
   {
       public function __construct($params)
       {
           parent::__construct($params);

           $this->permissions = array(
               'worlds' => array(
                   'use_telescope' => 1,
                   'send_probe'    => 2,
                   'visit'         => 4,
                   'full'          => 1024
               )
           );

           // Add standard category permissions
           $this->addStandardPermissions('categories');
       }

       public function buildForm(FormBuilderInterface &$builder, array $options, array $data)
       {
           // Add standard category form fields
           $this->addStandardFormFields('helloWorld', 'categories', $builder, $data);

           // Add custom 'worlds' level form fields
           $builder->add(
               'helloWorld:worlds',
               'permissionlist',
               array(
                   'choices' => array(
                       'use_telescope' => 'plugin.helloworld.permissions.use_telescope',
                       'send_probe'    => 'plugin.helloworld.permissions.send_probe',
                       'visit'         => 'plugin.helloworld.permissions.visit',
                       'full'          => 'mautic.core.permissions.full',
                   ),
                   'label' => 'plugin.helloworld.permissions',
                   'data'  => (!empty($data['worlds']) ? $data['worlds'] : array()),
                   'bundle' => 'helloWorld',
                   'level'  => 'worlds'
               )
           );
       }

       public function getName()
       {
           return 'helloWorld';
       }
   }

Most permission classes require three methods: ``__construct()``, ``buildForm()``, and ``getName()``.

``__construct()``
=================

The constructor performs two tasks. It calls ``parent::__construct($params)`` or sets ``$this->params = $params;``. It then defines the ``$this->permissions`` array. This array organizes permissions into levels, where each level contains specific permissions assigned to bits.

For example, in the code sample, a custom level of ``worlds`` includes ``use_telescope``, ``send_probe``, ``visit``, and ``full``. To verify if a User has the ``send_probe`` permission for the ``worlds`` level, use:

.. code-block:: php

   $mauticSecurity->isGranted('plugin:helloWorld:worlds:send_probe');

Mautic provides helper methods for common permission sets:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Method
     - Description
   * - ``addStandardPermissions()``
     - Sets ``view``, ``edit``, ``create``, ``delete``, ``publish`` - with an option to exclude - and ``full`` permissions.
   * - ``addExtendedPermissions()``
     - Sets creator-level restrictions - ``viewown``, ``viewother``, ``editown``, ``editother``, ``create``, ``deleteown``, ``deleteother``, ``publishown``, ``publishother``, and ``full``.
   * - ``addManagePermission()``
     - Sets a single ``manage`` permission.

``buildForm()``
===============

.. vale off

The ``buildForm()`` method appends permission toggles to the Role's Form. See :doc:`/plugin_extensions/forms` for details on Form builders and review the comments in the code sample for implementation details.

.. vale on

Mautic provides complementary helper methods for common permission sets:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Method
     - Description
   * - ``addStandardFormFields()``
     - Appends the standard permission sets to the Form.
   * - ``addExtendedFormFields()``
     - Appends the extended - creator restricted - permissions to the Form.
   * - ``addManageFormFields()``
     - Appends the single manager element to the Form.

``getName()``
=============

This method is mandatory. The return value must match the ``bundleName`` and the filename. For example, if the bundle name is ``HelloWorldBundle``, this method returns ``helloWorld`` and the file is ``HelloWorldPermissions.php``.

Permission aliases
******************

.. code-block:: php

   <?php

   protected function getSynonym($name, $level)
   {
       if ($name == 'send_satellite') {
           $name = 'send_probe';
       }

       return array($name, $level);
   }

To add a permission alias, use the ``getSynonym()`` method. Mautic calls this method before determining each requested permission, giving an opportunity to change the permission level or name as needed.

For example, ``parent::getSynonym()`` recognizes ``editown`` as ``edit`` if the ``$this->permissions`` property for that level doesn't define ``editown``.

Manipulating permissions before saving
**************************************

.. code-block:: php

   <?php

   public function analyzePermissions(array &$permissions, $allPermissions, $isSecondRound = false)
   {
       foreach ($permissions as $level => &$perms) {
           foreach ($perms as $perm) {
               $include = array();
               switch ($perm) {
                   case 'send_probe':
                       $include = array('use_telescope');
                       break;
                   case 'visit':
                       $include = array('use_telescope', 'send_probe');
                       break;
               }
               if (!empty($include)) {
                   foreach ($include as $r) {
                       list($ignore, $r) = $this->getSynonym($level, $r);
                       if ($this->isSupported($level, $r) && !in_array($r, $perms)) {
                           $perms[] = $r;
                       }
                   }
               }
           }
       }
       
       return false; 
   }

Plugins can adjust permissions based on other selections to prevent User error. For example, if a User has ``edit`` permission, they also require ``view`` permission. Use the ``analyzePermissions()`` method to modify permissions before Mautic persists them to the database.

To re-adjust permissions based on factors outside the Plugin's control, return ``true`` from ``analyzePermissions()``. This triggers a second round of analysis after all other bundles and Plugins finish their processing. During this round, the ``$isSecondRound`` argument is ``true``.

Advanced ``isGranted()`` logic
==============================

Override the parent method - ``public function isGranted($userPermissions, $name, $level)`` - to run custom logic rather than simple bit comparisons. Use this to define unique behavior for the class's own levels and individual permissions.

Advanced ``isSupported()`` logic
================================

The same rules apply to the ``isSupported()`` method. This method determines if a bundle or Plugin includes the requested permission and permission level. Use this to provide backward compatibility - BC - support.