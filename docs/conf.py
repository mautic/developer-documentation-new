# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import sys, os
import sphinx_rtd_theme

sys.path.append(os.path.abspath('ext'))
sys.path.append('.')

from links.link import *
from links import *

# We get code samples directly from GitHub. For more info, see the README.md file of this repo.

from code_samples._main_code_sample import *
from code_samples import *

# -- Project information -----------------------------------------------------

project = 'Mautic Developer Documentation'
copyright = '2021, Mautic contributors'
author = 'Mautic contributors'

# The full version, including alpha/beta/rc tags
release = '3.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
   'xref',
   'phpdomain',
   'code_samples_ext',
   'sphinx_rtd_theme',
   'sphinx.ext.viewcode',
   'sphinx.ext.autosectionlabel',
]

# Add any paths that contain templates here, relative to this directory.
#html_theme_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

templates_path = ['_templates']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Please add links here that do not pass the "make checklinks" check.
# A little context on the reason for ignoring is greatly appreciated!
linkcheck_ignore = [
   # Incorrectly reported as 'Anchor "webhooks" not found' so ignoring this
   'https://docs.mautic.org/en/setup/cron-jobs#webhooks'
]

linkcheck_anchors_ignore_for_url = [
  # github anchors cause failures in make checklinks check
  'https://github.com/mautic/mautic/.*'
]
