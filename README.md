# twitter-mirror
Mirror the tweets of a Twitter user to Mastodon.

## Configuration

To run this tool, you'll need one Twitter account and at least one Mastodon account.

### Twitter

You'll need a free Twitter developer account. Follow [these instructions](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api) to setup your access to the Twitter API.

This will give you an API key and API secret. You'll need to store the key and secret in environment variables for the shell instance running twitter-mirror.py script (e.g., `export API_KEY=<my Twitter API key>`). If you're running the script through cron, you can probably (depending on the version of cron your OS uses) set the variables in your crontab like this:

```bash
API_KEY=<my Twitter API key>
API_SECRET=<my Twitter API secret>

# Runs twitter-mirror python script every 10 minutes
*/10 * * * * root cd /var/www/twitter-mirror/; python3 twitter-mirror.py >> /var/log/cron/twitter-mirror.log 2>&1
```

### Mastodon

You'll need a Mastodon account for each Twitter user you want to mirror. Follow these steps:

1) Create a Mastodon account, on any Mastodon server.
2) Go to the Preferences page.
3) Open the Development tab.
4) Press the `New application` button.
5) Provide a name for the application (e.g. "twitter-mirror").
6) Use the default scopes or limit it to the minimum required scopes: `write:media`, `write:statuses`.
7) Press `SUBMIT`.
    - You will be returned to the Development tab and you should now see your newly created application.
8) Select your application.
9) Note the value of your "access token"

### Configuring users

With your Twitter and Mastodon accounts setup, you'll need to provide this information to the twitter-mirror service. As mentioned above, the Twitter credentials are provided through environment variables (`API_KEY` and `API_SECRET`).

For each Mastodon account that you want to post to, you'll need to provide the necessary information in a `users` file (`/twitter-mirror/data/users`). The file is a simple data structure. Each line of the file corresponds to one Mastodon account using this format:

```
<Twitter user ID> <Mastodon instance> <Mastodon access token>
<Twitter user ID 2> <Mastodon instance 2> <Mastodon access token 2>
```

e.g.:

```
123456789 mstdn.ca 2abcDEf_ghIJkLMNopqRstuV_W90xy8ZAb1cd-6EF3G
```

### Latest tweet

For each configured user, twitter-mirror keeps track of the ID of the last tweet mirrored from the account in a file at `twitter-mirror/data/<Twitter user ID>.latest`. For a new user, you can either create this file yourself with the ID that you would like or twitter-mirror will first request all tweets from that day and then initialize the .latest file based on that first request.
