Translating plugins
===================

Plugins include their own translations in their ``Translations`` directories organized by locale. Currently, only :xref:`Core translations are supported through Transifex<Translating Mautic>`. See :ref:`Translator` for information on writing translations and using the Translator service in your Plugin.

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
