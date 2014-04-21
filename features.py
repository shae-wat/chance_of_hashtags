
def tweet_sentiment_features(tweet):
    words = [line.strip().lower() for line in open('sentiment_words.txt')]
 
    features = {}
    #for each sentiment word
    for w in words:
        features['contains(%s)' % w] = (w in tweet)
    return features


#def tweet_location_features(tweet):

#def tweet_kind_features(tweet):
