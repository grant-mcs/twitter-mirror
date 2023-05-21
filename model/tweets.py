import html

class Tweet():
    id: int
    referencedTweets: dict
    media: list
    replyTo: str
    created: str

    def __init__(self, tweetData: dict, media: dict, referencedTweetData: dict, authors: dict):
        media = {} if media == None else media
        referencedTweetData = {} if referencedTweetData == None else referencedTweetData
        authors = {} if authors == None else authors

        self.id = tweetData.get("id")
        self.referencedTweets = tweetData.get("referenced_tweets") if tweetData.get("referenced_tweets") else {}
        self.text = tweetData.get("text")
        self.created = tweetData.get("created_at")
        self.replyTo = None

        self.update_text(referencedTweetData, authors)
        mediaSource = self.retweet_data(referencedTweetData) if (self.is_retweet() or self.is_quote_tweet()) else tweetData
        self.media = Tweet.parse_media_from_json(mediaSource, media)

        self.set_reply_to()


    def __str__(self):
        description = "Tweet " + self.id
        description += ", text: \"" + self.text
        description += "\", media = " + str(self.media)
        description += ", referenced tweets = " + str(self.referencedTweets)
        if self.is_retweet():
            description += ", retweet"
        if self.is_quote_tweet():
            description += ", quote tweet"
        if self.replyTo:
            description += ", reply to: " + self.replyTo

        return description

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, val: str):
        self.__text = html.unescape(val)

    def set_reply_to(self):
        for ref in self.referencedTweets:
            if ref.get("type") == "replied_to":
                self.replyTo = ref.get("id")

    def is_retweet(self):
        return self.text.startswith("RT ") and \
               len(self.referencedTweets) == 1 and \
               self.referencedTweets[0].get("type") == "retweeted"

    def is_quote_tweet(self):
        return len(self.referencedTweets) == 1 and \
               self.referencedTweets[0].get("type") == "quoted"

    def retweet_data(self, referencedTweetData: dict):
        return referencedTweetData.get(self.referencedTweets[0].get("id"))

    def update_text(self, referencedTweetData: dict, authors: dict):
        # If this is a retweet, use the text from the referenced tweet
        if self.is_retweet():
            prefixIdx = self.text.index(":") + 2
            prefix = self.text[:prefixIdx]
            self.text = prefix + self.retweet_data(referencedTweetData).get("text")
        elif self.is_quote_tweet():
            quoteTweetDivider = "\n====\n"
            quotedTweetData = self.retweet_data(referencedTweetData)
            authorName = Tweet.get_author_username(authors, quotedTweetData.get("author_id"))
            self.text = self.text + quoteTweetDivider + "@" + authorName + ": " + quotedTweetData.get("text")

    @staticmethod
    def parse_tweets_from_json(json: dict):
        data = json.get("data")
        if not data:
            return []

        includes = json.get("includes")
        referencedTweets = Tweet.parse_included_tweets(includes.get("tweets")) if includes else {}
        media = Tweet.parse_included_media(includes.get("media")) if includes else {}
        authors = Tweet.parse_authors(includes.get("users"))

        tweets = []
        for item in data:
            if Tweet.include_tweet(item, referencedTweets):
                tweet = Tweet(item, media, referencedTweets, authors)
                tweets.append(tweet)
        
        tweets.sort(key=lambda tweet: tweet.created)
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
        json = json if json else {}
        for author in json:
            authors[author.get("id")] = {
                "name": author.get("name"),
                "username": author.get("username"),
            }
        return authors

    @staticmethod
    def get_author_username(authors: dict, author_id: int):
        author = authors.get(author_id)
        if author:
            return author.get("username")

        return "Unknown"

    @staticmethod
    def parse_included_tweets(json: list):
        # Return a dict of referenced tweet IDs to their 'author_id' and 'text'
        tweets = {}
        if not json:
            return tweets

        for tweet in json:
            tweets[tweet.get("id")] = tweet
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
