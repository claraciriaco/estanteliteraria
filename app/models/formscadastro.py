from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired 

class CadastroForm(Form):
    username = StringField("username",validators=[DataRequired()])
    name = StringField("name",validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    
    submit = SubmitField('submit')