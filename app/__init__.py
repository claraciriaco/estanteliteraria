from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap(app) 

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


login = LoginManager()
login.init_app(app)


from app.controllers import default
from app.models import tables
from app.models import user



