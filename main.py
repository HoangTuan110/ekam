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
@click.option("--quiet", default=True, help="Don't print out the unnecessary debug data")
def ply(task, tree, quiet):
    with open("Ekamfile", "r") as f:
        run(f.read(), tree, quiet)
    if task in global_env and isinstance(global_env[task], tuple):
        # This is indexing hell
        click.echo(global_env[task][1][0]["v"])
    else:
        click.secho(f"No task named {task}", fg="red")

main.add_command(ply)

if __name__ == '__main__':
    main()
