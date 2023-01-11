"""
Ekam's CLI
"""

import click
from ekam import run

@click.command()
@click.option("tree", "-t", type=click.BOOL, default=False, help="Print parsed tree of each line before evaling")
def main(tree):
    with open('./Ekamfile', "r") as f:
        run(f.read(), tree)

if __name__ == '__main__':
    main()
