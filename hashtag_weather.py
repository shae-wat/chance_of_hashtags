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
    tweet_words = t[1][1].split()
    sentiment = (t[1][4], t[1][5], t[1][6])
    #construct sentiment feature set
    sentiment_featureset.append((tweet_sentiment_features(tweet_words), sentiment))
 
    
#============Bayesian classification============

train_set, test_set = sentiment_featureset[:300], sentiment_featureset[300:600]   
bayesian_classifier = nl.NaiveBayesClassifier.train(train_set)
print "bayesian classifier efficiency = " + str(nl.classify.accuracy(bayesian_classifier, test_set)) + "\n"
bayesian_classifier.show_most_informative_features(5)


#============Assess results============

#============Result in correct form============

#crossvalidation?

