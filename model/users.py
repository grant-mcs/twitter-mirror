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
            userProperties = line.split()
            if len(userProperties) == 3:
                users.append(User(userProperties[0], userProperties[1], userProperties[2]))

        f.close()
        return users

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
