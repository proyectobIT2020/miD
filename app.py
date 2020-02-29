from flask import Flask, render_template
from peewee import *

db = SqliteDatabase('midapp.db')

app = Flask (__name__)

#Ruta página inicio
#holis
<<<<<<< HEAD
#como estas?

=======
#PRUEBA NABI
>>>>>>> ec5084f8506202961f5bf528af5528ab3d232bca
@app.route('/')
def Index():
    return render_template('index.html')
#Registro
@app.route('/registro')
def registro():
    return 'Crear usuario nuevo'
#Ingresar datos
@app.route('/datos')
def datos():
    return 'Ingreso de datos'
#Login
@app.route('/ingresar')
def ingresar():
    return 'Iniciar sesión'
#Mi perfil
@app.route('/perfil')
def perfil():
    return 'Mi perfil'
#olvide contraseña
@app.route('/recuperarcontraseña')
def contra():
    return 'Contraseña incorrecta'

#Ejecución del servidor
#debug: reinicio automático
if __name__ == '__main__':
    app.run(port = 3000, debug = True)
