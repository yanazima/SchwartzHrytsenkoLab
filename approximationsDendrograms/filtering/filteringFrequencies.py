#!/usr/bin/env python

import tensorflow as tf
import os
import sys
import glob
import math
import pickle
import collections
import gc
import numpy as np
#workingdir = '/Users/yanazima/Desktop/finalKmerProject/'
workingdir ='.'



fileName = os.path.basename(sys.argv[1])
kvalue = os.path.basename(sys.argv[2])
filterValue = os.path.basename(sys.argv[3])

def filterFrequencies(fileName,kvalue,filterValue):
#def calcCosDistTF(fileName,fileName2,kvalue):

    pickle_in = open(fileName,"rb")
    unfilteredDict = pickle.load(pickle_in)

    filteredDict = {}
    for keys in unfilteredDict:
        if (unfilteredDict[keys] > filterValue):
            key = keys
            val = unfilteredDict[keys]
            filteredDict[key] = val

    picName = "%s_%s_>%s.pickle" % (fileName[:9],kvalue,filterValue)
    print picName

    pickle_out = open(picName,"wb" )
    pickle.dump(filteredDict, pickle_out)
    pickle_out.close()

    unfilteredDict.clear()
    gc.collect()


filterFrequencies(fileName,kvalue,filterValue)
