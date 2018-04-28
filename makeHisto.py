#!/usr/bin/env python2
import matplotlib
matplotlib.use('Agg')
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

########################creating histograms#######################################
def take(n, iterable):
    return list(islice(iterable, n))
workingdir ='.'
kk = []
pop = []
#z = 0

name = os.path.basename(sys.argv[1])

'''
pickle_in = open(name,"rb")
mydict = pickle.load(pickle_in)
mydictOrdered = collections.OrderedDict(sorted(mydict.items()))
kk = take(len(mydictOrdered), mydictOrdered.iteritems()) #contains the whole dictionary
for i in range(0,len(kk),1):
    b = kk[i][1]
    pop.append(b)
'''
####################################  whithout pickling ################################
with open(name, "r") as f2:
    for linef2 in f2:
        #key = linef2.split(" ",1)[0]
        vals = int(linef2.split(" ",1)[1])
        #matchSeq[key] = vals
        pop.append(vals)
f2.close()



#######################################################################################

plt.xscale('log')#TODO: check how the same graph looks under log and without log
plt.yscale('log')#TODO: check how the same graph looks under log and without log
hist(pop, bins='scott')
histName = "scott_%s.pdf" % os.path.basename(name)[:11]
plt.savefig(histName, bbox_inches='tight')

'''
plt.xscale('log')#TODO: check how the same graph looks under log and without log
#hist(pop, bins='freedman')
#plt.savefig('unsorted_freedman.pdf', bbox_inches='tight')

#hist(pop, bins='blocks')
#plt.savefig('blocks.pdf', bbox_inches='tight')


#hist(pop, bins='knuth')
#plt.savefig('knuth.pdf', bbox_inches='tight')

hist(pop, bins='scott')
plt.savefig('scott.pdf', bbox_inches='tight')
'''

'''

for name in sorted(glob.glob(workingdir+'/*.pickle')):
    #z = z + 1
    pickle_in = open(name,"rb")
    mydict = pickle.load(pickle_in)
    mydictOrdered = collections.OrderedDict(sorted(mydict.items()))
    kk = take(len(mydictOrdered), mydictOrdered.iteritems()) #contains the whole dictionary
    for i in range(0,len(kk),1):
        b = kk[i][1]
        pop.append(b)
    ##########################building individual histograms#########################
    plt.xscale('log')#TODO: check how the same graph looks under log and without log
    hist(pop, bins='scott')
    histName = "scott_%s.pdf" % os.path.basename(name)[:11]
    plt.savefig(histName, bbox_inches='tight')

'''
