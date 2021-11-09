from flask import Flask, json, jsonify, request
import mysql.connector
from flask_cors import CORS

db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Admin',
    database='db-encuesta'
)

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Hello World'


@app.post('/usuarios')
def CrearUsuario():
    #request = lo que envia el cliente
    #response = lo que voy a responder

    datos = request.json
    cursor = db.cursor()
    cursor.execute('''INSERT INTO usuario(nombre,email,contrasena) 
        VALUES(%s,%s,%s)''',(
        datos['nombres'],
        datos['email'],
        datos['contrasena']
        ))

    db.commit()

    return jsonify({
        "mensaje": "usuario creado exitosamente"
    })

@app.get('/usuarios')
def ListarUsuarios():
    cursor = db.cursor(dictionary=True)

    cursor.execute('select * from usuario')
    usuarios = cursor.fetchall()
    return jsonify(usuarios)


@app.put('/usuarios/<id>')
def actualizarUsuario(id):
    datos = request.json

    cursor = db.cursor()

    cursor.execute('''UPDATE usuario set nombre=%s, 
        email=%s, contrasena=%s where idusu=%s''',(
            datos['nombre'],
            datos['email'],
            datos['contrasena'],
            id
        ))

    db.commit()

    return jsonify({
        "mensaje": "Usuario actualizado correctamente"
    })

@app.delete('/usuarios/<id>')
def eliminarUsuario(id):
        
    cursor = db.cursor()
    cursor.execute('''DELETE FROM usuario WHERE idusu=%s''', (id,))
    db.commit()
    
    return jsonify({
        "mensaje": "Usuario eliminado correctamente"                      
    })

@app.post('/encuesta')
def CrearEncuesta():
    
    datos = request.json
    cursor = db.cursor()
    cursor.execute('''INSERT INTO encuesta(idusu,titulo,descripcion,imagen) 
        VALUES(%s,%s,%s,%s)''',(
        datos['idusu'],
        datos['titulo'],
        datos['descripcion'],
        datos['imagen']
        ))

    db.commit()

    return jsonify({
        "mensaje": "Encuesta creada exitosamente"
    })

@app.get('/encuesta')
def listarEncuestas():
    cursor = db.cursor(dictionary=True)

    cursor.execute('select * from encuesta')
    encuesta = cursor.fetchall()
    return jsonify(encuesta)

@app.put('/encuesta/<id>')
def actualizarEncuesta(id):
    datos = request.json

    cursor = db.cursor()

    cursor.execute('''UPDATE encuesta set idusu=%s,titulo=%s, 
        descripcion=%s, imagen=%s where idenc=%s''',(
            datos['idusu'],
            datos['titulo'],
            datos['descripcion'],
            datos['imagen'],
            id
        ))

    db.commit()

    return jsonify({
        "mensaje": "Encuesta actualizada correctamente"
    })

@app.delete('/encuesta/<id>')
def eliminarEncuesta(id):
        
    cursor = db.cursor()
    cursor.execute('''DELETE FROM encuesta WHERE idenc=%s''', (id,))
    db.commit()
    
    return jsonify({
        "mensaje": "Encuesta eliminada correctamente"                      
    })

@app.post('/seccion')
def CrearSeccion():
    
    datos = request.json
    cursor = db.cursor()
    cursor.execute('''INSERT INTO seccion(idenc,seccion) 
        VALUES(%s,%s)''',(
        datos['idenc'],
        datos['seccion']
        ))

    db.commit()

    return jsonify({
        "mensaje": "seccion creada exitosamente"
    })

@app.get('/seccion')
def listarSeccion():
    cursor = db.cursor(dictionary=True)

    cursor.execute('select * from seccion')
    seccion = cursor.fetchall()
    return jsonify(seccion)

@app.put('/seccion/<id>')
def actualizarSeccion(id):
    datos = request.json

    cursor = db.cursor()

    cursor.execute('''UPDATE seccion set idenc=%s,seccion=%s where idsec=%s''',(
            datos['idenc'],
            datos['seccion'],
            id
        ))

    db.commit()

    return jsonify({
        "mensaje": "seccion actualizada correctamente"
    })

@app.delete('/seccion/<id>')
def eliminarseccion(id):
        
    cursor = db.cursor()
    cursor.execute('''DELETE FROM seccion WHERE idsec=%s''', (id,))
    db.commit()
    
    return jsonify({
        "mensaje": "seccion eliminada correctamente"                      
    })
