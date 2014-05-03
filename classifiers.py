#
#SENTIMENT CLASSIFIER
#
def bayes_classifier_sentiment(featuresets):

	# s1 = f[1][0]  #i cant tell
	# s2 = f[1][1]  #negative
	# s3 = f[1][2]  #neutral 
	# s4 = f[1][3]  #positive
	# s5 = f[1][4]  #not related to weather

	s_range0 = (0,0.2)
	s_range1 = (0.2,0.4)
	s_range2 = (0.4,0.6)
	s_range3 = (0.6,0.8)
	s_range4 = (0.8,1.0)

	s1_range_count = ["s1", [0,0,0,0,0]];
	s2_range_count = ["s2", [0,0,0,0,0]];
	s3_range_count = ["s3", [0,0,0,0,0]];
	s4_range_count = ["s4", [0,0,0,0,0]];
	s5_range_count = ["s5", [0,0,0,0,0]];
	s_range_counts = [s1_range_count, s2_range_count, s3_range_count, s4_range_count, s5_range_count]

	feature_rating_counts = []
	features = []    #track all features discovered in training

	for f in featuresets:
		#print f[0]

		#count total number of occurances of s1-s5 ratings per range
		si=0
		for s in f[1]: 
			if (s_range0[0] <= s < s_range0[1]):
				s_range_counts[si][1][0] += 1
			if (s_range1[0] <= s < s_range1[1]):
				s_range_counts[si][1][1] += 1
			if (s_range2[0] <= s < s_range2[1]):
				s_range_counts[si][1][2] += 1
			if (s_range3[0] <= s < s_range3[1]):
				s_range_counts[si][1][3] += 1
			if (s_range4[0] <= s < s_range4[1]):
				s_range_counts[si][1][4] += 1
			si+=1
			

		#counts occurrances that appear per feature per range
		for feature, value in f[0].iteritems():
			#print "feature in f[0] = " + str(feature)
			f_s1_range_count = ["s1", [0,0,0,0,0]];
			f_s2_range_count = ["s2", [0,0,0,0,0]];
			f_s3_range_count = ["s3", [0,0,0,0,0]];
			f_s4_range_count = ["s4", [0,0,0,0,0]];
			f_s5_range_count = ["s5", [0,0,0,0,0]];
			f_range_count = [f_s1_range_count, f_s2_range_count, f_s3_range_count, f_s4_range_count, f_s5_range_count]

			si = 0
			for s in f[1]: 
				if (s_range0[0] <= s < s_range0[1]):
					f_range_count[si][1][0] += 1
				if (s_range1[0] <= s < s_range1[1]):
					f_range_count[si][1][1] += 1
				if (s_range2[0] <= s < s_range2[1]):
					f_range_count[si][1][2] += 1
				if (s_range3[0] <= s < s_range3[1]):
					f_range_count[si][1][3] += 1
				if (s_range4[0] <= s <= s_range4[1]):
					f_range_count[si][1][4] += 1
				si += 1

			feature_rating_counts.append([(feature,value), f_range_count])

			#print feature, value
			if (((feature,value) in features) == False):
				features.append((feature, value))
				# print "features appended ="
				# print (feature, value)

	return s_range_counts, feature_rating_counts, features



