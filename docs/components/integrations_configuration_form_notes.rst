.. It is a reference only page, not a part of doc tree.

:orphan:

.. vale off

Integration configuration form notes
####################################

.. vale on

The Integration framework lets developer define their custom messages for the Plugin's configuration Form.

The ``ConfigSupport`` class should implement the ``\Mautic\IntegrationsBundle\Integration\Interfaces\ConfigFormNotesInterface``

.. php:interface:: \Mautic\IntegrationsBundle\Integration\Interfaces\ConfigFormNotesInterface

.. php:method:: public function getAuthorizationNote(): ?Note

    :return: The message and type for Auth tab.
    :returntype: :ref:`Note<components/integrations_configuration_form_notes:Note Object>`

.. php:method:: public function getFeaturesNote(): ?Note

    :return: The message and type for Features tab.
    :returntype: :ref:`Note<components/integrations_configuration_form_notes:Note Object>`

.. php:method:: public function getFieldMappingNote(): ?Note

    :return: The message and type for Field Mapping tab.
    :returntype: :ref:`Note<components/integrations_configuration_form_notes:Note Object>`

_____

.. vale off

Note Object
***********

.. vale:on

.. php:class:: \Mautic\IntegrationsBundle\DTO\Note

.. php:attr:: public note;

.. php:attr:: public type;

.. php:method:: public function getNote(): string

    :return: The string to display.
    :returntype: string

.. php:method:: public function getType(): string

    :return: The note type, this helps annotate the note.
    :returntype: string

The following code snippet shows the use of ``\Mautic\IntegrationsBundle\Integration\Interfaces\ConfigFormNotesInterface``.

 .. code-block:: php

    <?php

    declare(strict_types=1);

    namespace MauticPlugin\HelloWorldBundle\Integration\Support;

    use Mautic\IntegrationsBundle\DTO\Note;
    use Mautic\IntegrationsBundle\Integration\ConfigFormNotesTrait;
    use Mautic\IntegrationsBundle\Integration\DefaultConfigFormTrait;
    use Mautic\IntegrationsBundle\Integration\Interfaces\ConfigFormAuthInterface;
    use Mautic\IntegrationsBundle\Integration\Interfaces\ConfigFormFeatureSettingsInterface;
    use Mautic\IntegrationsBundle\Integration\Interfaces\ConfigFormFeaturesInterface;
    use Mautic\IntegrationsBundle\Integration\Interfaces\ConfigFormInterface;
    use Mautic\IntegrationsBundle\Integration\Interfaces\ConfigFormNotesInterface;
    use Mautic\IntegrationsBundle\Integration\Interfaces\ConfigFormSyncInterface;
    use MauticPlugin\HelloWorldBundle\Form\Type\ConfigAuthType;
    use MauticPlugin\HelloWorldBundle\Form\Type\ConfigFeaturesType;
    use MauticPlugin\HelloWorldBundle\Integration\HelloWorldIntegration;

    class ConfigSupport extends HelloWorldIntegration implements ConfigFormInterface, ConfigFormAuthInterface, ConfigFormFeatureSettingsInterface, ConfigFormSyncInterface, ConfigFormFeaturesInterface, ConfigFormNotesInterface
    {
        use DefaultConfigFormTrait;
        use ConfigFormNotesTrait;

        public function getAuthConfigFormName(): string
        {
            return ConfigAuthType::class;
        }

        public function getFeatureSettingsConfigFormName(): string
        {
            return ConfigFeaturesType::class;
        }

        // ...

        /**
         * Adds message to the Enable/Auth tab.
         */
        public function getAuthorizationNote(): ?Note
        {
            return new Note('Additional information for Authorization tab.', Note::TYPE_INFO);
        }

        /**
         * Adds message to the Features tab.
         */
        public function getFeaturesNote(): ?Note
        {
            return new Note('Warning message for Features tab.', Note::TYPE_WARNING);
        }

        /**
         * Adds message to the Field Mapping tabs.
         */
        public function getFieldMappingNote(): ?Note
        {
            return new Note('Additional information for Field mapping tab.', Note::TYPE_INFO);
        }
    }

.. admonition:: Additional information

    - The trait ``Mautic\IntegrationsBundle\Integration\ConfigFormNotesTrait`` helps define the default ``null``.
    - Instead of plain string, one can pass the translation key which holds the message. for example ``new Note('helloworld.config.auth_tab', Note::TYPE_INFO);``
