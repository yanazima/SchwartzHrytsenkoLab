#!/usr/bin/env python2
import matplotlib.pyplot as plt
import pickle
import collections
from itertools import islice
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
from scipy.cluster import hierarchy
from matplotlib.ticker import NullFormatter

def take(n, iterable):
    return list(islice(iterable, n))

afr_afr = []
amr_amr = []
eas_eas = []
eur_eur = []
sas_sas = []

afr_amr = []
afr_eas = []
afr_eur = []
afr_sas = []

amr_eas = []
amr_eur = []
amr_sas = []

eas_eur = []
eas_sas = []

eur_sas = []

kk = []
#pickle_in = open("cosSimK12AllNations.pickle","rb")
pickle_in = open("4MerDistances.pickle","rb")
name = 'cosSimK4AllNations'
mydict = pickle.load(pickle_in)
mydictOrdered = collections.OrderedDict(sorted(mydict.items()))
#print mydictOrdered

kk = take(len(mydictOrdered), mydictOrdered.iteritems()) #contains the whole dictionary
#print kk
#print kk[0]

all_ppl = []

for i in range(0,len(kk),1):
    a = kk[i][0]
    if(a[0] not in all_ppl):
        all_ppl.append(a[0])
    if(a[1] not in all_ppl):
        all_ppl.append(a[1])
'''
for i in range(0,len(kk),1):
    a = kk[i][0]
    all_ppl.append(a)
'''

all_ppr = sorted(all_ppl)
print len(all_ppl)

#assign a key to each person
keyed_ppl = {}
for i in range(0,25,1):
    key = all_ppl[i]
    val = i
    keyed_ppl[key] = val


ppldictOrdered = collections.OrderedDict(sorted(keyed_ppl.items()))
another = take(len(ppldictOrdered), ppldictOrdered.iteritems())
for key in ppldictOrdered:
    #print (key, ppldictOrdered[key])
    print key[:6] + key[23:26], ppldictOrdered[key]


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
    val = kk[i][1] ##########################changed this################val = kk[i][1]######gives similarity instead of a distance
    #print val
    newKeysDictionary[key] = val

#print len(newKeysDictionary)


zz = np.asarray([[(newKeysDictionary[(x,y)] if (x,y) in newKeysDictionary else 0) for y in range(0,25)] for x in range(0,25)])
#print zz

'''
all_pop_unsorted = [afr_afr,amr_amr,eas_eas,eur_eur,sas_sas,afr_amr,afr_eas,
afr_eur,afr_sas,amr_eas,amr_eur,amr_sas,eas_eur,eas_sas,eur_sas]


#populating lists, using 1 - value to get the distance and not the similarity
for i in range(0,len(kk),1):
    a = kk[i][0]
    first_key = a[0][:3]
    second_key = a[1][:3]
    if (first_key == 'AFR' and second_key == 'AFR'):
        afr_afr.append(1-kk[i][1])
    if (first_key == 'AMR' and second_key == 'AMR'):
        amr_amr.append(1-kk[i][1])
    if (first_key == 'EAS' and second_key == 'EAS'):
        eas_eas.append(1-kk[i][1])
    if (first_key == 'EUR' and second_key == 'EUR'):
        eur_eur.append(1-kk[i][1])
    if (first_key == 'SAS' and second_key == 'SAS'):
        sas_sas.append(1-kk[i][1])
    if (first_key == 'AFR' and second_key == 'AMR'):
        afr_amr.append(1-kk[i][1])
    if (first_key == 'AFR' and second_key == 'EAS'):
        afr_eas.append(1-kk[i][1])
    if (first_key == 'AFR' and second_key == 'EUR'):
        afr_eur.append(1-kk[i][1])
    if (first_key == 'AFR' and second_key == 'SAS'):
        afr_sas.append(1-kk[i][1])
    if (first_key == 'AMR' and second_key == 'EAS'):
        amr_eas.append(1-kk[i][1])
    if (first_key == 'AMR' and second_key == 'EUR'):
        amr_eur.append(1-kk[i][1])
    if (first_key == 'AMR' and second_key == 'SAS'):
        amr_sas.append(1-kk[i][1])
    if (first_key == 'EAS' and second_key == 'EUR'):
        eas_eur.append(1-kk[i][1])
    if (first_key == 'EAS' and second_key == 'SAS'):
        eas_sas.append(1-kk[i][1])
    if (first_key == 'EUR' and second_key == 'SAS'):
        eur_sas.append(1-kk[i][1])

#sort each population list and append into a new clean list
all_pop = []
for i in range(0,len(all_pop_unsorted),1):
    pop = all_pop_unsorted[i]
    pop = sorted(pop)
    all_pop.append(pop) #overwriting with sorted lists
'''

'''
##############start clustering###############
X = zz
print X.shape
plt.scatter(X[:,0], X[:,1],c='b')
plt.show()

'''
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




#########################everything below is for the histograms########################################################
'''
lows_highs = []
for i in range(0,len(all_pop),1):
    pop = all_pop[i]
    lows_highs.append(pop[0])
    lows_highs.append(pop[len(pop)-1])

lows_highs = sorted(lows_highs)

low = lows_highs[0]
high = lows_highs[len(lows_highs)-1]

numOfVals = 0
for i in range(0,len(all_pop),1):
    pop = all_pop[i]
    numOfVals = numOfVals + len(pop)

avgNumOfVals = numOfVals/15

someNum = (high - low)/avgNumOfVals

bins = []
def frange(low,high, step=1.0):
    while low < high:
        yield low
        low +=step

for i in frange(low,high + someNum,someNum):
    bins.append(i)

print "here are bin values"
for j in range(0,len(bins),1):
    print "%0.4f" %bins[j]


all_pop_strings = ['afr_afr','amr_amr','eas_eas','eur_eur','sas_sas',
'afr_amr','afr_eas','afr_eur','afr_sas','amr_eas','amr_eur','amr_sas','eas_eur','eas_sas','eur_sas']
'''


'''
for i in range(0,len(all_pop),1):
    pop = all_pop[i]
    plt.title('Comparing CosSim %s 5mers' % all_pop_strings[i])
    plt.hist(pop, bins, histtype = 'bar', rwidth = 0.8)
    plt.savefig('cosSim%s5k.pdf' % all_pop_strings[i], bbox_inches='tight')

'''
