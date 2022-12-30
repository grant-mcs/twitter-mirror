import os
import requests

class Twitter():

    def get_access_token(self):
        data = {'grant_type': 'client_credentials'}
        apiKey = os.environ.get("API_KEY")
        apiSecret = os.environ.get("API_SECRET")
        response = requests.post('https://api.twitter.com/oauth2/token', data=data, auth=(apiKey, apiSecret))
        if response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(
                    response.status_code, response.text
                )
            )
        json = response.json()
        return json.get("access_token")

    def headers(self):
        return {
            "Authorization": f"Bearer " + self.get_access_token(),
            "User-Agent": "twitter-mirror"
        }

    def tweet_url_for_user(self, user_id: str):
        return "https://api.twitter.com/2/users/{}/tweets".format(user_id)
    
    def get_tweets(self, user_id: str, params: dict):
        url = self.tweet_url_for_user(user_id)
        response = requests.request("GET", url, headers=self.headers(), params=params)
        if response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(
                    response.status_code, response.text
                )
            )
        return response.json()

    def latest_tweet_content(self, user_id: str, since_id: str):
        expansions = "referenced_tweets.id,referenced_tweets.id.author_id,attachments.media_keys"
        tweetFields = "created_at"
        mediaFields = "url"
        return self.get_tweets(user_id, {"since_id": since_id, "expansions": expansions, "tweet.fields": tweetFields, "media.fields": mediaFields})
