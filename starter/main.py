#!/usr/bin/env python

def hello(name: str='Starter') -> str:
  """Test function that prints hello world

  :param name: name to be displayed, defaults to 'Starter'
  :type name: str, optional
  :return: hello world string
  :rtype: str
  """
  return f'Hello World! from {name}'

if __name__=='__main__':
  pass