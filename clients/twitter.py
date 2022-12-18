import os
import requests

class Twitter():

    def bearer_token(self):
        # export 'BEARER_TOKEN'='<your_bearer_token>'
        return os.environ.get("BEARER_TOKEN")

    def headers(self):
        return {
            "Authorization": f"Bearer " + self.bearer_token(),
            "User-Agent": "v2UserTweetsPython"
        }

    def tweet_url_for_user(self, user_id):
        return "https://api.twitter.com/2/users/{}/tweets".format(user_id)
    
    def get_tweets(self, url, params):
        response = requests.request("GET", url, headers=self.headers(), params=params)
        print(response.status_code)
        if response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(
                    response.status_code, response.text
                )
            )
        return response.json()

    def latest_tweet_content(self, user_id, since_id):
        url = self.tweet_url_for_user(user_id)
        return self.get_tweets(url, {"since_id": since_id, "expansions": "referenced_tweets.id"})
