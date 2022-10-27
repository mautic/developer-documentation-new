Points
######

.. vale off

Point Actions
*************

.. vale on

A custom Point Action used to give a Contact `x` Points for doing a certain action.

Mautic dispatches the Event ``\Mautic\PointBundle\PointEvents::POINT_ON_BUILD`` for Plugins to register their custom point action. Listeners receive a ``Mautic\PointBundle\Event\PointBuilderEvent`` object. Register the Event using the ``addAction`` method as described below.

.. php:class:: Mautic\PointBundle\Event\PointBuilderEvent

.. php:method:: public function addAction(string $key, array $action)

    :param string $key: Unique key for the Action.
    :param array $action: :ref:`Action definition<Custom Point Action definition>`.

.. php:method:: public getActions()

    :return: Array of registered Actions.
    :returntype: array


In order for the custom Point Action to work, add something like the following in the code logic when the Contact executes the custom action::

    $this->getModel('point')->triggerAction('helloworld.action', $event->getHit());

.. vale off

Custom Point Action definition
==============================

.. vale on

.. list-table::
    :header-rows: 1

    * - Key
      - Required
      - Type
      - Description
    * - ``label``
      - REQUIRED
      - string
      - The language string for the option in the dropdown
    * - ``formType``
      - OPTIONAL
      - string
      - The alias of a custom Form type used to set config options.
    * - ``formTypeOptions``
      - OPTIONAL
      - array[]
      - Array of options to include into the ``formType``’s $options argument
    * - ``formTypeCleanMasks``
      - OPTIONAL
      - array[]
      - Array of input masks to clean a values from ``formType``
    * - ``formTypeTheme``
      - OPTIONAL
      - string
      - Theme to customize elements for ``formType``
    * - ``template``
      - OPTIONAL
      - string
      - View template used to render the ``formType``
    * - ``callback``
      - OPTIONAL
      - mixed
      - Static callback function used to validate the action. Return true to add the Points to the Contact.

.. vale off

Point Triggers
**************

.. vale on

A custom Point Trigger used to execute a specific action once a Contact hits X number of Points.

Mautic dispatches the Event ``\Mautic\PointBundle\PointEvents::TRIGGER_ON_BUILD`` for Plugins to register their custom point triggers. Listeners receive a ``Mautic\PointBundle\Event\TriggerBuilderEvent`` object. Register the Event using the ``addEvent`` method as described below.

.. php:class:: Mautic\PointBundle\Event\TriggerBuilderEvent

.. php:method:: public function addEvent(string $key, array $action)

    :param string $key: Unique key for the Action.
    :param array $action: :ref:`Action definition<Custom Point Trigger definition>`.

.. php:method:: public getEvents()

    :return: Array of registered Events.
    :returntype: array

.. vale off

Custom Point Trigger definition
===============================

.. vale on

.. list-table::
    :header-rows: 1

    * - Key
      - Required
      - Type
      - Description
    * - ``label``
      - REQUIRED
      - string
      - The language string for the option in the dropdown
    * - ``formType``
      - OPTIONAL
      - string
      - The alias of a custom Form type used to set config options.
    * - ``formTypeOptions``
      - OPTIONAL
      - array[]
      - Array of options to include into the ``formType``'s $options argument
    * - ``formTypeCleanMasks``
      - OPTIONAL
      - array[]
      - Array of input masks to clean a values from ``formType``
    * - ``formTypeTheme``
      - OPTIONAL
      - string
      - Theme to customize elements for ``formType``
    * - ``template``
      - OPTIONAL
      - string
      - View template used to render the ``formType``
    * - ``callback``
      - OPTIONAL
      - mixed
      - Static callback function used to execute the custom action.