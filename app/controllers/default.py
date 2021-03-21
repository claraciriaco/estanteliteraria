from app import app
from flask import request, render_template, redirect, url_for, flash, abort
from flask_login import login_user, logout_user, login_required, current_user
from app.models.forms import LivroForm, LoginForm, CadastroForm
from app.models.tables import Book, User
from app import db, lm

from werkzeug.urls import url_parse

@app.route("/index")
@app.route("/")
def home():
    return render_template('index.html')


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route("/cadastrar", methods=['GET', 'POST'])
def cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        r = User(
            username=form.username.data,
            name=form.name.data, 
            email=form.email.data
            )
        r.set_password(form.password.data)

        confirmation = User.query.filter_by(email= form.email.data).first()

        if (confirmation == None):
            db.session.add(r)
            db.session.commit()
            flash("Conta Criada")
            return redirect(url_for('login'))

        else:
            flash("Já exite uma conta com esse e-mail!")
            
        

    return render_template('cadastro.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash("Seja bem-vindo!")
        return redirect(url_for('estante'))
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data): 
            login_user(user)
            flash("Usuário Confirmado")
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('estante')
            return redirect(next_page)

        else:
            flash("Dados Invélidos")    
    return render_template('login.html', form=form)

    #Usuário Logado

@app.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash("Sair da conta")
    return redirect(url_for("login"))

@app.route("/estante")
@login_required
def estante():
    Books = Book.query.all()
    return render_template('estante.html', Books=Books)

@app.route("/estante/novo", methods=['GET', 'POST'])
@login_required
def novolivro():
    user = User.query.get(current_user.id)
    book = user.book
    
    form = LivroForm()
    if form.validate_on_submit():
        f = Book(title=form.title.data, autor=form.autor.data,
      datainicio=form.datainicio.data, datafim=form.datafim.data, obs=form.obs.data, dono=user)
        db.session.add(f)
        db.session.commit()
        return redirect(url_for("estante"))
    return render_template("cadastrolivro.html", form=form)



#Tratamento de erros

@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', error_id=404, error_desc="Desculpa, página não encontrada!"), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('error.html', error_id=500, error_desc="Desculpa, erro interno do servidor!"), 500

#