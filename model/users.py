import os
from clients.db import DB
from model.tweets import Tweet


class User():
    twitter_id: str
    mastodon_instance: str
    mastodon_token: str

    def __init__(self, twitter_id: str, mastodon_instance: str, mastodon_token: str):
        self.twitter_id = twitter_id
        self.mastodon_instance = mastodon_instance
        self.mastodon_token = mastodon_token

    @staticmethod
    def load_users():
        db = DB.connect()
        userData = db.query("SELECT twitter_id, mastodon_instance, mastodon_token FROM users")
        users = []
        for u in userData:
            users.append(User(u[0], u[1], u[2]))

        return users

    def update_most_recent_tweet(self, json: dict):
        meta = json.get("meta")
        if not meta:
            print(f"\nError: no 'meta' found in Twitter results\n")
            return

        latest_tweet = meta.get("newest_id")
        if latest_tweet:
            f = open("data/" + self.twitter_id + ".latest", "w")
            f.write(latest_tweet)
            f.close()

    def most_recent_tweet(self):
        f = open("data/" + self.twitter_id + ".latest", "r")
        mostRecentTweet = f.read().strip()
        f.close()
        return mostRecentTweet
    
    def save_toot_data(self, tootData: dict, tweet: Tweet):
        tootId = tootData.get("id")
        if not tootId:
            return False

        # If this tweet has already been posted, nothing more to do
        if self.toot_id_for_tweet(tweet):
            return True

        db = DB.connect()
        result = db.execute("INSERT INTO toot_map (toot_id, tweet_id) VALUES (?, ?)", [tootId, tweet.id])

        return result > 0

    def toot_id_for_tweet(self, tweet: Tweet):
        db = DB.connect()
        return db.query_value("SELECT toot_id FROM toot_map WHERE tweet_id = ?", [tweet.id])

