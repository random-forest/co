from functools import wraps
from operator import *
from pprint import pprint

# GET USER INPUT ARGUMENTS
def arguments(sep):
  def decorator(fn):
    @wraps(fn)
    def fn_wrapper(cursor):
      return fn(input(cursor).split(sep))
    return fn_wrapper
  return decorator

# BUILD COMMAND FROM CLI ARGUMENTS
def build(fn):
  def decorator(arr):
    name = arr[0]
    opts = arr[1:] if gt(len(arr), 1) else None
    res = dict(name=name, options=opts)

    if eq(getitem(res, 'options'), None):
      delitem(res, 'options')
      return fn(res)
    else:
      return fn(res)
  return decorator

# BUILD COMMAND
@arguments(' ')
@build
def user_cmd(res):
  return res


