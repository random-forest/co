from app import _
from toolz.itertoolz import merge_sorted
from utils import *
#----------------------------------------------------------------------------
class command(object):
  def __init__(self, name, help_='Default help message', *args, **kwargs):
    self.name = name
    self.help = help_
    self.options = []

  def __call__(self, func, *args, **kwargs):
    if _.get_the('options') == []:
      setattr(self, 'options', None)
    else:
      setattr(self, 'options', list(merge_sorted(self.options, _.get_the('options'))))

    if is_Function(func):
      _.add_to('fns', func)

    _.add_to('commands', vars(self))
    _.drop_the('options')

    return vars(self)
#----------------------------------------------------------------------------
class option(object):
  def __init__(self, name, help_=None, *args, **kwargs):
    self.name = name
    self.help = help_

  def __call__(self, func):
    if is_Function(func):
      _.add_to('fns', func)

    _.add_to('options', vars(self))
