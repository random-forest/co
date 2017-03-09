from command import *
from operator import *
from utils import *

@command('help', help_='Example message')
@option(name='-l', help_='Option message')
@option(name='-a')
@option(name='-b')
def help_():
  """
  ---------------- -------- Help --------------------------------
  """
  pass

@command('build', help_='build [-es6, -jsx, -node] path')
@option(name='-es6', help_='Option message')
@option(name='-jsx')
@option(name='-node')
def build_(*argv, **kwargs):
  pass

