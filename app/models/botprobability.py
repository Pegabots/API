# from app.models import db, ma, migrate
from easydict import EasyDict as edict
import random


class BotProbability():
    def __init__(self):
        self.id = id
        self.total = 0
        self.friends = 0
        self.network = 0
        self.temporal = 0
        self.sentiment = 0

    def mockProbability(self):
        self.friends = float(random.uniform(0, 1)) *100
        self.network = float(random.uniform(0, 1)) *100
        self.temporal = float(random.uniform(0, 1)) *100
        self.sentiment = float(random.uniform(0, 1)) *100
        self.total = round((self.friends + self.sentiment + self.network + self.temporal) / 4, 2)

    def botProbability(self, handle, twitterTimeline=None, twitterUserData=None):
        self.mockProbability()
        return edict({
            'pegabot_version': 'version-1.0',
            'handle': handle,
            'total': self.total,
            'friends': round(self.friends, 2),
            'sentiment': round(self.sentiment, 2),
            'network': round(self.network, 2),
            'temporal': round(self.temporal, 2)
        })
