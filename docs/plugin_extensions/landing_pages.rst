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

Both use the ``\Mautic\PageBundle\PageEvents::PAGE_ON_BUILD`` event, and the tokens example below also handles the Page display event. In Mautic 8.0, the display event keys on ``PageDisplayEvent::class``, while ``PAGE_ON_BUILD`` stays keyed on its string constant.
Read more about :ref:`plugins/event_listeners:Event listeners`.

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
                PageEvents::PAGE_ON_BUILD => ['onPageBuild', 0],
                PageDisplayEvent::class   => ['onPageDisplay', 0],
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

.. note::

   A subscriber left on the old ``PageEvents::PAGE_ON_DISPLAY`` constant silently stops receiving the event in Mautic 8.0, because Mautic raises no error to flag the change. Re-key it on ``PageDisplayEvent::class``, as shown above.

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

Customizing Preference Center
*****************************

Preference Center lets Contacts manage their communication preferences. Since Mautic 7.2, you can customize the labels on Preference Center slot components using the Page display event.

.. vale on

This lets you override default translated labels with custom text for branding, localization beyond built-in translations, or dynamic label generation based on context.

.. note::

   In Mautic 8.0, Mautic dispatches the ``PageDisplayEvent`` by its class name. Subscribers key ``getSubscribedEvents()`` on ``PageDisplayEvent::class``. A subscriber still keyed on the old ``PageEvents::PAGE_ON_DISPLAY`` string constant no longer receives the event in Mautic 8.0, even though ``PageEvents`` keeps the constant defined for backward compatibility.

Available slot parameters
=========================

Each Preference Center slot accepts label attributes that override the default translated text:

.. vale off

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Slot
     - Attribute
     - Default translation key
   * - ``segmentlist``
     - ``label-text``
     - ``mautic.lead.form.list`` - **My segments**
   * - ``categorylist``
     - ``label-text``
     - ``mautic.lead.form.categories`` - **My categories**
   * - ``preferredchannel``
     - ``label-text``
     - ``mautic.lead.list.frequency.preferred.channel`` - **I prefer communication by**
   * - ``channelfrequency``
     - ``label-text``
     - ``mautic.lead.contact.me.label`` - **I want to receive %channel%**
   * - ``channelfrequency``
     - ``label-text1``
     - ``mautic.lead.list.frequency.number`` - **Do not contact more than**
   * - ``channelfrequency``
     - ``label-text2``
     - ``mautic.lead.list.frequency.times`` - **Messages each**
   * - ``channelfrequency``
     - ``label-text3``
     - ``mautic.lead.frequency.dates.label`` - **Pause from**
   * - ``channelfrequency``
     - ``label-text4``
     - ``mautic.lead.frequency.contact.end.date`` - **Pause to**
   * - ``saveprefsbutton``
     - ``btnText``
     - ``mautic.page.form.saveprefs`` - **Save preferences**

.. vale on

Example implementation
======================

Create an event subscriber that listens to ``PageDisplayEvent`` and modifies the slot parameters:

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/EventListener/PreferenceCenterSubscriber.php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Mautic\PageBundle\Event\PageDisplayEvent;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    class PreferenceCenterSubscriber implements EventSubscriberInterface
    {
        public static function getSubscribedEvents(): array
        {
            return [
                PageDisplayEvent::class => ['onPageDisplay', 100],
            ];
        }

        public function onPageDisplay(PageDisplayEvent $event): void
        {
            // Only modify Preference Center pages
            if (!$event->getPage()->getIsPreferenceCenter()) {
                return;
            }

            // Get current slot parameters
            $params = $event->getParams();

            // Customize segment list label
            $params['segmentlist']['label-text'] = 'Choose your mailing lists';

            // Customize category list label
            $params['categorylist']['label-text'] = 'Select your interests';

            // Customize preferred channel label
            $params['preferredchannel']['label-text'] = 'How would you like us to contact you?';

            // Customize channel frequency labels
            $params['channelfrequency']['label-text'] = 'I want to receive emails';
            $params['channelfrequency']['label-text1'] = 'Limit messages to';
            $params['channelfrequency']['label-text2'] = 'per';
            $params['channelfrequency']['label-text3'] = 'Pause starting';
            $params['channelfrequency']['label-text4'] = 'Pause ending';

            // Customize save button text
            $params['saveprefsbutton']['btnText'] = 'Update my preferences';

            // Apply the modified parameters
            $event->setParams($params);
        }
    }

Mautic autowires and registers event subscribers automatically, so you don't need to configure the service manually.

.. vale off

Landing Page lifecycle events
*****************************

.. vale on

.. vale off

Mautic dispatches events at key points in a Landing Page's lifecycle. Plugins can use these events to react to or modify behavior when a User creates, updates, deletes, or changes the **Available for use** status of a Landing Page.

.. vale on

.. vale off

Toggle 'Available for use' event
================================

.. vale on

The ``\Mautic\PageBundle\PageEvents::PAGE_ON_TOGGLE_PUBLISH`` event dispatches when a User toggles the **Available for use** status of a Landing Page. Mautic dispatches it before persisting the status change to the database, so Plugins can run actions or validations before the User makes the Landing Page available or unavailable.

.. note::

   ``PAGE_ON_TOGGLE_PUBLISH``, like ``PAGE_ON_BUILD``, dispatches the shared ``PageEvent`` class that several event names reuse, so it stays keyed on its ``PageEvents::*`` string constant. Only events with a dedicated event class, such as ``PageDisplayEvent``, changed to class-name keying in Mautic 8.0.

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
