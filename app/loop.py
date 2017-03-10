from parser import *
from utils import *

def loop(state):
  while True:
    try:
      args = input(":> ").split(' ')
      cmd  = build_cmd(args)
      echo(vars(state))
    except EOFError:
      quit()
    except KeyboardInterrupt:
      quit()
