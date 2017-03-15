"""
Example usage -->

from co.co import *

@command('init') - "init" name called automatically an app startup
def init(*argv):
	--- Exaple help message ---
	pass

@command('build', help_="build [ -opt1, -opt2, -opt3, --help ] /path") - custom command
@option(name='-opt1')
@option(name='-opt2')
@option(name='-opt3')
def build_(*argv):
	 name = argv[0]
	 options = argv[0][1]
	 path = argv[0][2]

	 call('path/to/{0}.sh {1} {2}'.format(name, options, path), shell=True)
"""

print(__doc__)
