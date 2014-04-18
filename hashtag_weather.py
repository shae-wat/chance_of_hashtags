#How to load the data?

import pandas as pds
import numpy as npy
#import matplotlib.pyplot as plt
import nltk as nl


#============Load data============

paths = ['/home/shaelyn/chance_of_hashtags/train.csv', '/home/shaelyn/chance_of_hashtags/test.csv']
train = pds.read_csv(paths[0])
#test = pds.read_csv(paths[1])
print train #display the data


#============Data in correct form============

print train.tweet[1]

#============Run algorithm on data============

#============Assess results============

#============Result in correct form============

#crossvalidation?

