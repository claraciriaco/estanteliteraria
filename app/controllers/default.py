from flask import render_template
from app import app


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/cadastro")
def cadastro():
    return render_template('cadastro.html')

@app.route("/estante")
def estante():
    return render_template('estante.html')

@app.route("/cadastrolivro")
def cadastrolivro():
    return render_template('cadastrolivro.html')
