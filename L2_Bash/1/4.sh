#!/bin/bash

while getopts "f:c:" man ; do
case "$man" in
    c) result=$( echo "man = $man"; echo "OPTARG = $OPTARG"; echo "scale=2; ($OPTARG * (9/5)) + 32" | bc );;
    f) result=$( echo "man = $man"; echo "OPTARG = $OPTARG"; echo "scale=2; ($OPTARG - 32) * (5/9)" | bc );;
    \?) result= echo "please enter something";;
esac
done
echo $result


#Temperature converter script using while.
# We cannot change $OPTARG but we can change variable name. 
