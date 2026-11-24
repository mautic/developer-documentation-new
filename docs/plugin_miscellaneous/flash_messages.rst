Flash messages
##############

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

The ``Mautic\CoreBundle\Service\FlashBag`` service manages flash messages - the alerts Mautic shows after an action. It takes care of translation and message levels, and can optionally add a matching entry to the notification center.

From a controller
*****************

.. vale off

Controllers that extend one of :ref:`Mautic's common controllers<plugins/mvc:Controllers>` can use the ``addFlashMessage()`` helper:

.. vale on

.. code-block:: php

    <?php

    $this->addFlashMessage(
        'mautic.translation.key',
        ['%placeholder%' => 'some text'],
        FlashBag::LEVEL_NOTICE, // Message level
        'flashes'               // Translation domain
    );

From a service
**************

From a model or any other service, inject ``Mautic\CoreBundle\Service\FlashBag`` and call ``add()``:

.. code-block:: php

    <?php

    use Mautic\CoreBundle\Service\FlashBag;

    final class ExampleService
    {
        public function __construct(private FlashBag $flashBag)
        {
        }

        public function notify(): void
        {
            $this->flashBag->add(
                'mautic.translation.key',
                ['%placeholder%' => 'some text'],
                FlashBag::LEVEL_NOTICE,
                'flashes'
            );
        }
    }

Both ``addFlashMessage()`` and ``FlashBag::add()`` take a final ``$addNotification`` argument. Set it to ``true`` to add a matching entry to the notification center alongside the flash message.

Notifications
*************

Mautic also has a notification center. Adding a flash message doesn't create a notification by default, but you can opt in with the ``$addNotification`` flag described earlier, or add one on its own. To add a standalone notification, inject ``Mautic\CoreBundle\Model\NotificationModel`` and call its ``addNotification()`` method.
