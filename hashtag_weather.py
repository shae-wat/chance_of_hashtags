#How to load the data?

import pandas as pds
import numpy as npy
import matplotlib.pyplot as plt


#============Load data============

paths = ['/home/shaelyn/data_mining/train.csv', '/home/shaelyn/data_mining/test.csv']
t = pds.read_csv(paths[0])
t2 = pds.read_csv(paths[1])
print t2 #display the data


#============Data in correct form============

#============Run algorithm on data============

#============Assess results============

#============Result in correct form============

#crossvalidation?

