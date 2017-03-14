from funcy import *
from operator import *
from toolz import *
from utils import *

def build_cmd(cmd):
  length = len(cmd)
  keys = ['name', 'option', 'path']
  res = map(lambda key: key, cmd[0:])

  return zipdict(keys[0:], [next(res) for i in range(length)])

def check_values(a, b):
  return areidentical(a, b)
