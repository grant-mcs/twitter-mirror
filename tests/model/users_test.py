import os
import unittest

from model.tweets import Tweet
from model.users import User

class TestUsers(unittest.TestCase):

    def setUp(self):
        os.remove("data/12345.toots")

    def test_save_toot_data(self):
        user = User("12345", "mastodon.test", "token_ABC")

        tweetData = {
            "id": 111111,
            "text": "Tweet tweet",
            "author_id": 1111,
        }
        tweet = Tweet(tweetData, {}, {})
        result = user.save_toot_data({}, tweet)
        self.assertFalse(result)

        tootData = {
            "id": "22222",
            "created_at": "2022-12-29T11:22:33.444Z",
            "content": "Tweet tweet",
            "account": {
                "id": "1",
                "username": "Gargron",
            },
        }
        result = user.save_toot_data(tootData, tweet)
        self.assertTrue(result)

