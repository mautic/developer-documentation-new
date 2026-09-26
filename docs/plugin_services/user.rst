User
####

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Use the ``Mautic\CoreBundle\Helper\UserHelper`` service to retrieve the currently logged-in User. Inject it into your service or subscriber through the constructor:

.. code-block:: php

    <?php

    use Mautic\CoreBundle\Helper\UserHelper;

    final class ExampleService
    {
        public function __construct(private UserHelper $userHelper)
        {
        }

        public function describeCurrentUser(): void
        {
            $user = $this->userHelper->getUser();

            $firstName = $user->getFirstName();
            $lastName  = $user->getLastName();
            $email     = $user->getEmail();

            if ($user->getRole()->isAdmin()) {
                // Do something for administrators.
            }
        }
    }

``getUser()`` returns the ``Mautic\UserBundle\Entity\User`` entity for the currently logged-in User, which you can then query for profile information. Pass ``true`` to receive ``null`` when the current request has no authenticated User.
