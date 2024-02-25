Tracking script ``MauticJS (mtc.js)``
#####################################

Mautic provides a means for Plugins to inject custom JavaScript into ``mtc.js``, the PHP generated script that manages Mautic's tracking pixel and Dynamic Web Content.
You can embed ``mtc.js`` in third party websites to manage communication between those and Mautic.

.. note:: For basic guidance on how to implement ``mtc.js`` on your website, please visit the :xref:`Mautic User Documentation<Mautic tracking script docs>`.

``mtc.js``
**********

.. code-block:: php

   <?php

   namespace Mautic\PageBundle\EventListener;

   use Mautic\CoreBundle\CoreEvents;
   use Mautic\CoreBundle\Event\BuildJsEvent;
   use Mautic\PageBundle\Event\TrackingEvent;
   use Mautic\PageBundle\PageEvents;
   use Symfony\Component\EventDispatcher\EventSubscriberInterface;

   class TrackingSubscriber implements EventSubscriberInterface
   {
       public static function getSubscribedEvents()
       {
           return [
               CoreEvents::BUILD_MAUTIC_JS    => ['onBuildJs', 0],
               PageEvents::ON_CONTACT_TRACKED => ['onContactTracked', 0],
           ];
       }

       public function onBuildJs(BuildJsEvent $event)
       {
           $event->appendJs(
               <<<JS

           document.addEventListener('mauticPageEventDelivered', function(e) {
               var detail   = e.detail;
               if (detail.response && detail.response.events && detail.response.events.tracked) {
                   console.log(detail.response.events.tracked);
               }
         });

   JS
           );
       }

       public function onContactTracked(TrackingEvent $event)
       {
           $contact  = $event->getContact();
           $response = $event->getResponse();

           $response->set(
               'tracked',
               [
                   'email' => $contact->getEmail()
               ]
           );
       }
   }

To inject custom JavaScript into ``mtc.js``, use an :ref:`Event Listener<plugins/event_listeners:Event listeners>` for the ``CoreEvents::BUILD_MAUTIC_JS`` event.
This event receives a ``Mautic\CoreBundle\Event\BuildJsEvent`` object where ``$event->appendJs($js, $sectionName);`` can be used to inject the script's code.

.. warning:: Note that the code that triggers the tracking call to Mautic has a priority of -255. Thus, any listener to this event should use a priority greater than -255.

.. warning:: Only use native JavaScript or <a href="#mauticjs-api-functions">MauticJS API functions</a> since ``jQuery`` and other libraries aren't guaranteed to be available in third party websites.


Hooking into the tracking process and returning custom responses
****************************************************************


If you need to do something during the request to track the Contact through ``/mtc/event``, or append to the payload returned to the tracking code which you can leverage by custom JavaScript injected through ``CoreEvents::BUILD_MAUTIC_JS``, subscribe to the ``PageEvents::ON_CONTACT_TRACKED`` event.
The listener can inject a custom payload through the ``Mautic\PageBundle\Event\TrackingEvent::set`` method.
This will expose the payload to the tracking code's ``mauticPageEventDelivered`` event in the ``detail.response.events`` object. See the PHP code example. 

.. vale off

JavaScript Form processing hooks
********************************

.. vale on

.. code-block:: js

   if (typeof MauticFormCallback == 'undefined') {
       var MauticFormCallback = {};
   }
   MauticFormCallback['replaceWithFormName'] = {
       onValidateEnd: function (formValid) {
            // before form submit
       },
       onResponse: function (response) { 
            // after form submit
       }
   };

If you wish to run additional code before or after submission of the Form, create a ``MauticFormCallback`` object.
In the example code, replace ``replaceWithFormName`` with the name of your Form. 

``onValidateEnd`` and ``onResponse`` are actions called by ``Form.customCallbackHandler``. 

``onValidate()``
================

Called before built-in Form validation.
Implement this callback to override the built-in Form validation logic.

Your callback's return value determines the processing of the Form:

1. Return ``True`` to skip the built-in form validation and **continue** with form processing.
2. Return ``False`` to skip the built-in form validation and **prevent** the form submission.
3. Return ``null`` to execute built-in form validation and let its logic determine whether to continue with or prevent the form submission.

Returning ``True`` or ``False`` will skip the execution of `onValidateStart`.

