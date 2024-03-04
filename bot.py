import tweepy
import os
from dotenv import load_dotenv
load_dotenv()


access_token = os.getenv("BEARER_TOKEN")



auth = tweepy.OAuth2BearerHandler(bearer_token=access_token)
api = tweepy.API(auth)


keywords = ["keyword1", "keyword2", "hashtag1", "hashtag2"]

# Search for tweets containing the keywords or hashtags
for keyword in keywords:
    tweets = api.search_tweets(q=keyword, count=10)
    for tweet in tweets:
        # Post a reply to the tweet
        # api.update_status(f"@{tweet.user.screen_name} Your tweet contains the keyword/hashtag: {keyword}", in_reply_to_status_id=tweet.id)/
        print(tweet)