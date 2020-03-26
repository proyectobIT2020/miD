from peewee import *
from datetime import date


db = SqliteDatabase('miDbd.db')

class BaseModel(Model):
    class Meta:
        database = db

class Usuario(BaseModel):
    idUsuario = AutoField(unique=True)
    email = TextField()
    contraseña_encriptada = TextField()

    class Meta:
        db_table = "Usuarios"

class PerfilBasico(BaseModel):
    id = ForeignKeyField(Usuario, backref='perfiles')
    nombre = TextField()
    apellido = TextField()
    celular = TextField()
    telefono = TextField()
    profesion = TextField()
    empresa = TextField()
    puesto = TextField()
    redSocial = TextField()

    class Meta:
        db_table = "Perfiles_basicos"

class PerfilIntegral(BaseModel):
    id = ForeignKeyField(Usuario, backref='perfiles')
    fecha_nacimiento = TextField()
    pais = TextField()
    ciudad = TextField()
    direccion = TextField()
    entidad_financiera = TextField()
    cuenta = TextField()

    class Meta:
        db_table = "Perfiles_integrales"

class Perfiles(BaseModel):
    id = ForeignKeyField(Usuario, backref='perfiles')
    basico = TextField()
    integral = TextField()
    financiero = TextField()

class DatosActivos(BaseModel):
    id = ForeignKeyField(Usuario, backref='datos')
    celular = BooleanField()
    telefono = BooleanField()
    profesion = BooleanField()
    empresa = BooleanField()
    puesto = BooleanField()
    redSocial = BooleanField()
    fecha_nacimiento = BooleanField()
    pais = BooleanField()
    ciudad = BooleanField()
    direccion = BooleanField()
    entidad_financiera = BooleanField()
    cuenta = BooleanField()

    class Meta:
        db_table = "Datos_activos"

class password(BaseModel):
    id = ForeignKeyField(Usuario, backref='contraseñas')
    contraseña_encriptada = TextField()
    contraseña = TextField()

    class Meta:
        db_table = "Contraseñas"

class Contacto(BaseModel):
    id = ForeignKeyField(Usuario, backref='usuario')
    id_contacto = ForeignKeyField(Usuario, backref='contacto')
    perfil = TextField()

    class Meta:
        db_table = "Contactos"

def agregarUsuario(email1="prueba2@hotmail", contraseña_encriptada1 = "prueba2"):
    """Agregar Usuario"""
    Usuario.create(
        email = email1,
        contraseña_encriptada = contraseña_encriptada1
    )

def borrarUsuario():
    usuario = Usuario.get(Usuario.email == "prueba@hotmail")
    Usuario.delete_instance(usuario)


if __name__ == '__main__':
    #borrarUsuario()
    agregarUsuario("prueba3@hotmail", "clave3")
