from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager 
from flask_migrate import Migrate, MigrateCommand
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object('config')

bootstrap = Bootstrap(app) 

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.models import tables, forms
from app.controllers import default


