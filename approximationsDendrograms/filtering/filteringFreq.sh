#!/bin/bash


#FILELIST=( $( find /data/yhrytsenko -maxdepth 1 -name "*.pickle" |sort) )
FILELIST=( $( find /Users/yanazima/Desktop/cancerGenomics/approximationsDendrograms/filtering -maxdepth 1 -name "*.pickle" |sort) )

ARRLEN=${#FILELIST[@]}
echo $ARRLEN



for (( i = 0; i < $ARRLEN; i++ ))      ### Outer for loop ###
do
        #python3 calcDistTF.py ${FILELIST[i]} ${FILELIST[j]} 4
        python filteringFrequencies.py ${FILELIST[i]} 12 100000

  echo "" #### print the new line ###
done
