#How to load the data?

import pandas as pds
import numpy as npy
#import matplotlib.pyplot as plt
import nltk as nl
from features import tweet_sentiment_features

#============Load data============

paths = ['/home/shaelyn/chance_of_hashtags/train.csv', '/home/shaelyn/chance_of_hashtags/test.csv']
train = pds.read_csv(paths[0])  
test = pds.read_csv(paths[1])
#print train, test #display the input data

sentiment_featureset = []
#for each tweet and associated info
for t in train.iterrows():
    print "******\n TWEET \n ******\n" + t[1][1] + "\n"    #print tweets
    tweet_words = t[1][1].split()

    print "tweet words before: " + str(tweet_words)
    for i in range(len(tweet_words)):
        #normalize words to same case
        tweet_words[i] = tweet_words[i].lower()
        #remove hashtag characters from beginning of words
        if tweet_words[i].startswith("#") or tweet_words[i].startswith("@"): 
            tweet_words[i] = tweet_words[i][1:]
        #separate punctuation
        if "!" in tweet_words[i]:
            punct_index = tweet_words[i].index("!")
            tweet_words.append(tweet_words[i][punct_index:])
            tweet_words[i] = tweet_words[i][:punct_index]
        if "?" in tweet_words[i]:
            punct_index = tweet_words[i].index("?")
            tweet_words.append(tweet_words[i][punct_index:])
            tweet_words[i] = tweet_words[i][:punct_index]
        if "." in tweet_words[i]:
            punct_index = tweet_words[i].index(".")
            tweet_words.append(tweet_words[i][punct_index:])
            tweet_words[i] = tweet_words[i][:punct_index]
        #remove common noise
        #if "{link}" in tweet_words:
         #   tweet_words.remove("{link}")
            
            
    #get training classification for this tweet
    sentiment = (t[1][4], t[1][5], t[1][6])
    print "tweet words after: " + str(tweet_words) + "\n\n"
    #construct sentiment feature set
    sentiment_featureset.append((tweet_sentiment_features(tweet_words), sentiment))
 
    
#============Bayesian classification============

train_set, test_set = sentiment_featureset[:200], sentiment_featureset[200:400]   
bayesian_classifier = nl.NaiveBayesClassifier.train(train_set)
print "bayesian classifier efficiency = " + str(nl.classify.accuracy(bayesian_classifier, test_set)) + "\n"
bayesian_classifier.show_most_informative_features(5)


#============Assess results============

#============Result in correct form============

#crossvalidation?

