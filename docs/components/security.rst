Security
########

Mautic provides a means of defining custom permissions for Roles through Permission objects.

.. _security-roles-and-permissions:

How permissions work
********************

Permissions get calculated based on bits assigned to a Plugin's level and permission. Bits are integers that increase by doubling the value. 1, 2, 4, 8, 16, 32, 64, 128, 512, 1024, and so forth.
The bits should never get numbers in between such as 3 or 5 as the permission won't be correctly calculated in such cases.

For example, imagine ``HelloWorldBundle`` needs to manage access to User's Worlds entity. A permission set for ``plugin:helloWorld:worlds`` might look like

.. list-table::
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

.. note:: ``plugin:helloWorld:worlds:view`` is a typically notation for requesting permissions in Mautic. The notation tells Mautic to validate the `view` permission for the Plugin, HelloWorldBundle, within the `worlds` level. Levels allow Plugins to set permissions for multiple areas.

Mautic takes the summation of the bits for the permissions given to a Role and stores it in the database. For example, if a Role has view and edit access, the stored bit is 3. If it has view and create access, the stored bit is 5.

When validating permissions, for example ``plugin:helloWorld:worlds:create``, Mautic checks if Role's generated bit has at least 4 for ``plugin:helloWorld:worlds``. If so, permission gets granted.

.. note:: The permission ``full`` grants access to all previous permissions within the level and thus should always be the highest bit.

Using permissions
*****************

You can use permissions as follows in your controllers and services:

.. code-block:: php

   <?php
   declare(strict_types=1);

   /** @var \Mautic\CoreBundle\Security\Permissions\CorePermissions */
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
   )
   ) {
       //do something
   }

   // Check if user is granted to at least one permission
   if ($security->isGranted(
       array(
           'plugin:helloWorld:worlds:view',
           'plugin:helloWorld:worlds:edit',
       ),
       'MATCH_ONE'
   )
   ) {
       //do something
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

To determine if a User has a specific permission, use Mautic's security service which has the ``mautic.security`` alias. The class is ``Mautic\CoreBundle\Security\Permissions\CorePermissions``.

As suggested in the preceding section, Mautic uses a special permission notation to refer to a specific permission.
For core bundles, use ``bundleName:permissionLevel:permission``.
For Plugins, append ``plugin:``, for example ``plugin:bundleName:permissionLevel:permission``. ``plugin:`` tells Mautic to look for the permission class in the ``plugins/`` directory and the ``MauticPlugin`` namespace. 

Mautic's core bundles and external Plugins are responsible for setting the permission level and permissions. For example, Mautic's core UserBundle has ``users`` and ``roles`` levels with ``view``, ``edit``, ``create``, ``delete`` and ``full`` permissions for each. 

.. note:: To validate whether a User has permissions to edit Roles, use ``$mauticSecurity->isGranted('user:roles:edit');``

Creating custom permissions
***************************

It's possible to define your own custom permissions within your Plugin. Make sure to extend ``Mautic\CoreBundle\Security\Permissions\AbstractPermissions`` like in the following example:

.. code-block:: php

   <?php
   // plugins/HelloWorldBundle/Security/Permissions/HelloWorldPermissions.php

   declare(strict_types=1);

   namespace MauticPlugin\HelloWorldBundle\Security\Permissions;

   use Symfony\Component\Form\FormBuilderInterface;
   use Mautic\CoreBundle\Security\Permissions\AbstractPermissions;

   class HelloWorldPermissions extends AbstractPermissions
   {
       public function __construct($params)
       {
           parent::__construct($params);

           $this->permissions = array(

               // Custom level
               'worlds' => array(

                   // Custom permissions
                   'use_telescope' => 1,
                   'send_probe'    => 2,
                   'visit'         => 4,
                   // Full will almost always be included and should be significantly higher than the
                   // others in case new permissions need to be added later 
                   'full'          => 1024
               )
           );

           // Add standard category permissions
           $this->addStandardPermissions('categories');
       }

       /**
        * Append the permission form fields to the Role form
        *
        * @param FormBuilderInterface $builder
        * @param array                $options
        * @param array                $data
        */
       public function buildForm(FormBuilderInterface &$builder, array $options, array $data)
       {
           // Add standard category form fields
           $this->addStandardFormFields('helloWorld', 'categories', $builder, $data);

           // Add custom 'worlds' level form fields
           $builder->add(

               // Form element name should be bundleName:permissionLevel
               'helloWorld:worlds',

               // Should always be permissionlist type
               'permissionlist',
               array(
                   'choices' => array(
                       'use_telescope' => 'plugin.helloworld.permissions.use_telescope',
                       'send_probe'    => 'plugin.helloworld.permissions.send_probe',
                       'visit'         => 'plugin.helloworld.permissions.visit',
                       'full'          => 'mautic.core.permissions.full',
                   ),
                   'label'   => 'plugin.helloworld.permissions',

                   // Set existing data
                   'data'    => (!empty($data['worlds']) ? $data['worlds'] : array()),

                   // Bundle name (used to build frontend form)
                   'bundle'  => 'helloWorld',

                   // Permission level (used to build frontend form)
                   'level'   => 'worlds'
               )
           );
       }

       /**
        * Permission set identifier; should be bundleName
        * 
        * @return string
        */
       public function getName()
       {
           return 'helloWorld';
       }
   }

You can register the permission class by adding it to your ``config.php`` as shown below. Make sure it's in the ``services.permissions`` group so that Mautic can pick it up correctly.

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/Config/config.php

    return [
        ...
        'services' => [
            'permissions' => [
                'marketplace.permissions' => [
                    'class' => \MauticPlugin\HelloWorldBundle\Security\Permissions\WorldsPermissions::class,
                ],
            ],
        ],
    ];

You can learn more about the available options by looking at the ``Mautic\CoreBundle\Security\Permissions\AbstractPermissions`` PHPDoc, but here's the most important information:

**__construct()**

The construct method should do two things. It should call ``parent::__construct($params)`` and/or it should set ``$this->params = $params;``. 

Then it should define ``$this->permissions``. ``$this->permissions`` is an array of permission levels that are each arrays with permissions assigned to bits. 
For example, in the code block, a custom permission level of ``worlds`` gets defined with the permissions of ``use_telescope``, ``send_probe``, ``visit`` and ``full``.
To validate whether a User has permission to the level ``worlds`` and permission ``send_probe`` , ``$mauticSecurity->isGranted('plugin:helloWorld:worlds:send_probe')`` would be used.

Mautic provides a few helper methods for common permission sets:

.. list-table::
   :header-rows: 1

   * - Method
     - Description
   * - ``addStandardPermissions()``
     - Set view, edit, create, delete, publish - with option to exclude, and full permissions.
   * - ``addExtendedPermissions()``
     - Set creator level restrictions: ``viewown``, ``viewother``, ``editown``, ``editother``, ``create``, ``deleteown``, ``deleteother``, ``publishown`` - with option to exclude, ``publishother`` - with option to exclude, and ``full``
   * - ``addManagePermission()``
     - Add a single ``manage`` permission, which is the same as ``full``. Use this in cases where you only need a single permission for everything, also known as an "all or nothing" approach.


**buildForm()**

The ``buildForm()`` method appends the permission toggles to the Role's Form. See :ref:`Forms` for details on Form builders. Review the comments in the code sample.

There are complimentary helper methods for the common permission sets:

.. list-table::
   :header-rows: 1

   * - Method
     - Description
   * - ``addStandardFormFields()``
     - Appends the standard permission sets to the Form
   * - ``addExtendedFormFields()``
     - Appends the extended, aka creator restricted, permissions to the Form 
   * - ``addManageFormFields()``
     - Appends the single manager element to the Form


**getName()**

This method is absolutely required and should match both the ``bundleName`` and the name of the file.
For example, if ``HelloWorldBundle`` is the bundle's name, then this would be ``helloWorld`` with a filename of ``HelloWorldPermissions.php``.

Permission aliases
==================

.. code-block:: php

   <?php

    protected function getSynonym($name, $level)
    {
        if ($name == 'send_satellite') {
            // Set real permission name
           $name = 'send_probe';
        }

        return array($name, $level);
    }

To add a permission alias, use the ``getSynonym()`` method.
Basically this method gets called before each requested permission gets determined, giving opportunity to change the permission level or name as needed.

For example, ``parent::getSynonym()`` will recognize ``editown`` as ``edit`` if ``editown`` isn't defined in the permission class' ``$this->permissions`` property for the requested level.

Manipulating permissions before saving
======================================

.. code-block:: php

    <?php

    /**
      * @param array $permissions     Plugin specific permissions
      * @param       $allPermissions  All role permissions
      * @param bool  $isSecondRound   Is round two after permissions have been updated by all permission classes 
      *
      * @return bool Return true if a second round is required; default false
      */
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

        // Return true if this method needs a second round after all the other bundles have adjusted permissions
        return false;
    }

