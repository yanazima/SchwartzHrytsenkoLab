#!/usr/bin/env python2
import os
import glob
import pickle
from collections import defaultdict



#workingdir = '/Users/yanazima/Desktop/finalKmerProject/'
workingdir ='.'

#Declaration of global variables
startKvalue = 4
kvalue = startKvalue

cosSim = {}
names = []
for name in sorted(glob.glob(workingdir+'/*.fa')):
    names.append(os.path.basename(name))

###############pickle all the .fa files first##################
for i in range(0,len(names),1):
        matchSeq = {}
        fileName = names[i]
        with open(fileName, "r") as f2:
            for linef2 in f2:
                key = linef2.split(" ",1)[0]
                vals = int(linef2.split(" ",1)[1])
                matchSeq[key] = vals
        f2.close()
        picName = "%s_%d.pickle" % (fileName[:9],kvalue)
        print picName
        pickle_out = open(picName,"wb" )
        pickle.dump(matchSeq, pickle_out)
        pickle_out.close()
