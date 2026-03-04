Emails
######

Use this endpoint to manipulate and obtain details on Mautic's Emails.

Using the Mautic API library
****************************

.. vale off

You can interact with this API using the :xref:`Mautic API Library` as below, or the various HTTP endpoints described in this document.

.. vale on

.. code-block:: php

   <?php
   use Mautic\MauticApi;
   use Mautic\Auth\ApiAuth;

   // ...
   $initAuth = new ApiAuth();
   $auth     = $initAuth->newAuth($settings);
   $apiUrl   = "https://example.com";
   $api      = new MauticApi();
   $emailApi = $api->newApi("emails", $auth, $apiUrl);

.. vale off

Get Email
*********

.. vale on

Retrieves an individual Email.

.. code-block:: php

   <?php

   //...
   $email = $emailApi->get($id);

.. vale off

HTTP request
============

.. vale on

``GET /emails/ID``

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Email.

.. _get Email response:

.. code-block:: json

   {
      "email": {
          "isPublished": true,
          "dateAdded": "2026-02-19T04:17:46+00:00",
          "dateModified": "2026-02-19T14:49:06+00:00",
          "createdBy": 1,
          "createdByUser": "Admin Mautic",
          "modifiedBy": 1,
          "modifiedByUser": "Admin Mautic",
          "id": 1,
          "name": "Acme General Conference Success",
          "subject": "Acme General Conference Success",
          "language": "en",
          "category": null,
          "fromAddress": "john.doe@acme.com",
          "fromName": "John Doe",
          "replyToAddress": null,
          "bccAddress": null,
          "useOwnerAsMailer": false,
          "utmTags": {
              "utmSource": null,
              "utmMedium": null,
              "utmCampaign": null,
              "utmContent": null
          },
          "preheaderText": null,
          "customHtml": "",
          "plainText": null,
          "template": "_make-announcement",
          "emailType": "template",
          "publishUp": null,
          "publishDown": null,
          "publicPreview": false,
          "readCount": 0,
          "sentCount": 0,
          "revision": 2,
          "assetAttachments": [],
          "variantStartDate": null,
          "variantSentCount": 0,
          "variantReadCount": 0,
          "variantParent": null,
          "variantChildren": [],
          "translationParent": null,
          "translationChildren": [],
          "unsubscribeForm": null,
          "dynamicContent": [
              {
                  "tokenName": "Dynamic Content 1",
                  "content": "Default Dynamic Content",
                  "filters": [
                      {
                          "content": null,
                          "filters": []
                      }
                  ]
              }
          ],
          "lists": [],
          "headers": [],
          "grapesjsbuilder": {
              "customMjml": "<mjml>\r\n  <mj-head>\r\n\t<!-- CSS-STYLE -->\r\n\t<mj-style inline=\"inline\"> p, li {margin:0 !important; padding:0; line-height:1.4em;}\r\n\t</mj-style>\r\n  </mj-head>\r\n  <!-- BODY -->\r\n  <mj-body background-color=\"#f4f4f4\">\r\n\t<mj-section padding-top=\"40px\" background-color=\"#ffffff\">\r\n\t  <mj-column>\r\n\t\t<mj-text font-size=\"11px\" align=\"center\">\r\n\t\t  <p>\r\n\t\t\t<span data-fr-verified=\"true\"><span data-fr-verified=\"true\" class=\"atwho-inserted\">{webview_text}</span>⁠⁠⁠⁠⁠⁠⁠</span>\r\n\t\t  </p>\r\n\t\t</mj-text>\r\n\t\t<mj-spacer>\r\n\t\t</mj-spacer>\r\n\t\t<mj-image src=\"/app/assets/images/placeholder-logo.png?v5214f417\" width=\"70px\" padding-bottom=\"0px\" padding-top=\"0px\">\r\n\t\t</mj-image>\r\n\t  </mj-column>\r\n\t</mj-section>\r\n\t<mj-section background-color=\"#ffffff\">\r\n\t  <mj-column width=\"550px\">\r\n\t\t<mj-text font-size=\"16px\" align=\"center\" font-style=\"italic\" color=\"#525252\">\r\n\t\t  <p>Ok, let's make an announcement\r\n\t\t  </p>\r\n\t\t</mj-text>\r\n\t\t<mj-spacer height=\"40px\">\r\n\t\t</mj-spacer>\r\n\t\t<mj-text font-size=\"24px\" align=\"center\" font-weight=\"700\">\r\n\t\t  <p>Start customizing your email\r\n\t\t  </p>\r\n\t\t</mj-text>\r\n\t  </mj-column>\r\n\t</mj-section>\r\n\t<mj-section background-color=\"#ffffff\" padding-top=\"0px\">\r\n\t  <mj-column padding-top=\"0px\">\r\n\t\t<mj-image src=\"/app/assets/images/placeholder-image.png?v5214f417\" padding-right=\"0px\" padding-left=\"0px\" padding-bottom=\"0px\" padding-top=\"0px\">\r\n\t\t</mj-image>\r\n\t  </mj-column>\r\n\t</mj-section>\r\n\t<mj-section background-color=\"#ffffff\" padding-top=\"0px\">\r\n\t  <mj-column padding-top=\"0px\">\r\n\t\t<mj-image src=\"/app/assets/images/placeholder-image.png?v5214f417\" padding-top=\"0px\">\r\n\t\t</mj-image>\r\n\t  </mj-column>\r\n\t  <mj-column padding-top=\"0px\">\r\n\t\t<mj-image src=\"/app/assets/images/placeholder-image.png?v5214f417\" padding-top=\"0px\">\r\n\t\t</mj-image>\r\n\t  </mj-column>\r\n\t</mj-section>\r\n\t<mj-section background-color=\"#ffffff\">\r\n\t  <mj-column width=\"550px\">\r\n\t\t<mj-text font-size=\"16px\" align=\"center\">\r\n\t\t  <p>Make your announcements pop with an eye-catching visual, then provide the crucial details for engagement.\r\n\t\t  </p>\r\n\t\t  <p>⁠⁠⁠⁠⁠⁠⁠\r\n\t\t\t<br/>Customize this section by inserting your own images or choosing a striking solid color backdrop.\r\n\t\t  </p>\r\n\t\t</mj-text>\r\n\t\t<mj-spacer height=\"30px\">\r\n\t\t</mj-spacer>\r\n\t\t<mj-divider border-width=\"2px\" border-color=\"#d0d0d0\">\r\n\t\t</mj-divider>\r\n\t\t<mj-spacer height=\"30px\">\r\n\t\t</mj-spacer>\r\n\t\t<mj-text font-size=\"22px\" font-weight=\"700\">\r\n\t\t  <p>Lead with an eye-catching title\r\n\t\t  </p>\r\n\t\t</mj-text>\r\n\t\t<mj-text font-size=\"16px\">\r\n\t\t  <p>Present your news in a brief paragraph. For crucial points, use a bulleted list:\r\n\t\t  </p>\r\n\t\t  <ul>\r\n\t\t\t<li>\r\n\t\t\t  <span class=\"ck-list-bogus-paragraph\"><span class=\"ck-list-bogus-paragraph\">What's on offer</span></span>\r\n\t\t\t</li>\r\n\t\t\t<li>\r\n\t\t\t  <span class=\"ck-list-bogus-paragraph\"><span class=\"ck-list-bogus-paragraph\">Where to find us</span></span>\r\n\t\t\t</li>\r\n\t\t\t<li>\r\n\t\t\t  <span class=\"ck-list-bogus-paragraph\"><span class=\"ck-list-bogus-paragraph\">Timing specifics</span></span>\r\n\t\t\t</li>\r\n\t\t  </ul>\r\n\t\t  <p>Be concise to motivate readers to explore your website for the full story.\r\n\t\t  </p>\r\n\t\t</mj-text>\r\n\t\t<mj-button href=\"https://\" background-color=\"#000000\" inner-padding=\"16px 32px\" border-radius=\"0px 0px 0px 0px\" font-size=\"16px\" align=\"left\">Button\r\n\t\t</mj-button>\r\n\t\t<mj-spacer align=\"center\">\r\n\t\t</mj-spacer>\r\n\t  </mj-column>\r\n\t</mj-section>\r\n\t<mj-section padding-top=\"0\" padding-bottom=\"20px\" background-color=\"#000000\">\r\n\t  <mj-column>\r\n\t\t<mj-spacer height=\"40px\">\r\n\t\t</mj-spacer>\r\n\t\t<mj-image src=\"/app/assets/images/placeholder-logo-inverse.png?v5214f417\" width=\"70px\" padding-bottom=\"0px\">\r\n\t\t</mj-image>\r\n\t\t<mj-spacer>\r\n\t\t</mj-spacer>\r\n\t\t<mj-text font-family=\"Ubuntu, Helvetica, Arial, sans-serif\" line-height=\"1.5\" align=\"center\" padding-top=\"0px\" padding-bottom=\"0px\" font-size=\"12px\" color=\"white\">\r\n\t\t  <p>Amazing Company\r\n\t\t\t<br/>11111 Beautiful City, 1212 Nice Street\r\n\t\t\t<br/>Brazil\r\n\t\t\t<br/>\r\n\t\t  </p>\r\n\t\t</mj-text>\r\n\t\t<mj-spacer>\r\n\t\t</mj-spacer>\r\n\t\t<mj-text font-size=\"11px\" align=\"center\" color=\"#a1a1a1\">\r\n\t\t  <p>Fancy seeing you down here. You’re getting this email because you gave us your email address.\r\n\t\t  </p>\r\n\t\t  <p>Want to change how you receive these emails?\r\n\t\t  </p>\r\n\t\t</mj-text>\r\n\t\t<mj-text font-size=\"11px\" align=\"center\" color=\"#a1a1a1\">\r\n\t\t  <p>\r\n\t\t\t<span data-fr-verified=\"true\"><span data-fr-verified=\"true\" class=\"atwho-inserted\">{unsubscribe_text}</span>⁠⁠⁠⁠⁠⁠⁠</span>\r\n\t\t  </p>\r\n\t\t</mj-text>\r\n\t\t<mj-spacer>\r\n\t\t</mj-spacer>\r\n\t  </mj-column>\r\n\t</mj-section>\r\n  </mj-body>\r\n</mjml>\r\n"
          }
      }
   }

