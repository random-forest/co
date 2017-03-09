from pprint import pprint
from types import FunctionType

def echo(*args):
  list(map(lambda i: pprint(i), args))

def is_Function(a):
  return type(a) is FunctionType

def call(*argv, **kwargs):
  def call_fn(fn):
    return fn(*argv, **kwargs)
  return call_fn
