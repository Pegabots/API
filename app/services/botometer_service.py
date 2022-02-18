# from flask import jsonify
from app.models import db
from app.models.models import Analysis, AnalysisSchema, BotProbability
from app.services.twitter_handler import TwitterHandler
# from app.models.botprobability import BotProbability
from datetime import datetime


class BotometerService():
    def __init__(self):
        self.pegabot = BotProbability()  # module which proccess user data and tweets and gives a result
        self.twitter_handler = TwitterHandler()

    def catch(self, handle):
        try:
            '''
            1. verify if the analysis is valid (by same version of the model or cachetime still valid)
            1.1. if still valid, update times_served for the analysis row
            2. if not, find user on twitter, perform another analysis, save analyses to database
            3. return the new analysis to client
            '''
            user = self.findUserAnalysisByHandle(handle=handle)
            if 'id' in user:
                # return self.update_cache_times_served(user)
                return user
            else: # should perform the analysis
                response = self.twitter_handler.findByHandle(handle=handle) # check on twitter
                # return response
                if 'api_errors' not in response: # if finds the user on twitter performs the analysis and saves to the database
                    timeline = self.twitter_handler.getUserTimeline(response.twitter_id, num_tweets=1)
                    probability = self.pegabot.botProbability(handle)  # mock bot probability

                    # save analisis to database
                    analysis = Analysis(
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
                        twitter_created_at = Analysis.process_bind_param(value=response.twitter_created_at),
                        twitter_default_profile = response.twitter_default_profile,
                        twitter_profile_image = response.twitter_profile_image,
                        # twitter_withheld_in_countries = response.twitter_withheld_in_countries, # giving error, needs a refactor
                        total = probability.total,
                        friends = probability.friends,
                        temporal = probability.temporal,
                        network = probability.network,
                        sentiment = probability.sentiment,
                        cache_times_served = 0, #
                        # cache_validity =
                        pegabot_version = probability.pegabot_version,
                    )
                    db.session.add(analysis)
                    db.session.commit()
                    analysis_schema = AnalysisSchema()
                    return analysis_schema.dump(analysis)
        except Exception as e:
            raise
        else:
            return response


    def findUserAnalysisByHandle(self, handle):
        analysis_schema = AnalysisSchema()
        analysis = Analysis.query.filter_by(handle=handle).order_by(Analysis.id.desc()).first()
        self.update_times_served_count(analysis)
        return analysis_schema.dump(analysis)

    def update_times_served_count(self, analysis):
        if analysis is not None:
            analysis.cache_times_served += 1  # analysiss.query.filter_by(id=analysis.get('id')).update(dict(cache_times_served=analysis.cache_times_served))
            db.session.add(analysis)
            db.session.commit()

    def botProbability(self, handle):
        p = BotProbability()
        response = p.botProbability(handle=handle)
        return response