import tweepy

from app import s
from easydict import EasyDict as edict
from datetime import datetime


class TwitterHandler():
    def __init__(self):
        self.twitter = {
            'TWITTER_API_KEY': s.os.environ.get("twitter_api_key"),
            'TWITTER_API_SECRET': s.os.environ.get("twitter_api_secret"),
            'TWITTER_API_TOKEN': s.os.environ.get("twitter_access_token"),
            'TWITTER_API_TOKEN_SECRET': s.os.environ.get("twitter_access_token_secret")
        }

        self.auth = tweepy.OAuthHandler(self.twitter.get('TWITTER_API_KEY'), self.twitter.get('TWITTER_API_SECRET'))

        # se não autenticar com o access token algumas funcionalidades da api
        # não ficam disponíveis. tipo verificar rate limits.
        self.auth.set_access_token(self.twitter.get('TWITTER_API_TOKEN'), self.twitter.get('TWITTER_API_TOKEN_SECRET'))

        # o objeto api é utilizado para realizar toda comunicação com a API do twitter.
        self.api = tweepy.API(self.auth)

    def api(self):
        return self.api

    def __show_twitter_credentials(self):
        for key in self.twitter:
            print(f' {key} - {self.twitter.get(key)}')

    # recuperando dados de um twitter user
    def findByHandle(self, handle):
        try:
            user = self.api.get_user(screen_name=handle)
            return edict({
                "twitter_id": user.id_str,
                "twitter_handle": str.lower(user.screen_name),
                "twitter_user_name": user.name,
                "twitter_is_protected": user.protected,
                "twitter_user_description": user.description,
                "twitter_followers_count": user.followers_count,
                "twitter_friends_count": user.friends_count,
                "twitter_location": user.location,
                # "createdAtOriginal": user.created_at,
                "twitter_created_at": datetime.strftime(user.created_at, '%Y-%m-%dT %H:%M:%S'),
                "twitter_is_verified": user.verified,
                "twitter_lang": user.lang,
                "twitter_default_profile": user.default_profile,
                "twitter_profile_image": user.profile_image_url,
                "twitter_withheld_in_countries": user.withheld_in_countries
            })
        except tweepy.HTTPException as e:
            print("Tweepy Error retrieving user: {}".format(e))
            return {'api_errors': e.api_errors, 'codes': e.api_codes, 'reason': e.response.reason, 'args': e.args}

    def searchTweets(self, q, num_tweets=10, result_type="recent"):
        tweets = self.api.search_tweets(
            q=q,
            count=num_tweets,
            result_type="recent"
        )

        return tweets

    def getUserTimeline(self, uid, num_tweets=100, exclude_replies=True):
        try:
            timeline = self.api.user_timeline(
                user_id = uid, 
                count = num_tweets,
                exclude_replies = exclude_replies
            )

            tweets = []
            for tweet in timeline:
                x = {
                    "tweet_author": tweet.author.screen_name,
                    "tweet_author_id_str": tweet.author.id_str,
                    "tweet_contributors": tweet.contributors,
                    "tweet_created_at": tweet.created_at,
                    "tweet_favorite_count": tweet.favorite_count,
                    "tweet_favorited": tweet.favorited,
                    "tweet_geo": tweet.geo,
                    "tweet_hashtags": str(list(map(lambda x: x['text'], tweet.entities['hashtags']))),
                    "tweet_id": tweet.id_str,
                    "tweet_id_str": tweet.id_str,
                    "tweet_is_retweet": tweet.retweeted,
                    "tweet_lang": tweet.lang,
                    "tweet_place": tweet.place,
                    "tweet_retweeted": tweet.is_quote_status,
                    "tweet_source": tweet.source,
                    "tweet_text": tweet.text
                }
                tweets.append(x)
            if(len(tweets) < 20):
                print("Tweepy Error getting user info. Too little information!")
                return {'api_errors': [{'code': '10', 'message:': 'Too little information available'}], 'codes': '10', 'reason': 'Too litle information available', 'args': 'Less than 20 tweets available.'}
            return (tweets)
        except tweepy.HTTPException as e:
            print("Tweepy Error retrieving timeline: {}".format(e))
            return {'api_errors': e.api_errors, 'codes': e.api_codes, 'reason': e.response.reason, 'args': e.args}

    def getUser(self, uid):
        try:
            user_data = self.api.get_user(user_id=uid)
            
            user = [{
                "created_at": user_data.created_at,
                "default_profile": user_data.default_profile,
                "description": user_data.description,
                "followers_count": user_data.followers_count,
                "friends_count": user_data.friends_count,
                "handle": user_data.screen_name,
                "lang": user_data.lang,
                "location": user_data.location,
                "name": user_data.name,
                "profile_image": user_data.profile_image_url,
                "twitter_id": uid,
                "twitter_is_protected": user_data.protected,
                "verified": user_data.verified,
                "withheld_in_countries": user_data.withheld_in_countries,
                "É Bot?": ''
            }]

            return(user)
        except tweepy.HTTPException as e:
            print("Tweepy Error retrieving timeline: {}".format(e))
            return {'api_errors': e.api_errors, 'codes': e.api_codes, 'reason': e.response.reason, 'args': e.args}

