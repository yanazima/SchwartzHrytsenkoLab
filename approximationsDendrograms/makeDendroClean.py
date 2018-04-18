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


##########################################FOR DENDROGRAM START HERE#############################
def take(n, iterable):
    return list(islice(iterable, n))

kk = []
#pickle_in = open("cosSimK12AllNations.pickle","rb")
pickle_in = open("12MersDistancesResultsGreater1000.pickle","rb")
name = '12MersDistancesResultsGreater1000'
mydict = pickle.load(pickle_in)
mydictOrdered = collections.OrderedDict(sorted(mydict.items()))
#print mydictOrdered

kk = take(len(mydictOrdered), mydictOrdered.iteritems()) #contains the whole dictionary
#print len(kk)



#print kk[0]

all_ppl = []
#j = 0
for i in range(0,len(kk),1):
    a = kk[i][0]
    #print a

    if(a[0] not in all_ppl):
        all_ppl.append(a[0])
        #j = j + 1
        #print a[0]
    if(a[1] not in all_ppl):
        all_ppl.append(a[1])
        #j = j + 1
        #print a[1]

all_ppr = sorted(all_ppl)


#print len(all_ppl)





#assign a key to each person
keyed_ppl = {}
for i in range(0,25,1):
#for i in range(0,5,1):
    key = all_ppl[i]
    val = i
    keyed_ppl[key] = val


#to print out keys and index
for i in sorted(keyed_ppl):
    print str(i) + " " + str(keyed_ppl[i])




ppldictOrdered = collections.OrderedDict(sorted(keyed_ppl.items()))
another = take(len(ppldictOrdered), ppldictOrdered.iteritems())
#for key in ppldictOrdered:
    #print (key, ppldictOrdered[key])
    #print key[:6] + key[23:26], ppldictOrdered[key]


#changing the key of the dictionary
newKeysDictionary = {}
for i in range(0,len(kk),1):
    a = kk[i][0]
    for j in range(0,len(another),1):
        if(a[0]== another[j][0]):
            d = another[j][1]
    for j in range(0,len(another),1):
        if(a[1]== another[j][0]):
            b = another[j][1]
    key = (d,b)
    val = kk[i][1]
    #print val
    newKeysDictionary[key] = val

#print len(newKeysDictionary)


zz = np.asarray([[(newKeysDictionary[(x,y)] if (x,y) in newKeysDictionary else 0) for y in range(0,25)] for x in range(0,25)])
#zz = np.asarray([[(newKeysDictionary[(x,y)] if (x,y) in newKeysDictionary else 0) for y in range(0,5)] for x in range(0,5)])
#print zz #prints a matrix of distances


##############Plotting Dendogram######################
# generate the linkage matrix
X = zz
Z = linkage(X, 'ward')
# calculate full dendrogram
plt.figure(figsize=(25, 10))
plt.title('Hierarchical Clustering Dendrogram for %s' % name)
plt.xlabel('sample index')
plt.ylabel('distance')
#plt.yscale('log')
#plt.yscale('log', linthreshy=0.02)
plt.gca().yaxis.set_minor_formatter(NullFormatter())
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

dendrogram(
    Z,
    leaf_rotation=90.,  # rotates the x axis labels
    leaf_font_size=8.,  # font size for the x axis labels
)
plt.show()
