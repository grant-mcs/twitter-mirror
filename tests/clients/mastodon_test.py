import unittest

from clients.mastodon import Mastodon
from model.users import User

class TestMastodon(unittest.TestCase):

    def test_headers(self):
        mastodon = Mastodon()
        user = User(123456, "masto.test", "abc123")
        headers = mastodon.headers(user)
        self.assertEqual(2, len(headers))
        self.assertEqual("Bearer abc123", headers["Authorization"])
        self.assertEqual("twitter-mirror", headers["User-Agent"])

