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
