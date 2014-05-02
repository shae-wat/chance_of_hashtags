

def bayes_classifier_sentiment(featuresets):

	feature_probabilities = []    #list of tuples [(feature, probability)]
	s_range_counts = [["s1", [0,0,0,0,0]], ["s2", [0,0,0,0,0]], ["s3", [0,0,0,0,0]], ["s4", [0,0,0,0,0]], ["s5", [0,0,0,0,0]]]


	# n = num instances yj
	s1_r0 = 0
	s1_r1 = 0
	s1_r2 = 0
	s1_r3 = 0
	s1_r4 = 0
	s2_r0 = 0
	s2_r1 = 0
	s2_r2 = 0
	s2_r3 = 0
	s2_r4 = 0
	s3_r0 = 0
	s3_r1 = 0
	s3_r2 = 0
	s3_r3 = 0
	s3_r4 = 0
	s4_r0 = 0
	s4_r1 = 0
	s4_r2 = 0
	s4_r3 = 0
	s4_r4 = 0
	s5_r0 = 0
	s5_r1 = 0
	s5_r2 = 0
	s5_r3 = 0
	s5_r4 = 0

	for f in featuresets:
		print f

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

		si = 0
		for s in f[1]: 
			print "\n" + str(s)
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
			si += 1
			print s_range_counts





	# for f in featuresets:
	# 	#print f
	# 	for feature in f[0]:
	# 		print feature + "\n"


