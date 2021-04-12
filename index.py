from flask import Flask, request
from hdbcli import dbapi
import pandas as pd
import json
app = Flask(__name__)
@app.route("/")
def hello():
    events = request.args.get('event')
    map = json.loads(events)
    key = map["documentInput"]["itemInput"]["attributes"][10]["name"]
    keyval = map["documentInput"]["itemInput"]["attributes"][10]["values"]
    return '''<h1> Below Events logs are:</h1> <br><br> key: {} :: keyVal:{}'''.format(key,keyval)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
