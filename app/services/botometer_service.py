from datetime import datetime, date, timedelta

from app.models import db
from app.models.models import Analises, AnaliseSchema, BotProbability
from app.services.twitter_handler import TwitterHandler

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
            response = self.twitter_handler.findByHandle(handle=handle) # check on twitter
            print(response)
            if 'id' in user:
                if 'api_errors' not in response: return user
                return response
            else: # should perform the analisis
                
                if 'api_errors' not in response: # if finds the user on twitter performs the analisis and saves to the database
                    timeline = self.twitter_handler.getUserTimeline(response.twitter_id)
                    user = self.twitter_handler.getUser(response.twitter_id)
                    
                    if 'api_errors' in timeline: 
                        if(date.today() == user[0]['created_at'].date()):
                            print("Account created today")
                            return {'api_errors': [{'code': '11', 'message:': 'Account created today.'}], 'codes': '11', 'reason': 'Too litle information available', 'args': 'Account created today.'}
                        return timeline
                    probability = self.pegabot.botProbability(handle, timeline, user)  # bot probability

                    # save analisis to database
                    analise = Analises(
                        # User
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
                        friends = 0,#probability.friends,
                        temporal = 0,#probability.temporal,
                        network = 0,#probability.network,
                        sentiment = 0,#probability.sentiment,
                        cache_times_served = 0, #
                        cache_validity = datetime.today() + timedelta(30),
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
        analise_schema = AnaliseSchema()
        analise = Analises.query.filter_by(handle=handle.lower()).order_by(Analises.id.desc()).first()

        self.check_cache_validity(analise, handle)
        self.update_times_served_count(analise)
        return analise_schema.dump(analise)

    def update_times_served_count(self, analise):
        if analise is not None:
            analise.cache_times_served += 1  # Analises.query.filter_by(id=analise.get('id')).update(dict(cache_times_served=analise.cache_times_served))
            db.session.add(analise)
            db.session.commit()
    
    def check_cache_validity(self, analise, handle):
        if analise is not None:
            if((datetime.today() - analise.cache_validity).days > 0):                
                response = self.twitter_handler.findByHandle(handle=handle) # check on twitter
                # return response
                if 'api_errors' not in response: # if finds the user on twitter performs the analisis and saves to the database
                    timeline = self.twitter_handler.getUserTimeline(response.twitter_id)
                    if 'api_errors' not in timeline:
                        user = self.twitter_handler.getUser(response.twitter_id)
                        probability = self.pegabot.botProbability(handle, timeline, user)  # bot probability
                        analise.total = probability.total
                        analise.cache_validity = datetime.today() + timedelta(30)
                        analise.updated_at = datetime.today()

                db.session.add(analise)
                db.session.commit()

    def botProbability(self, handle, user, timeline):
        p = BotProbability()
        response = p.botProbability(handle=handle, twitterTimeline=timeline, twitterUserData=user)
        return response