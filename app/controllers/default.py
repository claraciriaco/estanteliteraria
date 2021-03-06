from flask import request, render_template, redirect, url_for
from app import app, db

from app.models.tables import Book, User

from app.models.forms import LoginForm

from app.models.formscadastro import CadastroForm

from app.models.formslivro import LivroForm

from app import db

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    return render_template("login.html", form=form)
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
        return ("entrou")

@app.route("/cadastro/", methods=['GET', 'POST'])
def cadastro():
  form = CadastroForm()
  if form.validate_on_submit():
    i = User (username=form.username.data, password = form.password.data,
    name = form.name.data, email = form.email.data)
    db.session.add(i)
    db.session.commit()
    print(form.name.data)
    return redirect("login")
  return render_template("cadastro.html", form=form)
  


@app.route("/estante")
def estante():
    return render_template('estante.html')

@app.route("/estante/novo", methods=['GET', 'POST'])
def cadastrolivro():
  form = LivroForm()
  if form.validate_on_submit():
    f = Book(title=form.title.data, autor=form.autor.data,
      datainicio=form.datainicio.data, datafim=form.datafim.data, obs=form.obs.data)
    db.session.add(f)
    db.session.commit()
    print(form.title.data)
    return redirect(url_for("estante"))
  return render_template("cadastrolivro.html", form=form)


@app.route("/teste/<info>")
@app.route("/teste", defaults={"info" : None})
def teste(info):
    r = User.query.filter_by(username="claraC").all()
    print(r)
    return ("okay")