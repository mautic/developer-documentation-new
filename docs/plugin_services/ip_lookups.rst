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
