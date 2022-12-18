import json

from clients.twitter import Twitter

def main():
    twitter = Twitter()
    tweets = twitter.latest_tweet_content(281877818, 1604029197126537217)

    print(json.dumps(tweets, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
