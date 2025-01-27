#!/usr/bin/env python
import os
import sys

# Add the project's source directory to sys.path
sys.path.insert(0, os.path.abspath('../src'))

# Project-specific imports (ensure toy_py_package is importable)
try:
    import toy_py_package
    version = toy_py_package.__version__
    release = toy_py_package.__version__
except ImportError:
    version = '0.1.0'
    release = '0.1.0'

# -- General Configuration --
project = 'toy_py_package'
copyright = "2025, Hui Tang"
author = "Hui Tang"

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme'
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = False

# -- HTML Output --
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
htmlhelp_basename = 'toy_py_packagedoc'

# -- LaTeX Output --
latex_elements = {}
latex_documents = [
    (master_doc, 'toy_py_package.tex',
     'toy_py_package Documentation',
     'Hui Tang', 'manual'),
]

# -- Manual Page Output --
man_pages = [
    (master_doc, 'toy_py_package',
     'toy_py_package Documentation',
     [author], 1)
]

# -- Texinfo Output --
texinfo_documents = [
    (master_doc, 'toy_py_package',
     'toy_py_package Documentation',
     author,
     'toy_py_package',
     'One line description of project.',
     'Miscellaneous'),
]