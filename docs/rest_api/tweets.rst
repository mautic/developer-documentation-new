Tweets
######

Use this endpoint to obtain details on Mautic's tweets.

.. code-block:: php

   <?php
   use Mautic\MauticApi;
   use Mautic\Auth\ApiAuth;

   // ...
   $initAuth        = new ApiAuth();
   $auth            = $initAuth->newAuth($settings);
   $apiUrl          = "https://mautic.example.com";
   $api             = new MauticApi();
   $tweetApi = $api->newApi("tweets", $auth, $apiUrl);

.. vale off

Get Tweet
*********

.. vale on

.. code-block:: php

   <?php

   //...
   $tweet = $tweetApi->get($id);

Get an individual Tweet by ID.

.. vale off

**HTTP Request**

.. vale on

``GET /tweets/ID``

**Response**

``Expected Response Code: 200``

.. code-block:: json

   {  
       "tweet": {
           "isPublished": true,
           "dateAdded": "2017-02-03T17:51:58+01:00",
           "dateModified": "2017-03-28T11:03:03+02:00",
           "createdBy": 1,
           "createdByUser": "John Doe",
           "modifiedBy": 1,
           "modifiedByUser": "John Doe",
           "id": 1,
           "name": "Thank you tweet",
           "text": "Hi {twitter_handle}\n\nThanks for ...",
           "language": "en",
           "category": {
               "createdByUser": "John Doe",
               "modifiedByUser": null,
               "id": 185,
               "title": "Thank you tweets",
               "alias": "thank-you-tweets",
               "description": null,
               "color": "244bc9",
               "bundle": "global"
           },
           "tweetId": null,
           "mediaId": null,
           "mediaPath": null,
           "sentCount": 3,
           "favoriteCount": 0,
           "retweetCount": 0,
           "description": "Used in the Product A campaign 1"
       }
   }

**Tweet Properties**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Tweet
   * - ``name``
     - string
     - Title of the Tweet
   * - ``text``
     - string
     - Message of the Tweet
   * - ``isPublished``
     - boolean
     - Published state
   * - ``publishUp``
     - datetime/null
     - Tweet publish date/time
   * - ``publishDown``
     - datetime/null
     - Tweet unpublish date/time
   * - ``dateAdded``
     - ``datetime``
     - Tweet creation date/time
   * - ``createdBy``
     - int
     - ID of the User that created the Tweet
   * - ``createdByUser``
     - string
     - Name of the User that created the Tweet
   * - ``dateModified``
     - datetime/null
     - Date/time Tweet was last modified
   * - ``modifiedBy``
     - int
     - ID of the User that last modified the Tweet
   * - ``modifiedByUser``
     - string
     - Name of the User that last modified the Tweet
   * - ``language``
     - string
     - Language locale of the Tweet
   * - ``category``
     - null/object
     - Category

.. vale off

List Tweets
***********

.. vale on

.. code-block:: php

   <?php
   // ...

   $tweets = $tweetApi->getList($searchFilter, $start, $limit, $orderBy, $orderByDir, $publishedOnly, $minimal);

.. vale off

**HTTP Request**

.. vale on

``GET /tweets``

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
     - Limit number of entities to return. Defaults to the system configuration for pagination - defaults to 30.
   * - ``orderBy``
     - Column to sort by. Can use any column listed in the response.
   * - ``orderByDir``
     - Sort direction: ``asc`` or ``desc``.
   * - ``publishedOnly``
     - Only return currently published entities.
   * - ``minimal``
     - Return only array of entities without additional lists in it.


**Response**

``Expected Response Code: 200``

.. code-block:: json

   {  
       "total":1,
       "tweets":[  
           {
               "isPublished": true,
               "dateAdded": "2017-02-03T17:51:58+01:00",
               "dateModified": "2017-03-28T11:03:03+02:00",
               "createdBy": 1,
               "createdByUser": "John Doe",
               "modifiedBy": 1,
               "modifiedByUser": "John Doe",
               "id": 1,
               "name": "Thank you tweet",
               "text": "Hi {twitter_handle}\n\nThanks for ...",
               "language": "en",
               "category": null,
               "tweetId": null,
               "mediaId": null,
               "mediaPath": null,
               "favoriteCount": 0,
               "retweetCount": 0,
               "description": "Used in the Product A campaign 1"
           }
       ]
   }

**Properties**

Same as `Get Tweet <#get-tweet>`_.

.. vale off

Create Tweet
************

.. vale on

.. code-block:: php

   <?php 

   $data = array(
       'name'    => 'Tweet A',
       'heading' => 'Hello World!'
       'message' => 'This is my first Tweet created via API.',
   );

   $tweet = $tweetApi->create($data);

Create a new Tweet.

.. vale off

**HTTP Request**

.. vale on

``POST /tweets/new``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Tweet
   * - ``name``
     - string
     - Title of the Tweet
   * - ``text``
     - string
     - Message of the Tweet
   * - ``url``
     - string
     - URL to go to when the Tweet gets clicked
   * - ``isPublished``
     - boolean
     - Published state
   * - ``publishUp``
     - datetime/null
     - Tweet publish date/time
   * - ``publishDown``
     - datetime/null
     - Tweet unpublish date/time
   * - language
     - string
     - Language locale of the Tweet


**Response**

``Expected Response Code: 201``

**Properties**

Same as `Get Tweet <#get-tweet>`_.

.. vale off

Edit Tweet
**********

.. vale on

.. code-block:: php

   <?php

   $id   = 1;
   $data = array(
       'name' => 'Tweet A',
       'text' => 'This is my first Tweet created via API.',
   );

   // Create new a Tweet if ID 1 isn't found?
   $createIfNotFound = true;

   $tweet = $tweetApi->edit($id, $data, $createIfNotFound);

Edit a new Tweet. Note that this supports PUT or PATCH depending on the desired behavior.

**PUT** creates a Tweet if the given ID doesn't exist and clears all the Tweet information, adds the information from the request.

**PATCH** fails if the Tweet with the given ID doesn't exist and updates the Tweet field values with the values from the request.

.. vale off

**HTTP Request**

.. vale on

To edit a Tweet and return a 404 if the Tweet isn't found:

``PATCH /tweets/ID/edit``

To edit a Tweet and create a new one if the Tweet isn't found:

``PUT /tweets/ID/edit``

**POST Parameters**

.. list-table::
   :header-rows: 1

   * - Name
     - Type
     - Description
   * - ``id``
     - int
     - ID of the Tweet
   * - ``name``
     - string
     - Title of the Tweet
   * - ``text``
     - string
     - Message of the Tweet
   * - ``url``
     - string
     - URL to go to when the Tweet gets clicked
   * - ``isPublished``
     - boolean
     - Published state
   * - ``publishUp``
     - datetime/null
     - Tweet publish date/time
   * - ``publishDown``
     - datetime/null
     - Tweet unpublish date/time
   * - ``language``
     - string
     - Language locale of the Tweet


**Response**

If ``PUT``, the expected response code is ``200`` if the editing an existing Tweet ``201`` if creating a new one.

If ``PATCH``, the expected response code is ``200``.

**Properties**

Same as `Get Tweet <#get-tweet>`_.

.. vale off

Delete Tweet
************

.. vale on

.. code-block:: php

   <?php

   $tweet = $tweetApi->delete($id);

Delete a Tweet.

.. vale off

**HTTP Request**

.. vale on

``DELETE /tweets/ID/delete``

**Response**

``Expected Response Code: 200``

**Properties**

Same as `Get Tweet <#get-tweet>`_.
