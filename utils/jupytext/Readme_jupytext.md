# jupytext howto

* https://github.com/mwouts/jupytext

  `conda install  -c conda-forge jupytext`

* to move from a notebook to a py file:

   jupytext --to py:percent *ipynb

* to move from a py file to a notebook

  jupytext --to notebook *py  --sync --execute

* to copy change in a py file automatically to the ipynb
  partner while editing in jupyter:



  
