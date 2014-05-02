

def bayes_classifier(featureset):

	feature_probabilities = []    #list of tuples [(feature, probability)]

	for feature in featureset:
		print feature

		#sentiment
		if (len(feature[1]) == 5):
			print "yes"

