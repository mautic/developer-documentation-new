Update Plugins for Mautic 8
###########################

Mautic 8 adds native PHP return type declarations to the public methods on its repository classes, and a :xref:`phpstan` rule now enforces this across Mautic's repositories. There's no runtime behavior change - the declared return types match what the methods already returned.

If your Plugin or Integration subclasses a Mautic repository and overrides one of these methods without declaring the same return type, PHP raises a fatal error when it loads your class.

.. note::

   When you override a repository method, copy the parent's return type exactly.

.. vale off

CommonRepository
****************

.. vale on

Many of Mautic's repositories extend ``Mautic\CoreBundle\Entity\CommonRepository``, so its newly typed public methods have the widest impact. These signatures gain native return types:

.. code:: diff

   - public function checkUniqueAlias($alias, $entity = null)
   + public function checkUniqueAlias($alias, $entity = null): int
   - public function findOneBySlugs($alias, $catAlias = null, $lang = null)
   + public function findOneBySlugs($alias, $catAlias = null, $lang = null): ?object
   - public function getBaseColumns($entityClass, bool $returnColumnNames = false)
   + public function getBaseColumns($entityClass, bool $returnColumnNames = false): array
   - public function getEntities(array $args = [])
   + public function getEntities(array $args = []): iterable
   - public function getValue($id, $column)
   + public function getValue($id, $column): mixed
   - public function getTableName()
   + public function getTableName(): string

For an example of extending a repository in a Plugin, see :doc:`/plugin_extensions/contacts`.

A compliant override repeats the parent's return type:

.. code:: php

   public function getEntities(array $args = []): iterable
   {
       return parent::getEntities($args);
   }

Other repositories
******************

Concrete repositories across Mautic core also gain native return types on their public methods, so a Plugin that overrides a public method on any core repository must declare the matching return type.

Find affected overrides
***********************

Run :xref:`phpstan` against your Plugin on Mautic 8 before you ship. It flags every override whose return type no longer matches its parent, so you can fix them before a fatal error reaches production.
