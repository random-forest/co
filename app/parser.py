from funcy import *
from operator import *
from toolz import *
from toolz import map

def build_cmd(cmd):
  length = len(cmd)
  keys = ['name', 'option', 'path']
  res = map(lambda key: key, cmd[0:])

  return zipdict(keys[0:], [next(res) for i in range(length)])
