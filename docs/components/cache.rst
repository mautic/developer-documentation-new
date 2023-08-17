Cache
#####
Symfony makes heavy use of a filesystem cache. Frequently clearing this cache will be required when developing for Mautic. By default, the cache is located in app/cache/ENV where ENV is the environment currently accessed (i.e. dev or prod). To rebuild the cache, the ENV can just be deleted or run the Symfony command
