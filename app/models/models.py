import pickle
import pandas as pd

from app.models import db, ma
from datetime import datetime
from easydict import EasyDict as edict

#Importa a classe de preparação de dados
from app.models.prepare_data import MLTools

class Analises(db.Model):
    __tablename__ = 'analises'
    id = db.Column(db.Integer, primary_key=True)
    handle = db.Column(db.String(80), nullable=False)
    total = db.Column(db.String(120), nullable=True)
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
            try:
                return datetime.strptime(value, '%Y-%m-%dT %H:%M:%S')
            except:
                return datetime.strptime(value, "%a %b %d %H:%M:%S %z %Y")
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

class BotProbability():
    def __init__(self):
        self.id = id
        self.total = 0
        self.friends = 0
        self.network = 0
        self.temporal = 0
        self.sentiment = 0

    def predict(self, users_data, timeline_data, path_input_model="app/models/pegabot-model-01.model"):
        
        #Carrega o modelo do disco
        loaded_model = pickle.load(open(path_input_model, 'rb'))

        #Prepara os dados do usuário para a aplicação do modelo
        tools = MLTools()
        x_data = tools.prepare_data(users_data, timeline_data)

        #Aplica o modelo para predição e retorna a predição {[0] Não é Bot, [1] é Bot}
        #predicted = loaded_model.predict(x_data)

        #Aplica o modelo para retorno dentro da faixa de [0, 1] para as classes [não bot | bot]
        predicted_proba = loaded_model.predict_proba(x_data)

        return predicted_proba

    def botProbability(self, handle, twitterTimeline, twitterUserData):
        try:
            df_timeline = pd.DataFrame.from_dict(twitterTimeline)
            df_user_data = pd.DataFrame.from_dict(twitterUserData)
            analise = self.predict(df_user_data, df_timeline)
            self.total = round(analise[0][1]*100, 2)
        except:
            self.total = -1

        return edict({
            'pegabot_version': 'version-1.0',
            'handle': handle,
            'total': self.total
        })
