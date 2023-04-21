Contacts
########

Use this endpoint to manipulate and obtain details on Mautic's Contacts.

**Using Mautic's API Library**

You can interact with this API through the :xref:`Mautic API Library` as follows, or use the various http endpoints as described in this document.

.. code-block:: php

   <?php
   use Mautic\MauticApi;
   use Mautic\Auth\ApiAuth;

   // ...
   $initAuth   = new ApiAuth();
   $auth       = $initAuth->newAuth($settings);
   $apiUrl     = "https://example.com";
   $api        = new MauticApi();
   $contactApi = $api->newApi("contacts", $auth, $apiUrl);

.. vale off

Get Contact
***********

.. vale on

.. code-block:: php

   <?php

   //...
   $contact = $contactApi->get($id);

Get an individual Contact by ID.

.. vale off

**HTTP Request**

.. vale on

``GET /contacts/ID``

**Response**

``Expected Response Code: 200``

.. code-block:: json

       "contact": {
           "id": 47,
           "dateAdded": "2015-07-21T12:27:12-05:00",
           "createdBy": 1,
           "createdByUser": "Joe Smith",
           "dateModified": "2015-07-21T14:12:03-05:00",
           "modifiedBy": 1,
           "modifiedByUser": "Joe Smith",
           "owner": {
               "id": 1,
               "Username": "joesmith",
               "firstName": "Joe",
               "lastName": "Smith"
           },
           "points": 10,
           "lastActive": "2015-07-21T14:19:37-05:00",
           "dateIdentified": "2015-07-21T12:27:12-05:00",
           "color": "ab5959",
           "ipAddresses": {
               "111.111.111.111": {
                   "ipAddress": "111.111.111.111",
                   "ipDetails": {
                       "city": "",
                       "region": "",
                       "country": "",
                       "latitude": "",
                       "longitude": "",
                       "isp": "",
                       "organization": "",
                       "timezone": ""
                   }
               }
           },
           "fields": {
               "core": {
                   "title": {
                       "id": "1",
                       "label": "Title",
                       "alias": "title",
                       "type": "lookup",
                       "group": "core",
                       "value": "Mr"
                   },
                   "firstname": {
                       "id": "2",
                       "label": "First Name",
                       "alias": "firstname",
                       "type": "text",
                       "group": "core",
                       "value": "Jim"
                   },

                   "...": {
                       "..." : "..."
                   }

               },
               "social": {
                   "twitter": {
                       "id": "17",
                       "label": "Twitter",
                       "alias": "twitter",
                       "type": "text",
                       "group": "social",
                       "value": "jimcontact"
                   },

                   "...": {
                       "..." : "..."
                   }

               },
               "personal": [],
               "professional": [],
               "all": {
                   "title": "Mr",
                   "firstname": "Jim",
                   "twitter": "jimcontact",

                   "...": "..."
               }
           }
       }

**Contact Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Contact
   * - ``isPublished``
     - boolean
     - ``true`` if the Contact has the status of published
   * - ``dateAdded``
     - ``datetime``
     - Date/time Contact got created
   * - ``createdBy``
     - int
     - ID of the User that created the Contact
   * - ``createdByUser``
     - string
     - Name of the User that created the Contact
   * - ``dateModified``
     - datetime/null
     - Date/time Contact was last modified
   * - ``modifiedBy``
     - int
     - ID of the User that last modified the Contact
   * - ``modifiedByUser``
     - string
     - Name of the User that last modified the Contact
   * - ``owner``
     - object
     - User object that owns the Contact.
   * - ``points``
     - int
     - Contact's current number of Points
   * - ``lastActive``
     - datetime/null
     - Date/time for when the Contact was last recorded as active
   * - ``dateIdentified``
     - datetime/null
     - Date/time when the Contact identified themselves
   * - ``color``
     - string
     - Hex value given to Contact from Point Trigger definitions based on the number of Points the Contact got awarded
   * - ``ipAddresses``
     - array
     - Array of IP addresses currently associated with this Contact
   * - ``fields``
     - array
     - Array of all Contact fields with data grouped by field group. See JSON code example for format. This array includes an "all" key that includes an single level array of ``fieldAlias => ContactValue`` pairs.
   * - ``tags``
     - array
     - Array of tags associated with this Contact. See JSON code example for format.
   * - ``utmtags``
     - array
     - Array of UTM Tags associated with this Contact. See JSON code example for format.
   * - ``doNotContact``
     - array
     - Array of ``Do Not Contact`` objects. See JSON code example for format.

.. vale off

List Contacts
*************

.. vale on

.. code-block:: php

   <?php

   //...
   $contacts = $contactApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

Get a list of Contacts.

.. vale off

**HTTP Request**

.. vale on

``GET /contacts``

**Query Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - ``search``
     - String or search command to filter entities by.
   * - ``start``
     - Starting row for the entities returned. Defaults to 0.
   * - ``limit``
     - Limit number of entities to return. Defaults to the system configuration for pagination, which is 30 by default.
   * - ``orderBy``
     - Column to sort by. Can use any column listed in the response. However, you need to change all properties in the response written in ``camelCase`` a bit. Before every capital, add an underscore ``_`` and then change the capital letters to non-capital letters. So ``dateIdentified`` becomes ``date_identified``, ``modifiedByUser`` becomes ``modified_by_user``, etc.
   * - ``orderByDir``
     - Sort direction: ``asc`` or ``desc``.
   * - ``publishedOnly``
     - Only return currently published entities.
   * - ``minimal``
     - Return only array of entities without additional lists in it.
   * - ``where``
     - An array of advanced where conditions
   * - ``order``
     - An array of advanced order statements


Advanced filtering
~~~~~~~~~~~~~~~~~~

In some cases you may want to filter by specific values. Use URL parameters like this:

In PHP:

.. code-block:: php

   $where = [
     [
       'col' => 'phone',
       'expr' => 'in',
       'val' => '444444444,888888888',
     ]
   ];

