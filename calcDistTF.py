#!/usr/bin/env python3

import tensorflow as tf
import os
import sys
import glob
import math
import pickle
import collections
import gc

#workingdir = '/Users/yanazima/Desktop/finalKmerProject/'
workingdir ='.'

#Declaration of global variables
#startKvalue = 4
#kvalue = startKvalue


##################################start processing pickled files###############################


fileName = os.path.basename(sys.argv[1])
fileName2 = os.path.basename(sys.argv[2])
kvalue = os.path.basename(sys.argv[3])

def calcCosDistTF(fileName,fileName2,kvalue):
    print ("loading first dict")
    pickle_in = open(fileName,"rb")
    matchSeq = pickle.load(pickle_in)
    print ("finished loading first dict")

    print ("loading second dict")
    pickle_in = open(fileName2,"rb")
    matchSeq2 = pickle.load(pickle_in)
    print ("finished loading second dict")

    keys_a = set(matchSeq.keys())
    keys_b = set(matchSeq2.keys())
    print ("turned into sets")

    intersection = keys_a & keys_b
    print ("got their intersection")

    a = []
    for key in intersection:
        a.append(matchSeq[key])

    b = []
    for key in intersection:
        b.append(matchSeq2[key])

    print ("filled up both arrays with the keys")

    z = tf.placeholder(tf.float32, shape=[None], name="input_placeholder_a")
    k = tf.placeholder(tf.float32, shape=[None], name="input_placeholder_b")
    print ("placeholder")

    normalize_a = tf.nn.l2_normalize(z,0)
    normalize_b = tf.nn.l2_normalize(k,0)
    print ("normalized")

    print ("start cosine for %s and %s" % (fileName,fileName2))
    cos_similarity=tf.reduce_sum(tf.multiply(normalize_a,normalize_b))
    sess=tf.Session()
    cos_sim=sess.run(cos_similarity,feed_dict={z:a,k:b})


    print ("finished cosine for %s and %s" % (fileName,fileName2))
    key = (fileName,fileName2)
    val = format(1 - cos_sim,'.10f')

    print ("%s compared to %s is: %0.10f" %(fileName,fileName2,1 - cos_sim))
    print ("start freeing the memory of %s " % fileName2)
    matchSeq2.clear()
    gc.collect()
    print ("finished freeing the memory of %s " % fileName2)
    print ("start freeing the memory of %s " % fileName)
    matchSeq.clear()
    gc.collect()
    print ("finished freeing the memory of %s " % fileName)
    fileToWrite = "%sMersDistancesResults.txt" % kvalue
    with open(fileToWrite, 'a') as f:
        f.write("%s %s\n" % (key,val))

calcCosDistTF(fileName,fileName2,kvalue)
