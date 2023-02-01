import os as _os
import dotenv as _dotenv
import time as _time
import tweepy as _tweepy
import services as _services
import unsplash as _unsplash

_dotenv.load_dotenv()

API_KEY = _os.environ["TWITTER_API_KEY"]
SECRET_KEY = _os.environ["TWITTER_API_SECRET"]
ACCESS_TOKEN = _os.environ["TWITTER_ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = _os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

def _get_twitter_api():
    auth = _tweepy.OAuthHandler(API_KEY,SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    twitter_api = _tweepy.API(
        auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True
        )
    return twitter_api

def _write_tweet():
    tweet = _services.get_tweet()
    twitter_api = _get_twitter_api()
    twitter_api.update_status(tweet)
    
def _post_image():
    _unsplash.download_image()
    #tweet = _services.get_tweet()
    twitter_api = _get_twitter_api()
    twitter_api.update_with_media("picture.jpg")
    #twitter_api.update_with_media("picture.jpg",tweet)
    
def run():
    #count = 0
    #while True:
        # if count >=5:
        #     break        
        _write_tweet()
        _time.sleep(20)        
        _post_image()
        # count+=1
        #_time.sleep(86390)
        
if __name__ == "__main__":
    run()