.. code-block:: js

   MauticFormCallback['replaceWithFormName'] = {
       onValidate: function () {
           // executed before built-in form validation
           var formIsGood = True;
           var dontUpdate = False;
           if(dontUpdate){
               return null;
           }else if(formIsGood){
               return True;
           }else if(!formIsGood){
               return False;
           }
       },
   };

``onValidateStart()``
=====================

Called at the beginning of the default form validation, this receives no values and a return value isn't required and isn't processed.

.. warning:: `onValidateStart` will not get executed if you add the ``onValidate`` callback and it returns ``True`` or ``False``.

.. code-block:: js

   MauticFormCallback['replaceWithFormName'] = {
       onValidateStart: function () {
            // executed before built-in form validation
       },
   };

``onValidateEnd(formValid)``
============================

Called after all form validations are complete - either the default validations and/or the ``onValidate`` callback - and before the form gets submitted.
Receives ``formValid`` to determine if the form is valid.

If this callback returns ``False`` then this prevents submitting the form.

.. code-block:: js

   MauticFormCallback['replaceWithFormName'] = {
       onValidateEnd: function (formValid) {
            // before form submit
            // return False; // prevents submitting the form
       },
   };

``onErrorMark(callbackData)``
=============================

Called during error marking. It receives a ``callbackData`` object. Return ``True`` to skip the default error marking.

.. code-block:: js

   var callbackData = {
       containerId: containerId,
       valid: valid,
       validationMessage: callbackValidationMessage
   };

   MauticFormCallback['replaceWithFormName'] = {
       onErrorMark: function (callbackData) {
            // called during error marking
       },
   };

``onErrorClear(containerId)``
=============================

Called to clear an existing error. Receives ``containerId`` with the id of the element containing the error. Return ``True`` to skip the default error clearing.

.. code-block:: js

   MauticFormCallback['replaceWithFormName'] = {
       onErrorClear: function (containerId) {
            // called to clear an existing error
       },
   };

``onResponse(response)``
========================

Called prior to default form submission response processing. Receives ``response`` containing the form submission response.
Return ``True`` to skip the default Form submission response processing.

.. code-block:: js

   MauticFormCallback['replaceWithFormName'] = {
       onResponse: function (response) {
            // called to process the response to the form submission
       },
   };

``onResponseStart(response)``
=============================

Called at the beginning of the default form submission response processing. Receives ``response`` containing the form submission response.
Return value isn't required and isn't processed.

.. warning:: onResponseStart may not get executed if the default response processing gets handled during the ``onResponse`` callback

.. code-block:: js

   MauticFormCallback['replaceWithFormName'] = {
       onResponseStart: function (response) {
            // called to process the response to the form submission
       },
   };

``onResponseEnd(response)``
===========================

.. code-block:: js

   MauticFormCallback['replaceWithFormName'] = {
       onResponseEnd: function (response) {
            // called to process the response to the form submission
       },
   };

Called at the end default form submission response processing. Receives ``response`` containing the form submission response.
Return value isn't required and isn't processed.

.. warning:: onResponseEnd may not get executed if the default response processing gets handled during the ``onResponse`` callback


``onMessageSet(messageObject)``
===============================

Called prior to default message insertion. Receives a ``messageObject`` containing the message and message type.
Return ``True`` to skip the default message insertion.

.. code-block:: js

   var messageObject = {
       message: message,
       type: type
   };

   MauticFormCallback['replaceWithFormName'] = {
       onErrorMark: function (messageObject) {
            // called prior to default message insertion
       },
   };

``onSubmitButtonDisable(messageObject)``
========================================

Called prior to default disabling of the submit button. Receives no values. Return ``True`` to skip the default disabling of the submit button.

.. code-block:: js

   MauticFormCallback['replaceWithFormName'] = {
       onErrorMark: function (messageObject) {
            // called prior to default message insertion
       },
   };

``onSubmitButtonEnable()``
==========================

Called prior to default enabling of the submit button. Receives no values. Return ``True`` to skip the default enabling of the submit button.

.. code-block:: js

   MauticFormCallback['replaceWithFormName'] = {
       onErrorMark: function (messageObject) {
            // called prior to default message insertion
       },
   };

``onShowNextPage()``
====================

.. vale off

Called prior to going to the next page in the form. Useful to adjust the DOM prior to making the page visible.

.. vale on

