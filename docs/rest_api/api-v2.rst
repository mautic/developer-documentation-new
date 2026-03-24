Mautic API v2
#############

A quick overview
****************

Mautic introduces a powerful new REST API built on the robust **API Platform** framework. This modern API provides a more flexible, standardized, and well-documented way to interact with your Mautic data.

Accessing the API
*****************

To access the new API, you must authenticate within your Mautic instance.

The base endpoint for the new API is:  ``/api/v2``.

Once you authenticate, you can start making requests to this endpoint to interact with your Mautic data.

API documentation and discovery
*******************************

The new Mautic API is self-documenting. It means that you can navigate to the ``/api/v2`` endpoint in your web browser while logged into Mautic and see comprehensive, interactive API documentation.

.. vale off

This documentation provides a detailed list of all available API endpoints, the supported HTTP methods - such as ``GET``, ``POST``, ``PUT``, or ``DELETE`` - and the accepted parameters. You can use the interface to test API calls directly from your browser.

.. vale on

The API supports modern features such as:

* **Pagination:** the API paginates results by default for efficient data retrieval.
* **Multiple Data Formats:** the API supports various data formats, including JSON-LD, standard JSON and text/HTML.
