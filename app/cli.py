from operator import *
from pprint import pprint
from utils import user_cmd

class Cli(object):
  def __init__(self):
    self.cmds_stack = []

  def command(self, name):
    """ NEW COMMAND """
    def d_(res):
      fn   = getitem(res, 0) if eq(type(res), tuple) else res
      opts = getitem(res, 1) if eq(type(res), tuple) else None
      src  = getitem(res, 2) if eq(type(res), tuple) else fn.__name__

      rr = dict(names=name, options=opts, source=src)

      if eq(opts, None):
        delitem(rr, 'options')

      self.cmds_stack.append(rr)
      return fn(rr)
    return d_

  def options(self, options):
    """ NEW COMMAND OPTIONS """
    def d_(fn, *args, **kwargs):
      return fn, options, fn.__name__
    return d_

  def loop(self):
    """ APPLICATION LOOP """
    while True:
      raw = user_cmd(':> ')
      pprint(raw)
cli_ = Cli()

