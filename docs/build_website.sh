#!/bin/bash -v
#
# move the ipynb files into the doc_notebooks folder
#
mkdir -p _build/pdfs
rsync -avz ./pdfs/* _build/pdfs/.
rsync -avz ../notebooks/* doc_notebooks/
rsync -avz ../notebooks/miniproject1/pdfs/miniproject1.pdf _build/pdfs/
rsync -avz ../demonstrations/
#
# build the website
#
sphinx-build -N -v -b html . _build


