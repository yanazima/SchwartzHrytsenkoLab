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

def take(n, iterable):
    return list(islice(iterable, n))
fileName = os.path.basename(sys.argv[1])
kk = []
pickle_in = open(fileName,"rb")
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
#print len(sorted_kk) #600

all_ppl = []
for i in range(0,len(kk),1):
    a = kk[i][0]
    if(a[0] not in all_ppl):
        all_ppl.append(a[0])
    if(a[1] not in all_ppl):
        all_ppl.append(a[1])

all_ppr = sorted(all_ppl)
#print len(all_ppr) #25

#assign a key to each person
keyed_ppl = {}
for i in range(0,25,1):
    key = all_ppl[i]
    val = i
    keyed_ppl[key] = val
keyed_ppl = sorted(keyed_ppl)

s = []
for i in range (0,len(keyed_ppl),1): #get a pair a sample and put it together with another sample which is the shortest to it
    for j in range(0,len(sorted_kk),1):
        n = sorted_kk[j][0]
        n1 = n[0]
        if(keyed_ppl[i] == n1):
            s.append(sorted_kk[j])
            break;

#d containes pairs of closest neighbors for each sample
d = {}
for i in range(0,len(s),1):
    key = s[i][0]
    val = s[i][1]
    d[key] = val


sorted_d_low_values = sorted(d.items(), key=operator.itemgetter(1)) #sorts by value lowest to highest
#for i in sorted_d_low_values:
    #print i

#below containes indecies of the samples
#for i in range(0,len(keyed_ppl),1):
    #print str(keyed_ppl[i]) + " " + str(i)
X=[] #contins left sample in the tuple
Y=[] #containes right sample in the tuple

for i in range(0,len(s),1):
    a = s[i][0]
    X.append(a[0])
    Y.append(a[1])

X_keyed = [] #maps each left sample in the tuple to the index of the neighboring sample in the list
Y_keyed = [] #maps each right sample in the tuple to the index of the neighboring sample in the list

for i in range(0,len(X),1):
    for j in range(i,len(keyed_ppl),1):
        if(X[i] == keyed_ppl[j]):
            X_keyed.append(j)

for i in range(0,len(Y),1):
    for j in range(0,len(keyed_ppl),1):
        if(Y[i] == keyed_ppl[j]):
            Y_keyed.append(j)


plt.grid()
plt.plot(X_keyed, Y_keyed, 'o')
plt.xlim(0,24) #x-vlues
plt.ylim(0,24) #y-values

plt.xticks(X_keyed)
plt.yticks(X_keyed)
plt.title('Closest Neighbor for unfiltered 12mers')
plt.show()
exit()
