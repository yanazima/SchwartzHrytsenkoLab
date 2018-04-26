#!/bin/bash


#FILELIST=( $( find /data/yhrytsenko -maxdepth 1 -name "*.pickle" |sort) )
FILELIST=( $( find /Users/yanazima/Desktop/cancerGenomics -maxdepth 1 -name "*.pickle" |sort) )
#seq 10 100 1000 10000 100000 1000000 10000000
#VALUES=( $(seq 10 100 1000 10000 100000 1000000 10000000) )
#VALUESLEN=${#VALUES[@]}
ARRLEN=${#FILELIST[@]}
#echo $ARRLEN
#echo $VALUESLEN



for (( i = 0; i < $((ARRLEN-1)); i++ ))      ### Outer for loop ###
do
    python getFractionOfDiscardedFrequencies.py ${FILELIST[i]} ${VALUES[j]}

  echo "" #### print the new line ###
done
