from operator import *
from utils import *
#----------------------------------------------------------------------------
def Co():
  class Wrapper(object):
    def __init__(self, *args, **kwargs):
      self.pool = []
      self.commands = []
      self.fns = []

    def get_the(self, name):
    	return getattr(self, name)

    def add_to(self, name, value):
    	return getattr(self, name).append(value)

    def drop_the(self, name):
    	return getattr(self, name).clear()

  return Wrapper
#----------------------------------------------------------------------------

@Co()
def _():
  pass


