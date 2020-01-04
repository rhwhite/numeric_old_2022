.. toctree::
   :maxdepth: 1


Getting started 
---------------

#. Find the name of your home directory

   On windows:

   #. start a cmd shell by typing "cmd" in the windows search bar and executing the
      dos command prompt

   #. Note the location that is listed when you type

      echo %userprofile%

      in the command window

   On macs:

#. Start a terminal by typing terminal in spotlight

   #. Note the location that is listed when you type

      echo $HOME

#. Install Miniconda Python version 3.6 from https://conda.io/miniconda.html
   into a a folder called mini36 in your home directory.   When prompted, choose to install for just yourself, but make miniconda python the default python

#. To see if your installation is working, start a terminal and type

   where python  (on windows)

   or

   which python (on macs)

   You should see that mini36 python is the version that is found on your path

#. Install the git version control package (which we will learn more about later).  To do this, type

   conda install git

   at a prompt and answer yes to permit the install

#.  Clone the course software into a directory of your choosing.  Create a folder somewhere under your home directory and cd into that folder.  Then type the following at the prompt:

        git clone https://github.com/phaustin/numeric.git

#.  cd into the numeric folder and install the course software by typing (note single  minus sign in front of the e):

        pip install -e .

#.  cd into the numeric/utilities folder and install the required python packages by typing (note two minus signs in front of the file flag):

       conda install --file class_specs.txt

#.  If the packages have installed correctly then typing

       jupyter notebook

    at a prompt should launch jupyter.

    
Learning bash and git
---------------------

* The default shell on OSX is bash, which is taught in this set of lessons:  https://swcarpentry.github.io/shell-novice/

* if you are on Windows, you can get a bash shell by installing `msys2 <http://www.msys2.org/>`_

* A good place to go to learn git fundamentals is this lesson https://swcarpentry.github.io/git-novice/


Pulling changes from the github repository
------------------------------------------

When we commit changes to the master branch and push to our github repository, you'll need to
download those changes to keep current.  To do that:

1) open a shell
2) cd to the numeric repository
3) fetch the changes with::

     git fetch origin

4) make sure you aren't going to clobber any of your own files::

     git status

   you can ignore "untracked files", but pay attention to any files labeled "modified".  Those will be
   overwritten when you reset to our commit, so copy them to a new name or folder.

5) Finally, get to our commit with::

     git reset --hard origin/master

   If that worked, then printing the most recent log entry::

     git log -1

   should tell you the most recent commit message, and it should agree with what you see at our github repository.
     

Windows:  Combining bash utilities with the Windows cmd shell
-------------------------------------------------------------

I set my windows laptop up so that commands like ls, pwd, cat, etc. work from the standard windows shell.  To do this:

1) Install `msys2 <http://www.msys2.org/>`_ , which should create a new directory C:\\msys64

2) Below I'm assuming that you have created a folder like: c:\\Users\\phil\\bin to store your executable scripts.  On my installation my user directory c:\Users\phil is given by the
   %userprofile% environmental variable.  To check what it is on your machine, open a cmd shell
   and do::

     echo %userprofile%

3) Once you have created %userprofile%\\bin, you need to add it to your %path% environmental variable so that folder will be searched for scripts.  To do this, hit the windows key to get to the
   windows search bar and type::

     edit environ

   This should bring up a menu item that will take you to the control panel when you click it.  The
   My control panel entry looks like this:

   .. image:: doc_notebooks/screenshots/environ_good.png
                 :scale: 50

   Double click on the path entry to get the list of folders
   currently in your path.  My list looks like this (note
   I've install minconda python into a folder called num36)
                         
   .. image:: doc_notebooks/screenshots/path_good.png
                 :scale: 50

   You want to add the new directory::

    %userprofile%\bin

   to this list like I did.

4) Copy two files from you numeric repository to %userprofile%\\bin.  The files are:

   * `ncmd.cmd <https://github.com/phaustin/numeric/blob/master/utilities/ncmd.cmd>`_

   * `CmdInit.cmd <https://github.com/phaustin/numeric/blob/master/utilities/CmdInit.cmd>`_

