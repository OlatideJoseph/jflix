from parent import create_app
from managements import execute_from_command_line
app=create_app()

if __name__ == "__main__":
    execute_from_command_line(app)