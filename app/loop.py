from parser import *
from utils import *

def loop(state):
  while True:
    try:
      args = input(":> ").split(' ')
      cmd  = build_cmd(args)
      rules = state.get_the('commands')

      echo(rules)

    except EOFError:
      quit()
    except KeyboardInterrupt:
      quit()
