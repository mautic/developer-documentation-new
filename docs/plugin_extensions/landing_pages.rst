Landing Pages
#############

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

There are two ways to extend Landing Pages:

* Landing Page tokens used to insert Dynamic Content into a Landing Page
* A/B test winning criteria

Both leverage the ``\Mautic\PageBundle\PageEvents::PAGE_ON_BUILD`` event. Read more about :ref:`plugins/event_listeners:Event listeners`.

.. vale off

Landing Page tokens
*******************

.. vale on

Landing Page tokens get handled exactly the same as :ref:`Email tokens<components/emails:Email tokens and A/B testing>`.

.. vale off

Page A/B test winner criteria
*****************************

Custom Landing Page A/B test winner criteria get handled exactly the same as :ref:`Email A/B testing`, except the ``callback`` function receives the following arguments:

* ``Mautic\PageBundle\Entity\Page $page``
* ``Mautic\PageBundle\Entity\Page $parent``

``$children`` is an ArrayCollection of Page entities as well.

.. vale on

Below is an example of both Landing Page Tokens and Landing Page A/B Test Winner Criteria.

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

.. vale off

URL token replacement
*********************

.. vale on

When a Contact clicks a tracked link, Mautic's redirect handler can replace Contact field tokens in the target URL before redirecting. This allows personalized destination URLs based on Contact data.

The ``Mautic\PageBundle\Event\UrlTokenReplaceEvent`` event dispatches during the redirect process. Use it to customize or extend URL token replacement logic. By default, Mautic's built-in subscriber handles standard Contact field tokens like ``{contactfield=email}`` or ``{contactfield=firstname}``.

Use cases for this event include:

* Adding custom token types beyond Contact fields
* Transforming token values before URL insertion
* Implementing conditional token replacement based on Email context
* Logging or auditing token replacements

The event provides:

* ``getContent()`` - Returns the current URL string
* ``setContent(string $url)`` - Sets the modified URL
* ``getLead()`` - Returns the ``Mautic\LeadBundle\Entity\Lead`` Contact entity
* ``getEmailId()`` - Returns the Email ID if the redirect originated from an Email click, or ``null`` otherwise

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/EventListener/UrlTokenSubscriber.php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Mautic\LeadBundle\Helper\TokenHelper;
    use Mautic\PageBundle\Event\UrlTokenReplaceEvent;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    final class UrlTokenSubscriber implements EventSubscriberInterface
    {
        public static function getSubscribedEvents(): array
        {
            return [
                UrlTokenReplaceEvent::class => ['onUrlTokenReplace', 0],
            ];
        }

        public function onUrlTokenReplace(UrlTokenReplaceEvent $event): void
        {
            $url = $event->getContent();

            // Check if URL contains tokens using the public regex
            if (!preg_match(TokenHelper::REGEX, $url)) {
                return;
            }

            $contact = $event->getLead();
            $emailId = $event->getEmailId();

            // Implement custom token replacement logic
            // For example, replace a custom token with Contact data
            if (str_contains($url, '{custom_token}')) {
                $customValue = $this->getCustomValue($contact, $emailId);
                $url = str_replace('{custom_token}', urlencode($customValue), $url);
                $event->setContent($url);
            }
        }

        private function getCustomValue($contact, ?int $emailId): string
        {
            // Your custom logic here
            return 'custom_value';
        }
    }

.. note::

   The ``TokenHelper::REGEX`` constant provides the regular expression pattern for matching Contact field tokens. Use this to check whether a URL contains tokens before performing replacements.

.. vale off

Landing Page lifecycle events
*****************************

.. vale on

.. vale off

Mautic dispatches events at key points in a Landing Page's lifecycle. Plugins can use these events to react to or modify behavior when a User creates, updates, deletes, or changes the Available for use status of a Landing Page.

.. vale on

.. vale off

Toggle 'Available for use' event
================================

.. vale on

The ``\Mautic\PageBundle\PageEvents::PAGE_ON_TOGGLE_PUBLISH`` event dispatches when a User toggles the **Available for use** status of a Landing Page. Mautic dispatches it before persisting the status change to the database, so Plugins can run actions or validations before the User makes the Landing Page available or unavailable.

An event listener receives a ``Mautic\PageBundle\Event\PageEvent`` instance.

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/EventListener/PageLifecycleSubscriber.php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Mautic\PageBundle\PageEvents;
    use Mautic\PageBundle\Event\PageEvent;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    final class PageLifecycleSubscriber implements EventSubscriberInterface
    {
        public static function getSubscribedEvents(): array
        {
            return [
                PageEvents::PAGE_ON_TOGGLE_PUBLISH => ['onPageTogglePublish', 0],
            ];
        }

        public function onPageTogglePublish(PageEvent $event): void
        {
            $page = $event->getPage();

            // Check current publish status (before toggle)
            $isCurrentlyPublished = $page->isPublished();

            // Perform custom logic before the status changes
            // For example, notify an external service or invalidate a cache
        }
    }
