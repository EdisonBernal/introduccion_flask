from flask import Flask, json, jsonify, request
import mysql.connector

db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Admin',
    database='usuarios'   
)

app = Flask(__name__)

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
        email=%s, contrasena=%s where id=%s''',(
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
    cursor.execute('''DELETE FROM usuario WHERE id=%s''', (id,))
    db.commit()
    
    return jsonify({
        "mensaje": "Usuario eliminado correctamente"                      
    })
print(id)
app.run(debug=True)