Mautic API V2
#############

A Quick Overview
****************

Mautic introduces a powerful new REST API built on the robust **API Platform** framework.
This modern API provides a more flexible, standardized, and well-documented way to interact with your Mautic data.

----

Accessing the API
*****************

To access the new API, you will need to be authenticated within your Mautic instance.

The base endpoint for the new API is:  ``/api/v2``

Once you are authenticated, you can start making requests to this endpoint to interact with your Mautic data.

----

API Documentation and Discovery
*******************************

The new Mautic API is self-documenting.
This means that you can simply navigate to the ``/api/v2`` endpoint in your web browser while logged into Mautic, and you will be presented with comprehensive and interactive API documentation.

This documentation provides a detailed list of all available API endpoints, the HTTP methods they support (GET, POST, PUT, DELETE, etc.), and the parameters they accept.
You can even use this interface to test API calls directly from your browser.


The API supports modern features such as:

* **Pagination:** Results are paginated by default for efficient data retrieval.
* **Multiple Data Formats:** The API supports various data formats, including JSON-LD, standard JSON and text/html.
