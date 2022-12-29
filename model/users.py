import os
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
        f = open("data/users", "r")
        users = []
        for line in f:
            # Users can be commented out with a '#'
            normalizedLine = line.strip()
            if normalizedLine.startswith('#') or len(normalizedLine) == 0:
                continue

            userProperties = line.split()
            if len(userProperties) != 3:
                print(f"\nError: Invalid format for user configuration. Each user must have 3 properties separated by a space (Twitter ID, Mastodon instance, Mastodon access token): {line}\n")
                continue

            users.append(User(userProperties[0], userProperties[1], userProperties[2]))

        f.close()
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

        f = open("data/" + self.twitter_id + ".toots", "a")
        f.write(f"{tootId} {tweet.id}\n")
        f.close()

        return True

    def toot_id_for_tweet(self, tweet: Tweet):
        filename = f"data/{self.twitter_id}.toots"
        if not os.path.exists(filename):
            return None

        f = open(filename, "r")
        for line in f:
            # Ignore empty lines
            if len(line.strip()) == 0:
                continue

            tootMapping = line.split()
            if len(tootMapping) != 2:
                print(f"\nError: Invalid format for toot mapping. Each mapping must have 2 properties separated by a space (tweet ID, toot ID): {line}\n")
                continue

            if tootMapping[1] == tweet.id:
                return tootMapping[0]

        f.close()
        return None

