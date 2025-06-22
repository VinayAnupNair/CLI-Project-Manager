# command definitions
import click

@click.group()
def cli():
    pass

@cli.command()
def test():
    print("project manager working")