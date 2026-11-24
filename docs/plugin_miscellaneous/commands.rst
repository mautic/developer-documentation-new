Commands
########

You can add new console commands to your Plugin using :xref:`Symfony Console Component`. A command lives in your Plugin's ``Command`` directory and extends ``Symfony\Component\Console\Command\Command``.

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/Command/WorldCommand.php

    namespace MauticPlugin\HelloWorldBundle\Command;

    use Symfony\Component\Console\Attribute\AsCommand;
    use Symfony\Component\Console\Command\Command;
    use Symfony\Component\Console\Input\InputInterface;
    use Symfony\Component\Console\Output\OutputInterface;

    #[AsCommand(
        name: 'mautic:helloworld:greet',
        description: 'Greets the world.'
    )]
    class WorldCommand extends Command
    {
        protected function execute(InputInterface $input, OutputInterface $output): int
        {
            $output->writeln('Hello, world!');

            return Command::SUCCESS;
        }
    }

Registering commands
====================

Since Mautic 5, Autowiring and autoconfiguration handle commands for you, so you don't need to register them in your Plugin's ``config.php`` file. Mautic automatically tags any service that extends the Symfony ``Command`` class with ``console.command``. If you turn off autoconfiguration for your Plugin, register the command manually under the ``commands`` key in ``config.php``, which Mautic tags with :xref:`Symfony as a console command<Symfony console command tag>`.

Moderated commands
==================

Some commands shouldn't run more than one instance at a time, such as those that process queues or send scheduled Broadcasts. Extend ``Mautic\CoreBundle\Command\ModeratedCommand`` to lock the command so that only a single instance runs concurrently. Call ``checkRunStatus()`` at the start of ``execute()`` to acquire the lock, then call ``completeRun()`` once the work finishes to release it.

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/Command/WorldCommand.php

    namespace MauticPlugin\HelloWorldBundle\Command;

    use Mautic\CoreBundle\Command\ModeratedCommand;
    use Symfony\Component\Console\Attribute\AsCommand;
    use Symfony\Component\Console\Command\Command;
    use Symfony\Component\Console\Input\InputInterface;
    use Symfony\Component\Console\Output\OutputInterface;

    #[AsCommand(
        name: 'mautic:helloworld:greet',
        description: 'Greets the world.'
    )]
    class WorldCommand extends ModeratedCommand
    {
        protected function execute(InputInterface $input, OutputInterface $output): int
        {
            // Stop here if another instance of this command is already running.
            if (!$this->checkRunStatus($input, $output)) {
                return Command::SUCCESS;
            }

            // Do the work.
            $output->writeln('Hello, world!');

            // Release the lock.
            $this->completeRun();

            return Command::SUCCESS;
        }
    }

``ModeratedCommand`` adds the ``--bypass-locking``, ``--timeout``, and ``--lock_mode`` options and locks on the command name by default. When a single command needs to run in parallel for different targets, such as one lock per entity ID, pass a ``$moderationKey`` as the third argument to ``checkRunStatus()``.
