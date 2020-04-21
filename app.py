from flask import Flask, render_template, request, flash, redirect, url_for, session, g
from flaskext.mysql import MySQL
import mysql.connector
from peewee import *
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
import models

app = Flask (__name__)


#config MySQL
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'middb'
app.config['MYSQL_DATABASE_CURSORCLASS'] = 'DictCursor'

#init MySQL
mysql=MySQL()
mysql.init_app(app)

#Portada
@app.route('/')
def Index():
    return render_template('index.html')

#Registro

class RegisterForm(Form):
    email = StringField('Correo', [validators.Length(min=6, max=50)])
    password = PasswordField('Contraseña', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message="Las contraseñas no coinciden")
    ])
    confirm = PasswordField('Confirmar contraseña')

@app.route('/registro', methods = ['POST', 'GET'])
def registro():
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
