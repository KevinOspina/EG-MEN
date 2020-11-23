from flask import Flask, render_template, request
import requests

app = Flask(__name__)

tipo_destinatarios = ['Simple', 'Grupal']
tipo_canales = ['SMS', 'Email','WhatsApp','Llamada']

@app.route('/listarCanales', methods=['GET'])
def listarCanales():
    canales = requests.get('http://localhost:3000/canal').json()
    #print(canales)
    return render_template('canales.html', canales=canales)


@app.route('/crearCanales', methods=['GET'])
def crearCanales():
    return render_template('listarCanales.html',tipo_destinatarios=tipo_destinatarios,tipo_canales=tipo_canales)


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