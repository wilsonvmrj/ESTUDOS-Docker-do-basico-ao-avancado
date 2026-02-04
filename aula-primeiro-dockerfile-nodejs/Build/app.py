from flask import Flask 
from os import getenv
from requests import get 
import json 

app = Flask(__name__)

@app.route("/")
def hellor():
    return """
    <!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Flask</title>
  </head>
  <body>
    <h1>Teste de docker</h1>
  </body>
</html>

"""

@app.route('/health')
def health():
    return "UNHEALTH",200

if __name__ == '__main__':
    app().run(host='0.0.0.0')