.. _get Email properties:

Email properties
----------------

.. vale off

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``isPublished``
     - boolean
     - Email publication status
   * - ``dateAdded``
     - datetime
     - Email record creation date and time
   * - ``dateModified``
     - datetime
     - Email record last modification date and time
   * - ``createdBy``
     - integer
     - ID of the User who created the Email
   * - ``createdByUser``
     - string
     - Name of the User who created the Email
   * - ``modifiedBy``
     - integer
     - ID of the User who last modified the Email
   * - ``modifiedByUser``
     - string
     - Name of the User who last modified the Email
   * - ``id``
     - integer
     - ID of the Email
   * - ``name``
     - string
     - Email name
   * - ``subject``
     - string
     - Subject of the Email
   * - ``language``
     - string
     - The language code for the Email, such as ``en``, ``fr``, and so on
   * - ``category``
     - object
     - The Category for the Email
   * - ``fromAddress``
     - string
     - From Email address
   * - ``fromName``
     - string
     - From name
   * - ``replyToAddress``
     - string
     - Reply-to Email address
   * - ``bccAddress``
     - string
     - BCC Email address
   * - ``useOwnerAsMailer``
     - boolean
     - Contact owner mailer status - set to ``1`` or ``true`` to use the Contact owner as the mailer
   * - ``utmTags``
     - associative array
     - Associative array of Email UTM tags
   * - ``preheaderText``
     - string
     - Summary text that appears after the subject line
   * - ``customHtml``
     - string
     - Custom HTML content of the Email
   * - ``plainText``
     - string
     - Plain text version of the Email
   * - ``template``
     - string
     - Theme used to style the Email
   * - ``emailType``
     - string
     - Type of the Email - ``list`` or ``template``
   * - ``publishUp``
     - datetime
     - Activation date and time for the Email
   * - ``publishDown``
     - datetime
     - Deactivation date and time for the Email
   * - ``publicPreview``
     - boolean
     - Public preview status
   * - ``readCount``
     - integer
     - Number of times Users read the Email
   * - ``sentCount``
     - integer
     - Number of times the system sent the Email
   * - ``revision``
     - integer
     - Revision number of the Email
   * - ``assetAttachments``
     - array
     - Array of Assets attached to the Email
   * - ``variantStartDate``
     - datetime
     - Activation date and time for the Email A/B test
   * - ``variantSentCount``
     - integer
     - Number of times the system sent Email variants
   * - ``variantReadCount``
     - integer
     - Number of times Users read Email variants
   * - ``variantParent``
     - integer
     - ID of the parent Email for the variant
   * - ``variantChildren``
     - array
     - Array of child Email variant IDs
   * - ``translationParent``
     - integer
     - ID of the parent translation Email
   * - ``translationChildren``
     - array
     - Array of Email IDs that translate the parent Email
   * - ``unsubscribeForm``
     - object
     - The Unsubscribe Form for the Email
   * - ``dynamicContent``
     - array
     - Array of Dynamic Content variants
   * - ``lists``
     - array
     - Array of Segments that receive the Email
   * - ``headers``
     - array
     - Array of custom headers
   * - ``grapesjsbuilder``
     - associative array
     - Associative array of Email builder configuration

