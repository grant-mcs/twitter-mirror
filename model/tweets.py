class Tweet():
    id: int
    text: str
    referencedTweets: dict

    @staticmethod
    def parse_tweets_from_json(json: dict):
        data = json.get("data")
        tweets = []
        for item in data:
            tweet = Tweet()
            tweet.id = item.get("id")
            tweet.text = item.get("text")
            tweet.referencedTweets = item.get("referenced_tweets") if item.get("referenced_tweets") else {}
            tweets.append(tweet)
        
        return tweets
    

