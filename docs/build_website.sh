#!/bin/bash -v
#
# move the ipynb files into the doc_notebooks folder
#
mkdir -p ./pdfs
rsync -avz ./pdfs _build/pdfs
rsync -avz ../notebooks/* doc_notebooks/
#
# build the website
#
sphinx-build -N -v -b html . _build


