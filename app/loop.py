from app import *
from funcy import *
from operator import *
from parser import *
from utils import *

def loop():
  while True:
    try:
      args = input(":> ").split(' ')
      cmd  = build_cmd(args)

      echo(cmd)
    except EOFError:
      quit()
    except KeyboardInterrupt:
      quit()
