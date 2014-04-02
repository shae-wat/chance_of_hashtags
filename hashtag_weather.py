#How to load the data?

import pandas as pds
import numpy as npy
import matplotlib.pyplot as plt


#============Load data============

paths = ['/home/shaelyn/chance_of_hashtags/train.csv', '/home/shaelyn/chance_of_hashtags/test.csv']
t = pds.read_csv(paths[0])
t2 = pds.read_csv(paths[1])
print t #display the data


#============Data in correct form============

#============Run algorithm on data============

#============Assess results============

#============Result in correct form============

#crossvalidation?

