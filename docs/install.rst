Installation
============

There are two files in the repository that will help us setup a suitable
environment for our package with all the dependencies correctly
installed.

Environment Setup
-----------------

-  ``environment.yml``: This is a manually created environment file that
   will contain all the dependencies for the package that *can be*
   installed via ``conda``. It will also contain a contain that will
   install those dependencies that need to be installed via ``pip``
   through a requirements file
-  ``requirements_pip_only.txt``: This will contain all the dependencies
   that can not for some reason not be installed via ``conda``.
   Everything listed here will automatically be installed through
   ``pip`` when creating the Anaconda environment.

Please follow these steps to correctly setup the environment:

1. Clone the repository to a local folder called ``python_lib_starter`` and ``cd``
   into it.
2. Execute the following command:
   ``create env create -f environment.yml``. This will create an
   Anaconda environment called ``starter``.
3. Activate the environment: ``conda activate starter``

Package Installation
--------------------

Package installation involves installing the package and running the
tests. These can either be done using the ``Makefile`` or by typing
individual commands.

1. ``make install`` or ``pip install -e .`` installs an *editable*
   version of the package in the current Anaconda environment. An
   editable version implies that any changes that is done to the modules
   is automatically reflected without the need for re-installation.
2. ``make test`` or
   ``python -m pytest -v --disable-pytest-warnings -rsx`` will run the
   Python tests inside in the ``tests`` folder using ``pytest`` and
   display the results of testing.

Package Documentation
---------------------

Documentation is done using Sphinx. In particular, all documentation is
written in reStructured (or rst) files. We use ``autodoc`` to
automatically create documentation for modules and classes by parsing
the associated ``docstrings``.

The following commands builds the documentation in the ``docs`` folder:

1. ``rm -rf docs/_build``: Remove previously built docs
2. ``sphinx-apidoc -fo docs starter``: Build the module documentation
   using ``autodoc`` from Python docstrings
3. ``sphinx-build -b html docs docs/_build``: Build the Sphinx
   documentation

Once the documentation is built, we can ``cd`` to ``docs/_build`` and
launch the ``index.html`` page in a browser. From there we can navigate
to the pages we want in the documentation.

All of these steps can be done by using the ``make docs`` command in the
package folder.

Finally, typing ``make all`` does the install, testing, and building
docs all at once.
