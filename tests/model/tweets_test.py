import unittest

from model.tweets import Tweet

class TestTweets(unittest.TestCase):

    def test_parse_tweets_from_json(self):
        json = {
            "data": [
                {
                    "author_id": "281877818",
                    "id": "1604637321894055936",
                    "referenced_tweets": [
                        {
                            "id": "1604617643973124097",
                            "type": "retweeted"
                        }
                    ],
                    "created_at": "2022-12-30T09:00:31.000Z",
                    "text": "RT @elonmusk: Should I step down ..."
                },
                {
                    "author_id": "281877818",
                    "id": "1604555574942715904",
                    "referenced_tweets": [
                        {
                            "id": "1604545827505983488",
                            "type": "quoted"
                        },
                        {
                            "id": "1604554971017629696",
                            "type": "replied_to"
                        }
                    ],
                    "created_at": "2022-12-30T10:00:31.000Z",
                    "text": "@MarcGoldwein @cartervance My next tweet may be of interest. Always scroll down!\n\nhttps://t.co/QzBbheCC8D"
                },
                {
                    "author_id": "281877818",
                    "id": "1604549350469693440",
                    "referenced_tweets": [
                        {
                            "id": "1604549110920380417",
                            "type": "replied_to"
                        }
                    ],
                    "created_at": "2022-12-30T11:00:31.000Z",
                    "text": "@alfred_twu Well the % of 20-21 is flat..."
                },
                {
                    "author_id": "281877818",
                    "id": "1604548832401838080",
                    "created_at": "2022-12-30T16:00:31.000Z",
                    "text": "I'm just a plain old tweet"
                },
                {
                    "author_id": "281877818",
                    "id": "1604547577772331009",
                    "referenced_tweets": [
                        {
                            "id": "1604547475913682945",
                            "type": "replied_to"
                        }
                    ],
                    "created_at": "2022-12-30T08:00:31.000Z",
                    "text": "At least &gt; if we believe this is causal."
                },
                {
                    "author_id": "281877818",
                    "id": "1604547244522319872",
                    "referenced_tweets": [
                        {
                            "id": "1604546475676950529",
                            "type": "replied_to"
                        }
                    ],
                    "created_at": "2022-12-30T13:00:31.000Z",
                    "text": "@kimmytaylor You can see the peak among all age groups!"
                },
                {
                    "referenced_tweets": [
                        {
                            "type": "quoted",
                            "id": "1659588471571226625"
                        }
                    ],
                    "text": "This is a quote tweet https://t.co/GbqWB2I5Lk",
                    "author_id": "281877818",
                    "edit_history_tweet_ids": [
                        "1660003766488403968"
                    ],
                    "id": "1660003766488403968",
                    "created_at": "2023-05-20T19:25:13.000Z"
                },
            ],
            "includes": {
                "media": [
                    {
                        "media_key": "mediakey_1",
                        "type": "photo",
                        "url": "https://pbs.twimg.com/media/image1.jpg"
                    }
                ],
                "tweets": [
                    {
                        "author_id": "44196397",
                        "id": "1604617643973124097",
                        "text": "Should I step down as head of Twitter? I will abide by the results of this poll.",
                        "attachments": {
                            "media_keys": [
                                "mediakey_1"
                            ]
                        },
                    },
                    {
                        "author_id": "281877818",
                        "id": "1604545827505983488",
                        "referenced_tweets": [
                            {
                                "id": "1604543540838535170",
                                "type": "replied_to"
                            }
                        ],
                        "text": "Here is the share of the population enrolled in college, by age group. https://t.co/Dl5HtbIVWz"
                    },
                    {
                        "author_id": "420034061",
                        "id": "1604554971017629696",
                        "referenced_tweets": [
                            {
                                "id": "1604550926592638976",
                                "type": "replied_to"
                            }
                        ],
                        "text": "@Noahpinion @cartervance 20-24 year olds peaked in 2014. https://t.co/4LpWFasZui"
                    },
                    {
                        "author_id": "975493802197594112",
                        "id": "1604549110920380417",
                        "referenced_tweets": [
                            {
                                "id": "1604543540838535170",
                                "type": "replied_to"
                            }
                        ],
                        "text": "@Noahpinion Around that time the University of California put in a rule that requires students to graduate in 4 years, previously many students took 5 or more years to graduate.  Did other colleges do this also?\n\nIt'd explain how there are now fewer older students, but more age 20-21"
                    },
                    {
                        "author_id": "281877818",
                        "id": "1604547475913682945",
                        "text": "Worse in combination with this paper. https://t.co/dN0mMv0jkI"
                    },
                    {
                        "author_id": "281877818",
                        "id": "1604546475676950529",
                        "referenced_tweets": [
                            {
                                "id": "1604545549050740738",
                                "type": "replied_to"
                            }
                        ],
                        "text": "@kimmytaylor Here are the percentage rates by age group. https://t.co/uptK68jHgh"
                    },
                    {
                        "author_id": "12345678",
                        "id": "1604545549050740738",
                        "referenced_tweets": [
                            {
                                "id": "1604543540838535170",
                                "type": "replied_to"
                            }
                        ],
                        "text": "@Noahpinion I did. Also there will be 15% less high school students by 2026."
                    },
                    {
                        "edit_history_tweet_ids": [
                            "1659588471571226625"
                        ],
                        "id": "1659588471571226625",
                        "text": "This is something worth quoting",
                        "created_at": "2023-05-19T15:54:59.000Z",
                        "author_id": "1003777482"
                    },
                ],
                "users": [
                    {
                        "id": "281877818",
                        "name": "Noah Smith \ud83d\udc07\ud83c\uddfa\ud83c\udde6",
                        "username": "Noahpinion"
                    },
                    {
                        "id": "44196397",
                        "name": "Elon Musk",
                        "username": "elonmusk"
                    },
                    {
                        "id": "12345678",
                        "name": "Kimmy Taylor",
                        "username": "kimmytaylor"
                    },
                    {
                        "id": "975493802197594112",
                        "name": "Alfred Twu",
                        "username": "alfred_twu"
                    },
                    {
                        "id": "420034061",
                        "name": "Marc Goldwein",
                        "username": "MarcGoldwein"
                    },
                    {
                        "id": "1003777482",
                        "name": "Annie van Leur",
                        "username": "AnnevanLeur"
                    }
                ],
            },
            "meta": {
                "newest_id": "1604555574942715904",
                "next_token": "7140dibdnow9c7btw450bo1n9vtkg09swwpgolfwffjua",
                "oldest_id": "1604547244522319872",
                "result_count": 6
            }
        }
        tweets = Tweet.parse_tweets_from_json(json)
        self.assertEqual(4, len(tweets))
        self.assertEqual("I'm just a plain old tweet", tweets[2].text)
        self.assertEqual(0, len(tweets[2].referencedTweets))

        # Retweets use the text from the referenced tweet
        self.assertEqual("RT @elonmusk: Should I step down as head of Twitter? I will abide by the results of this poll.", tweets[1].text)
        self.assertEqual(1, len(tweets[1].referencedTweets))
        self.assertEqual(1, len(tweets[1].media))
        self.assertEqual("https://pbs.twimg.com/media/image1.jpg", tweets[1].media[0].get("url"))

        # Replies should have the ID of the tweet that was replied to
        self.assertEqual("At least > if we believe this is causal.", tweets[0].text)
        self.assertEqual(1, len(tweets[0].referencedTweets))
        self.assertEqual(0, len(tweets[0].media))
        self.assertEqual("1604547475913682945", tweets[0].replyTo)

        # Quote tweets should include the text of the original tweet
        self.assertEqual("This is a quote tweet https://t.co/GbqWB2I5Lk\n====\nAnnevanLeur: This is something worth quoting", tweets[3].text)
        self.assertEqual(1, len(tweets[3].referencedTweets))
        self.assertEqual(0, len(tweets[3].media))


    def test_parse_authors(self):
        json = [
            {"id": "1111", "name": "User One", "username": "user_one"},
            {"id": "2222", "name": "User Two", "username": "user_two"},
            {"id": "3333", "name": "User Three", "username": "user_three"},
        ]
        authors = Tweet.parse_authors(json)
        self.assertEqual(3, len(authors))
        self.assertEqual("User Three", authors["3333"]["name"])


    def test_parse_included_tweets(self):
        json = [
            {"id": "111111", "author_id": "1111", "text": "I'm a tweet"},
            {"id": "222222", "author_id": "2222", "text": "Tweetledee"},
            {"id": "333333", "author_id": "1111", "text": "Tweetledum"},
        ]
        tweets = Tweet.parse_included_tweets(json)
        self.assertEqual(3, len(tweets))
        self.assertEqual("Tweetledum", tweets["333333"]["text"])

    
    def test_include_tweet(self):
        # Simple tweet, no referenced tweets
        tweet = {
            "id": 111111,
            "text": "Tweet tweet",
            "author_id": 1111
        }
        self.assertTrue(Tweet.include_tweet(tweet, {}))

        # Retweet
        tweet = {
            "id": 111111,
            "text": "Tweet tweet",
            "author_id": 1111,
            "referenced_tweets": [
                {"id": "222222", "type": "retweeted"}
            ]
        }
        self.assertTrue(Tweet.include_tweet(tweet, {}))

        # Quote tweet
        tweet = {
            "id": 111111,
            "text": "Tweet tweet",
            "author_id": 1111,
            "referenced_tweets": [
                {"id": "222222", "type": "quoted"}
            ]
        }
        self.assertTrue(Tweet.include_tweet(tweet, {}))

        # Reply to someone else
        referencedTweets = {
            "222222": {
                "author_id": "2222",
                "text": "1 + 1 = 2"
            }
        }
        tweet = {
            "id": 111111,
            "text": "@Me This is the real answer",
            "author_id": "1111",
            "referenced_tweets": [
                {"id": "222222", "type": "replied_to"}
            ]
        }
        self.assertFalse(Tweet.include_tweet(tweet, referencedTweets))

        # Reply in a thread started by someone else
        referencedTweets = {
            "222222": {
                "author_id": "1111",
                "text": "@You 1 + 1 = 10",
                "referenced_tweets": [
                    {"id": "333333", "type": "replied_to"},
                ],
            },
            "333333": {
                "author_id": "2222",
                "text": "1 + 1 = 2",
            },
        }
        self.assertFalse(Tweet.include_tweet(tweet, referencedTweets))

        # Reply in a thread started by tweet author
        referencedTweets["333333"] = {
            "author_id": "1111",
            "text": "1 + 1 = 2",
        }
        self.assertTrue(Tweet.include_tweet(tweet, referencedTweets))


    def test_parse_media_from_json(self):
        tweet = {
            "id": 111111,
            "text": "Picture this",
            "author_id": "1111",
        }
        media = Tweet.parse_media_from_json(tweet, {})
        self.assertEqual([], media)

        tweet["attachments"] = {
            "media_keys": ["1234_12"]
        }
        mediaData = {
            "1234_12": {
                "key": "1234_12",
                "type": "photo",
                "url": "https://testimg.com/1234_12"
            }
        }
        media = Tweet.parse_media_from_json(tweet, mediaData)
        self.assertEqual([{"key": "1234_12", "type": "photo", "url": "https://testimg.com/1234_12"}], media)

    def test_is_quote_tweet(self):
        tweetData = {
            "id": 1234,
            "text": "Hath not quote tweet eyes?",
            "created_at": "2023-05-23T12:12:12Z",
        }
        tweet = Tweet(tweetData, {}, {}, {})
        self.assertFalse(tweet.is_quote_tweet())

        # Add a referenced tweet that is not quoted
        tweetData["referenced_tweets"] = [{
            "type": "replied_to",
            "id": 1235,
        }]
        referencedTweetData = {1235: {
            "id": 1235,
            "text": "Am I not a quote?",
            "created_at": "2023-05-23T11:11:11Z",
        }}
        tweet = Tweet(tweetData, {}, referencedTweetData, {})
        self.assertFalse(tweet.is_quote_tweet())

        # Now make that referenced tweet a quote
        tweetData["referenced_tweets"][0]["type"] = "quoted"
        tweet = Tweet(tweetData, {}, referencedTweetData, {})
        self.assertTrue(tweet.is_quote_tweet())

if __name__ == '__main__':
    unittest.main()