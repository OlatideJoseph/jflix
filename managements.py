import sys
from click import Command

args=sys.argv

def runserver(app,**options):
	app.run(debug=True,host="0.0.0.0")

func_command=[runserver]
def execute_from_command_line(app):
	try:
		arg=args[1]
		if arg:
			if arg == "runserver":
				runserver(app)
			else:
				Command('db')
	except IndexError:
		print("[commands]")
		for func in func_command:
			print("    ",func.__name__)
