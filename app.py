from flask import Flask, render_template, request
from peewee import *
#import forms
#import models.py

app = Flask (__name__)

#Portada
@app.route('/')
def Index():
    return render_template('index.html')
#Registro
@app.route('/registro', methods = ['POST', 'GET'])
def registro():
#    registro_form = forms.RegistroForm(request.form)
#    if request.method == 'POST':
#        mail = request.form['email']
#        contraseña = request.form['contraseña1']
#        contraseña = request.form['contraseña2']
#print()
    return render_template('registro.html')
    #print (email)
    #print (contraseña1)

#    if request.method == 'POST':
#        print (registro_form.mail.data)
#        print (registro_form.contraseña.data)

#    title = "Registro"
#    return render_template('Registro.html', title = title, form = registro_form)

app.config['SECRET_KEY'] = 'any secret string'



#Ingresar datos
@app.route('/datos')
def datos():
    #usuarioEmail = request.form['mail']
    return render_template('ingresarDatos.html')
#Login
@app.route('/inicio', methods = ['POST', 'GET'])
def ingresar():
    return render_template('iniciarsesion.html')
    #usuarioEmail = request.form['mail']
    #return "Ahora eres parte de miD"
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
