<<<<<<< HEAD
import sys
from click import Command

args=sys.argv




def p_a_c(func_command):
	print("[commands]")
	for func in func_command:
		print("    ",func.__name__)


def runserver(app,**kwargs):
	app.run(**kwargs)

func_command=[runserver]
def execute_from_command_line(app):
	try:
		arg=args[1]
		if arg:
			if "runserver" in arg:
				commands=arg.split(":")
				if len(commands) >=2:
					runserver(app,debug=True,port=int(commands[1]))
				else:
					runserver(app,debug=True)
			else:
				Command('db')
		else:
			p_a_c(func_command)
	except IndexError:
		p_a_c(func_command)
=======
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
>>>>>>> 69055f3de1f41ab8d7aa81f732a965e330c0d931
