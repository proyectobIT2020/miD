from flask import Flask, render_template
from peewee import *
import sqlite3

#***************************************************
#base de datos
conn = sqlite3.connect('miDbd.db')
cursor = con.cursor()
#insertar fila
cursor.execute(INSERT INTO usuario VALUES ('mail', 'contraseña'))
#salvar datos
conn.commit()
#cerrar conexion
conn.close()
#****************************************************

app = Flask (__name__)

#Portada
@app.route('/')
def Index():
    return render_template('index.html')
#Registro
@app.route('/registro')
def registro():
    return render_template('Registro.html')

#Ingresar datos
@app.route('/datos')
def datos():
    return 'Ingreso de datos'
#Login
@app.route('/inicio')
def ingresar():
    return render_template('iniciarsesion.html')
#Mi perfil
@app.route('/perfil')
def perfil():
    return 'Mi perfil'
#Contactos
@app.route('/contactos')
def contactos():
    return 'Mis contactos'
#olvide contraseña
@app.route('/recuperarcontraseña')
def contra():
    return 'Contraseña incorrecta'

#Ejecución del servidor
#debug: reinicio automático
if __name__ == '__main__':
    app.run(port = 3000, debug = True)
