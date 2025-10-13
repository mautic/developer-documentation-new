Mautic API v2
#############

A quick overview
****************

Mautic introduces a powerful new REST API built on the robust **API Platform** framework.
This modern API provides a more flexible, standardized, and well-documented way to interact with your Mautic data.

----

Accessing the API
*****************

To access the new API, you must authenticate within your Mautic instance.

The base endpoint for the new API is:  ``/api/v2``

Once you authenticate, you can start making requests to this endpoint to interact with your Mautic data.

----

API documentation and discovery
*******************************

The new Mautic API is self-documenting.
This means that you can simply navigate to the ``/api/v2`` endpoint in your web browser while logged into Mautic, and you see comprehensive and interactive API documentation.

This documentation provides a detailed list of all available API endpoints, the http methods they support (GET, POST, PUT, DELETE, etc.), and the parameters they accept.
You can even use this interface to test API calls directly from your browser.


The API supports modern features such as:

* **Pagination:** the API paginates results by default for efficient data retrieval.
* **Multiple Data Formats:** the API supports various data formats, including JSON-LD, standard JSON and text/HTML.