@app.post('/pregunta')
def CrearPregunta():
    
    datos = request.json
    cursor = db.cursor()
    cursor.execute('''INSERT INTO pregunta(idsec,idtpreg,pregunta) 
        VALUES(%s,%s,%s)''',(        
        datos['idsec'],
        datos['idtpreg'],
        datos['pregunta']
        ))

    db.commit()

    return jsonify({
        "mensaje": "Pregunta creada exitosamente"
    })

@app.get('/pregunta')
def listarPregunta():
    cursor = db.cursor(dictionary=True)

    cursor.execute('select * from pregunta')
    pregunta = cursor.fetchall()
    return jsonify(pregunta)

@app.put('/pregunta/<id>')
def actualizarPregunta(id):
    datos = request.json

    cursor = db.cursor()

    cursor.execute('''UPDATE pregunta set idsec=%s,idtpreg=%s,pregunta=%s where idpreg=%s''',(
            datos['idsec'],
            datos['idtpreg'],
            datos['pregunta'],
            id
        ))

    db.commit()

    return jsonify({
        "mensaje": "Pregunta actualizada correctamente"
    })

@app.delete('/pregunta/<id>')
def eliminarPregunta(id):
        
    cursor = db.cursor()
    cursor.execute('''DELETE FROM pregunta WHERE idpreg=%s''', (id,))
    db.commit()
    
    return jsonify({
        "mensaje": "Pregunta eliminada correctamente"                      
    })

@app.post('/tipo_pregunta')
def CrearTipo_pregunta():
    
    datos = request.json
    cursor = db.cursor()
    cursor.execute('''INSERT INTO tipo_pregunta(tipopregunta)
        VALUES(%s)''',(
        datos['tipopregunta'],
        ))

    db.commit()

    return jsonify({
        "mensaje": "Tipo de pregunta creada exitosamente"
    })

@app.get('/tipo_pregunta')
def listarTipo_pregunta():
    cursor = db.cursor(dictionary=True)

    cursor.execute('select * from tipo_pregunta')
    tipo_pregunta = cursor.fetchall()
    return jsonify(tipo_pregunta)

@app.put('/tipo_pregunta/<id>')
def actualizarTipo_pregunta(id):
    datos = request.json

    cursor = db.cursor()

    cursor.execute('''UPDATE tipo_pregunta set tipopregunta=%s where idtpreg=%s''',(
            datos['tipopregunta'],
            id
        ))

    db.commit()

    return jsonify({
        "mensaje": "tipo de pregunta actualizada correctamente"
    })

@app.delete('/tipo_pregunta/<id>')
def eliminarTipo_pregunta(id):
        
    cursor = db.cursor()
    cursor.execute('''DELETE FROM tipo_pregunta WHERE idtpreg=%s''', (id,))
    db.commit()
    
    return jsonify({
        "mensaje": "tipo de pregunta eliminada correctamente"                      
    })

@app.post('/opcion_pregunta')
def CrearOpcion_pregunta():
    
    datos = request.json
    cursor = db.cursor()
    cursor.execute('''INSERT INTO opcion_pregunta(opcpregunta)
        VALUES(%s)''',(
        datos['opcpregunta'],
        ))

    db.commit()

    return jsonify({
        "mensaje": "Opcion de pregunta creada exitosamente"
    })

@app.get('/opcion_pregunta')
def listarOpcion_pregunta():
    cursor = db.cursor(dictionary=True)

    cursor.execute('select * from opcion_pregunta')
    opcion_pregunta = cursor.fetchall()
    return jsonify(opcion_pregunta)

@app.put('/opcion_pregunta/<id>')
def actualizarOpcion_pregunta(id):
    datos = request.json

    cursor = db.cursor()

    cursor.execute('''UPDATE opcion_pregunta set opcpregunta=%s where idopcpreg=%s''',(
            datos['opcpregunta'],
            id
        ))

    db.commit()

    return jsonify({
        "mensaje": "Opcion de pregunta actualizada correctamente"
    })

@app.delete('/opcion_pregunta/<id>')
def eliminarOpcion_pregunta(id):
        
    cursor = db.cursor()
    cursor.execute('''DELETE FROM opcion_pregunta WHERE idtopcpreg=%s''', (id,))
    db.commit()
    
    return jsonify({
        "mensaje": "Opcion de pregunta eliminada correctamente"                      
    })

app.run(debug=True)