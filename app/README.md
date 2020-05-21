# HTTP Web Service

This is an HTTP API skeleton to run model inference. The web app is powered by Flask.

![screen](https://user-images.githubusercontent.com/7880/82588486-19c52800-9b58-11ea-85b4-9f48e141d9ad.png)

## Running the web app

From the project root:

```
whisk app start
```

The app is available at http://localhost:5000/. It contains two routes:

* http://localhost:5000/ - get predictions via an HTML form.
* http://localhost:5000/predict - Submit data for predictions via JSON.

If the source code (``*.py` files) is updated, the app is reloaded automatically in development mode.

## Example API Usage

```
curl --location --request POST 'http://localhost:5000/predict' \
--header 'Content-Type: application/json' \
--data-raw '{"data":["Just happened a terrible car crash", "Theyd probably still show more life than Arsenal did yesterday, eh? EH?"]}'
```

```
[
  [
    0.7632551789283752
  ],
  [
    0.162011981010437
  ]
]
```


## Creating an app on Heroku

From the project root:

```
whisk app create [HEROKU APP NAME]
```
