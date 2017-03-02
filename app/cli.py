from command import *
from operator import *
from pprint import pprint

class Cli(object):
  def __init__(self, cursor):
    self.cursor = cursor

  def loop(self):
    while True:
      try:
        args   = input(self.cursor).split(' ')
        cmd    = '%s_' % getitem(args, 0)
        source = self.__getattribute__(cmd)

        if type(source) == str:
          print(source)
        else:
          return source
      except KeyboardInterrupt:
        return self.quit_
      except EOFError:
        return self.quit_

  @command_('help')
  def help_():
    """
                                      Help
      1. help --> Show this message;
      2. quit --> Exit application;
      3. build [ -es6, -jsx, -node ] [ /path/to/dir ] --> Create application;
    """
    pass

  @command_('quit')
  def quit_():
    return SystemExit(1)

  @command_('build')
  @option_(name='-es6',  help='Example --> "build -es6 [ /path/to/dir/ ]";')
  def build_():
    pass

cli_ = Cli(':> ')

















































# from utils import user_cmd

# class Cli(object):
#   def __init__(self):
#     self.cmds_stack = []

#   def command(self, name):
#     """ NEW COMMAND """
#     def d_(res):
#       fn   = getitem(res, 0) if eq(type(res), tuple) else res
#       opts = getitem(res, 1) if eq(type(res), tuple) else None
#       src  = getitem(res, 2) if eq(type(res), tuple) else fn.__name__

#       rr = dict(names=name, options=opts, source=src)

#       if eq(opts, None):
#         delitem(rr, 'options')

#       self.cmds_stack.append(rr)
#       return fn(rr)
#     return d_

#   def options(self, options):
#     """ NEW COMMAND OPTIONS """
#     def d_(fn, *args, **kwargs):
#       return fn, options, fn.__name__
#     return d_

#   def loop(self):
#     """ APPLICATION LOOP """
#     while True:
#       raw = user_cmd(':> ')


# cli_ = Cli()

