Core
####

You can configure Mautic to use Read Replicas for the database. This is useful if you have a large database and want to offload the read queries to a separate database server. This is not a requirement for Mautic to function, but it can help with performance.

In order to use this feature you must have a separate database server that is configured to be a Read Replica of your main database server. You can use the same database name and user credentials for the Read Replica as you do for the main database server.

Inside your `app/config/local.php`, you need to add a new variable called `db_host_ro` and set it to the hostname of your Read Replica database server. For example:

    `db_host_ro = 'read-replica-db.example.com';`
