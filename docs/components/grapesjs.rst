GrapesJS Builder
========================================

Currently, Mautic uses the GrapesJS Builder for Emails and Landing pages. 

Setup 
-----------------------------------
.. code-block:: BASH

    npm install


Configure babel, eslint, prettier
-----------------------------------

Use the template files provided. For example .eslintrc.temp

**How to test standalone**

.. code-block:: BASH

    npm run start-helloWorld
    or
    npm run start-mautic

In order for start-mautic to work a running ddev container has to be present. 
If you are on some other development environment you need to update some paths in Demo/mautic/index.html

**How to build for production**

.. code-block:: BASH

    npm run build


Code architecture
-----------------------------------

There is PHP and the JavaScript code.

All the JavaScript code lives in the Assets/library folder. This handles the UI of the builder.

In addition to the code in this repo there is also the [Mautic preset](https://github.com/mautic/grapesjs-preset-mautic). 
This repo handles the basic Mautic specific code. The general idea is that this preset repo can be used as a base for various Mautic builder plugins. 
E.g one where the RTE editor is the CKEditor, or where we've some very customer or industry specific features.

```
- It's a pack of configurable feautures:
- Adds the function to edit source code
- Extends the original image and add a confirm dialog before removing it
- Add the option to hide/show the Layers Manager
- Add the option to enable/disable the import code button
- Moves the Settings panel inside Style Manager panel
- Opens the Block Manager at launch
- Add Dynamic Content Block for HTML used in Mautic
```

Issues
-----------------------------------
Issues are reported in the main Mautic repository and are labelded with [https://github.com/mautic/mautic/issues?q=is%3Aopen+is%3Aissue+label%3Abuilder-grapesjs](builder-grapesjs)

PRs
-----------------------------------
PRs are done to the main [Mautic repo](https://github.com/mautic/mautic/pulls)