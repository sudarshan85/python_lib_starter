#!/usr/bin/env python

import argparse

def hello(name: str) -> str:
  """Test function that prints hello world

  :param name: name to be displayed
  :type name: str, optional
  :return: hello world string
  :rtype: str
  """
  return f'Hello World! My name is {name}'

def parse_args() -> argparse.Namespace:
  """Argument parser function

  :return: parsed argument namespace
  :rtype: argparse.Namespace
  """
  parser = argparse.ArgumentParser(description="Console script to run starter", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument('-n', '--name', type=str, help='String to be displayed for hello world', default='Starter')
  return parser.parse_args()

def entry_point() -> None:
  """Main entry point for the program
  """
  args = parse_args()
  print(hello(args.name))
