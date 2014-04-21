#How to load the data?

import pandas as pds
import numpy as npy
#import matplotlib.pyplot as plt
import nltk as nl
from features import tweet_sentiment_features

#============Load data============

paths = ['/home/shaelyn/chance_of_hashtags/train.csv', '/home/shaelyn/chance_of_hashtags/test.csv']
train = pds.read_csv(paths[0])  
#test = pds.read_csv(paths[1])
#print train #display the data


#============Data in correct form============

#for each tweet and associated info
for t in train.iterrows():
    print t[1][1] + "\n"  #print each tweet
    tweet_words = t[1][1].split()
    #print tweet_sentiment_features(tweet_words)
    #print "\n\n\n"


#============Train classifiers============

#Naive Bayes
sentiment_featuresetsS1 = {}
for t in train.iterrows():
    tweet_words = t[1][1].split()
    s1 = t[1][4]
    s2 = t[1][5]
    s3 = t[1][6]
    #sentiment_featuresetsS1[tweet_sentiment_features(tweet_words)] = s1
    

#============Assess results============

#============Result in correct form============

#crossvalidation?

