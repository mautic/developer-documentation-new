==============
Best practices
==============

When creating plugins for Mautic, there's a few best practices which are highly recommend:

1. The Marketplace links to the GitHub repository. Make sure you have all the information your users need in the README.md file.
2. The GitHub repository should have issues enabled, so that your users are able to report issues and search for solutions. There is direct link to GitHub issues in the Marketplace.
3. Use GitHub releases. Tag every new version.
4. Write down changelog to all the GitHub releases. Again, the Marketplace links to all of them. Keep your users informed about what has changed in each version.
5. Write automatic unit and functional tests and run them automatically with a CI like `GitHub Actions <https://github.com/features/actions>`_. The effort you put into stability helps to catch bugs before they land with the users.
6. Take an advantage of releasing alpha and beta versions when working on big changes. Example beta version: ``1.2.0-beta``.
7. Use `semantic versioning <https://semver.org>`_ starting with 1.0. Don't tie your plugin version with Mautic's version. The require section in `composer.json` specifies which Mautic versions your Plugin supports.
