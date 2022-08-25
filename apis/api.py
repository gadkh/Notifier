from flask import Flask, request
import json


app = Flask(__name__)


@app.route("/notify", methods=['GET'])
def notify():
    status_code = 200
    return json.dumps({'message': "Hello world, it's work"}), status_code, {'ContentType': 'application/json'}


def run():
    app.run(debug=True, port=5000)
