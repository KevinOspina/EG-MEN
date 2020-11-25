from flask import jsonify, request
from db.db import cnx

class Canal:
    global cur  
    cur = cnx.cursor()
    
    def get():
        lista = []
        cur.execute("SELECT * FROM Canal")
        rows = cur.fetchall()
        colums = [i[0] for i in cur.description]
        for row in rows:
            registro = zip(colums,row)
            json = dict(registro)
            lista.append(json)
        return jsonify(lista)
        cnx.close


    def post(body):
        data = (body['nombre'],body['tipo'],body['tipo_destinatario'],body['fecha'])
        sql = "INSERT INTO Canal(nombre, tipo, tipo_destinatario,fecha) VALUES (%s,%s,%s,%s)"
        cur.execute(sql,data)
        cnx.commit()
        return{'estado': "OK"}, 200

    def delete(body):
        id_canal = (body['id_canal'])
        sql = "DELETE FROM Canal WHERE id_canal=" + id_canal
        cur.execute(sql,id_canal)
        cnx.commit()
        return {"status": "OK"}, 200

    



