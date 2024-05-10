import sys
import sphinx_rtd_theme

project = 'Transition'
copyright = '2024, altmattr'
author = 'altmattr'
extensions = ["myst_parser"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
master_doc = 'index'

pygments_style = 'sphinx'
todo_include_todos = True

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_show_sphinx = False