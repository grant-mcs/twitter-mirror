import os
import unittest
from unittest import mock

from clients.twitter import Twitter

# This method will be used by the mock to replace requests.post
def mocked_requests_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code, text=""):
            self.json_data = json_data
            self.status_code = status_code
            self.text = text

        def json(self):
            return self.json_data

    if args[0] == 'https://api.twitter.com/oauth2/token':
        api_key = kwargs.get("auth")[0]

        # We use the API key to identify cases needing special treatment
        if api_key == 'cba321':
            return MockResponse(None, 500, "Internal server error")

        return MockResponse({"access_token": "abc123"}, 200)

    return MockResponse(None, 404)

class TestTwitter(unittest.TestCase):

    @mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_headers_error(self, mock_post):
        twitter = Twitter()

        os.environ["API_KEY"] = "cba321"
        os.environ["API_SECRET"] = "secretsecret"
        headers = twitter.headers()
        self.assertIsNone(headers)

    @mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_headers_simple(self, mock_post):
        twitter = Twitter()

        os.environ["API_KEY"] = "abc123"
        os.environ["API_SECRET"] = "secretsecret"
        headers = twitter.headers()
        self.assertEqual(2, len(headers))
        self.assertEqual("Bearer abc123", headers["Authorization"])
        self.assertEqual("twitter-mirror", headers["User-Agent"])
