import twitter

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN_KEY = ""
ACCESS_TOKEN_SECRET = ""

api = twitter.Api(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN_KEY, access_token_secret=ACCESS_TOKEN_SECRET,
                  sleep_on_rate_limit=True)


def amount_of_tweets(numLeft: int) -> int:
    """
    Determines the number of tweets the api should call
    :param numLeft: Number of tweets remained to call
    :return: number of tweets the api should call
    """
    # If the number left is greater than the max, call 200
    if numLeft >= 200:
        return 200
    # else call the number left
    else:
        return numLeft


def add_tweet_to_list(tweets: list, timeLine: list) -> list:
    """
    Adds tweets to the list
    :param tweets: Entire list of tweets
    :param timeLine: List of tweets from new batch
    :return: List of tweets with new tweets added
    """
    for tweet in timeLine:
        tweets.append(tweet)
    return tweets


def get_tweets(username: str, num: int) -> [str]:
    """
    Return list of tweets
    :param username: (str) Username of user
    :param num: (int) Number of tweets extracted
    :return: ([str]) List of tweets list
    """
    try:
        tweets = []
        # Get 200 tweets and return the ones that are not retweets
        user_timeline = api.GetUserTimeline(screen_name=username, count=200, include_rts=False)

        # Add tweets to list
        add_tweet_to_list(tweets, user_timeline)

        # If there are no tweets, return nothing
        if len(tweets) == 0:
            return

        # Keep adding 200 tweets until 2000 tweets are analyzed
        while len(tweets) < 2000:
            # Gets the last tweet from the list)
            last_tweet = tweets[len(tweets) - 1]

            # Get tweets after last tweet
            user_timeline = api.GetUserTimeline(None, username, None, last_tweet.id - 1,
                                                amount_of_tweets(2000 - len(tweets)), False)

            # If there are no remaining tweets to get, end the while loop
            if len(user_timeline) == 0:
                break

            # Add the tweets to the list
            add_tweet_to_list(tweets, user_timeline)
        # Return tweets
        return tweets

    except twitter.error.TwitterError:
        pass
