from clients.mastodon import Mastodon
from clients.twitter import Twitter
from model.tweets import Tweet

def main():
    twitter = Twitter()
    tweetJson = twitter.latest_tweet_content(281877818, 1604548832401838080)
    tweets = Tweet.parse_tweets_from_json(tweetJson)

    mastodon = Mastodon()
    for tweet in tweets:
        mastodon.post_toot(tweet.text)
    
    print("\nPosted " + len(tweets) + " new toots\n")


if __name__ == "__main__":
    main()
