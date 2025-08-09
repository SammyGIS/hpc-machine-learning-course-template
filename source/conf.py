# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'HPC Machine Learning Course'
copyright = '2025, Sahar Mahdie'
author = 'Sahar Mahdie'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'nbsphinx',
    "sphinx_lesson",
    "sphinx.ext.githubpages",
    "sphinx_rtd_theme_ext_color_contrast",
    "sphinxemoji.sphinxemoji",
    'sphinxcontrib.plantuml',
    'sphinx.ext.graphviz',
    'sphinxcontrib.mermaid',
    'sphinx_copybutton',
    'jupyter_sphinx',
    'sphinx_design'
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
