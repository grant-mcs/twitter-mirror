import os
import requests

class Mastodon():

    def bearer_token(self):
        # export 'MASTODON_BEARER_TOKEN'='<your_bearer_token>'
        return os.environ.get("MASTODON_BEARER_TOKEN")

    def headers(self):
        return {
            "Authorization": f"Bearer " + self.bearer_token(),
            "User-Agent": "twitter-mirror"
        }

    def post_toot(self, text):
        params = {"status": text}
        response = requests.post("https://mstdn.ca/api/v1/statuses", headers=self.headers(), params=params)
        if response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(
                    response.status_code, response.text
                )
            )
        return response.json()