#
#WHEN CLASSIFIER
#
def bayes_classifier_when(featuresets):

	w_range0 = (0,0.2)
	w_range1 = (0.2,0.4)
	w_range2 = (0.4,0.6)
	w_range3 = (0.6,0.8)
	w_range4 = (0.8,1.0)

	w1_range_count = ["w1", [0,0,0,0]];
	w2_range_count = ["w2", [0,0,0,0]];
	w3_range_count = ["w3", [0,0,0,0]];
	w4_range_count = ["w4", [0,0,0,0]];
	w_range_counts = [w1_range_count, w2_range_count, w3_range_count, w4_range_count]

	feature_rating_counts = []
	features = []    #track all features discovered in training

	for f in featuresets:
		#print f[0]

		#count total number of occurances of s1-s5 ratings per range
		wi=0
		for w in f[1]: 
			if (w_range0[0] <= w < w_range0[1]):
				w_range_counts[wi][1][0] += 1
			if (w_range1[0] <= w < w_range1[1]):
				w_range_counts[wi][1][1] += 1
			if (w_range2[0] <= w < w_range2[1]):
				w_range_counts[wi][1][2] += 1
			if (w_range3[0] <= w < w_range3[1]):
				w_range_counts[wi][1][3] += 1
			wi+=1
			

		#counts occurrances that appear per feature per range
		for feature, value in f[0].iteritems():
			#print "feature in f[0] = " + str(feature)
			f_w1_range_count = ["w1", [0,0,0,0]];
			f_w2_range_count = ["w2", [0,0,0,0]];
			f_w3_range_count = ["w3", [0,0,0,0]];
			f_w4_range_count = ["w4", [0,0,0,0]];
			f_range_count = [f_w1_range_count, f_w2_range_count, f_w3_range_count, f_w4_range_count]

			wi = 0
			for w in f[1]: 
				if (w_range0[0] <= w < w_range0[1]):
					f_range_count[wi][1][0] += 1
				if (w_range1[0] <= w < w_range1[1]):
					f_range_count[wi][1][1] += 1
				if (w_range2[0] <= w < w_range2[1]):
					f_range_count[wi][1][2] += 1
				if (w_range3[0] <= w < w_range3[1]):
					f_range_count[wi][1][3] += 1
				wi += 1

			feature_rating_counts.append([(feature,value), f_range_count])

			#print feature, value
			if (((feature,value) in features) == False):
				features.append((feature, value))
				# print "features appended ="
				# print (feature, value)

	return w_range_counts, feature_rating_counts, features

def add_feature_counts(feature0, feature1):
	#print "\nfeature0 = " + str(feature0)
	#print "feature1 = " + str(feature1)
	new_feature =  [['s1', [0,0,0,0,0]], ['s2', [0,0,0,0,0]], ['s3', [0,0,0,0,0]], ['s4', [0,0,0,0,0]], ['s5', [0,0,0,0,0]]]
	for i in range(0,4):
		for j in range(0,4):
			count = feature0[1][i][1][j] + feature1[1][i][1][j]
			new_feature[i][1][j] = count
	#print "new_feature = " + str(new_feature)
	return new_feature



def s_calc_feature_probabilities(s_range_counts, feature_rating_counts):

	feature_count_totals = []
	for f_rating_count in feature_rating_counts:
		for f in feature_count_totals:
			if (cmp(f[0],f_rating_count[0]) == 0):
				#print "f[0] = " + str(f[0]) + "\nf_rating_count[0] = " + str(f_rating_count[0]) 
				new_feature_prob = add_feature_counts(f_rating_count, f)
				f_rating_count[1] = new_feature_prob
				#"******f_rating_count[1] = " + str(f_rating_count[1])
				feature_count_totals.remove(f)
		feature_count_totals.append(f_rating_count)
		#print "=====feature_count_totals.append(f_rating_count) = " + str(f_rating_count)


	feature_rating_probabilities = []

	for f_rating in feature_count_totals:
		s1_probs = ["s1", [0,0,0,0,0]]
		s2_probs = ["s2", [0,0,0,0,0]]
		s3_probs = ["s3", [0,0,0,0,0]]
		s4_probs = ["s4", [0,0,0,0,0]]
		s5_probs = ["s5", [0,0,0,0,0]]
		f_probs = [s1_probs, s2_probs, s3_probs, s4_probs, s5_probs]


		for i in range(0,4):
			for j in range(0,4):
				prob = float(f_rating[1][i][1][j] + (.5*2)) / float(s_range_counts[i][1][j] + 2)
				f_probs[i][1][j] = prob

		feature_rating_probabilities.append([f_rating[0], f_probs])
		#print "feature_rating_probabilities appended" 
		#print f_rating[0]
		#print f_probs
		#print "\n"


	return feature_rating_probabilities


def w_calc_feature_probabilities(w_range_counts, feature_rating_counts):

	feature_count_totals = []
	for f_rating_count in feature_rating_counts:
		for f in feature_count_totals:
			if (cmp(f[0],f_rating_count[0]) == 0):
				#print "f[0] = " + str(f[0]) + "\nf_rating_count[0] = " + str(f_rating_count[0]) 
				new_feature_prob = add_feature_counts(f_rating_count, f)
				f_rating_count[1] = new_feature_prob
				#"******f_rating_count[1] = " + str(f_rating_count[1])
				feature_count_totals.remove(f)
		feature_count_totals.append(f_rating_count)
		#print "=====feature_count_totals.append(f_rating_count) = " + str(f_rating_count)


	feature_rating_probabilities = []

	for f_rating in feature_count_totals:
		s1_probs = ["s1", [0,0,0,0]]
		s2_probs = ["s2", [0,0,0,0]]
		s3_probs = ["s3", [0,0,0,0]]
		s4_probs = ["s4", [0,0,0,0]]
		f_probs = [s1_probs, s2_probs, s3_probs, s4_probs]


		for i in range(0,3):
			for j in range(0,3):
				prob = float(f_rating[1][i][1][j] + (.5*2)) / float(w_range_counts[i][1][j] + 2)
				f_probs[i][1][j] = prob

		feature_rating_probabilities.append([f_rating[0], f_probs])
		#print "feature_rating_probabilities appended" 
		#print f_rating[0]
		#print f_probs
		#print "\n"


	return feature_rating_probabilities



