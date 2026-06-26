Point Insights
##############

Use this endpoint to manage Point Insights in Mautic. A Point Insight of type ``compare_point_groups`` compares a Contact's scores across the selected Point Groups and writes the winning Group to a Custom Field on the Contact, using the format ``ID (PointGroupName)``, for example ``47 (Umbrellas)``. Whenever a Contact's Point Group score changes, Mautic re-evaluates every activated Point Insight.

.. note::

   * Mautic 7 introduced Point Insights. The endpoints below require the ``point:insights`` permission set - ``view``, ``create``, ``edit``, ``delete``, ``publish``, and ``full``.
   * The Mautic API Library doesn't support the Point Insights API yet, so use the http endpoints described in this document instead.

.. vale off

Get Point Insight
*****************

.. vale on

Retrieves an individual Point Insight.

.. vale off

HTTP request
============

.. vale on

``GET /points/insights/ID``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Point Insight.

.. _get Point Insight response:

.. code-block:: json

   {
       "insight": {
           "id": 12,
           "name": "Main interest",
           "category": null,
           "description": null,
           "insightType": "compare_point_groups",
           "insightAction": "set_custom_field",
           "customField": "main_interest",
           "pointGroups": [47, 48]
       }
   }

.. _get Point Insight properties:

Point Insight properties
------------------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Point Insight
   * - ``name``
     - string
     - Point Insight name
   * - ``category``
     - object or null
     - Category the Point Insight belongs to, or ``null`` when the Point Insight has no Category
   * - ``description``
     - string or null
     - Point Insight description
   * - ``insightType``
     - string
     - Type of comparison the Insight performs. Currently ``compare_point_groups`` is the only supported value
   * - ``insightAction``
     - string
     - Action taken with the result. Currently ``set_custom_field`` is the only supported value
   * - ``customField``
     - string or null
     - Alias of the text Custom Field that receives the winning Point Group, in the format ``ID (PointGroupName)``
   * - ``pointGroups``
     - array
     - IDs of the Point Groups that the Insight compares

.. vale off

List Point Insights
*******************

.. vale on

Retrieves a list of Point Insights.

.. vale off

HTTP request
============

.. vale on

``GET /points/insights``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Point Insights list.

.. code-block:: json

   {
     "total": 1,
     "insights": [
       {
           "id": 12,
           "name": "Main interest",
           "category": null,
           "description": null
       },
       // ...
     ]
   }

Properties
----------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``total``
     - int
     - Total count of Point Insights
   * - ``insights``
     - array
     - Array of Point Insights

The list response returns the ``id``, ``name``, ``category``, and ``description`` of each Point Insight. Request a single Point Insight to retrieve the ``insightType``, ``insightAction``, ``customField``, and ``pointGroups`` properties.

.. vale off

For the rest of the properties, refer to :ref:`Point Insight properties <get Point Insight properties>`.

.. vale on

.. vale off

Create Point Insight
********************

.. vale on

Creates a new Point Insight.

.. code-block:: json

   {
       "name": "Main interest",
       "description": "Sets the Contact's main interest field.",
       "insightType": "compare_point_groups",
       "insightAction": "set_custom_field",
       "customField": "main_interest",
       "pointGroups": [47, 48]
   }

.. vale off

HTTP request
============

.. vale on

``POST /points/insights/new``

.. _create Point Insight POST parameters:

POST parameters
---------------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``name``
     - string
     - **Required.**

       Point Insight name.
   * - ``description``
     - string
     - A description of the Point Insight
   * - ``insightType``
     - string
     - Type of comparison. Defaults to ``compare_point_groups``
   * - ``insightAction``
     - string
     - Action taken with the result. Defaults to ``set_custom_field``
   * - ``customField``
     - string
     - Alias of the text Custom Field that receives the winning Point Group
   * - ``pointGroups``
     - array
     - Array of Point Group IDs to compare

.. note::

   The API doesn't validate ``customField`` and ``pointGroups``. A Point Insight does nothing until ``customField`` references an existing text Custom Field and ``pointGroups`` contains valid Point Group IDs.

Response
========

* Returns ``201 Created`` when the request successfully creates a Point Insight.

Properties
----------

Refer to :ref:`Point Insight properties <get Point Insight properties>`.

.. vale off

Edit Point Insight
******************

.. vale on

Edits a Point Insight.

This operation supports ``PUT`` or ``PATCH`` depending on the desired behavior:

* ``PUT``: **full replacement**. The request creates a new Point Insight if the ID is missing. If the ID exists, the request clears all existing data and replaces it with the provided values.
* ``PATCH``: **partial update**. The request only updates field values based on the request data. The request fails when the Point Insight ID doesn't exist.

.. code-block:: json

   {
       "name": "Main interest",
       "pointGroups": [47, 48, 49]
   }

.. vale off

HTTP request
============

.. vale on

* ``PUT /points/insights/ID/edit``: updates an existing Point Insight, or creates a new one when the ID doesn't exist.
* ``PATCH /points/insights/ID/edit``: updates an existing Point Insight. The request fails when the ID doesn't exist.

POST parameters
---------------

Accepts the same parameters as those described in :ref:`Create Point Insight <create Point Insight POST parameters>`. All parameters are optional.

Response
========

* ``PUT``: returns ``200 OK`` when the request successfully updates the Point Insight, or ``201 Created`` when the request creates a Point Insight.
* ``PATCH``: returns ``200 OK`` when the request successfully updates the Point Insight, or a ``404 Not Found`` error when the Point Insight ID doesn't exist.

Properties
----------

Refer to :ref:`Point Insight properties <get Point Insight properties>`.

.. vale off

Delete Point Insight
********************

.. vale on

Deletes a Point Insight.

.. vale off

HTTP request
============

.. vale on

``DELETE /points/insights/ID/delete``

Response
========

* Returns ``200 OK`` when the request successfully deletes the Point Insight.

The response is a JSON object containing the data of the deleted Point Insight, similar to :ref:`Get Point Insight <get Point Insight response>`.

Properties
----------

Refer to :ref:`Point Insight properties <get Point Insight properties>`.
