============================================
Allowlist: what is it and why is it needed?
============================================
 
Plugin development can be challenging. Mautic tries to make plugin development as easy and smooth as possible, but there's always a risk that a Plugin breaks Mautic entirely.
There are plans to build several safeguards into the Marketplace which should prevent Mautic from crashing when a Plugin is installed, however this is currently a work in progress. That's why there is a so-called `allowlist` in Mautic 4.1, meaning that Mautic's core team will have to approve your Plugin for it to show up in the Marketplace. This way, it is hoped that this ensures stability for all users of Mautic.

How does it work?
=================

The process roughly looks like this:

1. Plugin author fills out the `application form`_.
2. Mautic's core team reviews the submission.
3. Once accepted, the core team adds the Plugin to the list at https://github.com/mautic/marketplace-allowlist.

Applying for the allowlist
==========================

As mentioned, you can use the `application form`_ which is reviewed by the core team. Once reviewed, an update is sent by email to the address provided. In the meantime, you can keep an eye on the allowlist at https://github.com/mautic/marketplace-allowlist as it is updated regularly.

Moving forward: roadmap
=======================

- November 2021: Release Mautic 4.1 with allowlist enabled for the Marketplace
- February 2022: Release Mautic 4.2 which may switch from allowlist to blocklist (all plugins allowed except the ones that we know are incompatible or have security issues)

.. _application form: https://mau.tc/marketplace-allowlist