5) If the above is working, then going to the windows search bar and typing::

     ncmd

   should bring up a new console with working bash commands.

6) I also recommend installation of the `clink <https://mridgers.github.io/clink/>`_ utility to get command line editing and keyboard shortcuts.
   
     
                         
Working with python modules
---------------------------

* A good tutorial on python modules:  https://www.tutorialspoint.com/python/python_modules.htm

* Summary: python can import functions, classes, data structures from files that end in .py, as long is it can find them.  A statement like::

    from numpy import arange

  tells python to look through the set of directories that are contained in set that are listed when you do::

   import sys
   print(sys.path)

  When you import the arange from numpy, it opens the file numpy.py and reads in the function arange.

  Similarly, if you have a file called mymodule.py than contains myfun, then, as long as it is in the directory that you are currently working in, python  will find it and read in myfun.  If you aren't sure what directory you are working in, you can execute::

   import os
   print(os.getcwd())

  to get the current working directory.

* Note that python will not reload a modified file unless you tell it to.  If you edit mymodule.py, then to see those changes take effect you need to do::

    from importlib import reload
    reload(mymodule)

  I often put a print statement in the module, like::

    print('try number 3')

  to make sure I'm getting the fresh version, and not a cached version.


* Importing vs. running a module

  It's common practice to include executable code in a python file that contains functions, so that the functions can be tested or run to show how they work.  To support this, python uses the "__name__ == "__main__" trick::

    def fun1(alpha):
        return 2*alpha

    if __name__ == "__main__":
        myvar=2
        print(fun1(myvar))

  If you write a file called mymoodule.py containing these lines, you should find that when you  import it from another module::

    from mymodule import fun1

  nothing will print.  This is because the variable __name__ is set to "mymodule".

  If instead you run the function from python::

    python mymodule.py

  you will get a printed result, because now __name__ is set to "__main__".


Demonstration code
------------------

1) using the new scipy initial value problem solver: `scipy_integrate.ipynb <https://github.com/phaustin/numeric/blob/master/demonstrations/scipy_integrate/scipy_lab4.ipynb>`_
   
2) debugging `lab5_funs.py <https://github.com/phaustin/numeric/blob/master/demonstrations/debug_demo/lab5_funs.py>`_ with pdb.set_trace()

3) Using multiple cores with `joblib_example.ipynb <https://github.com/phaustin/numeric/blob/master/demonstrations/joblib_parallel/joblib_example.ipynb>`_

4) Multicore data processing with `zarr and dask <https://github.com/phaustin/numeric/blob/master/demonstrations/dask_zarr_demo.ipynb>`_    

5) `Introduction to pandas <https://github.com/phaustin/numeric/blob/master/demonstrations/pandas.ipynb>`_
extracted from `Research computing in the Earth Sciences <https://rabernat.github.io/research_computing/>`_

6) Confused about ANOVA, T-tests and chi-squared statistics?   Check out `Statistical rethinking <http://xcelab.net/rm/statistical-rethinking/>`_  with R-code ported to python at the `Statistical rethinking github account <https://github.com/aloctavodia/Statistical-Rethinking-with-Python-and-PyMC3>`_

7) An excellent course in `computational statistics <http://people.duke.edu/~ccc14/sta-663-2017/>`_
   with this `github repository <https://github.com/cliburn/sta-663-2017>`_

8) Slightly out of date `guide to parallel python <http://scipy-cookbook.readthedocs.io/items/ParallelProgramming.html>`_

9) `numba_demo notebook <https://github.com/phaustin/numeric/blob/master/demonstrations/numba_demo.ipynb>`_   

Background links
________________

* `cpu clock speed progress has stalled <https://www.extremetech.com/wp-content/uploads/2015/04/CPU-Scaling.jpg>`_

* multiple cores are getting cheaper

  - `16 core box for $Can 1000  <https://www.newegg.com/Product/Product.aspx?Item=N82E16819113447>`_

