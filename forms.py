#instalar con pip

from wtforms import Form, TextField, TextAreaField, SubmitField, validators, StringField
from wtforms.fields.html5 import EmailField

class RegistroForm(Form):
    mail = EmailField('Correo electronico')
    constraseña = TextField ('Constraseña')
