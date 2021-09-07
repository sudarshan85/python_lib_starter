# Python Library Starter Template

This is a Python package template that includes creating the module with
`setup.py`, creating an Ananconda environment, introductory docs with
Sphinx, and testing module with `pytest`.

## Usage

### Package Usage

The recommended way to use this package to jumpstart your Python library
development is as follows:

1.  Download (not clone) this repository and unpack it to a local
    folder.
2.  Rename the `starter` module with the name of your library.
3.  Replace references to `starter` in `README.md`, `environment.yml`,
    `setup.py`, `tests/test_main.py`, `main.py`, `Makefile`, and
    `docs/conf.py`.
4.  Replace `startit` in `setup.py` to the name of your library.
5.  Rename `starter.rst` to your library name (with `.rst` as
    extenstion) and replace `starter` with the name of your libarry.
6.  Replace references to `starter` in `modules.rst`, `install.rst` and
    other `rst` files with your library name that you just renamed.
7.  Populate `index.rst` with the documentation about your library.
8.  Delete `usage.rst` and remove its reference in index.rst.
9.  Follow the installation instructions below.

### Module Usage

In `setup.py` we have set `entry_points` with `startit` as the command
point to the `entry_point` function in `main.py`. To make sure the
package works, after installing the package, you can run
`startit -n Code`. This will return **Hello World! My name is Code**.
Once you've replaced `startit` with the name of your library, you can
use that to launch the code. From there you can develop your package as
you want.

## Installation

There are two files in the repository that will help us setup a suitable
environment for our package with all the dependencies correctly
installed.

### Environment Setup

-   `environment.yml`: This is a manually created environment file that
    will contain all the dependencies for the package that *can be*
    installed via `conda`. It will also contain a contain that will
    install those dependencies that need to be installed via `pip`
    through a requirements file
-   `requirements_pip_only.txt`: This will contain all the dependencies
    that can not for some reason not be installed via `conda`.
    Everything listed here will automatically be installed through `pip`
    when creating the Anaconda environment.

Please follow these steps to correctly setup the environment:

1.  Clone the repository to a local folder called `python_lib_starter` and `cd`
    into it.
2.  Execute the following command:
    `create env create -f environment.yml`. This will create an Anaconda
    environment called `starter`.
3.  Activate the environment: `conda activate starter`

### Package Installation

Package installation involves installing the package and running the
tests. These can either be done using the `Makefile` or by typing
individual commands.

1.  `make install` or `pip install -e .` installs an *editable* version
    of the package in the current Anaconda environment. An editable
    version implies that any changes that is done to the modules is
    automatically reflected without the need for re-installation.
2.  `make test` or `python -m pytest -v --disable-pytest-warnings -rsx`
    will run the Python tests inside in the `tests` folder using
    `pytest` and display the results of testing.

### Package Documentation

Documentation is done using Sphinx. In particular, all documentation is
written in reStructured (or rst) files. We use `autodoc` to
automatically create documentation for modules and classes by parsing
the associated `docstrings`.

The following commands builds the documentation in the `docs` folder:

1.  `rm -rf docs/_build`: Remove previously built docs
2.  `sphinx-apidoc -fo docs starter`: Build the module documentation
    using `autodoc` from Python docstrings
3.  `sphinx-build -b html docs docs/_build`: Build the Sphinx
    documentation

Once the documentation is built, we can `cd` to `docs/_build` and launch
the `index.html` page in a browser. From there we can navigate to the
pages we want in the documentation.

All of these steps can be done by using the `make docs` command in the
package folder. Finally, typing `make all` does the install, testing, and building docs
all at once.

For instructions on how to use this package to jumpstart your library development, please
check `docs/usage.rst` or go to the documentation page and check *Usage*.
