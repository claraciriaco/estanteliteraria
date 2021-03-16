from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired 

Form = FlaskForm

class LoginForm(Form):
    username = StringField("username",validators=[DataRequired()])
    password_hash = PasswordField("password_hash", validators=[DataRequired()])
    remember_me = BooleanField ("remember_me")
    
    submit = SubmitField('submit')
