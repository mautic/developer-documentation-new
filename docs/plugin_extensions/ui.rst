UI - User Interface
###################

.. vale off

.. note::

   The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. You can still access it in the :xref:`legacy repository`.

   If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

   Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

.. vale off

Injecting buttons
*****************

.. vale on

Mautic dispatches the event ``\Mautic\CoreBundle\CoreEvents::VIEW_INJECT_CUSTOM_BUTTONS`` for Plugins to register their buttons. Listeners receive a ``Mautic\CoreBundle\Event\CustomButtonEvent`` object. Register the event using the ``addButton`` method as described below.

.. php:class:: Mautic\CoreBundle\Event\CustomButtonEvent

    .. php:method:: public function getLocation()

        :return: Requested location for the button.

    .. php:method:: public function getButtons()

        :return: Array of registered buttons.
        :returntype: array

    .. php:method:: public function addButtons(array $buttons, $location = null, $route = null)

        :param array[] $buttons: Array of buttons.
        :param string $location: Location of the button to be placed.
        :param string $route: Route.

    .. php:method:: public function addButton(array $button, $location = null, $route = null)

        :param array[] $button: :ref:`Details for button<components/ui:Button Array Format>`.
        :param string $location: Location of the button to be placed.
        :param string $route: Route.

A Plugin can inject the buttons into five places in Mautic's UI.

.. list-table::
    :header-rows: 1

    *   - Location
        - Description
    *   - ``\Mautic\CoreBundle\Templating\Helper\ButtonHelper::LOCATION_LIST_ACTIONS``
        - Drop down actions per each item in list views.
    *   - ``\Mautic\CoreBundle\Templating\Helper\ButtonHelper::LOCATION_TOOLBAR_ACTIONS``
        - Top right preceding list view tables to the right of the table filter. Preferably buttons with icons only.
    *   - ``\Mautic\CoreBundle\Templating\Helper\ButtonHelper::LOCATION_PAGE_ACTIONS``
        - Main UI buttons to the right of the title: new, edit, and so forth. Primary buttons display as buttons, and the others appear in a drop-down.
    *   - ``\Mautic\CoreBundle\Templating\Helper\ButtonHelper::LOCATION_NAVBAR``
        - Top of the UI to the left of the account/profile menu. Buttons with text and/or icons.
    *   - ``\Mautic\CoreBundle\Templating\Helper\ButtonHelper::LOCATION_BULK_ACTIONS``
        - Buttons inside the bulk drop-down, around the ``checkall`` checkbox of lists.

Buttons use a priority system to determine the order.
The higher the priority, the button displayed closer to first the button.
The lower the priority, the button displayed closer to the last.
For a button drop-down, setting a button as ``primary`` displays the button in the button group rather than the drop-down.

.. vale off

Registering Integration to inject buttons
=========================================

.. vale on

.. code-block:: php

    <?php
    // plugins/HelloWorldBundle/Event/ButtonSubscriber.php

    namespace MauticPlugin\HelloWorldBundle\EventListener;


    use Mautic\CoreBundle\CoreEvents;
    use Mautic\CoreBundle\Event\CustomButtonEvent;
    use Mautic\CoreBundle\EventListener\CommonSubscriber;
    use Mautic\CoreBundle\Templating\Helper\ButtonHelper;
    use Mautic\LeadBundle\Entity\Lead;

    class ButtonSubscriber extends CommonSubscriber
    {
        public static function getSubscribedEvents()
        {
            return [
                CoreEvents::VIEW_INJECT_CUSTOM_BUTTONS => ['injectViewButtons', 0]
            ];
        }

        /**
         * @param CustomButtonEvent $event
         */
        public function injectViewButtons(CustomButtonEvent $event)
        {
            // Injects a button into the toolbar area for any page with a high priority (displays closer to first)
            $event->addButton(
                [
                    'attr'      => [
                        'class'       => 'btn btn-default btn-sm btn-nospin',
                        'data-toggle' => 'ajaxmodal',
                        'data-target' => '#MauticSharedModal',
                        'href'        => $this->router->generate('mautic_world_action', ['objectAction' => 'doSomething']),
                        'data-header' => 'Extra Button',
                    ],
                    'tooltip'   => $this->translator->trans('mautic.world.dosomething.btn.tooltip'),
                    'iconClass' => 'fa fa-star',
                    'priority'  => 255,
                ],
                ButtonHelper::LOCATION_TOOLBAR_ACTIONS
            );

            //
            if ($lead = $event->getItem()) {
                if ($lead instanceof Lead) {
                    $sendEmailButton = [
                        'attr'      => [
                            'data-toggle' => 'ajaxmodal',
                            'data-target' => '#MauticSharedModal',
                            'data-header' => $this->translator->trans(
                                'mautic.world.dosomething.header',
                                ['%email%' => $event->getItem()->getEmail()]
                            ),
                            'href'        => $this->router->generate(
                                'mautic_world_action',
                                ['objectId' => $event->getItem()->getId(), 'objectAction' => 'doSomething']
                            ),
                        ],
                        'btnText'   => 'Extra Button',
                        'iconClass' => 'fa fa-star',
                        'primary'   => true,
                        'priority'  => 255,
                    ];

                    // Inject a button into the page actions for the specified route (in this case /s/contacts/view/{contactId})
                    $event
                        ->addButton(
                            $sendEmailButton,
                            // Location of where to inject the button; this can be an array of multiple locations
                            ButtonHelper::LOCATION_PAGE_ACTIONS,
                            ['mautic_contact_action', ['objectAction' => 'view']]
                        )
                        // Inject a button into the list actions for each contact on the /s/contacts page
                        ->addButton(
                            $sendEmailButton,
                            ButtonHelper::LOCATION_LIST_ACTIONS,
                            'mautic_contact_index'
                        );
                }
            }
        }
    }

