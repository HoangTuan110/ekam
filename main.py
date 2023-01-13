"""
Ekam's CLI
"""

from os import system
import click
import ekam

def execute_recipe(env, recipe):
    # This is indexing hell
    cmds = env[recipe][1]
    for cmd in cmds:
        # If the command is actually not a command but another recipe
        # then we will ekam.run that recipe instead
        if cmd["t"] == 3:
            execute_recipe(env, cmd["v"])
        else:
            click.echo(cmd["v"])
            system(cmd["v"])

@click.group()
def main():
    pass

@click.command()
@click.argument("recipe")
@click.option("--tree", default=False)
@click.option("--quiet", default=True)
def ply(recipe, tree, quiet):
    with open("Ekamfile", "r") as f:
        _, env = ekam.run(f.read(), tree, quiet)
    # If the name is in the environment and it is an actual recipe (aka a tuple)
    # then we can ekam.run it
    if recipe in env and isinstance(env[recipe], tuple):
        execute_recipe(env, recipe)
    # If the recipe is an alias, then we simply execute the recipe name that
    # alias is associated with
    elif recipe in env and env[recipe]["t"] == 6:
        execute_recipe(env, env[recipe]["v"])
    else:
        click.secho(f"No recipe named {recipe}", fg="red")

main.add_command(ply)

if __name__ == '__main__':
    main()
