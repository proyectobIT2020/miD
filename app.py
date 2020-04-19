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
app.config['MYSQL_DATABASE_user'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'Mysql'
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
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message="Password do not match")
    ])
    confirm = PasswordField('Confirm Password')

@app.route('/registro', methods = ['POST', 'GET'])
def registro():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))

        cur = mysql.get_db().cursor()
        cur.execute("INSERT INTO users(email, password) VALUES(%s, %s)",(email, password))
        mysql.get_db().commit()
        cur.close()

        flash('You are now registered and can log in', 'success')
        redirect(url_for('index'))

        return render_template('registro.html', form=form)
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