Plugins can adjust permissions based on other selected permissions to prevent ``User error``.
For example, if a User has permission to ``edit``, then the User also needs permission to ``view`` whether that got selected in the Role Form or not.
You can use the method ``analyzePermissions()`` for this which the Plugin the opportunity to modify permissions based on other selections before persisting to the database. 

Sometimes, it may be necessary to re-adjust based on a permission that's outside the Plugin's control.
In this case, ``analyzePermissions()`` can return true and it gets called again after all the permissions got analyzed by the other bundles and Plugins.
In this case, the argument ``$isSecondRound`` is true.

Advanced ``isGranted`` logic
============================

If it's necessary to perform some logic other than simply comparing bits, the permission class can override the parent's ``public function isGranted($userPermissions, $name, $level)`` and do whatever is necessary for its own permission levels and individual permissions.

Advanced ``isSupported`` logic
==============================

The same applies for the method ``isSupported()`` which you can use to determine if a bundle or Plugin includes the requested permission and permission level.
You can also use this to provide BC support.

.. vale off

Single sign-on
**************

.. vale on

Todo:

- ``\Mautic\UserBundle\UserEvents::USER_LOGIN``
- ``\Mautic\UserBundle\UserEvents::USER_FORM_AUTHENTICATION``
- ``\Mautic\UserBundle\UserEvents::USER_PRE_AUTHENTICATION``
- ``\Mautic\UserBundle\UserEvents::USER_AUTHENTICATION_CONTENT``
