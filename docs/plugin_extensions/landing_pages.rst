Landing pages
#############

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

There are two way to extend Landing Pages:
- Landing Page tokens used to insert Dynamic Content into a Landing Page
- A/B test winning criteria

Both leverage the ``\Mautic\PageBundle\PageEvents::PAGE_ON_BUILD`` event. Read more about :ref:`plugins/event_listeners:Event listeners`.

.. vale off

Landing Page tokens
*******************

.. vale on

Landing Page tokens get handled exactly the same as :ref:`Email tokens<components/emails:Email tokens and A/B testing>`.

.. vale off

Page A/B Test Winner Criteria
*****************************

Custom Landing Page A/B test winner criteria get handled exactly the same as :ref:`Email A/B test winner criteria<components/emails:Email tokens and A/B testing>` with the only differences being that the ``callback`` function gets passed ``Mautic\PageBundle\Entity\Page $page`` and ``Mautic\PageBundle\Entity\Page $parent`` instead.
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

Preview PDF generation
**********************

.. vale on

Users can download Landing Page previews as PDF files. Mautic uses an event-driven PDF generation process, enabling Plugins and distributions to provide custom PDF generators.

Mautic dispatches the ``\Mautic\PageBundle\PageEvents::PAGE_PREVIEW_GENERATE_PDF`` event when a User downloads a Landing Page preview as a PDF. The default community implementation uses Dompdf when available, falling back to a basic stdlib-based PDF generator.

Event details
=============

* **Event name:** ``mautic.page_preview_generate_pdf``
* **Constant:** ``\Mautic\PageBundle\PageEvents::PAGE_PREVIEW_GENERATE_PDF``
* **Event class:** ``\Mautic\PageBundle\Event\PagePreviewPdfGenerationEvent``

Default implementation
======================

Mautic provides default PDF generation through:

* **Subscriber:** ``\Mautic\PageBundle\EventListener\PagePreviewPdfSubscriber``
* **Generator:** ``\Mautic\PageBundle\Pdf\PagePreviewPdfGenerator``

The default subscriber runs at priority ``-255``, allowing custom implementations to take precedence.

If no listener sets PDF content, the controller returns a 500 error.

Routes
======

Landing Page preview PDF downloads use these routes:

* ``/page/preview/{id}/download/{downloadType}``
* ``/page/preview/{id}/draft/download/{downloadType}``

The ``downloadType`` parameter defaults to ``pdf``.

Event payload
=============

The event provides access to:

.. vale off

* ``getHtmlContent()`` - The rendered HTML preview content
* ``getPage()`` - The Landing Page entity
* ``getContact()`` - The Contact context, if selected for preview
* ``getRequest()`` - The HTTP request object
* ``getFileName()`` - The suggested PDF filename

.. vale on

Event methods
=============

To provide a custom PDF:

#. Generate binary PDF bytes from the HTML content using ``getHtmlContent()``
#. Call ``setPdfContent($bytes)`` to set the PDF content
#. Optionally call ``setFileName()`` to customize the output filename
#. Use ``hasPdfContent()`` to verify if another subscriber already provided PDF content

.. vale off

Custom PDF generator example
============================

.. vale on

This example shows how to create a custom PDF generator using a hypothetical premium PDF service:

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/EventListener/PagePdfSubscriber.php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Mautic\PageBundle\Event\PagePreviewPdfGenerationEvent;
    use Mautic\PageBundle\PageEvents;
    use MauticPlugin\HelloWorldBundle\Service\PremiumPdfService;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    final class PagePdfSubscriber implements EventSubscriberInterface
    {
        public function __construct(
            private PremiumPdfService $pdfService,
        ) {
        }

        public static function getSubscribedEvents(): array
        {
            return [
                PageEvents::PAGE_PREVIEW_GENERATE_PDF => ['onPagePreviewGeneratePdf', 0],
            ];
        }

        public function onPagePreviewGeneratePdf(PagePreviewPdfGenerationEvent $event): void
        {
            if ($event->hasPdfContent()) {
                return;
            }

            $pdfBytes = $this->pdfService->htmlToPdf($event->getHtmlContent());
            $event->setPdfContent($pdfBytes);
        }
    }

.. note::

   Register your subscriber at a higher priority, such as ``0`` or ``100``, to override the default PDF generation.
