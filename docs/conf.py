import os
import sys

import pkg_resources
from datetime import datetime
import alabaster

sys.path.insert(0, os.path.abspath('../leaf'))


# -- Project information -----------------------------------------------------

project = "LEAF"
author = "Philipp Wiesner"
copyright = f"{datetime.now().year}, {author}"
# The short X.Y version
version = pkg_resources.get_distribution('leaf').version
# The full version, including alpha/beta/rc tags
release = version

html_theme_path = [alabaster.get_path()]

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "alabaster",
]
html_static_path = ["_static"]
html_theme_options = {
    "logo": "logo.svg",
    "logo_name": True,
    "logo_text_align": "center",
    "description": "Simulator for modeling energy consumption in cloud, fog and edge computing environments.",
    "github_user": "dos-group",
    "github_repo": "leaf",
    "github_banner": True,
    "github_button": True,
    #"travis_button": True,
    #"codecov_button": True,
    #"tidelift_url": "https://tidelift.com/subscription/pkg/pypi-fabric?utm_source=pypi-fabric&utm_medium=referral&utm_campaign=docs",
    #"analytics_id": "UA-18486793-1",
    "link": "#3782BE",
    "link_hover": "#3782BE",
    # Wide enough that 80-col code snippets aren't truncated on default font
    # settings (at least for bitprophet's Chrome-on-OSX-Yosemite setup)
    "page_width": "1024px",
}

html_theme = 'alabaster'

# Both the class’ and the __init__ method’s docstring are concatenated and inserted.
autoclass_content = "both"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of reference filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to reference directory, that match files and
# directories to ignore when looking for reference files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (reference start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'gcsfs.tex', 'gcsfs Documentation',
     'Othoz GmbH', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (reference start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'LEAF', 'LEAF Documentation', [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (reference start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'LEAF', 'LEAF Documentation', author, 'leaf', '-', 'Simulator'),
]
