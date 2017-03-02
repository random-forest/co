from operator import *
from pprint import pprint

class option_(object):
  def __init__(self, name, help, *args, **kwargs):
    self.name = name
    self.help_message = help

  def __call__(self, *args, **kwargs):
    return vars(self)

