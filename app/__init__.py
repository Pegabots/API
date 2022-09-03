import settings as s
from flask import Flask

app = Flask(__name__, template_folder="templates/")  # Flask core instance initiated
app.config["SQLALCHEMY_DATABASE_URI"] = s.os.environ.get("DATABASE_URL")
app.config['JSON_SORT_KEYS'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from app.routes.analise.route import router as analise_router
from app.routes.auth.route import router as auth_router

app.register_blueprint(analise_router)
app.register_blueprint(auth_router)