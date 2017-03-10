from pprint import pprint
from toolz import diff
from toolz import filter
from types import FunctionType
# ----------------------------------------------------------------------------

def echo(*args):
  list(map(lambda i: pprint(i), args))
# ----------------------------------------------------------------------------

def is_Function(a):
  return type(a) is FunctionType
# ----------------------------------------------------------------------------

def call(*argv, **kwargs):
  def call_fn(fn):
    return fn(*argv, **kwargs)
  return call_fn
# ----------------------------------------------------------------------------

def compact(iter):
  return filter(None, iter)
# ----------------------------------------------------------------------------

def areidentical(*seqs):
  return not any(diff(*seqs, default=object()))
