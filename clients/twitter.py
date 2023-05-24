import os
import requests
import logging

class Twitter():

    def get_access_token(self):
        data = {'grant_type': 'client_credentials'}
        apiKey = os.environ.get("API_KEY")
        apiSecret = os.environ.get("API_SECRET")
        response = requests.post('https://api.twitter.com/oauth2/token', data=data, auth=(apiKey, apiSecret))
        if response.status_code != 200:
            logging.warning(f"Failed to get auth token from Twitter (status: {response.status_code}): {response.text}")
            return None

        json = response.json()
        return json.get("access_token")

    def headers(self):
        token = self.get_access_token()
        if token:
            return {
                "Authorization": f"Bearer " + token,
                "User-Agent": "twitter-mirror"
            }
        return None

    def tweet_url_for_user(self, user_id: str):
        return "https://api.twitter.com/2/users/{}/tweets".format(user_id)
    
    def get_tweets(self, user_id: str, params: dict):
        url = self.tweet_url_for_user(user_id)
        headers = self.headers()
        if headers:
            response = requests.request("GET", url, headers=headers, params=params)
            if response.status_code != 200:
                logging.warning(f"Failed to get list of tweets from Twitter (status: {response.status_code}): {response.text}")
                return None

            return response.json()

        return None

    def latest_tweet_content(self, user_id: str, since_id: str):
        expansions = "referenced_tweets.id,referenced_tweets.id.author_id,attachments.media_keys"
        tweetFields = "created_at"
        mediaFields = "url"
        return self.get_tweets(user_id, {"since_id": since_id, "expansions": expansions, "tweet.fields": tweetFields, "media.fields": mediaFields})
