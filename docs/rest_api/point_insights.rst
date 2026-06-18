Point Insights
##############

Use this endpoint to manage Point Insights in Mautic. A Point Insight of type ``compare_point_groups`` compares a Contact's scores across the selected Point Groups and writes the winning Group to a Custom Field on the Contact, using the format ``ID (PointGroupName)``, for example ``47 (Umbrellas)``. Whenever a Contact's Point Group score changes, Mautic re-evaluates every published Point Insight.

.. note::

   Point Insights were added in Mautic 7. The endpoints below require the ``point:insights`` permission set (``view``, ``create``, ``edit``, ``delete``, ``publish`` and ``full``).

.. vale off

Get Point Insight
*****************

.. vale on

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

Get an individual Point Insight by ID.

.. vale off

**HTTP Request**

.. vale on

``GET /points/insights/ID``

**Response**

``Expected Response Code: 200``

See JSON code example.

**Point Insight Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - ``int``
     - ID of the Point Insight.
   * - ``name``
     - ``string``
     - Point Insight name.
   * - ``category``
     - ``object/null``
     - Category the Point Insight belongs to, or ``null`` when no Category is set.
   * - ``description``
     - ``string/null``
     - Point Insight description.
   * - ``insightType``
     - ``string``
     - Type of comparison the Insight performs. Currently ``compare_point_groups`` is the only supported value.
   * - ``insightAction``
     - ``string``
     - Action taken with the result. Currently ``set_custom_field`` is the only supported value.
   * - ``customField``
     - ``string/null``
     - Alias of the text Custom Field that receives the winning Point Group, in the format ``ID (PointGroupName)``.
   * - ``pointGroups``
     - ``array``
     - IDs of the Point Groups that the Insight compares.

.. vale off

List Point Insights
*******************

.. vale on

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
        ...
      ]
    }

.. vale off

**HTTP Request**

.. vale on

``GET /points/insights``

**Response**

``Expected Response Code: 200``

See JSON code example. The list response returns the ``id``, ``name``, ``category`` and ``description`` of each Point Insight. Request a single Point Insight to retrieve the ``insightType``, ``insightAction``, ``customField`` and ``pointGroups`` properties.

.. vale off

Create Point Insight
********************

.. vale on

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

**HTTP Request**

.. vale on

``POST /points/insights/new``

.. vale off

**Post Parameters**

.. vale on

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - ``name``
     - Point Insight name. This is the only required field.
   * - ``description``
     - A description of the Point Insight.
   * - ``insightType``
     - Type of comparison. Defaults to ``compare_point_groups``.
   * - ``insightAction``
     - Action taken with the result. Defaults to ``set_custom_field``.
   * - ``customField``
     - Alias of the text Custom Field that receives the winning Point Group.
   * - ``pointGroups``
     - Array of Point Group IDs to compare.

.. note::

   ``customField`` and ``pointGroups`` aren't validated at the API level. A Point Insight does nothing until ``customField`` references an existing text Custom Field and ``pointGroups`` contains valid Point Group IDs.

**Response**

``Expected Response Code: 201``

**Properties**

Same as `Get Point Insight`.

.. vale off

Edit Point Insight
******************

.. vale on

.. code-block:: json

    {
        "name": "Main interest",
        "pointGroups": [47, 48, 49]
    }

.. vale off

**HTTP Request**

.. vale on

To edit a Point Insight and return a 404 if the Point Insight isn't found:

``PATCH /points/insights/ID/edit``

To edit a Point Insight, or create a new one if it doesn't exist:

``PUT /points/insights/ID/edit``

.. note::

   When using ``PUT``, fields not supplied in the request are reset to their defaults. ``PATCH`` only updates the fields you supply.

.. vale off

**Post Parameters**

.. vale on

Same as `Create Point Insight`.

**Response**

If editing with ``PATCH`` or editing an existing Point Insight with ``PUT``:

``Expected Response Code: 200``

If creating a new Point Insight with ``PUT``:

``Expected Response Code: 201``

**Properties**

Same as `Get Point Insight`.

.. vale off

Delete Point Insight
********************

.. vale on

.. vale off

**HTTP Request**

.. vale on

``DELETE /points/insights/ID/delete``

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get Point Insight`.
