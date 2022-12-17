import requests
import os
import json

# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")


def tweet_url_for_user(user_id):
    return "https://api.twitter.com/2/users/{}/tweets".format(user_id)


def last_mirrored_id():
    return 1604029197126537217


def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserTweetsPython"
    return r


def get_tweets(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    url = tweet_url_for_user(281877818)
    tweet_id = last_mirrored_id()
    tweets = get_tweets(url, {"since_id": tweet_id, "expansions": "referenced_tweets.id"})
    print(json.dumps(tweets, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
