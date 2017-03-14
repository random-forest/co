from app import _
from operator import *
from toolz.itertoolz import merge_sorted
from utils import *
#----------------------------------------------------------------------------
def command(name, help_='Default help message'):
  class Wrapper(object):
    def __init__(self, *args, **kwargs):
      self.name = name
      self.help = help_
      self.options = []

      self.__call__()

    def __call__(self, *args, **kwargs):
      setattr(self, 'options', list(merge_sorted(self.options, _.get_the('pool'))))

      _.add_to('commands', vars(self))
      _.drop_the('pool')

      return vars(self)
  return Wrapper
#----------------------------------------------------------------------------
class option(object):
  def __init__(self, name, help_=None, *args, **kwargs):
    self.name = name
    self.help = help_

  def __call__(self, func):
    if func is not None:
      _.add_to('fns', func)

    _.add_to('pool', vars(self))
