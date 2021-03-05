from flask import render_template
from app import app

from app.models.forms import LoginForm

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    else:
        print(form.errors)
    return render_template('login.html', form=form)

@app.route("/cadastro")
def cadastro():
    return render_template('cadastro.html')

@app.route("/estante")
def estante():
    return render_template('estante.html')

@app.route("/cadastrolivro")
def cadastrolivro():
    return render_template('cadastrolivro.html')
