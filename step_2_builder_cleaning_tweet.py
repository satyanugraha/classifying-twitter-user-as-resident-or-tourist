import csv
from pprint import pprint
#importing punctuation models in python
from string import punctuation as p
#import regex
import re
import sys

def processtweet(tweet):
    #process the tweets
    
    #convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','',tweet)
    #delete username*
    tweet = re.sub('username[^\s]+','',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    #punctuation
    tweet = re.sub('[0123456789\!#$%&()*+,-./:;<=>?@^_`{|}~]','',tweet)
    #special case for ' " [ ]
    tweet = re.sub("'","",tweet)
    tweet = re.sub('"','',tweet)
    tweet = re.sub("\[","",tweet)
    tweet = re.sub("\]","",tweet)
    #delete all unicode
    tweet = re.sub(r'[^\x00-\x7F]+','',tweet)
    return tweet
 
maxInt = sys.maxsize
csv.field_size_limit(maxInt)
with open('step_1_output_tweet_concatenation_dataset.csv','rU') as csv_file:
    with open('step_2_output_tweet_clean_dataset.csv','wb') as csv_result:
        reader = csv.reader(csv_file, delimiter=',')
	#next(reader,None) #skipheader
        writer = csv.writer(csv_result)
        
        for line in reader:
	    tweet_array = []
            tweets = line[1]
            processedTweet = processtweet(tweets)
            tweet_array.append(processedTweet)
	    #print processedTweet
	    #print tweets
            print tweet_array
	    writer.writerow(tweet_array)
