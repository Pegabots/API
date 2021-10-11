from app import app
from flask import jsonify, request
from app.models.analises import Analises, AnaliseSchema
from app.twitter_handler import TwitterHandler
from app.models.botprobability import BotProbability

class BotometerService():
    def __init__(self):
            self.pegabot = BotProbability() # module which proccess user data and tweets and gives a result
            self.twitter_handler = TwitterHandler()

    def catch_service(self, handle):
        try:
            '''
            1. verify if the analisis is valid (by same version of the model or cachetime still valid)
            1.1. if stills valid, update times_served for the analisis row
            2. if not, find user on twitter, perform another analisis, save analises to database
            3. return the new analisis to client
            '''

            response = self.twitter_handler.findByHandle(handle)
            if 'api_errors' not in response:
                timeline = self.twitter_handler.getUserTimeline(response.twitter_id_str, num_tweets=1)
                probability = self.pegabot.botProbability() # receives tweets and user profile data
                return jsonify({'user': response,
                         'pebabot': probability,
                         'timeline': timeline
                         })
        except Exception as e:
            raise
        else:
            return response


    def findUserAnalisisByHandle(self, handle):
        user = Analises.query.filter_by(handle=handle).first()
        # user = Analises.query.get(1) # in case wants to find by database key
        print(f'{user}')
        analise_schema = AnaliseSchema()
        return analise_schema.dump(user)