This design allows to add multiple conditions in the same request.

If you aren't using PHP, here is URL-encoded version of the example:
``GET https://[example.com]/api/contacts?where%5B0%5D%5Bcol%5D=phone&where%5B0%5D%5Bexpr%5D=in&where%5B0%5D%5Bval%5D=444444444,888888888``

You can find a list of available expressions on :xref:`Doctrine ORM's website<Doctrine ORM Query Builder>`.

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "total": "1",
       "contacts": {
           "47": {
               "id": 47,
               "isPublished": true,
               "dateAdded": "2015-07-21T12:27:12-05:00",
               "createdBy": 1,
               "createdByUser": "Joe Smith",
               "dateModified": "2015-07-21T14:12:03-05:00",
               "modifiedBy": 1,
               "modifiedByUser": "Joe Smith",
               "owner": {
                   "id": 1,
                   "Username": "joesmith",
                   "firstName": "Joe",
                   "lastName": "Smith"
               },
               "points": 10,
               "lastActive": "2015-07-21T14:19:37-05:00",
               "dateIdentified": "2015-07-21T12:27:12-05:00",
               "color": "ab5959",
               "ipAddresses": {
                   "111.111.111.111": {
                       "ipAddress": "111.111.111.111",
                       "ipDetails": {
                           "city": "",
                           "region": "",
                           "country": "",
                           "latitude": "",
                           "longitude": "",
                           "isp": "",
                           "organization": "",
                           "timezone": ""
                       }
                   }
               },
               "fields": {
                   "core": {
                       "title": {
                           "id": "1",
                           "label": "Title",
                           "alias": "title",
                           "type": "lookup",
                           "group": "core",
                           "value": "Mr"
                       },
                       "firstname": {
                           "id": "2",
                           "label": "First Name",
                           "alias": "firstname",
                           "type": "text",
                           "group": "core",
                           "value": "Jim"
                       },

                       "...": {
                           "..." : "..."
                       }
                   },
                   "social": {
                       "twitter": {
                           "id": "17",
                           "label": "Twitter",
                           "alias": "twitter",
                           "type": "text",
                           "group": "social",
                           "value": "jimcontact"
                       },

                       "...": {
                           "..." : "..."
                       }
                   },
                   "personal": [],
                   "professional": [],
                   "all": {
                       "title": "Mr",
                       "firstname": "Jim",
                       "twitter": "jimcontact",

                       "...": "..."
                   }
               },
               "tags": [{
                 "tag": "aTag"
               },
               {
                 "tag": "bTag"
               }],
               "utmtags" : [{
                 "id": 1,
                 "query": {
                   "page": "asd",
                   "cid": "fb1"
                 },
                 "referer": "https://example.com/",
                 "remoteHost": "example.com",
                 "UserAgent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0",
                 "utmCampaign": "abcampaign",
                 "utmContent": "page",
                 "utmMedium": "social",
                 "utmSource": "fb",
                 "utmTerm": "test1"
               }],
               "doNotContact": [{
                   "id": 2,
                   "reason": 2,
                   "comments": "",
                   "channel": "email",
                   "channelId": null
               }]
           }
       }
   }

**Properties**

Same as :ref:`Get Contact`.

.. vale off

Create Contact
**************

.. vale on

.. code-block:: php

   <?php

   $data = array(
       'firstname' => 'Jim',
       'lastname'  => 'Contact',
       'email'     => 'jim@example.com',
       'ipAddress' => $_SERVER['REMOTE_ADDR'],
       'overwriteWithBlank' => true,
   );

   $contact = $contactApi->create($data);

Create a new Contact.

.. vale off

**HTTP Request**

.. vale on

``POST /contacts/new``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - ``*``
     - You can post any Contact field alias as a parameter. For example, ``firstname``, ``lastname``, ``email``, etc.
   * - ``ipAddress``
     - IP address to associate with the Contact
   * - ``lastActive``
     - Date/time in ``UTC``; preferably in the format of Y-m-d H:m:i but if that format fails, the string get sent through PHP's ``strtotime`` then formatted
   * - ``owner``
     - ID of a Mautic User to assign this Contact to
   * - ``overwriteWithBlank``
     - If true, then empty values get set to fields. Otherwise empty values get skipped


**Response**

``Expected Response Code: 201``

**Properties**

Same as :ref:`Get Contact`.

.. vale off

Create Batch Contact
********************

.. vale on

.. code-block:: php

   <?php

   $data = array(
       array(
       'firstname' => 'Jim',
       'lastname'  => 'Contact',
       'email'     => 'jim@example.com',
       'ipAddress' => $_SERVER['REMOTE_ADDR']
       ),
       array(
       'firstname' => 'Rudolf',
       'lastname'  => 'Große',
       'email'     => 'rudolf@example.com',
       'ipAddress' => $_SERVER['REMOTE_ADDR']
       )
   );
   $contact = $contactApi->createBatch($data);

Create a batch of new Contacts.

.. vale off

**HTTP Request**

.. vale on

``POST /contacts/batch/new``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - ``*``
     - You can post any Contact field alias as a parameter. For example, ``firstname``, ``lastname``, ``email``, etc.
   * - ``ipAddress``
     - IP address to associate with the Contact
   * - ``lastActive``
     - Date/time in ``UTC``; preferably in the format of Y-m-d H:m:i but if that format fails, the string get sent through PHP's ``strtotime`` then formatted
   * - ``owner``
     - ID of a Mautic User to assign this Contact to


**Response**

``Expected Response Code: 201``

**Properties**

Array of Contacts. Record is the same as :ref:`Get Contact`.

.. vale off

Edit Contact
************

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'email'     => 'isabel-new-address@example.com',
       'ipAddress' => $_SERVER['REMOTE_ADDR'],    
   );

   // Create new a Contact of ID 1 isn't found?
   $createIfNotFound = true;

   $contact = $contactApi->edit($id, $data, $createIfNotFound);

Edit a new Contact. Note that this supports PUT or PATCH depending on the desired behavior.

