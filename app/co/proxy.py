def Co():
  class Wrapper(object):
    def __init__(self, *args, **kwargs):
      self.options = []
      self.commands = []
      self.fns = []

    def get_the(self, name):
      return getattr(self, name)

    def add_to(self, name, value):
      return getattr(self, name).append(value)

    def drop_the(self, name):
      return getattr(self, name).clear()


  return Wrapper

@Co()
def co():
  pass
