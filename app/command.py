from toolz.itertoolz import merge_sorted
from utils import *

POOL = []

def command(name, help_='Default help message'):
  class Wrapper(object):
    def __init__(self, *args, **kwargs):
      self.name = name
      self.help = help_
      self.options = []

      self.__call__()

    def __call__(self, *args, **kwargs):
      POOL.pop()
      setattr(self, 'options', list(merge_sorted(self.options, POOL)))

      return vars(self)

  return Wrapper

class option(object):
  def __init__(self, name, help_='Default help message'):
    self.name = name
    self.help = help_

  def __call__(self, func):
    POOL.append(vars(self))

    return vars(self)
