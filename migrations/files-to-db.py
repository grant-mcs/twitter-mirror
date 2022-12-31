# This migration copies data from the old "simple" file structure to a SQLite database
import os
from clients.db import DB

def main():
    db = DB.connect()
    tootFiles = os.listdir("data/")
    for path in tootFiles:
        if path == "users":
            with open(path, "r") as f:
                for line in f:
                    if len(line.strip()) == 0:
                        continue
                    user = line.split()
                    result = db.query("SELECT * FROM users WHERE twitter_id = ?", [user[0]])
                    if not result:
                        db.execute("INSERT INTO users (twitter_id, mastodon_instance, mastodon_token) VALUES (?, ?, ?)", [user[0], user[1], user[2]])
        elif path.endswith(".toots"):
            with open(f"data/{path}", "r") as f:
                for line in f:
                    if len(line.strip()) == 0:
                        continue
                    tootMapping = line.split()
                    result = db.query("SELECT * FROM toot_map WHERE toot_id = ?", [tootMapping[0]])
                    if not result:
                        db.execute("INSERT INTO toot_map (toot_id, tweet_id) VALUES (?, ?)", [tootMapping[0], tootMapping[1]])


if __name__ == "__main__":
    main()
