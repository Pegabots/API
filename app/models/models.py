from app.models import db, ma, migrate
from datetime import datetime

class Analises(db.Model):
    __tablename__ = 'analises'
    id = db.Column(db.Integer, primary_key=True)
    handle = db.Column(db.String(80), nullable=False)
    total = db.Column(db.String(120), nullable=True)
    friends = db.Column(db.String(120), nullable=True)
    network = db.Column(db.String(120), nullable=True)
    sentiment = db.Column(db.String(120), nullable=True)
    temporal = db.Column(db.String(120), nullable=True)
    twitter_id = db.Column(db.String(120), nullable=True)
    twitter_handle = db.Column(db.String(120), nullable=True)
    twitter_user_name = db.Column(db.String(120), nullable=True)
    twitter_is_protected = db.Column(db.Boolean(), nullable=True)
    twitter_user_description = db.Column(db.String(255), nullable=True)
    twitter_followers_count = db.Column(db.Integer(), nullable=True)
    twitter_friends_count = db.Column(db.Integer(), nullable=True)
    twitter_location = db.Column(db.String(120), nullable=True)
    twitter_created_at = db.Column(db.TIMESTAMP(120), nullable=True)
    twitter_is_verified = db.Column(db.Boolean(120), nullable=True)
    twitter_lang = db.Column(db.TIMESTAMP(120), nullable=True)
    twitter_default_profile = db.Column(db.String(255), nullable=True)
    twitter_profile_image = db.Column(db.String(255), nullable=True)
    twitter_withheld_in_countries = db.Column(db.String(255), nullable=True)
    cache_times_served = db.Column(db.Integer(), nullable=True)
    cache_validity = db.Column(db.TIMESTAMP(), nullable=True)
    pegabot_version = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)


    def process_bind_param(value):
        if type(value) is str:
            return datetime.strptime(value, '%Y-%m-%dT %H:%M:%S')
        return value

    def __repr__(self):
        return '<Twitter User %r>' % self.twitter_handle

class AnaliseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Analises
        load_instance = True
        # fields = ("id", "handle", "total", "network") # list filds which will be available for final user


class Feedback(db.Model):
    __tablename__ = 'feedbacks'
    id = db.Column(db.Integer, primary_key=True)
    analisis_id = db.Column(db.String(80), nullable=False)
    feedback = db.Column(db.BOOLEAN(), nullable=False)

    def __repr__(self):
        return '<Feedback User %r>' % self.id

class FeedbackSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Feedback
        load_instance = True
        fields = ("id", "analisis_id", "feedback") # list filds which will be available for final user

class Reports(db.Model):
    __tablename__ = 'relatorios'
    id = db.Column(db.Integer, primary_key=True)
    report_name = db.Column(db.String(), nullable=False)
    analise_id = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Feedback User %r>' % self.id

class FeedbackSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Feedback
        load_instance = True
        fields = ("id", "analise_id", "report_name") # list filds which will be available for final user


