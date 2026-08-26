Installing, upgrading, and uninstalling
#######################################

Mautic informs your Plugin when it gets installed or updated through the ``ON_PLUGIN_INSTALL`` and ``ON_PLUGIN_UPDATE`` events. This can be useful in scenarios where you need to set up certain data structures or do other configuration work. Note that there is currently no hook for when your Plugin gets uninstalled. If that's of interest, please feel free to :xref:`contribute that feature<Contributing to Mautic>`.

.. note:: If your Plugin manages its own schema, Mautic recommends using :ref:`plugins/installation:database migrations` instead of the generic events mentioned earlier.

Install and update events
=========================

.. note:: The events below are available since Mautic 4.2.0.

Since Mautic 8, key your subscriber on the event class, ``PluginInstallEvent::class`` and ``PluginUpdateEvent::class``, rather than on a ``PluginEvents`` constant:

.. code-block:: php

    <?php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\EventListener;

    use Mautic\PluginBundle\Event\PluginInstallEvent;
    use Mautic\PluginBundle\Event\PluginUpdateEvent;
    use Symfony\Component\EventDispatcher\EventSubscriberInterface;

    class InstallUpdateSubscriber implements EventSubscriberInterface
    {
        public static function getSubscribedEvents(): array
        {
            return [
                PluginInstallEvent::class => ['onPluginInstall', 0],
                PluginUpdateEvent::class  => ['onPluginUpdate', 0],
            ];
        }

        public function onPluginInstall(PluginInstallEvent $event)
        {
            // Handle your logic here
        }

        public function onPluginUpdate(PluginUpdateEvent $event)
        {
            // Handle your logic here   
        }
    }

.. note::

   Since Mautic 8, Mautic dispatches these events by the event object alone, so the event's class name serves as the event name, matching the Symfony 4.3 dispatch style. This means:

   * The ``PluginEvents`` constants remain defined in the codebase, but Mautic no longer uses them for dispatch.
   * A subscriber still keyed on a ``PluginEvents`` constant, or on the old event string, fails silently. Mautic throws no exception and logs nothing, so the listener never runs.
   * Before Mautic 8, those ``PluginEvents`` constants were the correct keys.
   * Event families that still dispatch by string constant should keep keying on those constants.

Database migrations
===================

Mautic supports database migrations for Plugins to better manage their schema. Queries are in migration files that match the Plugin's version number in its config. When a Plugin gets installed or upgraded, Mautic loops over the migration files up to the latest version.

Check your Plugin's root bundle class
-------------------------------------

The Plugin's root bundle class should extend ``MauticPlugin\IntegrationsBundle\Bundle\AbstractPluginBundle``:

.. code-block:: php

    <?php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle;

    use Mautic\IntegrationsBundle\Bundle\AbstractPluginBundle;

    class HelloWorldBundle extends AbstractPluginBundle
    {
    }

Plugin migrations
-----------------

Please store migration files in the Plugin's ``Migration`` folder with a name that matches ``Version_X_Y_Z.php`` where ``X_Y_Z`` matches the semantic versioning of the Plugin. Each file should contain the incremental schema changes for the Plugin up to the latest version which should match the version in the Plugin's ``Config/config.php`` file.

There are two methods. ``isApplicable`` should return ``true/false`` if the migration should be ran. ``up`` should register the SQL to execute.

.. code-block:: php

    <?php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\Migrations;

    use Doctrine\DBAL\Schema\Schema;
    use Doctrine\DBAL\Schema\SchemaException;
    use Mautic\IntegrationsBundle\Migration\AbstractMigration;

    class Version_1_0_1 extends AbstractMigration
    {
        private $table = 'hello_world';

        protected function isApplicable(Schema $schema): bool
        {
            try {
                return !$schema->getTable($this->concatPrefix($this->table))->hasColumn('is_enabled');
            } catch (SchemaException $e) {
                return false;
            }
        }

        protected function up(): void
        {
            $this->addSql("ALTER TABLE `{$this->concatPrefix($this->table)}` ADD `is_enabled` tinyint(1) 0");

            $this->addSql("CREATE INDEX {$this->concatPrefix('is_enabled')} ON {$this->concatPrefix($this->table)}(is_enabled);");
        }
    }
