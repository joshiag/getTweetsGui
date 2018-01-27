#twitter stream api
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import time
import pandas as pd


def twitter_strm(x,y):

    consumer_key = 'n7Dgt6OqBBG9Mq07eVxQIVTl1'
    consumer_secret = 'IcmNCzQRbVlkb0g2ZKPUWCoxUnPNW08vcQ9ANRS06zBToE1ejG'
    access_token = '896952129687920640-Qhs0qiueDkW82QnyshgNQmilHdRCWDm'
    access_secret = 'za1MxgR0hOFqHaAbugXKN5XUMMlGShINKgZX8BsWxc3Wj'

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)


    results = []
    
    try:
            #Get the first 5000 items based on the search query
        for tweet in tweepy.Cursor(api.search, q=x).items(y):
            results.append(tweet)
            
    except:
            # Verify the number of items returned
            print len(results)

#    print "DEBUG"
    tweets_df = pd.DataFrame(vars(results[i]) for i in range (len(results)))
    tweets_df['year'] = tweets_df.created_at.dt.year
    tweets_df['month']=tweets_df.created_at.dt.month
    tweets_df['day']=tweets_df.created_at.dt.day
    
    # print 'got the dataframe'


        #   names of columns in tweets_df
        #
        #   Index([u'_api', u'_json', u'author', u'contributors', u'coordinates',
        #  u'created_at', u'entities', u'favorite_count', u'favorited', u'geo',
        #  u'id', u'id_str', u'in_reply_to_screen_name', u'in_reply_to_status_id',
        #  u'in_reply_to_status_id_str', u'in_reply_to_user_id',
        #  u'in_reply_to_user_id_str', u'is_quote_status', u'lang', u'metadata',
        #  u'place', u'possibly_sensitive', u'quoted_status', u'quoted_status_id',
        #  u'quoted_status_id_str', u'retweet_count', u'retweeted',
        #  u'retweeted_status', u'source', u'source_url', u'text', u'truncated',
        #  u'user'],
        # dtype='object')

    return tweets_df
