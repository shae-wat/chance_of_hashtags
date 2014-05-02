

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
		print f

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
			
			print feature
			print f_range_count
			print "\n"

			si = 0
			for s in f[1]: 
				#print "\n" + str(s)

				#count total number of occurances
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

			print feature
			print f_range_count
			print "\n"
			feature_rating_counts.append([feature, f_range_count])
			#print feature_rating_counts





