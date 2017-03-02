from cli import cli_

@cli_.command(['-build', '-b'])
@cli_.options(['es6', 'jsx', 'nodejs'])
def build_(res):
  pass

@cli_.command(['-help', '-h'])
def help_(res):
  pass

@cli_.command(['-quit', '-q'])
def quit_(res):
  pass
