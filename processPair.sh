#!/bin/bash


#FILELIST=( $( find /data/yhrytsenko -maxdepth 1 -name "*.pickle" |sort) )
FILELIST=( $( find /Users/yanazima/Desktop/cancerGenomics -maxdepth 1 -name "*.pickle" |sort) )

ARRLEN=${#FILELIST[@]}
echo $ARRLEN



for (( i = 0; i < $((ARRLEN-1)); i++ ))      ### Outer for loop ###
do

    for (( j = i+1; j < $ARRLEN; j++ )) ### Inner for loop ###
    do
        #python3 calcDistTF.py ${FILELIST[i]} ${FILELIST[j]} 4
        python calcDistTF.py ${FILELIST[i]} ${FILELIST[j]} 4
    done

  echo "" #### print the new line ###
done
