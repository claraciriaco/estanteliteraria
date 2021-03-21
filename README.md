Rodando o código no windows:

python -m venv venv

venv\Scripts\pip3 install -r requirements.txt

venv\Scripts\activate.bat

Atualizar banco de dados:
python run.py db migrate
python run.py db upgrade

Iniciar servidor:
python run.py runserver
