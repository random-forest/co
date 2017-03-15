from co.utils import *
from funcy import *
from operator import *

def build_cmd(cmd):
  return {
    'name': cmd[0] if len(cmd) > 0 else None,
    'options': cmd[1] if len(cmd) > 1 else None,
    'path': cmd[2] if len(cmd) > 2 else None
  }

def change_rule(a, b):
  length = len(b)
  current_name = getitem(a, 'name')
  current_options = getitem(a, 'options')

  rules = list(map(get_val, b))

  def by_option(x):
    return eq(getitem(x, 'name'), current_options)

  for rule in rules:
    r_name = getitem(rule, 'name')
    r_options = getitem(rule, 'options')
    setitem(a, 'help', getitem(rule, 'help'))

    if eq(current_name, r_name):
      if eq(r_options, None):
        return a
      else:
        if ne(any(by_option, r_options), True):
          if ne(current_options, None) and ne(current_options, "--help"):
            print('Sorry! But, command "{0}" doesn"t have option named "{1}"!'.format(current_name, current_options))

          setitem(a, 'options', "--help")
          return a

        if any(by_option, r_options):
          return a
        else:
          continue

def run_command(rule, root):
  fns = getattr(root, 'fns')

  if ne(rule, None):
    rule_name = rule['name'] + '_'
    rule_options = rule['options']

    for f in fns:
      if eq(rule_options, "--help"):
        print(getitem(rule, 'help'))
        break

      if eq(f.__name__, rule_name):
        return f(rule)
      else:
        continue
