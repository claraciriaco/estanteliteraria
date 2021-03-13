from flask import request, render_template, redirect, url_for

from app import app, db

from flask_login import current_user, login_user, logout_user

from app.models.tables import Book

from app.models.formslivro import LivroForm


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')



@app.route("/estante")
def estante():
    Books = Book.query.all()
    return render_template('estante.html', Books=Books)

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
