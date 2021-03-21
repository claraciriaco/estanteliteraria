from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class LivroForm(FlaskForm):
    title = StringField("title",validators=[DataRequired()])
    autor = StringField("autor",validators=[DataRequired()])
    datainicio = IntegerField("datainicio", validators=[DataRequired()])
    datafim = IntegerField("datafim", validators=[DataRequired()])
    obs = StringField("obs",validators=[DataRequired()])

    submit = SubmitField('submit')

class LoginForm(FlaskForm):
    username = StringField("username",validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField ("remember_me")
    
    submit = SubmitField('submit')

class CadastroForm(FlaskForm):
    username = StringField("username",validators=[DataRequired()])
    email = StringField("email",validators=[DataRequired()])
    name = StringField("name",validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    
    submit = SubmitField('submit')


