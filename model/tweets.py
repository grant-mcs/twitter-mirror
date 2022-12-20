class Tweet():
    id: int
    text: str
    referencedTweets: dict
    media: list

    @staticmethod
    def parse_tweets_from_json(json: dict):
        data = json.get("data")
        if not data:
            return []

        includes = json.get("includes")
        referencedTweets = Tweet.parse_included_tweets(includes.get("tweets")) if includes else {}
        media = Tweet.parse_included_media(includes.get("media")) if includes else {}

        tweets = []
        for item in data:
            if Tweet.include_tweet(item, referencedTweets):
                tweet = Tweet()
                tweet.id = item.get("id")
                tweet.text = item.get("text")
                tweet.referencedTweets = item.get("referenced_tweets") if item.get("referenced_tweets") else {}
                tweet.media = Tweet.parse_media_from_json(item, media)
                tweets.append(tweet)
        
        return tweets

    @staticmethod
    def parse_media_from_json(item: dict, media: dict):
        attachments = item.get("attachments")
        if not attachments:
            return []

        mediaKeys = attachments.get("media_keys")
        if not mediaKeys:
            return []

        tweetMedia = []
        for key in mediaKeys:
            mediaData = media.get(key)
            if mediaData:
                tweetMedia.append(mediaData)

        return tweetMedia

    @staticmethod
    def include_tweet(tweet: dict, referencedTweetDict: dict):
        if not tweet:
            return False

        referencedTweets = tweet.get("referenced_tweets")
        if referencedTweets:
            for ref in referencedTweets:
                refType = ref.get("type")
                # "retweeted" and "quoted" tweets will be included unless they're
                # a reply to someone else
                if refType == "replied_to":
                    # A reply to someone else is excluded, a reply to yourself is
                    # included _if_ it's part of a thread started by yourself
                    tweetData = referencedTweetDict.get(ref.get("id"))
                    if tweetData and tweetData["author_id"] != tweet.get("author_id"):
                        return False

                    includeReferencedTweet = Tweet.include_tweet(tweetData, referencedTweetDict)
                    if not includeReferencedTweet:
                        return False

        return True

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
        if not json:
            return tweets

        for tweet in json:
            tweets[tweet.get("id")] = {
                "author_id": tweet.get("author_id"),
                "text": tweet.get("text"),
            }
        return tweets

    @staticmethod
    def parse_included_media(json: list):
        # Return a dict of media keys to their 'type' and 'url'
        media = {}
        if not json:
            return media

        for item in json:
            media[item.get("media_key")] = {
                "key": item.get("media_key"),
                "type": item.get("type"),
                "url": item.get("url"),
            }
        return media
