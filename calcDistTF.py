#!/usr/bin/env python3

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

##################################start processing pickled files###############################


fileName = os.path.basename(sys.argv[1])
fileName2 = os.path.basename(sys.argv[2])
kvalue = os.path.basename(sys.argv[3])

def calcCosDistTF(fileName,fileName2,kvalue):


    pickle_in = open(fileName,"rb")
    matchSeq = pickle.load(pickle_in)


    pickle_in = open(fileName2,"rb")
    matchSeq2 = pickle.load(pickle_in)


    keys_a = set(matchSeq.keys())
    keys_b = set(matchSeq2.keys())

    intersection = keys_a & keys_b


    a = []
    for key in intersection:
        a.append(matchSeq[key])

    b = []
    for key in intersection:
        b.append(matchSeq2[key])


    #a = [10,10,10,100,100,100,1000,1000,10000,100000,1000000,10000000]
    #b = [10,10,10,100,100,100,1000,1000,10000,100000,1000000,10000000]

    '''
    when passed predefined int arrays the distance is 0.0 for %0.10f
    but if gave identical files (larger arrays of ints) there is some difference between two identical files
    if the precision is >7. The np.array_equal(a,b) returns true
    '''

    #print np.array_equal(a,b) ##########checking the equality of two arrays

    z = tf.placeholder(tf.float32, shape=[None], name="input_placeholder_a")
    k = tf.placeholder(tf.float32, shape=[None], name="input_placeholder_b")

    normalize_a = tf.nn.l2_normalize(z,0)
    normalize_b = tf.nn.l2_normalize(k,0)



    cos_similarity=tf.reduce_sum(tf.multiply(normalize_a,normalize_b))
    sess=tf.Session()
    cos_sim=sess.run(cos_similarity,feed_dict={z:a,k:b})



    key = (fileName,fileName2)
    #val = format(1 - cos_sim,'.10f')
    val = format(1-cos_sim,'.10f')

    print ("%s compared to %s is: %s" %(fileName,fileName2,val))

    matchSeq2.clear()
    gc.collect()

    matchSeq.clear()
    gc.collect()

    fileToWrite = "%sMersDistancesResults.txt" % kvalue
    with open(fileToWrite, 'a') as f:
        f.write("%s %s\n" % (key,val))

calcCosDistTF(fileName,fileName2,kvalue)