.. code-block:: js

   MauticFormCallback['replaceWithFormName'] = {
       onShowNextPage: function (pageNumber) {
            // called prior to going to the next page
       },
   };

``onShowPreviousPage()``
========================

.. vale off

Called prior to going back to a previous page in the form. Useful to adjust the DOM prior to making the page visible.

.. vale on

.. code-block:: js

   MauticFormCallback['replaceWithFormName'] = {
       onShowPreviousPage: function (pageNumber) {
            // called prior to going back to previous page
       },
   };

.. vale off

MauticJS API functions
**********************

.. vale on

``MauticJS.serialize(object)``
==============================

This method transforms an object properties into a key=value string, concatenating them with an ampersand.
It's used when submitting data via ``MauticJS.makeCORSRequest``.

.. code-block:: js

   var obj = {firstname: "John", lastname: "Doe"};

   var serialized = MauticJS.serialize(obj);

   alert(serialized); // Shows "firstname=John&lastname=Doe"

``MauticJS.documentReady(functionName|function)``
=================================================

This method validates if the document has finished rendering, then executes the given function.
The function argument can be the name of a function or an anonymous function.

.. code-block:: js

   function test() {
       alert('test');
   }

   MauticJS.documentReady(test);

``MauticJS.iterateCollection(collection)(functionName|function)``
=================================================================

This method iterates over the provided collection, which can be an ``array``, ``object``, ``HTMLCollection``, etc. - it uses the provided function argument.
The function argument can be the name of a function or an anonymous function. The function receives the collection node and the iteration number as arguments.

.. code-block:: js

   var videos = document.getElementsByTagName('video');

   // Add a custom data attribute to all videos
   MauticJS.iterateCollection(videos)(function(node, i) {
       node.dataset.customAttribute = 'test';
   });

``MauticJS.log(arguments)``
===========================

This method is a lightweight wrapper around ``console.log``. It exists because some browsers don't provide this feature.
It takes any number of arguments, logs them, then passes those same arguments to the ``console.log`` method if it exists.

.. code-block:: js

   MauticJS.log('Something happened');

``MauticJS.createCORSRequest(method, url)``
===========================================

This method creates an ``XMLHttpRequest``, then checks to see if it supports the ``withCredentials`` property.
If not, the User is probably on Windows, so it then checks for the existence of ``XDomainRequest``, then creates it if found.
Finally, it opens then returns the ``XHR``. You can use that to send cross-domain requests that include the cookies for the domain.
It's used internally within the ``MauticJS.makeCORSRequest`` method.

.. code-block:: js

   MauticJS.createCORSRequest('GET', 'https://mymautic.com/dwc/slot1');

``MauticJS.makeCORSRequest(method, url, data, callbackSuccess, callbackError)``
===============================================================================

This method uses ``MauticJS.createCORSRequest`` to open a cross domain request to the specified URL, then sets the ``callbackSuccess`` and ``callbackError`` values accordingly.
You may omit either of the callbacks. If you do, the callbacks get replaced with a basic function that uses ``MauticJS.log(response)`` to log the response from the request.
The callback methods receive the server response and the ``XHR`` object as arguments.
If the response is a JSON string, it's automatically parsed to a JSON object.
The data argument gets serialized using ``MauticJS.serialize(data)``, then sent with the request to the server.
All requests made this way have the ``X-Requested-With`` header set to ``XMLHttpRequest``.

.. code-block:: js

   MauticJS.makeCORSRequest('GET', 'https://mymautic.com/dwc/slot1', [], function (response, xhr) {
       if (response.success) {
           document.getElementById('slot1').innerHTML = response.content;
       }
   });

``MauticJS.parseTextToJSON(maybeJSON)``
=======================================

This method takes a text string and verifies whether it's a valid JSON string. If so, it parses it into a JSON object and returns.
If not, then it simply returns the argument passed to it.

.. code-block:: js

   var text = '{"firstname": "John", "lastname": "Doe"}';

   var json = MauticJS.parseTextToJSON(text);

   alert(json); // Will show [object Object]

   var text = 'not valid json';

   var json = MauticJS.parseTextToJSON(text);

   alert(json); // Will show 'not valid json'

``MauticJS.insertScript(scriptUrl)``
====================================

This method inserts a script tag with the provided URL in the head of your document, before other scripts.

.. code-block:: js

   MauticJS.insertScript('http://google.com/ga.js');
