import time
import twitter

import process
import tweet

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN_KEY = ""
ACCESS_TOKEN_SECRET = ""

api = twitter.Api(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN_KEY, access_token_secret=ACCESS_TOKEN_SECRET,
                  sleep_on_rate_limit=True)


if __name__ == "__main__":

    mentions = api.GetMentions(count=1)
    since_id = mentions[0].id
    print(mentions, since_id)
    username = mentions[0].user.screen_name

    while True:

        if len(mentions) >= 1:
            for mention in mentions:
                username = mention.user.screen_name
                since_id = mention.id

                # Get tweets
                tweets = tweet.get_tweets(username, 2000)
                tweets_text = process.get_text(tweets)

                # Process tweets for wordcloud
                wordcloud_data = process.list_to_str(tweets_text)
                process.generate_wordcloud(wordcloud_data)

                # Reply with wordcloud
                api.PostUpdate(status="Hello @{}, I am a bot".format(username), media="wordcloud.png",
                               in_reply_to_status_id=since_id)
        # Get new messages
        mentions = api.GetMentions(since_id=since_id)
        time.sleep(5)
