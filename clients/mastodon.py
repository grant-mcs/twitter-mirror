import os
import requests
from urllib.parse import urlparse

from model.users import User

class Mastodon():

    def headers(self, user: User):
        return {
            "Authorization": f"Bearer {user.mastodon_token}",
            "User-Agent": "twitter-mirror"
        }

    def post_toot(self, tweet, user):
        mediaIds = []
        for item in tweet.media:
            # Possible types are 'photo', 'animated_gif', and 'video'
            itemType = item.get("type")
            if itemType == "photo" or itemType == "animated_gif":
                mediaId = self.upload_media(item, user)
                if mediaId:
                    mediaIds.append(mediaId)

        params = {"status": tweet.text}
        if mediaIds:
            params["media_ids[]"] = ','.join(mediaIds)

        url = f"https://{user.mastodon_instance}/api/v1/statuses"
        response = requests.post(url, headers=self.headers(user), params=params)
        if response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(
                    response.status_code, response.text
                )
            )
        return response.json()

    def upload_media(self, item: dict, user: User):
        url = item.get("url")
        if not url:
            # Twitter sometimes provides media without a URL
            return None

        mediaContent = requests.get(url).content
        if not mediaContent:
            print("\nError: Unable to download " + item.get("type") + " from " + url)
            return None

        parsedUrl = urlparse(url)
        if not parsedUrl.path:
            print("\nError: Unable to parse path from url: " + url)
            return None

        files = {
            'file': (parsedUrl.path, mediaContent),
        }
        
        url = f"https://{user.mastodon_instance}/api/v2/media"
        response = requests.request("POST", url, headers=self.headers(user), files=files)
        json = response.json()
        return json.get("id")

