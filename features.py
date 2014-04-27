
#return a dictionary whose keys are features
#an whose values are true/false
def tweet_sentiment_features(tweet):
    words = [line.strip().lower() for line in open('sentiment_words.txt')]
 
    features = {}
    #for each sentiment word defined in sentiment_words.txt
    for w in words:
        features['contains(%s)' % w] = (w in tweet)
        
        #TODO
        
        #remove hashtags
        #correct mispellings, missing spaces
        #check context of found words
        #interpret punctuation
        
        
        
        
    return features


#def tweet_location_features(tweet):

#def tweet_kind_features(tweet):
