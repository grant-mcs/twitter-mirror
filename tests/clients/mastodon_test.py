import unittest
from unittest import mock

from clients.mastodon import Mastodon
from model.users import User
from model.tweets import Tweet

# This method will be used by the mock to replace requests.post
def mocked_requests_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code, text=""):
            self.json_data = json_data
            self.status_code = status_code
            self.text = text

        def json(self):
            return self.json_data

    if args[0] == 'https://masto.test/api/v1/statuses':
        tweet_id = int(kwargs.get("headers").get("Idempotency-Key"))

        # We use the tweet ID to identify cases needing special treatment
        if tweet_id == 1230:
            return MockResponse(None, 500, "Internal server error")

        toot_id = str(tweet_id + 90000)
        return MockResponse({"id": toot_id}, 200)

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
    def test_post_toot_error(self, mock_post):
        mastodon = Mastodon()
        user = User(123456, "masto.test", "abc123")

        # This tweet ID will trigger an error response from the Mastodon mock instance
        tweetData = {
            'id': '1230',
            'text': 'I will experience an error',
            'created_at': '2023-05-24 09:00:00',
            'referenced_tweets': {},
        }
        tweet = Tweet(tweetData)

        response = mastodon.post_toot(tweet, user)
        self.assertIsNone(response)

    @mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_post_toot_basic_and_reply(self, mock_post):
        mastodon = Mastodon()
        user = User(123456, "masto.test", "abc123")

        tweetData = {
            'id': '1234',
            'text': 'I am the tweet',
            'created_at': '2023-05-24 10:00:00',
            'referenced_tweets': {},
        }
        tweet = Tweet(tweetData)

        response = mastodon.post_toot(tweet, user)

        self.assertIsNotNone(response)
        self.assertEqual(mock_post.call_args.args, ("https://masto.test/api/v1/statuses", ))
        self.assertEqual(mock_post.call_args.kwargs, {'headers': {'Authorization': 'Bearer abc123', 'User-Agent': 'twitter-mirror', 'Idempotency-Key': '1234'}, 'params': {'status': 'I am the tweet'}})
        self.assertEqual(len(mastodon.currentTootMap), 1)
        self.assertEqual(mastodon.currentTootMap['1234'], '91234')

    @mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_post_toot_reply(self, mock_post):
        mastodon = Mastodon()
        user = User(123456, "masto.test", "abc123")

        tweetData = {
            'id': '1235',
            'text': 'I am the tweet',
            'created_at': '2023-05-24 10:00:00',
            'referenced_tweets': {},
        }
        tweet = Tweet(tweetData)
        response = mastodon.post_toot(tweet, user)
        self.assertIsNotNone(response)

        tweetData = {
            'id': '1236',
            'text': 'I am a reply',
            'created_at': '2023-05-24 10:02:00',
            'referenced_tweets': {},
        }
        replyTweet = Tweet(tweetData)
        replyTweet.replyTo = '1235'
        response = mastodon.post_toot(replyTweet, user)
        
        self.assertIsNotNone(response)

        self.assertEqual(mock_post.call_args.args, ("https://masto.test/api/v1/statuses", ))
        self.assertEqual(mock_post.call_args.kwargs, {'headers': {'Authorization': 'Bearer abc123', 'User-Agent': 'twitter-mirror', 'Idempotency-Key': '1236'}, 'params': {'status': 'I am a reply', 'in_reply_to_id': '91235'}})
        self.assertEqual(len(mastodon.currentTootMap), 2)
        self.assertEqual(mastodon.currentTootMap['1235'], '91235')
        self.assertEqual(mastodon.currentTootMap['1236'], '91236')
