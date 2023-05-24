from clients.mastodon import Mastodon
from clients.twitter import Twitter
from model.tweets import Tweet
from model.users import User
import logging

def main():
    logging.basicConfig(
        filename="/var/log/twitter-mirror.log",
        level=logging.DEBUG,
        format='%(levelname)s:%(asctime)s:%(message)s'
    )

    twitter = Twitter()
    mastodon = Mastodon()
    users = User.load_users()
    for user in users:
        mostRecentTweet = user.most_recent_tweet()
        tweetJson = twitter.latest_tweet_content(user.twitter_id, mostRecentTweet)
        if tweetJson:
            tweets = Tweet.parse_tweets_from_json(tweetJson)

            for tweet in tweets:
                response = mastodon.post_toot(tweet, user)
                if response:
                    user.save_toot_data(response, tweet)
                    logging.info("Posted tweet: " + str(tweet))
            
            user.update_most_recent_tweet(tweetJson)


if __name__ == "__main__":
    main()