.. vale on

.. vale off

List Emails
***********

.. vale on

Retrieves a list of Emails.

.. code-block:: php

   <?php
   // ...

   $emails = $emailApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

HTTP request
============

.. vale on

``GET /emails``

Query parameters
----------------

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``search``
     - string
     - String or search command to filter entities
   * - ``start``
     - integer
     - Starting row for the returned entities - defaults to 0
   * - ``limit``
     - integer
     - Maximum number of entities to return - defaults to 30
   * - ``orderBy``
     - string
     - Column to sort by. Any column in the response is valid.
       
       **Note**: convert ``camelCase`` properties to ``snake_case``. For example, ``dateAdded`` becomes ``date_added``, ``webhookUrl`` becomes ``webhook_url``, and so on
   * - ``orderByDir``
     - string
     - Order direction - ``asc`` or ``desc``
   * - ``publishedOnly``
     - boolean
     - Returns only currently published entities
   * - ``minimal``
     - boolean
     - Returns only a simple mapped object of entities without additional lists in it

Response
========

* Returns ``200 OK`` when the request successfully retrieves the Emails list.

.. code-block:: json

   {
      "total": 2,
      "emails": {
          "1": {
              "isPublished": true,
              "dateAdded": "2026-02-19T04:17:46+00:00",
              "dateModified": "2026-02-19T15:14:49+00:00",
              "createdBy": 1,
              "createdByUser": "Admin Mautic",
              "modifiedBy": 1,
              "modifiedByUser": "Admin Mautic",
              "id": 1,
              "name": "Acme General Conference Success",
              "subject": "Acme General Conference Success",
              "language": "en",
              "category": null,
              "fromAddress": "john.doe@acme.com",
              "fromName": "John Doe",
              "replyToAddress": null,
              "bccAddress": null,
              "useOwnerAsMailer": false,
              "utmTags": {
                  "utmSource": null,
                  "utmMedium": null,
                  "utmCampaign": null,
                  "utmContent": null
              },
              "preheaderText": null,
              "customHtml": "",
              "plainText": null,
              "template": "mautic_code_mode",
              "emailType": "template",
              "publishUp": null,
              "publishDown": null,
              "publicPreview": false,
              "readCount": 0,
              "sentCount": 0,
              "revision": 4,
              "assetAttachments": [],
              "variantStartDate": null,
              "variantSentCount": 0,
              "variantReadCount": 0,
              "variantParent": null,
              "variantChildren": [],
              "translationParent": null,
              "translationChildren": [],
              "unsubscribeForm": null,
              "dynamicContent": [
                  {
                      "tokenName": "Dynamic Content 1",
                      "content": "Default Dynamic Content",
                      "filters": [
                          {
                              "content": "Variation 1",
                              "filters": [
                                  {
                                      "glue": "and",
                                      "field": "email",
                                      "object": "lead",
                                      "type": "email",
                                      "filter": null,
                                      "display": null,
                                      "operator": "="
                                  }
                              ]
                          }
                      ]
                  }
              ],
              "lists": [],
              "headers": [],
              "grapesjsbuilder": {
                  "customMjml": "<mjml>\r\n  <mj-head>\r\n\t<!-- CSS-STYLE -->\r\n\t<mj-style inline=\"inline\"> p, li {margin:0 !important; padding:0; line-height:1.4em;}\r\n\t</mj-style>\r\n  </mj-head>\r\n  <!-- BODY -->\r\n  <mj-body background-color=\"#f4f4f4\">\r\n\t<mj-section padding-top=\"40px\" background-color=\"#ffffff\">\r\n\t  <mj-column>\r\n\t\t<mj-text font-size=\"11px\" align=\"center\">\r\n\t\t  <p>\r\n\t\t\t<span data-fr-verified=\"true\"><span data-fr-verified=\"true\" class=\"atwho-inserted\">{webview_text}</span>⁠⁠⁠⁠⁠⁠⁠</span>\r\n\t\t  </p>\r\n\t\t</mj-text>\r\n\t\t<mj-spacer>\r\n\t\t</mj-spacer>\r\n\t\t<mj-image src=\"/app/assets/images/placeholder-logo.png?v5214f417\" width=\"70px\" padding-bottom=\"0px\" padding-top=\"0px\">\r\n\t\t</mj-image>\r\n\t  </mj-column>\r\n\t</mj-section>\r\n\t<mj-section background-color=\"#ffffff\">\r\n\t  <mj-column width=\"550px\">\r\n\t\t<mj-text font-size=\"16px\" align=\"center\" font-style=\"italic\" color=\"#525252\">\r\n\t\t  <p>Ok, let's make an announcement\r\n\t\t  </p>\r\n\t\t</mj-text>\r\n\t\t<mj-spacer height=\"40px\">\r\n\t\t</mj-spacer>\r\n\t\t<mj-text font-size=\"24px\" align=\"center\" font-weight=\"700\">\r\n\t\t  <p>Start customizing your email\r\n\t\t  </p>\r\n\t\t</mj-text>\r\n\t  </mj-column>\r\n\t</mj-section>\r\n\t<mj-section background-color=\"#ffffff\" padding-top=\"0px\">\r\n\t  <mj-column padding-top=\"0px\">\r\n\t\t<mj-image src=\"/app/assets/images/placeholder-image.png?v5214f417\" padding-right=\"0px\" padding-left=\"0px\" padding-bottom=\"0px\" padding-top=\"0px\">\r\n\t\t</mj-image>\r\n\t  </mj-column>\r\n\t</mj-section>\r\n\t<mj-section background-color=\"#ffffff\" padding-top=\"0px\">\r\n\t  <mj-column padding-top=\"0px\">\r\n\t\t<mj-image src=\"/app/assets/images/placeholder-image.png?v5214f417\" padding-top=\"0px\">\r\n\t\t</mj-image>\r\n\t  </mj-column>\r\n\t  <mj-column padding-top=\"0px\">\r\n\t\t<mj-image src=\"/app/assets/images/placeholder-image.png?v5214f417\" padding-top=\"0px\">\r\n\t\t</mj-image>\r\n\t  </mj-column>\r\n\t</mj-section>\r\n\t<mj-section background-color=\"#ffffff\">\r\n\t  <mj-column width=\"550px\">\r\n\t\t<mj-text font-size=\"16px\" align=\"center\">\r\n\t\t  <p>Make your announcements pop with an eye-catching visual, then provide the crucial details for engagement.\r\n\t\t  </p>\r\n\t\t  <p>⁠⁠⁠⁠⁠⁠⁠\r\n\t\t\t<br/>Customize this section by inserting your own images or choosing a striking solid color backdrop.\r\n\t\t  </p>\r\n\t\t</mj-text>\r\n\t\t<mj-spacer height=\"30px\">\r\n\t\t</mj-spacer>\r\n\t\t<mj-divider border-width=\"2px\" border-color=\"#d0d0d0\">\r\n\t\t</mj-divider>\r\n\t\t<mj-spacer height=\"30px\">\r\n\t\t</mj-spacer>\r\n\t\t<mj-text font-size=\"22px\" font-weight=\"700\">\r\n\t\t  <p>Lead with an eye-catching title\r\n\t\t  </p>\r\n\t\t</mj-text>\r\n\t\t<mj-text font-size=\"16px\">\r\n\t\t  <p>Present your news in a brief paragraph. For crucial points, use a bulleted list:\r\n\t\t  </p>\r\n\t\t  <ul>\r\n\t\t\t<li>\r\n\t\t\t  <span class=\"ck-list-bogus-paragraph\"><span class=\"ck-list-bogus-paragraph\">What's on offer</span></span>\r\n\t\t\t</li>\r\n\t\t\t<li>\r\n\t\t\t  <span class=\"ck-list-bogus-paragraph\"><span class=\"ck-list-bogus-paragraph\">Where to find us</span></span>\r\n\t\t\t</li>\r\n\t\t\t<li>\r\n\t\t\t  <span class=\"ck-list-bogus-paragraph\"><span class=\"ck-list-bogus-paragraph\">Timing specifics</span></span>\r\n\t\t\t</li>\r\n\t\t  </ul>\r\n\t\t  <p>Be concise to motivate readers to explore your website for the full story.\r\n\t\t  </p>\r\n\t\t</mj-text>\r\n\t\t<mj-button href=\"https://\" background-color=\"#000000\" inner-padding=\"16px 32px\" border-radius=\"0px 0px 0px 0px\" font-size=\"16px\" align=\"left\">Button\r\n\t\t</mj-button>\r\n\t\t<mj-spacer align=\"center\">\r\n\t\t</mj-spacer>\r\n\t  </mj-column>\r\n\t</mj-section>\r\n\t<mj-section padding-top=\"0\" padding-bottom=\"20px\" background-color=\"#000000\">\r\n\t  <mj-column>\r\n\t\t<mj-spacer height=\"40px\">\r\n\t\t</mj-spacer>\r\n\t\t<mj-image src=\"/app/assets/images/placeholder-logo-inverse.png?v5214f417\" width=\"70px\" padding-bottom=\"0px\">\r\n\t\t</mj-image>\r\n\t\t<mj-spacer>\r\n\t\t</mj-spacer>\r\n\t\t<mj-text font-family=\"Ubuntu, Helvetica, Arial, sans-serif\" line-height=\"1.5\" align=\"center\" padding-top=\"0px\" padding-bottom=\"0px\" font-size=\"12px\" color=\"white\">\r\n\t\t  <p>Amazing Company\r\n\t\t\t<br/>11111 Beautiful City, 1212 Nice Street\r\n\t\t\t<br/>Brazil\r\n\t\t\t<br/>\r\n\t\t  </p>\r\n\t\t</mj-text>\r\n\t\t<mj-spacer>\r\n\t\t</mj-spacer>\r\n\t\t<mj-text font-size=\"11px\" align=\"center\" color=\"#a1a1a1\">\r\n\t\t  <p>Fancy seeing you down here. You’re getting this email because you gave us your email address.\r\n\t\t  </p>\r\n\t\t  <p>Want to change how you receive these emails?\r\n\t\t  </p>\r\n\t\t</mj-text>\r\n\t\t<mj-text font-size=\"11px\" align=\"center\" color=\"#a1a1a1\">\r\n\t\t  <p>\r\n\t\t\t<span data-fr-verified=\"true\"><span data-fr-verified=\"true\" class=\"atwho-inserted\">{unsubscribe_text}</span>⁠⁠⁠⁠⁠⁠⁠</span>\r\n\t\t  </p>\r\n\t\t</mj-text>\r\n\t\t<mj-spacer>\r\n\t\t</mj-spacer>\r\n\t  </mj-column>\r\n\t</mj-section>\r\n  </mj-body>\r\n</mjml>\r\n"
              }
          },
          // ...
      }
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
     - integer
     - Total count of Emails
   * - ``emails``
     - array
     - A mapped collection of Emails indexed by their ID

.. vale off

For the rest of the properties, refer to :ref:`Email properties <get Email properties>`.

.. vale off

Create Email
************

.. vale on

Creates a new Email.

.. code-block:: php

   <?php

   $data = array(
       'name'             => 'Email created via API', // Required
       'subject'          => 'Hello World!',          // Required
       'language'         => 'en',                    // Required
       'lists'            => array(1, 2),             // Required
       'emailType'        => 'list',
       'isPublished'      => true,
       'customHtml'       => '<h1>Hello from API!</h1>',
       'preheaderText'    => 'Check out our latest update',
       'assetAttachments' => array(5),
   );

   $email = $emailApi->create($data);

.. vale off

HTTP request
============

.. vale on

``POST /emails/new``

.. _create Email POST parameters:

POST parameters
---------------

.. vale off

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``name``
     - string
     - **Required.**
       
       Name of the Email
   * - ``subject``
     - string
     - **Required.**
       
       Subject of the Email
   * - ``language``
     - string
     - **Required.**
       
       The language code for the Email, such as ``en``, ``fr``, and so on
   * - ``lists``
     - array
     - **Required.**
       
       Array of Segments that receive the Email
   * - ``isPublished``
     - boolean
     - Email publication status
   * - ``category``
     - integer
     - ID of the Category for the Email
   * - ``fromAddress``
     - string
     - From Email address
   * - ``fromName``
     - string
     - From name
   * - ``replyToAddress``
     - string
     - Reply-to Email address
   * - ``bccAddress``
     - string
     - BCC Email address
   * - ``useOwnerAsMailer``
     - boolean
     - Contact owner mailer status - set to ``1`` or ``true`` to use the Contact owner as the mailer
   * - ``utmTags``
     - associative array
     - Associative array of Email UTM tags
   * - ``preheaderText``
     - string
     - Summary text that appears after the subject line
   * - ``customHtml``
     - string
     - Custom HTML content of the Email
   * - ``plainText``
     - string
     - Plain text version of the Email
   * - ``template``
     - string
     - Theme used to style the Email
   * - ``emailType``
     - string
     - Type of the Email - ``list`` or ``template``
   * - ``publishUp``
     - datetime
     - Activation date and time for the Email
   * - ``publishDown``
     - datetime
     - Deactivation date and time for the Email
   * - ``publicPreview``
     - boolean
     - Public preview status
   * - ``assetAttachments``
     - array
     - Array of Asset IDs attached to the Email
   * - ``unsubscribeForm``
     - integer
     - ID of the Unsubscribe Form for the Email
   * - ``dynamicContent``
     - array
     - Array of Dynamic Content variants
   * - ``headers``
     - array
     - Array of custom headers

.. vale on

Response
========

* Returns ``201 Created`` when the request successfully creates an Email.

The response is a JSON object similar to :ref:`Get Email <get Email response>`.

Properties
----------

Refer to :ref:`Email properties <get Email properties>`.

.. vale off

Edit Email
**********

.. vale on

Edits an Email. 

This operation supports ``PUT`` or ``PATCH`` depending on the desired behavior:

* ``PUT``: **full replacement**. The request creates a new Email if the ID is missing. If the ID exists, the request clears all existing data and replaces it with the provided values.
* ``PATCH``: **partial update**. The request only updates field values based on the request data. The request fails when the Email ID doesn't exist.

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'name'    => 'New email name',
       'subject' => 'New subject line',
   );

   // Create a new Email if ID 1 isn't found
   $createIfNotFound = true;

   $email = $emailApi->edit($id, $data, $createIfNotFound);

