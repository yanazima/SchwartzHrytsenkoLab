#!/usr/bin/env python2
import matplotlib.pyplot as plt
import pickle
import collections
from itertools import islice
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
from scipy.cluster import hierarchy
from matplotlib.ticker import NullFormatter
import os
import sys
import glob
from astropy.visualization import hist
import operator

##########################################FOR DENDROGRAM START HERE#############################
def take(n, iterable):
    return list(islice(iterable, n))
fileName = os.path.basename(sys.argv[1])
kk = []
#pickle_in = open("cosSimK12AllNations.pickle","rb")
pickle_in = open(fileName,"rb")
#name = '12MersDistancesResultsGreater1000'
mydict = pickle.load(pickle_in)
mydictOrdered = collections.OrderedDict(sorted(mydict.items()))

kk = take(len(mydictOrdered), mydictOrdered.iteritems()) #contains the whole dictionary

for i in range(0,len(kk),1):
    a = kk[i][0]
    firstValKey = a[0]
    secondValKey = a[1]
    newRecordKey = (secondValKey,firstValKey)
    newRecordVal = a = kk[i][1]
    mydict[newRecordKey] = newRecordVal

mydictOrdered = collections.OrderedDict(sorted(mydict.items()))
kk = take(len(mydictOrdered), mydictOrdered.iteritems()) #contains the whole dictionary

sorted_kk = sorted(mydictOrdered.items(), key=operator.itemgetter(1)) #sorts by value lowest to highest

#for i in sorted_kk:
    #print i
#print len(sorted_kk) #600

all_ppl = []
for i in range(0,len(kk),1):
    a = kk[i][0]
    if(a[0] not in all_ppl):
        all_ppl.append(a[0])
    if(a[1] not in all_ppl):
        all_ppl.append(a[1])

all_ppr = sorted(all_ppl)

#assign a key to each person
keyed_ppl = {}
for i in range(0,25,1):
#for i in range(0,5,1):
    key = all_ppl[i]
    val = i
    keyed_ppl[key] = val
keyed_ppl = sorted(keyed_ppl)

#print out key-value pair
#for i in range(0,len(keyed_ppl),1):
    #print str(keyed_ppl[i]) + " " + str(i)
s = []
l = []
for i in range (0,len(keyed_ppl),1):
    l.append(keyed_ppl[i])
    for j in range(0,len(sorted_kk),1):
        n = sorted_kk[j][0]
        n1 = n[0]
        if(keyed_ppl[i] == n1):
            s.append(sorted_kk[j])
            break;

for i in s:
    print i
