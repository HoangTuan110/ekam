"""
Ekam's CLI
"""

import click
from ekam import eval

@click.group()
def main():
    pass

@click.command()
@click.argument("task")
def ply(task):
    click.echo(eval(task))

main.add_command(ply)

if __name__ == '__main__':
    main()
