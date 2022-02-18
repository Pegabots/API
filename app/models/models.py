from app.models import db, ma
from datetime import datetime
from easydict import EasyDict as edict



class Analysis(db.Model):
    __tablename__ = 'analysis'
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

class AnalysisSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Analysis
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
        fields = ("id", "analysis_id", "feedback") # list filds which will be available for final user

class Reports(db.Model):
    __tablename__ = 'reports'
    id = db.Column(db.Integer, primary_key=True)
    report_name = db.Column(db.String(), nullable=False)
    analysis_id = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Feedback User %r>' % self.id

class FeedbackSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Feedback
        load_instance = True
        fields = ("id", "analysis_id", "report_name") # list filds which will be available for final user

class BotProbability():
    def __init__(self):
        self.id = id
        self.total = 0
        self.friends = 0
        self.network = 0
        self.temporal = 0
        self.sentiment = 0

    def mockProbability(self):
        import random
        self.friends = float(random.uniform(0, 1)) *100
        self.network = float(random.uniform(0, 1)) *100
        self.temporal = float(random.uniform(0, 1)) *100
        self.sentiment = float(random.uniform(0, 1)) *100
        self.total = round((self.friends + self.sentiment + self.network + self.temporal) / 4, 2)

    def botProbability(self, handle, twitterTimeline=None, twitterUserData=None):
        self.mockProbability()
        # sleep.time(15)
        return edict({
            'pegabot_version': 'version-1.0',
            'handle': handle,
            'total': self.total,
            'friends': round(self.friends, 2),
            'sentiment': round(self.sentiment, 2),
            'network': round(self.network, 2),
            'temporal': round(self.temporal, 2)
        })

