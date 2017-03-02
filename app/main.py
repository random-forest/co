from app import cli_

# MAIN APP POINT
def main(func):
  def wrapper():
    return cli_.loop()
  return wrapper

@main
def cli():
  pass

def main():
	cli()

if __name__ == '__main__':
	main()
