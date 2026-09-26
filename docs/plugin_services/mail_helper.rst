Mail helper
###########

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Use the mail helper to send Email through Mautic's mailer, passing the content through the event listeners that replace tokens and manipulate it. Inject ``Mautic\EmailBundle\Helper\MailHelper`` into your service, then call ``getMailer()`` to get a reset instance to work with:

.. code-block:: php

    <?php

    use Mautic\EmailBundle\Helper\MailHelper;

    final class ExampleService
    {
        public function __construct(private MailHelper $mailHelper)
        {
        }

        public function sendMail(): void
        {
            $mailer = $this->mailHelper->getMailer();

            // Recipients; you can also use setTo(), addCc(), setCc(), addBcc(), or setBcc()
            $mailer->addTo($toAddress, $toName);

            // Set a custom sender; Mautic uses the system settings by default
            $mailer->setFrom('sender@example.com', 'Sender Name');

            $mailer->setSubject($subject);

            // Set the content and parse the plain text version from the HTML
            $mailer->setBody($content);
            $mailer->parsePlainText($content);

            // Optional Contact tracking
            $mailer->setLead($lead);
            $mailer->setIdHash();

            // Pass true to dispatch through the event listeners that replace tokens
            if ($mailer->send(true)) {
                // Optionally create a stat to allow a web view, tracking, and so on
                $mailer->createEmailStat();
            } else {
                $errors           = $mailer->getErrors();
                $failedRecipients = $errors['failures'];
            }
        }
    }

.. note::

   In Mautic 7, the mail helper uses Symfony Mailer. The legacy SwiftMailer classes and the ``$this->get('mautic.helper.mailer')`` service-locator pattern no longer exist — inject the ``MailHelper`` service instead.

Sending to an Email entity
**************************

If you have an Email entity of type ``Mautic\EmailBundle\Entity\Email``, pass it to ``setEmail()``. Mautic extracts and sets the subject, body, Assets, and other properties for you:

.. code-block:: php

    <?php

    $mailer = $this->mailHelper->getMailer();
    $mailer->setEmail($email);
    $mailer->addTo($toAddress, $toName);
    $mailer->send(true);

Batch sending with the queue
****************************

Some transports, such as Mandrill, support tokenized Email for multiple recipients. The mail helper exposes this feature through its ``enableQueue()`` and ``flushQueue()`` functions. When you send the same Email to a batch of Contacts, enable tokenized sending with ``enableQueue()`` and flush the pending messages with ``flushQueue()`` rather than calling ``send()`` for each recipient.

When the queue reaches the transport's batch limit, ``addTo()`` throws a ``Mautic\EmailBundle\Mailer\Exception\BatchQueueMaxException``. Catch it, flush the queue, then add the recipient again:

.. code-block:: php

    <?php

    use Mautic\EmailBundle\Mailer\Exception\BatchQueueMaxException;

    $mailer = $this->mailHelper->getMailer();
    $failed = [];

    $mailer->enableQueue();

    foreach ($emailList as $email) {
        try {
            if (!$mailer->addTo($email['email'], $email['name'])) {
                // Clear the errors so they don't stop the next send
                $mailer->clearErrors();
                $failed[] = $email;

                continue;
            }
        } catch (BatchQueueMaxException) {
            // Queue full, so flush then try again
            if (!$mailer->flushQueue()) {
                $errors = $mailer->getErrors();
                $failed = array_merge($failed, $errors['failures']);
            }

            $mailer->addTo($email['email'], $email['name']);
        }
    }

    // Flush any remaining queued messages
    $mailer->flushQueue();

.. note::

   Queueing only activates when the transport supports tokenized sending. For other transports, the mail helper sends each message individually, so this code works in both cases.

Attachments
***********

Attach files to an Email with ``attachFile()``. To attach a Mautic Asset entity ``Mautic\AssetBundle\Entity\Asset``, use ``attachAsset()``:

.. code-block:: php

    <?php

    $mailer->attachFile($filePath, $fileName);
    $mailer->attachAsset($asset);

Refer to the ``MailHelper`` class for the full list of available functions.
