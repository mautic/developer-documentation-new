IP lookup services
##################

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
