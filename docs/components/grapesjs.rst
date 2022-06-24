GrapesJS Builder
################

Currently, Mautic uses the GrapesJS Builder for Emails and Landing pages. 

Setup 
*****

.. code-block:: BASH

    npm install

.. vale off

Configure Babel, ESLint, Prettier
=================================

.. vale on

Use the template files provided. For example .eslintrc.temp

How to test standalone
**********************

.. code-block:: BASH

    npm run start-helloWorld
    or
    npm run start-mautic

In order for ``start-mautic`` to work, a running DDEV container has to be present. 

If you are using another development environment you need to update some paths in ``Demo/mautic/index.html``.

How to build for production
***************************

.. code-block:: BASH

    npm run build

Code architecture
*****************

There is PHP and the JavaScript code.

All the JavaScript code lives in the Assets/library folder. This handles the UI of the builder.

In addition to the code in this repository, there is also the :xref:`GrapesJS Preset`. 

This repository handles the basic Mautic specific code. The general idea is that this preset repository is a base for various Mautic builder Plugins. 

E.g one where the Rich Text Editor is CKEditor, or where there is some very customer or industry specific features.

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
******

Report issues in the main Mautic repository, labelled as :xref:`GrapesJS builder issues`

PRs
***

Contributions to improve the GrapesJS Plugin happen in the main Mautic repository as :xref:`Github PRs`