class User():
    twitter_id: str

    def __init__(self, twitter_id: str):
        self.twitter_id = twitter_id

    def update_most_recent_tweet(self, json: dict):
        latest_tweet = json.get("meta").get("newest_id")
        if latest_tweet:
            f = open("data/" + self.twitter_id + ".latest", "w")
            f.write(latest_tweet)
            f.close()

    def most_recent_tweet(self):
        f = open("data/" + self.twitter_id + ".latest", "r")
        mostRecentTweet = f.read().strip()
        f.close()
        return mostRecentTweet
