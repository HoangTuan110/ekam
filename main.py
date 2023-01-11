"""
Ekam's CLI
"""

import click
from ekam import run, global_env

@click.group()
def main():
    pass

@click.command()
@click.argument("task")
@click.option("--tree", default=False, help="Print the parsed data as a tree")
def ply(task, tree):
    with open("Ekamfile", "r") as f:
        run(f.read(), tree)
    if task in global_env and isinstance(global_env[task], tuple):
        click.echo(global_env[task[1]["v"]])
    else:
        click.secho(f"No task named {task}", fg="red")

main.add_command(ply)

if __name__ == '__main__':
    main()
