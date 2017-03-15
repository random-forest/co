from co.co import *

@command('quit', help_="Safe exit from application")
def quit_(*argv, **kwargs):
  print("Have a nice trip! •ᴗ• ")
  quit()

@command('help', help_='Example message')
def help_(*argv, **kwargs):
  print('------ Help message ------')

def main():
	loop()

if __name__ == '__main__':
	main()
