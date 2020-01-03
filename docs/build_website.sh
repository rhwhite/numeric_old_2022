#!/bin/bash -v
#
# move the ipynb files into the doc_notebooks folder
#
rsync -avz ../notebooks/* doc_notebooks/
#
# build the website
#
sphinx-build -N -v -b html . _build
