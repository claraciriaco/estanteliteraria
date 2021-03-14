from flask_wtf import Form
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired 

class LivroForm(Form):
    title = StringField("title",validators=[DataRequired()])
    autor = StringField("autor",validators=[DataRequired()])
    datainicio = IntegerField("datainicio", validators=[DataRequired()])
    datafim = IntegerField("datafim", validators=[DataRequired()])
    obs = StringField("obs",validators=[DataRequired()])

    submit = SubmitField('submit')
