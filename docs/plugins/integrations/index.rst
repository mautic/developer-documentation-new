Integration framework
#####################

Each Integration provides its unique name as registered with Mautic, an icon, and a display name. When an Integration registers, the Integration helper classes manage the ``\Mautic\PluginBundle\Entity\Integration`` object through ``\Mautic\IntegrationsBundle\Integration\Interfaces\IntegrationInterface``. It handles decryption and encryption of the Integration's API keys, so the implementing code never has to.

----

.. toctree::
    :caption: Integration Framework
    :hidden:

    register
    integrations
    authentication
    builder
    configuration
    migrations
    sync
