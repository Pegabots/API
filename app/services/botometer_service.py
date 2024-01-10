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
            previous_user = 0
            previous_user = self.findUserAnalisisByHandle(handle=handle)
            user = self.twitter_handler.getUser(handle=handle) # check on twitter

            if 'id' in previous_user:
                if user==False: return previous_user
                return user
            else: # should perform the analisis
                
                if user != False: # if finds the user on twitter performs the analisis and saves to the database
                    timeline = self.twitter_handler.getUserTimeline(handle)
                   
                    if timeline == False:
                        return False
                    probability = self.pegabot.botProbability(handle, timeline, user)  # bot probability
                    print(probability)
                    user = user[0]
                    # save analisis to database
                    analise = Analises(
                        # User
                        twitter_id = user["id"],
                        handle = user["handle"],
                        twitter_handle = user["handle"],
                        twitter_user_name = user["name"],
                        twitter_user_description = user["description"],
                        twitter_created_at = Analises.process_bind_param(value=user["created_at"]),
                        twitter_followers_count = user["followers_count"],
                        twitter_friends_count = user["friends_count"],
                        twitter_statuses_count = user["statuses_count"],
                        twitter_favourites_count = user["favourites_count"],
                        twitter_is_verified = user["verified"],
                        total = probability.total,
                        cache_times_served = 0, #
                        cache_validity = datetime.today() + timedelta(30),
                        pegabot_version = probability.pegabot_version,
                    )
                    db.session.add(analise)
                    db.session.commit()
                    analise_schema = AnaliseSchema()
                    return analise_schema.dump(analise)
                else:
                    return user
        except Exception as e:
            raise


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
                user = self.twitter_handler.findByHandle(handle=handle) # check on twitter
                # return user
                if 'api_errors' not in user: # if finds the user on twitter performs the analisis and saves to the database
                    timeline = self.twitter_handler.getUserTimeline(user.twitter_id)
                    if 'api_errors' not in timeline:
                        user = self.twitter_handler.getUser(user.twitter_id)
                        probability = self.pegabot.botProbability(handle, timeline, user)  # bot probability
                        analise.total = probability.total
                        analise.cache_validity = datetime.today() + timedelta(30)
                        analise.updated_at = datetime.today()

                db.session.add(analise)
                db.session.commit()

    def botProbability(self, handle, user, timeline):
        p = BotProbability()
        user = p.botProbability(handle=handle, twitterTimeline=timeline, twitterUserData=user)
        return user