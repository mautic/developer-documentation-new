Channels
==========================================================

Todo:

Preference center integration

Listening for channel features
------------------------------

You can find several events through the ``ChannelEvents`` class.

.. code-block:: php

    <?php

    public static function getSubscribedEvents()
    {
        return [
            ChannelEvents::ADD_CHANNEL => ['onAddChannel', 100],
        ];
    }

    public function onAddChannel(ChannelEvent $event)
    {
        $event->addChannel(
            'email',
            [
                MessageModel::CHANNEL_FEATURE => [
                    'campaignAction'             => 'email.send',
                    'campaignDecisionsSupported' => [
                        'email.open',
                        'page.pagehit',
                        'asset.download',
                        'form.submit',
                    ],
                    'lookupFormType' => EmailListType::class,
                ],
                LeadModel::CHANNEL_FEATURE   => [],
                ReportModel::CHANNEL_FEATURE => [
                    'table' => 'emails',
                ],
            ]
        );
    }

Extending broadcasts
--------------------

Broadcasts are communications sent in bulk through a Channel such as Email.
An event is available to execute the sending of these bulk communications via the ``mautic:broadcasts:send`` command.

To hook into the ``mautic:broadcasts:send`` command, create a listener for the ``\Mautic\CoreBundle\CoreEvents::CHANNEL_BROADCAST`` event.
The event listener should check for the appropriate context and ID.

.. code-block:: php

    <?php
    // plugins\HelloWorldBundle\EventListener\BroadcastSubscriber

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Mautic\ChannelBundle\ChannelEvents;
    use Mautic\ChannelBundle\Event\ChannelBroadcastEvent;
    use MauticPlugin\HelloWorldPlugin\Model\WorldModel;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    class BroadcastSubscriber implements EventSubscriberInterface
    {
        private WorldModel $model;

        public function __construct(WorldModel $model)
        {
            $this->model = $model;
        }

        public static function getSubscribedEvents()
        {
            return [
                ChannelEvents::CHANNEL_BROADCAST => ['onChannelBroadcast', 0]
            ];
        }

        public function onChannelBroadcast(ChannelBroadcastEvent $event)
        {
            if (!$event->checkContext('world')) {
                return;
            }

            // Get list of published broadcasts or broadcast if there is only a single ID
            $id         = $event->getId();
            $broadcasts = $this->model->getRepository()->getPublishedBroadcasts($id);
            $output     = $event->getOutput();

            while (($broadcast = $broadcasts->next()) !== false) {
                list($sentCount, $failedCount, $ignore) = $this->model->sendIntergalacticMessages($broadcast[0], null, 100, true, $output);
                $event->setResults($this->translator->trans('plugin.helloworld').': '.$broadcast[0]->getName(), $sentCount, $failedCount);
            }
        }
    }
