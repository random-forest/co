from app import _
from command import *
from loop import loop
from utils import *
#----------------------------------------------------------------------------
@command('help', help_='Example message')
def help_():
  print('Help message')
  pass
#----------------------------------------------------------------------------
@command('build', help_='build [-es6, -jsx, -node] /a/b/c/')
@option(name='-es6')
@option(name='-jsx')
@option(name='-node')
def build_(*argv, **kwargs):
  pass
#----------------------------------------------------------------------------
@command('list')
@option(name='-a')
def list_(*argv, **kwargs):
  pass
#----------------------------------------------------------------------------
def main():
	loop(_)
#----------------------------------------------------------------------------
if __name__ == '__main__':
	main()
