import unittest
from unittest import mock

from clients.mastodon import Mastodon
from model.users import User
from model.tweets import Tweet

# This method will be used by the mock to replace requests.post
def mocked_requests_post(*args, **kwargs):
    class MockResponse:
        id: int = 45678

        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'https://masto.test/api/v1/statuses':
        return MockResponse({"id": "45678"}, 200)

    return MockResponse(None, 404)

class TestMastodon(unittest.TestCase):

    def test_headers(self):
        mastodon = Mastodon()
        user = User(123456, "masto.test", "abc123")
        headers = mastodon.headers(user)
        self.assertEqual(2, len(headers))
        self.assertEqual("Bearer abc123", headers["Authorization"])
        self.assertEqual("twitter-mirror", headers["User-Agent"])


    @mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_post_toot(self, mock_post):
        mastodon = Mastodon()

        tweetData = {
            'id': '1234',
            'text': 'I am the tweet',
            'created_at': '2023-05-24 10:00:00',
            'referenced_tweets': {},
        }
        tweet = Tweet(tweetData)
        user = User(123456, "masto.test", "abc123")

        mastodon.post_toot(tweet, user)

        self.assertEqual(mock_post.call_args.args, ("https://masto.test/api/v1/statuses", ))
        self.assertEqual(mock_post.call_args.kwargs, {'headers': {'Authorization': 'Bearer abc123', 'User-Agent': 'twitter-mirror', 'Idempotency-Key': '1234'}, 'params': {'status': 'I am the tweet'}})
        self.assertEqual(len(mastodon.currentTootMap), 1)
        self.assertEqual(mastodon.currentTootMap['1234'], '45678')
