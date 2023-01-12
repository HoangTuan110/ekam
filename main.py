"""
Ekam's CLI
"""

import click
from os import system
from ekam import run, global_env

def execute_task(task):
    # This is indexing hell
    cmds = global_env[task][1]
    for cmd in cmds:
        # If the command is actually not a command but another recipe
        # then we will run that recipe instead
        if cmd["t"] == 3:
            execute_task(cmd["v"])
        else:
            click.echo(cmd["v"])
            system(cmd["v"])

@click.group()
def main():
    pass

@click.command()
@click.argument("task")
@click.option("--tree", default=False)
@click.option("--quiet", default=True)
def ply(task, tree, quiet):
    with open("Ekamfile", "r") as f:
        run(f.read(), tree, quiet)
    # If the name is in the environment and it is an actual task (aka a tuple)
    # then we can run it
    if task in global_env and isinstance(global_env[task], tuple):
        execute_task(task)
    # If the task is an alias, then we simply execute the task name that
    # alias is associated with
    elif task in global_env and global_env[task]["t"] == 6:
        execute_task(global_env[task]["v"])
    else:
        click.secho(f"No task named {task}", fg="red")

main.add_command(ply)

if __name__ == '__main__':
    main()
