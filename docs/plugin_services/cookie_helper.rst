Cookie helper
#############

.. vale off

The Cookie helper lets Plugins read request cookies and queue response cookies while reusing Mautic cookie defaults - path, domain, secure, and HTTP-only.

.. vale on

Using the helper
****************

Inject ``Mautic\CoreBundle\Helper\CookieHelper`` into your service, or retrieve it from the container in legacy code.

.. code-block:: php

   <?php

   use Mautic\CoreBundle\Helper\CookieHelper;

   final class ExampleService
   {
       public function __construct(private CookieHelper $cookieHelper)
       {
       }

       public function handleCookie(): void
       {
           // Set a cookie that expires in 1 hour (3600 seconds)
           $this->cookieHelper->setCookie('example_cookie', 'example_value', 3600);

           // Read a cookie value with fallback
           $value = $this->cookieHelper->getCookie('example_cookie', 'default_value');

           // Remove the cookie
           $this->cookieHelper->deleteCookie('example_cookie');
       }
   }

Cookie methods
**************

The helper exposes these main methods:

* ``getCookie(string $key, $default = null)``: reads a cookie from the current request.
* ``setCookie(string $name, $value, ?int $expire = 1800, ?string $path = null, ?string $domain = null, ?bool $secure = null, ?bool $httpOnly = null, ?string $sameSite = Cookie::SAMESITE_LAX)``: queues a cookie on the response.
* ``deleteCookie(string $name, ?string $path = null, ?string $domain = null, ?bool $secure = null, ?bool $httpOnly = null, ?string $sameSite = Cookie::SAMESITE_LAX)``: expires a cookie.

If you omit optional arguments in ``setCookie()`` and ``deleteCookie()``, Mautic uses configured defaults.

.. tip::

   Use ``Cookie::SAMESITE_STRICT`` or ``Cookie::SAMESITE_NONE`` when your Plugin requires explicit SameSite behavior.
