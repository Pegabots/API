from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Analises(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    handle = db.Column(db.String(80), nullable=False)
    total = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return '<Twitter User %r>' % self.handle

class AnaliseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Analises
        load_instance = True
        fields = ("id", "handle", "total")