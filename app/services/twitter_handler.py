
from typing import Dict
from loguru import logger as log
from scrapfly import ScrapeConfig, ScrapflyClient
from datetime import datetime

import calendar
import http.client
import asyncio
import json
import re

class TwitterHandler():
    def __init__(self):
        self.SCRAPFLY = ScrapflyClient(key="scp-live-608f1f81a859476da561076fa6147b8c")
        self.BASE_CONFIG = {
            # Twitter.com requires Anti Scraping Protection bypass feature.
            # for more: https://scrapfly.io/docs/scrape-api/anti-scraping-protection
            "asp": True,
            # Twitter.com is javascript-powered web application so it requires
            # headless browsers for scraping
            "render_js": True,
            # "country": "CA",  # set prefered country here, for example Canada
        }

    def api(self):
        return self.api
    
    async def _scrape_twitter_app(self, url: str, _retries: int = 0, **scrape_config) -> Dict:
        """Scrape Twitter page and scroll to the end of the page if possible"""
        if not _retries:
            log.info("scraping {}", url)
        else:
            log.info("retrying {}/2 {}", _retries, url)
        result = await self.SCRAPFLY.async_scrape(
            ScrapeConfig(url, auto_scroll=True, **scrape_config, **self.BASE_CONFIG)
        )
        if "Something went wrong, but" in result.content:
            if _retries > 2:
                raise Exception("Twitter web app crashed too many times")
            return await self._scrape_twitter_app(url, _retries=_retries + 1, **scrape_config)
        return result

    async def scrape_profile(self, url: str) -> Dict:
        """
        Scrapes Twitter user profile page e.g.:
        https://twitter.com/scrapfly_dev
        returns user data and latest tweets
        """
        result = await self._scrape_twitter_app(url, wait_for_selector="[data-testid='tweet']")
        # capture background requests and extract ones that contain user data
        # and their latest tweets
        _xhr_calls = result.scrape_result["browser_data"]["xhr_call"]
        user_calls = [f for f in _xhr_calls if "UserBy" in f["url"]]

        tweet_paging_calls = [f for f in _xhr_calls if "UserTweets" in f["url"]]
        return {
            "users": user_calls,
            "tweets": tweet_paging_calls
        }

    async def scrape_tweet(self, url: str) -> Dict:
        """
        Scrape a single tweet page for Tweet thread e.g.:
        https://twitter.com/Scrapfly_dev/status/1667013143904567296
        Return parent tweet, reply tweets and recommended tweets
        """
        result = await self._scrape_twitter_app(url, wait_for_selector="[data-testid='tweet']")
        # capture background requests and extract ones that request Tweet data
        _xhr_calls = result.scrape_result["browser_data"]["xhr_call"]
        tweet_call = [f for f in _xhr_calls if "TweetResultByRestId" in f["url"]]
        return tweet_call

    def scrape_tweets(self, username: str):
        conn = http.client.HTTPSConnection("twitter-api45.p.rapidapi.com")

        headers = {
            'X-RapidAPI-Key': "0aab88c81dmsh895e703bc15092fp1314b3jsn2e5c3520e9c2",
            'X-RapidAPI-Host': "twitter-api45.p.rapidapi.com"
        }

        req = "/timeline.php?screenname="+username
        conn.request("GET", req, headers=headers)

        res = conn.getresponse()
        data = res.read()
        dados = data.decode()
        return dados

    def e_retweet(self, tweet):
        try:
            if(tweet['retweeted']['id']): return False
        except: 
            return True

    def reply_to(self, tweet):
        try:
            if(tweet['author']): return 0
        except:
            return tweet['conversation_id']


    def is_quote(self, tweet):
        try:
            if(tweet['quoted']): return True
        except:
            return False
    
    def retweeted(self, tweet):
        try:
            if(t['timeline'][0]['retweeted']): return True
        except:
            return False

    def get_source(self, handle, tweet):
        link_tweet = "https://twitter.com/"+handle+"/status/"+tweet['tweet_id']
        dados_tweet = asyncio.run(self.scrape_tweet(link_tweet))
        info_tweet = json.loads(dados_tweet[0]['response']['body'])
        s = info_tweet['data']['tweetResult']['result']['source']
        pattern_source = r'>\w+\s*\w*\s*\w*\s*\w*\s*\w*<'
        source = re.search(pattern_source, s).group(0)
        source = source[1:-1]
        return source

    def getUserTimeline(self, handle, num_tweets=20):
        #try:
        timeline = json.loads(self.scrape_tweets(handle))
        tweets = []
        for tweet in timeline['timeline']:

            #Atributo de Publicação
            in_reply_to_status_id = self.reply_to(tweet)

            created_at = tweet['created_at'].split()
            month = list(calendar.month_abbr).index(created_at[1])
            created_at = datetime.strptime(created_at[5]+'-'+str(month)+'-'+created_at[2]+' '+created_at[3]+created_at[4], '%Y-%m-%d %H:%M:%S%z')

            quoted_status_text = ''
            if(self.is_quote == True):
                quoted_status_text = tweet['quoted']['text']

            #Atributo de Publicação
            retweet_count = tweet['retweets']

            #Atributo de Publicação
            text = tweet['text']

            pattern_hashtags = r"#\w+"
            pattern_users = r"@\w+"

            #Atributo de Publicação
            text_hashtags = re.findall(pattern_hashtags, text)

            #Atributo de Publicação
            text_user_mentions = re.findall(pattern_users, text)

            #Atributo de Publicação
            source = self.get_source(handle, tweet)

            x = {
                "tweet_author_id": tweet['author']['rest_id'],
                "tweet_author": tweet['author']['screen_name'],
                "tweet_created_at": str(created_at),
                "tweet_favorite_count": tweet['favorites'],
                "tweet_hashtags": str(text_hashtags),
                "tweet_retweet_count": retweet_count,
                "tweet_is_retweet": self.e_retweet(tweet),
                "tweet_is_quote": self.is_quote(tweet),
                "tweet_source": source,
                "tweet_retweeted": self.retweeted(tweet),
                "in_reply_to_status_id": str(in_reply_to_status_id),
                "quoted_status_text": quoted_status_text,
                "text_user_mentions": text_user_mentions,
                "tweet_text": text
            }
            tweets.append(x)

            if(len(tweets)>=num_tweets):
                return (tweets)
        return (tweets)
        #except:
        #    return False

    def getUser(self, handle):
        try:
            perfil = asyncio.run(self.scrape_profile("https://twitter.com/"+handle))
            perfil = perfil['users'][0]['response']['body']
            perfil = json.loads(perfil)
            
            created_at = perfil['data']['user']['result']['legacy']['created_at']
            created_at = created_at.split()
            month = list(calendar.month_abbr).index(created_at[1])
            created_at = datetime.strptime(created_at[5]+'-'+str(month)+'-'+created_at[2]+' '+created_at[3]+created_at[4], '%Y-%m-%d %H:%M:%S%z')

            user = [{
                "id": perfil['data']['user']['result']['rest_id'],
                "created_at": str(created_at),
                "description": perfil['data']['user']['result']['legacy']['description'],
                "followers_count": perfil['data']['user']['result']['legacy']['followers_count'],
                "friends_count": perfil['data']['user']['result']['legacy']['friends_count'],
                "statuses_count": perfil['data']['user']['result']['legacy']['statuses_count'],
                "favourites_count": perfil['data']['user']['result']['legacy']['favourites_count'],
                "handle": perfil['data']['user']['result']['legacy']['screen_name'],
                "name": perfil['data']['user']['result']['legacy']['name'],
                "verified": perfil['data']['user']['result']['legacy']['verified'],
                "É Bot?": ''
            }]

            return(user)
        except:
            return False

