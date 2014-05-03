import pandas as pds
import numpy as npy
#import matplotlib.pyplot as plt
import nltk as nl
from feature_extractor import tweet_sentiment_features
from classifiers import bayes_classifier_sentiment, bayes_classify, calc_feature_probabilities

#============Load data============

paths = ['/home/shaelyn/chance_of_hashtags/train.csv', '/home/shaelyn/chance_of_hashtags/test.csv']
train = pds.read_csv(paths[0])  
test = pds.read_csv(paths[1])
#print train, testing    # uncomment to display the input data
stop_words = [line.strip().lower() for line in open('my_stop_words.txt')]


#============Construct featuresets============

sentiment_featureset = []
where_featureset = []
kind_featureset = []

for t in train.iterrows():
    #print t[1][1] + "\n" + str(t[1][2]) + "\n" + str(t[1][3]) + "\n"    #uncomment to print tweets
    tweet_words = t[1][1].split()

    #print "tweet words before preprocessing : " + str(tweet_words)
    for i in range(len(tweet_words)):
        #normalize words to same case
        tweet_words[i] = tweet_words[i].lower()
        #remove hashtag and mention characters from beginning of words
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
    
            
    #get sentiment training classification for this tweet
    sentiment = (t[1][4], t[1][5], t[1][6], t[1][7], t[1][8])
    #construct sentiment feature set
    sentiment_featureset.append((tweet_sentiment_features(tweet_words), sentiment))
    
    #get when training classification for this tweet
    where = (t[1][9], t[1][10], t[1][11], t[1][12])
    #construct where feature set
    where_featureset.append((tweet_sentiment_features(tweet_words), where))
    
    #get kind training classification for this tweet
    kind = (t[1][13], t[1][14], t[1][15], t[1][16], t[1][17],
            t[1][18], t[1][19], t[1][20], t[1][21], t[1][22],
            t[1][23], t[1][24], t[1][25], t[1][26], t[1][27])
    #construct kind feature set
    kind_featureset.append((tweet_sentiment_features(tweet_words), kind))


    
 
#============Training and testing sets============
#TODO : implement cross validation

s_train_set, s_test_set = sentiment_featureset[:50], sentiment_featureset[50:100]

w_train_set, w_test_set = where_featureset[:50], where_featureset[50:100] 

k_train_set, k_test_set = kind_featureset[:50], kind_featureset[50:100] 

    
#============Bayesian classification============


s_range_counts, s_feature_rating_counts, s_features = bayes_classifier_sentiment(s_train_set)
#print s_features 
feature_probabilities = calc_feature_probabilities(s_range_counts, s_feature_rating_counts)

for t in test.iterrows():
    print "\n\n" + t[1][1] + "\n" + str(t[1][2]) + "\n" + str(t[1][3]) + "\n"    #uncomment to print tweets
    tweet_words = t[1][1].split()

    #print "tweet words before preprocessing : " + str(tweet_words)
    for i in range(len(tweet_words)):
        #normalize words to same case
        tweet_words[i] = tweet_words[i].lower()
        #remove hashtag and mention characters from beginning of words
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

    bayes_sentiment = bayes_classify(feature_probabilities, tweet_sentiment_features(tweet_words), s_features)
    print "bayes sentiment = " + str(bayes_sentiment)



#where
#w_bayesian_classifier = nl.NaiveBayesClassifier.train(w_train_set)
#print "when bayesian classifier efficiency = " + str(nl.classify.accuracy(w_bayesian_classifier, w_test_set)) + "\n"
#w_bayesian_classifier.show_most_informative_features(7)

#kind
#k_bayesian_classifier = nl.NaiveBayesClassifier.train(k_train_set)
#print "kind bayesian classifier efficiency = " + str(nl.classify.accuracy(k_bayesian_classifier, k_test_set)) + "\n"
#k_bayesian_classifier.show_most_informative_features(7)


#============Assess results============

#============Result in correct form============

#crossvalidation?

