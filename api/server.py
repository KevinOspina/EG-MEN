from flask import Flask, request
from flask_cors import CORS
from controllers.Canal import Canal

app = Flask(__name__)


@app.route('/canal', methods=['GET'])
def getAll():
    return (Canal.get())

@app.route('/canal', methods=['POST'])
def post():
    body =  request.json
    return (Canal.post(body))

@app.route('/canal', methods=['DELETE'])
def delete():
    body = request.json
    return (Canal.delete(body))
