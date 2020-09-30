from flask import Flask, request
from flask_cors import CORS
from controllers.Canal import Canal
from flask_mysqldb import MySQL
from db.db import cnx

app = Flask(__name__)


@app.route('/canal', methods=['GET'])
def getAll():
    return (Canal.list())

@app.route('/canal', methods=['POST'])
def post():
    body =  request.json
    return (Canal.post(body))

@app.route('/canal', methods=['DELETE'])
def delete():
    body = request.json
    return (Canal.delete(body))

if __name__ == '__main__':
 app.run(port = 3000, debug=True)

