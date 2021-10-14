from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
