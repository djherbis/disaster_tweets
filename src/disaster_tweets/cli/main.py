import click
from disaster_tweets.models.model import Model

@click.group()
def cli():
    pass

@cli.command()
@click.argument('x')
def predict(x):
    """
    Predict whether a tweet is about a real disaster (or not).
    Returns a Float between 0-1 (unlikely - likely).

    Example usage:\n
    disaster_tweets predict "Just happened a terrible car crash"
    """
    model = Model()
    res = model.predict([x])[0][0]
    click.echo(res)

if __name__ == "__main__":
    cli()
