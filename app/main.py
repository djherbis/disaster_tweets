import flask
import whisk.dvc as dvc
from disaster_tweets.models.model import Model
import sys
import os

# initialize the Flask application
app = flask.Flask(__name__)
model = Model()

@app.route("/predict", methods=["POST"])
def predict():
    """
    Accepts a payload w/content-type="application/json" and expects a `data` key/value.
    `data` is passed into the model for inference.
    """
    input = flask.request.json['data']
    result = model.predict(input)
    return flask.jsonify(result)

if __name__ == "__main__":
    app.run()
