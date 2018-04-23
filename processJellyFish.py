#!/usr/bin/env python2

import os
import sys
import glob
import subprocess
from subprocess import call
from itertools import izip_longest, izip, product
import math
import pickle
from collections import defaultdict

#workingdir = '/Users/yanazima/Desktop/finalKmerProject/'
workingdir ='.'

#Declaration of global variables
#startKvalue = 12
#kvalue = startKvalue
kvalue = int(sys.argv[1])
names = []
for name in sorted(glob.glob(workingdir+'/*fastq.gz')):
    names.append(os.path.basename(name))

finalSeq = []
for i in range(0,int(len(names)/2),1):
    finalSeq.append('finalSeq%d' % i)

def countFrequencies(names,kvalue):
    fileNameCompared = []
    for i in range(0,len(names),2):
        for n in range(int(i/2),int((i/2)+1),1):
                fileName = names[i]
                fileName2 = names[i+1]
                #fileNameOut = "%s_mer_counts_%s.jf" % (fileName[:10],kvalue) #will contain the results from left and right read together
                fileNameOut = "%s_mer_counts_%s.jf" % (fileName[:11],kvalue) #will contain the results from left and right read together
                subprocess.call("/bin/bash -c \"jellyfish count <(gunzip -c %s) <(gunzip -c %s) -m %d -s 100M -t 28 -C -o %s\"" % (fileName,fileName2, kvalue, fileNameOut), shell=True)

                fileName = fileNameOut
                #fileNameOut = "%s_counts_out_%s.fa" % (fileName[:10],kvalue)
                fileNameOut = "%s_counts_out_%s.fa" % (fileName[:11],kvalue)
                subprocess.call("jellyfish dump %s > %s -c" % (fileName, fileNameOut), shell=True)
    subprocess.call("find . -type f -iname \*.jf -delete", shell=True)

countFrequencies(names,kvalue)
