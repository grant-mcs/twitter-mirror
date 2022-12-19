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
    
    @staticmethod
    def parse_authors(json: list):
        # Return a dict of author IDs to their 'name' and 'username'
        authors = {}
        for author in json:
            authors[author.get("id")] = {
                "name": author.get("name"),
                "username": author.get("username"),
            }
        return authors

    @staticmethod
    def parse_included_tweets(json: list):
        # Return a dict of referenced tweet IDs to their 'author_id' and 'text'
        tweets = {}
        for tweet in json:
            tweets[tweet.get("id")] = {
                "author_id": tweet.get("author_id"),
                "text": tweet.get("text"),
            }
        return tweets
