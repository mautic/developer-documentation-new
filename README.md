[![Documentation Status][RTD badge URL]][RTD URL]
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/mautic/developer-documentation-new)

# Mautic developer documentation - new

This repository hosts the new developer documentation for Mautic on the [Read the Docs platform][ReadTheDocs]. Merging a PR results in immediate build and deployment to https://mautic-developer.readthedocs.io/

If you're looking for the legacy developer documentation, please go to https://developer.mautic.org/ or the [GitHub repository][Legacy dev docs].

## Migration of developer docs to Read the Docs

The aim is to move all aspects of the developer documentation to Read the Docs.
In the video below, [@dennisameling][dennisameling GH profile] explains how the documentation is currently structured and briefly touches upon current limitations.

For more background, the end goal, and reaching out if you want to help, please review [this issue][New docs background and goals]. Thanks in advance.

[![Link to YouTube video with explanation of the current developer documentation structure][YouTube video image]][YouTube video URL]

## Adding a code sample

Code samples get downloaded from GitHub to ensure that they're always up to date. If you want to add a new code sample, follow these two steps:

1. Create a file in `docs/code_samples/` and add a permalink in there. Look at other files in that directory for examples. URLs should always start with `https://raw.githubusercontent.com/...` to ensure that Sphinx can download the file correctly.
2. In any documentation file, add a `literalinclude` block to include the code, like so:

```
.. The link to this file is defined in docs/code_samples/helloworld_entity_world.py 
.. literalinclude:: ../code_samples_downloaded/Entity_World.php
    :language: php
```

Tip: downloaded files get cached in `docs/code_samples_downloaded` to prevent overloading GitHub with download requests. If you change the URL to a file, simply remove the cached file from `docs/code_samples_downloaded` and Sphinx automatically re-downloads it.

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
6. This generates HTML in docs/build/html. Setup a web server with the web root as docs/build/html or open docs/build/html/index.html in a browser.

## Troubleshooting

If the build isn't working for some reason, here's some tips:

- Try running the `make html` command in the terminal: `cd docs && make html`. This command normally provides a lot of additional context.
- If the preview isn't working, click the `esbonio` section in the bottom right corner of the VS Code window. That rebuilds the docs and previews, and tells you if something is wrong.

### Vale
Before pushing, run Vale and address suggestions and errors as applicable.
1. Install [`vale`][Vale] 
2. `vale .`

### PhpStorm/PyCharm File Watcher
You can automatically build changes to .rst files using a file watcher. 
1. Go to Preferences -> Tools -> File Watchers -> + button -> custom
2. Configure the watcher as presented in the screenshot

<img width="753" alt="Screen Shot 2021-10-06 at 15 52 06" src="https://user-images.githubusercontent.com/63312/136281761-204861f9-340a-4e3e-8ce5-e0584236303c.png">

### Style guide

Please consult Mautic's [`style-guide`][Style guide] before contributing to the documentation. Some rules get enforced through Vale.

As a quick reference, here's the list of headings Mautic uses:

```
H1: ############
H2: ****************
H3: ============
H4: ----------------
H5: ~~~~~~~~~~~~
```

 <!-- vale off -->

### Converting markdown to reStructuredText

 <!-- vale on -->

Mautic's documentation uses ``reStructuredText``, or ``.rst`` files. Luckily, there's converters available that help you convert ``.md`` to ``.rst`` files. Here's an example of ``m2r`` - this converter also converts tables into ``list-table`` directives properly.

```
pip install m2r
# This creates a new file with the .rst extension:
m2r my_markdown_file.md
```

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
[Style Guide]: <https://contribute.mautic.org/education-team/technical-writing-styleguide>
## Contributors ✨
<!-- vale off -->
Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://robert-parker.me"><img src="https://avatars.githubusercontent.com/u/25473863?v=4?s=100" width="100px;" alt="Robert Parker"/><br /><sub><b>Robert Parker</b></sub></a><br /><a href="https://github.com/mautic/developer-documentation-new/commits?author=diaboloshogunate" title="Documentation">📖</a></td>
      <td align="center"><a href="https://github.com/shinde-rahul"><img src="https://avatars.githubusercontent.com/u/1046788?v=4?s=100" width="100px;" alt="Rahul Shinde"/><br /><sub><b>Rahul Shinde</b></sub></a><br /><a href="https://github.com/mautic/developer-documentation-new/commits?author=shinde-rahul" title="Documentation">📖</a></td>
      <td align="center"><a href="https://dennisameling.com"><img src="https://avatars.githubusercontent.com/u/17739158?v=4?s=100" width="100px;" alt="Dennis Ameling"/><br /><sub><b>Dennis Ameling</b></sub></a><br /><a href="https://github.com/mautic/developer-documentation-new/commits?author=dennisameling" title="Documentation">📖</a> <a href="https://github.com/mautic/developer-documentation-new/pulls?q=is%3Apr+reviewed-by%3Adennisameling" title="Reviewed Pull Requests">👀</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
<!-- vale on -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome.