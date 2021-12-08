Translator
==============

Mautic leverages a decorated Symfony Translator service for translations.

Visit :xref:`Translating Mautic` for information on how to translate Core. :ref:`Plugins must include their own translations<Translating plugins>`.

Translation file and directory structure
------------------------------------------

Translations are `INI` files organized in the following directory structure for Core bundles and Plugins::

Translations/
    {locale}/
        {:ref:`domain<Translation domains>`}.ini

.. note:: All Core bundles and Plugins must include translations for the US English, en_US, locale.

Mautic loads translations through ``\Mautic\CoreBundle\Loader\TranslationLoader`` where it loads translations in the following order. Note that the value for the key loaded last is what Mautic uses.

#. ``{bundle}/Translations/{locale}/``
#. ``themes/{default_theme}/translations/``
#. ``translations/{locale}/``
#. ``translations/overrides/{locale}/``

.. note:: The loader finds and loads all `INI` files within those directories or their subdirectories.

Translation domains
------------------------

Translation domains organize translations into files. The following are defined by Mautic but the plugin can define and use its own domains by passing the domain into the :php:meth:`Mautic\CoreBundle\Translation\Translator::trans` method.

.. list-table::
    :header-rows: 1

    * - Domain
      - Description
    * - ``messages``
      - Default domain for translations.
    * - ``flashes``
      - Default domain for translations for the ``\Mautic\CoreBundle\Service\FlashBag`` service.
    * - ``validators``
      - Default domain for constraint messages for validations in :ref:`Symfony form field types<Symfony 4 custom form field type tag>`.

Translation strings
------------------------

Translations are key/value pairs in the ``INI`` format. There is no hard and fast rule but, typically, Mautic uses periods, ``.``, to separate domains in translation keys and underscores, ``_``, to separate words. You can also use placeholders for the Translator service to replace with values given by the calling code. Placeholders typically are wrapped in percent signs, ``%``.

.. code-block:: ini

    helloworld.greeting="Welcome %name%!"
    helloworld.form.world_select="Select the world you want to visit."
    helloworld.form.world_select.tooltip="Note that most are visit at your own risk!"
    helloworld.moons.number_of_moons="{0}%world% has no moons|{1}%world% has one moon|]1,Inf[ %world% has %count% moons"

Using the Translator service
-----------------------------

Plugins have access to service by passing ``translator`` as :ref:`a service dependency<Service config items>`. Type-hint the argument in the service's construct with ``Symfony\Component\Translation\TranslatorInterface``.

In PHP templates, use ``$view['translator']`` to access the Translator service.

.. php:class:: Mautic\CoreBundle\Translation\Translator

.. php:method:: trans(string $id[, array $parameters = [], ?string $domain = null, ?string $locale = null])

    Returns the translation for the given key.

    :param array $parameters: Parameters as key/value pairs to populate placeholders in the translation. Note that Symfony has deprecated `transChoice()` in favor of using this method plus defining the key ``%count%`` in ``$parameters``. For example, ``echo $translator->trans('helloworld.number_of_moons', ['%count%' => 1, '%world% => 'Earth']);`` with the translation, ``"helloworld.number_of_moons="{0}%world% has no moons|{1}%world% has one moon|]1,Inf[ %world% has %count% moons"``.
    :param string|null $domain: Specific domain to look for the translation key. Defaults to ``messages`` if ``NULL``.
    :param string|null $locale: Specific locale to look for the translation key. Defaults to system or user configured locale.

    :returns: Returns the translated string if the key is found. Otherwise, an empty string.
    :returntype: string

.. php:method:: transConditional(string $preferred, string $alternative[, array $parameters = [], ?string $domain = null, ?string $locale = null])

    Translates the preferred key if it exists and the alternate key if it does not.

    :param string $preferred: Preferred translation key.
    :param string $alternative: Alternate translation key if the preferred does does not exist.
    :param array $parameters: Parameters as key/value pairs to populate placeholders in the translation.
    :param string|null $domain: Specific domain to look for the translation key. Defaults to ``messages`` if ``NULL``.
    :param string|null $locale: Specific locale to look for the translation key. Defaults to system or user configured locale.

    :returns: Returns the translated string if the key is found. Otherwise, an empty string.
    :returntype: string

.. php:method:: hasId(string $id[, ?string $domain = null, ?string $local = null])

    Checks to see if a translation key exists.

    :param string $id: Translation key. For example, ``mautic.core.empty``.
    :param string|null $domain: Specific domain to search. Defaults to ``messages`` if ``NULL``.
    :param string|null $locale: Specific locale to search. Defaults to system or user configured locale.

    :returns: ``TRUE`` if the translation key exists. ``FALSE`` otherwise.
    :returntype: boolean
