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
