============================================
Allowlist: what is it and why do we need it?
============================================
 
Plugin development can be challenging. While we try to make plugin development for Mautic as easy and smooth as possible, there's always a risk that a plugin breaks Mautic entirely.
We are planning to build several safeguards into the Marketplace that should prevent Mautic from crashing when a plugin is installed, but we're not there yet. That's why we are introducing a so-called allowlist in Mautic 4.1, meaning that Mautic's core team will have to approve your plugin for it to show up in the Marketplace. This way, we hope to keep stability at a high level for all users of Mautic.

How does it work?
=================

The process roughly looks like this:

1. Plugin author fills out our `application form`_.
2. Mautic's core team will review the submission.
3. When the submission is accepted, the core team adds the plugin to the list at https://github.com/mautic/marketplace-allowlist.

Applying for the allowlist
==========================

As mentioned above, you can use our `application form`_ in order to be added to our allowlist. Once you do, we'll get back to you as soon as possible. In the meantime, you can keep an eye on the allowlist at https://github.com/mautic/marketplace-allowlist as we'll be updating it regularly.

Moving forward: roadmap
=======================

- November 2021: Release Mautic 4.1 with allowlist enabled for the Marketplace
- February 2022: Release Mautic 4.2 where we switch from allowlist to blocklist (all plugins allowed except the ones that we know are incompatible or have security issues)

.. _application form: https://mau.tc/marketplace-allowlist