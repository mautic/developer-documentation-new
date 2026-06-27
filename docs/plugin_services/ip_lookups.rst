IP lookup services
##################

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

It's possible for your Plugin to retrieve the real User IP for the request. You can do so as follows:

.. code-block:: php

    <?php
    /** @var \Mautic\CoreBundle\Helper\IpLookupHelper */
    $ipHelper = $this->get('mautic.helper.ip_lookup');

    $requestIp = $ipHelper->getIpAddressFromRequest(); // 1.2.3.4

    /** @var \Mautic\CoreBundle\Entity\IpAddress $ipAddressEntity */
    $ipAddressEntity = $ipHelper->getIpAddress();

    /** @var array $details */
    $details = $ipAddressEntity->getIpDetails();

    echo $details['city'];

Checking whether Mautic should track a request
***********************************************

Before you record a Landing Page hit, Email open, Asset download, or Contact, call ``isRequestTrackable()`` to confirm the request comes from a real visitor. The method checks the active request for bot indicators and privacy signals, and returns ``false`` when Mautic shouldn't track it:

.. code-block:: php

    <?php
    /** @var \Mautic\CoreBundle\Helper\IpLookupHelper $ipHelper */
    $ipHelper = $this->get('mautic.helper.ip_lookup');

    if ($ipHelper->isRequestTrackable()) {
        // Record the page hit, email open, asset download, or Contact.
    }

``isRequestTrackable()`` returns ``false`` when any of the following apply to the current request:

.. vale off

* The request method is ``HEAD``, which bots and monitoring tools commonly use.
* The request carries a ``Purpose`` or ``Sec-Purpose`` header set to ``prefetch`` or ``prerender``, which browsers send when speculatively loading links.
* The ``Sec-GPC: 1`` header is present, signalling Global Privacy Control.
* The ``DNT: 1`` header is present, signalling Do Not Track.
* The IP address or User-Agent matches Mautic's bot filtering, described in :ref:`Automatic bot detection <automatic bot detection>`.

.. vale on

When there's no active request, such as when running from the command line, the method falls back to whether the resolved IP address is trackable.

Mautic Core runs this validation when it records Landing Page hits, Email opens, Asset downloads, and Contact tracking, so it filters out traffic from bots and privacy-conscious visitors consistently.

.. _automatic bot detection:

Automatic bot detection
***********************

``getIpAddress()`` automatically flags known bots as not trackable. Alongside the configured list of bot User-Agent patterns, Mautic runs each request's User-Agent through Matomo's :xref:`Matomo DeviceDetector library`, which recognizes over 500 known bots such as search engine crawlers, scrapers, monitoring services, and more, and keeps their traffic out of your analytics without any configuration.

When Mautic detects a bot, it marks the returned ``IpAddress`` entity as not trackable:

.. code-block:: php

    <?php
    /** @var \Mautic\CoreBundle\Helper\IpLookupHelper $ipHelper */
    $ipHelper = $this->get('mautic.helper.ip_lookup');

    $ipAddressEntity = $ipHelper->getIpAddress();

    if ($ipAddressEntity->isTrackable()) {
        // Not a known bot — safe to associate with a Contact.
    }

Adding custom bot patterns
==========================

Automatic detection covers the vast majority of bots, so most installations need no extra configuration. To block a bot that Mautic doesn't recognize automatically, add its User-Agent pattern to the ``do_not_track_bots`` configuration parameter. Mautic matches each entry as a case-sensitive substring of the request's User-Agent header:

.. code-block:: php

    // app/config/local.php
    'do_not_track_bots' => [
        'MyCustomCrawler',
        'InternalMonitor',
    ],

Mautic treats a request whose User-Agent contains any of these patterns the same way as an automatically detected bot.
