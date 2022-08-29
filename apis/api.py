from flask import Flask, request
from controllers import Controller
import json


app = Flask(__name__)

@app.route("/notify", methods=['GET'])
def notify():
    status_code = 200
    controller = Controller("Gad")
    message = json.dumps(controller.get_message())
    return message, status_code, {'ContentType': 'application/json'}
    # return json.dumps({'message': "Hello world, it's work"}), status_code, {'ContentType': 'application/json'}


def run():
    app.run(debug=True, port=5000)
