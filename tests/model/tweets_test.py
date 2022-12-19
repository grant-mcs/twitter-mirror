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
                    "text": "RT @elonmusk: Should I step down as head of Twitter? I will abide by the results of this poll."
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
                "tweets": [
                    {
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
                        "id": "20651841",
                        "name": "Wally Nowinski",
                        "username": "Nowooski"
                    },
                ],
            },
            "meta": {
                "newest_id": "1604555574942715904",
                "next_token": "7140dibdnow9c7btw450bo1n9vtkg09swwpgolfwffjua",
                "oldest_id": "1604547244522319872",
                "result_count": 5
            }
        }
        tweets = Tweet.parse_tweets_from_json(json)
        self.assertEqual(6, len(tweets))
        self.assertEqual("I'm just a plain old tweet", tweets[3].text)
        self.assertEqual(0, len(tweets[3].referencedTweets))


    def test_parse_authors(self):
        json = [
            {"id": "1111", "name": "User One", "username": "user_one"},
            {"id": "2222", "name": "User Two", "username": "user_two"},
            {"id": "3333", "name": "User Three", "username": "user_three"},
        ]
        authors = Tweet.parse_authors(json)
        self.assertEqual(3, len(authors))
        self.assertEqual("User Three", authors["3333"]["name"])


if __name__ == '__main__':
    unittest.main()