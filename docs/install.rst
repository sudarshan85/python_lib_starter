Installation
============

There are two files in the repository that will help us setup a suitable
environment for our package with all the dependencies correctly
installed.

-  ``environment.yml``: This is a manually created environment file that
   will contain all the dependencies for the package that *can be*
   installed via ``conda``. It will also contain a contain that will
   install those dependencies that need to be installed via ``pip``
   through a requirements file
-  ``requirements_pip_only.txt``: This will contain all the dependencies
   that can not for some reason not be installed via ``conda``.
   Everything listed here will automatically be installed through
   ``pip`` when creating the Anaconda environment.

Please follow these steps to correctly setup the environment, install

1. Clone the repository to a local folder called ``starter`` and ``cd``
   into it.

2. Execute the following command:
   ``create env create -f environment.yml``. This will create an
   Anaconda environment called ``starter``.

3. Activate the environment: ``conda activate starter``