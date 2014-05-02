

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

	for f in featuresets:
		#print f

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
		for feature in f[0]:
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

			feature_rating_counts.append([feature, f_range_count])

	#==Calculate features rating probabilities
	#per feature s1-5 per range

	feature_rating_probabilities = []

	for f in feature_rating_counts:
		s1_probs = ["s1", [0,0,0,0,0]];
		s2_probs = ["s2", [0,0,0,0,0]];
		s3_probs = ["s3", [0,0,0,0,0]];
		s4_probs = ["s4", [0,0,0,0,0]];
		s5_probs = ["s5", [0,0,0,0,0]];
		f_probs = [s1_probs, s2_probs, s3_probs, s4_probs, s5_probs]

		f_s1_range_count = f[1][0]
		f_s2_range_count = f[1][1]
		f_s3_range_count = f[1][2]
		f_s4_range_count = f[1][3]
		f_s5_range_count = f[1][4]

		for i in range(0,4):
			for j in range(0,4):
				prob = float(f[1][i][1][j] + (.5*2)) / float(s_range_counts[i][1][j] + 2)
				f_probs[i][1][j] = prob

		feature_rating_probabilities.append([f[0], f_probs])


	return feature_rating_probabilities

		





