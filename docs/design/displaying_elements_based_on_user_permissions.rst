Displaying elements based on User permissions
=============================================

In Mautic, it's possible to control the visibility of elements on the user interface based on the User's permissions. This allows for showing or hiding certain features, links, or sections depending on the User's Role and the permissions associated with that Role.

This approach enhances security and provides a tailored experience for each User based on their role and access level.

Using the ``securityIsGranted`` function
------------------------------------

To display elements conditionally based on User permissions, use the ``securityIsGranted`` function in Twig templates. The ``securityIsGranted`` function checks if the current User has the specified permission and returns a boolean value indicating whether the permission is granted or not.

Here's the basic syntax:

.. code-block:: twig

   {% if securityIsGranted('permission:string') %}
       <!-- Content to display if the user has the specified permission -->
   {% endif %}

In this structure, 'permission:string' represents the specific permission being checked for. Mautic uses a hierarchical permission system, in the format of 'bundle:level:permission'.

Displaying a user invitation link as example
--------------------------------------------

Let's examine a practical example of how to use this function to display a link for inviting new users to the platform. This link should only be visible to users who have the permission to create new user accounts.

In this example, we're using the securityIsGranted function to check if the current user has the 'user:users:create' permission. This permission string is structured to indicate that we're checking for the ability to create new users within the user management system.

.. code-block:: twig

   {% if securityIsGranted('user:users:create') %}
       <li>
           <a href="{{ path('mautic_user_action', {objectAction: 'new'}) }}">
               <i class="ri-team-line"></i>
               <span>{{ 'mautic.user.profile.invite'|trans }}</span>
           </a>
       </li>
   {% endif %}

If the current user has the user:users:create permission, the code inside the if block will be rendered, displaying the link to invite new users. The link is created using the path function, which generates a URL based on the specified route (mautic_user_action) and any additional parameters ({objectAction: 'new'}).

The 'mautic.user.profile.invite'|trans expression is used to translate the text "Invite your team" using Mautic's translation system. This ensures that the text is displayed in the appropriate language based on the user's locale settings.

This not only prevents unauthorized access but also keeps the interface clean and relevant for each user's role.

When implementing permission-based displays, it's essential to also secure the backend routes and actions that these interface elements might trigger. The frontend permission check should be considered an additional layer of security and user experience enhancement, not the sole method of access control.

Locating defined permissions
----------------------------

Mautic organizes its permissions on a per-bundle basis. Each bundle typically defines its own set of permissions in a dedicated PHP file. The standard location for these permission definitions is:

[BundleName]/Security/[BundleName]Permissions.php

For example:

- User permissions: UserBundle/Security/UserPermissions.php
- Email permissions: EmailBundle/Security/EmailPermissions.php
- SMS permissions: SmsBundle/Security/SmsPermissions.php

These PHP files contain classes that extend AbstractPermissions and define the specific permissions available for that bundle. They usually include methods for building the permission matrix and checking individual permissions.

Examining permission files
--------------------------

When opening one of these permission files, they'll typically find:

- A definePermissions method that outlines all available permissions for the bundle.
- Constants defining permission levels (e.g., LEVEL_VIEW, LEVEL_EDIT, LEVEL_FULL).
- Methods for checking specific permissions (e.g., canViewUsers, canEditEmails).

For example, in the UserPermissions.php file, the UserPermissions class defines the available permissions for the UserBundle using a more structured approach. Let's go through the important parts:

.. code-block:: php

   $this->permissions = [
       'profile' => [
           'editusername' => 1,
           'editemail'    => 2,
           'editposition' => 4,
           'editname'     => 8,
           'full'         => 1024,
       ],
   ];

In this example, the profile key represents the permission category, and the nested array defines the specific permission levels for actions like editing the username, email, position, name, and having full access to the user profile.

To use these permission keys with the securityIsGranted function in Twig templates, construct the appropriate permission string. The permission string follows the format: [bundle]:[level]:[permission].

Map the permission keys from the UserPermissions class to the corresponding permission strings:

- editusername => user:profile:editusername
- editemail => user:profile:editemail
- editposition => user:profile:editposition
- editname => user:profile:editname
- full => user:profile:full

In each if statement, the securityIsGranted function is used with the corresponding permission string. If the current user has the specified permission, the code inside the if block will be executed, displaying the relevant form fields for editing the user profile information.

For more information, refer to the Security documentation.