**PUT** creates a Contact if the given ID doesn't exist and clears all the Contact information, adds the information from the request.
**PATCH** fails if the Contact with the given ID doesn't exist and updates the Contact field values with the values from the request.

.. vale off

**HTTP Request**

.. vale on

To edit a Contact and return a 404 if the Contact isn't found:

``PATCH /contacts/ID/edit``

To edit a Contact and create a new one if the Contact isn't found:

``PUT /contacts/ID/edit``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - ``*``
     - You can post any Contact field alias as a parameter. For example, ``firstname``, ``lastname``, ``email``, etc.
   * - ``ipAddress``
     - IP address to associate with the Contact
   * - ``lastActive``
     - Date/time in ``UTC``; preferably in the format of Y-m-d H:m:i but if that format fails, the string get sent through PHP's ``strtotime`` then formatted
   * - ``owner``
     - ID of a Mautic User to assign this Contact to
   * - ``overwriteWithBlank``
     - If ``true``, then empty values get set to fields. Otherwise empty values get skipped

**Response**

If ``PUT``, the expected response code is ``200`` if the Contact got edited or ``201`` if created.
If ``PATCH``, the expected response code is ``200``.

**Properties**

Same as :ref:`Get Contact`.

.. note:: In order to remove a tag from the Contact, add minus ``-`` before it. For example: ``tags: ['one', '-two']`` - sending this in request body will add tag ``one`` and remove tag ``two`` from Contact.

.. vale off

Edit Batch Contact
******************

.. vale on

.. code-block:: php

   <?php

   $data = [
       [
           'id'        => 1,
           'firstname' => 'Jim',
           'lastname'  => 'Contact',
           'title'     => '', // This will be ignored because overwriteWithBlank is false by default
           'email'     => 'jim@example.com',
           'ipAddress' => $_SERVER['REMOTE_ADDR']
       ],
       [
           'overwriteWithBlank' => true, // This flag will allow to overwrite any field with a blank value
           'id'                 => 2,
           'firstname'          => 'Ashish',
           'lastname'           => 'Wallach',
           'title'              => '', // This will set the title to blank because overwriteWithBlank is true
           'email'              => 'ashish@example.com',
           'ipAddress'          => $_SERVER['REMOTE_ADDR']
       ]
   ];

   $contact = $contactApi->editBatch($data);

Edit several Contacts in one request.  Note that this supports PUT or PATCH depending on the desired behavior.

**PUT** creates a Contact if the given ID doesn't exist and clears all the Contact information, adds the information from the request.
**PATCH** fails if the Contact with the given ID doesn't exist and updates the Contact field values with the values from the request.

.. vale off

**HTTP Request**

.. vale on

To edit a Contact and return a 404 if the Contact isn't found:

``PATCH /contacts/batch/edit``

To edit a Contact and create a new one if the Contact isn't found:

``PUT /contacts/batch/edit``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - ``*``
     - You can post any Contact field alias as a parameter. For example, ``firstname``, ``lastname``, ``email``, etc.
   * - ``ipAddress``
     - IP address to associate with the Contact
   * - ``lastActive``
     - Date/time in ``UTC``; preferably in the format of Y-m-d H:m:i but if that format fails, the string get sent through PHP's ``strtotime`` then formatted
   * - ``owner``
     - ID of a Mautic User to assign this Contact to
   * - ``overwriteWithBlank``
     - If ``true``, then empty values get set to fields. Otherwise empty values get skipped

**Response**

If ``PUT``, the expected response code is ``200`` if the Contact got edited or ``201`` if created.
If ``PATCH``, the expected response code is ``200``.

**Properties**

Contacts array. Record same as :ref:`Get Contact`.

.. note:: In order to remove a tag from the Contact, add minus ``-`` before it. For example: ``tags: ['one', '-two']`` - sending this in request body will add tag ``one`` and remove tag ``two`` from Contact.

.. vale off

Delete Contact
**************

.. vale on

.. code-block:: php

   <?php

   $contact = $contactApi->delete($id);

Delete a Contact.

.. vale off

**HTTP Request**

.. vale on

``DELETE /contacts/ID/delete``

**Response**

``Expected Response Code: 200``

**Properties**

Same as :ref:`Get Contact`.

.. vale off

Delete Batch Contact
********************

.. vale on

.. code-block:: php

   <?php
   $data = array(1, 2);
   $contact = $contactApi->deleteBatch($data);

Delete Contacts.

.. vale off

**HTTP Request**

.. vale on

``DELETE /contacts/batch/delete``

If you aren't using PHP, here is a URL example:

``DELETE https://[example.com]/api/contacts/batch/delete?ids=1,2``

**Response**

``Expected Response Code: 200``

**Properties**

Contacts array. Record same as :ref:`Get Contact`.

.. vale off

Add Do Not Contact
******************

.. vale on

.. code-block:: php

   <?php

   $contactApi->addDnc($contactId, $channel, $reason, $channelId, $comments);

Add a Contact to DNC list

.. vale off

**HTTP Request**

.. vale on

To add a ``Do Not Contact`` entry to a Contact:

``POST /contacts/ID/dnc/CHANNEL/add``

.. vale off

**Data Parameters (optional)**

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - ``channel``
     - Channel of DNC. For example ``email``, ``sms``, etc. - default is email.
   * - ``reason``
     - Int value of the reason. Use Contacts constants: ``Contacts::UNSUBSCRIBED (1)``, ``Contacts::BOUNCED (2)``, ``Contacts::MANUAL (3)``. Default is Manual
   * - ``channelId``
     - ID of the entity which was the reason for unsubscription
   * - ``comments``
     - A text describing details of DNC entry

.. vale on

**Response**

.. code-block:: json

   {
     "channelId": "26",
     "reason": "Integration issued DNC",
     "comments": "Unsubscribed via API"
   }

.. vale off

Remove from Do Not Contact
**************************

.. vale on

.. code-block:: php

   <?php
   $contactApi->removeDnc($contactId, $channel);

