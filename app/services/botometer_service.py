# from flask import jsonify
from app.models import db
from app.models.models import Analises, AnaliseSchema
from app.services.twitter_handler import TwitterHandler
from app.models.botprobability import BotProbability
from datetime import datetime


class BotometerService():
    def __init__(self):
        self.pegabot = BotProbability()  # module which proccess user data and tweets and gives a result
        self.twitter_handler = TwitterHandler()

    def catch(self, handle):
        try:
            '''
            1. verify if the analisis is valid (by same version of the model or cachetime still valid)
            1.1. if stills valid, update times_served for the analisis row
            2. if not, find user on twitter, perform another analisis, save analises to database
            3. return the new analisis to client
            '''
            user = self.findUserAnalisisByHandle(handle=handle)
            if 'twitter_handle' in user:
                # verify cache value
                # update do time served
                # if caches is 7_day
                # self.updateCacheTimesServed(user)
                return user
            else: # should perform the analisis
                response = self.twitter_handler.findByHandle(handle=handle) # check on twitter
                # return response
                if 'api_errors' not in response: # if finds the user on twitter performs the analisis and saves to the database
                    timeline = self.twitter_handler.getUserTimeline(response.twitter_id, num_tweets=1)
                    probability = self.pegabot.botProbability(handle)  # mock bot probability

                    # save analisis to database
                    analise = Analises(
                        handle = response.twitter_handle,
                        twitter_id = response.twitter_id,
                        twitter_handle = response.twitter_handle,
                        twitter_user_name = response.twitter_user_name,
                        twitter_is_protected = response.twitter_is_protected,
                        twitter_user_description = response.twitter_user_description,
                        twitter_followers_count = response.twitter_followers_count,
                        twitter_friends_count = response.twitter_friends_count,
                        twitter_location = response.twitter_location,
                        twitter_is_verified = response.twitter_is_verified,
                        twitter_lang = response.twitter_lang,
                        twitter_created_at = Analises.process_bind_param(value=response.twitter_created_at),
                        twitter_default_profile = response.twitter_default_profile,
                        twitter_profile_image = response.twitter_profile_image,
                        # twitter_withheld_in_countries = response.twitter_withheld_in_countries, # giving error, needs a refactor
                        total = probability.total,
                        friends = probability.friends,
                        temporal = probability.temporal,
                        network = probability.network,
                        sentiment = probability.sentiment,
                        cache_times_served = 1, #
                        # cache_validity =
                        pegabot_version = probability.pegabot_version,
                    )
                    db.session.add(analise)
                    db.session.commit()
                    analise_schema = AnaliseSchema()
                    return analise_schema.dump(analise)
        except Exception as e:
            raise
        else:
            return response

    def findUserAnalisisByHandle(self, handle):
        user = Analises.query.filter_by(handle=handle).order_by(Analises.id.desc()).first()
        analise_schema = AnaliseSchema()
        return analise_schema.dump(user)

    '''
        TO-DO: this code should be refactored. It's only working with records that are already on the database
    '''
    def update_times_served(self, user):
        pass
        # if user != '': #     needs to update times-served in order to know how many times each analisis has been used in a timeframe.
            # user.cache_times_served +=1
            # db.session.add(user)
            # db.session.commit()

    def updateCacheTimesServed(self, user):
        cache = user.get('cache_times_served')
        cache +=1
        # print(cache)
        user['cache_times_served'] = cache
        # print(user)
        # needs to update times-served in order to know how many times each analisis has been used in a timeframe.
        db.session.add(user)
        db.session.commit()

    def botProbability(self, handle):
        p = BotProbability()
        response = p.botProbability(handle=handle)
        return response