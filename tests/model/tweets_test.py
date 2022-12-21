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
                    "text": "@alfred_twu Well the % of 20-21 is flat..."
                },
                {
                    "author_id": "281877818",
                    "id": "1604548832401838080",
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
                    "text": "@emollick At least, if we believe this is causal."
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
                    "text": "@kimmytaylor You can see the peak among all age groups!"
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
                        "author_id": "39125788",
                        "id": "1604547475913682945",
                        "referenced_tweets": [
                            {
                                "id": "1603834378861281302",
                                "type": "quoted"
                            },
                            {
                                "id": "1604545827505983488",
                                "type": "replied_to"
                            }
                        ],
                        "text": "@Noahpinion Worse in combination with this paper. https://t.co/dN0mMv0jkI"
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
                        "id": "39125788",
                        "name": "Ethan Mollick",
                        "username": "emollick"
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
        self.assertEqual(2, len(tweets))
        self.assertEqual("I'm just a plain old tweet", tweets[1].text)
        self.assertEqual(0, len(tweets[1].referencedTweets))

        # Retweets use the text from the referenced tweet
        self.assertEqual("RT @elonmusk: Should I step down as head of Twitter? I will abide by the results of this poll.", tweets[0].text)
        self.assertEqual(1, len(tweets[0].referencedTweets))
        self.assertEqual(1, len(tweets[0].media))
        self.assertEqual("https://pbs.twimg.com/media/image1.jpg", tweets[0].media[0].get("url"))


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

if __name__ == '__main__':
    unittest.main()