.. vale off

HTTP request
============

.. vale on

* ``PUT /emails/ID/edit``: updates an existing Email or creates a new one when the ID doesn't exist.
* ``PATCH /emails/ID/edit``: updates an existing Email. The request fails when the ID doesn't exist.

POST parameters
---------------

Accepts the same parameters as those described in :ref:`Create Email <create Email POST parameters>`. All parameters are optional.

Response
========

* ``PUT``: returns ``200 OK`` when the request successfully updates the Email or ``201 Created`` when the request creates an Email.
* ``PATCH``: returns ``200 OK`` when the request successfully updates the Email or ``404 Not Found`` error when the Email ID doesn't exist.

The response is a JSON object similar to :ref:`Get Email <get Email response>`.

Properties
----------

Refer to :ref:`Email properties <get Email properties>`.

.. vale off

Delete Email
************

.. vale on

Deletes an Email.

.. code-block:: php

   <?php

   $email = $emailApi->delete($id);

.. vale off

HTTP request
============

.. vale on

``DELETE /emails/ID/delete``

Response
========

* Returns ``200 OK`` when the request successfully deletes the Email.

The response is a JSON object containing the data of the deleted Email, similar to :ref:`Get Email <get Email response>`.

Properties
----------

Refer to :ref:`Email properties <get Email properties>`.

