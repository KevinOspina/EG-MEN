from flask import Flask, render_template, request
import requests
from flask_cors import CORS


app = Flask(__name__, template_folder='templates', static_folder='static' )

@app.route('/listCanales', methods=['GET'])
def listarCanales():
    canales = requests.get('http://localhost:3000/canal').json()
    #print(canales)
    return render_template('canales.html', canales=canales)


@app.route('/crearCanales', methods=['GET'])
def crearCanales():
    return render_template('index.html')


@app.route('/guardarCanales', methods=['POST'])
def guardarCanales():

    canal = dict(request.values)
    
    canal['nombre'] = str(request.form['nombre'])
    canal['tipo'] = str(request.form['tipo'])
    canal['tipo_destinatario'] = str(request.form['tipo_destinatario'])
    canal['fecha'] = str(request.form['fecha'])

    requests.post('http://localhost:3000/canal', json=canal)

    return (listarCanales())


app.run(port=3001, host='0.0.0.0', debug=True)