from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Length

class LoginForm(FlaskForm):
    username=StringField("Usuario: ",validators=[DataRequired()])
    password=PasswordField("Contraseña: ",validators=[DataRequired()])
    boton=SubmitField("Ingresar")

class EditProfileForm(FlaskForm):
    name = StringField('Nombre:', validators=[Length(0, 64)])
    location = StringField('Locación:', validators=[Length(0, 64)])
    about_me = TextAreaField('Sobre mi:')
    submit = SubmitField('Actualizar')

class PostForm(FlaskForm):
    body = TextAreaField("¿En qué estás pensando?", validators=[DataRequired()])
    submit = SubmitField('Postear')

class EditPostForm(FlaskForm):
    body = TextAreaField("¿En qué estás pensando?", validators=[DataRequired()])
    submit = SubmitField('Actualizar')

