from flask import jsonify, request
from db.db import cnx

class Canal:
    global cur  
    cur = cnx.cursor()
    
    def list():
        lista = []
        cur.execute("SELECT * FROM canal")
        rows = cur.fetchall()
        colums = [i[0] for i in cur.description]
        for row in rows:
            registro = zip(colums,row)
            json = dict(registro)
            lista.append(json)
        return jsonify(lista)
        cnx.close


    def insert(body):
        data = (body['nombre'],body['tipo'],body['tipoDestinatario'],body['fecha'])
        sql = "INSERT INTO canal(nombre, tipo, tipoDestinatario,fecha) VALUES (%s,%s,%s,%s)"
        cur.execute(sql,data)
        cnx.commit()
        return{'estado': "OK"}, 200

    def delete(body):
        idCanal = (body['idCanal'])
        sql = "DELETE FROM canal WHERE idCanal=" + idCanal
        cur.execute(sql,idCanal)
        cnx.commit()
        return {"status": "OK"}, 200



