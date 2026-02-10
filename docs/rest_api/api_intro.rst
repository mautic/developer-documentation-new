Introduction
############

.. vale off

.. note::

  The content for this page requires a major update. The legacy page contains outdated and potentially inaccurate information. But you can still access it in the :xref:`legacy repository`.

  If you're interested in helping develop the new content for this page and others, consider joining the documentation efforts.

  Please read the :xref:`dev docs contributing guidelines` and :xref:`Contributing to Mautic’s documentation` to get started.

.. vale on

Mautic provides a REST API to manipulate and obtain information for various entities of Mautic.

.. warning::

   All Mautic API endpoints require an OAuth1a signtature or OAuth2 access token.

Error handling
**************

If there's an OAuth error, you should see a JSON encoded array similar to:

.. code-block:: JSON

   {
      "error": "invalid_grant",
      "error_description": "The access token provided has expired."
   }

If a system error encountered, you should see a JSON encoded array similar to:

.. code-block:: JSON

   {
      "error": {
        "message": "You do not have access to the requested area/action.",
        "code": 403
      }
   }

Mautic version check
********************

In case your API service wants to support several Mautic versions with different features, you might need to check the version of Mautic you communicate with. Since Mautic ``2.4.0``, the version number is added to all API response headers. The header name is ``Mautic-Version``.

You can get the Mautic version with Mautic PHP API library:

.. code-block:: text

   // Make any API request:
   $api = $this->getContext('contacts');
   $response = $api->getList('', 0, 1);

   // Get the version number from the response header:
   $version = $api->getMauticVersion();

The ``$version`` is in a semantic versioning format of ``[major].[minor].[patch]`` - for example, ``2.4.0``. If you try it on the latest GitHub version, the version has a suffix ``-dev``, such as ``2.5.1-dev``.

API endpoints
*************

All responses are JSON encoded.

The base API endpoint is ``https://your-mautic.com/api``.