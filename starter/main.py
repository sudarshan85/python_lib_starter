#!/usr/bin/env python

import argparse

def hello(name: str) -> str:
  """Test function that prints hello world

  :param name: name to be displayed
  :type name: str, optional
  :return: hello world string
  :rtype: str
  """
  return f'Hello World! from {name}'

def parse_args():
  parser = argparse.ArgumentParser(description="Console script to run starter", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument('-n', '--name', type=str, help='String to be displayed for hello world', default='Starter')
  return parser.parse_args()

def entry_point():
  args = parse_args()
  print(hello(args.name))
