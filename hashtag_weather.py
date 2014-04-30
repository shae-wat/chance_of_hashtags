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
stop_words = [line.strip().lower() for line in open('my_stop_words.txt')]

sentiment_featureset = []
where_featureset = []
kind_featureset = []
#for each tweet and associated info
for t in train.iterrows():
    #print t[1][1] + "\n"    #print tweets
    tweet_words = t[1][1].split()

    #print "tweet words before: " + str(tweet_words)
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
    for word in tweet_words:
        if word in stop_words:
            tweet_words.remove(word)
    
    
    #print "******t[] composition"
    #print t[1]
    #print "tweet words after: " + str(tweet_words) + "\n\n"
    
            
    #get sentiment training classification for this tweet
    sentiment = (t[1][4], t[1][5], t[1][6], t[1][7], t[1][8])
    #construct sentiment feature set
    sentiment_featureset.append((tweet_sentiment_features(tweet_words), sentiment))
    
    #get where training classification for this tweet
    where = (t[1][9], t[1][10], t[1][11], t[1][12])
    #construct where feature set
    where_featureset.append((tweet_sentiment_features(tweet_words), sentiment))
    
    #get kind training classification for this tweet
    kind = (t[1][13], t[1][14], t[1][15], t[1][16], t[1][17],
            t[1][18], t[1][19], t[1][20], t[1][21], t[1][22],
            t[1][23], t[1][24], t[1][25], t[1][26], t[1][27])
    #construct where feature set
    kind_featureset.append((tweet_sentiment_features(tweet_words), sentiment))
    
 
    
#============Bayesian classification============
 

#sentiment 
s_train_set, s_test_set = sentiment_featureset[:200], sentiment_featureset[200:300] 
s_bayesian_classifier = nl.NaiveBayesClassifier.train(s_train_set)
print "sentiment bayesian classifier efficiency = " + str(nl.classify.accuracy(s_bayesian_classifier, s_test_set)) + "\n"
s_bayesian_classifier.show_most_informative_features(5)

#where
w_train_set, w_test_set = where_featureset[:200], where_featureset[200:300] 
w_bayesian_classifier = nl.NaiveBayesClassifier.train(w_train_set)
print "where bayesian classifier efficiency = " + str(nl.classify.accuracy(w_bayesian_classifier, w_test_set)) + "\n"
w_bayesian_classifier.show_most_informative_features(5)

#kind
k_train_set, k_test_set = kind_featureset[:200], kind_featureset[200:300] 
bayesian_classifier = nl.NaiveBayesClassifier.train(k_train_set)
print "kind bayesian classifier efficiency = " + str(nl.classify.accuracy(bayesian_classifier, k_test_set)) + "\n"
bayesian_classifier.show_most_informative_features(5)


#============Assess results============

#============Result in correct form============

#crossvalidation?

