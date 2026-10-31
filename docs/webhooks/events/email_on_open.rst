Email open event
################

Triggered when a Contact presumably opens an Email.

.. Note:: Email clients may load the tracking pixel through a proxy or scanned by bots and so may not be a reliable metric.

.. _email_on_open_event_type:

Event type
**********

``mautic.email_on_open``

.. _email_on_open_event_properties:

Event properties
****************

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``stat``
      - object
      - The :ref:`Email stat object<Webhooks/events/email_on_open:Email stat properties>` that records the Email send and its opens.
    * - ``timestamp``
      - string
      - Date/time the event occurred in ISO 8601 format.

Email stat properties
*********************

.. list-table::
    :header-rows: 1

    * - Key
      - Type
      - Description
    * - ``id``
      - int
      - ID of the Email stat.
    * - ``emailAddress``
      - string
      - Email address Mautic sent the Email to.
    * - ``ipAddress``
      - object|null
      - IP address record of the open.
    * - ``dateSent``
      - string|null
      - Date/time Mautic sent the Email in ISO 8601 format.
    * - ``isRead``
      - boolean
      - ``true`` if Mautic has recorded an open for this send.
    * - ``isFailed``
      - boolean
      - ``true`` if the send failed.
    * - ``dateRead``
      - string|null
      - Date/time of the first recorded open in ISO 8601 format.
    * - ``retryCount``
      - int|null
      - Number of times Mautic retried the send.
    * - ``source``
      - string|null
      - The Component that sent the Email, such as ``campaign.event``.
    * - ``sourceId``
      - int|null
      - ID of the Component that sent the Email.
    * - ``openCount``
      - int|null
      - Number of recorded opens.
    * - ``lastOpened``
      - string|null
      - Date/time of the most recent recorded open in ISO 8601 format.
    * - ``trackingHash``
      - string|null
      - Unique hash that identifies this send in tracking URLs.
    * - ``viewedInBrowser``
      - boolean
      - ``true`` if the Contact opened the Email's web version.
    * - ``lead``
      - object|null
      - The Contact the Email went to. Contains only the Contact's ``id``, ``points``, ``color``, and ``fields``. See :ref:`Contact object<Webhooks/events/lead_post_save_new:Contact properties>` for these properties.
    * - ``email``
      - object|null
      - The :ref:`Email object<Webhooks/events/email_on_send:Email properties>` the Contact opened. Mautic leaves out ``customHtml`` and ``plainText`` if you turn off the ``Send Email details`` Webhook Setting.
