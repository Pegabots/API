# import datetime
# from app.models import db, ma
# from datetime import date
from flask import jsonify
import random
class BotProbability():
    def __init__(self):
        self.id = id
        self.total = ''
        self.friends = float(random.uniform(0, 1))
        self.network = float(random.uniform(0, 1))
        self.temporal = float(random.uniform(0, 1))
        self.sentiment = float(random.uniform(0, 1))

    def botProbability(self):
        return {
                'version': 'v0.1.0',
                'created_at' : '',
                'updated_at': '',
                'friends' : round(self.friends, 2),
                'sentiment': round(self.sentiment,2),
                'network': round(self.network,2),
                'temporal': round(self.temporal,2),
                'botProbability' : round(((self.friends + self.sentiment + self.network + self.temporal) / 4),2)
            }
