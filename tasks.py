import sys
from solve_me import TasksCommand


try:
    # Extract Arguments from Command Line
    cli_args = sys.argv[1:]
    command = None
    arguments = None
    if len(cli_args) == 0:
        raise Exception("Arguments not supplied")
    elif len(cli_args) == 1:
        command = cli_args[0]
    if len(cli_args) > 1:
        command = cli_args[0]
        arguments = cli_args[1:]
    # Run the Task Command Class with the arguments supplied
    TasksCommand().run(command, arguments)
except Exception as e:
    print(str(e))
