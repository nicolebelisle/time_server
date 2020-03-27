from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)


@app.route("/time", methods=["GET"])
def current_time():
    t = datetime.now().time().strftime("%H:%M:%S")
    return t

if __name__=="__main__":
    app.run()