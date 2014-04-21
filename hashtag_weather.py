#How to load the data?

import pandas as pds
import numpy as npy
#import matplotlib.pyplot as plt
import nltk as nl
from features import tweet_sentiment_features

#============Load data============

paths = ['/home/shaelyn/chance_of_hashtags/train.csv', '/home/shaelyn/chance_of_hashtags/test.csv']
train = pds.read_csv(paths[0]) #dataframe 
#test = pds.read_csv(paths[1])
#print train #display the data


#============Data in correct form============

#for each tweet and related info
for t in train.iterrows():
    print t[1][1] + "\n"  #prints each tweet
    tweet_words = t[1][1].split()
    print tweet_sentiment_features(tweet_words)
    print "\n\n\n"


#============Run algorithm on data============

#============Assess results============

#============Result in correct form============

#crossvalidation?

