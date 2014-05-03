#return a dictionary whose keys are features and whose values are true/false

def tweet_sentiment_features(tweet):
	features = {}
	words = [line.strip().lower() for line in open('sentiment_words.txt')]
	#for each sentiment word defined in sentiment_words.txt
	for w in words:
		features['contains(%s)' % w] = (w in tweet)    
	return features


#def tweet_when_features(tweet):

