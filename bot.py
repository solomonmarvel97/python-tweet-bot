import tweepy
import time
from keyfile import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

created_file = 'last_seen.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('tweets', flush=True)

    last_seen_id = retrieve_last_seen_id(created_file)

    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, created_file)
        if '#whatsup' in mention.full_text.lower():
            print('i just #geek!', flush=True)
            
            print('replying ...', flush=True)
            api.update_status('@' + mention.user.screen_name +
                    '#whatsup my friend!', mention.id)

while True:
    reply_to_tweets()
    time.sleep(10)
