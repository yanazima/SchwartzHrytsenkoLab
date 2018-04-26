#!/usr/bin/env python2
from __future__ import division
import os
import sys
import glob
import math
import pickle
import collections
import gc

#workingdir = '/Users/yanazima/Desktop/finalKmerProject/'
workingdir ='.'

##################################start processing pickled files###############################


fileName = os.path.basename(sys.argv[1])
#filterValue = os.path.basename(sys.argv[2])

pickle_in = open(fileName,"rb")
matchSeq = pickle.load(pickle_in)

totalNumKmers = 0
filteredNumKmers = 0
filterValue = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
for i in range(0,len(filterValue),1):
    for keys in matchSeq:
        totalNumKmers = totalNumKmers + 1
        if (matchSeq[keys] > int(filterValue[i])):
            filteredNumKmers = filteredNumKmers + 1

    discardedKmers = totalNumKmers - filteredNumKmers
    fractioniscarded = (discardedKmers / totalNumKmers) * 100

    fileToWrite = "%sDiscarded12Mers.txt" %fileName
    greaterSign = "> than"
    with open(fileToWrite, 'a') as f:
        f.write("%s %s %f\n" % (greaterSign,filterValue[i],fractioniscarded))
