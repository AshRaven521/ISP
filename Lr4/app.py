from flask_migrate import Migrate
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
database = SQLAlchemy(app)
migration = Migrate(app, database)