.. vale off

Button array format
===================

.. vale on

The array defining the button can include the following keys:

.. list-table::
    :header-rows: 1

    *   - Key
        - Type
        - Description
    *   - ``attr``
        - array[]
        - Array of attributes to appended to the button (data attributes, href, etc)
    *   - ``btnText``
        - string
        - Text to display for the button
    *   - ``iconClass``
        - string
        - Font Awesome class to use as the icon within the button
    *   - ``tooltip``
        - string
        - Text to display as a tooltip
    *   - ``primary``
        - boolean
        - For button drop-down formats, this displays the button in the group rather than in the drop-down
    *   - ``priority``
        - int
        - Determines the order of buttons. The higher the priority, the button displayed closer to the first button. Buttons with the same priority get ordered alphabetically.

If a button is to display a confirmation modal, the key ``confirm``  is a must. A ``confirm`` array  can have the following keys:

.. list-table::
    :header-rows: 1

    *   - Key
        - Type
        - Description
    *   - ``message``
        - string
        - Translated message to display in the confirmation window
    *   - ``confirmText``
        - string
        - Text to display as the confirm button
    *   - ``confirmAction``
        - string
        - href of the button
    *   - ``cancelText``
        - string
        - Text to display as the cancel button
    *   - ``cancelCallback``
        - string
        - Mautic namespaced JavaScript method to execute when the cancel button clicked.
    *   - ``confirmCallback``
        - string
        - Mautic namespaced JavaScript method to execute when the confirm button clicked
    *   - ``precheck``
        - string
        - Mautic namespaced JavaScript method to executed before displaying the confirmation modal
    *   - ``btnClass``
        - string
        - Class for the button
    *   - ``iconClass``
        - string
        - Font Awesome class to use as the icon
    *   - ``btnTextAttr``
        - string
        - string of attributes to append to the button's inner text
    *   - ``attr``
        - array[]
        - Array of attributes to append to the button's outer tag
    *   - ``tooltip``
        - string
        - Translated string to display as a tooltip
    *   - ``tag``
        - string
        - Tag to use as the button. Defaults to an ``a`` tag.
    *   - ``wrapOpeningTag``
        - string
        - Tag or HTML to wrap the button in. Defaults to nothing.
    *   - ``wrapClosingTag``
        - string
        - Tag or HTML to close ``wrapOpeningTag``. Defaults to nothing.

On the same nested level as the ``confirm`` key can include ``primary`` and/or ``priority``.

.. vale off

Defining button locations
*************************

.. vale on

.. code-block:: php

    <?php
    $dropdownOpenHtml = '<button type="button" class="btn btn-default btn-nospin  dropdown-toggle" data-toggle="dropdown" aria-expanded="false"><i class="fa fa-caret-down"></i></button>'
              ."\n";
    $dropdownOpenHtml .= '<ul class="dropdown-menu dropdown-menu-right" role="menu">'."\n";

    echo $view['buttons']->reset($app->getRequest(), 'custom_location')->renderButtons($dropdownOpenHtml, '</ul>');


A Plugin can define its own locations that other Plugins can leverage by using the template ``buttons`` helper.

There are three types of button groups supported:

.. list-table::
    :header-rows: 1

    *   - Type
        - Description
    *   - ``\Mautic\CoreBundle\Templating\Helper\ButtonHelper::TYPE_BUTTON_DROPDOWN``
        - Primary buttons renders in a button group while others in a drop-down menu.
    *   - ``\Mautic\CoreBundle\Templating\Helper\ButtonHelper::TYPE_DROPDOWN``
        - Buttons displayed in a drop-down menu.
    *   - ``\Mautic\CoreBundle\Templating\Helper\ButtonHelper::TYPE_GROUP``
        - A group of buttons side by side.

Drop-downs require the wrapping HTML to pass to the ``renderButtons`` method.