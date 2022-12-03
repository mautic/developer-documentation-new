Landing pages
#############

There are two way to extend Landing Pages:
- Landing Page tokens used to insert Dynamic Content into a Landing Page
- A/B test winning criteria

Both leverage the ``\Mautic\PageBundle\PageEvents::PAGE_ON_BUILD`` event. Read more about :ref:`Event listeners`.

.. vale off

Landing Page tokens
*******************

.. vale on

Landing Page tokens get handled exactly the same as :ref:`Email tokens<Email tokens and A/B testing>`.

.. vale off

Page A/B Test Winner Criteria
*****************************

Custom Landing Page A/B test winner criteria get handled exactly the same as :ref:`Email A/B test winner criteria<Email tokens and A/B testing>` with the only differences being that the ``callback`` function gets passed ``Mautic\PageBundle\Entity\Page $page`` and ``Mautic\PageBundle\Entity\Page $parent`` instead.
Of course ``$children`` is an ArrayCollection of Page entities as well.

.. vale on

Please find a below an example of both Landing Page Tokens and Landing Page A/B Test Winner Criteria.

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/EventListener/PageSubscriber.php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Mautic\CoreBundle\Helper\TemplatingHelper;
    use Mautic\PageBundle\PageEvents;
    use Mautic\PageBundle\Event\PageBuilderEvent;
    use Mautic\PageBundle\Event\PageDisplayEvent;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    class PageSubscriber implements EventSubscriberInterface
    {
        private TemplatingHelper $templating;

        public function __construct(TemplatingHelper $templating)
        {
            $this->templating = $templating;
        }

        static public function getSubscribedEvents()
        {
            return [
                PageEvents::PAGE_ON_BUILD   => ['onPageBuild', 0],
                PageEvents::PAGE_ON_DISPLAY => ['onPageDisplay', 0]
            ];
        }

        /**
        * Register the tokens and a custom A/B test winner
        */
        public function onPageBuild(PageBuilderEvent $event)
        {
            // Add page token
            $event->addToken('{helloworld.token}', 'Helloworld token');

            // Add AB Test Winner Criteria
            $event->addAbTestWinnerCriteria(
                'helloworld.planetvisits',
                array(
                    // Label to group by
                    'group'    => 'plugin.helloworld.header',

                    // Label for this specific a/b test winning criteria
                    'label'    => 'plugin.helloworld.pagetokens.',

                    // Static callback function that will be used to determine the winner
                    'callback' => '\MauticPlugin\HelloWorldBundle\Helper\AbTestHelper::determinePlanetVisitWinner'
                )
            );
        }

        /**
        * Search and replace tokens with content
        */
        public function onPageDisplay(PageDisplayEvent $event)
        {
            // Get content
            $content = $event->getContent();

            // Search and replace tokens
            $content = str_replace(
                '{helloworld.token}',
                $this->templating->render('HelloWorldBundle:SubscribedEvents\PageToken:token.html.php');,
                $content
            );

            // Set updated content
            $event->setContent($content);
        }
    }
