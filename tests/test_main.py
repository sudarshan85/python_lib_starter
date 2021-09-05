#!/usr/bin/env python

import pytest
from starter.main import *

def test_hello():
  assert hello('Snickers') == 'Hello World! My name is Snickers'