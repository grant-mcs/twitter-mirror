import os
import requests
from urllib.parse import urlparse

class Mastodon():

    def bearer_token(self):
        # export 'MASTODON_BEARER_TOKEN'='<your_bearer_token>'
        return os.environ.get("MASTODON_BEARER_TOKEN")

    def headers(self):
        return {
            "Authorization": f"Bearer " + self.bearer_token(),
            "User-Agent": "twitter-mirror"
        }

    def post_toot(self, tweet):
        mediaIds = []
        for item in tweet.media:
            # Possible types are 'photo', 'animated_gif', and 'video'
            itemType = item.get("type")
            if itemType == "photo" or itemType == "animated_gif":
                mediaId = self.upload_media(item)
                if mediaId:
                    mediaIds.append(mediaId)

        params = {"status": tweet.text}
        if mediaIds:
            params["media_ids[]"] = ','.join(mediaIds)

        response = requests.post("https://mstdn.ca/api/v1/statuses", headers=self.headers(), params=params)
        if response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(
                    response.status_code, response.text
                )
            )
        return response.json()

    def upload_media(self, item: dict):
        mediaContent = requests.get(item.get("url")).content
        if not mediaContent:
            print("\nError: Unable to download " + item.get("type") + " from " + item.get("url"))
            return None

        parsedUrl = urlparse(item.get("url"))
        files = {
            'file': (parsedUrl.path, mediaContent),
        }
        response = requests.request("POST", "https://mstdn.ca/api/v2/media", headers=self.headers(), files=files)
        json = response.json()
        return json.get("id")

