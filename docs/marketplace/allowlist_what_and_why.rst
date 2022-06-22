Allowlist: what is it and why is it needed?
===========================================
 
Plugin development can be challenging. Mautic tries to make Plugin development as easy and smooth as possible, but there's always a risk that a Plugin breaks Mautic entirely.
There are plans to build several safeguards into the Marketplace which should prevent Mautic from crashing when installing a Plugin, however this is currently a work in progress. That's why there is a so-called ``allowlist`` in Mautic 4.1, meaning that Mautic's core team has to approve your Plugin for it to show up in the Marketplace. This should ensure a higher level of stability for all users of Mautic.

How does it work?
=================

The process roughly looks like this:

1. Plugin author fills out the :xref:`Marketplace allowlist application form`.
2. Mautic's core team reviews the submission.
3. Once accepted, the core team adds the Plugin to the list at https://github.com/mautic/marketplace-allowlist.

Applying for the allowlist
==========================

As mentioned, you can use the :xref:`Marketplace allowlist application form` which gets reviewed by the core team. Once reviewed, the requester receives an update by email. In the meantime, you can keep an eye on the allowlist at https://github.com/mautic/marketplace-allowlist to track the latest updates.

Moving forward: roadmap
=======================

- November 2021: release Mautic 4.1 with allowlist enabled for the Marketplace
- February 2022: release Mautic 4.2 which may switch from allowlist to blocklist - all plugins allowed except the ones that are incompatible or have security issues

