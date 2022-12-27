from clients.mastodon import Mastodon
from clients.twitter import Twitter
from model.tweets import Tweet
from model.users import User

def main():
    twitter = Twitter()
    user = User("281877818", "mstdn.ca", "2glaYCt_tzUSkBUVtvsLwrxL_P90kw8EKv1mc-6TV3Y")
    mostRecentTweet = user.most_recent_tweet()
    tweetJson = twitter.latest_tweet_content(user.twitter_id, mostRecentTweet)
    tweets = Tweet.parse_tweets_from_json(tweetJson)

    mastodon = Mastodon()
    for tweet in tweets:
        mastodon.post_toot(tweet, user)
    
    user.update_most_recent_tweet(tweetJson)

    print("\nPosted " + str(len(tweets)) + " new toots\n")


if __name__ == "__main__":
    main()
