from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired 

class LoginForm(Form):
    username = StringField("username",validators=[DataRequired()])
    password_hash = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField ("remember_me")
    
    submit = SubmitField('submit')

class CadastroForm(Form):
    username = StringField("username",validators=[DataRequired()])
    email = StringField("email",validators=[DataRequired()])
    password_hash = PasswordField("password_hash", validators=[DataRequired()])
    
    submit = SubmitField('submit')

