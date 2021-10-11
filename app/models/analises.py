from app.models import db, ma
import random

class Analises(db.Model):
    __tablename__ = 'analises'
    id = db.Column(db.Integer, primary_key=True)
    handle = db.Column(db.String(80), nullable=False)
    total = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return '<Twitter User %r>' % self.handle

class AnaliseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Analises
        load_instance = True
        fields = ("id", "handle", "total") # list filds which will be available for final user