Remove a Contact from DNC list

.. vale off

**HTTP Request**

.. vale on

To remove ``Do Not Contact`` entry from a Contact:

``POST /contacts/ID/dnc/CHANNEL/remove``

.. vale off

**Data Parameters (optional)**

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - ``channel``
     - Channel of DNC. For example ``email``, ``sms``, etc. - default is email.

.. vale on

**Response**

Same as :ref:`Get Contact`.

.. vale off

Add UTM Tags
************

.. vale on

.. code-block:: php

   <?php

   $data = array(
       'utm_campaign' => 'apicampaign',
       'utm_source'   => 'fb',
       'utm_medium'   => 'social',
       'utm_content'  => 'fbad',
       'utm_term'     => 'mautic api',
       'Useragent'    => 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
       'url'          => '/product/fbad01/',
       'referer'      => 'https://google.com/q=mautic+api',
       'query'        => ['cid'=>'abc','cond'=>'new'], // or as string with "cid=abc&cond=new"
       'remotehost'   => 'example.com',
       'lastActive'   => '2017-01-17T00:30:08+00:00'
    );
   $contactApi->addUtm($contactId, $data);

Add UTM tags to a Contact

.. vale off

**HTTP Request**

.. vale on

To add UTM tag entry to a Contact:

``POST /contacts/ID/utm/add``

.. vale off

**UTM Parameters (required)**

.. vale on

Mautic requires the parameter array. Each ``UTM`` tag entry is optional.

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - ``utm_campaign``
     - The UTM Campaign parameter
   * - ``utm_source``
     - The UTM Source parameter
   * - ``utm_medium``
     - The UTM Medium parameter
   * - ``utm_content``
     - The UTM Content parameter
   * - ``utm_term``
     - The UTM Term parameter
   * - ``Useragent``
     - The browser's UserAgent. If provided a new Device entry gets created if necessary.
   * - ``url``
     - The ``page`` URL
   * - ``referer``
     - The URL of the referrer,
   * - ``query``
     - Any extra query parameters you wish to include. Array or http query string
   * - ``remotehost``
     - The Host name
   * - ``lastActive``
     - The date that the action occured. Contact's ``lastActive`` date gets updated if included. Date format required ``2017-01-17T00:30:08+00:00``.


**Response**

Same as :ref:`Get Contact` with the added UTM Tags.

.. vale off

Remove UTM Tags from a Contact
******************************

.. vale on

.. code-block:: php

   <?php
   $contactApi->removeUtm($contactId, $utmId);

Remove a set of UTM Tags from a Contact

.. vale off

**HTTP Request**

.. vale on

To remove UTM Tags from a Contact:

``POST /contacts/ID/utm/UTMID/remove``

**Data Parameters**

None required.

**Response**

Same as :ref:`Get Contact` without the removed UTM Tags.

.. vale off

Add Points
**********

.. vale on

.. code-block:: php

   <?php

   $data = [
        'eventName' => 'Score via api',
        'actionName' => 'Adding',
   ];
   $contactApi->addPoints($contactId, $pointDelta, $data);

Add Contact Points

.. vale off

**HTTP Request**

.. vale on

To add Points to a Contact and return a 404 if the Contact isn't found:

``POST /contacts/ID/points/plus/POINTS``

.. vale off

**Data Parameters (optional)**

.. vale on

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - ``eventName``
     - Name of the event
   * - ``actionName``
     - Name of the action


**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "success": true
   }

.. vale off

Subtract Points
***************

.. vale on

.. code-block:: php

   <?php

   $data = array(
        'eventname' => 'Score via api',
        'actionname' => 'Subtracting',
    );
   $contactApi->subtractPoints($contactId, $pointDelta, $data);

Subtract Contact Points

.. vale off

**HTTP Request**

.. vale on

To subtract Points from a Contact and return a 404 if the Contact isn't found:

``POST /contacts/ID/points/minus/POINTS``

.. vale off

**Data Parameters (optional)**

.. vale on

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - ``eventname``
     - Name of the event
   * - ``actionname``
     - Name of the action


**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "success": true
   }

.. vale off

List Available Owners
*********************

.. vale on

.. code-block:: php

   <?php

   $owners = $contactApi->getOwners();

Get a list of owners that you can use to assign Contacts to when creating/editing.

.. vale off

**HTTP Request**

.. vale on

``GET /contacts/list/owners``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   [
     {
       "id": 1,
       "firstName": "Joe",
       "lastName": "Smith"
     },
     {
       "id": 2,
       "firstName": "Jane",
       "lastName": "Smith"
     }
   ]

**Owner Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Mautic User
   * - ``firstName``
     - string
     - First name of the Mautic User
   * - ``lastName``
     - string
     - Last name of the Mautic User

.. vale off

List Available Fields
*********************

.. vale on

.. code-block:: php

   <?php

   $fields = $contactApi->getFieldList();

Get a list of available Contact fields including custom ones.

.. vale off

**HTTP Request**

.. vale on

``GET /contacts/list/fields``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {
       "1": {
           "id": 1,
           "label": "Title",
           "alias": "title",
           "type": "lookup",
           "group": "core",
           "order": 1
       },
       "2": {
           "id": 2,
           "label": "First Name",
           "alias": "firstname",
           "type": "text",
           "group": "core",
           "order": 2
       },
       "3": {
           "id": 3,
           "label": "Last Name",
           "alias": "lastname",
           "type": "text",
           "group": "core",
           "order": 3
       },

       "...": {
           "..." : "..."
       }
   }

**Field Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the field
   * - ``label``
     - string
     - Field label
   * - ``alias``
     - string
     - Field alias used as the column name in the database
   * - ``type``
     - string
     - Type of field, for example ``text``, ``lookup``, etc
   * - ``group``
     - string
     - Group the field belongs to
   * - ``order``
     - int
     - Field order

.. vale off

List Contact Notes
******************

.. vale on

