from flask import Flask, render_template, request
from peewee import *


app = Flask (__name__)

#Portada
@app.route('/')
def Index():
    return render_template('Registro.html')
#Registro
@app.route('/registro', methods=['POST'])
def registro():
    if request.method == 'POST':
        mail = request.form['mail']
        contraseña = request.form['contraseña']
        print(mail)
        print(contraseña)
    return 'usuario registrado'

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
