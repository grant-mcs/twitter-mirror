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
