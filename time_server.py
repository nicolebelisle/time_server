from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)


@app.route("/time", methods=["GET"])
def current_time():
    t = datetime.now().time().strftime("%H:%M:%S")
    return t


@app.route("/date", methods=["GET"])
def current_date():
    d = datetime.now().date().strftime("%m-%d-%y")
    return d

if __name__=="__main__":
    app.run()