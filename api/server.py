from flask import Flask, request
from flask_cors import CORS
from controllers.Canal import Canal

app = Flask(__name__)

@app.route('/')
def Index():
    return 'Hello world'

@app.route('/canal', methods=['GET'])
def getAll():
    return (Canal.list())

@app.route('/canal', methods=['POST'])
def insert():
    body =  request.json
    return (Canal.insert(body))

@app.route('/canal', methods=['DELETE'])
def delete():
    body = request.json
    return (Canal.delete(body))



if __name__ == '__main__':
 app.run(port = 3000, debug=True)

