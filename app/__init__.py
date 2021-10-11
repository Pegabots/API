import settings as s
from flask import Flask

app = Flask(__name__)  # Flask core instance initiated
app.config["SQLALCHEMY_DATABASE_URI"] = s.os.environ.get("DATABASE_URL")
app.config['JSON_SORT_KEYS'] = False

from app.routes import routes