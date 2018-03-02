#!/usr/bin/env python3

import tensorflow as tf
import os
import sys
import glob
import math
import pickle
import collections

fileName = "14MersDistancesResults.txt"
matchSeq = {}
with open(fileName, "r") as f2:
      for linef2 in f2:
          names = linef2.rstrip('\n').split(")",1)[0]
          name1 = names[2:13]
          name2 = names[24:35]
          key = (name1,name2)
          vals = linef2.rstrip('\n').split(")",1)[1]
          matchSeq[key] = vals
f2.close()
matchSeq2 = collections.OrderedDict(sorted(matchSeq.items()))
for i in matchSeq2:
    print i


print ("strated pickling")
pickle_out = open("14MerDistances.pickle","wb")
pickle.dump(matchSeq2, pickle_out)
pickle_out.close()

'''
print len(matchSeq2)
#mydictOrdered = collections.OrderedDict(sorted(matchSeq.items()))
for i in matchSeq2:
    print i
'''