.. code-block:: php

   <?php

   $notes = $contactApi->getContactNotes($id, $searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

Get a list of notes for a specific Contact.

.. vale off

**HTTP Request**

.. vale on

``GET /contacts/ID/notes``

**Query Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - ``search``
     - String or search command to filter entities by.
   * - ``start``
     - Starting row for the entities returned. Defaults to 0.
   * - ``limit``
     - Limit number of entities to return. Defaults to the system configuration for pagination, which is 30 by default.
   * - ``orderBy``
     - Column to sort by. Can use any column listed in the response.
   * - ``orderByDir``
     - Sort direction: ``asc`` or ``desc``.


**Response**

``Expected response code: 200``

.. code-block:: json

   {
       "total": 1,
       "notes": [
           {
                 "id": 1,
                 "text": "<p>Jim is super cool!</p>",
                 "type": "general",
                 "dateTime": "2015-07-23T13:14:00-05:00"
           }
       ]
   }

**Note Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the note
   * - ``text``
     - string
     - Body of the note
   * - ``type``
     - string
     - Type of note. Options are ``general``, ``email``, ``call``, ``meeting``
   * - ``dateTime``
     - ``datetime``
     - Date/time string of when the note got created.

.. vale off

Get Segment Memberships
***********************

.. vale on

.. code-block:: php

   <?php

   $segments = $contactApi->getContactSegments($id);

Get a list of Contact Segments the Contact is a member of.

.. vale off

**HTTP Request**

.. vale on

``GET /contacts/ID/segments``

**Response**

``Expected response code: 200``

.. code-block:: json

   {
       "total": 1,
       "segments": {
           "3": {
               "id": 3,
               "name": "New Contacts",
               "alias": "newcontacts"
           }
       }
   }

**List Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the list
   * - ``name``
     - string
     - Name of the list
   * - ``alias``
     - string
     - Alias of the list used with search commands.
   * - ``dateAdded``
     - ``datetime``
     - Date/time string for when the Contact got added to the list
   * - ``manuallyAdded``
     - boolean
     - ``true`` if the Contact was manually added to the list versus added by a filter
   * - ``manuallyRemoved``
     - boolean
     - ``true`` if the Contact was manually removed from the list even though the list's filter is a match


.. vale off

Change List Memberships
***********************

.. vale on

See `Segments <#segments>`_.

.. vale off

Get Campaign Memberships
************************

.. vale on

.. code-block:: php

   <?php

   $campaigns = $contactApi->getContactCampaigns($id);

Get a list of Campaigns the Contact is a member of.

.. vale off

**HTTP Request**

.. vale on

``GET /contacts/ID/campaigns``

**Response**

``Expected response code: 200``

.. code-block:: json

   {
       "total": 1,
       "campaigns": {
           "1": {
               "id": 1,
               "name": "Welcome Campaign",
               "dateAdded": "2015-07-21T14:11:47-05:00",
               "manuallyRemoved": false,
               "manuallyAdded": false,
               "list_membership": [
                   3
               ]
           }
       }
   }

**List Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Campaign
   * - ``name``
     - string
     - Name of the Campaign
   * - ``dateAdded``
     - ``datetime``
     - Date/time string for when the Contact got added to the Campaign
   * - ``manuallyAdded``
     - boolean
     - ``true`` if the Contact was manually added to the Campaign versus added by a Contact list
   * - ``manuallyRemoved``
     - boolean
     - ``true`` if the Contact was manually removed from the Campaign when the Contact's list got assigned to the Campaign
   * - ``listMembership``
     - array
     - Array of Contact list IDs this Contact belongs to that's also associated with this Campaign


.. vale off

Change Campaign Memberships
***************************

.. vale on

See `Campaigns <#campaigns>`_.

.. vale off

Get Contact's Events
********************

.. vale on

.. code-block:: php

   <?php

   $events = $contactApi->getEvents($id, $search, $includeEvents, $excludeEvents, $orderBy, $orderByDir, $page);

.. warning:: Deprecated. Use ``getActivityForContact`` instead.

Get a list of Contact events the Contact created.

**Query Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - ``id``
     - Contact ID
   * - ``filters[search]``
     - String or search command to filter events by.
   * - ``filters[includeEvents][]``
     - Array of event types to include.
   * - ``filters[excludeEvents][]``
     - Array of event types to exclude.
   * - ``order``
     - Array of Column and Direction [COLUMN, DIRECTION].
   * - ``page``
     - What ``page`` number to load

.. vale off

**HTTP Request**

.. vale on

``GET /contacts/ID/events``

.. warning:: Deprecated. Use ``GET /contacts/ID/activity`` instead.

**Response**

``Expected response code: 200``

.. code-block:: json

   {
     "events":[
       {
         "event":"lead.identified",
         "icon":"fa-User",
         "eventType":"Contact identified",
         "eventPriority":-4,
         "timestamp":"2016-06-09T21:39:08+00:00",
         "featured":true
       }
     ],
     "filters":{
       "search":"",
       "includeEvents":[
         "lead.identified"
       ],
       "excludeEvents":[]
     },
     "order":[
       "",
       "ASC"
     ],
     "types":{
       "lead.ipadded":"Accessed from IP",
       "asset.download":"Asset downloaded",
       "campaign.event":"Campaign action triggered",
       "lead.create":"Contact created",
       "lead.identified":"Contact identified",
       "lead.donotcontact":"Do not contact",
       "email.read":"Email read",
       "email.sent":"Email sent",
       "email.failed":"Failed",
       "form.submitted":"Form submitted",
       "page.hit":"Page hit",
       "point.gained":"Point gained",
       "stage.changed":"Stage changed",
       "lead.utmtagsadded":"UTM tags recorded",
       "page.videohit":"Video View Event"
     },
     "total":1,
     "page":1,
     "limit":25,
     "maxPages":1
   }

**List Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``events``
     - array
     - List of events
   * - ``event``
     - string
     - ID of the event type
   * - ``icon``
     - string
     - Icon class from FontAwesome
   * - ``eventType``
     - string
     - Human name of the event
   * - ``eventPriority``
     - string
     - Priority of the event
   * - ``timestamp``
     - timestamp
     - Date and time when the event got created
   * - ``featured``
     - boolean
     - Flag whether this is a featured event
   * - ``filters``
     - array
     - Filters used in the query
   * - ``order``
     - array
     - Ordering used in the query
   * - ``types``
     - array
     - Array of available event types
   * - ``total``
     - int
     - Total number of events in the request
   * - ``page``
     - int
     - Current ``page`` number
   * - ``limit``
     - int
     - Limit of events per ``page``
   * - ``maxPages``
     - int
     - How many ``pages`` of events are there

.. vale off

Get activity events for specific Contact
****************************************

.. vale on

.. code-block:: php

   <?php

   $events = $contactApi->getActivityForContact($id, $search, $includeEvents, $excludeEvents, $orderBy, $orderByDir, $page, $dateFrom, $dateTo);

**Query Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - ``id``
     - Contact ID
   * - ``filters[search]``
     - String or search command to filter events by.
   * - ``filters[includeEvents][]``
     - Array of event types to include.
   * - ``filters[excludeEvents][]``
     - Array of event types to exclude.
   * - ``filters[dateFrom]``
     - Date from filter. Must be type of ``\DateTime`` for the PHP API Library and in format ``Y-m-d H:i:s`` for HTTP param
   * - ``filters[dateTo]``
     - Date to filter. Must be type of ``\DateTime`` for the PHP API Library and in format ``Y-m-d H:i:s`` for HTTP param
   * - ``order``
     - Array of Column and Direction [COLUMN, DIRECTION].
   * - ``page``
     - What ``page`` number to load
   * - ``limit``
     - Limit of events per ``page``

Get a list of Contact events the Contact had created.

.. vale off

**HTTP Request**

.. vale on

``GET /contacts/ID/activity``

**Response**

``Expected response code: 200``

.. code-block:: json

   {
     "events":[
       {
         "event":"lead.identified",
         "icon":"fa-User",
         "eventType":"Contact identified",
         "eventPriority":-4,
         "timestamp":"2016-06-09T21:39:08+00:00",
         "featured":true
       }
     ],
     "filters":{
       "search":"",
       "includeEvents":[
         "lead.identified"
       ],
       "excludeEvents":[]
     },
     "order":[
       "",
       "ASC"
     ],
     "types":{
       "asset.download": "Asset downloaded",
       "campaign.event": "Campaign action triggered",
       "campaign.event.scheduled": "Campaign event scheduled",
       "lead.donotcontact": "Do not contact",
       "email.failed": "Email failed",
       "email.read": "Email read",
       "email.sent": "Email sent",
       "form.submitted": "Form submitted",
       "lead.imported": "Imported",
       "page.hit": "Page hit",
       "point.gained": "Point gained",
       "stage.changed": "Stage changed",
       "lead.utmtagsadded": "UTM tags recorded",
       "page.videohit": "Video view event"
     },
     "total":1,
     "page":1,
     "limit":25,
     "maxPages":1
   }

**List Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``events``
     - array
     - List of events
   * - ``event``
     - string
     - ID of the event type
   * - ``icon``
     - string
     - Icon class from FontAwesome
   * - ``eventType``
     - string
     - Human name of the event
   * - ``eventPriority``
     - string
     - Priority of the event
   * - ``timestamp``
     - timestamp
     - Date and time when the event got created
   * - ``featured``
     - boolean
     - Flag whether this is a featured event
   * - ``filters``
     - array
     - Filters used in the query
   * - ``order``
     - array
     - Ordering used in the query
   * - ``types``
     - array
     - Array of available event types
   * - ``total``
     - int
     - Total number of events in the request
   * - ``page``
     - int
     - Current ``page`` number
   * - ``limit``
     - int
     - Limit of events per ``page``
   * - ``maxPages``
     - int
     - How many ``pages`` of events are there

.. vale off

Get Activity events for all Contacts
************************************

.. vale on

.. code-block:: php

   <?php

   $events = $contactApi->getActivity($search, $includeEvents, $excludeEvents, $orderBy, $orderByDir, $page, $dateFrom, $dateTo);

**Query Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Description
   * - ``filters[search]``
     - String or search command to filter events by.
   * - ``filters[includeEvents][]``
     - Array of event types to include.
   * - ``filters[excludeEvents][]``
     - Array of event types to exclude.
   * - ``filters[dateFrom]``
     - Date from filter. Must be type of ``\DateTime`` for the PHP API Library and in format ``Y-m-d H:i:s`` for HTTP param
   * - ``filters[dateTo]``
     - Date to filter. Must be type of ``\DateTime`` for the PHP API Library and in format ``Y-m-d H:i:s`` for HTTP param
   * - ``orderBy``
     - Column to sort by. Can use any column listed in the response.
   * - ``orderByDir``
     - Sort direction: ``asc`` or ``desc``.
   * - ``page``
     - What ``page`` number to load

.. vale off

**HTTP Request**

.. vale on

``GET /contacts/activity``

**Response**

``Expected response code: 200``

.. code-block:: json

    {
     "events": [
       {
         "event": "meeting.attended",
         "eventId": "meeting.attended65",
         "eventLabel": "Attended meeting - Mautic instance",
         "eventType": "Meeting attendance",
         "timestamp": "2017-08-03T21:03:04+00:00",
         "contactId": "12180",
         "details": {
           "eventName": "mautic-instance",
           "eventId": "371343405",
           "eventDesc": "Mautic instance",
           "joinUrl": ""
         }
       },
       {
         "event": "webinar.attended",
         "eventId": "webinar.attended67",
         "eventLabel": "Attended webinar - Mautic",
         "eventType": "Webinar attendance",
         "timestamp": "2017-08-03T21:03:04+00:00",
         "contactId": "12180",
         "details": {
           "eventName": "mautic",
           "eventId": "530287395",
           "eventDesc": "Mautic",
           "joinUrl": ""
         }
       },
       {
         "event": "webinar.registered",
         "eventId": "webinar.registered66",
         "eventLabel": "Registered for webinar - Mautic",
         "eventType": "Webinar registered for",
         "timestamp": "2017-08-03T21:03:04+00:00",
         "contactId": "12180",
         "details": {
           "eventName": "mautic",
           "eventId": "530287395",
           "eventDesc": "Mautic",
           "joinUrl": "https://global.gotowebinar.com/join/xxx/xxx"
         }
       },
       {
         "event": "campaign.event",
         "eventId": "campaign.event892",
         "eventLabel": {
           "label": "Contact field value \/ Campaign Date",
           "href": "\/s\/campaigns\/view\/498"
         },
         "eventType": "Campaign action triggered",
         "timestamp": "2017-08-03T00:58:25+00:00",
         "contactId": "12281",
         "details": {
           "log": {
             "dateTriggered": "2017-08-03T00:58:25+00:00",
             "metadata": [],
             "type": "lead.field_value",
             "isScheduled": "0",
             "logId": "892",
             "eventId": "1457",
             "campaignId": "498",
             "eventName": "Contact field value",
             "campaignName": "Campaign Date"
           }
         }
       },
       {
         "event": "email.sent",
         "eventId": "email.sent796",
         "eventLabel": {
           "label": "2017-05-23 - Email - Leads - Nurture Flow (Monica) 1",
           "href": "http:\/\/example.com\/email\/view\/597a116ae69ca",
           "isExternal": true
         },
         "eventType": "Email sent",
         "timestamp": "2017-07-27T16:14:34+00:00",
         "contactId": "16419",
         "details": {
           "stat": {
             "id": "796",
             "dateSent": "2017-07-27T16:14:34+00:00",
             "subject": "How to make the case for digital",
             "isRead": "0",
             "isFailed": "0",
             "viewedInBrowser": "0",
             "retryCount": "0",
             "idHash": "597a116ae69ca",
             "openDetails": [],
             "storedSubject": "How to make the case for digital",
             "timeToRead": false,
             "emailId": "78",
             "emailName": "2017-05-23 - Email - Leads - Nurture Flow (Monica) 1"
           },
           "type": "sent"
         }
       },
       {
         "event": "email.read",
         "eventId": "email.read769",
         "eventLabel": {
           "label": "Custom Email: device test",
           "href": "http:\/\/example.com\/email\/view\/5966b0cd571f4",
           "isExternal": true
         },
         "eventType": "Email read",
         "timestamp": "2017-07-12T23:30:56+00:00",
         "contactId": "13930",
         "details": {
           "stat": {
             "id": "769",
             "dateRead": "2017-07-12T23:30:56+00:00",
             "dateSent": "2017-07-12T23:29:17+00:00",
             "isRead": "1",
             "isFailed": "0",
             "viewedInBrowser": "0",
             "retryCount": "0",
             "idHash": "5966b0cd571f4",
             "openDetails": [
               {
                 "datetime": "2017-07-12 23:30:56",
                 "Useragent": "Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/59.0.3071.115 Safari\/537.36",
                 "inBrowser": false
               },
               {
                 "datetime": "2017-07-13 02:18:51",
                 "Useragent": "Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/59.0.3071.115 Safari\/537.36",
                 "inBrowser": false
               }
             ],
             "storedSubject": "device test",
             "timeToRead": "PT1M39S"
           },
           "type": "read"
         }
       },
       {
         "event": "lead.ipadded",
         "eventId": "lead.ipadded3263",
         "eventLabel": "127.0.0.1",
         "eventType": "Accessed from IP",
         "timestamp": "2017-07-27T03:09:09+00:00",
         "contactId": "3263",
         "details": []
       },
       {
         "event": "form.submitted",
         "eventId": "form.submitted503",
         "eventLabel": {
           "label": "3586 Test",
           "href": "\/s\/forms\/view\/143"
         },
         "eventType": "Form submitted",
         "timestamp": "2017-07-27T03:09:07+00:00",
         "contactId": "16417",
         "details": {
           "submission": {
             "id": 503,
             "ipAddress": {
               "ip": "127.0.0.1"
             },
             "form": {
               "id": 143,
               "name": "3586 Test",
               "alias": "3586_test"
             },
             "dateSubmitted": "2017-07-27T03:09:07+00:00",
             "referer": "http:\/\/example.com\/form\/143",
             "results": {
               "form_id": "143",
               "email": "formtest7@example.com",
               "f_name": ""
             }
           },
           "form": {
             "id": 143,
             "name": "3586 Test",
             "alias": "3586_test"
           },
           "page": {}
         }
       },
       {
         "event": "page.hit",
         "eventLabel": {
           "label": "Test",
           "href": "\/s\/pages\/view\/8"
         },
         "eventType": "Page hit",
         "timestamp": "2017-07-21T20:36:49+00:00",
         "contactId": "16380",
         "details": {
           "hit": {
             "UserAgent": "Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/59.0.3071.115 Safari\/537.36",
             "dateHit": "2017-07-21T20:36:49+00:00",
             "url": "http:\/\/example.com\/uncategorized\/translation-test1",
             "query": {
               "pageUrl": "http:\/\/example.com\/uncategorized\/translation-test1"
             },
             "clientInfo": "a:6:{s:4:\"type\";s:7:\"browser\";s:4:\"name\";s:6:\"Chrome\";s:10:\"short_name\";s:2:\"CH\";s:7:\"version\";s:4:\"59.0\";s:6:\"engine\";s:5:\"Blink\";s:14:\"engine_version\";s:0:\"\";}",
             "device": "desktop",
             "deviceOsName": "Mac",
             "deviceBrand": "",
             "deviceModel": "",
             "pageId": "8"
           }
         }
       },
       {
         "event": "point.gained",
         "eventLabel": "2: Page Hit Test \/ 20",
         "eventType": "Point gained",
         "timestamp": "2017-07-20T22:38:28+00:00",
         "contactId": "16379",
         "details": {
           "log": {
             "eventName": "2: Page Hit Test",
             "actionName": "hit",
             "dateAdded": "2017-07-20T22:38:28+00:00",
             "type": "url",
             "delta": "20",
             "id": "2"
           }
         }
       },
       {
         "event": "lead.imported",
         "eventId": "lead.imported6324",
         "eventType": "Imported",
         "eventLabel": {
           "label": "Contact import failed from FakeNameGenerator.com_20d05d9c.csv",
           "href": "\/s\/contacts\/import\/view\/4"
         },
         "timestamp": "2017-07-17T21:42:35+00:00",
         "details": {
           "id": "6324",
           "bundle": "lead",
           "object": "import",
           "action": "failed",
           "properties": {
             "line": 2001,
             "file": "FakeNameGenerator.com_20d05d9c.csv",
             "error": "No data found"
           },
           "UserId": "2",
           "UserName": "Bob Smith",
           "objectId": "4",
           "dateAdded": "2017-07-17T21:42:35+00:00"
         }
       },
       {
         "event": "asset.download",
         "eventId": "asset.download11",
         "eventLabel": {
           "label": "Download Mautic",
           "href": "\/s\/assets\/view\/1"
         },
         "eventType": "Asset downloaded",
         "timestamp": "2017-04-04T01:49:13+00:00",
         "details": {
           "asset": {
             "id": 1,
             "title": "Download Mautic",
             "alias": "download-mautic",
             "description": "test"
           },
           "assetDownloadUrl": "http:\/\/example.com\/asset\/1:download-mautic"
         }
       },
     ],
     "filters": {
       "search": "",
       "includeEvents": [],
       "excludeEvents": []
     },
     "order": [
       "timestamp",
       "DESC"
     ],
     "types": {
       "lead.ipadded": "Accessed from IP",
       "asset.download": "Asset downloaded",
       "meeting.attended": "Attended meeting",
       "webinar.attended": "Attended webinar",
       "campaign.event": "Campaign action triggered",
       "campaign.event.scheduled": "Campaign event scheduled",
       "lead.donotcontact": "Do not contact",
       "email.failed": "Email failed",
       "email.read": "Email read",
       "email.sent": "Email sent",
       "form.submitted": "Form submitted",
       "lead.imported": "Imported",
       "page.hit": "Page hit",
       "point.gained": "Point gained",
       "meeting.registered": "Registered for meeting",
       "webinar.registered": "Registration to Webinar",
       "stage.changed": "Stage changed",
       "lead.utmtagsadded": "UTM tags recorded",
       "page.videohit": "Video view event"
     },
     "total": 12,
     "page": 1,
     "limit": 25,
     "maxPages": 1
   }

**List Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``events``
     - array
     - List of events
   * - ``event``
     - string
     - ID of the event type
   * - ``icon``
     - string
     - Icon class from FontAwesome
   * - ``eventType``
     - string
     - Human name of the event
   * - ``eventPriority``
     - string
     - Priority of the event
   * - ``contactId``
     - int
     - ID of the Contact that created the event
   * - ``timestamp``
     - timestamp
     - Date and time when the event got created
   * - ``featured``
     - boolean
     - Flag whether this is a featured event
   * - ``filters``
     - array
     - Filters used in the query
   * - ``order``
     - array
     - Ordering used in the query
   * - ``types``
     - array
     - Array of available event types
   * - ``total``
     - int
     - Total number of events in the request
   * - ``page``
     - int
     - Current ``page`` number
   * - ``limit``
     - int
     - Limit of events per ``page``
   * - ``maxPages``
     - int
     - How many ``pages`` of events are there

.. vale off

Get Contact's Companies
***********************

.. vale on

.. code-block:: php

   <?php

   $companies = $contactApi->getContactCompanies($contactId);

Get a list of Contact's Companies the Contact belongs to.

.. vale off

**HTTP Request**

.. vale on

``GET /contacts/ID/companies``

**Response**

``Expected response code: 200``

.. code-block:: json

   {
     "total":1,
     "companies":[
       {
         "company_id":"420",
         "date_associated":"2016-12-27 15:03:43",
         "is_primary":"0",
         "companyname":"test",
         "companyemail":"test@example.com",
         "companycity":"Raleigh",
         "score":"0",
         "date_added":"2016-12-27 15:03:42"
       }
     ]
   }

**List Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``company_id``
     - int
     - Company ID
   * - ``date_associated``
     - ``datetime``
     - Date and time when the Contact got associated to the Company
   * - ``date_added``
     - ``datetime``
     - Date and time when the Company got created
   * - ``is_primary``
     - boolean
     - Flag whether the Company association is primary
   * - ``companyname``
     - string
     - Name of the Company
   * - ``companyemail``
     - string
     - Email of the Company
   * - ``companycity``
     - string
     - City of the Company
   * - ``score``
     - int
     - Score of the Company

.. vale off

Get Contact's Devices
*********************

.. vale on

.. code-block:: php

   <?php

   $devices = $contactApi->getContactDevices($contactId);

Get a list of Contact's devices the Contact has used.

.. vale off

**HTTP Request**

.. vale on

``GET /contacts/ID/devices``

**Response**

``Expected response code: 200``

.. code-block:: json

   {
     "total":1,
     "devices":[
       {
         "id":60,
         "lead":[],
         "clientInfo":[],
         "device":"desktop",
         "deviceOsName":"Ubuntu",
         "deviceOsShortName":"UBT",
         "deviceOsPlatform":"x64"
       }
     ]
   }

**List Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - Device ID
   * - ``clientInfo``
     - array
     - Array with various information about the client/browser
   * - ``device``
     - string
     - Device type; desktop, mobile..
   * - ``deviceOsName``
     - string
     - Full device OS name
   * - ``deviceOsShortName``
     - string
     - Short device OS name
   * - ``deviceOsPlatform``
     - string
     - OS platform
