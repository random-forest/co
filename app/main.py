from app import _
from command import *
from loop import loop
from utils import *
#----------------------------------------------------------------------------
@command('quit', help_="Safe exit from application")
def quit_(*argv, **kwargs):
  quit()
#----------------------------------------------------------------------------
@command('help', help_='Example message')
def help_(*argv, **kwargs):
  print('------Help message-------')
#----------------------------------------------------------------------------
@command('build', help_='build [-es6, -jsx, -node] /a/b/c/')
@option(name='-es6')
@option(name='-jsx')
@option(name='-node')
def build_(*argv):
  print('BUILD FUNCTION')
  pass
#----------------------------------------------------------------------------
def main():
	loop(_)
#----------------------------------------------------------------------------
if __name__ == '__main__':
	main()