.. vale off

Send Email to Contact
*********************

.. vale on

Sends an Email to a specific Contact.

.. code-block:: php

   <?php

   $response = $emailApi->sendToContact($emailId, $contactId, $options);

Tokens
======

You can send custom tokens to the Email via the ``tokens`` parameter. Use the format ``{token_name}`` for tokens within the Email content.

.. code-block:: php

   <?php

   $tokens = array(
       '{first_name}' => 'John',
       '{last_name}'  => 'Doe',
       '{custom_token}' => 'Custom Value'
   );

   $response = $emailApi->sendToContact($emailId, $contactId, array('tokens' => $tokens));

.. vale off

HTTP request
============

.. vale on

``POST /emails/ID/contact/CONTACT_ID/send``

Parameters
----------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``tokens``
     - associative array
     - Associative array of tokens to replace in the Email content

Response
========

* Returns ``200 OK`` when the request successfully delivers the Email to the Contact.

.. code-block:: json

   {
       "success": true
   }

.. vale off

Send Email to Segment
*********************

.. vale on

Sends an Email to the Contacts in the Email's assigned Segments or to specific Segment IDs.

.. code-block:: php

   <?php

   // Send to all Contacts in the Email's assigned Segments
   $response = $emailApi->send($id);

   // Sends to specific Segment(s)
   $response = $emailApi->sendToLists($id, $listIds);

.. vale off

HTTP request
============

.. vale on

``POST /emails/ID/send``

Parameters
----------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``listIds``
     - array
     - Array of Segment IDs to target. This parameter overrides the Email's assigned Segments

Response
========

* Returns ``200 OK`` when the request successfully delivers the Email to the Segments.

.. code-block:: json

   {
       "success": 1,
       "sentCount": 1,
       "failedRecipients": 0
   }

Properties
----------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``success``
     - boolean
     - Delivery success status - ``1`` or ``true`` indicates a successful send
   * - ``sentCount``
     - integer
     - Total number of successfully sent Emails
   * - ``failedRecipients``
     - integer
     - Total number of Emails that failed to deliver

.. vale off

Create Email reply
******************

.. vale on

Creates a reply to an Email using the tracking hash from the Email statistics.

.. code-block:: php

   <?php

   $response = $emailApi->reply($trackingHash);

.. vale off

HTTP request
============

.. vale on

``POST /emails/reply/TRACKING_HASH``

Parameters
----------

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``trackingHash``
     - string
     - Unique hash used to track Email statistics

Response
========

* Returns ``201 Created`` when the request successfully creates the reply.

.. code-block:: json

   {
       "success": true
   }
