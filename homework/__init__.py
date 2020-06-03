from flask import Flask

from config import Config

# Import for Flask Db and Migrator
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create flask app variable
app = Flask(__name__) 
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from homework import routes, models
