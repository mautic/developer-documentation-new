Translating Plugins
###################

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Plugins include their own translations in their ``Translations`` directories organized by locale. Currently, only :xref:`Core translations are supported through Transifex<Translating Mautic>`. See :ref:`components/translator:Translator` for information on writing translations and using the Translator service in your Plugin.

.. note:: All Plugins must include a US English, en_US, translation.

Below is an example Plugin's translations::

    Translations/
        en_US/
            flashes.ini
            messages.ini
            validators.ini
        es_MX/
            flashes.ini
            messages.ini
            validators.ini
        fr_FR/
            flashes.ini
            messages.ini
            validators.ini
