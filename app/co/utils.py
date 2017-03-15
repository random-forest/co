from operator import *
from pprint import pprint
from toolz import diff
from toolz import filter
from types import FunctionType

def get_val(val):
  return val
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
def is_Empty(arr):
  return eq(arr, [])
# ----------------------------------------------------------------------------
def compact(iter):
  return filter(None, iter)
# ----------------------------------------------------------------------------
def areidentical(*seqs):
  return not any(diff(*seqs, default=object()))
# ----------------------------------------------------------------------------
def hasattr(a, b):
  return a.__contains__(b)
# ----------------------------------------------------------------------------
def cond(a, b):
  if a is not b:
    return a
  else:
    return False
