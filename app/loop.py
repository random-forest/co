from operator import *
from parser import *
from utils import *

def loop(state):
  while True:
    try:
      cmd = build_cmd(input(":> ").split(' '))
      rule = find_rule(cmd, state.get_the('commands'))
      src = find_script(rule, state)
    except (EOFError, KeyboardInterrupt):
      quit()
