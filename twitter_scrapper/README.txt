Setup:

Install python in your machine from - https://www.python.org/downloads/
Install pip through command line:
                                py get-pip.py
Install tweepy through command line:
                                pip install tweepy

Run the script in python Pycharm (scraper.py): 
	Use Run as and choose the interpreter as 3.8 or higher 
                           

Wait for 15 minutes as the code is pulling 5000 tweets.
The Twitter rate limiter will wait and pull the tweets accordingly

Explanation of how code works:

lines 2-8
importing required libraries for code to run

lines 12-15
giving authentication to the system to connect using your twitter key credentials

lines 17-19
authenticating tweepy with the twitter credentials to pull data from twitter

line 22
search words = required hashtags on which required tweets are being collected

lines 25-27
To collect 5000 tweets from Twitter database.
Search function by tweepy, where q is query to search tweets based on the search words defined.

lines 30-41
Pulling information from tweets iterable object.
Generated length of tweet text (length_of_text) attribute to eliminate any tweets that have text below 5 words.

line 44
json.dumps function to convert the obtained list to a json string

line 47
json.load function to convert the json string to json dict format

line 51-52
loading the dict object into a formatted json file - LAKERS_full.json
Saving this file for the purpose of this assignment

line 55
Filtering the json dict object which we got in line 47, to remove any tweets that have less than 5 words
using the length_of_text attribute that we generated for this purpose.

line 58-61
Filtering the refined json that have length_of_text greater than 5 words & users with more than 1000 followers_count
to collect 300 sample tweets with file name LAKERS_sample.json

line 66
In order to get keys of the iterable list we created a variable that holds only the first object of the list.
Now we have all the keys related to the object in key.

line 68-70
collecting complete list of data for each key into a single dictionary
collecting the list data for only 'text' key

line 72
removing links and hashtags from text to do word frequency analysis using the re library and regular expression.

line 74
converting the list of words into all lowercase words for each text, as capital letters are considered a unique word and
will cause discrepancies during word frequency analysis

line 76
converting all texts into a single list of words using itertools library

line 78
Counting the frequency of words in the list using collections library

line 80-81
Creating a Pandas data frame with giving 15 most common 'Frequent words' and its 'Frequency' as columns

line 83
Declaring the size of the graph plot

line 85
declaring a graph variable to give an output as bar histogram with frequent words, frequency in axis
and sorting the values based on order of frequency

line 87
setting the title of the histogram output

line 88-90
getting the required plot output and saving it as a pdf file LAKERS.pdf

################################### END ########################################