from app import app

@app.route("/index")
@app.route("/")
def index():
    return "Página principal" 

@app.route("/cadastro")
def cadastro ():
    return "Página de Cadastro" 

@app.route("/login")
def cadastro ():
    return "Página de Login"

@app.route("/estante")
def estante ():
    return "Página dos livros" 

@app.route("/cadastrolivro")
def cadastrolivro ():
    return "Cadastrar um novo livro" 
