from operator import *
from option import option_
from pprint import pprint
from types import FunctionType

class command_(object):
  def __init__(self, name):
    self.name = name
    self.options = []

  def __call__(self, fn, *args, **kwargs):
    if eq(isinstance(fn, FunctionType), True):
      if fn.__doc__ != None:
        return fn.__doc__
      else:
        return fn
    else:
      self.options.append(fn)


