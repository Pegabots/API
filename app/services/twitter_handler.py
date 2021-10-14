from app import s
import tweepy
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


    def getUserTimeline(self, uid, num_tweets=100):
        try:
            timeline = tweepy.Cursor(self.api.user_timeline, user_id=uid, count=num_tweets).items(num_tweets)
            tweets = []
            for tweet in timeline:
                x = {
                    "tweetId": tweet.id_str,
                    "tweetAuthor": tweet.author.screen_name,
                    "tweetIsRetweeted": tweet.retweeted,
                    "tweetCreated_at": tweet.created_at,
                    "tweetSource": tweet.source,
                    "tweetAuthorId": tweet.author.id_str,
                    "tweetText": tweet.text,
                    "tweetContributors": tweet.contributors,
                    "tweetFavoriteCount": tweet.favorite_count,
                    "tweetIsFavorited": tweet.favorited,
                    "tweetGeo": tweet.geo,
                    "tweetIsRetweet": tweet.is_quote_status,
                    "tweetLang": tweet.lang,
                    "tweetPlace": tweet.place,
                    "tweetHashtags": list(map(lambda x: x['text'], tweet.entities['hashtags']))
                }
                tweets.append(x)
            return (tweets)
        except tweepy.HTTPException as e:
            print("Tweepy Error retrieving timeline: {}".format(e))
            return {'api_errors': e.api_errors, 'codes': e.api_codes, 'reason': e.response.reason, 'args': e.args}

    def getUserAndTimeline(self, twitter_id):
        user = self.getUserTimeline(twitter_id)
        # if type(user)


# Loading variables for tweepy


