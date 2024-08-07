Notifications
=============

Notifications are a critical Component of User experience (UX) in digital products, serving as a bridge between the system and the User. They should enhance, not detract from, the User experience, assisting Users in achieving their goals and providing immediate, relevant feedback. This guide synthesizes best practices from the Carbon Design System and industry standards to help developers create effective and User-friendly notifications.

Notification types and their use
================================

Understanding notification variants
-----------------------------------

Notifications come in various forms, each serving a specific purpose within an app:

- **Inline notifications**: integrated into task flows to inform Users about the status of an action or system changes. Mautic displays these at the top of the content area or near the relevant item.

- **Toast notifications**: these are time-based messages that appear at the top of the screen and disappear after a short duration. Mautic displays these as brief messages that don't require User interaction.

- **Actionable notifications**: includes interactive elements and require User interaction. Styled similarly to inline or toast notifications, but more disruptive due to their interactive nature.

Design
------

- Carefully examine the context in which notifications appear. Use them sparingly and only when they add value to the User experience.
- Maintain consistency in the design and behavior of notifications across the app.
- Be sure to use high-contrast notifications for critical messaging, as low-contrast notifications are less visually disruptive.

Content
-------

- Notifications should be concise and to the point, with a short and descriptive title. Limit the body content to one or two sentences.

Actions
-------

- Limit actionable notifications to one action per notification to avoid overwhelming the User.
- Inline notifications should persist until dismissed by the User or resolved through an action. Toast notifications can time out but should also include a close button.

Accessibility
-------------

- Notifications should be accessible and not rely solely on color to convey status, as this can be problematic for Users with color blindness, so use additional HTML attributes according to the notification type.
- Toast notifications with interactive content shouldn't automatically disappear to remain WCAG 2.1 compliant.

.. vale off

Using notification Components
=============================

.. vale on

Standard notifications with icons
---------------------------------

For standard notifications that include an icon, developers should use a ``<div>`` element with the class ``alert`` and an additional class to specify the type of notification:

- ``.alert-success`` for success messages
- ``.alert-info`` for informational messages
- ``.alert-warning`` for warnings
- ``.alert-danger`` for errors

Each class corresponds to a specific icon and color that's automatically applied using CSS logic.

Example:

.. code-block:: html

    <div class="alert alert-warning" role="alert">
      No emails are scheduled to be sent.
    </div>

This displays a warning notification with an appropriate icon and color styling.

Larger notification blocks without icons
----------------------------------------

When you need a larger notification block - for instance to include headings or additional content - developers should use the ``alert`` class along with a column class that starts with the ``col-`` prefix. These notifications don't display an icon but have only a colored left border indicative of the notification type.

Example:

.. code-block:: html

    <div class="alert alert-warning col-md-6">
      <h4>No Results Found</h4>
      <p>Seems there are none! Try changing a filter (if applicable) or how about creating a new one?</p>
    </div>

This creates a more substantial notification block with a heading and paragraph, distinguished by a yellow left border for a warning but without an accompanying icon.


Notifications for the notifications panel
=========================================

The ``NotificationModel`` class in ``NotificationModel.php`` manages notifications under the panel.

.. note::

   The system defines the notification template in ``notification.html.twig``.

Creating a notification
-----------------------

To create a notification, use the ``addNotification`` method of the ``NotificationModel`` class. This method accepts several parameters to customize the notification:

.. code-block:: php

   $notificationModel->addNotification(
       $message,
       $type,
       $isRead,
       $header,
       $iconClass,
       $datetime,
       $user,
       $deduplicateValue,
       $deduplicateDateTimeFrom
   );

.. note::

   All notifications must have a header string defined.

Parameters:
^^^^^^^^^^^

.. vale of

- ``$message`` (string): the main content of the notification.
- ``$type`` (string|null): identifies the source and style of the notification (optional).
- ``$isRead`` (boolean): indicates if the system has marked the notification as read (default: true).
- ``$header`` (string|null): the header text for the notification (required).
- ``$iconClass`` (string|null): CSS class for the notification icon (for example, 'ri-eye-line').
- ``$datetime`` (\\DateTime|null): creation date of the notification.
- ``$user`` (User|null): the User object associated with the notification defaults to the current User.
- ``$deduplicateValue`` (string|null): used to prevent duplicate notifications within a specified timeframe.
- ``$deduplicateDateTimeFrom`` (\\DateTime|null): customizes the ``deduplication timeframe``.

.. vale on

.. note::

   The header should only contain the translation string; Twig handles the translation.


Notification types
------------------

The ``$type`` parameter determines the visual style of the notification:
.. vale off

- ``'success'``: green alert with success icon
- ``'info'``: blue alert with info icon
- ``'warning'``: yellow alert with warning icon
- ``'error'``: red alert with error icon
- ``''`` (empty string): default style without colors and icon

.. vale on

Example usage
-------------

Here's how to create a notification when you schedule a Contact export:

.. code-block:: php

   public function onContactExportScheduled(ContactExportSchedulerEvent $event): void
   {
       /** @var User $user */
       $user    = $event->getContactExportScheduler()->getUser();
       $message = $this->translator->trans('mautic.lead.export.being.prepared', ['%user_email%' => $user->getEmail()]);

       $this->notificationModel->addNotification(
           $message,
           'info',
           false,
           'mautic.lead.export.being.prepared.header',
           null,
           null,
           $user
       );
   }

This use case shows how to integrate the NotificationModel into event-driven processes within Mautic.
This example calls the ``addNotification`` method with specific parameters tailored to the Contact export scenario. The Translator service handles the ``$message`` parameter to generate a localized message. This approach includes the User's Email address in the notification message. The system uses the translation key ``mautic.lead.export.being.prepared`` with the parameter ``%user_email%``, replacing it with the actual Email of the User who scheduled the export. This method allows for dynamic content insertion into the translated string.
If the User's Email weren't needed in the message, the system could have used a normal translation string without parameter replacement.

The other parameters in the ``addNotification`` call are equally important. The system styles the notification as an informational alert using the ``info`` type, which is appropriate for a status update on a scheduled task. The false value for ``$isRead`` ensures that the notification appears as unread, drawing the User's attention to this new information. The header, like the message, uses a translation key ``mautic.lead.export.being.prepared.header`` to maintain language consistency. Null values for the icon class and ``datetime`` mean that the system uses default values for these optional parameters. Finally, by passing the ``$user`` object, the notification is specifically associated with the user who initiated the export, ensuring it appears in their personal notification panel.