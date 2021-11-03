import settings as s
from flask import Flask
from celery import Celery

app = Flask(__name__)  # Flask core instance initiated
app.config["SQLALCHEMY_DATABASE_URI"] = s.os.environ.get("DATABASE_URL")
app.config['JSON_SORT_KEYS'] = False
app.config['CELERY_BROKER_URL'] = s.os.environ.get("CELERY_BROKER_URL")
app.config['CELERY_RESULT_BACKEND'] = s.os.environ.get("CELERY_RESULT_BACKEND")

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

from app.routes import routes