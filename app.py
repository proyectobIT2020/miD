from flask import Flask, render_template, request, flash, redirect, url_for, session, g
from flaskext.mysql import MySQL
import mysql.connector
from peewee import *
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

app = Flask (__name__)


#config MySQL - CAMBIAR CONTRASEÑA LOCAL
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

#class ID():
#    cur = mysql.get_db().cursor()
#    cur = cur.execute ("SELECT id FROM Usuarios WHERE email = ()")
#    mysql.get_db().commit()
#    cur.close()

#Ingresar datos
class DatosForm(Form):
    nombre = StringField('Nombre/s', [validators.Length(min=1, max=50)])
    apellido = StringField('Apellido/s', [validators.Length(min=1, max=50)])
    fecha_nacimiento = StringField('Fecha de Nacimiento', [validators.Length(min=1, max=50)])
    celular = StringField('Celular', [validators.Length(min=1, max=50)])
    telefono = StringField('Teléfono', [validators.Length(min=1, max=50)])
    pais = StringField('País', [validators.Length(min=1, max=50)])
    ciudad = StringField('Ciudad', [validators.Length(min=1, max=50)])
    direccion = StringField('Dirección', [validators.Length(min=1, max=50)])
    profesion = StringField('Profesión', [validators.Length(min=1, max=50)])
    empresa = StringField('Empresa', [validators.Length(min=1, max=50)])
    cargo = StringField('Cargo', [validators.Length(min=1, max=50)])
    banco = StringField('Banco', [validators.Length(min=1, max=50)])
    num_cuenta = StringField('Numero de cuenta', [validators.Length(min=1, max=50)])
    redes_sociales = StringField('Redes sociales', [validators.Length(min=1, max=50)])

@app.route('/datos', methods = ['POST', 'GET'])
def datos():
    form = DatosForm(request.form)
    if request.method == 'POST' and form.validate():
        nombre = form.nombre.data
        apellido = form.apellido.data
        fecha_nacimiento = form.fecha_nacimiento.data
        celular = form.celular.data
        telefono = form.telefono.data
        pais = form.pais.data
        ciudad = form.ciudad.data
        direccion = form.direccion.data
        profesion = form.profesion.data
        empresa = form.empresa.data
        cargo = form.cargo.data
        banco = form.banco.data
        num_cuenta = form.num_cuenta.data
        redes_sociales = form.redes_sociales.data

        cur = mysql.get_db().cursor()
        cur.execute("INSERT INTO datos_activos(nombre, apellido, fecha_nacimiento, celular, telefono, pais, ciudad, direccion, profesion, empresa, cargo, banco, num_cuenta, redes_sociales) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(nombre, apellido, fecha_nacimiento, celular, telefono, pais, ciudad, direccion, profesion, empresa, cargo, banco, num_cuenta, redes_sociales))
        mysql.get_db().commit()
        cur.close()

        flash('¡Datos completos!', 'success')
        return redirect(url_for('Index'))
    return render_template('ingresarDatos.html', form=form)



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
