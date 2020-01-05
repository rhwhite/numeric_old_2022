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
#    anaconda installation to create the numeric environment.
#
# 2. clone the repo:
#
# ```
# git clone https://github.com/phaustin/numeric
# cd numeric
# ```
#
# 3. cd to the `course_utils` folder and create and activate the numeric environment
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
#
# ## Push the student notebooks to their download repo
#
# We have a separate repo to maintain the notebooks and libraries that the students will
# download:  https://github.com/phaustin/numeric_students
#
# This repository is a mirror of everything that is in our [students folder](https://github.com/phaustin/numeric/tree/master/students).  My workflow for deploying
# to this folder:
#
# 1. add a no-passphrase public key to the numeric_students repository (mine is named new_pha_git)
#
# 2. I put the following entry into my .ssh/config:
#
#         Host phaustin
#              HostName github.com
#              User git
#              IdentityFile ~/.ssh/new_pha_git
#              IdentitiesOnly yes
#              
# 3. Add the following remote to the main numeric repository
#
# ```
# git add remote students phaustin:phaustin/numeric_students
# ```
#
# 2. Now you can use ghp-import to push the students folder to that remote using [push_students.sh](https://github.com/phaustin/numeric/blob/master/scripts/push_students.sh)
#
# ```
# scripts/push_students.sh
# ```
#
# Note that I've removed the master branch from the repo and made "downloads" the default branch
# so we don't get confused.
#
# **Important point -- you can commit new notebooks to the student folder as part of a numeric branch, but push_students.sh makes a separate commit of every file in the folder and completely overwrites the remote
# branch for every push.  So treat everything on the remote branch as ephemeral.**
#
# # Student installs
#
# **If you already have conda or anaconda installed, skip to `Git install` below**
#
#
#
# ## For MacOS new installs
#
#
# 1. Download miniconda from  https://docs.conda.io/en/latest/miniconda.html  -- choose the `Miniconda3 MacOSX 64-bit pkg` file from the menu and run it, agreeing to the licences and accepting all defaults. You should install for "just me"
#
# 1. To test your installation, open a fresh terminal window and at the prompt type `which conda`.  You should see something resembling the following output, with your username instead of `phil`:
#
# ```
# % which conda
# /Users/phil/opt/miniconda3/bin/conda
# ```
#
# ## For Windows new installs
#
# 1. Download miniconda from  https://docs.conda.io/en/latest/miniconda.html  -- choose the `Miniconda3 Windows 64-bit`. download from the menu and run it, agreeing to the licences and accepting all defaults.
#
# The installer should suggest installing in a path that looks like:
#
# ```
# C:\Users\phil\Miniconda3
# ```
#
# 2. Once the install completes hit the windows key and start typing `anaconda`.  You should see a shortcut that looks like:
#
# ```
# Anaconda Powershell Prompt
# (Miniconda3)
# ```
#
# **Note that Windows comes with two different terminals `cmd` (old) and `powershell` (new).  Always select the powershell version of the anaconda terminal**
#
# 3. Select the short cut.  If the install was successful you should see something like:
#
# ```
# (base) (Miniconda3):Users/phil>
# ```
# with your username substituted for phil.
#
# ## Git install
#
# Inside your powershell or MacOs terminal, install git using conda:
#
# ```
# conda install git
# ```
#
# ## Setting up the course repository
#
# In the terminal, change directories to your home directory (called `~` for short) and make a new directory
# called `repos` to hold the course notebook repository.  Change into `repos` and clone the course:
#
# ```
# cd ~
# mkdir repos
# cd repos
# git clone https://github.com/phaustin/numeric_students.git
# ```
#
# ## Creating the course environment
#
# In the terminal, execute the following commands:
#
# ```
# cd numeric_students/utils
# conda env create -f numeric.yml
# conda activate numeric
# ```
#
# ## Opening the notebook folder
#
# ```
# cd ~/repos/numeric_students/numeric_notebooks
# jupyter notebook
# ```
#
