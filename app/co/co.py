from co.command import *
from co.parser import *
from co.proxy import co
from co.utils import *

def loop():
  while True:
    try:
      cmd = build_cmd(input(":> ").split(' '))
      rule = change_rule(cmd, co.get_the('commands'))
      src = run_command(rule, co)
    except (EOFError, KeyboardInterrupt):
      quit()

__package__ = 'co'


