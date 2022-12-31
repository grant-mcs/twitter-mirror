# This migration copies data from the old "simple" file structure to a SQLite database
import os
from clients.db import DB

def main():
    db = DB.connect()
    tootFiles = os.listdir("data/")
    for path in tootFiles:
        if path.endswith(".toots"):
            with open("data/", "r") as f:
                for line in f:
                    if len(line.strip()) == 0:
                        continue
                    tootMapping = line.split()
                    db.execute("INSERT INTO toot_map (toot_id, tweet_id) VALUES (?, ?)", [tootMapping[0], tootMapping[1]])


if __name__ == "__main__":
    main()
