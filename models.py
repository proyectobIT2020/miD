import datetime

from peewee import *

db = SqliteDatabase('miDbd.db')

class BaseModel(Model):
    class Meta:
        database = database

class Usuario(BaseModel):
    id = AutoField(unique=true)
    email = TextField()
    contraseña_encriptada = TextField()

class PerfilBasico(BaseModel):
    id = ForeignKeyField(Usuario, backref='usuarios')
    nombre = TextField()
    apellido = TextField()
    celular = TextField()