def s_bayes_classify(feature_probabilities, test_featureset, features):
	#print "===test_featureset = " + str(test_featureset)
	#print features

	tweet_feature_probabilities = []
	tweet_classificatons = []

	for feature, value in test_featureset.iteritems():
		#print feature, value
		# predict category ratings for this feature
		if (feature,value) in features:
			for f in feature_probabilities:
				if (cmp(f[0],(feature,value)) == 0):
					tweet_feature_probabilities.append(f)

	for feature in tweet_feature_probabilities:
		#print "*feature = " + str(feature)
		s1 = feature[1][0][1].index(max(feature[1][0][1]))
		s1 = (s1+1)*.2
		s2 = feature[1][1][1].index(max(feature[1][1][1]))
		s2 = (s2+1)*.2
		s3 = feature[1][2][1].index(max(feature[1][2][1]))
		s3 = (s3+1)*.2
		s4 = feature[1][3][1].index(max(feature[1][3][1]))
		s4 = (s4+1)*.2
		s5 = feature[1][4][1].index(max(feature[1][4][1]))
		s5 = (s5+1)*.2
		tweet_classificatons.append([s1, s2, s3, s4, s5])

	tweet_s1 = 0
	tweet_s2 = 0
	tweet_s3 = 0
	tweet_s4 = 0
	tweet_s5 = 0	

	for rating in tweet_classificatons:
		if rating[0] > tweet_s1:
			tweet_s1 = rating[0]
		if rating[1] > tweet_s2:
			tweet_s2 = rating[1]
		if rating[2] > tweet_s3:
			tweet_s3 = rating[2]
		if rating[3] > tweet_s4:
			tweet_s4 = rating[3]
		if rating[4] > tweet_s5:
			tweet_s5 = rating[4]

	norm = float(tweet_s1 + tweet_s2 + tweet_s3 + tweet_s4 + tweet_s5)
	tweet_classification = tweet_s1/norm, tweet_s2/norm, tweet_s3/norm, tweet_s4/norm, tweet_s5/norm

	return tweet_classification

def w_bayes_classify(feature_probabilities, test_featureset, features):
	#print "===test_featureset = " + str(test_featureset)
	#print features

	tweet_feature_probabilities = []
	tweet_classificatons = []

	for feature, value in test_featureset.iteritems():
		#print feature, value
		# predict category ratings for this feature
		if (feature,value) in features:
			for f in feature_probabilities:
				if (cmp(f[0],(feature,value)) == 0):
					tweet_feature_probabilities.append(f)

	for feature in tweet_feature_probabilities:
		#print "*feature = " + str(feature)
		w1 = feature[1][0][1].index(max(feature[1][0][1]))
		w1 = (w1+1)*.2
		w2 = feature[1][1][1].index(max(feature[1][1][1]))
		w2 = (w2+1)*.2
		w3 = feature[1][2][1].index(max(feature[1][2][1]))
		w3 = (w3+1)*.2
		w4 = feature[1][3][1].index(max(feature[1][3][1]))
		w4 = (w4+1)*.2
		
		tweet_classificatons.append([w1, w2, w3, w4])

	tweet_w1 = 0
	tweet_w2 = 0
	tweet_w3 = 0
	tweet_w4 = 0	

	for rating in tweet_classificatons:
		if rating[0] > tweet_w1:
			tweet_w1 = rating[0]
		if rating[1] > tweet_w2:
			tweet_w2 = rating[1]
		if rating[2] > tweet_w3:
			tweet_w3 = rating[2]
		if rating[3] > tweet_w4:
			tweet_w4 = rating[3]


	norm = float(tweet_w1 + tweet_w2 + tweet_w3 + tweet_w4)
	tweet_classification = tweet_w1/norm, tweet_w2/norm, tweet_w3/norm, tweet_w4/norm

	return tweet_classification





		





