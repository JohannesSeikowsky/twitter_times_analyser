# Twitter Times Analyser
# Basic script to analyse and graph how a Twitter account's tweets perform
# during different times of the day on average. Version 1.
import GetOldTweets3 as got
import matplotlib.pylab as plt

# get tweets
no_of_tweets = 100
target_account = "Seikowsky"
tweetCriteria = got.manager.TweetCriteria().setUsername(target_account).setMaxTweets(no_of_tweets)
tweets = got.manager.TweetManager.getTweets(tweetCriteria)


# tweet and likes counters for all hours of the day
tweets_counter = {}
likes_counter = {}

for hour_index in range(0,24):
	tweets_counter[hour_index] = 0
	likes_counter[hour_index] = 0


# go through tweets and adjust tweet and likes counter for each
for tweet in tweets:
	hour = tweet.date.hour
	likes = tweet.favorites

	tweets_counter[hour] = tweets_counter[hour] + 1
	likes_counter[hour] = likes_counter[hour] + likes


# compute average likes for all hours of the day
avg_likes = []
for hour_index in range(0,24):
	if tweets_counter[hour_index] != 0:
		likes = likes_counter[hour_index] / tweets_counter[hour_index]
		avg_likes.append(likes)
	else:
		avg_likes.append(0)


# plot
plt.plot(avg_likes)
plt.title(target_account)
plt.show()