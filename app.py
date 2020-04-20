from flask import Flask, render_template, request
from peewee import *
#import forms
import models

app = Flask (__name__)

#Portada
@app.route('/')
def Index():
    return render_template('index.html')

#Registro
@app.route('/registro', methods = ['POST', 'GET'])
def registro():
#        contraseña = request.form['contraseña1']
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))

        cur = mysql.get_db().cursor()
        cur.execute("INSERT INTO Usuarios(email, contraseña_encriptada) VALUES(%s, %s)",(email, password))
        mysql.get_db().commit()
        cur.close()

        flash('¡Ya estás registrado!', 'success')
        return redirect(url_for('datos'))

    return render_template('registro.html', form=form)


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
    return render_template('perfil.html')
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
