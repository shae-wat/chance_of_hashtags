#return a dictionary whose keys are features and whose values are true/false

def tweet_sentiment_features(tweet):
	features = {}
	words = [line.strip().lower() for line in open('sentiment_words.txt')]
	#for each sentiment word defined in sentiment_words.txt
	#print "tweet" + str(tweet)
	for i, word in enumerate(tweet):
		if (word in words and tweet[i-1]!="not") :
			features['contains(%s)' % word] = (word in words)
			#print "contains "+ word + " = " + str(word in words)
	return features


#def tweet_when_features(tweet):

