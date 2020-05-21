from flask import Flask, render_template, request, jsonify
import whisk.dvc as dvc
from disaster_tweets.models.model import Model
import sys
import os

# initialize the Flask application
app = Flask(__name__)
model = Model()

@app.route('/', methods=["GET"])
def index():
    result = None
    text=request.args.get("text",None)
    if text:
        result = model.predict([text])[0][0]

    return render_template('index.html', result=result)


@app.route("/predict", methods=["POST"])
def predict():
    """
    Accepts a payload w/content-type="application/json" and expects a `data` key/value.
    `data` is passed into the model for inference.
    """
    input = request.json['data']
    result = model.predict(input)
    return jsonify(result)

if __name__ == "__main__":
    app.run()
