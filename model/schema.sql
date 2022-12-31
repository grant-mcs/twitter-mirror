BEGIN;
CREATE TABLE IF NOT EXISTS toot_map (
    toot_id VARCHAR(128) NOT NULL,
    tweet_id VARCHAR(128) NOT NULL,
    PRIMARY KEY (toot_id)
);
CREATE INDEX tweet_id ON toot_map(tweet_id);
COMMIT;