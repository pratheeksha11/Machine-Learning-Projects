# Twitter Data Analysis on Lakers Tweets

## Overview
This project involves collecting, processing, and analyzing tweets related to the Los Angeles Lakers basketball team. The primary focus is on tweets containing specific hashtags related to the Lakers, such as `#lakers`, `#lebron`, `#AnthonyDavis`, and `#LebronJames`, while excluding retweets to maintain unique content.

## Data Collection
- **Twitter API**: The Tweepy library is used to interact with the Twitter API. Necessary credentials (`consumer_key`, `consumer_secret`, `access_token`, `access_token_secret`) are required for authentication.
- **Search Criteria**: Tweets are fetched using specific search words related to the Lakers, filtering out retweets.
- **Tweet Volume**: The script aims to collect up to 5000 tweets.

## Data Processing
- **Tweet Attributes**: Each tweet is stored with several attributes, including ID, text, creation date, retweet count, favorite count, follower count of the user, friends count, language, and the user's screen name.
- **JSON Conversion**: The collected tweets are converted into JSON format and saved in a file named `LAKERS_full.json`.
- **Filtering**: Tweets with less than 5 words are excluded to focus on more substantial content. Further filtering is done to include only tweets from users with more than 1000 followers. The first 300 of these filtered tweets are saved in `LAKERS_sample.json`.

## Analysis
- **Text Refinement**: Special characters and URLs are removed from the tweet texts for cleaner analysis.
- **Word Frequency**: The script calculates the frequency of words in the processed tweets, ignoring case differences.
- **Data Representation**: The frequencies of the top 15 words are displayed in a bar graph, highlighting the most commonly used words in the Lakers-related tweets.

## Output
- **Graphical Visualization**: The word frequency data is plotted in a horizontal bar graph and saved as a PDF file (`LAKERS.pdf`), providing a visual representation of the most frequent words in the analyzed tweets.
