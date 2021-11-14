[![Documentation Status][RTD badge URL]][RTD URL]

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/mautic/developer-documentation-new)

# Mautic developer documentation (new)TEST

This repository hosts the new developer documentation for Mautic on the [Read the Docs platform][ReadTheDocs]. Whenever a PR is merged, changes are deployed immediately to https://mautic-developer.readthedocs.io/

If you're looking for our legacy developer documentation, please go to https://developer.mautic.org/ or the [GitHub repository][Legacy dev docs].

## Migration of developer docs to Read the Docs

We aim to move all aspects of the developer documentation to Read the Docs (with the exception of the REST API documentation).
In the video below, [@dennisameling][dennisameling GH profile] explains how the documentation is currently structured and briefly touches upon current limitations we're running into.

For more background, our end goal, and to let us know if you want to help, please check out [this issue][New docs background and goals]. Thanks in advance!

[![Link to YouTube video with explanation of the current developer documentation structure][YouTube video image]][YouTube video URL]

## Build documentation locally

- [RST Syntax Cheatsheet][RST Cheatsheet]
- [Sphinx Demo][Sphinx Demo]
- [Sphinx Syntax][Sphinx Template]

The following provides instructions for how to build docs locally for visualization without pushing to the remote:

1. Install Python 3 for your OS if not already installed
2. Install Sphinx `pip install sphinx`
3. Install sphinx-rtd-theme `pip install sphinx-rtd-theme`
4. CD into the docs directory `cd [path to this repo]/docs`
5. Run `make html`
6. This will generate HTML in docs/build/html. Setup a web server with the web root as docs/build/html or open docs/build/html/index.html in a browser.
 
### Vale
Before pushing, run Vale and address suggestions and errors as applicable.
1. Install [`vale`][Vale] 
2. `vale .`

### PhpStorm/PyCharm File Watcher
You can automatically build changes to rst files using a file watcher. 
1. Go to Preferences -> Tools -> File Watchers -> + button -> custom
2. Configure the watcher as presented in the screenshot

<img width="753" alt="Screen Shot 2021-10-06 at 15 52 06" src="https://user-images.githubusercontent.com/63312/136281761-204861f9-340a-4e3e-8ce5-e0584236303c.png">


[ReadTheDocs]: <https://readthedocs.org>
[Legacy dev docs]: <https://github.com/mautic/developer-documentation>
[dennisameling GH profile]: <https://github.com/dennisameling>
[New docs background and goals]: <https://github.com/mautic/developer-documentation-new/issues/2>
[YouTube video image]: <https://img.youtube.com/vi/O3zXdKLznPQ/0.jpg>
[YouTube video URL]: <https://www.youtube.com/watch?v=O3zXdKLznPQ>
[RTD badge URL]: <https://readthedocs.org/projects/mautic-developer/badge/?version=latest>
[RTD URL]: <https://mautic-developer.readthedocs.io/en/latest/?badge=latest>
[RST Cheatsheet]: <https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst>
[Sphinx Template]: <https://github.com/readthedocs/sphinx_rtd_theme/tree/master/docs/demo>
[Sphinx Demo]: <https://sphinx-rtd-theme.readthedocs.io/en/stable/demo/structure.html>
[Vale]: <https://docs.errata.ai/vale/install>