* `HPC is dying, and MPI is killing it <https://www.dursi.ca/post/hpc-is-dying-and-mpi-is-killing-it.html>`_

* `C++ HPX <http://stellar.cct.lsu.edu/projects/hpx/>`_  
   
* `Threads vs. processes <https://stackoverflow.com/questions/200469/what-is-the-difference-between-a-process-and-a-thread>`_
  
Dan's suggestions
_________________


1. Saving model data in a convenient format to be post-processed later, e.g., hdf5, pkl, vtk or another binary format and using xarray or pandas or something to deal with the data effectively. Slicing multidimensional data.

2. A skeleton of the most basic model using classes, with classes like "solver" "timestepping", "grid?" ...  We sort of already have this in the daisyworld lab and other places.

3. speeding up code, starting from the slowest to the fastest, some examples of how to get faster results, with examples like, a nested for loops and lists, to faster operations using numpy library, to fast operations on one processor achieving near C speed through some mechanism, to using mpi4py to run code on multiple processors. Guidance on when each method is worthwhile and when it's a waste of time.


   
Books and tutorials
-------------------

- If you are new to python, I would recommend you go over the following ebook in detail:

  -  Jake Vanderplas' `Whirlwind tour of Python <https://github.com/jakevdp/WhirlwindTourOfPython/blob/f40b435dea823ad5f094d48d158cc8b8f282e9d5/Index.ipynb>`_ is available both as a set of notebooks which you can clone from github or as a free ebook: http://www.oreilly.com/programming/free/a-whirlwind-tour-of-python.csp

     - to get the notebooks do:

       git clone https://github.com/jakevdp/WhirlwindTourOfPython

- We will be referencing chapters from:
   
  - A Springer ebook from the UBC library:  `Numerical Python <https://login.ezproxy.library.ubc.ca/login?qurl=https%3a%2f%2flink.springer.com%2fopenurl%3fgenre%3dbook%26isbn%3d978-1-4842-0554-9>`_

    - with code on github:

      git clone https://github.com/jrjohansson/numerical-python-book-code
   
- Two other texts that are available as a set of notebooks you can clone with git:   

  - https://github.com/fangohr/introduction-to-python-for-computational-science-and-engineering   

  - https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/Index.ipynb
     
-  Our version of David Pine's Introduction to Python:  http://clouds.eos.ubc.ca/~phil/djpine_python/
   
- My favorite O'Reilly book is:

  - `Python for Data Analysis <http://shop.oreilly.com/product/0636920023784.do>`_

- Some other resources:

  - If you know Matlab, there is `Numpy for Maltab users <http://wiki.scipy.org/NumPy_for_Matlab_Users>`_

  - Here is a `python translation <http://nbviewer.jupyter.org/gist/phaustin/1af744215e51562d010b9f6a19c0724c>`_  by `Don MacMillen <http://blogs.siam.org/from-matlab-guide-to-ipython-notebook/>`_ of `Chapter 1 of his matlab guide <http://clouds.eos.ubc.ca/~phil/courses/atsc301/downloads_pw/matlab_guide_2nd.pdf>`_
        
  - `Python data structure cheat sheet <pdffiles/Python-data-manipulations.pdf>`_


  - `Numpy beginners guide <http://www.packtpub.com/numpy-mathematical-2e-beginners-guide/book>`_

  - `Learning Ipython <http://www.packtpub.com/learning-ipython-for-interactive-computing-and-data-visualization/book>`_

  - `The official Python tutorial <http://docs.python.org/tut/tut.html>`_

  - `Numpy cookbook <http://www.packtpub.com/numpy-for-python-cookbook/book>`_
  
  - A general computing introduction: `How to think like a computer scientist <http://www.openbookproject.net/thinkcs/python/english3e>`_ with an `interactive version <http://interactivepython.org/courselib/static/thinkcspy/index.html>`_

  - `Think Stats <http://greenteapress.com/wp/think-stats-2e/>`_

  - `Think Bayes <http://greenteapress.com/wp/think-bayes/>`_ 




