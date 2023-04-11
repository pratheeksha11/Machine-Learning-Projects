# Define the search term and the date_since date
import json
import tweepy
import re
import itertools
import collections
import pandas as pd
import matplotlib.pyplot as pyplot


# First update below varibales with your own information
consumer_key = "Add you own consumer_key"
consumer_secret = "Add you own consumer_secret"
access_token = "Add you own access_token"
access_token_secret = "Add you own access_token_secret"
# Setting up Tweepy authorization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Define the search term
search_words = "#lakers OR #lebron OR #AnthonyDavis OR #LebronJames -filter:retweets"

# Collect tweets
tweets = tweepy.Cursor(api.search_tweets,
                       q=search_words,
                       lang="en").items(5000)

# Pulling information from tweets iterable object
tweets_list = [{'id':tweet.id,
                'text':tweet.text,
                # adding an attribute length of tweet
                'length_of_text': len(tweet.text.split()),
                'created_at':str(tweet.created_at),
                'retweet_count':tweet.retweet_count,
                'favorite_count':tweet.favorite_count,
                'followers_count':tweet.user.followers_count,
                'friends_count':tweet.user.friends_count,
                'language':tweet.lang,
                'screen_name':tweet.user.screen_name}
               for tweet in tweets]

# dump the JSON data into file
json_string = json.dumps(tweets_list)

# lakers full dict of 5000 tweets
lakers_full_dict = json.loads(json_string)

# Write pretty JSON to file
# Saving 5000 tweets into the LAKERS_full.json
with open('LAKERS_full.json','w') as formatted_file:
    json.dump(lakers_full_dict, formatted_file, indent=4)

# Filtering the full json to remove any tweets that have less than 5 words
less_than_5_words = [x for x in lakers_full_dict if x['length_of_text'] > 5]

# Filtering the refined json of tweets greater than 5 words to have more than 1000 followers count
lakers_dict = [x for x in less_than_5_words if x['followers_count'] > 1000]
sample_300 = lakers_dict[:300]
with open('LAKERS_sample.json', 'w') as filtered_file:
    json.dump(sample_300, filtered_file, indent=4)

# Word frequency in tweets text
# For this I want to remove any url links or special characters present in the tweets text
# Using one object of the list to store the keys in key and use them to map in single dict
keys = sample_300[0]
# collapse values into a single dictionary
value_dict = {k: set(d[k] for d in sample_300) for k in keys}
# Creating a list of texts to refine
text_list = [text for text in value_dict['text']]
# removing links and hashtags from text to do word frequency analysis
all_text_urls_removed = [" ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", urls).split()) for urls in text_list]
# List of lists containing all lowercase words for each text as capital letters are considered a unique word
words_in_text = [t.lower().split() for t in all_text_urls_removed]
# list of words of all text
all_words_in_one_list = list(itertools.chain(*words_in_text))
# counting all words in the list using collections library
counter_words = collections.Counter(all_words_in_one_list)
# creating a pandas data frame
word_frequency = pd.DataFrame(counter_words.most_common(15), columns=['Frequent Words', 'Frequency'])
word_frequency.head()
# size of the graph plot
fig, ax = pyplot.subplots(figsize=(10, 10))
#declaring graph variables
graph = word_frequency.sort_values(by='Frequency').plot.barh(x='Frequent Words', y='Frequency', ax=ax, color="blue")
#setting the header
ax.set_title("Frequent words found in tweets of lakers")
graph.plot()
#saving the output as pdf file
pyplot.savefig('LAKERS.pdf')

