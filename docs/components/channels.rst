Channels
========
Todo:

Preference center integration

How to register Channel features:

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