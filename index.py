from flask import Flask, request
from hdbcli import dbapi
import pandas as pd

app = Flask(__name__)
@app.route("/")
def hello():
    events = request.args.get('event')
    return '''<h1> Below Events logs are:</h1> <br><br> {}'''.format(events)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
