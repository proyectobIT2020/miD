from flask import Flask, render_template
from peewee import *
import sqlite3

#***************************************************
#base de datos
con = sqlite3.connect('miDbd.db')
cursorObj = con.cursor()
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('miDbd.db')
        return con
    except Error:
        print(Error)

def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE if not exists usuario(IDusuario integer PRIMARY KEY, mail text, contraseña text)")
    con.commit()

con = sql_connection()

sql_table(con)
#****************************************************

app = Flask (__name__)

#Portada
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
@app.route('/inicio')
def ingresar():
    return 'Iniciar sesión'
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
