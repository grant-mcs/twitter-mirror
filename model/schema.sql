BEGIN;
CREATE TABLE IF NOT EXISTS toot_map (
    toot_id VARCHAR(128) NOT NULL,
    tweet_id VARCHAR(128) NOT NULL,
    PRIMARY KEY (toot_id)
);
CREATE INDEX tweet_id ON toot_map(tweet_id);

CREATE TABLE IF NOT EXISTS users (
    twitter_id VARCHAR(64) NOT NULL,
    mastodon_instance VARCHAR(128) NOT NULL,
    mastodon_token VARCHAR(128) NOT NULL,
    most_recent_tweet VARCHAR(128) NULL,
    PRIMARY KEY (twitter_id)
);
COMMIT;