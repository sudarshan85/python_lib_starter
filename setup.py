#!/usr/bin/env python

from setuptools import setup, find_packages
import starter

setup(
  name='starter',
  version=starter.__version__,
  packages=find_packages(include=['starter', 'starter.*'])
)