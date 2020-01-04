# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     formats: ipynb,py:percent
#     notebook_metadata_filter: all,-language_info,-toc,-latex_envs
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.3.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Initial setup for instructors
#
# ## General workflow
#
#   * Always edit py files, treat the ipynb files as read only output storage
#   * If you  forget, you can sync with: `jupytext --sync thenotebook.py`
#   * or sync and execute: `jupytext --sync --execute thenotebook.py`
#
# To get familiar with how jupytext works, it would be good 
# to spend some time at https://jupytext.readthedocs.io/en/latest/?badge=latest
#
# The notes below show how to bootstrap a repository with notebooks only committed
# as python files.  That means that the first time through, we need to convert and
# execute the ipynb versions.  Subsequently, jupyter will handle this through
# the modified jupyter_notebook_config.py described below.
#
# ## installation
#
# 1. Install miniconda if you don't have it -- note that our environment
#    will be 100% conda-forge, so you don't want to use a large existing
#    anaconda installation to create the e213 environment.
#
# 2. clone the repo:
#
# ```
# git clone https://github.com/phaustin/numeric
# cd numeric
# ```
#
# 3. cd to the `course_utils` folder and create and activate the e213 environment
#
# ```
# cd course_utils
# conda env create -f numeric.yml
# conda activate numeric
# ```
#
# 4. Make sure you have a jupyter config folder
#
# ```
# jupyter notebook --generate-config
# ```
#
# This should put a `jupyter_notebook_config.py` file in your `~/.jupyter` folder
#
# 5. Replace the config with the one in conda_utils
#
# ```
# cp conda_utils/jupyter_notebook_config.py ~/.jupyter/.
# ```
#
# ## Building the notebooks
#
# We need to track three different flavors of notebook:
#
# a) Student versions
# b) Notebooks with solutions
# c) Documentation notebooks for website
#
# At the moment there are two sets, the student notebooks are in
# `numerics/notebooks` and the documentation notebooks
# are in `numeric/docs/docs_notebooks`
#
# To build from scratch, we need to convert the py files to ipynb files.
#
# To do this:
#
# 1. `cd numeric`
# 2. `python scripts/find_notebooks.py notebooks notebook_filelist.json --initial`
#
# This should create an ipynb file for every py file and a new json
# file calle `notebook_filelist.json`.  We need to execute
# these, at this point we can suppress all errors:
#
# `python scripts/jup_build.py exec-noerrors-nb notebook_filelist.json`
#
# Repeat this for the docs notebooks:
#
# ```
# python scripts/find_notebooks.py docs/doc_notebooks notebook_docs_filelist.json --initial
# python scripts/jup_build.py exec-noerrors-nb notebook_docs_filelist.json
# ```
#
# ## Making the course website
#
# The notebooks (ipynb) and any restructured text (rst) and markdown (md) files are assembled
# into a website using [nbsphinx](https://nbsphinx.readthedocs.io/en/0.5.0/).  To build and
# deploy with github-pages:
#
# 1. `cd numeric/docs`
# 2. `./build_website.sh`
#
#
# and push to github
#
#
# 1. `cd numeric/docs`
# 2. `./push_pages.sh`
#
#
# 1. Install miniconda for you architecture:  https://docs.conda.io/en/latest/miniconda.html
#
# ## For MacOS
#
# a. Start a terminal and type:
#
# ```
# conda install git
# ```
#
# b. cd to your home directory and make a folder called repos
#
# ```
# mkdir repos
# cd repos
# ```
#
# c. clone the course repository and cd into it
#
# ```
# git clone https://github.com/phaustin/numeric
# cd numeric
# ```
#
# e. cd to the course folder and create and activate the e213 environment
#
# ```
# cd conda
# conda env create -f numeric.yml
# conda activate numeric
# ```
#
# f. change back to the notebooks folder and start jupyter
#
# ```
# cd ../notebooks
# jupyter notebook
# ```
#
#
