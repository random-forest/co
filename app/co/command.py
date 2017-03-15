from co.proxy import co
from co.utils import *
from toolz.itertoolz import merge_sorted

#----------------------------------------------------------------------------
class command(object):
  def __init__(self, name, help_='Default test message', *args, **kwargs):
    self.name = name
    self.help = help_
    self.options = []

  def __call__(self, func, *args, **kwargs):
    if co.get_the('options') == []:
      setattr(self, 'options', None)
    else:
      setattr(self, 'options', list(merge_sorted(self.options, co.get_the('options'))))

    if is_Function(func):
      co.add_to('fns', func)

      if func.__name__ == 'init_':
        print(func.__doc__)

    co.add_to('commands', vars(self))
    co.drop_the('options')

    return vars(self)
#----------------------------------------------------------------------------
class option(object):
  def __init__(self, name, help_=None, *args, **kwargs):
    self.name = name
    self.help = help_

  def __call__(self, func):
    if is_Function(func):
      co.add_to('fns', func)

    co.add_to('options', vars(self))

# __package__ = 'command'
