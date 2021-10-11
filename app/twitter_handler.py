from app import s
import tweepy
from easydict import EasyDict as edict

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
        return self.api()

    def show(self):
        for key in self.twitter:
            print(f' {key} - {self.twitter.get(key)}')

    # recuperando dados de um twitter user
    def findByHandle(self, handle):
        # print(f'findByHandlehandle {handle}')
        try:
            user = self.api.get_user(screen_name=handle)
            return edict({
                'twitter_id': user.id,
                'twitter_id_str': user.id_str,
                'handle': user.screen_name,
                'name': user.name,
                'twitter_is_protected': user.protected,
                'description': user.description,
                'followers_count': user.followers_count,
                'friends_count': user.friends_count,
                'location': user.location,
                'created_at': user.created_at,
                'verified': user.verified,
                'lang': user.lang,
                'default_profile': user.default_profile,
                'profile_image': user.profile_image_url,
                'withheld_in_countries': user.withheld_in_countries
            })
        except tweepy.HTTPException as e:
            print("Tweepy Error retrieving user: {}".format(e))
            return {'api_errors': e.api_errors, 'codes': e.api_codes, 'reason': e.response.reason, 'args': e.args}


    def getUserTimeline(self, uid, num_tweets=100):
        try:
            timeline = tweepy.Cursor(self.api.user_timeline, user_id=uid, count=num_tweets).items(num_tweets)
            t = []
            for tweet in timeline:
                x = {
                    'tweet_id_str': tweet.id_str,
                    'tweet_id': tweet.id,
                    'tweet_author': tweet.author.screen_name,
                    'tweet_retweeted': tweet.retweeted,
                    'tweet_created_at': tweet.created_at,
                    'tweet_source': tweet.source,
                    'tweet_author_id_str': tweet.author.id_str,
                    'tweet_text': tweet.text,
                    'tweet_contributors': tweet.contributors,
                    'tweet_favorite_count': tweet.favorite_count,
                    'tweet_favorited': tweet.favorited,
                    'tweet_geo': tweet.geo,
                    'tweet_is_retweet': tweet.is_quote_status,
                    'tweet_lang': tweet.lang,
                    'tweet_place': tweet.place,
                    'tweet_hashtags': list(map(lambda x: x['text'], tweet.entities['hashtags']))
                }
                t.append(x)
            return (t)
        except tweepy.HTTPException as e:
            print("Tweepy Error retrieving timeline: {}".format(e))
            return {'api_errors': e.api_errors, 'codes': e.api_codes, 'reason': e.response.reason, 'args': e.args}

    def getUserAndTimeline(self, twitter_id):
        user = self.getUserTimeline(twitter_id)
        # if type(user)


# Loading variables for tweepy


