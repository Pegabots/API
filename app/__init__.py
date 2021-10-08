import settings as s
from flask import Flask

app = Flask(__name__)  # Flask core instance initiated
app.config["SQLALCHEMY_DATABASE_URI"] = s.os.environ.get("DATABASE_URL")

from app import routes